# Monitoring evaluation: iteration 2

Iteration 2 adopts **s1: K1 chargeback evidence + Y young-merchant concentration +
X delivery confirmation**. On world 416, dev non-bust-out review load falls from
17.82 to 3.54 per 100 eligible merchant-quarters, within the unchanged ceiling of
5, while s1 catches 4 of 4 dev and 4 of 4 held-out bust-outs before closure. It
catches 15 of 16 on two fresh worlds; across all three worlds, X provides
settlement-pause evidence before closure at 15 of 24 bust-outs.

## Worlds and provenance

All three synthetic worlds come from
[`bnpl-fraud-workbench`](https://github.com/nacapule/bnpl-fraud-workbench), generator
2.0.0 at commit
[`1db054d`](https://github.com/nacapule/bnpl-fraud-workbench/tree/1db054dacb04da11672d4c4e71267f122ce02e7e).
Approved orders run from 2024-01-01 through 2025-08-31; outcomes are observed
through 2025-12-29. Their manifest identities are:

- [416-baseline](../monitor/eval/world_416-baseline.json):
  `208122eba8effdd94fb5b19bcac8d9916c5c13a7d71119c972ab24c368b7bc29`.
- [1041-baseline](../monitor/eval/world_1041-baseline.json):
  `decde07cfa196e682f7956b0ab52093def3a2b49417c773ce0d1346cf7a0bb60`.
- [2718-baseline](../monitor/eval/world_2718-baseline.json):
  `6d031b7f75697a295610408b7a57db979c01e7205c5ffb340bdd129eddb658c8`.

World 416 is audit-informed: iteration 1's c0 alerts and c1b's held-out result
were public before registration. The earlier audit had also summarised all eight
bust-outs, including their closure dates; this held-out comparison is not blind.
Worlds 1041 and 2718 were generated only after the adoption commit, with 416's
calibration carried over unchanged. They are fresh draws of the same generator
and bust-out mechanism, not tests of a different fraud type.

Source tables, event exports and the daily calendar reconcile exactly; shipment
exports also reconcile to their source. Dispute reasons are allegations, separate
from the workbench's later adjudicated labels. No world contains refund events.

| World | Approved orders | Disputes | Non-receipt | Not as described | Unauthorized | Shipments | Carrier confirmations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 416 | 151,268 | 1,855 | 953 | 576 | 326 | 151,268 | 148,120 |
| 1041 | 151,152 | 1,947 | 1,025 | 582 | 340 | 151,152 | 147,979 |
| 2718 | 152,297 | 1,936 | 999 | 572 | 365 | 152,297 | 149,180 |

## What changed

Iteration 1 could not select an extension because c0's chargeback workload
already exceeded capacity. **K1** replaces the raw-rate test with an evidence test
for the dispute count under [AUP-06.1](../policy/acceptable-use.md#aup-06--ongoing-monitoring-triggers-portfolio-side):
at least 20 approved orders and 3 disputes in 30 days, then a Poisson upper-tail
probability no greater than 0.05 at the warning rate of 1.5% or breach rate of
2.5%. A breach alerts alone; a warning needs corroboration. At 100 orders, for
example, a breach needs 6 disputes. This removes many small-count breaches while
retaining the control's volume, ticket and new-account-share triggers.

**K2** applies K1 to non-receipt and not-as-described disputes only, leaving
unauthorized allegations to surveillance.

**Y**, c1b carried forward unchanged as AUP-06.4b, alerts when a merchant is under
90 days since onboarding and new accounts contribute at least 60% of trailing
GMV. An account is new if created within 30 days before its order. Y is the early
warning.

The simulated platform settles merchants when they report shipments. **X**,
AUP-06.6, tests a seven-day cohort of reported shipments that have reached the
calibrated confirmation deadline. It needs at
least 3 unconfirmed shipments and a binomial upper-tail probability no greater
than 0.00005 at the portfolio reference share. Missing confirmation supports
review; it does not prove non-delivery.

Every trigger requires at least 14 days and 30 cumulative approved orders since
the merchant's first order, retaining iteration 1's eligibility rule.

A firing opens a case, suppressing another opening for 90 days. The first X
firing inside a case not opened with X creates a settlement-pause escalation,
without restarting suppression. Openings and escalations each count as reviews.
The separate three-dispute surveillance flag remains outside selection and the
main detection count.

Screening reads the dated
[August policy snapshot](../screen/prompts/acceptable-use_2026-08.md), so AUP-06
could change without changing cached screening results. Replay dates shipments
and carrier confirmations by when the platform knew them; a later confirmation
never rewrites an earlier day. Prefix checks at 2024-09-30, 2024-12-31 and
2025-05-31 reproduce earlier openings, escalations and flags for every arm in
every world.

## Frozen sequence

The [registered protocol](../monitor/ITERATION.md#4-iteration-2-chargeback-evidence-and-delivery-confirmation)
fixed the policy proposal, candidates, capacity criteria and evaluation before
any iteration-2 run. The commit sequence records each boundary:

| Step | Commit |
| --- | --- |
| Proposed policy text and screening snapshot | [62a80f9](https://github.com/nacapule/merchant-risk-screener/commit/62a80f9) |
| Registration before calibration or candidate runs | [aa17735](https://github.com/nacapule/merchant-risk-screener/commit/aa17735) |
| Delivery calibration | [9770d4f](https://github.com/nacapule/merchant-risk-screener/commit/9770d4f) |
| s1 adoption and AUP-06 update | [a18303d](https://github.com/nacapule/merchant-risk-screener/commit/a18303d) |
| Full-period and fresh-world evaluation | [ce98210](https://github.com/nacapule/merchant-risk-screener/commit/ce98210) |

## Calibration and dev gate

Calibration uses only world 416 data known by **2024-08-31**, without labels.
The 95th-percentile confirmation lag among 42,924 shipments reported by
2024-07-31 and confirmed by the cutoff gives a **5-day deadline**. In the
reference cohort, 2,287 of 49,734 shipments lacked confirmation within that
deadline: an observed share of 0.04598. Its one-sided 99% upper confidence bound
sets **p_ref = 0.048215897**. Including bust-outs can raise that reference and
make X harder to fire. X's replay before September 2024 is in-sample for this
calibration; the held-out period and fresh worlds are out of sample.

**The gate uses only world 416's dev data**, events known by 2024-10-31, with
dev bust-outs excluded from workload. It adopts the first candidate in the
registered order s1, s2, s3, s4 with total review load ≤ 5 and delivery review
load ≤ 1 per 100 eligible merchant-quarters. Detection does not rank candidates.
All reported non-bust-out reviews below are openings; there are no escalations.

| Set | Components | Reviews | Eligible quarters | Review load / 100 | Delivery load / 100 | Dev caught |
| --- | --- | --- | --- | --- | --- | --- |
| **s1, adopted** | K1 + Y + X | 11 | 310.3 | 3.54 | 0.00 | 4 of 4 |
| s2 | K2 + Y + X | 6 | 314.7 | 1.91 | 0.00 | 4 of 4 |
| s3 | K1 + Y | 11 | 310.3 | 3.54 | 0.00 | 4 of 4 |
| s4 | K2 + Y | 6 | 314.7 | 1.91 | 0.00 | 4 of 4 |
| k1 | K1 control | 11 | 310.3 | 3.54 | 0.00 | 1 of 4 |
| k2 | K2 control | 6 | 314.7 | 1.91 | 0.00 | 1 of 4 |
| x | X alone | 0 | 320.1 | 0.00 | 0.00 | 3 of 4 |
| c0, reference | Iteration-1 control | 50 | 280.6 | 17.82 | 0.00 | 1 of 4 |

## Full-period workload

Workload counts non-bust-out openings plus escalations. Exposure is eligible
merchant-days outside suppression, divided by 91.3125; it differs by rule set.
Dev ends 2024-10-31, operating held-out runs 2024-11-01–2025-08-31, and follow-up
runs 2025-09-01–2025-12-29. All reviews in this table are openings, and delivery
review load is zero throughout.

| World | Period | s1 reviews | s1 quarters | s1 load / 100 | c0 reviews | c0 quarters | c0 load / 100 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 416 | Dev | 11 | 310.3 | 3.54 | 50 | 280.6 | 17.82 |
| 416 | Operating held-out | 12 | 412.6 | 2.91 | 73 | 348.4 | 20.95 |
| 416 | Follow-up | 10 | 163.7 | 6.11 | 9 | 160.1 | 5.62 |
| 1041 | Dev | 8 | 305.4 | 2.62 | 54 | 268.3 | 20.13 |
| 1041 | Operating held-out | 10 | 406.1 | 2.46 | 71 | 346.9 | 20.47 |
| 1041 | Follow-up | 15 | 156.2 | 9.60 | 12 | 150.1 | 8.00 |
| 2718 | Dev | 16 | 314.5 | 5.09 | 66 | 274.0 | 24.09 |
| 2718 | Operating held-out | 10 | 424.1 | 2.36 | 72 | 363.9 | 19.78 |
| 2718 | Follow-up | 12 | 168.2 | 7.13 | 10 | 160.5 | 6.23 |

The K2 control lowers workload further; on 416, k2's rates are
1.91, 2.17 and 5.45 across the three periods. The registered order did not need
this alternative because s1 qualified first.

Including bust-outs, s1 opens 41 cases with 8 escalations on 416, 41 with 7 on
1041, and 46 with 8 on 2718. The 416 output retains 179 dispute-count flags and
has [49 advisory memos](monitoring_memos.md): 25 opening memos recommend a reserve,
16 recommend monitoring, and all 8 escalation memos recommend a settlement pause.
None recommends offboarding.

## Bust-out results

Cohorts use closure date: dev before 2024-11-01, held-out thereafter. A firing on
the closure day is not a detection. In the tables, positive timing means days
before closure, zero means the closure day, and negative timing means after.
Shipped GMV after X counts shipments reported on later calendar days as a share
of that merchant's total shipped GMV.

### World 416

s1 catches **4 of 4 dev and 4 of 4 held-out**; K1 and c0 each catch 1 of 4 in
each cohort. Y supplies all first cases, 18–49 days before closure.

| Merchant / cohort | Closure | First s1 case | Y lead, days | First X / timing, days | Shipped GMV after X |
| --- | --- | --- | --- | --- | --- |
| 132 / dev | 2024-04-06 | 2024-03-17 | +20 | 2024-04-04 / +2 | 3.4% |
| 136 / dev | 2024-06-26 | 2024-05-23 | +34 | 2024-06-21 / +5 | 2.6% |
| 139 / dev | 2024-08-30 | 2024-08-09 | +21 | 2024-08-29 / +1 | 3.3% |
| 145 / dev | 2024-10-30 | 2024-10-09 | +21 | 2024-10-31 / −1 | 0.0% |
| 147 / held-out | 2025-02-06 | 2024-12-19 | +49 | 2025-02-02 / +4 | 11.0% |
| 149 / held-out | 2025-03-06 | 2025-02-10 | +24 | 2025-03-06 / 0 | 0.0% |
| 151 / held-out | 2025-04-27 | 2025-04-09 | +18 | 2025-04-26 / +1 | 1.8% |
| 158 / held-out | 2025-08-29 | 2025-08-10 | +19 | 2025-08-29 / 0 | 0.0% |

### World 1041

s1 catches **3 of 3 dev and 4 of 5 held-out**; K1 and c0 each catch 1 of 3 and
3 of 5. Merchant 149 never fires Y; X opens its first case one day after closure.

| Merchant / cohort | Closure | First s1 case | Y lead, days | First X / timing, days | Shipped GMV after X |
| --- | --- | --- | --- | --- | --- |
| 133 / dev | 2024-04-23 | 2024-04-15 | +8 | 2024-04-22 / +1 | 5.2% |
| 137 / dev | 2024-07-04 | 2024-06-20 | +14 | 2024-07-01 / +3 | 5.1% |
| 142 / dev | 2024-09-30 | 2024-09-07 | +23 | 2024-09-30 / 0 | 0.0% |
| 145 / held-out | 2024-11-24 | 2024-11-05 | +19 | 2024-11-21 / +3 | 5.2% |
| 149 / held-out | 2024-12-25 | 2024-12-26 | Never | 2024-12-26 / −1 | 0.0% |
| 152 / held-out | 2025-03-24 | 2025-03-06 | +18 | 2025-03-24 / 0 | 0.0% |
| 154 / held-out | 2025-05-17 | 2025-04-19 | +28 | 2025-05-13 / +4 | 13.3% |
| 157 / held-out | 2025-08-03 | 2025-07-04 | +30 | 2025-07-30 / +4 | 12.9% |

### World 2718

s1 catches **3 of 3 dev and 5 of 5 held-out**; K1 and c0 each catch 2 of 3 and
3 of 5. Across the fresh worlds, Y catches 15 of 16, 8–41 days before closure.

| Merchant / cohort | Closure | First s1 case | Y lead, days | First X / timing, days | Shipped GMV after X |
| --- | --- | --- | --- | --- | --- |
| 135 / dev | 2024-04-21 | 2024-03-14 | +38 | 2024-04-15 / +6 | 17.7% |
| 138 / dev | 2024-06-05 | 2024-05-14 | +22 | 2024-06-02 / +3 | 10.1% |
| 141 / dev | 2024-08-09 | 2024-07-09 | +31 | 2024-08-09 / 0 | 0.0% |
| 143 / held-out | 2024-11-24 | 2024-10-30 | +25 | 2024-11-22 / +2 | 10.9% |
| 144 / held-out | 2024-12-21 | 2024-11-12 | +39 | 2024-12-21 / 0 | 0.0% |
| 148 / held-out | 2025-03-02 | 2025-01-20 | +41 | 2025-02-28 / +2 | 3.6% |
| 153 / held-out | 2025-05-07 | 2025-04-03 | +34 | 2025-05-05 / +2 | 0.0% |
| 158 / held-out | 2025-08-05 | 2025-07-19 | +17 | 2025-08-05 / 0 | 0.0% |

## Delivery confirmation and the registered expectations

X fires at **24 of 24 bust-outs and at no other merchant** in any period. It
fires before closure at **15 of 24**, 5 of 8 in each world, with leads of 1–6
days. The remaining firings occur on the closure day or one day after. Shipped
GMV reported after its first firing ranges from 0.0% to 17.7% per bust-out.

This fits [§4.6's expectations](../monitor/ITERATION.md#46-expectations-stated-in-advance):
with a 5-day deadline, X's expected lead is at most about 9 days and can be zero
or negative. It supplies settlement-pause evidence rather than early warning.
K1 and c0 have identical pre-closure detection in every world and cohort;
bust-out disputes mostly arrive after closure. Y again flags most fresh-world
bust-outs weeks earlier. The isolated x arm preserves X's record independently
of the combined rule's case suppression.

The mechanism was known from the workbench's
[public methods document](https://github.com/nacapule/bnpl-fraud-workbench/blob/1db054d/docs/methods.md):
bust-outs stop delivering 8–14 days before disappearing while still reporting
shipments. These results are mechanism-informed validation, not a discovery.

## Non-bust-out cases: evaluation-only diagnostics

Non-bust-out labels do not establish that a case was unwarranted. B means
chargeback breach, W warning, V volume and S new-account concentration. Breaches
dominate s1's cases, followed by volume with concentration; Y and X add no
non-bust-out cases in these worlds.

| World | B | B+S | V+S | W+S | W+V | Chargeback cases | Cases with ≥ half of window disputes on fraud/abuse-labelled orders |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 416 | 19 | 1 | 9 | 2 | 2 | 24 | 5 of 24 |
| 1041 | 20 | 1 | 9 | 1 | 2 | 24 | 6 of 24 |
| 2718 | 19 | 0 | 12 | 5 | 2 | 26 | 7 of 26 |

The window dispute reasons and later adjudicated bases are:

| World | Non-receipt | Not as described | Unauthorized | No fraud basis (`none`) | Third-party fraud | Never-pay | Non-receipt abuse |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 416 | 42 | 30 | 28 | 72 | 16 | 10 | 2 |
| 1041 | 45 | 32 | 20 | 75 | 11 | 9 | 2 |
| 2718 | 46 | 31 | 25 | 76 | 17 | 7 | 2 |

These bases describe customer-side fraud or abuse on disputed orders, not proof
against the merchant. `none` means no adjudicated fraud basis, not a resolved
merchant-risk judgment. Labels enter only the evaluation diagnostics; the
monitor reads observable events. c0's corresponding chargeback-case counts are
123, 129 and 137, with full diagnostics in the JSONs.

## Capacity after orders stop

s1's follow-up load exceeds 5 in every world. Every merchant's orders end on
2025-08-31 while disputes keep arriving, so the trailing order denominator
shrinks against delayed disputes. All ten 416 follow-up openings fall on
2025-09-14–27 and fire B alone, with 21–102 orders and 3–6 disputes in their
windows. This boundary needs separate treatment before interpreting follow-up
load as an ongoing portfolio's capacity requirement.

World 2718's dev load, **5.09**, is also just above the ceiling. The registered
gate applied only to world 416; it did not promise capacity compliance on fresh
worlds or in every subsequent period. No threshold was changed after adoption.

## Iteration 1 and limits

Iteration 1 retained c0 under its own registered fallback: c0's dev workload was
already 17.82 per 100 eligible merchant-quarters, above 5, and every candidate
extended it. c1b was reported as a secondary result, catching 4 of 4 dev and
4 of 4 held-out bust-outs with the same workload. Iteration 2 changes the
chargeback evidence requirement and adopts that young-merchant rule; it does
not revise iteration 1's selection.

The evaluation covers three synthetic worlds and one known bust-out mechanism.
World 416's held-out comparison is audit-informed, and fresh seeds test variation
within the same mechanism. Monitoring thresholds and review-capacity assumptions
are illustrative, not calibrated to a real portfolio. Carrier outages or
merchant differences could invalidate X's binomial reference. Approved sales
after Y and shipments after X are remaining exposure, not prevented loss: the
replay does not simulate intervention or its effect on settlement and losses.

Sources: [416 evaluation](monitoring_evaluation.json),
[1041 evaluation](monitoring_evaluation_1041-baseline.json),
[2718 evaluation](monitoring_evaluation_2718-baseline.json),
[delivery calibration](monitoring_delivery_calibration.json),
[iteration-2 dev gate](monitoring_gate_dev.json),
[s1 openings, escalations and flags](monitoring_alerts.json), and
[iteration-1 selection](monitoring_selection_dev.json). Export and evaluation
input locations are listed in the [report index](README.md).
