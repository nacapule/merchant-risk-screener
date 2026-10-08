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

## 2. Dev selection (events known by 2024-10-31)

`python -m monitor.evaluate select` → [`reports/monitoring_selection_dev.json`](../reports/monitoring_selection_dev.json).

| Rule set | Dev bust-outs caught (of 4) | Non-bust-out episodes | Per 100 eligible merchant-quarters | Within ceiling (≤ 5) |
| --- | --- | --- | --- | --- |
| c0 | 1 | 50 | 17.8 | no |
| c1a | 4 | 51 | 18.2 | no |
| c1b | 4 | 50 | 17.8 | no |
| c1c | 4 | 53 | 19.1 | no |
| c2 | 1 | 50 | 17.8 | no |
| c3 (c0, c1b's rule, F) | 4 | 50 | 17.8 | no |

Exposure: 280.6 eligible non-bust-out merchant-quarters.

- **Nothing is selected; c0 ships.** The control alone produces 17.8 non-bust-out
  episodes per 100 eligible merchant-quarters, more than three times the ceiling.
  Every candidate adds conditions to c0, so none can meet the ceiling. As registered,
  the ceiling is not relaxed, and `config.yaml` keeps `monitor.rule_set: c0`.
- **Where the workload comes from.** 45 of c0's 50 dev episodes rest on at least 3
  disputes in the window: chargeback-rate alerts at small merchants. The extensions
  are not the problem.
- **The dev ranking without the ceiling** puts c1b first: young merchant (under 90
  days since onboarding) with a new-account GMV share of at least 60%. It catches all
  four dev bust-outs, 20, 34, 21 and 21 days before closure, and adds no non-bust-out
  episode on dev. It is evaluated on the held-out period as the dev-ranked candidate,
  a secondary result. It does not ship.
- **c0 on dev:** one bust-out caught before closure (136, 10 days before). Its alerts
  on 132 and 139 came two and three days after closure; 145 had no alert by
  2024-10-31.

A next iteration would need a new protocol that addresses the control's
chargeback workload at low volume.

## 3. Full-period evaluation (after the freeze)

The frozen rules were replayed through 2025-12-29. c0 remains the shipped control:
its dev workload exceeded the pre-registered ceiling of 5 non-bust-out episodes per
100 eligible merchant-quarters, so no extension could be selected. c1b is reported
as the dev-ranked candidate, a secondary result; it does not ship.

| Rule set | Dev caught before closure | Dev lead days | Held-out caught before closure | Held-out lead days |
| --- | --- | --- | --- | --- |
| c0 (shipped) | 1 of 4 | 136: 10 | 1 of 4 | 147: 6 |
| c1b (secondary) | 4 of 4 | 132: 20; 136: 34; 139: 21; 145: 21 | 4 of 4 | 147: 49; 149: 24; 151: 18; 158: 19 |

Both rule sets produce 140 core episodes, with exactly the same non-bust-out
episodes in each period: dev 50, operating held-out 73, follow-up 9. c1b moves the
bust-out alerts earlier; 50.2–76.9% of each bust-out's approved sales occur after its
first alert. The other c0 bust-out alerts occur on or after closure, and every
bust-out receives a dispute-count flag 6–15 days after closure.

For all six rule sets, prefixes ending 2024-09-30, 2024-12-31 and 2025-05-31
reproduce the full-history alerts and flags through those dates exactly. Source,
event and calendar totals also reconcile: 151,268 approved orders, 1,855 disputes
and no refunds.

The comparison remains audit-informed, on one synthetic seed. Merchant-level
results, workload denominators and limits are in
[`reports/monitoring_evaluation.md`](../reports/monitoring_evaluation.md), backed by
[`monitoring_evaluation.json`](../reports/monitoring_evaluation.json).

## 4. Iteration 2: chargeback evidence and delivery confirmation

### 4.1 Proposed policy text (written before any iteration-2 code, calibration or run)

Screening now reads a byte-identical snapshot of the policy as it was screened,
[`screen/prompts/acceptable-use_2026-08.md`](../screen/prompts/acceptable-use_2026-08.md).
A test re-renders every cached screening prompt from it, so the offline decision matrix
stays reproducible while AUP-06 changes. AUP-06 is outside screening scope. The live
[`policy/acceptable-use.md`](../policy/acceptable-use.md) changes only for what the dev
gate adopts (§4.3); until then this is a proposal.

Proposed AUP-06 bullets (the introduction and the actions ladder stay):

- **06.1 Chargeback rate**: warn at 1.5%, breach at 2.5% of approved orders over 30
  days. A level is reached when the disputes learned of in the last 30 days are more than
  that level would plausibly produce at the merchant's 30-day order volume: a Poisson
  count with mean level × orders reaches at least that many disputes with probability at
  most 5%. The window needs at least 3 disputes and 20 approved orders. A breach alerts
  alone; a warning needs a second trigger.
  *Alternative wording, used only if the registered order in §4.3 reaches it:* the count
  includes only disputes alleging that goods did not arrive or were not as described.
  Disputes alleging unauthorized use are counted separately for fraud surveillance and do
  not trigger 06.1.
- **06.2** Volume z-score ≥ 3 against the merchant's completed 90-day baseline.
- **06.3** Average-ticket drift ≥ 2× baseline.
- **06.4** New-account GMV share ≥ 40% (thin-account concentration). **06.4b** At a
  merchant less than 90 days after onboarding, a new-account GMV share ≥ 60% alerts alone.
- **06.5** Refund rate collapse to about zero while disputes rise.
- **06.6 Delivery confirmation**: the platform settles a merchant when it reports a
  shipment. A reported shipment is overdue when the carrier has not confirmed delivery
  within the time by which 95% of the portfolio's carrier-confirmed deliveries arrive.
  When more of a merchant's shipments from the last seven days that have reached this
  deadline remain unconfirmed than the portfolio's normal unconfirmed share could
  plausibly produce, settlement pauses pending delivery evidence. Missing confirmation
  is a reason to review, not proof of non-delivery: some carriers do not confirm.
- An alert opens a case; the same merchant opens no new case for 90 days. A
  delivery-confirmation alert inside an open case escalates it to a settlement-pause
  review without restarting the 90 days.

### 4.2 What was known when this protocol was written

- Everything in §2 and §3 was public: all 140 c0 alert episodes with their metrics, and
  c1b's held-out result (4 of 4). On world 416 the held-out comparison is therefore
  audit-informed twice over, and c1b's held-out result is no longer a test.
- The workbench's public methods document describes the bust-out mechanism: a resale
  merchant ramps up for 40 to 75 days, stops delivering 8 to 14 days before it
  disappears and still reports shipments, and its customers claim non-delivery after
  the closure. It also states the legitimate world's delivery assumptions (median 2.5
  days; 0.5% of parcels lost; 1.5% delivered without carrier confirmation). The
  delivery rule below is mechanism-informed monitoring validation, not a discovery. The
  workbench's simulator code was not read.
