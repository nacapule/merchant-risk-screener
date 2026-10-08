"""Synthetic histories test calendar, cutoff and episode semantics without a database."""

from __future__ import annotations

import copy
import gzip
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

import numpy as np
import pandas as pd
import pytest
import yaml

import monitor.evaluate as evaluation
import monitor.memo as memo
import monitor.watch as watch
from llm.client import CodexCLIClient, LLMResponse
from monitor.metrics import compute_metrics
from monitor.rollup import (
    COLUMNS,
    COUNT_COLUMNS,
    REASONS,
    REPO,
    VALUES,
    ReconciliationError,
    build_spine,
    counts_at,
    event_totals,
    export_events,
    load_events,
    reconcile,
    source_info,
)
from monitor.rules import RULE_SETS, predicates

CFG = yaml.safe_load((REPO / "config.yaml").read_text())


def events(rows: list[dict], as_of: str | None = None) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    for col in VALUES:
        if col not in df:
            df[col] = 0
    df = df[COLUMNS].fillna(0)
    if not any(row.keys() & REASONS.keys() for row in rows):
        df["n_disputes_not_received"] = df["n_disputes"]
    df["d"] = pd.to_datetime(df["d"])
    for col in ["merchant_id", *VALUES]:
        df[col] = df[col].astype("int64")
    last = as_of or str(df.d.max().date())
    df.attrs["meta"] = {"as_of": last, "counts": event_totals(df),
                        "onboarding": {str(mid): str(df.loc[df.merchant_id.eq(mid), "d"].min())
                                       for mid in df.merchant_id.unique()},
                        "source": {"file": "synthetic", "sha256": "synthetic"}}
    return df


def history(counts: list[int], start: str = "2024-01-01", mid: int = 1,
            disputes: int = 0) -> pd.DataFrame:
    return events([{"merchant_id": mid, "d": str(date.date()), "n_orders": count,
                    "gmv_cents": count * 1000, "n_disputes": disputes}
                   for date, count in zip(pd.date_range(start, periods=len(counts)),
                                          counts, strict=True)])


def replay(df: pd.DataFrame, as_of: str, rule_set: str = "c0") -> dict:
    return watch.evaluate(compute_metrics(build_spine(df, as_of), CFG), CFG, rule_set)


def test_spine_keeps_dispute_and_refund_days_without_orders() -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": 30, "gmv_cents": 34567},
                 {"merchant_id": 1, "d": "2024-01-03", "n_disputes": 3, "n_refunds": 2},
                 {"merchant_id": 2, "d": "2024-01-02", "n_orders": 4}])
    spine = build_spine(df, "2024-01-05")
    assert len(spine) == 9
    assert spine.loc[spine.d.eq("2024-01-03"), "n_orders"].sum() == 0
    assert spine.n_disputes.sum() == 3 and spine.n_refunds.sum() == 2
    assert all(spine[col].dtype == np.dtype("int64") for col in VALUES)
    result = reconcile(spine, df, {**dict.fromkeys(COUNT_COLUMNS, 0), "n_orders": 34,
                                   "n_disputes": 3, "n_refunds": 2,
                                   "n_disputes_not_received": 3})
    assert result["spine"] == result["events"] == result["source"]


def test_reconcile_names_mismatch_and_both_totals() -> None:
    df = history([1, 1])
    with pytest.raises(ReconciliationError, match="n_orders: event total 2 != source total 3"):
        reconcile(build_spine(df, "2024-01-03"), df,
                  {**dict.fromkeys(COUNT_COLUMNS, 0), "n_orders": 3})
    broken = build_spine(df, "2024-01-03")
    broken.loc[0, "n_disputes"] = 1
    with pytest.raises(ReconciliationError, match="n_disputes: spine total 1 != event total 0"):
        reconcile(broken, df, event_totals(df))


