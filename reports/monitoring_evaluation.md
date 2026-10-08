# Monitoring evaluation

The shipped control, **c0**, catches 1 of 4 dev bust-outs and 1 of 4 held-out
bust-outs before closure. **c1b**, the dev-ranked candidate, catches 4 of 4 in each
group with the same non-bust-out workload. It does not ship: the pre-registered
workload ceiling rejected the control itself, so no extension could be selected.

## World and monitor

This evaluation uses the current
[`bnpl-fraud-workbench`](https://github.com/nacapule/bnpl-fraud-workbench) event
world `416-baseline`: seed 416, generator 2.0.0, regenerated at
[`1db054d`](https://github.com/nacapule/bnpl-fraud-workbench/tree/1db054dacb04da11672d4c4e71267f122ce02e7e).
Its manifest identity is
`208122eba8effdd94fb5b19bcac8d9916c5c13a7d71119c972ab24c368b7bc29`, matching the
world used by the workbench's committed results at `417a9b1`. There are 158
merchants; approved orders run from 2024-01-01 through 2025-08-31, with outcomes
observed through 2025-12-29. Full provenance is in
[`monitor/eval/world_416-baseline.json`](../monitor/eval/world_416-baseline.json)
and the evaluation JSON's `meta.world`.

The monitor replays daily merchant activity against
[AUP-06](../policy/acceptable-use.md#aup-06--ongoing-monitoring-triggers-portfolio-side).
c0 alerts on a chargeback breach alone or two corroborating triggers: chargeback
warning/breach, volume z-score, ticket drift or new-account GMV share. Episodes
re-arm after 90 days. A separate flag records at least 3 disputes in 30 days,
regardless of order volume; it is outside rule selection and the main detection
count. Bust-out labels and closure dates are evaluation-only inputs.

## Corrections and checks

An audit of the previous monitor on this world found that its order-day rollup
dropped 405 of 1,855 disputes, later data rewrote earlier alerts, and zero-order
windows produced non-finite metrics. That monitor produced 45 alerts and caught
2 of 8 bust-outs through one-dispute breaches.

The corrected calendar includes days without orders and continues through the
observation cutoff. Source tables, extracted events and the calendar reconcile
exactly: **151,268 approved orders, 1,855 disputes and 0 refunds**. Replay evaluates
each day with information available by its end: orders at order time, disputes at
opening and refunds at their known time. The prior baseline excludes the trailing
30-day window and uses up to 90 days, requiring at least 30 baseline days and 20
baseline orders. Trailing ratios are undefined below 20 approved orders, and
warning/breach triggers require at least 3 disputes. Undefined metrics serialize
as `null`; non-finite output is rejected. New-account GMV share is now weighted by
order amount.

For all six rule sets, replaying only data through **2024-09-30, 2024-12-31 and
2025-05-31** reproduces the full-history alerts and dispute-count flags through
each cutoff exactly. These are the days before the workbench's classifier,
calibrator and policy freezes. The recorded checks are in
[`monitoring_evaluation.json`](monitoring_evaluation.json); the test suite has
53 passing tests, 38 of them for the monitor (one replays the committed export to the
committed alerts), and the underwriting decision matrix remains 16/16.

## Frozen protocol and dev selection

The [protocol](../monitor/ITERATION.md#1-protocol-fixed-before-any-rule-selection)
fixed six rule sets and a workload ceiling of 5 non-bust-out episodes per 100
eligible merchant-quarters, selecting only on events known by 2024-10-31. Bust-outs
were split by closure date: four before 2024-11-01 for dev and four later for the
held-out comparison; rules and the secondary comparison were frozen before the
full-period replay. The comparison is audit-informed: the prior audit had already
summarised all eight bust-outs, so this is not a blind test.

The [dev selection](monitoring_selection_dev.json) found c0 already above the
ceiling: 50 non-bust-out episodes over 280.6 eligible merchant-quarters, or 17.8 per
100. All extensions retain c0, so none could qualify. Under the registered fallback,
**c0 ships**; the ceiling was not relaxed. Without the ceiling, the dev ranking
puts c1b first: add an alert for a merchant under 90 days since onboarding whose
new-account GMV share is at least 60%. It catches 4 of 4 dev bust-outs without
adding a non-bust-out episode and is reported below as a secondary result.

There are no merchant-refund events in this world. The implemented refund-collapse
extension cannot fire: c2 equals c0, and c3 equals c1b here.

## Bust-out results

Full-period c0 produces **140 core alert episodes at 72 merchants** and **179
dispute-count flags**. c1b also produces 140 core episodes. Each result cell below
shows **first core alert · calendar days before/after closure · share of approved
sales after the alert**. Sales means GMV, not order count; the share includes only
sales on later calendar days. An alert on the closure day is not an early detection.

### Dev bust-outs

| Merchant | c0: alert · timing · sales after | c1b: alert · timing · sales after | First dispute-count flag · days after closure |
| --- | --- | --- | --- |
| 132 | 2024-04-08 · 2 after · 0.0% | 2024-03-17 · 20 before · 64.7% | 2024-04-17 · 11 |
| 136 | 2024-06-16 · 10 before · 8.1% | 2024-05-23 · 34 before · 68.3% | 2024-07-04 · 8 |
| 139 | 2024-09-02 · 3 after · 0.0% | 2024-08-09 · 21 before · 50.2% | 2024-09-10 · 11 |
| 145 | 2024-11-10 · 11 after · 0.0% | 2024-10-09 · 21 before · 53.3% | 2024-11-10 · 11 |

Merchant 145's c0 alert occurs after the dev selection cutoff; full-period reporting
retains its dev assignment by closure date.

### Held-out bust-outs

| Merchant | c0: alert · timing · sales after | c1b: alert · timing · sales after | First dispute-count flag · days after closure |
| --- | --- | --- | --- |
| 147 | 2025-01-31 · 6 before · 13.6% | 2024-12-19 · 49 before · 76.9% | 2025-02-12 · 6 |
| 149 | 2025-03-06 · closure day · 0.0% | 2025-02-10 · 24 before · 64.7% | 2025-03-16 · 10 |
| 151 | 2025-05-03 · 6 after · 0.0% | 2025-04-09 · 18 before · 51.0% | 2025-05-07 · 10 |
| 158 | 2025-09-05 · 7 after · 0.0% | 2025-08-10 · 19 before · 61.6% | 2025-09-13 · 15 |

c0's six remaining first alerts occur on or after closure. Five combine volume z
and new-account share after enough prior history becomes available; merchant 145
alerts on breach plus new-account share. Every bust-out's dispute-count flag arrives
6–15 days after closure. These flags preserve surveillance of low-volume disputes,
but offer no pre-closure warning here.

## Non-bust-out workload

c0 and c1b have exactly the same non-bust-out episodes in every reporting period.
Exposure counts eligible days outside the 90-day suppression period and divides
them by 91.3125 to obtain merchant-quarters.

| Period | Episodes, c0 = c1b | Eligible merchant-quarters | Episodes per 100 quarters | Episodes with ≥ 3 disputes |
| --- | --- | --- | --- | --- |
| Dev: 2024-01-01–2024-10-31 | 50 | 280.6 | 17.8 | 45 |
| Operating held-out: 2024-11-01–2025-08-31 | 73 | 348.4 | 21.0 | 69 |
| Follow-up: 2025-09-01–2025-12-29 | 9 | 160.1 | 5.6 | 9 |

The table totals **132 non-bust-out alert episodes**. The labels identify bust-outs,
not every merchant that warrants review. Chargeback rules dominate this workload:
45 of 50 dev episodes and 69 of 73 operating held-out episodes have at least
3 disputes in the window.

Across the whole portfolio, including bust-outs, c0's **140 core episodes** comprise
108 breach alone, 16 volume z plus new-account share, 12 warning plus volume z,
3 breach plus new-account share and 1 breach plus volume z. The JSON also reports
non-bust-out workload for each workbench protocol window.

## Interpretation and next step

c1b separates the young merchants in this world: the 11 young non-bust-out merchants
that became eligible peak at 20–49% new-account GMV share, versus 68–88% for the eight
bust-outs. Nineteen non-bust-out merchants onboard during the world, so age alone is
not a label. Across eligible non-bust-out merchants of any age, 76 of 110 exceed 40%
and 7 exceed 60%; the age condition matters. Portfolio new-account share also drifts
from about 0.29 in January 2024 to about 0.20–0.22 in 2025.

The earlier c1b alerts leave 50.2–76.9% of each bust-out's approved sales after the
alert. That is remaining exposure, not measured prevented loss: the replay does not
simulate intervention. Thresholds are illustrative, not calibrated. Four held-out
bust-outs on one synthetic seed, already described by the audit, do not provide a
general performance estimate.

The next step is a separately pre-registered delivery-confirmation rule using the
workbench's dated shipment and carrier-delivery evidence, alongside a new protocol
for the control's chargeback workload at low volume. That protocol must set the
review-capacity criterion before evaluation.

Sources: [full evaluation JSON](monitoring_evaluation.json),
[dev selection JSON](monitoring_selection_dev.json),
[c0 alerts and flags](monitoring_alerts.json), and
[event export metadata](monitor_events_416-baseline.csv.gz.meta.json).
[`monitoring_memos.md`](monitoring_memos.md) holds one advisory memo per c0 alert
episode (140), drafted by the configured model `gpt-6.1-sol` through the Codex CLI;
`make memos-offline` reproduces it from the cached responses.
