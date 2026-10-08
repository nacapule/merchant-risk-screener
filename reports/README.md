# Reports

- `decisions_summary.json`: underwriting decisions for the 16 fixture merchants
  (`make screen`). It does not depend on the workbench.
- `monitor_events_416-baseline.csv.gz` and its `.meta.json`: the daily merchant event
  rollup the monitor reads, exported from
  [`bnpl-fraud-workbench`](https://github.com/nacapule/bnpl-fraud-workbench) world
  `416-baseline` (manifest identity `208122eb…`; provenance in
  [`../monitor/eval/world_416-baseline.json`](../monitor/eval/world_416-baseline.json)),
  so the monitor replays without MySQL (`make monitor-offline`).
- [`v1-2026-08/`](v1-2026-08): the earlier monitor's alerts and memos. They were
  produced on the workbench's synthetic world at tag
  [`v1-2026-08`](https://github.com/nacapule/bnpl-fraud-workbench/tree/v1-2026-08)
  (seed 416, orders from 2025-07-01 to 2026-06-25) by this repo at
  [`8371b9f`](https://github.com/nacapule/merchant-risk-screener/tree/8371b9f). Merchant
  ids and dates refer to that world.
- [`monitoring_alerts.json`](monitoring_alerts.json): c0's 140 alert episodes and
  179 separate dispute-count flags, `as_of 2025-12-29` (`make monitor-offline`).
- [`monitoring_memos.md`](monitoring_memos.md): one advisory memo per c0 alert
  episode (140), drafted by the configured model `gpt-6.1-sol` through the Codex CLI.
  The responses are cached in `screen/eval/cache/`, so `make memos-offline`
  reproduces the file.
- [`monitoring_selection_dev.json`](monitoring_selection_dev.json): the frozen
  dev comparison using events known by 2024-10-31. The workload ceiling rejects
  c0 itself, so c0 ships; c1b is the dev-ranked candidate, reported separately.
- [`monitoring_evaluation.json`](monitoring_evaluation.json) and
  [`monitoring_evaluation.md`](monitoring_evaluation.md): full-period results for
  all six rule sets and the evaluation write-up, including dev and held-out
  detection, non-bust-out workload, reconciliation, prefix checks and world
  provenance (`make monitor-eval` regenerates the JSON).
