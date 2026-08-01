# Merchant monitoring memos (Claude-drafted, advisory)

## Merchant 1 — first alerting day 2026-04-30
Triggers: AUP-06.1 warn: 30d chargeback rate 2.1%; AUP-06.2: volume z=3.1 vs baseline
**Recommended action: monitor**

**Merchant 1 — 2026-04-30 review**

Volume spiked sharply (z=3.1) but the composition doesn't match a bust-out pattern: new-buyer share is 0.0% and average ticket size is flat (drift 1.03x). Bust-outs typically show rising ticket size and reliance on thin/new accounts — neither is present here. The 2.1% CB rate triggered only a warn-tier threshold and disputes lag 60-90 days, so it's too early to read as confirmed fraud.

Most likely explanation is a seasonal or marketing-driven volume lift from the existing buyer base. Recommend monitoring the next window rather than restricting payouts. Before closing this out, sanity-check that new_share=0.0 isn't a data pipeline artifact, and check for a known promo/seasonal driver.

Evidence gaps: Confirm new_share=0.0 isn't a tagging/pipeline artifact (spot-check a sample of recent-window orders for buyer account age); Check merchant's marketing calendar / promo codes for the period driving volume_z; Compare category-wide seasonal baseline for late April to isolate merchant-specific vs market-wide lift; Pull next 30-60d chargeback trend given the 60-90d dispute lag before the 2.1% warn is actionable

## Merchant 7 — first alerting day 2026-06-07
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7%
**Recommended action: monitor**

**Merchant 7 — AUP-06.1 review (2026-06-07)**

Single trigger: 30d chargeback rate at 2.68%, above threshold. No corroborating stress signals: volume is flat (z=-0.2), ticket size is down 10% vs. baseline, and new-buyer share is only 0.9% — none of the ramp behavior typical of an active bust-out (which pushes volume, ticket size, and new/thin accounts up before disputes land).

Most consistent with a category-baseline CB rate or a lagged reaction to activity from ~60-90 days back, not active extraction. Data-pipeline artifact (shrinking denominator) is also plausible given negative volume_z.

**Recommendation: monitor.** Pull CB reason codes and the merchant's volume/ticket trend from Q1 2026 to see if there was an earlier ramp that would now be surfacing as disputes. No basis yet for reserve/pause — revisit if next window shows volume or ticket-size acceleration alongside continued CB elevation.

