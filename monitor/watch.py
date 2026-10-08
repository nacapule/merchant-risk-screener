"""Replay daily monitoring facts; later events cannot rewrite an earlier episode."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yaml

from monitor.metrics import compute_metrics
from monitor.rollup import (
    REPO,
    ReconciliationError,
    build_spine,
    clip_shipments,
    counts_at,
    day,
    event_totals,
    export_events,
    export_shipments,
    load_events,
    load_shipments,
    reconcile,
    reconcile_shipments,
    shipment_counts_at,
)
from monitor.rules import (
    ALL_SETS,
    ITERATION2_FIELDS,
    RULE_SETS,
    describe,
    needs_delivery,
    predicates,
)


def json_value(value: Any) -> Any:
    """Missing metrics serialize as null, while counts and booleans retain their types."""
    if pd.isna(value):
        return None
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and not np.isfinite(value):
        raise ValueError("non-finite monitoring metric")
    return value


def evaluate(spine_metrics: pd.DataFrame, cfg: dict, rule_set: str,
             start: str | None = None) -> dict[str, list[dict]]:
    """Core alerts and dispute flags each re-arm after their own suppression period.

    Replay state before an optional output start, so changing a reporting window
    never creates an episode that would have been suppressed by earlier history.
    A delivery-confirmation firing inside an open case not opened by one escalates
    it once; the escalation is a review but does not restart the suppression period.
    """
    result: dict[str, list[dict]] = {"alerts": [], "escalations": [], "dispute_count_flags": []}
    if spine_metrics.empty:
        return result
    g = spine_metrics.sort_values(["merchant_id", "d"]).reset_index(drop=True)
    p = predicates(g, cfg, rule_set)
    suppression = cfg["monitor"]["episode_suppression_days"]
    first_output = day(start) if start else None
    hidden = {"merchant_id", "d", *(ITERATION2_FIELDS if rule_set in RULE_SETS else ())}

    def record(index: int, codes: list[str]) -> dict:
        row = g.loc[index]
        metrics = {key: json_value(value) for key, value in row.items() if key not in hidden}
        return {"merchant_id": int(row.merchant_id), "date": str(row.d.date()),
                "trigger_codes": codes, "triggers": describe(metrics, codes, cfg, rule_set),
                "metrics": metrics}

    for signal, target in [("core", "alerts"), ("D", "dispute_count_flags")]:
        last: dict[int, pd.Timestamp] = {}
        escalated: set[int] = set()
        for index in p.index[p[signal]]:
            mid, date = int(g.at[index, "merchant_id"]), g.at[index, "d"]
            visible = first_output is None or date >= first_output
            if mid in last and (date - last[mid]).days <= suppression:
                if signal == "core" and p.at[index, "X"] and mid not in escalated:
                    escalated.add(mid)
                    if visible:
                        result["escalations"].append(
                            {**record(index, ["X"]), "case_opened": str(last[mid].date())})
                continue
            last[mid] = date
            escalated.discard(mid)
            if signal == "core" and p.at[index, "X"]:
                escalated.add(mid)
            if not visible:
                continue
            codes = (["D"] if signal == "D" else
                     [code for code in ("W", "B", "V", "T", "S", "Y", "F", "X")
                      if p.at[index, code]])
            result[target].append(record(index, codes))
    for alerts in result.values():
        alerts.sort(key=lambda alert: (alert["date"], alert["merchant_id"]))
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", type=Path)
    ap.add_argument("--as-of")
    ap.add_argument("--rules", choices=ALL_SETS)
    ap.add_argument("--export-events", type=Path)
    ap.add_argument("--shipments", type=Path)
    ap.add_argument("--export-shipments", type=Path)
    ap.add_argument("--calibration", type=Path)
    ap.add_argument("--out", type=Path, default=REPO / "reports/monitoring_alerts.json")
    args = ap.parse_args()
    cfg = yaml.safe_load((REPO / "config.yaml").read_text())
    rule_set = args.rules or cfg["monitor"]["rule_set"]
    try:
        events = load_events(args.events)
        as_of = day(args.as_of or events.attrs["meta"]["as_of"])
        if args.events and as_of > day(events.attrs["meta"]["as_of"]):
            raise ValueError("as_of cannot exceed the event export's observation date")
        if args.events and event_totals(events) != events.attrs["meta"]["counts"]:
            raise ReconciliationError(f"event totals {event_totals(events)} != source totals "
                                      f"{events.attrs['meta']['counts']}")
        clipped = events.loc[events.d <= as_of].copy()
        spine = build_spine(clipped, as_of)
        counts = reconcile(spine, clipped, counts_at(events, as_of))
        shipments = calibration = None
        if needs_delivery(rule_set) or args.export_shipments:
            if args.events and not args.shipments:
                raise ValueError("delivery confirmation from file exports needs --shipments")
            shipments = load_shipments(args.shipments)
            if args.shipments and as_of > day(shipments.attrs["meta"]["as_of"]):
                raise ValueError("as_of cannot exceed the shipment export's observation date")
            if args.shipments:
                reconcile_shipments(shipments, shipments.attrs["meta"]["counts"])
            counts["shipments"] = reconcile_shipments(
                clip_shipments(shipments, as_of), shipment_counts_at(shipments, as_of))
        if needs_delivery(rule_set):
            path = args.calibration or REPO / cfg["monitor"]["delivery"]["calibration"]
            calibration = json.loads(path.read_text())
        metrics = compute_metrics(spine, cfg, shipments, calibration)
        output = evaluate(metrics, cfg, rule_set)
        output["meta"] = {"rule_set": rule_set, "as_of": str(as_of.date()),
                          "source": events.attrs["meta"]["source"],
                          "parameters": cfg["monitor"], "counts": counts,
                          "money_unit": "cents"}
        if calibration is not None:
            output["meta"]["calibration"] = calibration
            output["meta"]["shipments_source"] = shipments.attrs["meta"]["source"]
        if args.export_events:
            export_events(args.export_events, events, as_of)
        if args.export_shipments:
            export_shipments(args.export_shipments, shipments, as_of)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, indent=1, allow_nan=False))
    except (ReconciliationError, ValueError) as exc:
        ap.exit(2, f"monitor: {exc}\n")
    print(f"{len(output['alerts'])} merchant alerts, {len(output['escalations'])} escalations "
          f"-> {args.out}")
    for alert in sorted(output["alerts"] + output["escalations"],
                        key=lambda a: (a["date"], a["merchant_id"])):
        kind = "escalation" if "case_opened" in alert else "alert"
        print(f"  merchant {alert['merchant_id']} {kind} on {alert['date']}: "
              + "; ".join(alert["triggers"]))


if __name__ == "__main__":
    main()
