"""Synthetic histories test chargeback evidence, delivery confirmation and case escalation."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml
from scipy.stats import beta

import monitor.evaluate as evaluation
import monitor.watch as watch
from monitor.metrics import compute_metrics, delivery_cohorts, evidence_p
from monitor.rollup import (
    COLUMNS,
    REPO,
    VALUES,
    build_spine,
    clip_shipments,
    event_totals,
    export_events,
    export_shipments,
    shipment_totals,
)

CFG = yaml.safe_load((REPO / "config.yaml").read_text())
CALIBRATION = {"deadline_days": 3, "p_ref": 0.05}


def events(rows: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    for col in VALUES:
        if col not in df:
            df[col] = 0
    df = df[COLUMNS].fillna(0)
    df["d"] = pd.to_datetime(df["d"])
    for col in ["merchant_id", *VALUES]:
        df[col] = df[col].astype("int64")
    df.attrs["meta"] = {"as_of": str(df.d.max().date()), "counts": event_totals(df),
                        "onboarding": {str(mid): str(df.loc[df.merchant_id.eq(mid), "d"].min())
                                       for mid in df.merchant_id.unique()},
                        "source": {"file": "synthetic", "sha256": "synthetic"}}
    return df


def steady(days: int, orders: int, mid: int = 1, start: str = "2024-01-01",
           disputes: dict[int, dict] | None = None) -> list[dict]:
    rows = []
    for i, date in enumerate(pd.date_range(start, periods=days)):
        row = {"merchant_id": mid, "d": str(date.date()), "n_orders": orders,
               "gmv_cents": orders * 5000}
        for col, count in (disputes or {}).get(i, {}).items():
            row[col] = count
            row["n_disputes"] = row.get("n_disputes", 0) + count
        rows.append(row)
    return rows


def ship_frame(rows: list[tuple]) -> pd.DataFrame:
    df = pd.DataFrame(rows, columns=["merchant_id", "order_id", "amount_cents", "shipped_d",
                                     "confirmed_d"])
    for col in ("shipped_d", "confirmed_d"):
        df[col] = pd.to_datetime(df[col])
    return df


@pytest.mark.parametrize("disputes,orders,rate,fires", [
    (3, 30, 0.025, True), (3, 32, 0.025, True), (3, 33, 0.025, False), (3, 40, 0.025, False),
    (3, 40, 0.015, True), (3, 54, 0.015, True), (3, 55, 0.015, False),
    (5, 100, 0.025, False), (6, 100, 0.025, True),
])
def test_poisson_evidence_thresholds(disputes: int, orders: int, rate: float,
                                     fires: bool) -> None:
    p = evidence_p(pd.Series([disputes]), pd.Series([orders]), rate).iloc[0]
    assert bool(p <= CFG["monitor"]["chargeback_evidence_max_p"]) is fires


def test_three_disputes_on_forty_orders_warn_but_do_not_breach() -> None:
    p = evidence_p(pd.Series([3]), pd.Series([40]), 0.025).iloc[0]
    assert p == pytest.approx(0.0803, abs=1e-4)


@pytest.mark.parametrize("reason,k2_fires", [("n_disputes_unauthorized", False),
                                             ("n_disputes_not_received", True)])
def test_k2_counts_only_fulfilment_related_disputes(reason: str, k2_fires: bool) -> None:
    df = events(steady(60, 1, disputes={50: {reason: 3}}))
    metrics = compute_metrics(build_spine(df, "2024-02-29"), CFG)
    k1, k2 = (watch.evaluate(metrics, CFG, name)["alerts"] for name in ("k1", "k2"))
    assert [a["trigger_codes"] for a in k1] == [["B"]]
    assert bool(k2) is k2_fires


def test_iteration1_sets_keep_their_record_shape() -> None:
    df = events(steady(60, 1, disputes={50: {"n_disputes_not_received": 3}}))
    metrics = compute_metrics(build_spine(df, "2024-02-29"), CFG)
    c0 = watch.evaluate(metrics, CFG, "c0")["alerts"][0]["metrics"]
    k1 = watch.evaluate(metrics, CFG, "k1")["alerts"][0]["metrics"]
    assert "cb_breach_p" not in c0 and "n_disputes_not_received" not in c0
    assert "cb_breach_p" in k1 and set(c0) < set(k1)


def test_delivery_cohort_counts_until_the_confirmation_is_known() -> None:
    g = pd.DataFrame({"d": pd.date_range("2024-01-01", "2024-01-31")})
    ships = ship_frame([(1, 1, 100, "2024-01-05", "2024-01-12"),
                        (1, 2, 100, "2024-01-05", None),
                        (1, 3, 100, "2023-12-28", None)])
    n, u = delivery_cohorts(g, ships, deadline=3, cohort_days=7)
    days = {str(d.date()): (int(a), int(b)) for d, a, b in zip(g.d, n, u, strict=True)}
    assert days["2024-01-07"] == (0, 0)
    assert days["2024-01-08"] == (2, 2)
    assert days["2024-01-11"] == (2, 2)
    assert days["2024-01-12"] == (2, 1)
    assert days["2024-01-14"] == (2, 1)
    assert days["2024-01-15"] == (0, 0)
    assert days["2024-01-01"] == (1, 1) and days["2024-01-06"] == (1, 1)


def bustout_world(confirm_late: bool = False) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Ships every order and confirms it two days later until deliveries stop on day 80."""
    df = events(steady(120, 5) + steady(120, 4, mid=2))
    rows, order = [], 0
    for mid, per_day in [(1, 5), (2, 4)]:
        for i, date in enumerate(pd.date_range("2024-01-01", periods=120)):
            for _ in range(per_day):
                order += 1
                if mid == 1 and i >= 80:
                    confirmed = date + pd.Timedelta(days=30) if confirm_late else None
                else:
                    confirmed = date + pd.Timedelta(days=2)
                rows.append((mid, order, 5000, date, confirmed))
    return df, ship_frame(rows)