Evidence gaps: CB reason codes (fraud vs. product/quality dispute) for the 30d window; Volume/ticket/new-buyer trend from ~60-90 days prior (the cohort actually generating today's chargebacks, given dispute lag); Raw CB count and transaction denominator to rule out a pipeline/data artifact; Peer CB-rate benchmark for this merchant's category

## Merchant 15 — first alerting day 2026-04-28
Triggers: AUP-06.1 warn: 30d chargeback rate 1.6%; AUP-06.2: volume z=5.0 vs baseline
**Recommended action: monitor**

**Merchant 15 — AUP-06 review, 2026-04-28**

Volume spiked sharply (z=5.0), triggering AUP-06.2. However, ticket size is flat (drift 1.01) and new/thin-buyer share is low (2.4%), which is inconsistent with the classic bust-out pattern of ramping ticket size via fresh accounts. CB rate (1.6%) is only warn-level and, given the 60-90 day dispute lag, isn't yet informative about this window's volume.

Most likely explanations: seasonal or marketing-driven demand from the existing buyer base, or a data pipeline artifact given the extreme z-score. Bust-out is possible but not well-corroborated by the available signals.

**Recommendation:** monitor next window; do not pause settlement absent corroborating evidence. Prioritize the cheap checks below — they should quickly separate benign demand from a fraud or data-quality explanation.

Evidence gaps: Confirm volume spike against merchant's own historical seasonality/promo calendar (any known sale event around 2026-04-28?); Check for duplicate/retry transactions or pipeline anomalies feeding the volume_z calculation; Pull new-vs-returning buyer breakdown for the recent window to confirm new_share stayed low at the transaction level, not just aggregate; Check refund/return rate trend as an earlier-arriving proxy than chargebacks (which lag 60-90 days)

## Merchant 23 — first alerting day 2026-05-06
Triggers: AUP-06.1 warn: 30d chargeback rate 1.6%; AUP-06.2: volume z=3.1 vs baseline
**Recommended action: monitor**

**Merchant 23 — AUP-06 review (2026-05-06)**

Triggers: 30d chargeback rate 1.6% (warn) and volume z=3.1 vs baseline.

However, the two markers most diagnostic of bust-out — new-buyer share (0.5%, low) and ticket-size drift (0.95, flat) — are both unremarkable. Bust-out typically pairs a volume ramp with escalating ticket size on thin/new accounts; neither is present here, favoring a benign explanation (seasonal spike or marketing push on the existing customer base).

**Action: monitor.** No corroborating bust-out evidence to justify reserve or payout action yet.

Cheapest next checks: confirm the volume spike is concentrated in repeat buyers, rule out a duplicate-transaction pipeline issue, check for a promo/seasonal driver, and re-check cb_rate next window given the 60-90d dispute lag.

Evidence gaps: Buyer-cohort split of the volume spike: is it repeat buyers or new accounts (contradicts/confirms new_share reading)?; Order-level dedup check for the volume spike window (rules out pipeline duplication); Merchant's promo/seasonal calendar for the period around 2026-05-06; Next-window cb_rate trajectory, given 60-90d dispute lag

## Merchant 25 — first alerting day 2026-06-01
Triggers: AUP-06.1 warn: 30d chargeback rate 1.5%; AUP-06.2: volume z=4.0 vs baseline
**Recommended action: reserve**

**Merchant 25 — AUP-06 Review (2026-06-01)**

Volume spiked 4σ above baseline with a modest +13% ticket drift and cb rate at the 1.53% warn line. The key mitigating fact: new buyer share is just 0.5% — this growth is coming from existing buyers, not the new/thin accounts a bust-out needs to extract value before disputes surface (which lag 60-90 days). That shape favors a marketing push or seasonal demand event over fraud, though a data pipeline artifact can't yet be ruled out.

**Recommendation:** reserve a % of payouts pending cheap confirmatory checks (campaign/channel attribution, prior-window trend, refund rate) rather than pausing settlement outright — the evidence doesn't yet corroborate bust-out, but the volume anomaly is large enough to warrant a buffer while gathering it.

Evidence gaps: Order source/channel breakdown (promo codes, campaign IDs) to confirm/deny marketing_push; Prior 2-3 monitoring windows for new_share and volume_z trend (step change vs gradual ramp) to rule out data_issue; Repeat-purchase rate and buyer tenure distribution behind the existing-buyer volume growth; Category-level seasonal calendar check for early June demand patterns; Refund/return rate trend alongside cb_rate (bust-out typically shows returns dropping while cb climbs)

## Merchant 27 — first alerting day 2026-04-26
Triggers: AUP-06.1 breach: 30d chargeback rate 3.8%
**Recommended action: monitor**

**Merchant 27 — AUP-06.1 chargeback breach (3.85% 30d)**

Threshold breach is isolated: no bust-out ramp signature present. New-buyer share is low (1.5%), avg ticket is flat-to-down (0.97x), and volume is below baseline (z=-0.6) — inconsistent with the volume/ticket/new-account ramp that defines a bust-out. More likely explanations: category-normal dispute variance, or a lagged-cohort/data attribution effect given the 60-90 day dispute lag against declining current volume.

No corroborating fraud evidence exists to justify holding payouts. Recommend **monitor** next window, with a quick check on cohort-level cb attribution (opened-date) and category peer baseline before escalating to reserve.

Evidence gaps: Cohort-level cb attribution: are the chargebacks concentrated in a specific past order window (opened-date), consistent with lagged disputes rather than new fraud?; Category/peer baseline cb rate to see if 3.85% is anomalous or within normal range for this merchant's vertical; Confirm cb_rate_30d isn't a pipeline/data artifact (e.g., denominator shrinking as volume_z falls, inflating the rate)

## Merchant 28 — first alerting day 2026-05-11
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5%
**Recommended action: monitor**

**Merchant 28 — AUP-06.1 review (2026-05-11)**

Only one threshold breached: 30d chargeback rate at 2.5%. No other AUP-06 signals fired — volume is actually *down* vs. baseline (z=-0.5), new-account share is low (2.5%), and ticket size is flat (drift 0.97).

This pattern doesn't match bust-out, which needs a volume/ticket ramp on thin accounts ahead of the cb spike. More likely: (1) a denominator effect — chargebacks lag 60-90 days, so a flat cb count against shrinking recent volume mechanically inflates the rate, or (2) this merchant's category simply runs a higher baseline dispute rate.

**Recommendation: monitor.** Single isolated trigger with no corroborating ramp signals doesn't clear the bar for reserve/pause. Before escalating, pull the underlying chargeback cohort dates and category peer benchmark — cheap checks that would quickly confirm or rule out a real risk shift.

Evidence gaps: Pull raw chargeback count vs. volume trend separately to check if the rate rise is a denominator artifact (data_issue check); Check cohort/transaction dates behind the current chargebacks — old cohort consistent with normal 60-90d lag vs. recent activity; Compare cb_rate_30d to category peer benchmark to test category_norm; Confirm no recent pipeline/attribution changes to the metrics feed for this merchant

## Merchant 29 — first alerting day 2026-05-27
Triggers: AUP-06.1 warn: 30d chargeback rate 1.7%; AUP-06.2: volume z=3.3 vs baseline
**Recommended action: monitor**

**Merchant 29 — 2026-05-27 review**

Triggers: 30d chargeback rate 1.66% (warn) and volume z=3.3 vs baseline.

The volume spike is real but doesn't carry the usual bust-out fingerprints: ticket size is flat (drift 0.95, not escalating) and new-buyer share is only 0.6% — no surge of thin/new accounts absorbing the extra volume. That points more toward a seasonal or marketing-driven demand spike than extraction behavior. The cb_rate is only at warn level, and given the 60-90 day dispute lag, it's premature to read it as bust-out fallout yet.

**Recommendation: monitor.** No reserve or settlement action warranted on this evidence — holding payouts on a merchant showing normal ticket behavior risks unnecessary friction. Re-check next window, and pull marketing-calendar/category-seasonality context now so the next read is faster. Escalate to reserve if ticket_drift or new_share start climbing alongside volume.

Evidence gaps: Check merchant's promo/marketing calendar for the window around 2026-05-27; Compare volume spike against category-wide seasonal norm for same period; Confirm volume spike is broad-based across SKUs/buyers vs concentrated in a few accounts; Re-run cb_rate and volume_z at next 30d window once dispute lag (60-90d) clears to see if trend continues or reverts

## Merchant 32 — first alerting day 2026-04-26
Triggers: AUP-06.1 warn: 30d chargeback rate 2.0%; AUP-06.2: volume z=3.6 vs baseline
**Recommended action: monitor**

**Merchant 32 — AUP-06 review (2026-04-26)**

Volume spiked sharply (z=3.6) alongside a chargeback rate crossing the 2.0% warn threshold (1.95%). However, new/thin-account share is only 2% and ticket size is only 13% above baseline — the spike is concentrated in existing buyers with stable basket sizes, which argues against a bust-out ramp (typically driven by new accounts with rising tickets).

Most likely a seasonal or promo-driven demand surge. Chargebacks lag 60-90 days, so current cb figures likely reflect pre-spike cohorts, not the new volume.

**Recommendation:** monitor next window; no payout action warranted yet given weak bust-out corroboration. Re-escalate if new_share or ticket_drift rise alongside continued volume growth, or if a promo/seasonal explanation can't be confirmed.

Evidence gaps: Merchant's marketing/promo calendar and category seasonality around 2026-04-26; Volume z-score decomposition: new vs. returning buyer contribution, to confirm existing-buyer concentration; Chargeback cohort dates (are cb's from pre-spike transactions, consistent with the 60-90d dispute lag, or already reflecting the new volume?); Pipeline/ingestion health check for the volume metric on this date to rule out double-counting

