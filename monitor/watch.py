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
    counts_at,
    day,
    export_events,
    load_events,
    reconcile,
)
from monitor.rules import RULE_SETS, describe, predicates


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
    """
    result: dict[str, list[dict]] = {"alerts": [], "dispute_count_flags": []}
    if spine_metrics.empty:
        return result
    g = spine_metrics.sort_values(["merchant_id", "d"]).reset_index(drop=True)
    p = predicates(g, cfg, rule_set)
    suppression = cfg["monitor"]["episode_suppression_days"]
    first_output = day(start) if start else None
    for signal, target in [("core", "alerts"), ("D", "dispute_count_flags")]:
        last: dict[int, pd.Timestamp] = {}
        for index in p.index[p[signal]]:
            row = g.loc[index]
            mid, date = int(row.merchant_id), row.d
            if mid in last and (date - last[mid]).days <= suppression:
                continue
            last[mid] = date
            if first_output is not None and date < first_output:
                continue
            codes = (["D"] if signal == "D" else
                     [code for code in ("W", "B", "V", "T", "S", "Y", "F") if p.at[index, code]])
            metrics = {key: json_value(value) for key, value in row.items()
                       if key not in ("merchant_id", "d")}
            result[target].append({"merchant_id": mid, "date": str(date.date()),
                                   "trigger_codes": codes,
                                   "triggers": describe(metrics, codes, cfg, rule_set),
                                   "metrics": metrics})
        result[target].sort(key=lambda alert: (alert["date"], alert["merchant_id"]))
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", type=Path)
    ap.add_argument("--as-of")
    ap.add_argument("--rules", choices=RULE_SETS)
    ap.add_argument("--export-events", type=Path)
    ap.add_argument("--out", type=Path, default=REPO / "reports/monitoring_alerts.json")
    args = ap.parse_args()
    cfg = yaml.safe_load((REPO / "config.yaml").read_text())
    rule_set = args.rules or cfg["monitor"]["rule_set"]
    try:
        events = load_events(args.events)
        as_of = day(args.as_of or events.attrs["meta"]["as_of"])
        if args.events and as_of > day(events.attrs["meta"]["as_of"]):
            raise ValueError("as_of cannot exceed the event export's observation date")
        clipped = events.loc[events.d <= as_of].copy()
        spine = build_spine(clipped, as_of)
        counts = reconcile(spine, clipped, counts_at(events, as_of))
        metrics = compute_metrics(spine, cfg)
        output = evaluate(metrics, cfg, rule_set)
        output["meta"] = {"rule_set": rule_set, "as_of": str(as_of.date()),
                          "source": events.attrs["meta"]["source"],
                          "parameters": cfg["monitor"], "counts": counts,
                          "money_unit": "cents"}
        if args.export_events:
            export_events(args.export_events, events, as_of)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(output, indent=1, allow_nan=False))
    except (ReconciliationError, ValueError) as exc:
        ap.exit(2, f"monitor: {exc}\n")
    print(f"{len(output['alerts'])} merchant alerts -> {args.out}")
    for alert in output["alerts"]:
        print(f"  merchant {alert['merchant_id']} on {alert['date']}: "
              + "; ".join(alert["triggers"]))


if __name__ == "__main__":
    main()