@pytest.mark.parametrize("table,count", [
    ("orders", "n_orders"), ("chargebacks", "n_disputes"), ("cash_events", "n_refunds"),
])
def test_mysql_cutoff_includes_latest_event_lost_by_join(
        table: str, count: str, monkeypatch: pytest.MonkeyPatch) -> None:
    df = history([1])
    sources = {"orders": [pd.Timestamp("2024-01-01")], "chargebacks": [], "cash_events": [],
               "fulfilments": [], "deliveries": []}
    sources[table].append(pd.Timestamp("2024-01-03"))

    def execute(sql: str, params: dict | None = None) -> SimpleNamespace | list[tuple[int, str]]:
        if sql == "SELECT merchant_id, created_at FROM merchants":
            return [(1, "2024-01-01")]
        assert "JOIN" not in sql.upper()
        source = next(name for name in sources if f"FROM {name}" in sql)
        if source == "orders":
            assert "status='approved'" in sql
        if source == "cash_events":
            assert "kind='refund'" in sql
        if "MAX(" in sql:
            assert "DATE(" in sql
            value = max(sources[source], default=None)
        elif "reason =" in sql and "'item_not_received'" not in sql:
            value = 0
        else:
            assert params is not None
            value = sum(date < params["end"] for date in sources[source])
        return SimpleNamespace(scalar_one=lambda: value)

    engine, conn = MagicMock(), MagicMock()
    engine.connect.return_value.__enter__.return_value = conn
    conn.execute.side_effect = execute
    monkeypatch.setitem(sys.modules, "sqlalchemy", SimpleNamespace(
        create_engine=lambda url: engine, text=lambda sql: sql))
    monkeypatch.setattr(pd, "read_sql", lambda sql, conn, coerce_float: df.copy())
    loaded = load_events("mysql+pymysql://fake:fake@localhost/fake")
    meta = loaded.attrs["meta"]
    assert meta["as_of"] == "2024-01-03"
    expected = event_totals(df)
    expected[count] += 1
    if count == "n_disputes":
        expected["n_disputes_not_received"] += 1
    assert meta["counts"] == expected
    with pytest.raises(ReconciliationError, match=f"{count}: event total .* != source total"):
        reconcile(build_spine(loaded, meta["as_of"]), loaded, meta["counts"])
    engine.dispose.assert_called_once()


def test_export_is_deterministic_with_sidecar_counts_and_hash(tmp_path: Path) -> None:
    df = events([{"merchant_id": 2, "d": "2024-01-04", "n_refunds": 2},
                 {"merchant_id": 1, "d": "2024-01-01", "n_orders": 35, "gmv_cents": 98765}],
                as_of="2024-01-06")
    a, b = tmp_path / "a.csv.gz", tmp_path / "b.csv.gz"
    export_events(a, df)
    export_events(b, df.iloc[::-1])
    assert a.read_bytes() == b.read_bytes()
    assert a.read_bytes()[4:8] == b"\x00\x00\x00\x00"
    assert gzip.decompress(a.read_bytes()).decode().splitlines()[0] == ",".join(COLUMNS)
    meta = json.loads(Path(f"{a}.meta.json").read_text())
    assert meta["sha256"] == hashlib.sha256(a.read_bytes()).hexdigest()
    assert meta["counts"] == event_totals(df)
    loaded = load_events(a)
    assert loaded.attrs["meta"]["as_of"] == "2024-01-06"
    assert loaded.gmv_cents.sum() == 98765
    assert counts_at(loaded, "2024-01-01")["n_refunds"] == 0
    loaded.attrs["meta"]["counts"]["n_orders"] = 36
    with pytest.raises(ReconciliationError):
        reconcile(build_spine(loaded, "2024-01-06"), loaded, counts_at(loaded, "2024-01-06"))
    assert source_info("mysql+pymysql://someone:secret@127.0.0.1:3350/bnpl") == {
        "host": "127.0.0.1", "port": 3350, "database": "bnpl"}
    a.write_bytes(a.read_bytes() + b"tampered")
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        load_events(a)