## Merchant 37 — first alerting day 2026-04-26
Triggers: AUP-06.1 warn: 30d chargeback rate 2.1%; AUP-06.2: volume z=4.1 vs baseline
**Recommended action: monitor**

**Merchant 37 — 2026-04-26 review**

Volume spiked sharply (z=4.1 vs baseline), tripping AUP-06.2. Chargeback rate ticked up to 2.08%, a soft AUP-06.1 warn. However, ticket size is flat (drift 1.02) and new-buyer share is low (2.1%) — the volume growth is not concentrated in fresh, thin-file accounts taking larger tickets, which is the fingerprint of a bust-out ramp. This pattern looks more consistent with a seasonal or promotional demand spike from the existing buyer base.

**Recommendation:** monitor. No reserve or settlement action warranted yet given the single warn-level trigger and benign-consistent ticket/new-share profile.

**Before next review:** confirm the volume spike against known seasonal/marketing calendar, sanity-check the volume metric against raw counts, and re-pull cb_rate_30d once the 60-90 day dispute lag has passed — chargebacks tied to this volume spike would only be fully visible by then.

Evidence gaps: Check merchant's category/calendar for known seasonal events or an active promo/marketing campaign around 2026-04-26; Confirm volume_z isn't a data pipeline artifact (re-pull raw transaction counts for the window); Pull buyer-tenure distribution behind the 2.1% new_share to confirm existing buyers, not just uncounted new ones; Re-check cb_rate_30d in 2-4 weeks once the 60-90 day dispute lag catches up to the volume spike

## Merchant 42 — first alerting day 2026-04-28
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6%
**Recommended action: monitor**

Merchant 42 breached AUP-06.1 (30d cb rate 2.6%) but the surrounding metrics don't fit a bust-out pattern: new_share is only 0.7% (bust-out needs a thin/new-buyer ramp) and ticket_drift is 0.89, meaning average ticket is *down* ~11% vs baseline rather than escalating. Volume_z of 1.6 is a mild lift, not a spike. This looks more like a single-metric threshold breach — possibly category-normal cb noise or a data artifact — than coordinated extraction. Given the dispute lag (60-90d), a bust-out this early would typically co-occur with rising tickets and new accounts, which we don't see. Recommend monitor: watch next window's cb rate and ticket/new-share trend before considering reserve. Pause/offboard not warranted without corroborating volume, ticket, or new-account signals.

Evidence gaps: cb_rate_30d trend over prior 2-3 windows to see if this is a step change or noise; chargeback reason codes (fraud vs. quality/non-receipt) to rule out a processing/fulfillment issue; confirm order-count denominator wasn't affected by a data pipeline gap on this date; category peer cb-rate benchmark to check if 2.6% is within normal range for this vertical

## Merchant 47 — first alerting day 2026-05-08
Triggers: AUP-06.1 warn: 30d chargeback rate 1.8%; AUP-06.2: volume z=4.3 vs baseline
**Recommended action: reserve**

Merchant 47 tripped two AUP-06 thresholds on 2026-05-08: 30d chargeback rate 1.8% (warn) and volume z=4.3 vs baseline. The classic bust-out fingerprint is absent — new/thin-buyer share is only 3.6% of volume and average ticket size is flat-to-down (drift 0.95), so the surge looks like existing buyers transacting at normal basket sizes rather than a ramp on thin accounts with inflating tickets. The date falls two days before Mother's Day (5/10), a plausible seasonal demand driver. Because chargeback disputes lag 60-90 days, bust-out can't be fully cleared yet, but the decoupling of volume from new_share/ticket_drift favors a benign spike over extraction. Recommend reserve: hold a portion of payouts as a reversible hedge while checking category seasonality, marketing spend, buyer-mix trend over the next 1-2 windows, and pipeline integrity for the ingestion date. Escalate to pause_settlement if new_share or ticket_drift start trending upward alongside volume, or if cb_rate crosses the critical threshold.

