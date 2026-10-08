# Reports

- `decisions_summary.json`: underwriting decisions for the 16 fixture merchants
  (`make screen`). It does not depend on the workbench.
- `monitor_events_416-baseline.csv.gz` and its `.meta.json`: the daily merchant event
  rollup the monitor reads, including dispute counts by alleged reason, exported from
  [`bnpl-fraud-workbench`](https://github.com/nacapule/bnpl-fraud-workbench) world
  `416-baseline` (manifest identity `208122eb…`; provenance in
  [`../monitor/eval/world_416-baseline.json`](../monitor/eval/world_416-baseline.json)),
  so the monitor replays without MySQL (`make monitor-offline`).
- `monitor_shipments_416-baseline.csv.gz` and its `.meta.json`: order-level reported
  shipments and carrier confirmations, dated by when the platform knew them. The
  monitor reads these alongside the event rollup for delivery-confirmation checks.
- `monitor_events_1041-baseline.csv.gz`, `monitor_events_2718-baseline.csv.gz`,
  `monitor_shipments_1041-baseline.csv.gz`, `monitor_shipments_2718-baseline.csv.gz`
  and their `.meta.json` files: equivalent exports for the two fresh worlds,
  generated at workbench `1db054d` only after s1's adoption. Evaluation carries
  over world 416's frozen calibration.
- [`v1-2026-08/`](v1-2026-08): the earlier monitor's alerts and memos. They were
  produced on the workbench's synthetic world at tag
  [`v1-2026-08`](https://github.com/nacapule/bnpl-fraud-workbench/tree/v1-2026-08)
  (seed 416, orders from 2025-07-01 to 2026-06-25) by this repo at
  [`8371b9f`](https://github.com/nacapule/merchant-risk-screener/tree/8371b9f). Merchant
  ids and dates refer to that world.
- [`monitoring_delivery_calibration.json`](monitoring_delivery_calibration.json):
  delivery deadline and reference share fitted on world 416 data known by
  2024-08-31, without labels: 5 days and p_ref = 0.048215897
  (`make monitor-calibrate`).
- [`monitoring_gate_dev.json`](monitoring_gate_dev.json): iteration 2's registered
  dev gate, using only world 416 events known by 2024-10-31. It adopts s1, the
  first candidate within the total-review and delivery-review ceilings
  (`make monitor-gate`).
- [`monitoring_alerts.json`](monitoring_alerts.json): s1's 41 case openings,
  8 settlement-pause escalations and 179 separate dispute-count flags on world 416,
  `as_of 2025-12-29` (`make monitor-offline`).
- [`monitoring_memos.md`](monitoring_memos.md): 49 advisory memos, one per case
  opening or escalation on world 416, drafted by the configured model
  `gpt-6.1-sol` through the Codex CLI with prompt version `monitor_v3`.
  The responses are cached in `screen/eval/cache/`, so `make memos-offline`
  reproduces the file.
- [`monitoring_selection_dev.json`](monitoring_selection_dev.json): the frozen
  iteration-1 dev selection using events known by 2024-10-31. That iteration's
  workload ceiling rejected c0 itself, so c0 shipped; c1b was the dev-ranked
  candidate, reported as secondary. This file preserves that selection.
- [`monitoring_evaluation.json`](monitoring_evaluation.json) and
  the fresh-world files
  [`monitoring_evaluation_1041-baseline.json`](monitoring_evaluation_1041-baseline.json)
  and [`monitoring_evaluation_2718-baseline.json`](monitoring_evaluation_2718-baseline.json):
  full-period results for the frozen arms, including dev and held-out detection,
  non-bust-out review load, delivery timing, reconciliation, prefix checks and
  world provenance. `make monitor-eval` regenerates all three JSONs.
- [`monitoring_evaluation.md`](monitoring_evaluation.md): the current write-up,
  led by iteration 2's adoption and results, with iteration 1's selection retained
  in brief.
- [`../monitor/eval/`](../monitor/eval/): evaluation-only `world_*.json` provenance
  and bust-out facts, plus `dispute_labels_*.csv.gz` and their metadata for later
  adjudicated dispute diagnostics. The monitor does not read these inputs.