@pytest.mark.parametrize("rule_set", RULE_SETS)
def test_random_prefix_invariance_including_late_disputes_and_flags(rule_set: str) -> None:
    rng = np.random.default_rng(42)
    rows = []
    for mid in (1, 2, 3):
        for i, date in enumerate(pd.date_range("2024-01-01", periods=240)):
            count = int(rng.poisson(4 if i < 90 else 12)) if i < 165 else 0
            disputes = int(rng.poisson(0.08 if i < 165 else 0.4))
            rows.append({"merchant_id": mid, "d": str(date.date()), "n_orders": count,
                         "gmv_cents": count * (1000 if i < 90 else 3000),
                         "new_gmv_cents": count * (100 if i < 90 else 2400),
                         "n_disputes": disputes, "n_refunds": int(rng.poisson(0.2))})
    # The order is known in January; its dispute becomes known only on this later day.
    rows[200]["n_disputes"] += 4
    # A merchant can have a dispute-only history before its first approved order.
    rows.extend([{"merchant_id": 4, "d": "2024-01-01", "n_disputes": 3},
                 {"merchant_id": 4, "d": "2024-03-01", "n_orders": 30, "gmv_cents": 30000}])
    df = events(rows)
    full = replay(df, "2024-08-27", rule_set)
    assert full["alerts"] and full["dispute_count_flags"]
    for offset in sorted(rng.choice(np.arange(1, 239), size=7, replace=False)):
        cutoff = pd.Timestamp("2024-01-01") + pd.Timedelta(days=int(offset))
        clipped = df.loc[df.d.le(cutoff)].copy()
        partial = replay(clipped, str(cutoff.date()), rule_set)
        assert partial == {key: [a for a in value if pd.Timestamp(a["date"]) <= cutoff]
                           for key, value in full.items()}
    early = replay(df, "2024-01-02", rule_set)["dispute_count_flags"]
    assert early[0]["metrics"]["days_since_first_order"] is None


def test_quiet_days_have_null_ratios_and_json_safe_dispute_flags() -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": 30, "gmv_cents": 30000},
                 {"merchant_id": 1, "d": "2024-03-10", "n_disputes": 3},
                 {"merchant_id": 2, "d": "2024-03-10", "n_disputes": 3}])
    metrics = compute_metrics(build_spine(df, "2024-03-11"), CFG)
    for column in ("cb_rate_30d", "ticket_drift", "new_gmv_share", "refund_rate_30d"):
        assert metrics.loc[metrics.orders_30d.eq(0), column].isna().all()
    assert not np.isinf(metrics.select_dtypes(include="number").to_numpy()).any()
    result = watch.evaluate(metrics, CFG, "c0")
    assert not result["alerts"] and len(result["dispute_count_flags"]) == 2
    json.dumps(result, allow_nan=False)
    assert result["dispute_count_flags"][0]["metrics"]["cb_rate_30d"] is None


def test_new_share_is_gmv_weighted() -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": 20,
                  "n_new_orders": 1, "gmv_cents": 11900, "new_gmv_cents": 10000}])
    row = compute_metrics(build_spine(df, "2024-01-01"), CFG).iloc[0]
    assert row.new_gmv_share == pytest.approx(10000 / 11900)
    assert row.new_gmv_share != pytest.approx(1 / 20)


def test_money_stays_integer_through_missing_days_and_window_sums() -> None:
    amount = 2**53 + 1
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": 20,
                  "gmv_cents": amount, "new_gmv_cents": amount - 1},
                 {"merchant_id": 1, "d": "2024-01-03", "n_orders": 1, "gmv_cents": 17}])
    spine = build_spine(df, "2024-03-01")
    assert spine.iloc[0].gmv_cents == amount
    metrics = compute_metrics(spine, CFG)
    assert metrics.iloc[2].gmv_30d == amount + 17
    assert metrics.iloc[2].new_gmv_30d == amount - 1
    assert metrics.iloc[-1].base_gmv == amount + 17