Evidence gaps: Merchant category/vertical check against the 2026-05-10 Mother's Day calendar to confirm a benign seasonal driver; New-buyer share and ticket-size trend over the prior 2-3 windows, to see if the bust-out shape is starting to emerge; Promo code / marketing spend log for the trigger window; Pipeline/ETL health check (row counts, dedup) for the 2026-05-08 ingestion to rule out a data artifact; Any pending settlement withdrawal or bank-account-change requests from the merchant (bust-out precursor)

## Merchant 63 — first alerting day 2026-04-26
Triggers: AUP-06.1 warn: 30d chargeback rate 1.7%; AUP-06.2: volume z=3.3 vs baseline
**Recommended action: monitor**

**Merchant 63 — AUP-06 review (2026-04-26)**

Volume spiked 3.3σ above baseline, triggering AUP-06.2, alongside a 1.65% 30d chargeback rate at the AUP-06.1 warn threshold. However, ticket size is flat (drift 1.02) and new-customer share is low (1.3%) — both run counter to a bust-out pattern, which typically shows rising ticket size and thin-file buyer growth as a merchant ramps extraction. This profile better fits organic seasonal demand or a marketing push among existing customers.

Given the warn-level (not critical) chargeback trigger and the absence of corroborating bust-out signals, recommend **monitor** rather than reserve/pause. Cheapest next checks: split volume_z by new vs. returning buyers, confirm no seasonal/promo calendar event, and pull chargeback reason codes. Escalate to reserve if next window shows rising ticket drift or new-buyer share alongside continued cb elevation — remember disputes lag 60–90 days, so this window's true chargeback impact isn't fully visible yet.

Evidence gaps: Volume z-score broken out by new vs. returning buyer cohort — confirms whether the spike is thin-file-driven; Merchant category/seasonal calendar check for known promo or holiday demand events on 2026-04-26; Chargeback reason codes for the 1.65% — fraud vs. product/service disputes; ETL/ingest log check for the volume_z computation window (rule out pipeline duplication)

## Merchant 64 — first alerting day 2026-04-26
Triggers: AUP-06.1 breach: 30d chargeback rate 3.6%; AUP-06.2: volume z=4.2 vs baseline
**Recommended action: reserve**

Merchant 64 breached both AUP-06 thresholds in the 2026-04-26 window: cb_rate_30d 3.65% and volume_z 4.2. However, the bust-out signature is weak — new_share is only 0.5% (volume is coming from existing buyers, not a fresh thin-file cohort) and ticket_drift is flat at 0.98 (no ticket-size ramp). Given the 60-90 day dispute lag, the current cb rate likely reflects sales predating this volume spike, not the spike itself — worth confirming via cohort analysis. Pattern is more consistent with a seasonal/promo volume surge on the existing buyer base, though a chargeback-attribution pipeline issue can't yet be ruled out. Recommend **reserve**: hold a percentage of payouts pending cohort verification and category baseline check, rather than pause/offboard, since the strongest bust-out markers (new-account ramp, ticket inflation) are absent.

Evidence gaps: Cohort/vintage the cb_rate_30d spike by original sale date — confirm it predates the current volume ramp (expected given 60-90d lag) rather than correlating with it; Buyer-level breakdown of the volume_z increase: repeat-order frequency vs distinct account count, to confirm existing-buyer-driven growth; Category/seasonal peer baseline for this merchant's vertical to test seasonal_spike vs anomaly; Pipeline check on chargeback attribution/counting logic for this window (rule out double-count or point-in-time artifact)

## Merchant 68 — first alerting day 2026-04-26
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7%
**Recommended action: monitor**

Merchant 68 breached AUP-06.1 (30d CB rate 2.68%) as its sole trigger. Supporting metrics are mild: volume_z 1.2, ticket_drift 1.08, and new_share only 3.4% — notably low, which cuts against the classic bust-out signature of ramping volume/ticket on a thin, new-buyer base. This profile looks more like normal chargeback noise or category baseline drift than a coordinated exit. Recommend **monitor** for the next window rather than restricting settlement. Before escalating, pull the CB reason-code mix and confirm whether disputes cluster in new accounts or are spread across the established base — that single check would most efficiently confirm or rule out bust-out.

Evidence gaps: Baseline-window cb_rate_30d value to size the actual delta, not just the threshold breach; Buyer-account age distribution on disputed transactions (thin/new vs established); Dispute reason codes (fraud vs. product/service not received) to distinguish bust-out from ops issues; Whether the CB uptick is concentrated in a narrow cohort/date range (pipeline gap) or spread evenly

## Merchant 75 — first alerting day 2026-04-27
Triggers: AUP-06.1 breach: 30d chargeback rate 2.8%
**Recommended action: monitor**

**Merchant 75 — AUP-06.1 review (2026-04-27)**

Single trigger: 30d chargeback rate at 2.8%, breaching the AUP-06.1 threshold. Supporting metrics are unremarkable — volume_z 1.0, ticket_drift 1.15x, new_share 2.8% — none showing the ramp-on-thin-accounts pattern typical of bust-out. Most likely explanation is normal variance around the merchant's category baseline rather than active fraud escalation, but the single-metric breach alone doesn't rule out an early-stage issue given chargeback reporting lag.

