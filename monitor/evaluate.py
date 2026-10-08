"""Keep outcome facts outside the monitor and enforce a dev-only selection boundary."""

from __future__ import annotations

import argparse
import copy
import gzip
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from scipy.stats import beta

from monitor.metrics import compute_metrics
from monitor.rollup import (
    REPO,
    build_spine,
    clip_shipments,
    counts_at,
    day,
    db_url,
    event_totals,
    load_events,
    load_shipments,
    reconcile,
    reconcile_shipments,
    shipment_counts_at,
    source_info,
)
from monitor.rules import ALL_SETS, RULE_SETS, needs_delivery, predicates
from monitor.watch import evaluate

DEV_START = pd.Timestamp("2024-01-01")
DEV_AS_OF = pd.Timestamp("2024-10-31")
DEV_END = pd.Timestamp("2024-11-01")
OPERATING_END = pd.Timestamp("2025-09-01")
FOLLOWUP_END = pd.Timestamp("2025-12-30")
WORLD_PATH = REPO / "monitor/eval/world_416-baseline.json"
ADDED_PREDICATES = {"c0": 0, "c1a": 1, "c1b": 1, "c1c": 1, "c2": 1, "c3": 2}


def read_world(path: Path = WORLD_PATH) -> dict:
    return json.loads(path.read_text())


LABEL_COLUMNS = ["merchant_id", "d", "reason", "basis"]