@pytest.mark.parametrize("disputes,orders,warn,breach", [
    (2, 50, False, False), (3, 200, True, False), (3, 120, False, True),
    (3, 19, False, False),
])
def test_chargeback_floor_and_breach_counts_once(disputes: int, orders: int,
                                                warn: bool, breach: bool) -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": orders,
                  "gmv_cents": orders * 1000, "n_disputes": disputes}])
    metrics = compute_metrics(build_spine(df, "2024-01-15"), CFG)
    p = predicates(metrics, CFG, "c0").iloc[-1]
    assert bool(p.W) == warn and bool(p.B) == breach
    assert bool(p.core) == breach  # a single warning is not two predicates
    assert bool(p.D) == (disputes >= 3)


@pytest.mark.parametrize("base", [[2] * 90, [0, 4] * 45])
def test_volume_z_and_baseline_on_hand_computed_history(base: list[int]) -> None:
    df = history(base + [6] * 30 + [1000])
    row = compute_metrics(build_spine(df, "2024-04-30"), CFG).iloc[119]
    mu, var = np.mean(base), np.var(base, ddof=1)
    assert row.base_days == 90 and row.base_orders == sum(base)
    assert row.base_mu == pytest.approx(mu) and row.base_var == pytest.approx(var)
    assert row.orders_30d == 180
    assert row.volume_z == pytest.approx((180 - 30 * mu) / np.sqrt(30 * max(mu, var)))
    assert row.ticket_drift == pytest.approx(1)
    assert np.isnan(compute_metrics(build_spine(df, "2024-01-31"), CFG).iloc[-1].volume_z)


def test_eligibility_is_daily_and_age_uses_onboarding() -> None:
    df = history([1] * 35)
    df.attrs["meta"]["onboarding"]["1"] = "2023-12-01 23:00:00"
    metrics = compute_metrics(build_spine(df, "2024-02-04"), CFG)
    assert not metrics.iloc[:29].eligible.any()
    assert metrics.iloc[29:].eligible.all()
    assert metrics.iloc[0].merchant_age_days == 31
    df = history([30] + [0] * 20)
    metrics = compute_metrics(build_spine(df, "2024-01-21"), CFG)
    assert not metrics.iloc[:14].eligible.any() and metrics.iloc[14:].eligible.all()


def test_episode_suppression_rearms_at_day_91_and_start_preserves_state() -> None:
    df = history([5] * 220, disputes=1)
    full = replay(df, "2024-08-07")
    for key in ("alerts", "dispute_count_flags"):
        dates = [pd.Timestamp(a["date"]) for a in full[key]]
        assert len(dates) == 3
        assert [(b - a).days for a, b in zip(dates, dates[1:], strict=False)] == [91, 91]
    metrics = compute_metrics(build_spine(df, "2024-08-07"), CFG)
    start = "2024-04-01"
    assert watch.evaluate(metrics, CFG, "c0", start=start) == {
        key: [a for a in value if a["date"] >= start] for key, value in full.items()}


def test_young_variants_and_refund_collapse_are_separate_extensions() -> None:
    df = history([10] * 120)
    metrics = compute_metrics(build_spine(df, "2024-04-29"), CFG).tail(1).copy()
    metrics["merchant_age_days"] = 100
    metrics["new_gmv_share"] = 0.5
    metrics["base_refund_rate"] = 0.03
    metrics["refund_rate_30d"] = 0.004
    metrics["disputes_30d"] = 3
    metrics["cb_rate_30d"] = 0.01
    assert not predicates(metrics, CFG, "c0").iloc[0].core
    assert not predicates(metrics, CFG, "c1a").iloc[0].core
    assert not predicates(metrics, CFG, "c1b").iloc[0].core
    assert predicates(metrics, CFG, "c1c").iloc[0].core
    assert predicates(metrics, CFG, "c2").iloc[0].core
    cfg = copy.deepcopy(CFG)
    cfg["monitor"]["c3_young"] = "c1c"
    assert predicates(metrics, cfg, "c3").iloc[0].core
    metrics["disputes_30d"] = 2
    assert not predicates(metrics, cfg, "c2").iloc[0].F