**Recommendation:** monitor next window. Pull chargeback reason codes now (cheap, fast) to confirm whether disputes are fraud-coded or service-related — that alone would materially move this from monitor toward reserve if fraud-coded disputes cluster on recent, larger tickets.

Evidence gaps: Chargeback reason codes for the 30d window (fraud vs. product/service dispute vs. non-receipt) — cheapest single check to rule bust-out in or out; cb_rate trend over the prior 2-3 windows to confirm this is a step-change vs. noise; New vs. returning buyer split within the disputed transactions specifically (not just overall new_share)

## Merchant 77 — first alerting day 2026-05-06
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9%
**Recommended action: monitor**

**Merchant 77 — AUP-06.1 review (2026-05-06)**

30d chargeback rate breached threshold at 2.9%, but it's an isolated signal: new-buyer share is low (5%), ticket drift is modest (1.1x), and volume is only mildly elevated (z=1.1). This doesn't match the bust-out fingerprint of a ramp on thin/new accounts with rising tickets — more consistent with category-normal chargeback levels or a chargeback-attribution artifact (opened- vs charge-date).

**Recommendation:** monitor next window; no reserve or settlement action warranted on a single uncorroborated trigger.

**Before escalating**, check: (1) category cb benchmark, (2) whether disputes cluster in specific accounts/tickets, (3) cb_rate recomputed on charge-date attribution, (4) trend over prior windows to confirm this isn't noise.

Evidence gaps: Category-normalized cb benchmark for this merchant's vertical to test category_norm; Dispute reason codes / whether chargebacks cluster in a handful of large tickets or specific buyer cohort; Re-run cb_rate_30d using charge-date attribution instead of opened-date to rule out data_issue; Baseline cb_rate_30d trend over prior 2-3 windows to confirm this is a step-change vs noise

## Merchant 84 — first alerting day 2026-04-26
Triggers: AUP-06.1 warn: 30d chargeback rate 1.9%; AUP-06.2: volume z=3.9 vs baseline
**Recommended action: reserve**

**Merchant 84 — AUP-06 review (2026-04-26)**

Volume spiked sharply (z=3.9), triggering a warn-level chargeback flag (1.92% cb rate). However, ticket size is flat (drift 0.98) and new/thin-file buyers are only 1.9% of volume — the classic bust-out stack (rising ticket + rising new-buyer share) is absent. This pattern looks more like a seasonal or marketing-driven demand surge than credit extraction, though the cb-rate signal is inherently uninformative this early given the 60–90 day dispute lag.

Given the magnitude of the volume anomaly, a light reversible hedge (reserve) is warranted while cheap checks are run: confirm a marketing/promo event, compare against category seasonality, and verify the buyer mix is genuinely repeat customers. No corroborating bust-out evidence exists to justify pause_settlement or offboard at this time.

Evidence gaps: Marketing/promo calendar for the merchant around 2026-04-26 to explain the volume spike; Category seasonal baseline to check if z=3.9 is normal for this vertical/period; Buyer file age/repeat-purchase breakdown to confirm the spike is repeat buyers, not disguised new accounts; Settlement/payout velocity check (any unusual withdrawal requests) as a direct bust-out tell

## Merchant 87 — first alerting day 2026-04-26
Triggers: AUP-06.1 breach: 30d chargeback rate 4.0%
**Recommended action: monitor**

**Merchant 87 — AUP-06.1 review (2026-04-26)**

Single threshold breach: 30d chargeback rate at 4.03%, just above the 4.0% line. No corroborating signal — new-buyer share is low (4%), ticket size is flat (1.02x baseline), and volume is only mildly elevated (z=1.8). This profile doesn't match a bust-out ramp, which typically shows rising ticket size and share of new/thin accounts alongside volume growth.

Most likely explanations: the merchant's category simply runs close to this threshold, or the breach reflects noise/a reporting artifact given the marginal overage and lack of a trend. **Recommend monitor** — watch the next window for persistence or trend, and check reason codes and peer benchmarks before considering any payout action. No basis yet for reserve or pause given the absence of corroborating bust-out signals.

Evidence gaps: Prior 2-3 monitoring windows for this merchant to see if cb_rate is trending up or is a one-off blip; Category/peer benchmark cb_rate to test the category_norm hypothesis; Chargeback reason codes (fraud vs. dissatisfaction vs. non-receipt) to rule out a data/attribution issue; Whether the 4.0% threshold was crossed on a small denominator (low order count) making the rate noisy

## Merchant 99 — first alerting day 2026-04-26
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9%
**Recommended action: reserve**

**Merchant 99 — AUP-06.1 breach (cb_rate 2.9%)**

Single threshold breach: 30d chargeback rate at 2.9%. However, corroborating bust-out signals are absent — new-buyer share is just 1% and ticket size is flat (1.03x), meaning volume is coming from established repeat buyers, not a thin-account ramp. Volume is elevated (z=2.5), but given the 60-90 day dispute lag, today's chargebacks likely reflect Jan-Feb activity, predating this volume spike — the two may be unrelated.

Most likely explanation is a benign demand spike (seasonal/marketing) or a category-normal cb rate, though a data/tagging issue on the cb metric can't be excluded.

**Recommendation:** reserve a portion of payouts pending review — proportionate given a real threshold breach but no bust-out corroboration. Pull category baseline and reason-code breakdown before considering pause_settlement.