def export_dispute_labels(path: Path, url: str | None = None) -> pd.DataFrame:
    """Adjudicated bases describe non-bust-out cases after the fact; the monitor never sees them."""
    import sqlalchemy as sa

    url = url or db_url()
    engine = sa.create_engine(url)
    try:
        with engine.connect() as conn:
            labels = pd.read_sql(sa.text((REPO / "monitor/eval/dispute_labels.sql").read_text()),
                                 conn)[LABEL_COLUMNS]
    finally:
        engine.dispose()
    labels["d"] = pd.to_datetime(labels["d"]).dt.normalize()
    csv = labels.to_csv(index=False, date_format="%Y-%m-%d", lineterminator="\n")
    with path.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(csv.encode("utf-8"))
    meta = {"rows": len(labels), "source": source_info(url),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    Path(f"{path}.meta.json").write_text(json.dumps(meta, indent=1, sort_keys=True))
    return labels


def load_dispute_labels(path: Path) -> pd.DataFrame:
    meta = json.loads(Path(f"{path}.meta.json").read_text())
    if hashlib.sha256(path.read_bytes()).hexdigest() != meta["sha256"]:
        raise ValueError(f"dispute label export SHA-256 mismatch: {path}")
    labels = pd.read_csv(path, parse_dates=["d"])
    if len(labels) != meta["rows"]:
        raise ValueError(f"dispute label export has {len(labels)} rows, sidecar {meta['rows']}")
    return labels


def workload(metrics: pd.DataFrame, alerts: list[dict], bustout_ids: set[int],
             start: pd.Timestamp, end: pd.Timestamp, cfg: dict) -> dict:
    """Count exposure on eligible days outside days 1..90 after a core episode.

    Episodes before a reporting window still suppress exposure inside that window.
    The episode day itself remains exposed because it was not yet suppressed.
    """
    non = metrics.loc[~metrics.merchant_id.isin(bustout_ids)]
    suppressed = pd.Series(False, index=non.index)
    days = cfg["monitor"]["episode_suppression_days"]
    for alert in alerts:
        if alert["merchant_id"] in bustout_ids:
            continue
        date = day(alert["date"])
        suppressed |= (non.merchant_id.eq(alert["merchant_id"]) & non.d.gt(date)
                       & non.d.le(date + pd.Timedelta(days=days)))
    eligible = non.eligible & non.d.ge(start) & non.d.lt(end)
    exposure_days = int((eligible & ~suppressed).sum())
    quarters = exposure_days / cfg["monitor"]["merchant_quarter_days"]
    episodes = [a for a in alerts if a["merchant_id"] not in bustout_ids
                and start <= day(a["date"]) < end]
    return {"episodes": len(episodes), "eligible_merchant_days": int(eligible.sum()),
            "suppressed_eligible_days": int((eligible & suppressed).sum()),
            "exposure_days": exposure_days, "eligible_merchant_quarters": quarters,
            "eligible_merchants": int(non.loc[eligible, "merchant_id"].nunique()),
            "episodes_per_100_eligible_merchant_quarters": (
                100 * len(episodes) / quarters if quarters > 0 else None),
            "non_bustout_alerts_with_at_least_3_disputes": sum(
                a["metrics"]["disputes_30d"] >= cfg["monitor"]["min_disputes"] for a in episodes)}


def detections(events: pd.DataFrame, replay: dict, cohort: list[dict]) -> dict:
    """A core episode must precede the calendar closure date to count as caught."""
    rows, late = [], []
    for merchant in cohort:
        mid, closure = merchant["merchant_id"], day(merchant["closed_at"])
        core = [a for a in replay["alerts"] if a["merchant_id"] == mid]
        first = day(core[0]["date"]) if core else None
        g = events.loc[events.merchant_id.eq(mid)]
        total_gmv = int(g.gmv_cents.sum())
        after_gmv = int(g.loc[g.d.gt(first), "gmv_cents"].sum()) if first is not None else None
        caught = first is not None and first < closure
        rows.append({"merchant_id": mid, "onboarded_at": merchant["onboarded_at"],
                     "closed_at": merchant["closed_at"],
                     "first_core_alert": str(first.date()) if first is not None else None,
                     "caught_before_closure": caught,
                     "lead_days": int((closure - first).days) if caught else None,
                     "approved_gmv_cents": total_gmv, "gmv_after_alert_cents": after_gmv,
                     "exposure_after_alert_share": (after_gmv / total_gmv
                                                    if first is not None and total_gmv else None)})
        for kind, key in [("core_alert", "alerts"), ("D_flag", "dispute_count_flags")]:
            for alert in replay[key]:
                if (alert["merchant_id"] == mid
                        and (kind == "D_flag" or day(alert["date"]) >= closure)):
                    late.append({"merchant_id": mid, "kind": kind, "date": alert["date"],
                                 "days_after_closure": int((day(alert["date"]) - closure).days),
                                 "before_closure": day(alert["date"]) < closure,
                                 "trigger_codes": alert["trigger_codes"]})
    return {"n_bustouts": len(rows), "caught_before_closure": sum(
                row["caught_before_closure"] for row in rows),
            "merchants": rows, "late_detections": late}


def _dev_candidate(events: pd.DataFrame, metrics: pd.DataFrame, cfg: dict,
                   rule_set: str, world: dict) -> dict:
    # Check at the last boundary before replay, even when callers bypass the CLI.
    if (events.d.gt(DEV_AS_OF).any() or metrics.d.gt(DEV_AS_OF).any()):
        raise ValueError("selection refuses data after 2024-10-31")
    cohort = [b for b in world["bustouts"] if day(b["closed_at"]) < DEV_END]
    replay = evaluate(metrics, cfg, rule_set)
    detection = detections(events, replay, cohort)
    load = workload(metrics, replay["alerts"], {b["merchant_id"] for b in cohort},
                    metrics.d.min(), DEV_END, cfg)
    rate = load["episodes_per_100_eligible_merchant_quarters"]
    return {"rule_set": rule_set, "detections": detection, "non_bustout_workload": load,
            "feasible": rate is not None and rate <= cfg["monitor"]["selection_workload_max"],
            "added_predicates": ADDED_PREDICATES[rule_set],
            "core_episodes": len(replay["alerts"])}


def _rank(candidate: dict) -> tuple:
    rate = candidate["non_bustout_workload"]["episodes_per_100_eligible_merchant_quarters"]
    return (not candidate["feasible"], -candidate["detections"]["caught_before_closure"],
            rate if rate is not None else float("inf"), candidate["added_predicates"],
            candidate["rule_set"])


def select_dev(events: pd.DataFrame, cfg: dict, world: dict) -> dict:
    """Accept only truncated events; direct callers cannot accidentally tune on later days."""
    if events.d.gt(DEV_AS_OF).any():
        raise ValueError("selection refuses data after 2024-10-31; truncate before selection")
    assert not events.d.gt(DEV_AS_OF).any()
    cfg = copy.deepcopy(cfg)
    spine = build_spine(events, DEV_AS_OF)
    metrics = compute_metrics(spine, cfg)
    candidates = [_dev_candidate(events, metrics, cfg, name, world) for name in RULE_SETS[:-1]]
    best_young = min((c for c in candidates if c["rule_set"] in ("c1a", "c1b", "c1c")),
                     key=_rank)["rule_set"]
    cfg["monitor"]["c3_young"] = best_young
    candidates.append(_dev_candidate(events, metrics, cfg, "c3", world))
    ranking = sorted(candidates, key=_rank)
    feasible = [c for c in ranking if c["feasible"]]
    selected = feasible[0]["rule_set"] if candidates[0]["feasible"] and feasible else None
    return {"as_of": str(DEV_AS_OF.date()), "candidates": candidates,
            "ranking": [c["rule_set"] for c in ranking], "selected_rule_set": selected,
            "ship_rule_set": selected or "c0", "c3_young": best_young,
            "parameters": cfg["monitor"], "source": events.attrs.get("meta", {}).get("source"),
            "provenance": {key: value for key, value in world.items()
                           if key not in ("bustouts", "protocol_windows",
                                          "protocol_freezes", "horizon")},
            "selection_reason": ("ranked feasible candidates" if selected else
                                 "c0 infeasible or no feasible candidate; c0 ships")}


def calibrate(shipments: pd.DataFrame, cfg: dict, world_name: str) -> dict:
    """Fix the delivery deadline and reference rate from early shipments only, without labels."""
    d = cfg["monitor"]["delivery"]
    known_by, shipped_by = day(d["calibration_known_by"]), day(d["calibration_shipped_by"])
    if shipments.shipped_d.gt(known_by).any() or shipments.confirmed_d.gt(known_by).any():
        raise ValueError(f"calibration refuses data after {known_by.date()}")
    timed = shipments.loc[shipments.shipped_d.le(shipped_by) & shipments.confirmed_d.notna()]
    lags = np.sort((timed.confirmed_d - timed.shipped_d).dt.days.to_numpy())
    if not len(lags):
        raise ValueError("no confirmed shipments to calibrate the deadline")
    # The smallest whole day t with at least the quantile share of lags <= t.
    deadline = max(int(lags[int(np.ceil(d["deadline_quantile"] * len(lags))) - 1]), 0)
    reference = shipments.loc[shipments.shipped_d.le(known_by - pd.Timedelta(days=deadline))]
    late = reference.confirmed_d.isna() | reference.confirmed_d.gt(
        reference.shipped_d + pd.Timedelta(days=deadline))
    x, n = int(late.sum()), len(reference)
    if not n:
        raise ValueError("no shipments reached the deadline before the calibration cutoff")
    upper = 1.0 if x == n else float(beta.ppf(d["reference_upper_confidence"], x + 1, n - x))
    meta = shipments.attrs.get("meta", {})
    return {"world": world_name, "deadline_days": deadline, "p_ref": upper,
            "lag_shipments": len(lags), "reference_shipments": n, "reference_unconfirmed": x,
            "reference_observed_share": x / n, "deadline_quantile": d["deadline_quantile"],
            "reference_upper_confidence": d["reference_upper_confidence"],
            "calibration_shipped_by": str(shipped_by.date()),
            "calibration_known_by": str(known_by.date()),
            "source": meta.get("source"), "export_as_of": meta.get("as_of")}


def load_calibration(cfg: dict, path: Path | None = None) -> dict:
    return json.loads((path or REPO / cfg["monitor"]["delivery"]["calibration"]).read_text())


def review_load(metrics: pd.DataFrame, replay: dict, bustout_ids: set[int],
                start: pd.Timestamp, end: pd.Timestamp, cfg: dict) -> dict:
    """Case openings and escalations are both reviews; X reviews also have their own ceiling."""
    load = workload(metrics, replay["alerts"], bustout_ids, start, end, cfg)
    inside = [[a for a in replay[key] if a["merchant_id"] not in bustout_ids
               and start <= day(a["date"]) < end] for key in ("alerts", "escalations")]
    openings, escalations = inside
    delivery = sum("X" in a["trigger_codes"] for a in openings) + len(escalations)
    quarters = load["eligible_merchant_quarters"]

    def per_100(n: int) -> float | None:
        return 100 * n / quarters if quarters > 0 else None

    non = metrics.loc[~metrics.merchant_id.isin(bustout_ids)]
    total = int((non.eligible & non.d.ge(start) & non.d.lt(end)).sum())
    return {**load, "case_openings": len(openings), "escalations": len(escalations),
            "reviews": len(openings) + len(escalations), "delivery_reviews": delivery,
            "review_load": per_100(len(openings) + len(escalations)),
            "delivery_review_load": per_100(delivery),
            "total_eligible_merchant_quarters": total / cfg["monitor"]["merchant_quarter_days"]}


def arm_firsts(metrics: pd.DataFrame, cfg: dict, rule_set: str, cohort: list[dict]) -> dict:
    """Each arm's first eligible firing, regardless of case suppression."""
    p = predicates(metrics, cfg, rule_set)
    arms = {"control": p.control, "Y": p.Y, "X": p.X}
    result = {}
    for merchant in cohort:
        mid, closure = merchant["merchant_id"], day(merchant["closed_at"])
        mine = metrics.merchant_id.eq(mid) & metrics.eligible
        row = {}
        for arm, fired in arms.items():
            days = metrics.loc[mine & fired, "d"]
            first = days.min() if len(days) else None
            row[arm] = None if first is None else {
                "date": str(first.date()), "days_before_closure": int((closure - first).days),
                "before_closure": bool(first < closure)}
        result[str(mid)] = row
    return result


def adopt(candidates: dict, cfg: dict) -> str | None:
    """The first registered set within the review ceiling and, with X, the delivery ceiling."""
    m = cfg["monitor"]
    for name in m["ladder"]:
        load = candidates[name]["review_load"]
        ok = load["review_load"] is not None and load["review_load"] <= m["selection_workload_max"]
        if needs_delivery(name):
            rate = load["delivery_review_load"]
            ok = ok and rate is not None and rate <= m["delivery_review_max"]
        if ok:
            return name
    return None


def gate_dev(events: pd.DataFrame, shipments: pd.DataFrame, cfg: dict, world: dict,
             calibration: dict) -> dict:
    """Apply the registered ladder to dev data only; bust-out detection does not rank sets."""
    if events.d.gt(DEV_AS_OF).any() or shipments.shipped_d.gt(DEV_AS_OF).any() \
            or shipments.confirmed_d.gt(DEV_AS_OF).any():
        raise ValueError("the gate refuses data after 2024-10-31")
    spine = build_spine(events, DEV_AS_OF)
    metrics = compute_metrics(spine, cfg, shipments, calibration)
    cohort = [b for b in world["bustouts"] if day(b["closed_at"]) < DEV_END]
    ids = {b["merchant_id"] for b in cohort}
    names = [*cfg["monitor"]["ladder"], "k1", "k2", "x", "c0"]
    sets = {}
    for name in names:
        replay = evaluate(metrics, cfg, name)
        sets[name] = {"review_load": review_load(metrics, replay, ids, DEV_START, DEV_END, cfg),
                      "detections": detections(events, replay, cohort),
                      "arm_first_firings": arm_firsts(metrics, cfg, name, cohort),
                      "escalations": len(replay["escalations"]),
                      "core_episodes": len(replay["alerts"])}
    adopted = adopt(sets, cfg)
    return {"as_of": str(DEV_AS_OF.date()), "ladder": cfg["monitor"]["ladder"],
            "adopted_rule_set": adopted, "ship_rule_set": adopted or "c0",
            "reason": ("first registered set within both ceilings" if adopted else
                       "no capacity-feasible replacement adopted; c0 stays as the reference"),
            "calibration": calibration, "sets": sets, "parameters": cfg["monitor"],
            "source": {"events": events.attrs.get("meta", {}).get("source"),
                       "shipments": shipments.attrs.get("meta", {}).get("source")}}


KEYS = ("alerts", "escalations", "dispute_count_flags")


def prefix_checks(events: pd.DataFrame, shipments: pd.DataFrame | None,
                  calibration: dict | None, replays: dict[str, dict], cfg: dict,
                  world: dict, as_of: pd.Timestamp) -> dict[str, dict]:
    """Replay each freeze cutoff once; metrics do not depend on the rule set."""
    checks: dict[str, dict] = {name: {} for name in replays}
    for name, freeze in world["protocol_freezes"].items():
        cutoff = day(freeze) - pd.Timedelta(days=1)
        if cutoff > as_of:
            continue
        clipped = events.loc[events.d.le(cutoff)].copy()
        ships = None if shipments is None else clip_shipments(shipments, cutoff)
        metrics = compute_metrics(build_spine(clipped, cutoff), cfg, ships, calibration)
        for rule_set, full in replays.items():
            replay = evaluate(metrics, cfg, rule_set)
            expected = {key: [a for a in full[key] if day(a["date"]) <= cutoff] for key in KEYS}
            if replay != expected:
                raise ValueError(f"prefix invariance failed for {rule_set} at {cutoff.date()}")
            checks[rule_set][name] = {"as_of": str(cutoff.date()), "passed": True,
                                      **{key: len(replay[key]) for key in KEYS}}
    return checks


def remaining_exposure(arms: dict, events: pd.DataFrame,
                       shipments: pd.DataFrame | None) -> dict:
    """Sales after each arm's first firing; for X also the shipments settlement still paid."""
    for mid, row in arms.items():
        g = events.loc[events.merchant_id.eq(int(mid))]
        total = int(g.gmv_cents.sum())
        ships = (None if shipments is None
                 else shipments.loc[shipments.merchant_id.eq(int(mid))])
        for arm, first in row.items():
            if first is None:
                continue
            date = day(first["date"])
            after = int(g.loc[g.d.gt(date), "gmv_cents"].sum())
            first["approved_gmv_after_share"] = after / total if total else None
            if arm == "X" and ships is not None:
                shipped = int(ships.amount_cents.sum())
                later = int(ships.loc[ships.shipped_d.gt(date), "amount_cents"].sum())
                first["shipped_gmv_after_cents"] = later
                first["shipped_gmv_after_share"] = later / shipped if shipped else None
    return arms


FRAUD_BASES = ("third_party_fraud", "account_takeover", "never_pay", "inr_abuse", "promo_abuse")


def case_diagnostics(replay: dict, bustout_ids: set[int], labels: pd.DataFrame,
                     cfg: dict) -> dict:
    """Describe non-bust-out chargeback cases by dispute reason and adjudicated basis.

    Evaluation only: the bases are known after the fact and never reach the monitor.
    """
    window = pd.Timedelta(days=cfg["monitor"]["window_days"] - 1)
    cases, mix = [], {}
    for alert in replay["alerts"]:
        if alert["merchant_id"] in bustout_ids:
            continue
        codes = "+".join(alert["trigger_codes"])
        mix[codes] = mix.get(codes, 0) + 1
        if not {"B", "W"} & set(alert["trigger_codes"]):
            continue
        date = day(alert["date"])
        mine = labels.loc[labels.merchant_id.eq(alert["merchant_id"])
                          & labels.d.between(date - window, date)]
        cases.append({"merchant_id": alert["merchant_id"], "date": alert["date"],
                      "trigger_codes": alert["trigger_codes"], "disputes": len(mine),
                      "reasons": mine.reason.value_counts().sort_index().to_dict(),
                      "bases": mine.basis.value_counts().sort_index().to_dict(),
                      "fraud_or_abuse_share": (float(mine.basis.isin(FRAUD_BASES).mean())
                                               if len(mine) else None)})
    totals = {key: {} for key in ("reasons", "bases")}
    for case in cases:
        for key in totals:
            for name, n in case[key].items():
                totals[key][name] = totals[key].get(name, 0) + int(n)
    return {"non_bustout_case_trigger_mix": dict(sorted(mix.items())),
            "chargeback_cases": len(cases),
            "chargeback_cases_mostly_fraud_or_abuse": sum(
                (c["fraud_or_abuse_share"] or 0) >= 0.5 for c in cases),
            "dispute_reasons": totals["reasons"], "dispute_bases": totals["bases"],
            "cases": cases}


def report(events: pd.DataFrame, cfg: dict, world: dict, shipments: pd.DataFrame | None = None,
           calibration: dict | None = None, labels: pd.DataFrame | None = None) -> dict:
    as_of = day(events.attrs["meta"]["as_of"])
    events = events.loc[events.d.le(as_of)].copy()
    spine = build_spine(events, as_of)
    counts = reconcile(spine, events, counts_at(events, as_of))
    if shipments is not None:
        counts["shipments"] = reconcile_shipments(clip_shipments(shipments, as_of),
                                                  shipment_counts_at(shipments, as_of))
        shipments = clip_shipments(shipments, as_of)
    metrics = compute_metrics(spine, cfg, shipments, calibration)
    names = [name for name in ALL_SETS if shipments is not None or not needs_delivery(name)]
    bustout_ids = {b["merchant_id"] for b in world["bustouts"]}
    cohorts = {"dev": [b for b in world["bustouts"] if day(b["closed_at"]) < DEV_END],
               "held_out": [b for b in world["bustouts"] if day(b["closed_at"]) >= DEV_END]}
    periods = {"dev": (DEV_START, DEV_END),
               "operating_held_out": (DEV_END, OPERATING_END),
               "follow_up": (OPERATING_END, FOLLOWUP_END)}
    windows = {name: (day(start), day(end))
               for name, (start, end) in world["protocol_windows"].items()}
    replays = {name: evaluate(metrics, cfg, name) for name in names}
    prefix = prefix_checks(events, shipments, calibration, replays, cfg, world, as_of)
    results = {}
    for name, replay in replays.items():
        arms = arm_firsts(metrics, cfg, name, world["bustouts"])
        results[name] = {
            "selected": name == cfg["monitor"]["rule_set"],
            "core_episodes": len(replay["alerts"]), "escalations": len(replay["escalations"]),
            "detections": {cohort: detections(events, replay, members)
                           for cohort, members in cohorts.items()},
            "arm_first_firings": remaining_exposure(arms, events, shipments),
            "review_load": {period: review_load(metrics, replay, bustout_ids, start, end, cfg)
                            for period, (start, end) in periods.items()},
            "protocol_review_load": {window: review_load(metrics, replay, bustout_ids, start,
                                                         end, cfg)
                                     for window, (start, end) in windows.items()},
            "prefix_invariance": prefix[name],
        }
    diagnostics = {}
    if labels is not None:
        diagnostics = {name: case_diagnostics(replays[name], bustout_ids, labels, cfg)
                       for name in dict.fromkeys([cfg["monitor"]["rule_set"], "c0"])
                       if name in replays}
    monthly = spine.assign(month=spine.d.dt.strftime("%Y-%m")).groupby("month")
    shares = []
    for month, g in monthly:
        total, new = int(g.gmv_cents.sum()), int(g.new_gmv_cents.sum())
        shares.append({"month": month, "gmv_cents": total, "new_gmv_cents": new,
                       "new_account_gmv_share": new / total if total else None})
    return {"meta": {"as_of": str(as_of.date()), "parameters": cfg["monitor"],
                     "selected_rule_set": cfg["monitor"]["rule_set"],
                     "source": events.attrs["meta"]["source"],
                     "shipments_source": (None if shipments is None
                                          else shipments.attrs["meta"]["source"]),
                     "calibration": calibration, "counts": counts, "world": world},
            "rule_sets": results, "case_diagnostics": diagnostics,
            "portfolio_new_account_gmv_share_by_month": shares}


def _clip_checked(ap: argparse.ArgumentParser, events: pd.DataFrame | None,
                  shipments: pd.DataFrame | None, cutoff: pd.Timestamp) -> tuple:
    """Check export totals before clipping, then keep only what was known by the cutoff.

    An export observed before the cutoff would zero-fill days it never saw, so it is refused.
    """
    for name, frame in [("event", events), ("shipment", shipments)]:
        if frame is not None and day(frame.attrs["meta"]["as_of"]) < cutoff:
            ap.exit(2, f"monitor: {name} export observed only through "
                       f"{frame.attrs['meta']['as_of']}, before {cutoff.date()}\n")
    if events is not None:
        totals, counts = event_totals(events), events.attrs["meta"]["counts"]
        if totals != counts:
            ap.exit(2, f"monitor: event totals {totals} != source totals {counts}\n")
        events = events.loc[events.d.le(cutoff)].copy()
        assert not events.d.gt(cutoff).any()
    if shipments is not None:
        meta = shipments.attrs["meta"]
        reconcile_shipments(shipments, shipment_counts_at(shipments, meta["as_of"]))
        shipments = clip_shipments(shipments, cutoff)
        assert not (shipments.shipped_d.gt(cutoff).any() or shipments.confirmed_d.gt(cutoff).any())
    return events, shipments


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("select", "calibrate", "gate", "report", "export-labels"))
    ap.add_argument("--events", type=Path)
    ap.add_argument("--shipments", type=Path)
    ap.add_argument("--world", default="416-baseline")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    if args.command == "export-labels":
        if args.out is None:
            ap.error("export-labels needs --out")
        labels = export_dispute_labels(args.out)
        print(f"wrote {args.out} ({len(labels)} disputes)")
        return
    if args.command == "calibrate":
        if args.shipments is None:
            ap.error("calibrate needs --shipments")
        cfg = yaml.safe_load((REPO / "config.yaml").read_text())
        known_by = day(cfg["monitor"]["delivery"]["calibration_known_by"])
        _, shipments = _clip_checked(ap, None, load_shipments(args.shipments), known_by)
        output = calibrate(shipments, cfg, read_world()["world"])
        path = REPO / cfg["monitor"]["delivery"]["calibration"]
        path.write_text(json.dumps(output, indent=1, allow_nan=False))
        print(f"deadline {output['deadline_days']} days; reference unconfirmed share "
              f"{output['reference_observed_share']:.4f}, upper bound {output['p_ref']:.4f} "
              f"({output['reference_unconfirmed']} of {output['reference_shipments']})")
        print(f"wrote {path}")
        return
    if args.events is None:
        ap.error("--events is required")
    events = load_events(args.events)
    if args.command == "gate":
        if args.shipments is None:
            ap.error("gate needs --shipments")
        events, shipments = _clip_checked(ap, events, load_shipments(args.shipments), DEV_AS_OF)
        cfg = yaml.safe_load((REPO / "config.yaml").read_text())
        output = gate_dev(events, shipments, cfg, read_world(), load_calibration(cfg))
        path = REPO / "reports" / "monitoring_gate_dev.json"
        path.write_text(json.dumps(output, indent=1, allow_nan=False))
        print("set   reviews  per 100 mq  X reviews  X per 100 mq  dev bust-outs caught")
        for name, result in output["sets"].items():
            load = result["review_load"]
            rate, x_rate = load["review_load"], load["delivery_review_load"]
            print(f"{name:4s}  {load['reviews']:7d}  {rate:10.2f}  {load['delivery_reviews']:9d}  "
                  f"{x_rate:12.2f}  {result['detections']['caught_before_closure']}")
        print(f"adopted: {output['adopted_rule_set']}; ships: {output['ship_rule_set']}")
        print(f"wrote {path}")
        return
    if args.command == "select":
        events, _ = _clip_checked(ap, events, None, DEV_AS_OF)
    cfg = yaml.safe_load((REPO / "config.yaml").read_text())
    world = read_world(REPO / f"monitor/eval/world_{args.world}.json")
    if args.command == "select":
        output = select_dev(events, cfg, world)
        name = "monitoring_selection_dev.json"
    else:
        shipments = None if args.shipments is None else load_shipments(args.shipments)
        labels_path = REPO / f"monitor/eval/dispute_labels_{args.world}.csv.gz"
        output = report(events, cfg, world, shipments,
                        None if shipments is None else load_calibration(cfg),
                        load_dispute_labels(labels_path) if labels_path.exists() else None)
        name = ("monitoring_evaluation.json" if args.world == "416-baseline"
                else f"monitoring_evaluation_{args.world}.json")
    path = REPO / "reports" / name
    path.write_text(json.dumps(output, indent=1, allow_nan=False))
    if args.command == "select":
        print("rules  dev caught  non-bust-out episodes/100 quarters  feasible")
        for c in output["candidates"]:
            rate = c["non_bustout_workload"]["episodes_per_100_eligible_merchant_quarters"]
            rate_text = f"{rate:.3f}" if rate is not None else "undefined"
            print(f"{c['rule_set']:5s}  {c['detections']['caught_before_closure']:10d}  "
                  f"{rate_text:37s}  {c['feasible']}")
        print(f"selected: {output['selected_rule_set']}; ships: {output['ship_rule_set']}; "
              f"c3 young: {output['c3_young']}")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