def world_file(tmp_path: Path) -> dict:
    world = {"world": "synthetic", "bustouts": [
        {"merchant_id": 1, "onboarded_at": "2024-01-01", "closed_at": "2024-06-01"},
        {"merchant_id": 3, "onboarded_at": "2024-11-01", "closed_at": "2025-01-01"}],
        "protocol_freezes": {"freeze": "2024-10-01"},
        "protocol_windows": {"dev": ["2024-01-01", "2024-11-01"]}}
    path = tmp_path / "world.json"
    path.write_text(json.dumps(world))
    return evaluation.read_world(path)


def test_selection_refuses_untruncated_data_and_cli_clips_before_metrics(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    df = events(history([2] * 400).to_dict("records")
                + history([2] * 400, mid=2).to_dict("records"))
    world = world_file(tmp_path)
    with pytest.raises(ValueError, match="selection refuses data after 2024-10-31"):
        evaluation.select_dev(df, CFG, world)
    clipped = df.loc[df.d.le(evaluation.DEV_AS_OF)].copy()
    result = evaluation.select_dev(clipped, CFG, world)
    assert result["as_of"] == "2024-10-31"
    assert len(result["candidates"]) == 6 and result["selected_rule_set"] == "c0"
    assert all(c["detections"]["n_bustouts"] == 1 for c in result["candidates"])
    json.dumps(result, allow_nan=False)
    root = tmp_path / "repo"
    (root / "reports").mkdir(parents=True)
    (root / "config.yaml").write_text(yaml.safe_dump(CFG))
    monkeypatch.setattr(evaluation, "REPO", root)
    monkeypatch.setattr(evaluation, "load_events", lambda path: df)
    monkeypatch.setattr(evaluation, "read_world", lambda: world)
    actual = evaluation.select_dev
    actual_metrics = evaluation.compute_metrics
    seen = []

    def guarded(rows: pd.DataFrame, cfg: dict, facts: dict) -> dict:
        assert rows.d.max() <= evaluation.DEV_AS_OF
        seen.append(rows.d.max())
        return actual(rows, cfg, facts)

    def guarded_metrics(spine: pd.DataFrame, cfg: dict) -> pd.DataFrame:
        assert spine.d.max() <= evaluation.DEV_AS_OF
        return actual_metrics(spine, cfg)

    monkeypatch.setattr(evaluation, "select_dev", guarded)
    monkeypatch.setattr(evaluation, "compute_metrics", guarded_metrics)
    monkeypatch.setattr(sys, "argv", ["monitor.evaluate", "select", "--events", "synthetic.gz"])
    evaluation.main()
    assert seen == [evaluation.DEV_AS_OF]
    saved = json.loads((root / "reports/monitoring_selection_dev.json").read_text())
    assert saved["selected_rule_set"] == "c0"


@pytest.mark.parametrize("count", COUNT_COLUMNS)
def test_select_cli_refuses_hash_valid_export_with_wrong_sidecar_counts(
        count: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str]) -> None:
    df = events([{"merchant_id": 1, "d": "2024-10-31", "n_orders": 1},
                 {"merchant_id": 1, "d": "2024-11-02", "n_orders": 1,
                  "n_disputes": 1, "n_refunds": 1}])
    path = tmp_path / "events.csv.gz"
    export_events(path, df)
    sidecar = Path(f"{path}.meta.json")
    meta = json.loads(sidecar.read_text())
    meta["counts"][count] += 1
    sidecar.write_text(json.dumps(meta))
    assert event_totals(load_events(path)) == event_totals(df)
    monkeypatch.setattr(evaluation, "REPO", tmp_path)
    monkeypatch.setattr(sys, "argv", ["monitor.evaluate", "select", "--events", str(path)])
    with pytest.raises(SystemExit) as exc:
        evaluation.main()
    assert exc.value.code == 2
    message = f"event totals {event_totals(df)} != source totals {meta['counts']}"
    assert message in capsys.readouterr().err
    assert not (tmp_path / "reports/monitoring_selection_dev.json").exists()