Evidence gaps: Category-level baseline chargeback rate for comparable merchants; Chargeback reason-code breakdown (fraud vs. product/quality vs. friendly fraud); Whether the disputed transactions (60-90d lag, so from ~Jan-Feb) predate the current volume spike, to confirm the two aren't causally linked yet; New-vs-repeat buyer split within the disputed transactions specifically

## Merchant 102 — first alerting day 2026-04-30
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5%
**Recommended action: monitor**

**Merchant 102 — AUP-06.1 review (2026-04-30)**

Single threshold breach: 30d chargeback rate 2.52%, just over the 2.5% line. No other AUP-06 sub-thresholds fired.

Critically, the bust-out precursors are absent: volume_z is 0.8 (no ramp), ticket_drift is 0.98 (flat), and new_share is 2.5% (no thin-account concentration). A genuine bust-out typically shows volume/ticket inflation on new buyers *before* the CB spike lands (60-90d lag) — none of that shows here.

Most likely this is normal variance near the category baseline, possibly compounded by a reporting artifact. Recommend **monitor** rather than reserve/pause — no corroborating signal justifies restricting payouts yet.

Cheapest next steps: pull peer cb_rate benchmark, check dispute reason-code mix, and confirm the CB feed ran cleanly this window. Escalate to reserve only if the next window shows volume/ticket drift joining the cb_rate breach.

Evidence gaps: Category/peer benchmark cb_rate for this merchant's vertical — is 2.52% actually anomalous or near-median?; Chargeback reason codes for the 30d window (fraud vs. product/service dispute) to rule out a systemic quality issue vs. bust-out signature; Confirm CB feed pipeline ran normally for this window (rules out data_issue); Vintage of disputed transactions — concentrated in a recent cohort (consistent w/ ramp) or spread evenly (consistent w/ noise)?

## Merchant 103 — first alerting day 2026-05-01
Triggers: AUP-06.1 breach: 30d chargeback rate 3.0%
**Recommended action: monitor**

**Merchant 103 — AUP-06.1 review (2026-05-01)**

Single trigger: 30d chargeback rate 3.05%, marginally over the 3.0% threshold. Volume is up (z=2.1) but new-buyer share is only 0.6% — essentially no new/thin-file account growth — and ticket size drift is mild (+8%). This profile does not match bust-out (which needs new-account ramp + aggressive ticket escalation); it looks more consistent with a seasonal/promo volume bump or category-normal chargeback noise, possibly a data attribution artifact given the marginal breach size.

**Recommendation:** monitor next window. No reserve/pause warranted absent corroborating new-account or ticket-escalation signals.

**Before escalating**, check whether the cb spike traces to buyers acquired ~60-90 days ago (matching the volume spike) vs. scattered older cohorts, and confirm category baseline for cb rate.

Evidence gaps: Cohort split of the volume spike: new vs. repeat buyers, and whether tickets cluster in size/timing typical of bust-out; Whether cb spike traces to a specific ~60-90d-prior sales window aligned with the volume_z spike, vs. broad/old-cohort disputes (data issue signature); Category-baseline cb rate comparison to judge if 3.05% is actually elevated for this vertical; Merchant's promo/marketing calendar around the volume spike period

## Merchant 112 — first alerting day 2026-05-02
Triggers: AUP-06.1 warn: 30d chargeback rate 1.7%; AUP-06.2: volume z=3.6 vs baseline
**Recommended action: monitor**

**Merchant 112 — 2026-05-02**

Triggers: volume z=3.6 (AUP-06.2) and CB rate 1.74% (AUP-06.1 warn).

The volume spike does *not* carry the bust-out signature: new-buyer share is low (1.7%) and ticket size is flat-to-down (0.94x baseline) rather than ramping. That combination points toward a legitimate demand surge among existing buyers — seasonal or promo-driven — more than extraction behavior, which typically shows rising tickets on thin/new accounts.

CB rate is at warn, not critical, and current disputes reflect pre-spike volume given the 60-90d lag — so this window's true CB signal isn't observable yet.

**Recommendation: monitor.** No reserve or settlement action is warranted without corroborating evidence of ticket/new-account ramp. Re-check new_share and ticket_drift next window, and confirm the volume spike isn't a pipeline artifact before treating it as real.

Evidence gaps: New vs. returning buyer volume split over the last 3-4 windows (confirm new_share stayed low, not just this snapshot); Order-level ticket size distribution, not just mean drift (rules out a bimodal mix masking a high-ticket subset); Merchant promo/marketing calendar around 2026-05-02; Pipeline dedup check on the volume spike (row counts vs. distinct order IDs); CB rate trend by cohort once the 60-90d dispute lag clears for this window's volume

## Merchant 123 — first alerting day 2026-06-18
Triggers: AUP-06.1 warn: 30d chargeback rate 2.3%; AUP-06.2: volume z=3.0 vs baseline
**Recommended action: monitor**

**Merchant 123 — AUP-06 Review (2026-06-18)**

Volume spiked 3σ above baseline with a mild chargeback warn (2.3%), but the composition argues against bust-out: new buyer share is 0.0% (all volume from repeat customers) and ticket size is essentially flat (1.07x). Classic bust-out ramps show rising new_share and escalating tickets alongside volume growth — neither is present here.

