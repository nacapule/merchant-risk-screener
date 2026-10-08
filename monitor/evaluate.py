"""Keep outcome facts outside the monitor and enforce a dev-only selection boundary."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import pandas as pd
import yaml

from monitor.metrics import compute_metrics
from monitor.rollup import REPO, build_spine, counts_at, day, event_totals, load_events, reconcile
from monitor.rules import RULE_SETS
from monitor.watch import evaluate

DEV_AS_OF = pd.Timestamp("2024-10-31")
DEV_END = pd.Timestamp("2024-11-01")
OPERATING_END = pd.Timestamp("2025-09-01")
FOLLOWUP_END = pd.Timestamp("2025-12-30")
WORLD_PATH = REPO / "monitor/eval/world_416-baseline.json"
ADDED_PREDICATES = {"c0": 0, "c1a": 1, "c1b": 1, "c1c": 1, "c2": 1, "c3": 2}


def read_world(path: Path = WORLD_PATH) -> dict:
    return json.loads(path.read_text())


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


def prefix_checks(events: pd.DataFrame, full: dict, cfg: dict, rule_set: str,
                  world: dict, as_of: pd.Timestamp) -> dict:
    checks = {}
    for name, freeze in world["protocol_freezes"].items():
        cutoff = day(freeze) - pd.Timedelta(days=1)
        if cutoff > as_of:
            continue
        clipped = events.loc[events.d.le(cutoff)].copy()
        replay = evaluate(compute_metrics(build_spine(clipped, cutoff), cfg), cfg, rule_set)
        expected = {key: [a for a in full[key] if day(a["date"]) <= cutoff]
                    for key in ("alerts", "dispute_count_flags")}
        if replay != expected:
            raise ValueError(f"prefix invariance failed for {rule_set} at {cutoff.date()}")
        checks[name] = {"as_of": str(cutoff.date()), "passed": True,
                        "alerts": len(replay["alerts"]),
                        "dispute_count_flags": len(replay["dispute_count_flags"])}
    return checks


def report(events: pd.DataFrame, cfg: dict, world: dict) -> dict:
    as_of = day(events.attrs["meta"]["as_of"])
    events = events.loc[events.d.le(as_of)].copy()
    spine = build_spine(events, as_of)
    counts = reconcile(spine, events, counts_at(events, as_of))
    metrics = compute_metrics(spine, cfg)
    bustout_ids = {b["merchant_id"] for b in world["bustouts"]}
    cohorts = {"dev": [b for b in world["bustouts"] if day(b["closed_at"]) < DEV_END],
               "held_out": [b for b in world["bustouts"] if day(b["closed_at"]) >= DEV_END]}
    periods = {"dev": (events.d.min(), DEV_END),
               "operating_held_out": (DEV_END, OPERATING_END),
               "follow_up": (OPERATING_END, FOLLOWUP_END)}
    windows = {name: (day(start), day(end))
               for name, (start, end) in world["protocol_windows"].items()}
    results = {}
    for rule_set in RULE_SETS:
        replay = evaluate(metrics, cfg, rule_set)
        results[rule_set] = {
            "selected": rule_set == cfg["monitor"]["rule_set"],
            "core_episodes": len(replay["alerts"]),
            "detections": {name: detections(events, replay, cohort)
                           for name, cohort in cohorts.items()},
            "non_bustout_workload": {name: workload(metrics, replay["alerts"], bustout_ids,
                                                   start, end, cfg)
                                     for name, (start, end) in periods.items()},
            "protocol_workload": {name: workload(metrics, replay["alerts"], bustout_ids,
                                                 start, end, cfg)
                                  for name, (start, end) in windows.items()},
            "prefix_invariance": prefix_checks(events, replay, cfg, rule_set, world, as_of),
        }
    monthly = spine.assign(month=spine.d.dt.strftime("%Y-%m")).groupby("month")
    shares = []
    for month, g in monthly:
        total, new = int(g.gmv_cents.sum()), int(g.new_gmv_cents.sum())
        shares.append({"month": month, "gmv_cents": total, "new_gmv_cents": new,
                       "new_account_gmv_share": new / total if total else None})
    return {"meta": {"as_of": str(as_of.date()), "parameters": cfg["monitor"],
                     "selected_rule_set": cfg["monitor"]["rule_set"],
                     "source": events.attrs["meta"]["source"], "counts": counts,
                     "world": world},
            "rule_sets": results, "portfolio_new_account_gmv_share_by_month": shares}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("select", "report"))
    ap.add_argument("--events", type=Path, required=True)
    args = ap.parse_args()
    events = load_events(args.events)
    if args.command == "select":
        # Check export totals before clipping; metrics remain dev-only.
        totals = event_totals(events)
        counts = events.attrs["meta"]["counts"]
        if totals != counts:
            ap.exit(2, f"monitor: event totals {totals} != source totals {counts}\n")
        events = events.loc[events.d.le(DEV_AS_OF)].copy()
        assert not events.d.gt(DEV_AS_OF).any()
    cfg = yaml.safe_load((REPO / "config.yaml").read_text())
    world = read_world()
    output = (select_dev(events, cfg, world) if args.command == "select"
              else report(events, cfg, world))
    name = ("monitoring_selection_dev.json" if args.command == "select"
            else "monitoring_evaluation.json")
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