def test_selection_ranking_and_infeasible_control(tmp_path: Path) -> None:
    df = history([5] * 305, mid=2, disputes=1)
    world = world_file(tmp_path)
    result = evaluation.select_dev(df, CFG, world)
    assert result["selected_rule_set"] is None and result["ship_rule_set"] == "c0"
    assert not result["candidates"][0]["feasible"]
    assert result["candidates"][0]["non_bustout_workload"][
        "episodes_per_100_eligible_merchant_quarters"] > 5
    candidates = [
        {"rule_set": name, "feasible": True, "detections": {"caught_before_closure": caught},
         "non_bustout_workload": {"episodes_per_100_eligible_merchant_quarters": rate},
         "added_predicates": evaluation.ADDED_PREDICATES[name]}
        for name, caught, rate in [("c0", 0, 0), ("c1a", 1, 4), ("c1b", 1, 3), ("c2", 1, 3),
                                   ("c3", 1, 3)]]
    assert [c["rule_set"] for c in sorted(candidates, key=evaluation._rank)] == [
        "c1b", "c2", "c3", "c1a", "c0"]


def test_workload_excludes_suppressed_days_across_period_boundary() -> None:
    df = history([5] * 200, mid=2)
    metrics = compute_metrics(build_spine(df, "2024-07-18"), CFG)
    alerts = [{"merchant_id": 2, "date": "2024-01-20", "metrics": {"disputes_30d": 3}},
              {"merchant_id": 2, "date": "2024-04-20", "metrics": {"disputes_30d": 3}}]
    load = evaluation.workload(metrics, alerts, set(), pd.Timestamp("2024-04-01"),
                               pd.Timestamp("2024-05-01"), CFG)
    assert load["episodes"] == 1
    assert load["eligible_merchant_days"] == 30 and load["exposure_days"] == 1
    assert load["suppressed_eligible_days"] == 29
    assert load["episodes_per_100_eligible_merchant_quarters"] == pytest.approx(9131.25)


def test_detection_uses_strict_calendar_date_and_gmv_after_alert() -> None:
    df = history([1] * 6)
    alert = {"merchant_id": 1, "date": "2024-01-03", "trigger_codes": ["B"]}
    cohort = [{"merchant_id": 1, "onboarded_at": "2024-01-01",
               "closed_at": "2024-01-03 23:59:59"}]
    result = evaluation.detections(df, {"alerts": [alert], "dispute_count_flags": [alert]}, cohort)
    assert result["caught_before_closure"] == 0
    assert result["merchants"][0]["exposure_after_alert_share"] == pytest.approx(0.5)
    assert {a["kind"] for a in result["late_detections"]} == {"core_alert", "D_flag"}
    assert all(a["days_after_closure"] == 0 for a in result["late_detections"])
    cohort[0]["closed_at"] = "2024-01-05"
    result = evaluation.detections(df, {"alerts": [alert], "dispute_count_flags": []}, cohort)
    assert result["caught_before_closure"] == 1 and result["merchants"][0]["lead_days"] == 2


def test_report_on_synthetic_data(tmp_path: Path) -> None:
    df = history([5] * 400, disputes=1)
    cfg = copy.deepcopy(CFG)
    cfg["monitor"]["rule_set"] = "c0"
    result = evaluation.report(df, cfg, world_file(tmp_path))
    assert set(result["rule_sets"]) == set(RULE_SETS)
    assert result["rule_sets"]["c0"]["selected"]
    assert all(r["prefix_invariance"]["freeze"]["passed"] for r in result["rule_sets"].values())
    json.dumps(result, allow_nan=False)


