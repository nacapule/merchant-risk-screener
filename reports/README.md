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