def test_delivery_rule_fires_after_deliveries_stop_and_needs_eligibility() -> None:
    df, ships = bustout_world()
    metrics = compute_metrics(build_spine(df, "2024-04-29"), CFG, ships, CALIBRATION)
    result = watch.evaluate(metrics, CFG, "x")
    assert [(a["merchant_id"], a["trigger_codes"]) for a in result["alerts"]] == [(1, ["X"])]
    fired = pd.Timestamp(result["alerts"][0]["date"])
    stop = pd.Timestamp("2024-01-01") + pd.Timedelta(days=80)
    assert stop + pd.Timedelta(days=3) <= fired <= stop + pd.Timedelta(days=5)
    assert "AUP-06.6 delivery confirmation" in result["alerts"][0]["triggers"][0]
    metrics["eligible"] = False
    assert watch.evaluate(metrics, CFG, "x")["alerts"] == []


def test_x_never_fires_on_fewer_than_three_unconfirmed() -> None:
    df = events(steady(60, 1))
    ships = ship_frame([(1, i, 5000, date, None if i < 2 else date + pd.Timedelta(days=1))
                        for i, date in enumerate(pd.date_range("2024-01-01", periods=60))])
    metrics = compute_metrics(build_spine(df, "2024-02-29"), CFG, ships,
                              {"deadline_days": 3, "p_ref": 1e-9})
    assert watch.evaluate(metrics, CFG, "x")["alerts"] == []


@pytest.mark.parametrize("cutoff", ["2024-03-25", "2024-03-27", "2024-04-05", "2024-04-20"])
def test_late_confirmation_never_repairs_an_earlier_day(cutoff: str) -> None:
    df, ships = bustout_world(confirm_late=True)
    full = watch.evaluate(compute_metrics(build_spine(df, "2024-04-29"), CFG, ships, CALIBRATION),
                          CFG, "s1")
    clipped = clip_shipments(ships, cutoff)
    early = df.loc[df.d.le(cutoff)].copy()
    prefix = watch.evaluate(compute_metrics(build_spine(early, cutoff), CFG, clipped,
                                            CALIBRATION), CFG, "s1")
    for key in ("alerts", "escalations", "dispute_count_flags"):
        assert prefix[key] == [a for a in full[key] if a["date"] <= cutoff], key
    assert any("X" in a["trigger_codes"] for a in full["alerts"] + full["escalations"])


def crafted(fires: dict[str, list[tuple[int, int]]], days: int = 200) -> tuple:
    dates = pd.date_range("2024-01-01", periods=days)
    g = pd.DataFrame([(mid, d) for mid in (1, 2) for d in dates], columns=["merchant_id", "d"])
    g["eligible"] = True
    for col, value in [("merchant_age_days", 10), ("new_gmv_share", 0.7),
                       ("ship_cohort_unconfirmed", 9), ("ship_cohort_n", 10),
                       ("delivery_deadline_days", 3), ("delivery_p_ref", 0.05),
                       ("delivery_p", 1e-9)]:
        g[col] = value
    p = pd.DataFrame(False, index=g.index,
                     columns=["W", "B", "V", "T", "S", "Y", "F", "X", "control", "core", "D"])
    for code, points in fires.items():
        for mid, offset in points:
            p.loc[g.merchant_id.eq(mid) & g.d.eq(dates[offset]), code] = True
    p["core"] = p.Y | p.X
    return g, p, dates