- No iteration-2 rule set was run before this registration, and no per-merchant or
  per-period delivery or dispute-reason statistic was computed. Loading and exporting
  the world printed whole-period totals only, as reconciliation checks: 151,268
  shipments and 148,120 carrier confirmations; 1,855 disputes, of which 326 allege
  unauthorized use, 953 non-receipt and 576 goods not as described. c0 was replayed
  on the new export to confirm that its 140 alerts and 179 flags are unchanged.

### 4.3 Rules, candidates and the registered order

Parameters are in `config.yaml` `monitor:`; everything not listed here is as in §1.

- **K1 chargeback evidence.** With at least 20 approved orders and at least 3 disputes in
  the trailing 30 days: breach B when P[Poisson(0.025 × orders) ≥ disputes] ≤ 0.05;
  warning W when not B and P[Poisson(0.015 × orders) ≥ disputes] ≤ 0.05. Three disputes
  breach up to 32 orders and warn up to 54; 100 orders need 6 disputes to breach.
- **K2** is K1 counting only disputes that allege non-receipt or not-as-described goods;
  the 3-dispute floor applies to that count. Unauthorized disputes are reported, not
  used.
- The control keeps c0's structure: B alone, or any two of {W or B, V, T, S}.
- **Y** is c1b, unchanged: under 90 days since onboarding and new-account GMV share
  ≥ 60%.
- **X delivery confirmation.** With D and p_ref from §4.4: on day d, n = the merchant's
  shipments reported on days d − D − 6 through d − D; u = those without a carrier
  confirmation known by the end of d. X fires when u ≥ 3 and P[Binomial(n, p_ref) ≥ u]
  ≤ 0.00005. About 91 daily looks per merchant-quarter × 0.00005 gives 0.46 nominal
  noise firings per 100 merchant-quarters if the binomial reference holds; merchant
  differences or carrier outages would break that.
- Every trigger needs the merchant eligible that day (§1).
- **Cases.** A firing opens a case unless the merchant opened one in the previous 90
  days. The first X firing inside an open case not opened with X is an escalation to a
  settlement-pause review: at most one per case, and the 90 days do not restart.