Most likely benign: a seasonal or promotional spike among existing customers. One caveat — new_share reading exactly 0.0 is unusually clean and merits a data-quality check before ruling out an undercount.

**Recommendation:** monitor next window; no reserve or settlement action warranted on current evidence. Revisit chargeback rate in 60-90 days once dispute lag clears, and verify the new_share field isn't defaulting incorrectly.

Evidence gaps: Confirm new_share=0.0 against raw new-vs-returning buyer counts (rule out pipeline defect); Check marketing/promo calendar for a campaign coinciding with 2026-06-18; Pull ticket-size distribution by buyer cohort to confirm no escalation is masked in aggregate drift; Re-check cb_rate_30d in 60-90 days once dispute lag clears, since current 2.3% may understate true risk if this is an early bust-out

## Merchant 131 — first alerting day 2026-06-01
Triggers: AUP-06.1 warn: 30d chargeback rate 1.5%; AUP-06.2: volume z=3.3 vs baseline
**Recommended action: monitor**

**Merchant 131 — AUP-06 review (2026-06-01)**

Volume is running 3.3σ above baseline (AUP-06.2) with a 15% ticket-size increase, and 30d chargeback rate sits at 1.51% (AUP-06.1 warn). However, new-buyer share is only 1% — the volume spike is coming from established accounts, not the thin/new-account ramp that characterizes bust-out. That mix argues for a benign driver (seasonal demand or a marketing push) over extraction.

Caveat: chargebacks lag 60-90 days, so the current cb_rate reflects pre-spike cohorts, not the risk of this volume surge itself. Recommend monitor this cycle, confirm buyer-cohort composition and rule out a pipeline miscount, and re-check cb_rate trend over the next two windows before considering a reserve.

Evidence gaps: Buyer cohort breakdown for the spike volume — confirm it's repeat/established accounts consistent with new_share=0.01, not a mislabeled new-buyer surge; Check merchant's category/seasonal calendar and any known promo/campaign around 2026-06-01; Spot-check volume_z pipeline inputs for double-counting or ingestion gap on this date; Track cb_rate_30d over the next 1-2 windows — current rate reflects pre-spike cohorts since disputes lag 60-90 days, so the spike's true chargeback risk isn't observable yet

## Merchant 133 — first alerting day 2026-05-17
Triggers: AUP-06.1 breach: 30d chargeback rate 3.0%
**Recommended action: monitor**

Merchant 133 tripped AUP-06.1 (30d cb_rate 2.96%, ~3.0% threshold) as the sole trigger. Supporting signals argue against active bust-out: new_share is low (2.2%), ticket_drift is flat-to-down (0.94), and volume_z (1.5) is only mildly elevated — none show the coordinated ramp typical of extraction. Most likely this is either a marginal/rounding-boundary breach, category-normal variance, or a data artifact rather than a developing bust-out. Given disputes lag 60-90 days, absence of a ramp today doesn't fully rule out risk building underneath, but current evidence doesn't support payout action. Recommend monitor status: re-check next window, pull chargeback reason codes and this merchant's historical cb_rate band before considering reserve. No irreversible action warranted on a single, uncorroborated threshold trip.

Evidence gaps: Chargeback reason codes for the 30d window (fraud vs. non-fraud/service disputes); Merchant's historical cb_rate distribution — is 2.9-3.0% within its normal band?; Category-peer cb_rate baseline for comparison; New-account share and ticket size trend over the prior 2-3 windows (single point vs. drift); Any pipeline/reporting incidents flagged for this merchant or date range

## Merchant 134 — first alerting day 2026-04-26
Triggers: AUP-06.1 warn: 30d chargeback rate 1.6%; AUP-06.2: volume z=3.3 vs baseline
**Recommended action: monitor**

**Merchant 134 — 2026-04-26 review**

Triggers: 30d chargeback rate 1.58% (warn) and volume z=3.3 vs baseline. However, new-buyer share is only 0.4% and ticket size is unchanged (drift 1.0x) — this doesn't match the bust-out signature of ramping volume on thin, newly-acquired accounts with rising tickets. The profile better fits a seasonal or promo-driven demand spike among existing buyers, or possibly a data pipeline artifact inflating the volume count.

Given the chargeback rate is only at warn level and no corroborating new-account/ticket-drift signal exists, no payout action is warranted yet. Recommend monitoring next window and running two cheap checks: (1) confirm the volume spike isn't concentrated in new accounts, (2) reconcile transaction counts to rule out a pipeline double-count. Chargebacks lag 60-90 days, so re-score once the next cb_rate window lands before escalating.

Evidence gaps: Pull buyer cohort breakdown for the volume spike window (existing vs new) to confirm it's not disguised new-account ramp; Reconcile raw transaction/settlement counts against pipeline source to rule out double-counting; Check merchant's promo/marketing calendar for the trigger date; Re-check cb_rate_30d and volume_z next window (disputes lag 60-90d, so current cb rate may understate true risk)

## Merchant 143 — first alerting day 2026-05-03
Triggers: AUP-06.1 breach: 30d chargeback rate 3.5%
**Recommended action: reserve**

**Merchant 143 — AUP-06.1 review (2026-05-03)**

Triggered on a 30d chargeback rate of 3.52%, alongside a volume spike (z=2.5). However, the two classic bust-out markers are absent: new-buyer share is only 2.1% and ticket size is flat (drift=0.99) vs baseline — the volume growth isn't concentrated in thin, ramping-ticket accounts.