def test_escalation_inside_an_open_case(monkeypatch: pytest.MonkeyPatch) -> None:
    g, p, dates = crafted({"Y": [(1, 0), (2, 6)], "X": [(1, 10), (1, 20), (1, 91), (1, 100),
                                                         (2, 5)]})
    monkeypatch.setattr(watch, "predicates", lambda metrics, cfg, rule_set: p)
    result = watch.evaluate(g, CFG, "s1")
    day = {i: str(d.date()) for i, d in enumerate(dates)}
    assert [(a["merchant_id"], a["date"], a["trigger_codes"]) for a in result["alerts"]] == [
        (1, day[0], ["Y"]), (2, day[5], ["X"]), (1, day[91], ["X"])]
    assert [(a["merchant_id"], a["date"], a["case_opened"]) for a in result["escalations"]] == [
        (1, day[10], day[0])]


def test_escalation_does_not_restart_the_case(monkeypatch: pytest.MonkeyPatch) -> None:
    g, p, dates = crafted({"Y": [(1, 0), (1, 91)], "X": [(1, 80)]})
    monkeypatch.setattr(watch, "predicates", lambda metrics, cfg, rule_set: p)
    result = watch.evaluate(g, CFG, "s1")
    assert [a["date"] for a in result["alerts"]] == [str(dates[0].date()), str(dates[91].date())]
    assert len(result["escalations"]) == 1


def test_calibration_uses_early_shipments_only() -> None:
    rows = [(1, i, 100, pd.Timestamp("2024-06-01"), pd.Timestamp("2024-06-01")
             + pd.Timedelta(days=i)) for i in range(1, 21)]
    rows += [(2, 100 + i, 100, pd.Timestamp("2024-08-01"), None) for i in range(5)]
    ships = ship_frame(rows)
    result = evaluation.calibrate(ships, CFG, "synthetic")
    assert result["deadline_days"] == 19
    reference = ships.loc[ships.shipped_d.le(pd.Timestamp("2024-08-31") - pd.Timedelta(days=19))]
    late = reference.confirmed_d.isna() | reference.confirmed_d.gt(
        reference.shipped_d + pd.Timedelta(days=19))
    x, n = int(late.sum()), len(reference)
    assert (x, n) == (6, 25)
    assert result["p_ref"] == pytest.approx(beta.ppf(0.99, x + 1, n - x))
    later = ship_frame([*rows, (3, 999, 100, pd.Timestamp("2024-09-01"), None)])
    with pytest.raises(ValueError, match="refuses data after 2024-08-31"):
        evaluation.calibrate(later, CFG, "synthetic")


def candidate(review: float, delivery: float) -> dict:
    return {"review_load": {"review_load": review, "delivery_review_load": delivery}}


def test_adoption_follows_the_registered_order() -> None:
    sets = {"s1": candidate(4.0, 1.5), "s2": candidate(6.0, 0.5), "s3": candidate(4.5, 0.0),
            "s4": candidate(3.0, 0.0)}
    assert evaluation.adopt(sets, CFG) == "s3"
    sets["s1"] = candidate(5.0, 1.0)
    assert evaluation.adopt(sets, CFG) == "s1"
    assert evaluation.adopt({name: candidate(5.1, 0.0) for name in sets}, CFG) is None


def test_gate_refuses_data_after_the_dev_cutoff() -> None:
    df, ships = bustout_world()
    late = events(steady(5, 1, start="2024-10-30"))
    with pytest.raises(ValueError, match="refuses data after 2024-10-31"):
        evaluation.gate_dev(late, ships, CFG, {"bustouts": []}, CALIBRATION)
    with pytest.raises(ValueError, match="refuses data after 2024-10-31"):
        evaluation.gate_dev(df, ship_frame([(1, 1, 1, "2024-11-02", None)]), CFG,
                            {"bustouts": []}, CALIBRATION)


def test_review_load_counts_escalations_and_delivery_reviews() -> None:
    df, ships = bustout_world()
    metrics = compute_metrics(build_spine(df, "2024-04-29"), CFG, ships, CALIBRATION)
    replay = {"alerts": [{"merchant_id": 2, "date": "2024-02-01", "trigger_codes": ["Y"],
                          "metrics": {"disputes_30d": 0}}],
              "escalations": [{"merchant_id": 2, "date": "2024-02-11", "trigger_codes": ["X"]}],
              "dispute_count_flags": []}
    load = evaluation.review_load(metrics, replay, {1}, metrics.d.min(),
                                  pd.Timestamp("2024-04-30"), CFG)
    assert (load["case_openings"], load["escalations"], load["delivery_reviews"]) == (1, 1, 1)
    assert load["review_load"] == pytest.approx(
        200 / load["eligible_merchant_quarters"])
    assert np.isfinite(load["total_eligible_merchant_quarters"])