def test_watch_cli_reconciliation_failure_is_exit_2(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    df = history([1, 1])
    df.attrs["meta"]["counts"]["n_orders"] = 3
    monkeypatch.setattr(watch, "load_events", lambda path: df)
    monkeypatch.setattr(sys, "argv", ["monitor.watch", "--events", "synthetic.gz",
                                    "--out", str(tmp_path / "alerts.json")])
    with pytest.raises(SystemExit) as exc:
        watch.main()
    assert exc.value.code == 2
    assert not (tmp_path / "alerts.json").exists()


def test_watch_cli_file_mode_defaults_to_sidecar_date(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_orders": 30,
                  "gmv_cents": 30000, "n_disputes": 3}], as_of="2024-02-15")
    path, out = tmp_path / "events.csv.gz", tmp_path / "alerts.json"
    export_events(path, df)
    monkeypatch.setattr(sys, "argv", ["monitor.watch", "--events", str(path), "--rules", "c0",
                                      "--out", str(out)])
    watch.main()
    saved = json.loads(out.read_text())
    assert saved["meta"]["as_of"] == "2024-02-15"
    assert saved["meta"]["rule_set"] == "c0"
    assert saved["meta"]["source"]["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert saved["alerts"] == replay(df, "2024-02-15")["alerts"]


def test_memo_concurrency_preserves_episode_order_and_offline(
        monkeypatch: pytest.MonkeyPatch) -> None:
    completed = []

    def fake_draft(alert: dict, offline: bool) -> dict:
        assert offline
        if alert["date"] == "0":
            time.sleep(0.05)
        completed.append(alert["date"])
        return {"episode": alert["date"]}

    monkeypatch.setattr(memo, "draft", fake_draft)
    alerts = [{"date": str(i)} for i in range(12)]
    assert memo.draft_all(alerts, True, jobs=4) == [{"episode": str(i)} for i in range(12)]
    assert completed.index("0") > completed.index("1")
    with pytest.raises(ValueError, match="jobs must be at least 1"):
        memo.draft_all(alerts, True, jobs=0)


def test_memo_uses_new_prompt_full_context_and_codex_effort(
        monkeypatch: pytest.MonkeyPatch) -> None:
    alert = replay(history([5] * 30, disputes=1), "2024-01-30")["alerts"][0]

    def cached(prompt: str, *, task: str, offline: bool) -> LLMResponse:
        assert task == "monitor_memo" and offline
        assert json.dumps(alert, indent=1, sort_keys=True, allow_nan=False) in prompt
        assert "confirm or dismiss" in prompt and "Null metrics" in prompt
        assert "60–90" not in prompt
        return LLMResponse(text='{"recommended_action": "monitor"}',
                           model="synthetic", backend="cache", duration_ms=0, cached=True)

    monkeypatch.setattr(memo, "complete_cached", cached)
    assert memo.draft(alert, True)["recommended_action"] == "monitor"
    monkeypatch.delenv("CODEX_EFFORT", raising=False)
    assert CodexCLIClient().effort == "high"
    monkeypatch.setenv("CODEX_EFFORT", "xhigh")
    assert CodexCLIClient().effort == "xhigh"


def test_watch_path_isolation() -> None:
    forbidden = re.compile(r"closed_at|labels|latent_|evaluation_only|monitor[/\.]eval|"
                           r"bustout|bust.out|\b(?:132|136|139|145|147|149|151|158)\b")
    for name in ("events.sql", "rollup.py", "metrics.py", "rules.py", "watch.py"):
        assert not forbidden.search((REPO / "monitor" / name).read_text()), name
    assert "installments" not in (REPO / "monitor/events.sql").read_text()


def test_dispute_reasons_must_sum_to_the_total() -> None:
    df = events([{"merchant_id": 1, "d": "2024-01-01", "n_disputes": 2,
                  "n_disputes_unauthorized": 1}])
    with pytest.raises(ReconciliationError, match="dispute reasons must sum"):
        build_spine(df, "2024-01-02")