This profile looks more consistent with a seasonal or marketing-driven demand surge among existing customers, or possibly a data/attribution artifact given the 60-90 day dispute lag. Bust-out isn't ruled out, but current evidence doesn't corroborate it.

**Recommendation:** reserve a portion of payouts pending cohort-level review (cheap, reversible) rather than pausing settlement outright. Pull chargeback reason codes, confirm the order-count denominator wasn't distorted by a pipeline gap, and check for a concurrent promo/seasonal event before escalating.

Evidence gaps: Chargeback count and dispute reason codes behind the 3.52% figure, plus the 30d order count denominator, to rule out a pipeline/attribution artifact; Cohort split: what share of the volume spike and of the disputes is new vs returning buyers; Calendar/promo check: any campaign, holiday, or seasonal event around 2026-05-03; Ticket-size distribution by account age (a masked new-account ramp wouldn't show in the merchant-wide average)

## Merchant 145 — first alerting day 2026-05-22
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5%
**Recommended action: monitor**

**Merchant 145 — AUP-06.1 CB Rate Breach**

30d chargeback rate hit 2.55% (threshold breach), with a moderate volume uptick (z=2.1). However, the two strongest bust-out fingerprints are absent: new-buyer share is flat at 0.6% and ticket size is unchanged (drift 1.01x). Bust-out typically shows *both* rising new-account share and increasing ticket size alongside volume growth — neither is present here.

Given disputes lag 60-90 days, this CB rate reflects sales from roughly Feb-Mar, which may predate the current volume trend entirely — these could be two unrelated signals rather than one escalating pattern.

**Recommendation: monitor next window.** No corroborated fraud-ramp evidence to justify reserve/pause. Pull CB reason codes and compare against category baseline before next review; if new_share or ticket_drift begin moving alongside CB rate, escalate to reserve.

Evidence gaps: CB reason-code breakdown (fraud/unauthorized vs. quality/non-receipt disputes) — distinguishes bust-out from fulfillment issues; Merchant's CB rate vs. category baseline for the same window; Reconcile cb_rate_30d numerator/denominator against processor records for a pipeline error; New-buyer share and ticket size trend over the prior 2-3 windows (not just current snapshot) to rule out a delayed ramp

## Merchant 151 — first alerting day 2025-10-22
Triggers: AUP-06.3: avg ticket 2.1x baseline; AUP-06.4: new-account share 100%
**Recommended action: reserve**

**Merchant 151 — AUP-06 review (window ending 2025-10-22)**

Two thresholds fired together: avg ticket at 2.1x baseline (AUP-06.3) and new-account share at 100% (AUP-06.4) — the classic thin-buyer/high-ticket fingerprint. However, volume_z is -3.0, i.e. recent volume is far *below* baseline, which is inconsistent with the volume ramp that typically accompanies bust-out. That contradiction raises real odds this is a small-sample artifact or pipeline issue rather than fraud: with order counts likely low, both ratio metrics (100% new, 2.1x ticket) become unstable and easy to trigger on noise. cb_rate_30d is 0.0, but that's uninformative given 60–90 day dispute lag.

Recommend **reserve** — hold back a portion of payouts while confirming order-count denominators, ETL health, and new-account identity overlap. This is proportional: it protects against a genuine early bust-out without the irreversible cost of pause/offboard on evidence that's currently self-contradictory.

Evidence gaps: Raw order count (n) in the recent window vs baseline, to check if ratios are computed on an unstably small sample; ETL/ingestion health check for this merchant's volume feed on/around 2025-10-22 (dropped records, schema change, delayed load); Overlap analysis on the 'new' accounts (device/IP/payment fingerprint) to distinguish synthetic identities from genuine new customers; Any merchant-filed catalog, pricing, or promo change that would explain the ticket-size jump; Authorization retry/decline velocity on the elevated-ticket transactions

## Merchant 152 — first alerting day 2025-11-29
Triggers: AUP-06.3: avg ticket 2.0x baseline; AUP-06.4: new-account share 100%
**Recommended action: monitor**

**Merchant 152 — AUP-06 triggers, 2025-11-29**

Two thresholds fired: avg ticket 2.0x baseline and 100% new-account share. On the surface this resembles bust-out staging (inflate tickets on thin new accounts). However, volume_z = -1.9 shows recent volume well *below* baseline — the opposite of the ramp that defines bust-out extraction. This mismatch is more consistent with a small transaction count making both ratios noisy (data/sample-size artifact) or a genuine category/seasonal pattern (Black Friday weekend, high-ticket goods) than with an active bust-out.

cb_rate_30d=0.0 is uninformative given 60-90 day dispute lag — do not read it as reassurance.

**Recommendation: monitor.** The core bust-out signature (volume ramp) is missing, so a payout hold isn't yet justified. Pull the absolute transaction count first — if it's very low (e.g., single digits), these ratios are likely noise and no further action is needed. Re-check next window; escalate to reserve if new_share stays elevated as volume recovers.

Evidence gaps: Absolute transaction count in the recent window (cheapest check — confirms whether ratios are small-sample noise); Category/peer benchmark for ticket size and new-customer share around Black Friday; Buyer thin-file/velocity check (device, address, payment-method reuse across the 'new' accounts); Pipeline QA on the new_share/ticket_drift computation for this merchant this run