def write_exports(tmp_path: Path, df: pd.DataFrame, ships: pd.DataFrame,
                  as_of: str) -> tuple[Path, Path]:
    ships = ships.copy()
    ships.attrs["meta"] = {"as_of": as_of, "counts": shipment_totals(clip_shipments(ships, as_of)),
                           "source": {"file": "synthetic", "sha256": "synthetic"}}
    events_path, ships_path = tmp_path / "events.csv.gz", tmp_path / "ships.csv.gz"
    export_events(events_path, df, as_of)
    export_shipments(ships_path, ships, as_of)
    return events_path, ships_path


def test_gate_cli_refuses_exports_observed_before_the_cutoff(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str]) -> None:
    df, ships = bustout_world()
    events_path, ships_path = write_exports(tmp_path, df, ships, "2024-04-29")
    monkeypatch.setattr(sys, "argv", ["monitor.evaluate", "gate", "--events", str(events_path),
                                      "--shipments", str(ships_path)])
    with pytest.raises(SystemExit) as exc:
        evaluation.main()
    assert exc.value.code == 2
    assert "observed only through 2024-04-29, before 2024-10-31" in capsys.readouterr().err


def test_watch_checks_full_sidecar_counts_at_an_earlier_cutoff(
        tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
        capsys: pytest.CaptureFixture[str]) -> None:
    df, ships = bustout_world()
    events_path, ships_path = write_exports(tmp_path, df, ships, "2024-04-29")
    sidecar = Path(f"{ships_path}.meta.json")
    meta = json.loads(sidecar.read_text())
    meta["counts"]["n_confirmed"] += 1
    sidecar.write_text(json.dumps(meta))
    monkeypatch.setattr(sys, "argv", ["monitor.watch", "--events", str(events_path),
                                      "--shipments", str(ships_path), "--rules", "x",
                                      "--as-of", "2024-02-29", "--out",
                                      str(tmp_path / "alerts.json")])
    calibration = tmp_path / "calibration.json"
    calibration.write_text(json.dumps(CALIBRATION))
    monkeypatch.setattr(watch, "REPO", tmp_path)
    cfg = copy.deepcopy(CFG)
    cfg["monitor"]["delivery"]["calibration"] = "calibration.json"
    (tmp_path / "config.yaml").write_text(yaml.safe_dump(cfg))
    with pytest.raises(SystemExit) as exc:
        watch.main()
    assert exc.value.code == 2
    assert "n_confirmed: export total" in capsys.readouterr().err


def test_gate_counts_reviews_from_january_only() -> None:
    rows = steady(120, 3, mid=2, start="2023-11-01")
    for row in rows:
        row["new_gmv_cents"] = row["gmv_cents"]
    df = events(rows)
    ships = ship_frame([(2, 1, 100, "2023-11-01", "2023-11-02")])
    metrics = compute_metrics(build_spine(df, "2024-02-28"), CFG, ships, CALIBRATION)
    assert watch.evaluate(metrics, CFG, "s3")["alerts"][0]["date"] < "2024-01-01"
    result = evaluation.gate_dev(df, ships, CFG, {"bustouts": []}, CALIBRATION)
    load = result["sets"]["s3"]["review_load"]
    assert load["case_openings"] == 0
    assert load["eligible_merchant_days"] == len(pd.date_range("2024-01-01", "2024-10-31"))


def test_report_with_shipments_and_labels() -> None:
    df, ships = bustout_world()
    df.attrs["meta"]["as_of"] = "2024-04-29"
    ships.attrs["meta"] = {"as_of": "2024-04-29",
                           "counts": shipment_totals(clip_shipments(ships, "2024-04-29")),
                           "source": {"file": "synthetic", "sha256": "synthetic"}}
    world = {"world": "synthetic",
             "bustouts": [{"merchant_id": 1, "onboarded_at": "2024-01-01",
                           "closed_at": "2024-04-01"}],
             "protocol_freezes": {"early": "2024-03-01", "late": "2024-04-10"},
             "protocol_windows": {"all": ["2024-01-01", "2024-05-01"]}}
    labels = pd.DataFrame({"merchant_id": [2, 2], "d": pd.to_datetime(["2024-02-01"] * 2),
                           "reason": ["unauthorized", "item_not_received"],
                           "basis": ["third_party_fraud", "none"]})
    cfg = copy.deepcopy(CFG)
    cfg["monitor"]["rule_set"] = "s1"
    result = evaluation.report(df, cfg, world, ships, CALIBRATION, labels)
    s1 = result["rule_sets"]["s1"]
    assert s1["selected"] and set(result["rule_sets"]) == set(evaluation.ALL_SETS)
    x = s1["arm_first_firings"]["1"]["X"]
    assert x["before_closure"] and 0 < x["shipped_gmv_after_share"] < 1
    assert all(check["passed"] for check in s1["prefix_invariance"].values())
    assert set(result["case_diagnostics"]) == {"s1", "c0"}
    json.dumps(result, allow_nan=False)
