# Monitoring iteration log: AUP-06 on the bnpl-fraud-workbench event world

## 1. Protocol (fixed before any rule selection)

**World.** bnpl-fraud-workbench world `416-baseline` (seed 416, generator 2.0.0),
manifest identity `208122eba8effdd94fb5b19bcac8d9916c5c13a7d71119c972ab24c368b7bc29`,
regenerated at workbench commit `1db054d` and loaded into a scratch MySQL. It is the
world the workbench's own committed results use (its code commit `417a9b1`). 158
merchants; approved orders 2024-01-01 to 2025-08-31; outcomes observed to 2025-12-29.
Provenance and the evaluation-only facts are in
[`eval/world_416-baseline.json`](eval/world_416-baseline.json); only
[`evaluate.py`](evaluate.py) reads that file.

**What was already known.** An audit of the previous monitor on this world had
summarised all eight bust-out merchants, including the four held out below: their
closure dates, peak ticket drift (1.03–1.70×), volume z (≤ 1.5), new-account share
(≥ 40% at all eight) and the timing of their disputes (almost all after closure). The
held-out evaluation is therefore a pre-specified, audit-informed comparison with a
frozen temporal split, not a blind test. The bust-out logic in the workbench's
simulator was not read.

**Point-in-time rules.** Each day d is evaluated with the events the platform knew by
the end of d: orders by order time, disputes by the time the platform learned of
them, refunds by their known time. Every merchant has a row for every calendar day
from its first approved order, so disputes on days without orders count. Rollup
totals are reconciled to the source tables on every run.

**Metrics** (parameters in `config.yaml` `monitor:`):

- Trailing window: the 30 days ending on d. Baseline: the 90 days before that window,
  limited to days since the merchant's first order.
- Ratios (chargeback rate, ticket drift, new-account GMV share, refund rate) are
  computed only when the trailing window has at least 20 approved orders; otherwise
  they are empty and cannot trigger.
- Volume z and ticket drift also need at least 30 baseline days and 20 baseline
  orders. Volume z = (orders in window − 30μ) / √(30·max(μ, s²)), with μ and s² the
  baseline's daily mean and variance.
- New-account GMV share is weighted by order amount; an account is new when it was
  created within 30 days before the order.
- A merchant is eligible on d once it has at least 14 days and 30 approved orders
  since its first order.

**Triggers.** W: chargeback rate ≥ 1.5%; B: ≥ 2.5% (both also need at least 3
disputes in the window); V: volume z ≥ 3; T: ticket drift ≥ 2×; S: new-account GMV
share ≥ 40%; Y(age, x): merchant younger than `age` days since onboarding with
new-account GMV share ≥ x; F: refund collapse (baseline refund rate ≥ 2%, current
≤ 0.5%, at least 3 disputes in the window).

**Candidate rule sets.** An alert needs the merchant to be eligible that day.

| Rule set | Alert when |
| --- | --- |
| c0 (control: AUP-06 as written, corrected) | B, or any two of {W or B, V, T, S} |
| c1a | c0, or Y(90 days, 40%) |
| c1b | c0, or Y(90 days, 60%) |
| c1c | c0, or Y(180 days, 40%) |
| c2 | c0, or F |
| c3 | c0, or the best of c1a–c1c, or F |

Thresholds were not searched beyond these six. The 3-dispute floor, the volume
minimums, the 90-day episode length and the young-merchant ages are fixed. The world
turned out to contain no refund events (found while building the extraction, before
any selection), so F cannot fire here: c2 behaves as c0 and c3 as its c1 component.

**Alerts and workload.** An alert opens an episode; the same merchant cannot alert
again for 90 days. A separate surveillance flag D (at least 3 disputes in the
trailing 30 days, regardless of volume) is recorded but takes no part in selection
or in the main detection count.

**Split.** Bust-outs are assigned by closure date: dev = the four closed before
2024-11-01 (132, 136, 139, 145); held out = the four closed later (147, 149, 151,
158). Selection sees only events known by 2024-10-31.

**Selection criterion.**

1. Feasible: on dev data, at most 5 alert episodes on non-bust-out merchants per 100
   eligible non-bust-out merchant-quarters. This is an illustrative review-capacity
   assumption, not an industry figure. If c0 itself exceeds it, nothing is selected
   and c0 ships.
2. Among feasible rule sets, prefer: more dev bust-outs caught (first alert on a
   calendar day before closure); then fewer non-bust-out episodes per exposure; then
   fewer added conditions.

The winner is written to `config.yaml` `monitor.rule_set` and committed before the
full-period evaluation runs.

**What gets reported for every rule set.**

- Bust-outs caught before closure, as counts out of four (dev and held out), with
  lead time and the share of each bust-out's sales made after its alert.
- Late detection: core alerts on or after closure, and D flags, with days after
  closure.
- Non-bust-out workload for dev, for the held-out operating period (2024-11-01 to
  2025-08-31) and for the follow-up months after orders stop, with raw counts.
- A prefix check at the workbench's three freeze dates: replaying with data up to
  each date reproduces the full-history alerts up to that date.

"Non-bust-out alerts" are not called false alerts: the world labels bust-outs, not
every merchant worth a review.

**Not tested here.** The workbench world also records shipments and carrier-confirmed
deliveries. Non-delivery is the bust-outs' defining behaviour, so a delivery rule
would be the obvious next signal. It is outside AUP-06, and adding it after the audit
would test a rule chosen with the answer in view. It is left for a separately
pre-registered follow-up.
