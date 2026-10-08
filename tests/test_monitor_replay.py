"""The committed alerts must be what the committed exports replay to."""

from __future__ import annotations

import json
import math
from pathlib import Path

import yaml

from monitor.metrics import compute_metrics
from monitor.rollup import build_spine, counts_at, day, load_events, load_shipments, reconcile
from monitor.rules import needs_delivery
from monitor.watch import evaluate

REPO = Path(__file__).resolve().parent.parent
EXPORT = REPO / "reports" / "monitor_events_416-baseline.csv.gz"
SHIPMENTS = REPO / "reports" / "monitor_shipments_416-baseline.csv.gz"
CALIBRATION = REPO / "reports" / "monitoring_delivery_calibration.json"
ALERTS = REPO / "reports" / "monitoring_alerts.json"


def same(a: object, b: object) -> bool:
    """Floats may differ in the last bits across numpy/pandas builds; nothing else may."""
    if isinstance(a, float) and isinstance(b, float):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-12)
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b, strict=True))
    return a == b


def test_committed_alerts_replay_from_committed_export() -> None:
    committed = json.loads(ALERTS.read_text())
    cfg = yaml.safe_load((REPO / "config.yaml").read_text())
    rule_set = committed["meta"]["rule_set"]
    events = load_events(EXPORT)
    as_of = day(committed["meta"]["as_of"])
    spine = build_spine(events, as_of)
    counts = reconcile(spine, events, counts_at(events, as_of))
    assert counts["source"] == committed["meta"]["counts"]["source"]
    shipments = calibration = None
    if needs_delivery(rule_set):
        shipments = load_shipments(SHIPMENTS)
        calibration = json.loads(CALIBRATION.read_text())
        assert committed["meta"]["calibration"] == calibration
    replay = evaluate(compute_metrics(spine, cfg, shipments, calibration), cfg, rule_set)
    for key in ("alerts", "escalations", "dispute_count_flags"):
        assert same(replay[key], committed.get(key, [])), key