| Set | Components | Role |
| --- | --- | --- |
| s1 | K1 control + Y + X | candidate 1 |
| s2 | K2 control + Y + X | candidate 2 |
| s3 | K1 control + Y | candidate 3 |
| s4 | K2 control + Y | candidate 4 |
| k1, k2 | control variants alone | reported arms |
| x | X alone | reported arm |
| c0 | iteration-1 control | reference |

**Criterion.** On dev (events known by 2024-10-31; the four dev bust-outs excluded):

- review load = non-bust-out case openings plus escalations per 100 eligible
  non-bust-out merchant-quarters, with §1's exposure (eligible days outside days 1–90
  after a case opening, divided by 91.3125);
- delivery review load = openings that include X plus escalations, on the same exposure.

The first set in the order s1, s2, s3, s4 with review load ≤ 5 and, when it contains X,
delivery review load ≤ 1 is adopted. The ceiling of 5 is §1's, unchanged. Bust-out
detection does not rank candidates. If no set qualifies, no capacity-feasible
replacement is adopted: `config.yaml` keeps c0 as the reference, and the arms are
reported as secondary results.

The gate writes [`reports/monitoring_gate_dev.json`](../reports/monitoring_gate_dev.json).
The adoption commit sets `monitor.rule_set` and replaces AUP-06's bullets in
`policy/acceptable-use.md` with the §4.1 text for the adopted components only: 06.1
(K1, or the alternative wording for K2), 06.4b if Y, and 06.6 with the case sentence if
X. It is committed before any full-period run.

### 4.4 Delivery calibration (data through 2024-08-31 only)

- D = the smallest whole number of days t such that at least 95% of the lags
  (confirmation day − shipment day) of shipments reported by 2024-07-31 and confirmed by
  2024-08-31 are at most t. Every such shipment has at least 31 days of follow-up.
- p_ref = the one-sided 99% Clopper–Pearson upper bound of the share of shipments
  reported by 2024-08-31 − D that were not confirmed within D days.
- All merchants, no labels. Bust-outs' unconfirmed shipments raise p_ref, which can only
  make X harder to fire.
- Written to
  [`reports/monitoring_delivery_calibration.json`](../reports/monitoring_delivery_calibration.json)
  and committed before the gate. X's replay before September 2024 uses parameters fitted
  on that period; it is reported as in-sample for X's calibration. The held-out period
  and the fresh worlds are out of sample.

### 4.5 Evaluation after the adoption commit

- **World 416, full period**, with §1's periods (dev; operating held-out 2024-11-01 to
  2025-08-31; follow-up to 2025-12-29) and the same prefix checks at 2024-09-30,
  2024-12-31 and 2025-05-31, extended to escalations.
- **Fresh worlds.** `1041-baseline` and `2718-baseline` (the workbench's other
  development seeds) are generated at workbench commit `1db054d` only after the adoption
  commit. They are loaded in the same scratch MySQL and exported like 416. Bust-out ids and
  closure times come from each world for evaluation only. 416's calibration is carried
  over unchanged. Every set is replayed once over the whole period. A bug fix is allowed
  and disclosed; a parameter change is not.
- **Reported for every bust-out and arm** (the control in use, Y, X, and c0): first
  firing; days before or after closure; approved GMV after the first firing. For X,
  also the shipped GMV reported after its first firing, which settlement would still
  have paid. This is remaining exposure, not prevented loss.
- **Workload.** Review load and delivery review load per period and per world, with raw
  counts and total eligible exposure, since suppression makes the denominator depend on
  the set.
- **Diagnostics, evaluation only.** The dispute-reason mix of each chargeback case, and
  the workbench's adjudicated labels on the disputed orders in each non-bust-out case's
  window. Non-bust-out cases are not called false alerts.
- **Reconciliation** of approved orders, disputes by reason, shipments and
  confirmations against the source on every world.
- **Memos.** One memo per case opening and per escalation of the adopted set on 416, drafted
  by the configured memo model. If nothing is adopted, c0's alerts and memos stay.

### 4.6 Expectations stated in advance

- X fires about D + 1 to 3 days after a bust-out stops delivering, so its lead before
  closure is at most about 14 − D days, and may be zero or negative for some bust-outs.
  It is evidence for a settlement pause, not an early warning.
- K1 and K2 do not change pre-closure bust-out detection: bust-out disputes arrive after
  closure.
- Y is the early warning. If the fresh worlds follow the documented mechanism, it
  should again flag most bust-outs weeks before closure.
- Either chargeback variant may still exceed the ceiling; then the fallback above is
  the result.
