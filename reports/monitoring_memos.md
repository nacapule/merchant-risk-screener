# Merchant monitoring memos (model-drafted, advisory)

Provenance: rule set c0 · as_of 2025-12-29 · model gpt-6.1-sol

## Merchant 49 — alert episode 2024-02-12
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (3 disputes / 93 orders)
**Recommended action: reserve**

Merchant 49 triggered AUP-06.1 on February 12, 2024: three disputes across 93 trailing-30-day orders, a 3.2% chargeback rate. GMV was 885,239 cents; new-GMV share was 33.4%. No refunds were recorded. Observed trading history spans 42 days, with only 13 baseline days; volume, ticket and baseline-refund comparisons are unavailable, not zero-risk findings.

Recommend a percentage reserve while a human reviews the evidence. The breach supports temporary payout protection, but bust-out remains a hypothesis. The supplied metrics do not establish acceleration, thin buyers or non-delivery.

First inspect the three disputes, verify fulfillment on those orders and a recent sample, and reconcile refund requests with recorded refunds. Corroborated non-delivery alongside coordinated buyer activity or settlement extraction would strengthen bust-out and support a settlement pause. Verified delivery, isolated or invalid disputes, and a documented campaign matching sales would weaken it. Reconciled source records showing an incorrect rate would dismiss the reported breach. Zero recorded refunds alone does not clear the merchant. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records for reason codes, underlying orders, duplicate cases and supporting evidence; verify the reported 3/93 calculation.; Check delivery evidence for disputed orders and a small sample of recent orders, including carrier acceptance, delivery confirmation and unresolved customer complaints.; Reconcile zero recorded refunds against refund requests, cancellations, support tickets and processor records; distinguish no requests from unprocessed or missing refunds.; Request campaign dates, channels and promotion details, then compare them with daily sales and verified fulfillment.; Check event completeness and merchant-ID mapping, and clarify what 'new' GMV measures before interpreting it as buyer-account risk.

## Merchant 59 — alert episode 2024-02-17
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (3 disputes / 110 orders)
**Recommended action: monitor**

As of 2024-02-17, merchant 59 triggered a chargeback breach: 3 disputes across 110 trailing-30-day orders (2.73%). GMV was 777,871 cents; new GMV share was 31.66%. Recorded refunds were zero, which does not establish successful delivery.

Trading history is limited to 47 days despite merchant age of 782 days. Volume z-score, ticket drift, and baseline refund rate are null; acceleration and refund deterioration cannot be assessed from these comparisons.

Recommend monitor while promptly reviewing dispute reasons, delivery evidence, overdue orders, refund requests, and source-record completeness. Bust-out is uncorroborated. Ordinary category disputes, campaign activity, or a reporting defect remain possible explanations.

Verified non-delivery across recent orders, unresolved refund requests, and concentrated thin-account purchases tied to accelerated settlements would strengthen the alert and support reserve or reversible payout suspension. Documented fulfillment, ordinary dispute causes, campaign-linked sales, or corrected reporting would weaken it. A human owns any action; offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records: unique IDs, linked orders, reasons, dates, status, and delivery evidence. Repeated non-delivery would strengthen concern; duplicates or documented fulfillment would weaken it.; Check fulfillment for disputed orders and a small sample of recent orders using promised delivery dates, tracking, and delivery confirmation. Verify any overdue backlog.; Reconcile refund requests, pending refunds, and processor records against the reported zero completed refunds. Unprocessed requests alongside non-delivery would strengthen concern.; Reconcile the 110 orders and three disputes to source records, checking ingestion gaps and window definitions.; Request dated sales-campaign records and category benchmarks; link campaign-driven orders to fulfillment. If concerns persist, inspect buyer-account depth, concentration, and settlement timing.

## Merchant 118 — alert episode 2024-02-21
Triggers: AUP-06.1 breach: 30d chargeback rate 3.3% (3 disputes / 91 orders)
**Recommended action: reserve**

As of 2024-02-21, merchant 118 breached the chargeback trigger: 3 disputes across 91 trailing-30-day orders (3.3%). GMV was 684,090 cents; new-buyer GMV share was 31.7%. Recorded refunds were zero. Transaction history spans 51 days, with only 22 baseline days. Null volume and ticket comparisons cannot establish a spike or dismiss risk.

Recommend a reserve, with the payout percentage set by the human risk owner under applicable policy, while promptly reviewing the three disputes and fulfillment evidence. The breach supports investigation; bust-out remains uncorroborated.

Confirm concern through verified overdue non-delivery, coordinated thin buyer accounts, settlement extraction or unresolved customer complaints. Weaken or dismiss it through accurate dispute reconciliation, verified delivery and campaign records that explain buyer activity. Check pending refund requests alongside completed refunds. Correct source-data errors and reassess if found. Escalate to a reversible settlement pause if corroborated fulfillment failures indicate continuing exposure; offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records, reason codes and original orders; verify unique cases, event dates and the 91-order denominator against source records.; Check promised delivery dates and carrier delivery evidence for disputed orders plus a small sample of recent orders. Widespread overdue, undelivered orders would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations, pending refunds and completed refunds. Zero recorded refunds does not establish that customers received goods or requested no refunds.; Request dated campaign or promotion records and compare them with daily order and new-buyer activity. Matching campaigns with verified fulfillment would support a benign explanation.; Check buyer-account history and concentration, recent settlements and merchant responsiveness. Coordinated thin accounts, extracted payouts and corroborated non-delivery would strengthen the bust-out hypothesis.

## Merchant 96 — alert episode 2024-02-23
Triggers: AUP-06.1 breach: 30d chargeback rate 5.8% (3 disputes / 52 orders)
**Recommended action: reserve**

Merchant 96 breached the reported chargeback threshold: 3 disputes across 52 orders, or 5.8%, as of February 23. Trailing GMV was 544,894 cents; refunds were zero. Volume and ticket comparisons are unavailable, so neither acceleration nor stable behavior is established.

Recommend a provisional percentage reserve, with the percentage set by the human reviewer under portfolio policy, while completing prompt checks. The dispute exposure supports caution; bust-out remains uncorroborated.

First reconcile dispute reasons, unique records and the order denominator. Check fulfillment, promised delivery dates, refund requests and processor refunds. Obtain dated campaign evidence.

Verified non-delivery combined with coordinated buyer activity and payout extraction would strengthen bust-out concern and support escalation. Valid delivery evidence, resolved disputes and documented campaigns would weaken that hypothesis. Duplicate disputes or missing orders could invalidate the reported breach. Offboarding requires corroborated bust-out evidence; the current metrics alone do not justify it.

Evidence gaps: Reconcile the three disputes against processor records: unique order IDs, reasons, status and correct window; verify the 52-order denominator and ingestion completeness.; Inspect fulfillment and delivery evidence for disputed orders and a small recent-order sample, including promised delivery dates and customer complaints.; Check refund requests, pending refunds and processor refund records against the reported zero completed refunds.; Request dated campaign records and promotion-linked orders; check category seasonality if readily available.; If non-delivery is corroborated, inspect buyer-account linkage and settlement records for coordinated purchases and payout extraction.

## Merchant 3 — alert episode 2024-03-12
Triggers: AUP-06.1 breach: 30d chargeback rate 4.9% (3 disputes / 61 orders)
**Recommended action: reserve**

As of March 12, merchant 3 triggered AUP-06.1: three disputes across 61 trailing-30-day orders, a 4.9% reported rate. GMV was 351,336 cents; new-customer GMV share was 32.7%. Volume z-score was 1.015 and ticket drift 1.088, offering limited evidence of a pronounced ramp. The baseline covers only 42 days, and transaction history spans 71 days.

Bust-out remains uncorroborated. Zero recorded refunds does not establish successful delivery. A campaign could explain some sales changes, while a recording error could materially affect this small dispute count.

Recommend a temporary reserve, with the percentage set by the human reviewer based on exposure, pending prompt verification. Reconcile all three disputes, inspect delivery promises and fulfillment evidence, check refund requests against processor records, and obtain campaign dates. Repeated overdue non-delivery combined with coordinated thin-account purchases or payout extraction would strengthen the concern. Verified fulfillment, reconciled refunds and a documented campaign would weaken the bust-out hypothesis; corrected dispute records could dismiss the rate alert. These metrics alone do not justify offboarding.

Evidence gaps: Review the three dispute records for unique IDs, reasons, transaction dates and status; reconcile the numerator and 61-order denominator with source records.; Check promised delivery dates and carrier or service-completion evidence for disputed orders, then sample recent orders. Repeated overdue, unfulfilled orders would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile refund requests, pending refunds and completed refunds against processor records; determine whether the reported zero reflects accurate capture or missing events.; Request dated campaign records and compare promoted products and orders with the sales changes; a matching campaign plus verified delivery would support a benign explanation.; Review new-buyer account quality and settlement history for coordinated purchasing or accelerated payout extraction; new-customer share alone does not establish thin accounts.

## Merchant 12 — alert episode 2024-03-14
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (3 disputes / 113 orders)
**Recommended action: reserve**

As of March 14, merchant 12 triggered AUP-06.1: three disputes across 113 trailing-30-day orders, a 2.65% chargeback rate. GMV was 2,079,389 cents; volume_z was 2.33 and ticket_drift was 1.015. Recorded refunds were zero. The comparison baseline covers only 44 days, and observed order history spans 73 days despite a merchant age of 1,288 days.

These facts warrant review but do not establish bust-out. A marketing push could explain the volume signal; missing records could distort the metrics. Zero recorded refunds do not establish successful fulfillment.

Recommend a temporary percentage reserve, with the human reviewer setting its size against unresolved fulfillment exposure. Review the three disputes, delivery promises and tracking, refund requests, campaign dates, and source-data completeness. Repeated overdue non-delivery with corroborating dispute and refund records would strengthen bust-out concerns and support pausing settlement. Verified delivery and a documented campaign, or corrected data that removes the breach, would weaken or dismiss the alert and support returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: reasons, underlying orders, duplicates, status, and merchant responses. Verified non-delivery would strengthen the alert; unrelated or incorrectly recorded disputes would weaken it.; Check promised delivery dates and carrier delivery evidence for disputed orders and a small recent-order sample; seek buyer confirmation where records conflict. Repeated overdue, undelivered orders would support escalation.; Reconcile refund and cancellation requests with the merchant ledger and platform ingestion. Unresolved non-delivery refunds would increase concern; complete records would help validate the reported zeros.; Request dated campaign records and compare campaign timing with order growth and fulfillment. Documented promotion plus successful delivery would support a benign explanation.; Reconcile the 113-order denominator and dispute numerator against source records, and check ingestion completeness. Corrected metrics below the trigger would support dismissing the metric alert.

## Merchant 62 — alert episode 2024-03-16
Triggers: AUP-06.1 breach: 30d chargeback rate 3.4% (3 disputes / 87 orders)
**Recommended action: reserve**

Merchant 62 breached the chargeback trigger: 3 disputes across 87 trailing-30-day orders (3.45%). GMV was 1,038,451 cents. Volume_z was -0.439 and ticket_drift was 0.993, so the supplied comparisons do not show a sales ramp or larger tickets. New-GMV share was 39.61%; this does not establish thin buyer accounts. No refunds were recorded. Comparison history covers 46 baseline days.

Recommend a temporary payout reserve while the human reviewer verifies the breach and fulfillment. The dispute count warrants review, but bust-out is uncorroborated; these metrics do not justify offboarding.

Start with the three dispute records and their delivery evidence. Repeated verified non-delivery, linked thin buyer accounts and unresolved refund requests would strengthen bust-out concern. Valid delivery evidence and ordinary complaint reasons would weaken it. Duplicate disputes or missing denominator orders could invalidate the alert. Reconcile refund requests against recorded refunds, and check dated campaign records and category dispute benchmarks. A campaign explanation requires evidence of fulfilled sales; it does not erase a valid chargeback breach. Reassess the reserve after these checks and watch the next window.

Evidence gaps: Inspect the three dispute records for unique transaction IDs, reasons, dates, status and links to the 87 orders; reconcile against source records to confirm or invalidate the breach.; Check fulfillment evidence for disputed orders first, then a small sample of recent orders: shipment tracking, delivery confirmation or service completion. Repeated verified non-delivery would strengthen bust-out concern.; Reconcile refund requests, cancellations and pending refunds with the zero recorded refunds; distinguish absent requests from unprocessed or missing refunds.; Obtain dated campaign records and compare promoted orders with fulfillment and disputes; fulfilled campaign sales would support a benign explanation.; Compare historical and category dispute rates, and inspect buyer-account age and repeated buyer/payment links; establish whether complaint levels and buyer concentration are unusual.

## Merchant 1 — alert episode 2024-03-18
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (3 disputes / 103 orders)
**Recommended action: reserve**

As of 2024-03-18, merchant 1 triggered AUP-06.1: three disputes across 103 trailing-30-day orders, a 2.91% chargeback rate. Reported GMV was 1,050,174 cents; refunds were zero. Volume_z was 0.688, which does not establish a pronounced sales ramp. Although the merchant is 1,375 days old, observed order history spans 77 days and the baseline contains 48 days.

The breach warrants review, but these facts do not corroborate bust-out. Recommend a temporary payout reserve, with the percentage and release conditions set by the human owner while checks proceed.

First inspect all three disputes, delivery evidence and refund records, then reconcile source feeds. Check campaign timing and recent-order fulfillment. Repeated verified non-delivery alongside suspicious sales or buyer patterns would strengthen bust-out concerns and support pausing settlement. Verified fulfillment, resolved or erroneous disputes, and a documented campaign would weaken them and support monitoring. Zero recorded refunds do not prove fulfillment. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reason, status, duplicate entries, merchant attribution and supporting fulfillment evidence.; Check delivery evidence for disputed orders and a small sample of recent orders, including tracking, promised delivery dates and existing buyer confirmations.; Reconcile reported zero refunds against refund requests, pending refunds and processor records; verify order and dispute feed completeness.; Review existing campaign and seasonal calendars, and compare sales timing and buyer mix with the claimed promotion.

## Merchant 43 — alert episode 2024-04-03
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: monitor**

As of April 3, merchant 43 triggered volume and new-account-share alerts: volume_z is 3.1092 and new-account GMV share is 48.33%. Trailing 30-day GMV is $1,941.62 across 29 orders; ticket_drift is 1.5382. The baseline contains 35 orders across 64 days, limiting confidence in the comparison.

Bust-out is plausible but uncorroborated. Zero recorded refunds and disputes do not establish successful fulfillment. Merchant age of 1,026 days also should not substitute for transaction history: the first order was 93 days ago.

Recommend monitoring the next window while promptly checking source-data completeness, recent fulfillment, refund requests, dispute records and campaign activity. Verified deliveries and campaign-aligned acquisition would support dismissing the alert; a corrected pipeline could also resolve it. Coordinated buyer activity combined with overdue non-delivery or unresolved customer claims would strengthen the case for a reserve or reversible settlement pause. Current evidence does not support offboarding. A human owns the action.

Evidence gaps: Reconcile order, GMV and account-creation records against source transactions; check baseline completeness, duplicates and classification errors, then recompute the triggers.; Sample recent high-value and new-account orders for promised delivery dates, shipment tracking and delivery confirmation; verify whether overdue orders remain unfulfilled.; Reconcile the reported zero refunds and disputes with payment records, refund requests, pending refunds, dispute records and support complaints.; Request campaign dates, spend, acquisition channels and promotion terms; compare them with order timing and new-account purchases.; Check whether new buyers share payment, device or delivery identifiers. Corroborated coordination plus overdue non-delivery would strengthen bust-out concerns; verified deliveries and campaign-attributable growth would weaken them.

## Merchant 132 — alert episode 2024-04-08
Triggers: AUP-06.2: volume z=7.5 vs baseline; AUP-06.4: new-account GMV share 71%
**Recommended action: reserve**

As of 2024-04-08, merchant 132 triggered volume and new-account concentration alerts: volume_z is 7.49 and new accounts represent 70.92% of trailing GMV. The 30-day window contains 44 orders and $15,096.76 GMV. The baseline contains only 20 orders across 40 days, limiting confidence in the comparison. Reported refunds and disputes are both zero; this does not verify delivery or eliminate risk.

Recommend holding a percentage of payouts through a reserve while conducting a targeted review; a human owns the decision. Bust-out is plausible but uncorroborated. A marketing campaign or seasonal demand could explain the growth.

Prioritize sampled fulfillment evidence, outstanding refund requests, underlying dispute records, campaign documentation and source-data reconciliation. Repeated overdue nondelivery with coordinated buyers would strengthen the bust-out hypothesis. Verified deliveries and campaign-linked acquisition would support returning to monitoring; corrected data that removes the triggers would support dismissing the alert. Escalate to a reversible settlement pause if corroborated fulfillment failures justify it. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Sample recent orders, emphasizing new-account GMV: verify promised delivery dates, carrier acceptance and delivery evidence, and buyer receipt. Repeated overdue nondelivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations and merchant refund records with reported zero refunds; check unresolved requests and processing failures.; Inspect underlying dispute records and buyer complaints, including order and filing dates; verify ingestion completeness. Zero reported disputes alone does not dismiss the alert.; Request dated campaign records and compare acquisition channels, promotion timing and resulting orders. A documented campaign with fulfilled orders would support a benign explanation.; Recompute trailing totals, new-account classification and baseline statistics from source orders; check completeness and duplicates. A corrected calculation that removes the triggers would support dismissing the alert.; Check sampled new buyers for shared identifiers or coordinated purchasing; new-account status alone does not establish thin or linked accounts.

## Merchant 4 — alert episode 2024-04-11
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 41%
**Recommended action: reserve**

As of April 11, merchant 4 triggered elevated volume (z=3.05) and new-account GMV share of 41.0%. Trailing 30-day GMV was 2,480,666 cents across 52 orders; baseline GMV was 4,195,354 cents across 82 orders and 72 days. Recorded trailing refunds and disputes were both zero.

These facts warrant review but do not establish bust-out. A marketing campaign could explain the sales increase and new buyers; seasonal demand and pipeline errors remain unverified alternatives. New-account status alone does not establish weak buyer accounts, and recorded zeros do not verify fulfillment.

Recommend a temporary percentage reserve, with the percentage set by the human risk owner, while conducting focused checks. Reconcile source totals and account classification; sample delivery evidence against promised dates; inspect refund requests and dispute records; and match sales to campaign activity. Repeated overdue non-delivery coupled with settlement extraction would strengthen bust-out concern and support pausing payouts. Verified fulfillment and attributable campaign sales, or corrected data that removes the triggers, would support releasing the reserve and monitoring the next window. Current evidence does not support offboarding.

Evidence gaps: Reconcile daily order and GMV totals against source records, check baseline completeness, and verify new-account classification. Corrected metrics below trigger thresholds would dismiss the corresponding alert signals.; Sample recent orders, prioritizing new-account and high-value purchases; compare promised delivery dates with carrier acceptance, delivery proof, and customer contacts. Repeated overdue, unfulfilled orders would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations, processed refunds, and dispute records to these orders. Verify the recorded zeros and examine complaint reasons; non-delivery complaints would corroborate concern.; Request campaign dates and order attribution, plus any documented seasonal promotion. A matching sales increase with verified fulfillment would support a benign explanation.; Inspect settlement records alongside fulfillment exceptions for payout concentration or accelerated extraction. Corroborated extraction and non-delivery would support escalation.

## Merchant 14 — alert episode 2024-04-13
Triggers: AUP-06.1 breach: 30d chargeback rate 2.8% (4 disputes / 142 orders)
**Recommended action: reserve**

Merchant 14 triggered AUP-06.1 on April 13, 2024: four disputes across 142 trailing-30-day orders, a reported rate of 2.8%. GMV was 7,287,972 cents. Volume_z was 0.60, ticket_drift was 0.95, and new_gmv_share was 22.3%. These metrics do not establish a pronounced sales ramp. Zero recorded refunds does not demonstrate successful fulfillment.

Recommend a temporary reserve at a human-approved payout percentage while reviewing the four disputes and recent fulfillment. Bust-out is currently a low-likelihood hypothesis; campaign, seasonal and data explanations remain unverified.

First reconcile dispute and order records, inspect dispute reasons, verify delivery against promised dates, and check pending refunds. Obtain campaign records and relevant seasonal context. Corroborated non-delivery, linked thin buyers and continued settlement extraction would strengthen the bust-out hypothesis and support considering a settlement pause. Verified delivery, resolved disputes, documented benign sales drivers or corrected source-data errors would weaken the alert and support releasing the reserve. Offboarding is unsupported by the supplied evidence.

Evidence gaps: Reconcile the four dispute records and 142 orders with source systems; check duplicates, event dates and ingestion completeness.; Read dispute reasons, statuses and merchant responses; determine whether complaints concern non-delivery, unauthorized purchases or another cause.; Check delivery evidence for disputed orders and a small sample of recent orders, including promised delivery dates and overdue fulfillment.; Inspect pending refund requests, cancellations and refund-processing records; zero recorded refunds does not establish that customers received goods.; Request dated campaign records and category-specific seasonal context; compare associated sales and fulfillment with the alert window.; Check whether buyer accounts are thin or linked; the supplied new_gmv_share alone does not establish either condition.

## Merchant 98 — alert episode 2024-04-14
Triggers: AUP-06.1 breach: 30d chargeback rate 6.0% (3 disputes / 50 orders)
**Recommended action: reserve**

As of 2024-04-14, merchant 98 breached the chargeback trigger: 3 disputes across 50 trailing-30-day orders (6.0%). GMV was 618,628 cents. Volume z-score was 1.04 and ticket drift was 0.837, providing limited support for a bust-out ramp. New buyers accounted for 25.98% of GMV; this does not establish thin accounts. Zero recorded refunds does not clear fulfillment risk. The baseline contains 74 days.

Recommend a temporary percentage reserve, with the percentage set by the human reviewer under applicable policy, while checking disputes, delivery evidence, refund requests, campaign records and feed completeness. The small order count makes individual cases consequential.

Verified repeated non-delivery, unresolved refunds and concentrated thin-account sales would strengthen the bust-out hypothesis and support pausing settlement. Valid delivery evidence, resolved disputes, a documented campaign or corrected records would weaken the alert and support monitoring. Offboarding requires corroborated bust-out evidence. The human reviewer owns the action.

Evidence gaps: Inspect the three dispute records: verify unique cases, linked orders, reasons, status and supporting evidence. Repeated non-delivery would strengthen concern; duplicates or documented delivery could weaken it.; Check tracking and delivery evidence for disputed orders and a small recent-order sample, plus outstanding fulfillment obligations. Broad non-fulfillment would support pausing settlement.; Reconcile the zero recorded refunds against refund requests, cancellations and processor records; determine whether unresolved requests are accumulating.; Check campaign dates, promotion terms and attributed orders. Verified campaign-driven sales with documented fulfillment would support a benign explanation.; Reconcile the 50-order denominator and dispute feed through the alert date; confirm window definitions and completeness. Review available buyer-account history for concentration or thin accounts without treating new-GMV share as proof.

## Merchant 73 — alert episode 2024-04-22
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (5 disputes / 186 orders)
**Recommended action: reserve**

Merchant 73 triggered AUP-06.1 on April 22: five disputes across 186 trailing-30-day orders, a 2.69% rate. Recorded refunds are zero. Volume_z is 0.50 and ticket_drift is 0.933; these do not show a pronounced ramp. New GMV represents 25.67% of GMV, without a supplied comparison establishing an increase.

Bust-out is uncorroborated. Recommend a temporary reserve, with the percentage set by the human reviewer, while resolving the dispute and fulfillment evidence. The breach creates payout exposure, but the supplied facts do not justify stopping settlement or terminating the merchant.

First inspect all five disputes and their delivery evidence, reconcile dispute/order/refund feeds, and check refund requests and campaign records. Repeated verified non-delivery combined with thin-account concentration and settlement extraction would support escalation. Verified fulfillment, explained complaints, completed refunds or corrected source records would weaken the alert and support releasing the reserve. A campaign explanation requires corroboration.

Evidence gaps: Review the five dispute records for reasons, status, linked orders and duplicates; reconcile their inclusion and the 186-order denominator against source records as of 2024-04-22.; Check delivery or service-completion evidence for disputed orders and a small sample of recent orders. Repeated confirmed non-delivery would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile the zero recorded refunds with refund requests, cancellations, support tickets and payment-ledger entries to distinguish no refunds from an incomplete feed or unprocessed requests.; Request the campaign calendar and associated order cohorts; compare promised delivery dates with actual fulfillment to test a benign campaign explanation.; Inspect recent buyer-account histories and payout records for concentrated purchases by thin accounts and settlement extraction; the supplied new-GMV share alone does not establish either.

## Merchant 34 — alert episode 2024-04-23
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (3 disputes / 114 orders)
**Recommended action: monitor**

Merchant 34 triggered AUP-06.1 on April 23: three disputes across 114 trailing-30-day orders, a 2.63% chargeback rate. GMV was 5,851,546 cents. Volume z-score was 0.346; ticket drift was 1.101. These observations do not establish a pronounced sales ramp. New GMV share was 23.21%, which does not itself establish thin buyer accounts. Recorded refunds were zero, but that does not establish successful fulfillment.

Recommend monitoring the next window while promptly reviewing the three disputes, delivery evidence, refund requests and campaign records. Validate dispute uniqueness and denominator completeness, and reconcile the daily and trailing dispute counts by reporting scope.

Repeated non-delivery combined with concentrated thin-account purchases and settlement extraction would support bust-out and justify considering a settlement pause. Verified fulfillment, resolved disputes, documented campaign attribution or a corrected data error removing the breach would weaken the alert. Current evidence does not support irreversible offboarding. A human owns the action.

Evidence gaps: Review the three dispute records: reason codes, linked orders, status and supporting evidence; reconcile n_disputes of 2 with disputes_30d of 3 using their defined reporting scopes.; Check delivery or service-completion evidence for disputed orders and a small sample of recent orders; repeated non-delivery would strengthen the bust-out hypothesis, while verified fulfillment would weaken it.; Reconcile zero recorded refunds against refund requests, cancellations, processor records and pending refunds; identify unresolved customer claims or ingestion omissions.; Ask for recent campaign dates and attributed sales, and validate order/dispute ingestion completeness; documented campaigns with fulfilled orders or corrected records removing the breach would weaken the alert.; Inspect buyer-account history and concentration for recent orders; new_gmv_share alone does not establish thin accounts or coordinated purchasing.

## Merchant 106 — alert episode 2024-05-03
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (5 disputes / 186 orders)
**Recommended action: reserve**

Merchant 106 triggered AUP-06.1 on 2024-05-03: five disputes across 186 trailing-30-day orders, a 2.688% rate. GMV was 1,175,630 cents; volume_z was 1.914 and ticket_drift was 1.054. Recorded refunds were zero, which does not establish successful fulfillment.

The breach warrants a temporary payout reserve at a human-approved percentage while records are checked. Current evidence does not corroborate bust-out or justify termination. A marketing push remains possible; campaign attribution is unavailable.

First reconcile the five disputes, order denominator, and refund feed. Review dispute reasons and statuses, promised delivery dates, tracking, and unresolved customer requests. Verify campaigns and buyer-account concentration.

Verified overdue non-delivery combined with concentrated thin accounts and settlement extraction would support escalation to a reversible settlement pause. Consistent delivery, explainable dispute records, and campaign-attributed sales would weaken the bust-out interpretation. Corrected source data could invalidate the numerical alert; benign sales alone would not erase a valid breach. The portfolio-risk owner decides the action.

Evidence gaps: Inspect all five processor dispute records for unique transaction IDs, reasons, status, and supporting evidence; reconcile the 186-order denominator and event ingestion.; Check promised delivery dates, tracking, delivery confirmation, and customer contacts for disputed orders and a small sample of recent orders. Verified overdue non-delivery would support escalation; consistent fulfillment would weaken bust-out.; Reconcile the zero recorded refunds with processor refunds, cancellations, and pending refund requests; determine whether events are missing or customers remain unresolved.; Check campaign dates and attributable orders, and compare buyer-account history and concentration with baseline. A documented campaign with fulfilled orders would support a benign explanation; concentrated thin accounts with non-delivery would strengthen bust-out.; If fulfillment concerns are verified, compare settlement timing and payout-account changes with the sales increase before considering further action.

## Merchant 56 — alert episode 2024-05-06
Triggers: AUP-06.1 breach: 30d chargeback rate 6.1% (3 disputes / 49 orders)
**Recommended action: reserve**

As of May 6, merchant 56 triggered AUP-06.1 with three disputes across 49 trailing-30-day orders (6.1%). GMV was 2,407,189 cents. Volume_z was −1.54, ticket_drift was 0.986, and new-buyer GMV share was 22.0%. These observations do not establish the sales ramp expected in a bust-out. Zero recorded refunds does not establish satisfactory fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer against outstanding delivery exposure. The dispute breach warrants protection while evidence is gathered; bust-out is uncorroborated.

First reconcile the three disputes and order denominator, inspect dispute reasons and delivery proof, and check pending refunds against source records. Verify campaign timing and buyer-account history. Repeated overdue non-delivery, thin-account concentration and settlement extraction would strengthen the bust-out hypothesis and support pausing settlement. Verified fulfillment, isolated disputes, or a corrected pipeline error would weaken it and support returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes to unique orders and processor records; inspect reason codes, status and fulfillment evidence, and verify the 49-order denominator.; Check promised delivery dates and carrier scans or service-completion records for disputed orders and a small sample of recent orders; look for repeated overdue non-delivery.; Compare refund requests and pending or rejected refunds with payment records; verify that zero recorded refunds reflects complete ingestion.; Request campaign dates, channels and promotions, and compare affected orders with the merchant's historical category and seasonal patterns.; Inspect existing buyer-account history for recent and disputed orders, and compare settlement receipts with outstanding fulfillment obligations.

## Merchant 65 — alert episode 2024-05-21
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: reserve**

As of 2024-05-21, merchant 65 triggered volume and new-account-share alerts. Observed volume z is 3.07; new accounts contributed 48.07% of trailing-30-day GMV. That window contains 54 orders and 1,230,039 cents in GMV, with ticket drift of 1.397. Recorded refunds and disputes are both zero; those counts do not establish successful fulfillment.

Bust-out is plausible but uncorroborated. Customer acquisition or seasonal demand could explain growth, and source-data errors remain possible.

Recommend a temporary payout reserve, with the percentage determined by the human reviewer using unsettled exposure and delivery obligations. Prioritize sampled delivery verification, pending refund requests, processor disputes and campaign records, alongside source-data reconciliation.

Confirmed overdue non-delivery, coordinated buyer activity and settlement extraction would strengthen the alert and support considering a settlement pause. Verified deliveries and a documented campaign, or a corrected data defect that removes the triggers, would support returning to monitoring. Offboarding requires corroborated bust-out evidence. The human reviewer owns the action.

Evidence gaps: Sample recent high-value and new-account orders for promised delivery dates, carrier acceptance and delivery confirmation; contact sampled buyers where records are inconclusive. Confirmed overdue non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations and pending refunds against processed refund records. The reported zero refunds does not establish that no customers requested refunds.; Check processor dispute records and customer complaints against the platform's zero-dispute count, matching records to order dates and fulfillment status without assuming a dispute-lag interval.; Request campaign dates, spend, promotions and acquisition-channel records; compare them with the sales increase and new-account orders. A documented campaign with fulfilled orders would support a benign explanation.; Reconcile daily order counts and GMV cents to source transactions, checking baseline completeness, duplicates and the new-account definition; inspect available buyer-account history and links for concentration or coordination.

## Merchant 40 — alert episode 2024-05-25
Triggers: AUP-06.1 breach: 30d chargeback rate 4.1% (3 disputes / 74 orders)
**Recommended action: reserve**

As of May 25, merchant 40 triggered AUP-06.1: three disputes across 74 trailing-30-day orders, a 4.05% chargeback rate. GMV was 1,560,445 cents. volume_z was −1.46 and ticket_drift was 0.986; these comparisons do not show a sales or ticket ramp. new_gmv_share was 19.09%, with no supplied comparison establishing unusual buyer mix. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary reserve at a human-selected payout percentage while completing prompt checks. The breach supports payout protection, but the supplied evidence does not corroborate bust-out or justify termination.

Inspect dispute reasons and transaction links, verify delivery for disputed and recent orders, and reconcile refund requests with processed refunds. Confirm order and dispute ingestion completeness. Request campaign and seasonal records tied to the affected dates.

Verified non-delivery concentrated among thin buyer accounts, alongside settlement extraction, would strengthen bust-out concern and support considering a settlement pause. Documented delivery and legitimate campaigns would weaken it; a reconciliation error that removes the breach could dismiss the alert. A human owns the action.

Evidence gaps: Inspect the three dispute records for reasons, status, duplicates, transaction links and dates; obtain baseline dispute counts to assess whether this is a change.; Check shipment tracking, delivery confirmation and overdue fulfillment for disputed orders and a small recent-order sample. Repeated verified non-delivery would strengthen bust-out concern; reliable delivery would weaken it.; Reconcile the 74 orders and three disputes against source records and check ingestion completeness, merchant attribution and window boundaries. Corrected counts could dismiss the reported breach.; Review refund requests, cancellations, pending refunds and processor records; determine whether zero recorded refunds reflects actual activity or missing/unprocessed refunds.; Request campaign dates, promotion details and comparable seasonal sales records; compare affected orders and buyer cohorts with those records. New-account share alone does not establish buyer thinness.

## Merchant 118 — alert episode 2024-06-03
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 118 orders)
**Recommended action: reserve**

As of 2024-06-03, merchant 118 triggered the supplied chargeback-policy breach: 3 disputes across 118 trailing-30-day orders, or 2.54%. GMV was 829,356 cents. Volume_z was 1.327, ticket_drift 0.971, and new-buyer GMV share 24.77%. No refunds were recorded.

These observations support investigating disputes; they do not establish bust-out. The metrics show no pronounced volume or ticket ramp, and new buyers are not necessarily thin accounts. Seasonal demand or a campaign remains possible but unverified. Zero refunds does not establish successful fulfillment.

Recommend a payout reserve under the applicable policy while a human reviews the three disputes, delivery evidence, outstanding refund requests and source-ledger completeness. Coordinate purchasing plus repeated overdue non-delivery would strengthen bust-out suspicion and support considering a settlement pause. Verified fulfillment, ordinary resolved disputes and a documented campaign would weaken that hypothesis; a reconciliation that removes the breach could dismiss the alert. Reassess the reserve promptly after these checks and monitor the next window.

Evidence gaps: Review all three dispute records: reason codes, linked orders, consumer allegations, status and duplicates. Determine whether they concern non-delivery, unauthorized purchases or other causes.; Check delivery evidence for disputed orders and sample recent new-buyer orders; compare promised delivery dates with carrier scans or service-completion records. Repeated overdue non-delivery would strengthen the alert.; Inspect refund requests, cancellations, promised refunds and payment records. Confirm whether zero recorded refunds reflects no requests or unprocessed/missing refunds.; Reconcile the 118 orders and three disputes against source ledgers, including ingestion completeness and window boundaries. A corrected rate could dismiss the metric breach.; Check campaign dates and seasonal sales records against order growth; inspect buyer-account history and shared identifiers for coordination. Verified campaigns with fulfilled orders would weaken bust-out suspicion.

## Merchant 62 — alert episode 2024-06-15
Triggers: AUP-06.1 breach: 30d chargeback rate 4.4% (4 disputes / 90 orders)
**Recommended action: reserve**

As of June 15, 2024, merchant 62 triggered AUP-06.1 with four disputes across 90 trailing-30-day orders (4.44%). GMV was 1,070,034 cents ($10,700.34). Volume_z was 0.385 and ticket_drift was 1.037; neither indicates a pronounced ramp. Reported refunds were zero, which does not establish successful fulfillment.

Recommend a temporary reserve, with its percentage set by the human reviewer after checking disputed amounts and outstanding fulfillment exposure. Current evidence supports investigating the chargeback breach, but does not corroborate bust-out.

First reconcile disputes and the order denominator, then inspect delivery evidence and refund records. Verified non-delivery across disputed and recent orders, especially alongside coordinated buyers and payout extraction, would strengthen bust-out and support pausing settlement pending review. Verified delivery, isolated dispute causes, or corrected records that remove the breach would support releasing the reserve and monitoring. Campaign records may explain buyer mix but must be checked alongside fulfillment. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the four disputes against processor records: unique identifiers, reasons, amounts, affected orders and status; verify the 90-order denominator and window attribution.; Check delivery evidence for all four disputed orders and a small sample of recent orders, including promised delivery dates, tracking and customer complaints.; Reconcile refund requests and completed refunds against customer-support, merchant and processor records; determine whether the reported zero reflects complete ingestion.; Obtain campaign dates and sales-channel records; compare associated orders' fulfillment and buyer-account characteristics.; If non-delivery is corroborated, examine settlement records and buyer-account links for coordinated ordering and payout extraction before escalating.

## Merchant 37 — alert episode 2024-06-16
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (4 disputes / 124 orders)
**Recommended action: reserve**

Merchant 37 breached the chargeback trigger: four disputes across 124 trailing-30-day orders (3.2%). GMV was 2,917,820 cents. Volume_z was -0.362 and ticket_drift 1.048, offering little support for a sales ramp. New GMV represented 33.1%; this does not establish thin buyer accounts. Zero recorded refunds does not establish successful fulfillment.

Recommend a payout reserve, with the percentage set by the human reviewer, while conducting targeted checks. The dispute signal warrants exposure control, but corroborated bust-out evidence is absent.

Review all four disputes, verify delivery for those orders and a small recent-order sample, reconcile refund requests against processor records, and validate source counts and ingestion. Obtain campaign records and inspect buyer concentration.

Confirmed non-delivery, overdue unfulfilled orders and linked thin-account purchasing would strengthen the bust-out hypothesis. Documented delivery, resolved disputes, a supported campaign explanation or a corrected rate below the trigger would weaken or dismiss the alert. Verified ongoing fulfillment failure could justify pausing settlement; offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the four dispute records: reason codes, linked orders, duplicate status, merchant responses and supporting delivery evidence. Verified non-delivery strengthens concern; duplicates or documented delivery weaken it.; Check tracking and delivery confirmation for disputed orders and a small sample of recent orders, distinguishing overdue shipments from orders still within promised delivery dates.; Compare refund requests, approvals and processor transactions with recorded refunds. Unresolved requests or missing ingestion would materially change the interpretation of zero recorded refunds.; Reconcile dispute and order counts against source records and check ingestion completeness through the alert date; recompute the chargeback rate if discrepancies appear.; Request campaign dates, promotion details and buyer-mix records. A documented campaign with successful fulfillment supports a benign explanation; linked thin accounts and concentrated purchasing strengthen bust-out concern.

## Merchant 136 — alert episode 2024-06-16
Triggers: AUP-06.2: volume z=10.1 vs baseline; AUP-06.4: new-account GMV share 82%
**Recommended action: reserve**

As of 2024-06-16, merchant 136 triggered AUP-06.2 and AUP-06.4: volume z=10.118 and new-account GMV share=81.93%. Trailing 30-day GMV was $18,757.60 across 51 orders. The baseline contains only 44 days and 20 orders; the merchant is 74 days old. Recorded 30-day refunds and disputes are both zero, which does not verify fulfillment.

A bust-out ramp is plausible but uncorroborated. A marketing campaign, seasonal demand or a pipeline defect could explain the alert.

Recommend a percentage reserve, with the amount set by the human reviewer under policy, while conducting prompt checks. First reconcile source transactions and account classification. Then sample recent orders for promised dates and verified delivery, reconcile refund requests and dispute records, and request campaign attribution.

Verified overdue non-delivery, fabricated tracking or coordinated buyers alongside settlement extraction would strengthen the case for pausing payouts. Corrected metrics or campaign-linked growth with verified delivery would support dismissing the alert and releasing the reserve. Current evidence does not support irreversible offboarding.

Evidence gaps: Reconcile baseline and recent order counts and GMV against source transactions; check missing ingestion dates, duplicates and new-account classification. Corrected metrics that remove the anomaly would dismiss the metric alert.; Sample recent high-value and new-account orders for promised delivery dates, carrier acceptance and delivered status; verify selected deliveries with buyers. Overdue non-delivery or fabricated tracking would strengthen the bust-out hypothesis.; Reconcile refund requests, cancellations and issued refunds with support and payment records; inspect available dispute records and complaints for non-delivery. Confirm whether reported zeros reflect complete records.; Request dated campaign records and order attribution, plus product-level seasonal context. A matching acquisition campaign or seasonal increase with verified fulfillment would support a benign explanation.; Review existing payout records and buyer-linkage indicators for rapid settlement extraction or coordinated purchasing; assess these alongside fulfillment evidence.

## Merchant 110 — alert episode 2024-06-17
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: reserve**

As of June 17, merchant 110 triggered volume and new-account concentration alerts. Trailing 30-day GMV was $7,376.56 across 79 orders; volume z was 3.07 and new accounts contributed 43.84% of GMV. The preceding 90 days contained 168 orders and $14,225.80 GMV. Ticket drift was 1.103. One dispute and zero refunds were recorded in the trailing window.

The pattern is compatible with bust-out, but does not establish coordinated buyers or nondelivery. A marketing campaign or seasonal demand could explain growth; a pipeline defect could distort the comparison. Zero refunds does not establish successful fulfillment.

Recommend a proportionate reserve, with the human reviewer setting the percentage after checking outstanding fulfillment exposure. Verify sampled deliveries, refund requests and processing, the dispute record, campaign dates, and transaction completeness. Repeated overdue nondelivery, fabricated tracking, and coordinated purchasing would strengthen bust-out concerns and support pausing settlement. Verified fulfillment with attributable campaign sales, or a reconciled data defect that removes the spike, would support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Sample recent orders, prioritizing high-value new-account purchases: check promised delivery dates, carrier acceptance, delivery evidence, cancellations, and customer complaints. Repeated overdue nondelivery or fabricated tracking would strengthen bust-out concerns; verified delivery would weaken them.; Reconcile refund requests, cancellations, and processed refunds against order and payment records. Determine whether zero recorded refunds reflects no requests or missing/unprocessed records.; Inspect the single dispute's reason, order date, fulfillment evidence, and status; reconcile dispute records available as of 2024-06-17. Do not treat the observed dispute rate as proof of fulfillment.; Request dated campaign, promotion, or seasonal-event records and compare attributable sales and customer acquisition with the spike.; Reconcile baseline and trailing-window orders and GMV with source transactions; check ingestion completeness, duplicates, window boundaries, and new-account classification.; Review available buyer-account history and links among sampled orders for coordinated purchasing, and inspect outstanding unfulfilled order value to size any reserve.

## Merchant 1 — alert episode 2024-06-18
Triggers: AUP-06.1 breach: 30d chargeback rate 3.4% (3 disputes / 88 orders)
**Recommended action: reserve**

The alert reports an AUP-06.1 chargeback-rate breach: 3 disputes across 88 trailing-30-day orders (3.4%). GMV was 1,078,976 cents, volume_z was -1.32, and ticket_drift was 1.105. New GMV represented 22.2% of GMV. No refunds were recorded.

These facts warrant review but do not establish bust-out. Volume does not show the expected ramp, and fulfillment failure, thin-account concentration and settlement extraction remain unverified. Zero recorded refunds does not demonstrate successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer under applicable policy. First inspect the three disputes, verify delivery for disputed and sampled recent orders, and reconcile refund requests and source-system counts. Check campaign and seasonal records for a supported benign explanation.

Verified non-delivery combined with thin-account purchases and settlement extraction would strengthen bust-out concern and support pausing settlement. Verified fulfillment and explained disputes would weaken it; corrected records eliminating the breach would dismiss this trigger. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: reason codes, order links, status, duplicates and supporting evidence. Non-delivery findings would strengthen concern; unrelated or erroneous records would weaken it.; Check tracking and delivery evidence for disputed orders and a small sample of recent orders, alongside overdue fulfillment and customer complaints.; Reconcile refund requests and pending refunds with processor records; zero recorded refunds does not establish that customers received their goods.; Reconcile the 88-order denominator and dispute numerator with source systems and ingestion logs to identify missing orders or duplicated disputes.; Review dated campaign records and historical seasonal sales, then compare affected orders' fulfillment and disputes.; Check buyer-account history and payout records for concentrated thin-account purchases followed by settlement extraction.

## Merchant 49 — alert episode 2024-06-19
Triggers: AUP-06.1 breach: 30d chargeback rate 3.4% (3 disputes / 88 orders)
**Recommended action: monitor**

Merchant 49 breached the chargeback-rate trigger as of June 19: three disputes across 88 trailing-30-day orders, or 3.41%. This is an observed dispute signal, not corroborated bust-out evidence. Volume_z is −0.465 and ticket_drift is 1.028, providing no evidence of a sales ramp. Zero recorded refunds does not establish successful delivery.

Recommend monitor and review the three disputes promptly. Verify fulfillment against promised dates, inspect refund requests and complaints, and reconcile source records. Request campaign details to assess a benign explanation.

Repeated non-delivery, corroborated thin-account concentration, and settlement extraction would strengthen the bust-out hypothesis and support reserve or a reversible settlement pause. Verified delivery, resolved disputes, or a corrected denominator would weaken the alert. Check the next window for persistence. Offboarding requires corroborated bust-out evidence; a human owns the action.

Evidence gaps: Inspect the three dispute records for reasons, affected orders, duplicate entries, status, and any fulfillment evidence.; Check carrier acceptance and delivery records for disputed orders and a small sample of recent orders; compare promised delivery dates with actual fulfillment.; Reconcile order, dispute, and refund counts against source systems; inspect pending refund requests and customer complaints despite zero recorded refunds.; Ask for the campaign calendar and promotion records, and compare order composition with prior seasonal periods if available.; Check available buyer-account history and payout records for concentrated thin accounts and settlement extraction.

## Merchant 82 — alert episode 2024-06-25
Triggers: AUP-06.1 breach: 30d chargeback rate 5.6% (3 disputes / 54 orders); AUP-06.4: new-account GMV share 56%
**Recommended action: reserve**

As of June 25, merchant 82 triggered alerts for a 5.6% dispute rate (3/54 orders) and 55.8% new-account GMV share. Thirty-day GMV was $30,608.09, including $17,066.35 from new accounts. Volume z-score was 1.16 and ticket drift 1.126; these do not establish a sharp sales ramp. Recorded refunds were zero.

Recommend a proportionate payout reserve while the human reviewer checks the underlying evidence. The combination warrants exposure control, but bust-out is unconfirmed. A marketing campaign could explain buyer acquisition; new accounts do not establish thin or coordinated buyers.

First inspect dispute reasons and delivery evidence, sample recent high-value new-account fulfillment, and reconcile refunds and pending requests. Obtain dated campaign records and verify aggregate completeness and account classification.

Repeated non-delivery, coordinated buyers and settlement extraction would corroborate bust-out and support considering a reversible settlement pause. Verified fulfillment plus documented acquisition activity, or a reconciled data error removing the triggers, would support dismissing the alert and releasing the reserve. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: reasons, status, underlying order dates, delivery evidence and any duplication. Confirm the reported rate uses the intended numerator and denominator.; Check fulfillment for disputed orders and a small sample of recent high-value new-account orders using carrier acceptance, delivery scans or service-completion evidence.; Reconcile refunds, cancellations and pending refund requests against processor and support records; zero recorded refunds does not establish successful delivery.; Request dated campaign records, promotion terms and acquisition-source data; compare campaign orders with the new-account sales concentration and fulfillment results.; Reconcile daily order, dispute and buyer-account records with the aggregates, checking ingestion completeness and new-account classification; inspect existing buyer-linkage and settlement records for coordination and payout extraction.

## Merchant 104 — alert episode 2024-07-01
Triggers: AUP-06.1 breach: 30d chargeback rate 7.7% (3 disputes / 39 orders)
**Recommended action: reserve**

As of July 1, merchant 104 triggered AUP-06.1: three disputes across 39 trailing-30-day orders (7.7%). GMV was 261,934 cents. Volume_z was 0.1622, ticket_drift 1.0962, and new_gmv_share 15.1%. Recorded refunds were zero; this does not establish successful delivery.

Bust-out remains plausible but uncorroborated. The metrics provide little evidence of a sales ramp, and neither thin buyer accounts nor non-delivery is established. A campaign or reporting error remains a possible benign explanation.

Recommend a temporary percentage reserve, with its size set by the human reviewer after checking unsettled exposure. Prioritize the three dispute files, delivery proof, refund requests, and source-record reconciliation. Check campaign dates against sales patterns.

Multiple verified non-delivery cases, overdue fulfillment, and settlement extraction would strengthen the bust-out hypothesis and support pausing settlement. Verified delivery, resolved disputes, or corrected reporting would weaken it. A campaign alone would not dismiss the dispute signal. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records: reason codes, associated orders, dates, status, and merchant responses; establish whether they concern non-delivery.; Reconcile the three disputes and 39 orders to source records, checking duplicates, missing ingestion, and numerator/denominator window alignment.; Check shipment tracking or service-delivery proof for the disputed orders and a small sample of recent unsettled orders; identify overdue fulfillment.; Reconcile refund requests, cancellations, and pending or failed refunds against the reported zero refunds.; Check dated campaign or promotion records and prior seasonal patterns against order timing and buyer mix; compare available historical and category dispute rates.

## Merchant 88 — alert episode 2024-07-02
Triggers: AUP-06.1 breach: 30d chargeback rate 7.1% (3 disputes / 42 orders)
**Recommended action: reserve**

As of July 2, 2024, merchant 88 triggered AUP-06.1: three disputes across 42 trailing-30-day orders, a reported 7.1% rate. GMV was 981351 cents; volume_z was -2.045 and ticket_drift was 0.989. These observations do not show a sales ramp. New GMV share was 17.7%; this does not establish thin buyer accounts. Zero recorded refunds does not establish successful fulfillment.

Recommend a provisional percentage reserve, with the percentage and action owned by the human reviewer. The dispute signal warrants payout protection while inexpensive checks establish its cause; current evidence does not corroborate bust-out.

First reconcile dispute records and order ingestion, then inspect fulfillment and refund handling for affected orders. Repeated overdue non-delivery, concentrated thin buyers and settlement extraction would strengthen the bust-out hypothesis. Verified fulfillment, resolved complaints, or corrected source-data errors would weaken or dismiss it. Check campaign and seasonal records for a benign explanation. Review the reserve after these checks.

Evidence gaps: Inspect the three source dispute records: unique IDs, merchant and order attribution, reasons, status and event dates. Reconcile the 42-order denominator and ingestion completeness; establish which orders the disputes concern.; Check delivery or service-completion evidence for the disputed orders and a small sample of recent orders, including promised dates and customer complaints. Repeated overdue non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile zero recorded refunds against refund requests, support tickets, processor records and pending refunds. Determine whether complaints were resolved or refund requests remain unfulfilled.; Request existing campaign and seasonal-sales records covering the window; compare dates and resulting orders. Review buyer-account history and concentration separately because new_gmv_share does not establish thin accounts.

## Merchant 57 — alert episode 2024-07-06
Triggers: AUP-06.1 breach: 30d chargeback rate 5.1% (3 disputes / 59 orders)
**Recommended action: reserve**

As of July 6, 2024, merchant 57 triggered AUP-06.1: three disputes across 59 trailing-30-day orders produced a 5.1% chargeback rate. GMV was $4,021.27; volume_z was 0.728 and ticket_drift was 1.121. New-buyer GMV share was 20.1%. No refunds were recorded.

The breach is observed; bust-out remains uncorroborated. These metrics provide limited evidence of a sales ramp and do not establish thin buyer accounts, payout extraction or failed delivery. Recorded zero refunds do not prove satisfactory fulfillment.

Recommend a temporary reserve, with the percentage set by the human reviewer, while checking the three disputes and delivery evidence. Reconcile order, dispute and refund records, including pending refund requests, and inspect campaign records and buyer connections.

Repeated non-delivery tied to coordinated buyers and payout extraction would strengthen bust-out concerns and support escalation. Verified fulfillment, resolved disputes, a documented campaign or corrected reporting could support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Review the three dispute records: verify distinct underlying orders, reasons, status and merchant responses. Corroborated non-delivery would strengthen the alert; duplicates or reporting errors would weaken it.; Check fulfillment records and carrier delivery evidence for disputed orders and recent orders due for delivery. Repeated missed commitments would support escalation; verified delivery would weaken the bust-out hypothesis.; Reconcile the 59 orders, three disputes and zero refunds against source systems using the same window and as-of cutoff. Check refund requests and pending refunds as well as completed refunds.; Check campaign dates, promotions and seasonal sales records against order timing and ticket changes. A documented campaign with verified fulfillment would support a benign explanation.; Inspect buyer-account history and connections, alongside settlement records, for coordinated purchases and payout extraction. New-buyer GMV share alone does not establish thin accounts.

## Merchant 91 — alert episode 2024-07-06
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (5 disputes / 198 orders)
**Recommended action: reserve**

As of July 6, merchant 91 triggered B: five disputes across 198 trailing-30-day orders, a 2.525% rate. GMV was 2,091,229 cents. Volume_z was 0.445 and ticket_drift 0.988, providing little support for a pronounced sales ramp. New-customer GMV share was 30.523%, with no prior comparison supplied. Recorded refunds were zero in both windows; this does not establish absence of complaints.

Recommend a provisional payout reserve for human review while resolving the dispute evidence. The breach warrants investigation, but these metrics do not corroborate bust-out or justify termination.

First reconcile dispute classifications, duplicates, and the order denominator. Verify fulfillment for disputed orders and a small recent-order sample, reconcile refund requests with payment records, and inspect campaign records. Repeated verified non-delivery combined with coordinated thin-account purchasing and settlement extraction would strengthen bust-out suspicion. Verified delivery, resolved disputes, or a corrected rate below the trigger would weaken or dismiss the alert. A documented campaign may explain acquisition patterns but would not by itself explain fulfillment failures.

Evidence gaps: Review the five dispute records: reason codes, status, transaction linkage, dates, and duplicates; confirm that they support the trigger's chargeback classification.; Check carrier delivery evidence or service-completion records for the disputed orders and a small sample of recent orders. Repeated verified non-delivery would strengthen bust-out suspicion; verified fulfillment would weaken it.; Reconcile refund requests, pending refunds, and completed refunds against support and payment records. Zero recorded refunds does not establish zero customer complaints.; Reconcile the 198 orders and five disputes with source systems and ingestion logs. Correcting missing orders or duplicate disputes could dismiss the numerical breach.; Check campaign calendars, promotion dates, and acquisition records for a documented benign explanation; compare new-customer share with prior periods if available.; Check settlement records and linked buyer accounts for concentrated purchases, thin accounts, or coordinated activity alongside fulfillment failures.

## Merchant 66 — alert episode 2024-07-09
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (5 disputes / 184 orders)
**Recommended action: reserve**

Merchant 66 triggered AUP-06.1 with five disputes across 184 trailing-30-day orders (2.7%). GMV was 3,089,973 cents, with new GMV share of 31.33%. Volume_z was -0.098, providing no support for a sales ramp. Recorded refunds were zero in both windows; this does not establish successful fulfillment.

Bust-out remains a low-likelihood hypothesis without corroboration of non-delivery, linked thin buyer accounts or settlement extraction. A marketing push or reporting issue is possible but unverified.

Recommend a temporary reserve, with the payout percentage set by the human reviewer under policy and exposure. First inspect the five dispute records, delivery evidence, refund requests and feed completeness. Repeated overdue non-delivery combined with suspicious buyer links or settlement activity would strengthen bust-out concerns. Verified fulfillment, resolved disputes or a corrected reporting error would weaken the alert. Campaign records could explain new-buyer activity but would not independently resolve fulfillment concerns. Reassess after these checks; irreversible offboarding lacks corroborated evidence.

Evidence gaps: Inspect the five dispute records for reasons, status, duplicates and underlying order dates; compare with prior dispute history, which is absent here.; Check promised delivery dates, tracking and delivery evidence for the five disputed orders and a small comparable sample of other orders. Repeated overdue non-delivery would strengthen the alert; verified fulfillment and resolved complaints would weaken it.; Reconcile the zero recorded refunds with processor records, refund requests and support complaints; distinguish genuine absence from delayed, denied or missing refunds.; Verify order, dispute and refund feed completeness as of 2024-07-09. Recompute the rate after correcting any duplication or ingestion gaps.; Review dated campaign records and buyer-account history or shared identifiers for disputed orders; reconcile settlement activity with outstanding fulfillment obligations.

## Merchant 22 — alert episode 2024-07-14
Triggers: AUP-06.1 breach: 30d chargeback rate 7.5% (3 disputes / 40 orders)
**Recommended action: reserve**

As of July 14, merchant 22 breached the chargeback trigger: three disputes across 40 trailing-30-day orders (7.5%). GMV was 264,279 cents. Volume z-score was 0.38 and ticket drift was 0.991, providing little evidence of a sales ramp. New-buyer GMV share was 29.48%; no comparison establishes an increase. Recorded refunds were zero, which does not establish successful delivery.

Recommend a human-approved percentage reserve while completing targeted checks. The breach supports precaution, but bust-out is uncorroborated.

Confirm source counts, inspect all three dispute records, verify overdue and disputed deliveries, reconcile refund requests, and check dated campaign records. Repeated non-delivery combined with thin or linked buyers and settlement extraction would strengthen bust-out concerns and support pausing payouts. Verified fulfillment, unrelated dispute causes, or corrected source data would weaken the alert and support monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes and 40 orders against source records; verify uniqueness, merchant linkage, window attribution and ingestion completeness.; Read the three dispute records for reasons, affected orders, status and outcomes; distinguish non-delivery from unrelated causes.; Check promised delivery dates and carrier-confirmed delivery for disputed orders and a small sample of recent orders, prioritizing overdue shipments.; Reconcile refund requests, cancellations and issued refunds against support and payment records; determine whether the recorded zero refunds omits pending or external refunds.; Request dated campaign records and compare promoted orders, buyer cohorts and fulfillment performance with other orders.; Inspect buyer-account history and links among disputed and recent orders to assess whether thin or connected accounts accompany settlement extraction.

## Merchant 35 — alert episode 2024-07-19
Triggers: AUP-06.1 breach: 30d chargeback rate 5.8% (3 disputes / 52 orders)
**Recommended action: reserve**

As of July 19, merchant 35 breached the chargeback trigger: 3 disputes across 52 trailing-30-day orders (5.8%). Recorded refunds are zero. Volume_z is -1.094 and ticket_drift is 0.959; these do not support the sales acceleration expected in a bust-out. New GMV share is 21.1%, but this does not establish thin buyer accounts.

Recommend a temporary percentage reserve while the human reviewer completes targeted checks. The breach supports payout protection; these metrics alone do not corroborate bust-out or justify termination.

First reconcile disputes and orders to source records, then review dispute reasons, delivery evidence and pending refund requests. Repeated non-delivery combined with suspicious buyer activity would strengthen the bust-out hypothesis. Verified fulfillment and ordinary dispute causes would weaken it. Duplicate disputes or missing orders could dismiss the metric breach after correction. Campaign and category records may support a benign explanation, but should be assessed alongside fulfillment. Reassess the reserve promptly after these checks.

Evidence gaps: Reconcile the three disputes and 52 orders to source records; check duplicates, merchant attribution and ingestion completeness.; Read dispute reasons and inspect fulfillment, tracking and delivery evidence for disputed orders plus a small sample of recent orders. Repeated non-delivery would strengthen bust-out concerns; verified delivery would weaken them.; Check refund requests, pending refunds and processor records. Zero recorded refunds does not establish successful fulfillment.; Check campaign dates, promotions and seasonal/category comparisons, including comparable chargeback rates and buyer-history distributions.

## Merchant 122 — alert episode 2024-07-22
Triggers: AUP-06.1 breach: 30d chargeback rate 4.5% (3 disputes / 66 orders)
**Recommended action: reserve**

As of July 22, merchant 122 breached AUP-06.1: three disputes across 66 trailing-30-day orders, a 4.5% chargeback rate. GMV was 1,036,029 cents; volume_z was 1.004 and ticket_drift was 1.119. Recorded refunds were zero, which does not establish successful fulfillment.

Bust-out remains uncorroborated. The metrics show no extreme volume ramp and do not establish thin buyer accounts or settlement extraction. A marketing push is a possible benign explanation, but campaign evidence is absent. Source-data completeness also needs checking.

Recommend a proportionate payout reserve while a human reviews the breach. Size it using unsettled exposure and open fulfillment obligations. Review all three disputes, verify fulfillment for their orders and a small recent-order sample, and reconcile refund requests and source-system counts. Obtain dated campaign records.

Repeated verified non-delivery combined with suspicious buyer or settlement patterns would support the bust-out hypothesis and escalation to a settlement pause. Valid delivery evidence, resolved disputes, a documented campaign, or corrected source data would weaken the alert and support monitoring or reserve release. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for unique IDs, reason codes, underlying orders, and merchant responses; determine whether they corroborate non-delivery.; Check delivery or service-completion evidence for disputed orders and a small recent-order sample, including orders still within promised fulfillment dates.; Reconcile order, dispute, and refund counts against source records through the alert date; inspect failed ingestion jobs and pending refund requests.; Obtain dated campaign or promotion records and compare their timing with sales changes.; Check unsettled payouts and open fulfillment obligations to size a proportionate reserve; inspect buyer-account concentration and settlement patterns if non-delivery is corroborated.

## Merchant 2 — alert episode 2024-07-26
Triggers: AUP-06.1 breach: 30d chargeback rate 4.7% (3 disputes / 64 orders)
**Recommended action: reserve**

Merchant 2 triggered AUP-06.1 with 3 recorded disputes across 64 trailing-30-day orders: 4.6875%. GMV was 461006 cents. Volume_z was -0.6227 and ticket_drift was 0.9864, providing little support for the rapid sales expansion associated with bust-out. Recorded refunds were zero; that does not establish successful fulfillment.

Recommend a temporary reserve, with the payout percentage set by the human reviewer under applicable policy. The dispute breach warrants protection while evidence is checked, but the supplied metrics do not corroborate bust-out.

First inspect the three dispute records and corresponding fulfillment evidence, then reconcile source order, dispute and refund records. Verify any claimed campaign and examine buyer-account history and concentration.

Repeated non-delivery, unresolved refund requests and coordinated thin-account purchases would strengthen the bust-out hypothesis and support pausing settlement. Verified fulfillment, resolved disputes, legitimate campaign activity or a corrected ingestion error would weaken it and support returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records for unique order IDs, reasons, filing dates, status and outcomes; determine whether they corroborate non-delivery.; Check shipment tracking, delivery confirmation or service-completion records for disputed orders and a small sample of recent orders; compare promised fulfillment dates with actual completion.; Reconcile order, dispute and refund counts against source records through the alert cutoff; check duplicates, missing batches, pending refunds and unprocessed refund requests.; Request campaign dates, offers and channel reports; inspect buyer-account history and linked-account concentration to distinguish legitimate acquisition from coordinated thin-account purchasing.

## Merchant 56 — alert episode 2024-08-05
Triggers: AUP-06.1 breach: 30d chargeback rate 4.5% (3 disputes / 67 orders)
**Recommended action: reserve**

Merchant 56 triggered AUP-06.1 on August 5, 2024: three disputes across 67 trailing-30-day orders, a reported chargeback rate of 4.48%. GMV was 4,307,164 cents; volume_z was 0.687 and ticket_drift was 1.214. New-buyer GMV share was 22.81%. Recorded refunds were zero in both windows.

The dispute signal merits a proportionate payout reserve while a human reviews the cases. Bust-out remains uncorroborated: the metrics do not establish a strong sales ramp, thin buyers, or fulfillment failure. Zero recorded refunds do not establish customer satisfaction.

First review all three disputes, verify fulfillment, reconcile source counts, and check pending refund requests. Repeated verified non-delivery, concentrated thin buyer accounts, and unresolved refunds would strengthen the alert and support considering a settlement pause. Verified delivery, unrelated dispute reasons, or corrected source counts would weaken it. Campaign records could support a benign explanation if the affected orders were fulfilled. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reason, order linkage, status, and merchant response; distinguish non-delivery allegations from unrelated disputes.; Check delivery or service-completion evidence for the disputed orders and a small sample of recent orders, including new buyers. Repeated verified non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile the three disputes and 67 orders with source systems, checking duplicates, window boundaries, and ingestion completeness.; Compare recorded zero refunds with refund requests, pending refunds, cancellations, and processor records; determine whether unresolved non-delivery complaints are going unrefunded.; Request campaign dates and promotion records, then compare affected orders and fulfillment outcomes. Check buyer-account depth and concentration rather than treating new_gmv_share as evidence of thin accounts.

## Merchant 12 — alert episode 2024-08-07
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 120 orders)
**Recommended action: monitor**

As of August 7, 2024, merchant 12 breached AUP-06.1: three disputes across 120 trailing-30-day orders produce a 2.5% chargeback rate. GMV was 2,166,004 cents; volume_z was 0.309 and ticket_drift was 1.034. These metrics provide little evidence of the sales acceleration associated with bust-out. New buyers contributed 33.06% of GMV, but their account quality and historical share are unknown. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window while promptly checking dispute records, fulfillment, refund requests, campaign activity, and data reconciliation. Repeated overdue deliveries, substantiated non-delivery disputes, and concentrated thin-account purchases would strengthen the alert. Verified delivery, resolved disputes, documented legitimate acquisition, or a corrected data error would weaken it.

If checks establish material unfulfilled exposure, consider a reserve; systemic non-delivery with continuing payout exposure could justify a reversible settlement pause. Current evidence does not support offboarding. A human owns the action.

Evidence gaps: Inspect the three dispute records: linked orders, reasons, filing dates, status, and duplicate or attribution errors; reconcile the 120-order denominator.; Check promised delivery dates and shipment or delivery evidence for disputed orders and a small sample of recent orders. Repeated overdue, undelivered orders would strengthen bust-out concern; verified fulfillment would weaken it.; Review refund requests, cancellations, pending refunds, and processor records to determine whether zero recorded refunds reflects no requests, unprocessed requests, or missing data.; Request campaign dates and acquisition-channel records; compare campaign-linked orders and buyer account histories to test legitimate acquisition versus concentrated thin-account buying.

## Merchant 139 — alert episode 2024-09-02
Triggers: AUP-06.2: volume z=3.2 vs baseline; AUP-06.4: new-account GMV share 56%
**Recommended action: reserve**

As of September 2, volume z is 3.15 and new-account GMV share is 55.76%, triggering V and S. Trailing GMV is $32,837.58 across 37 orders, versus baseline GMV of $12,263.33 across 22 orders. Ticket drift is 1.59. There is one dispute (2.70%) and zero recorded refunds. The merchant is 60 days old, and the baseline contains only 30 days.

The pattern warrants review but does not establish bust-out. New accounts are not evidence of coordinated buyers, and a single dispute provides limited support. Marketing or seasonal demand could explain the ramp.

Recommend a provisional percentage reserve, with the human owner setting the percentage after reviewing exposure. Confirm delivery on sampled recent high-value and new-account orders, inspect the dispute, reconcile refund requests and processor records, and obtain campaign attribution. Validate baseline and ingestion completeness.

Repeated overdue non-delivery, coordinated purchasing and corroborating complaints would strengthen the alert and could justify pausing settlement. Verified fulfillment, campaign-linked growth and complete records would support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Sample recent high-value and new-account orders: reconcile promised delivery dates, carrier delivery records and buyer confirmations. Repeated overdue non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations and processor refund records against refunds_30d = 0. Unprocessed requests tied to non-delivery would strengthen concern; complete records showing no such requests would weaken it.; Inspect the single dispute's reason, transaction date, status and supporting documents; reconcile processor records for missing disputes.; Request dated campaign and promotion records, spend and order attribution. Campaign-linked sales with verified delivery would support a benign explanation.; Validate baseline coverage, order deduplication, new-account classification and ingestion completeness against source records. Recompute the triggers if discrepancies appear.

## Merchant 52 — alert episode 2024-09-09
Triggers: AUP-06.1 warn: 30d chargeback rate 2.2% (5 disputes / 227 orders); AUP-06.2: volume z=3.2 vs baseline
**Recommended action: reserve**

As of 2024-09-09, merchant 52 triggered a chargeback warning and a volume alert. The trailing window contains 227 orders, 1,329,361 cents of GMV and five disputes (2.2%); volume_z is 3.2003. New GMV share is 26.1%, ticket drift is 1.0061, and recorded refunds are zero in both windows.

These observations support concern but do not establish bust-out. Buyer thinness, failed delivery and settlement extraction are unverified. Seasonal demand or a campaign could explain the sales increase; ingestion problems could distort the metrics.

Recommend a payout reserve for human review while checking disputed-order fulfillment, a small recent-order sample, refund records, campaign evidence and pipeline completeness. Verified non-delivery across recent orders, unsupported fulfillment claims and evidence of settlement extraction would strengthen bust-out concern and support pausing settlement. Valid fulfillment, explained disputes and a documented campaign or corrected data would support dismissing the alert and returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the five dispute records: reasons, affected orders, transaction dates, duplicate status and merchant responses. Confirm whether they concern non-delivery or unrelated issues; no baseline dispute rate is supplied.; Check fulfillment for disputed orders and a small sample of recent orders, including those contributing to new GMV: promised delivery dates, carrier acceptance, delivery confirmation or service-completion evidence.; Reconcile zero recorded refunds against processor records, cancellations and pending refund requests; determine whether refunds are missing, delayed or genuinely absent.; Request campaign dates and supporting sales records, and check category seasonality against the timing of the increase.; Validate order, dispute and refund ingestion across both windows, reconcile totals to source records, and confirm definitions of volume_z and new_gmv_share.

## Merchant 14 — alert episode 2024-09-15
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (4 disputes / 156 orders)
**Recommended action: monitor**

As of 2024-09-15, merchant 14 breached the stated chargeback threshold: four disputes across 156 trailing-30-day orders (2.56%). GMV was 9,157,525 cents. Volume z-score was 0.28 and ticket drift was 1.007, providing little support for a sales ramp. New-customer GMV share was 29.94%; this does not establish thin buyer accounts. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window while promptly reviewing the four disputes, delivery evidence, refund requests and ledger records. Verify order/dispute ingestion and campaign records.

Repeated non-delivery, concentrated suspicious buyers and settlement extraction would strengthen the bust-out hypothesis and support a reserve or reversible settlement pause. Verified delivery, resolved isolated disputes and a documented campaign would weaken it. Corrected source data could dismiss a reporting-driven breach. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Inspect the four dispute records for unique identifiers, reasons, associated orders and current status; reconcile the 156-order denominator with source records.; Check fulfillment and carrier delivery evidence for disputed orders and a small sample of recent orders; identify overdue deliveries and unresolved customer complaints.; Reconcile zero recorded refunds with the payment ledger and refund requests, including pending or rejected requests.; Check campaign dates, promotion details and acquisition sources against order activity; inspect buyer account history and concentration for disputed and recent orders.; Check ingestion completeness through the alert date and available earlier dispute records to distinguish a reporting problem from a persistent deterioration.

## Merchant 1 — alert episode 2024-09-17
Triggers: AUP-06.1 breach: 30d chargeback rate 2.8% (3 disputes / 108 orders)
**Recommended action: monitor**

As of 2024-09-17, trigger B reports three disputes across 108 trailing-30-day orders (2.8%). GMV is $11,854.78; volume_z is 0.26 and ticket_drift is 0.96. These comparisons do not show the sales acceleration typical of the described bust-out pattern. New-GMV share is 22.9%, but buyer-account quality is unknown. Reported zero refunds do not establish successful fulfillment.

Recommend monitoring the next window, with prompt review of the three disputes, delivery evidence, overdue orders and refund requests. Validate dispute/order linkage and feed completeness, and obtain campaign records plus historical dispute comparisons.

Coordinated non-delivery, concentrated thin buyers and settlement extraction would strengthen bust-out suspicion and support a payout-control review. Verified fulfillment, benign dispute explanations and complete records consistent with historical or campaign activity would support dismissing the alert. A campaign alone would not explain away non-delivery. The supplied evidence does not support offboarding; the human reviewer owns any action.

Evidence gaps: Inspect the three dispute records for reason codes, amounts, distinct orders and buyers, duplicate entries, and current outcomes; reconcile the 108-order denominator.; Check promised delivery dates, carrier delivery evidence or service completion for disputed orders and a small sample of recent orders; verify any overdue fulfillment backlog.; Reconcile refund requests, support complaints, pending refunds and processor refund records against the reported zero refunds.; Request campaign dates, promotion details and seasonal sales context; compare disputed orders with campaign cohorts.; Check historical merchant and category dispute rates, buyer-account quality and concentration, and settlement activity; validate source-feed completeness before treating zeros as missing data.

## Merchant 97 — alert episode 2024-09-18
Triggers: AUP-06.1 breach: 30d chargeback rate 9.4% (3 disputes / 32 orders); AUP-06.4: new-account GMV share 42%
**Recommended action: reserve**

Merchant 97, September 18, 2024: three disputes across 32 trailing-30-day orders produce a 9.375% chargeback rate. New accounts contribute 42.19% of GMV. These triggered B and S. Volume_z is 0.0592, providing little evidence of a sales ramp; recorded refunds are zero.

Recommend a reserve pending prompt human review. The dispute rate merits protection, but the small denominator and absent fulfillment evidence do not establish bust-out. New accounts are not necessarily thin or coordinated buyers.

First validate the three disputes and denominator, then check disputed and sampled new-account orders for delivery against merchant promises. Reconcile refund requests and processor records with zero recorded refunds. Obtain campaign dates and acquisition reports.

Verified systematic nonfulfillment coupled with coordinated buyer activity and settlement extraction would corroborate bust-out and support pausing payouts. Confirmed delivery, resolved or misattributed disputes, and documented legitimate acquisition would weaken or dismiss the alert. A campaign alone would not resolve valid nonfulfillment disputes. Offboarding requires corroborated bust-out evidence; a human owns the action.

Evidence gaps: Review the three dispute records: reasons, transaction links, filing dates, duplicates and available outcomes; reconcile the 32-order denominator and ingestion completeness.; Check fulfillment for disputed orders and a small sample of new-account orders against promised delivery dates, carrier tracking, delivery confirmation and customer communications.; Reconcile zero recorded refunds with refund requests, cancellations, pending or failed refunds and processor records.; Request dated campaign or promotion records and acquisition-channel reports; test whether they explain the new-account sales.; Check available buyer-account history and shared identifiers for concentration or coordination; new-account status alone does not establish thin buyers.

## Merchant 75 — alert episode 2024-09-24
Triggers: AUP-06.2: volume z=3.0 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: reserve**

As of September 24, merchant 75 triggered volume and new-account-share alerts: volume z=3.01 and new-account GMV share=44.5%. Trailing 30-day sales were 772,812 cents across 37 orders. Recorded refunds and disputes were zero; those counts do not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set under existing policy, while a human reviews the evidence. The combination warrants exposure control, but bust-out remains a hypothesis. A marketing campaign or seasonal demand could explain the increase.

First reconcile source transactions and baseline completeness. Then sample fulfillment across new and established buyers, inspect refund requests and pending refunds, reconcile processor disputes and complaints, and obtain campaign attribution.

Verified non-delivery combined with coordinated thin-account purchasing would strengthen the bust-out hypothesis and support considering a settlement pause. Verified delivery and campaign-linked sales would support dismissing the alert and releasing the reserve. A reconciled pipeline error would also support dismissal. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile daily order and GMV totals against source transactions; check baseline completeness, duplicates and new-account classification.; Sample recent orders across new and established accounts for promised delivery dates, shipment tracking, carrier acceptance and delivery confirmation.; Inspect refund requests, cancellations, pending refunds and completed refunds; reconcile them with the reported zero refunds.; Reconcile dispute records with processor records and customer complaints, including event dates and ingestion status.; Request campaign dates, spend, referral sources and order attribution; check whether they explain the sales increase.; Check buyer-account history and shared payment, device or delivery identifiers for coordinated purchasing.

## Merchant 117 — alert episode 2024-10-04
Triggers: AUP-06.1 breach: 30d chargeback rate 4.1% (3 disputes / 73 orders)
**Recommended action: reserve**

As of October 4, the alert reports a 4.1% chargeback rate, calculated from three disputes across 73 trailing-window orders. GMV is 1,569,166 cents; volume_z is 1.21, ticket_drift is 1.13, and new-buyer GMV share is 25.6%. Reported refunds are zero; this does not establish successful fulfillment.

Recommend a proportionate payout reserve, with the percentage set by the human reviewer using exposure and applicable policy. The dispute signal merits protection, but the metrics do not corroborate bust-out or justify termination.

First reconcile dispute and order records, then inspect delivery evidence and refund requests. Verified non-delivery combined with coordinated thin buyers and continued settlement extraction would strengthen bust-out concerns and support considering a settlement pause. Valid deliveries, resolved disputes, and reconciled records would weaken those concerns. Documented campaigns could explain growth but would not independently dismiss the dispute alert. A corrected pipeline that removes the breach would support returning to monitoring.

Evidence gaps: Review the three dispute records: reasons, linked orders, status, and duplicates; reconcile the 73-order denominator and check ingestion completeness.; Check fulfillment and delivery evidence for disputed orders and a small sample of recent orders; investigate missing shipments and unfulfilled backlogs.; Reconcile the zero reported refunds with refund requests, processor records, and pending or failed refunds.; Request dated campaign or seasonal-promotion records and compare their timing with sales and new-buyer activity.; Check disputed and recent buyers for thin account histories or shared identifiers; review outstanding settlement exposure to size the reserve.

## Merchant 37 — alert episode 2024-10-08
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (4 disputes / 124 orders)
**Recommended action: reserve**

Merchant 37 breached the reported AUP-06.1 chargeback threshold: four disputes across 124 trailing-30-day orders, or 3.2%. Volume is near baseline (volume_z −0.137), and ticket_drift is 0.9975. New-customer GMV share is 20.1%, without a supplied comparison. Zero recorded refunds does not establish successful delivery or absence of refund requests.

The evidence supports elevated dispute exposure, but does not corroborate bust-out. Recommend a temporary reserve, sized by the human reviewer to verified exposure, while conducting targeted checks.

First inspect the four dispute records, verify fulfillment of affected and sampled recent orders, and reconcile refund requests with processor records. Check documented campaigns and reconcile order/dispute feeds. Repeated overdue deliveries, unresolved refunds, and payout extraction would strengthen concern. Verified fulfillment, adequately explained disputes, or a corrected feed that removes the breach would weaken the alert. Campaign evidence would support a benign explanation only alongside fulfillment checks.

A human owns the action. Offboarding is unsupported by the current evidence.

Evidence gaps: Inspect the four dispute records for unique IDs, reasons, affected orders, amounts, and merchant responses; reconcile them with processor records and the rate denominator.; Check fulfillment evidence for disputed orders and a small recent-order sample: promised delivery dates, carrier acceptance, delivery confirmation, or service completion. Repeated overdue, undelivered orders would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile zero recorded refunds with refund requests, support tickets, and processor refund records; identify any overdue or unprocessed refunds.; Request campaign dates and promotion records, then compare associated orders and buyer history. A documented campaign with verified fulfillment would support a benign explanation.; Check order-feed completeness and dispute deduplication for the alert window; recalculate the rate after correcting any errors.; Review recent settlement amounts and outstanding unfulfilled-order exposure to size a temporary reserve; concentrated payout extraction alongside failed fulfillment would strengthen concern.

## Merchant 135 — alert episode 2024-10-09
Triggers: AUP-06.1 breach: 30d chargeback rate 5.0% (3 disputes / 60 orders)
**Recommended action: reserve**

Merchant 135 breached AUP-06.1 on 2024-10-09: three disputes across 60 trailing-30-day orders produce a 5.0% reported chargeback rate. GMV was 540,015 cents. Volume_z was 0.263 and ticket_drift was 1.043; neither shows a pronounced ramp. Reported refunds were zero, which does not establish successful fulfillment.

Recommend a provisional payout reserve for human approval while reviewing the disputed transactions. The breach warrants exposure protection, but these metrics alone do not corroborate bust-out or justify offboarding.

Prioritize dispute reasons and supporting records, independently verifiable fulfillment, and reconciliation of refund requests with processor activity. Check campaign records and reconcile dispute/order counts with source data. Repeated verified non-delivery, unresolved refund requests and continued payout extraction would strengthen the concern and support considering a settlement pause. Verified delivery, explained disputes, or corrected source counts would weaken it and support returning to monitoring. Campaign evidence helps explain sales only when fulfillment is also verified.

Evidence gaps: Review the three dispute records for reason, status, transaction linkage and supporting evidence. Corroborated non-delivery would strengthen the bust-out concern; resolved service issues or invalid records would weaken it.; Check fulfillment evidence for disputed orders and a small sample of recent high-value orders: carrier acceptance, delivery confirmation or applicable service-completion records. Verify selected records independently.; Reconcile the reported zero refunds against refund requests, cancellations and processor records. Unprocessed requests alongside missing fulfillment would increase concern.; Request campaign dates, offer terms and order-source records to test whether legitimate promotion explains affected sales and whether fulfillment kept pace.; Reconcile the 60 orders and three disputes with source records, checking completeness, duplicates and window definitions. Confirm what 'new_gmv' measures before interpreting it as buyer-account risk.

## Merchant 6 — alert episode 2024-10-12
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (4 disputes / 150 orders)
**Recommended action: reserve**

As of 2024-10-12, merchant 6 triggered a reported AUP-06.1 chargeback-rate breach: four disputes across 150 trailing-30-day orders (2.67%). GMV was 1,035,077 cents. Volume_z was -0.308, ticket_drift was 1.119, and new_gmv_share was 0.224. Recorded refunds were zero.

These facts support a dispute-risk review but do not establish bust-out. The metrics show no volume surge and provide no direct evidence of thin buyer accounts or non-delivery. Seasonal or campaign context remains unverified; a reporting issue is also possible.

Recommend a temporary percentage reserve, sized under existing policy to payout exposure, pending human review. First validate the four disputes and denominator, inspect delivery evidence, reconcile refund requests and records, and check campaign timing.

Verified non-delivery alongside coordinated buyer activity and settlement extraction would corroborate bust-out and support escalation. Valid delivery with explained disputes would weaken it; corrected records removing the breach would dismiss the reported trigger. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the four dispute records for unique order IDs, reason codes, status, and event dates known by 2024-10-12; establish whether they are chargebacks or another dispute type.; Reconcile the 150-order denominator and dispute/refund feeds against source records, checking completeness, duplicates, and window boundaries.; Check fulfillment and delivery evidence for the four disputed orders and a small sample of recent orders; identify overdue or undelivered orders.; Reconcile zero recorded refunds with refund requests, cancellations, pending refunds, and processor records.; Request existing campaign dates, promoted products, and seasonal sales context; compare disputed orders with campaign cohorts and category benchmarks.

## Merchant 57 — alert episode 2024-10-16
Triggers: AUP-06.1 breach: 30d chargeback rate 5.4% (3 disputes / 56 orders)
**Recommended action: reserve**

As of 2024-10-16, merchant 57 triggered B: three disputes across 56 trailing-30-day orders, a 5.36% chargeback rate. GMV was 333,765 cents; volume_z was 0.6385, ticket_drift 0.9208, and new_gmv_share 20.43%. Reported refunds were zero; this does not establish successful fulfillment.

The dispute breach warrants a temporary payout reserve, with the percentage set by the human risk owner. Bust-out remains plausible but uncorroborated: the metrics do not establish a sharp sales ramp, thin buyer accounts or settlement extraction.

First reconcile dispute and order records, then inspect dispute reasons, promised delivery dates, delivery evidence and refund requests. Check documented campaigns or seasonal explanations against affected orders. Corrected records eliminating the breach, or verified delivery with resolved disputes, would support returning to monitoring. Repeated overdue non-delivery, unresolved refunds and corroborating buyer or payout patterns would support escalating to pause settlement. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three distinct disputes and 56 orders to source records, checking duplicates, window boundaries and missing orders; inspect dispute reasons, statuses and associated purchases.; Check promised delivery dates and carrier or delivery evidence for disputed orders, then sample recent undisputed orders. Repeated overdue non-delivery would strengthen bust-out concerns; verified fulfillment would weaken them.; Reconcile refund requests, cancellations, pending refunds and completed refunds against source records. Determine whether the reported zero refunds reflects complete reporting and whether unresolved requests accompany non-delivery.; Request dated campaign and seasonal-sales records, matching them to order changes and disputed purchases. Verify any explanation against fulfillment outcomes.; Review buyer-account history and settlement records for concentration in thin accounts and payout extraction associated with unfulfilled orders.

## Merchant 105 — alert episode 2024-10-17
Triggers: AUP-06.1 breach: 30d chargeback rate 3.7% (3 disputes / 81 orders)
**Recommended action: monitor**

Merchant 105 breached AUP-06.1: three disputes across 81 trailing-30-day orders produce a 3.7% chargeback rate. GMV was 876749 cents, volume_z was -1.0803886334497992, and ticket_drift was 1.2341038180427608. No refunds were recorded. These facts establish a dispute alert, but do not establish a sales ramp or bust-out.

Recommend monitor, with prompt review of the three disputes. Validate unique records, dates and order-feed completeness; check delivery evidence against promised dates; reconcile requested, pending and completed refunds; and obtain dated campaign records.

Repeated overdue non-delivery, obstructed refunds and concentrated thin-account purchases linked to settlement extraction would strengthen bust-out suspicion and support considering a reversible settlement pause. Verified fulfillment and documented campaigns would weaken that hypothesis; corrected duplicate disputes or missing-order data could dismiss the reported breach. Legitimate unresolved disputes would remain a risk signal even if bust-out is dismissed. A human owns any action.

Evidence gaps: Inspect the three dispute records for unique IDs, linked orders, reasons, event dates and outcomes; reconcile the two alert-day disputes with the trailing-window count and verify order-feed completeness.; Check promised delivery dates and carrier or delivery evidence for disputed orders, then sample other overdue orders. Repeated non-delivery would strengthen bust-out suspicion; verified fulfillment would weaken it.; Reconcile refund requests, approvals, pending items and completed refunds. Zero recorded refunds does not establish that no customers requested refunds.; Request dated campaign or promotion records and compare affected orders with ticket changes and the new-GMV classification. Verify what 'new' means before treating it as evidence of thin buyer accounts.; If non-delivery is corroborated, inspect buyer-account concentration and settlement withdrawals to distinguish operational problems from coordinated extraction.

## Merchant 91 — alert episode 2024-10-20
Triggers: AUP-06.1 warn: 30d chargeback rate 2.1% (5 disputes / 234 orders); AUP-06.2: volume z=3.4 vs baseline
**Recommended action: reserve**

Merchant 91 triggered volume and chargeback alerts as of October 20, 2024. Observed volume_z is 3.35; the trailing 30 days contain 234 orders, 2,380,388 cents GMV, and five disputes (2.14%). New GMV share is 23.84%, and reported refunds are zero.

Bust-out is a plausible hypothesis, but failed delivery, thin buyer accounts, and intentional settlement extraction are unverified. A marketing or seasonal increase could explain sales growth; a feed or aggregation issue could distort the alert. Zero reported refunds do not establish successful fulfillment.

Recommend a temporary percentage reserve for human consideration while reviewing the five disputes, sampling delivery evidence, reconciling refunds and source records, and checking campaign timing. Corroborated nonreceipt, overdue fulfillment, coordinated thin accounts, or unfulfilled refund requests would strengthen concern and support considering a settlement pause. Verified delivery, benign dispute explanations, matching campaign evidence, or corrected data that removes the anomaly would weaken or dismiss the alert. Termination is unsupported without corroborated bust-out evidence.

Evidence gaps: Review the five underlying disputes for reason, order date, delivery evidence, duplication, and status; verified nonreceipt would strengthen concern, while resolved processing issues would weaken it.; Sample recent orders, especially new-buyer orders, for carrier-confirmed delivery, cancellations, and overdue fulfillment; compare with promised delivery dates.; Reconcile reported zero refunds against refund requests, support tickets, processor records, and pending refunds; check whether requests are being fulfilled.; Request campaign dates, offers, acquisition channels, and associated sales; compare with the volume increase and available seasonal history.; Reconcile source order, GMV, dispute, and refund records to the alert window and baseline; check missing feeds, duplicates, and denominator calculations.; Inspect buyer-account history and concentration for recent orders; new GMV share alone does not establish thin or coordinated buyers.

## Merchant 115 — alert episode 2024-10-21
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (8 disputes / 278 orders)
**Recommended action: reserve**

Merchant 115 breached AUP-06.1 as of October 21, 2024: eight disputes across 278 trailing-30-day orders, a 2.88% chargeback rate. GMV was 3,100,512 cents; volume_z was 0.673 and ticket_drift was 1.053. These comparisons do not show a pronounced sales ramp. New buyers contributed 30.05% of GMV, which does not establish thin accounts. Recorded refunds were zero in both windows; that does not demonstrate successful fulfillment.

Recommend a temporary reserve, with the human reviewer setting the payout percentage while checks proceed. Bust-out remains uncorroborated. A campaign or reporting issue is possible but unverified.

First reconcile dispute and order records, inspect dispute reasons, verify fulfillment, and compare refund requests with processor records. Obtain campaign dates and review buyer histories. Repeated verified non-delivery combined with coordinated thin-account sales and settlement extraction would support escalation. Verified fulfillment, resolved disputes or a corrected reporting error would weaken the alert. A campaign alone would not dismiss the chargeback breach.

Evidence gaps: Inspect the eight disputes: verify unique transaction references, reasons, status and merchant responses; reconcile the order denominator against source records.; Check fulfillment for disputed orders and a small recent-order sample using shipment, delivery or service-completion evidence. Repeated verified non-delivery would strengthen bust-out concerns; verified fulfillment would weaken them.; Reconcile recorded zero refunds with processor records, refund requests and support tickets; distinguish absent refunds from missing ingestion or unresolved requests.; Request dated campaign and seasonal sales records, and inspect new-buyer account history for thin accounts or coordinated purchasing.; Review available payout and fulfillment records together for settlement extraction preceding delivery failures.

## Merchant 31 — alert episode 2024-10-22
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (3 disputes / 104 orders)
**Recommended action: reserve**

Merchant 31 triggered AUP-06.1: three disputes across 104 trailing-30-day orders, a 2.9% chargeback rate. GMV was 1,156,201 cents; volume_z was 1.36 and ticket_drift was 1.10. New GMV share was 25.46%, without evidence that these buyers have thin accounts. No refunds were recorded in either window; this does not verify fulfillment.

Recommend a temporary reserve at a human-selected payout percentage while completing targeted checks. The breach supports precautionary protection, but the supplied metrics do not corroborate bust-out or justify offboarding.

Confirm concern through verified non-delivery, overdue fulfillment, unresolved refund requests and related dispute records, particularly if concentrated among recent buyers. Dismiss or downgrade the alert if source reconciliation corrects the breach, or delivery evidence and resolved disputes establish isolated issues. Verified campaign activity could explain sales changes, but would not explain away non-delivery. Reassess the reserve after these checks and watch the next window.

Evidence gaps: Review the three dispute records: verify unique order links, reason codes, filing dates and current outcomes; determine whether they concern non-delivery.; Check fulfillment and delivery evidence for disputed orders and a small recent-order sample; identify overdue orders and unfulfilled exposure.; Reconcile refund requests, pending refunds and completed refunds against payment records; zero recorded refunds does not establish customer satisfaction.; Reconcile order, dispute and refund ingestion with source records, including completeness and duplicate checks.; Request dated campaign or seasonal-sale records and compare attributable orders, buyer-account characteristics and fulfillment with the baseline.

## Merchant 7 — alert episode 2024-11-01
Triggers: AUP-06.1 breach: 30d chargeback rate 7.7% (3 disputes / 39 orders)
**Recommended action: reserve**

As of 2024-11-01, merchant 7 triggered AUP-06.1: three disputes across 39 trailing-30-day orders produce a 7.7% chargeback rate. GMV was 1,947,824 cents. Volume_z is -0.158 and ticket_drift is 0.963, providing no clear evidence of a sales ramp. Recorded refunds are zero; that does not establish successful fulfillment.

Recommend a temporary percentage reserve, with the human reviewer setting its size and release criteria. The dispute signal warrants protection and review, but these metrics alone do not corroborate bust-out or justify termination.

First reconcile dispute and order records, inspect dispute reasons, verify fulfillment, and check pending or unrecorded refund requests. Review campaign evidence and buyer-account concentration. Repeated verified nonfulfillment alongside thin-account purchases and settlement extraction would strengthen bust-out concerns and support pausing settlement pending review. Verified delivery, resolved disputes, or a corrected pipeline error would weaken the alert and support releasing the reserve and monitoring the next window.

Evidence gaps: Inspect the three dispute records for reasons, underlying order dates, duplicates, outcomes and merchant responses; reconcile the numerator and 39-order denominator to source records.; Verify delivery or service completion for disputed orders and a small sample of recent orders using independent tracking or customer confirmation. Repeated verified nonfulfillment would strengthen the bust-out hypothesis; documented fulfillment would weaken it.; Reconcile refund requests, cancellations and pending refunds with the zero recorded refunds; check whether customers sought refunds that were refused or never processed.; Request campaign dates, offers and order attribution, plus comparable seasonal sales history, to test a benign explanation.; Inspect buyer-account history and payout records for concentrated thin-account purchases and rapid settlement extraction before escalating.

## Merchant 59 — alert episode 2024-11-03
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (4 disputes / 146 orders)
**Recommended action: reserve**

As of 2024-11-03, merchant 59 breached AUP-06.1: four disputes across 146 trailing-30-day orders produce a 2.74% chargeback rate. GMV was 1,014,133 cents; volume_z was 1.70 and ticket_drift was 0.988. Recorded refunds were zero, which does not establish successful fulfillment.

Recommend a reserve, with the payout percentage set by the human reviewer under policy. The breach supports protecting exposure while investigating; these metrics alone do not corroborate bust-out.

First reconcile disputes and order counts, then inspect delivery evidence and refund requests. Repeated overdue non-delivery, related thin buyer accounts and settlement extraction would strengthen the bust-out hypothesis and support considering a settlement pause. Verified deliveries, resolved disputes and attributable campaign sales would weaken it. A corrected source-data discrepancy could dismiss the metric alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the four dispute records for reasons, order IDs, duplicates and status; reconcile the 146-order denominator and dispute inclusion rules against processor and order-system records.; Check promised delivery dates and carrier or delivery evidence for disputed orders and a small sample of recent orders; identify overdue unfulfilled orders and merchant responses.; Reconcile the zero recorded refunds against processor refunds, cancellations and customer refund requests; check whether ingestion is complete.; Request campaign dates and attributable sales, and inspect existing buyer-account age and concentration data to distinguish legitimate acquisition from concentrated thin-account purchasing.

## Merchant 40 — alert episode 2024-11-08
Triggers: AUP-06.1 breach: 30d chargeback rate 3.6% (3 disputes / 84 orders)
**Recommended action: reserve**

Merchant 40 triggered AUP-06.1 on November 8: three disputes across 84 trailing-30-day orders, a 3.57% rate. GMV was 1,730,781 cents. Volume_z was 0.104 and ticket_drift was 1.034, providing little evidence of a sales ramp. Reported refunds were zero; this does not establish satisfactory fulfillment.

Recommend a temporary reserve, with the percentage set by the human reviewer, while checking dispute validity and delivery. The breach warrants protection, but these metrics do not corroborate bust-out or justify termination.

First reconcile dispute records and the denominator, then inspect dispute reasons, fulfillment evidence and outstanding refund requests. Verified repeated non-delivery, especially involving linked thin buyer accounts and settled orders, would strengthen the alert and support pausing settlement. Corrected duplicate or misassigned disputes could dismiss the trigger; verified delivery and documented legitimate campaigns would weaken the bust-out hypothesis. Reassess the reserve after these checks.

Evidence gaps: Reconcile the three disputes to processor records and the 84-order denominator; verify unique records, timestamps and pipeline completeness.; Read dispute reasons and sample the affected orders plus recent undisputed orders for promised delivery dates, carrier acceptance and delivery evidence. Repeated overdue non-delivery would strengthen the bust-out hypothesis.; Check refund requests, pending refunds and processor refund records against the reported zero completed refunds; unresolved requests would increase concern.; Request dated campaign records and compare campaign-linked orders with verified fulfillment. Legitimate campaigns with delivered orders would support a benign explanation.; Check whether recent buyers are thin or linked accounts and whether their orders received settlement without fulfillment; corroboration would support escalation.

## Merchant 12 — alert episode 2024-11-10
Triggers: AUP-06.1 breach: 30d chargeback rate 3.1% (4 disputes / 129 orders)
**Recommended action: reserve**

Merchant 12 breached the chargeback trigger: four disputes across 129 trailing-30-day orders (3.1%). Volume_z is 0.51 and ticket_drift is 0.972, providing little support for a sales ramp. New buyers account for 31.34% of GMV; this does not establish thin accounts. Recorded refunds are zero, which does not establish successful fulfillment.

Recommend a temporary percentage reserve, with the amount set by the human reviewer, while checking the four disputes and recent fulfillment. The breach establishes a loss concern, but bust-out remains uncorroborated.

Repeated non-delivery, unresolved refund requests, and concentrated thin-buyer activity would strengthen the alert and support considering a settlement pause. Verified fulfillment, resolved disputes, and documented campaigns or seasonal patterns would weaken the bust-out hypothesis. Reconcile source records before attributing the rate to merchant behavior; a counting or pipeline error could dismiss the breach. Offboarding is not supported by the supplied evidence.

Evidence gaps: Review the four dispute records for reasons, order links, status, and merchant responses; compare with prior dispute history.; Check delivery or service-completion evidence for disputed orders and a small recent-order sample; repeated non-delivery would strengthen bust-out concern.; Reconcile refund requests, cancellations, pending refunds, and processor records against the reported zero refunds.; Check campaign dates and seasonal sales history; matched campaigns with completed fulfillment would support a benign explanation.; Reconcile dispute and order counts with source systems and verify pipeline completeness; corrected counts could dismiss the breach.; Inspect recent buyer-account history and concentration to determine whether new-buyer sales involve thin or linked accounts.

## Merchant 145 — alert episode 2024-11-10
Triggers: AUP-06.1 breach: 30d chargeback rate 13.0% (3 disputes / 23 orders); AUP-06.4: new-account GMV share 59%
**Recommended action: reserve**

As of November 10, merchant 145 has three disputes across 23 trailing-30-day orders (13.0%) and 58.9% of GMV from new accounts. Trailing GMV is 1,940,672 cents. Volume_z is -0.87, which does not support a sales ramp. The baseline covers only 37 days and 34 orders; zero recorded refunds does not establish successful fulfillment.

Recommend a reserve, with the percentage set by outstanding exposure and human review. These signals warrant investigation but do not establish bust-out or justify irreversible offboarding.

First reconcile dispute records, order counts and ingestion completeness. Check delivery evidence for disputed and high-value new-account orders, refund requests against processor records, and dated acquisition campaigns.

Verified non-delivery combined with coordinated buyer activity or continued payout extraction would strengthen the bust-out hypothesis and support pausing settlement pending review. Valid fulfillment and campaign attribution would weaken it; a verified pipeline error that removes the triggering conditions would support dismissing the alert. Campaign evidence alone would not resolve the disputes.

Evidence gaps: Review the three dispute records for reason codes, order links, event dates, duplicates and status; reconcile the 23-order denominator with the order ledger.; Check fulfillment for disputed orders and a small sample of high-value new-account orders using shipment, delivery or service-completion evidence.; Reconcile refunds_30d against refund requests, cancellations and processor records; determine whether recorded zero refunds omits pending or failed refunds.; Request dated campaign records and acquisition-channel results to test whether legitimate promotions explain the new-account concentration.; Check ingestion completeness and new-account classification; compare affected buyers for shared identifiers or other evidence of coordination.; Review unsettled payouts and outstanding fulfillment obligations to size a reserve against current exposure.

## Merchant 25 — alert episode 2024-11-11
Triggers: AUP-06.1 breach: 30d chargeback rate 5.7% (3 disputes / 53 orders)
**Recommended action: reserve**

Merchant 25 triggered B on 2024-11-11: three disputes across 53 trailing-30-day orders, a reported rate of 5.66%. GMV was 317,526 cents. Volume_z is -0.686 and ticket_drift is 0.968, so the supplied comparisons do not support a sales ramp. New-buyer GMV share is 17.94%; zero recorded refunds does not establish successful fulfillment.

Recommend a temporary percentage reserve, with the human reviewer setting the percentage against verified exposure while completing prompt checks. The dispute breach supports caution, but bust-out is uncorroborated and offboarding is unsupported.

Confirm the alert by validating unique dispute records and the order denominator. Repeated non-delivery, unresolved refund requests and coordinated thin-buyer purchasing would strengthen bust-out. Credible delivery evidence and resolved isolated disputes would weaken it. Missing orders or duplicate disputes could dismiss the reported breach after reconciliation; campaign records could explain buyer-mix changes. Release or adjust the reserve based on these findings.

Evidence gaps: Inspect the three dispute records for unique IDs, reason codes, order links and merchant responses; reconcile the 53-order denominator against source records through the alert cutoff.; Request delivery or service-completion evidence for disputed orders and a small sample of recent orders. Repeated verified non-delivery would strengthen bust-out; credible fulfillment would weaken it.; Check refund requests, cancellations, pending refunds and processor records. Zero recorded refunds does not establish that customers have no unresolved claims.; Check campaign dates and promoted orders against the disputed transactions; review buyer account history and links for coordinated purchasing.

## Merchant 137 — alert episode 2024-11-14
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (3 disputes / 105 orders)
**Recommended action: monitor**

Merchant 137 triggered AUP-06.1 on November 14: three disputes across 105 trailing-30-day orders, with cb_rate_30d of 0.02857142857142857. Recorded GMV was 999752 cents, volume_z was -1.67351278716791, and new_gmv_share was 0.2760674647312534. No refunds were recorded.

The breach is observed; bust-out is a hypothesis. Current metrics do not show the described sales ramp or establish thin buyer accounts. Zero refunds does not prove successful fulfillment.

Recommend monitor for the next window, with immediate review of the three disputes, delivery evidence, refund requests and source-data completeness. Verified non-delivery combined with coordinated buyer activity would strengthen bust-out and support a reserve or reversible settlement pause. Valid deliveries and resolved dispute explanations would weaken it. Corrected duplicate disputes or missing denominator orders could dismiss the measured breach; a campaign alone would not explain away fulfillment complaints.

Review campaign records and buyer histories. A human owns any payout restriction; offboarding lacks corroborated support.

Evidence gaps: Inspect the three dispute records: verify uniqueness, order linkage, reason codes and status; reconcile the 105-order denominator and ingestion completeness.; Check tracking, delivery confirmation and customer correspondence for disputed orders, then a small sample of recent orders. Repeated verified non-delivery would support escalation; documented fulfillment would weaken bust-out.; Reconcile refund requests, approvals and processor records. Zero recorded refunds does not establish that no customers requested refunds.; Review campaign dates, offers and attributed orders; check buyer account history and concentration to distinguish ordinary acquisition from coordinated thin-account purchases.

## Merchant 73 — alert episode 2024-11-19
Triggers: AUP-06.1 warn: 30d chargeback rate 1.6% (4 disputes / 252 orders); AUP-06.2: volume z=3.6 vs baseline
**Recommended action: reserve**

As of November 19, merchant 73 triggered chargeback and volume alerts: four disputes across 252 trailing orders (1.59%) and volume z=3.63. Trailing GMV is 2,299,269 cents; the preceding 90-day baseline contains 601 orders and 5,475,593 cents. Ticket drift is 1.00146, new GMV share is 26.54%, and recorded trailing refunds are zero.

Recommend a temporary, proportionate payout reserve, with the percentage set by the human reviewer under policy. The combined signals justify limiting exposure while checking delivery, but do not establish bust-out or support termination.

Inspect all four disputes, sample fulfillment against promised delivery dates, reconcile refund requests and payment records, and check campaign timing and source-data completeness. Repeated overdue nonfulfillment, concentrated nonreceipt disputes and coordinated thin-account purchasing would strengthen the bust-out hypothesis and support considering a settlement pause. Verified delivery, explained disputes and campaign or seasonal demand matching the increase would weaken it. A confirmed ingestion defect would require correcting and recomputing the alert. A human owns the action.

Evidence gaps: Inspect the four dispute records for reasons, associated orders, delivery evidence and resolution; nonreceipt clustering would strengthen concern, while supported unrelated causes would weaken it.; Sample recent orders, including disputed orders, against promised delivery dates, carrier scans and customer receipt confirmations; overdue unfulfilled orders would support escalation.; Reconcile refund requests, cancellations and pending refunds with payment records; zero recorded refunds does not establish that customers received their goods.; Check campaign dates, attributed orders and available seasonal comparators; a matching demand increase with verified fulfillment would support a benign explanation.; Reconcile recent and baseline order, GMV and dispute totals with source records, checking missing dates, duplicates and metric definitions.; Review buyer concentration and available account-history indicators for recent orders; new GMV share alone does not establish thin or coordinated buyer accounts.

## Merchant 98 — alert episode 2024-11-20
Triggers: AUP-06.1 breach: 30d chargeback rate 6.7% (3 disputes / 45 orders)
**Recommended action: reserve**

Merchant 98 breached AUP-06.1: three disputes across 45 trailing-30-day orders produce a 6.7% chargeback rate. GMV was $6,393.77. Volume z-score is 0.40 and ticket drift is 1.029, providing little support for a pronounced ramp. New-buyer GMV share is 24.4%; this does not establish thin accounts. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary payout reserve, sized to verified undelivered and disputed exposure, with human approval and reassessment after reconciliation. The breach warrants protection, but current evidence does not corroborate bust-out.

First reconcile dispute and order records, inspect dispute reasons, and verify delivery for disputed orders plus a recent sample. Check pending refund requests and complaints, then request campaign attribution and buyer-account history. Repeated verified non-delivery combined with thin-account sales and settlement extraction would support escalation to a settlement pause. Corrected records eliminating the breach, or verified delivery and resolved disputes, would support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three dispute records and 45 orders against source systems; check duplicates, status, window assignment, and ingestion completeness. Recalculate the rate after corrections.; Review dispute reasons and outcomes, then verify tracking and delivery for disputed orders and a small recent-order sample. Repeated verified non-delivery would strengthen the bust-out hypothesis.; Check refund requests, pending refunds, cancellations, and support complaints against processor records; determine whether zero recorded refunds reflects no requests or unprocessed requests.; Request campaign dates and order-level attribution; compare disputed and successfully fulfilled orders by campaign and buyer cohort.; Review buyer-account history and current undelivered exposure to distinguish ordinary new customers from thin accounts and size a temporary reserve.

## Merchant 35 — alert episode 2024-11-24
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (3 disputes / 95 orders)
**Recommended action: reserve**

Merchant 35 breached the chargeback trigger: 3 disputes across 95 trailing-30-day orders, a 3.2% rate. Volume_z is 2.9069, ticket_drift is 1.0869, and new GMV share is 22.1%. Recorded refunds are zero in both windows; that does not establish customer satisfaction.

Bust-out is possible but uncorroborated. These metrics do not demonstrate failed delivery, thin buyers, or coordinated purchasing. Seasonal demand and a marketing campaign are plausible explanations for increased sales; neither is verified.

Recommend a temporary percentage reserve, with the percentage set by the human reviewer after assessing outstanding fulfillment exposure. First inspect all three disputes, sample recent fulfillment, reconcile refund requests and records, verify campaign timing, and check pipeline completeness.

Repeated nondelivery, unresolved refund requests, and suspicious buyer links would strengthen the alert and support pausing settlement. Verified deliveries, explained disputes, and documented campaigns or seasonal demand would support releasing the reserve and monitoring. A source-data correction could dismiss the breach. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reason codes, associated orders, delivery evidence, and outcomes. Verified nondelivery would strengthen concern; documented delivery or unrelated dispute causes would weaken it.; Check fulfillment status and carrier delivery evidence for disputed orders and a small sample of recent orders, including new-buyer orders. Look for overdue shipments, cancellations, or repeated buyer details.; Reconcile refund requests, support complaints, and processor refund records against the reported zero refunds; distinguish no requests from unresolved or unrecorded requests.; Request campaign dates and sales reports, and compare available prior seasonal or category patterns. A documented demand spike with normal fulfillment would support a benign explanation.; Reconcile order and dispute counts to source records and check ingestion completeness through 2024-11-24. Corrected counts could confirm or dismiss the rate breach.

## Merchant 121 — alert episode 2024-11-26
Triggers: AUP-06.1 warn: 30d chargeback rate 1.8% (5 disputes / 277 orders); AUP-06.2: volume z=4.5 vs baseline
**Recommended action: reserve**

As of 2024-11-26, merchant 121 triggered a volume anomaly (z=4.46) and a 30-day chargeback warning: five disputes across 277 orders (1.805%). Thirty-day GMV was 1,520,220 cents; new-customer GMV share was 21.46%. Recorded refunds were zero, which does not establish successful delivery.

Bust-out is plausible but uncorroborated. Seasonal demand or a marketing campaign could explain the increase; metric integrity also needs verification.

Recommend a temporary payout reserve, with the percentage and release criteria set by the human reviewer. First inspect the five disputes, verify delivery for those orders and a small recent-order sample, reconcile refund requests with processor records, and obtain campaign evidence. Recompute the volume statistic against complete source data.

Repeated non-delivery combined with coordinated buyer activity and settlement extraction would strengthen the bust-out hypothesis and support pausing settlement. Verified fulfillment, reconciled dispute/refund records, and campaign or seasonal evidence would support dismissing the alert and releasing the reserve. A confirmed pipeline error could also dismiss the metric trigger. Current evidence does not justify irreversible offboarding.

Evidence gaps: Inspect the five dispute records for reasons, underlying order dates, duplication, and fulfillment evidence; reconcile their count and denominator to source records.; Check tracking and delivery confirmation for disputed orders and a small sample of recent orders; repeated non-delivery would strengthen bust-out concern.; Reconcile refund requests, cancellations, pending refunds, and processor records against the zero recorded refunds.; Request dated campaign records and comparable seasonal sales; campaign-linked orders with verified delivery would support a benign explanation.; Recompute volume_z from source daily counts and verify baseline/window completeness, duplicate handling, and metric definitions.; Review buyer concentration and account history for the volume increase, alongside recent payout changes, to test for coordinated purchases and extraction.

## Merchant 88 — alert episode 2024-11-27
Triggers: AUP-06.1 breach: 30d chargeback rate 4.6% (3 disputes / 65 orders)
**Recommended action: reserve**

Merchant 88 triggered the reported chargeback breach: 3 disputes across 65 trailing-30-day orders (4.6%). GMV was $14,127.42. Volume_z was 0.83, ticket_drift was 0.924, and new_gmv_share was 24.1%; these metrics do not establish a bust-out ramp or thin buyer accounts. No refunds were recorded, which does not prove successful delivery.

Recommend a temporary payout reserve, with its percentage set by the human reviewer after assessing exposure. Current evidence warrants investigation but does not corroborate bust-out sufficiently for termination.

First inspect all three disputes and verify fulfillment on those orders plus a small recent-order sample. Reconcile refund requests and processor records, confirm source-data completeness, and check campaign timing and buyer-account concentration.

Verified non-delivery combined with coordinated thin-account purchasing would strengthen bust-out and support pausing settlement. Valid deliveries, explainable disputes, and documented campaigns would weaken it. A source-data correction that removes the breach would dismiss the metric alert. The human reviewer owns the action.

Evidence gaps: Inspect the three dispute records: reason codes, underlying order dates, merchant attribution, duplication, and current status.; Check shipment, carrier acceptance, delivery confirmation, and customer complaints for disputed orders and a small sample of recent orders.; Reconcile refund requests, cancellations, pending refunds, and processor records with the reported zero refunds.; Reconcile the 65 orders and three disputes against source records and ingestion completeness.; Review dated campaign records, promotion spend, and comparable seasonal activity; inspect buyer-account age and linked-account concentration.

## Merchant 62 — alert episode 2024-11-28
Triggers: AUP-06.1 warn: 30d chargeback rate 2.3% (3 disputes / 129 orders); AUP-06.2: volume z=3.7 vs baseline
**Recommended action: reserve**

Merchant 62 triggered W and V on November 28: volume z=3.73 and three disputes across 129 trailing-30-day orders (2.33%). GMV was 1,453,967 cents. Recorded refunds were zero, and ticket_drift was 0.9944. These are observed signals; fulfillment failure and deliberate settlement extraction remain hypotheses.

Recommend a temporary payout reserve, with the percentage set by the human reviewer against verified outstanding delivery exposure. The combined signals warrant protection while evidence is gathered, but do not establish bust-out.

First reconcile orders, baseline coverage, and dispute records. Review dispute reasons and delivery evidence, then sample recent orders against promised delivery dates. Check refund requests and pending or processor-recorded refunds. Request dated campaign evidence and inspect buyer concentration and payout timing.

Verified overdue non-delivery, related disputes, and payouts against unfulfilled sales would strengthen the bust-out hypothesis and support pausing settlement. Reconciled data, reliable fulfillment, explained disputes, and a documented campaign or seasonal pattern would weaken it and support monitoring. A verified pipeline defect could dismiss the metric anomaly. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the 129 orders and three unique dispute records to source systems; verify window boundaries, baseline completeness, dispute reasons, statuses, and linked orders.; Inspect delivery evidence and promised delivery dates for disputed orders and a small sample of recent orders; expand the sample if overdue or unverifiable deliveries appear.; Check refund requests, cancellations, pending refunds, and processor refund records; zero recorded refunds does not establish satisfied customers.; Request dated campaign records and compare campaign-driven orders with the volume increase; check prior comparable seasonal periods if available.; Compare payout timing and amounts with fulfilled versus overdue orders, and inspect buyer-account history and concentration for the recent sales increase.

## Merchant 146 — alert episode 2024-12-01
Triggers: AUP-06.1 breach: 30d chargeback rate 4.6% (3 disputes / 65 orders)
**Recommended action: reserve**

The alert reports three disputes across 65 trailing-30-day orders (4.6%). This warrants prompt review, but does not establish bust-out. Volume_z is 0.068, ticket_drift is 0.817, and new-buyer GMV share is 14.9%; these do not demonstrate a sales ramp or thin buyer accounts. Zero recorded refunds do not establish successful fulfillment.

Recommend a policy-sized payout reserve, with the percentage and release decision owned by a human reviewer. Reconcile dispute records and the order denominator, inspect fulfillment evidence, verify refund completeness, and review campaign timing and category comparisons.

Repeated overdue, undelivered orders combined with settlement extraction and suspicious buyer patterns would strengthen the bust-out hypothesis and support considering a settlement pause. Verified timely delivery, isolated explained disputes, or corrected records that remove the breach would weaken the alert and support releasing the reserve and monitoring. Campaign evidence alone would not resolve delivery complaints. Offboarding is unsupported without corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes to unique orders, reasons, dates and status; verify whether they represent chargebacks and confirm the 65-order denominator.; Check promised delivery dates, carrier acceptance and delivery evidence for disputed orders, then sample other recent orders for recurring fulfillment failures.; Reconcile zero reported refunds against merchant and processor records, including pending requests and ingestion completeness.; Review campaign dates and seasonal/category benchmarks; compare affected buyers with other buyers using available account-history and linkage evidence.; Match settlements to disputed and unfulfilled orders to assess whether payouts preceded a broader delivery breakdown.

## Merchant 87 — alert episode 2024-12-05
Triggers: AUP-06.1 warn: 30d chargeback rate 1.7% (3 disputes / 177 orders); AUP-06.2: volume z=3.5 vs baseline
**Recommended action: reserve**

Merchant 87 triggered volume and chargeback warnings as of December 5, 2024. Recorded 30-day activity comprises 177 orders, 1,005,421 cents GMV and three disputes (1.69%); volume_z is 3.48. Recorded refunds are zero, which does not establish successful fulfillment.

Bust-out is plausible but uncorroborated. Holiday demand or a marketing campaign could explain the volume signal; neither is documented. Buyer thinness and delivery failure are not established.

Recommend a temporary payout reserve, with the percentage set by the human reviewer while completing prompt checks. Inspect the three disputes, sample delivery evidence against promised dates, reconcile refund requests and payments, verify campaign records, and recompute the alert from source data.

Repeated overdue non-delivery, related disputes and concentrated thin buyers would strengthen the alert and support considering a settlement pause. Verified fulfillment, a documented demand driver and reconciled records would weaken it and support returning to monitoring. Offboarding requires corroborated bust-out evidence. The human reviewer owns the action.

Evidence gaps: Sample recent orders for promised delivery dates, carrier delivery evidence and customer confirmations; compare with baseline fulfillment. Repeated overdue non-delivery would strengthen bust-out concerns.; Inspect all three dispute records for reasons, underlying orders, event dates and duplicates. Determine whether they concern non-delivery or another cause.; Reconcile refund requests, approvals and payments with the zero recorded refunds; check for unresolved cancellations or unprocessed refunds.; Check dated campaign records, attributed orders and comparable holiday sales. A matching demand increase with reliable fulfillment would weaken bust-out concerns.; Recompute volume_z and dispute counts from source records; verify baseline completeness, ingestion status and the 177-order denominator.; Review recent buyer-account history and concentration, particularly disputed orders. The supplied new_gmv_share does not establish buyer thinness.

## Merchant 118 — alert episode 2024-12-07
Triggers: AUP-06.1 warn: 30d chargeback rate 1.8% (3 disputes / 167 orders); AUP-06.2: volume z=5.8 vs baseline
**Recommended action: monitor**

As of December 7, volume_z is 5.80 and the trailing window contains 3 disputes across 167 orders (1.80%). Order pace is approximately 56% above the preceding baseline. Recorded refunds are zero; new GMV share is 15.82% and ticket_drift is 0.897. These facts warrant review but do not establish bust-out.

Holiday demand or a campaign could explain the volume increase. Verify campaign timing and source-data completeness, inspect all three disputes, and sample delivery evidence against promised dates. Reconcile refund requests with processor and support records; zero recorded refunds is not proof of satisfactory fulfillment.

Recommend monitoring the next window while completing these checks. Verified deliveries, explained disputes, and campaign-linked sales would support dismissing the bust-out hypothesis. Repeated non-delivery, concentrated thin buyer accounts, and settlement extraction tied to unfulfilled orders would strengthen it and support a reserve or reversible settlement pause. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Review the three dispute records for reasons, affected order dates, delivery evidence, and outcomes; determine whether they reveal a common fulfillment failure.; Sample recent fulfilled and overdue orders, including disputed orders, using promised delivery dates, carrier scans, and customer confirmations.; Reconcile refund requests and completed refunds against processor records and support tickets; zero recorded refunds does not establish zero complaints.; Check campaign calendars, discounts, and order attribution, plus comparable seasonal sales where available.; Reconcile daily source-order totals with the current window and baseline; check missing ingestion days, duplicates, and dispute/refund feed completeness.; Inspect recent buyer-account history and concentration, then reconcile settlement amounts with unfulfilled-order exposure.

## Merchant 55 — alert episode 2024-12-11
Triggers: AUP-06.1 breach: 30d chargeback rate 3.4% (3 disputes / 88 orders); AUP-06.2: volume z=5.2 vs baseline
**Recommended action: reserve**

As of December 11, merchant 55 has 3 disputes across 88 trailing-30-day orders (3.4%), triggering AUP-06.1, and volume_z of 5.18, triggering AUP-06.2. GMV is 4,696,857 cents; recorded refunds are zero. These are observed signals, not proof of bust-out.

Recommend a reserve, with the percentage set by the human reviewer, while completing targeted checks. The combined alerts justify payout protection, but fulfillment failure and coordinated purchasing are unconfirmed.

First reconcile orders, disputes, and baseline ingestion. Review all three dispute files, delivery tracking, refund requests and processing, and campaign records. Check recent buyers for thin histories and shared identifiers.

Verified non-delivery alongside coordinated purchases and settlement extraction would corroborate bust-out and support stronger action. Verified fulfillment and campaign or seasonal attribution would weaken that hypothesis; corrected source data could dismiss the metric alert. Zero recorded refunds alone does not demonstrate successful fulfillment. Escalate to a reversible settlement pause if checks substantiate ongoing exposure; offboard only with corroborated bust-out evidence.

Evidence gaps: Reconcile the 3 disputes and 88 orders to source records; check duplicates, date assignment, and baseline ingestion completeness.; Review all three dispute files for reason codes, affected orders, delivery evidence, and merchant responses.; Check carrier acceptance and delivery records for disputed orders and a small sample of recent orders; compare against promised delivery dates.; Inspect refund requests, support complaints, cancellations, and refund-processing records; determine whether zero recorded refunds reflects no requests or unprocessed requests.; Match sales increases to documented campaign dates, attributed orders, and available prior seasonal sales.; Check recent buyers for account history and shared identifiers, and reconcile settlements with orders to assess coordinated purchasing and payout extraction.

## Merchant 14 — alert episode 2024-12-15
Triggers: AUP-06.1 warn: 30d chargeback rate 2.0% (5 disputes / 255 orders); AUP-06.2: volume z=7.2 vs baseline
**Recommended action: reserve**

As of December 15, merchant 14 has 255 trailing-30-day orders and 14,293,701 cents in GMV, versus 485 orders and 26,956,889 cents over the preceding 90 days. Volume z is 7.18. Five disputes produce a 1.96% trailing chargeback rate. Recorded refunds are zero; ticket_drift is 1.0085 and new_gmv_share is 22.33%.

The volume and dispute signals support a temporary reserve while a human reviews the evidence. They do not establish bust-out. Holiday demand or a campaign could explain the increase; incomplete data could distort comparisons.

First inspect recent fulfillment and all five disputes, reconcile refund requests with recorded refunds, verify campaign timing, and check pipeline completeness. Missing deliveries corroborated by carrier records, non-delivery disputes and unresolved refund requests would strengthen the bust-out hypothesis and support pausing settlement. Verified delivery, explained disputes and documented campaign or seasonal demand would support returning to monitoring. Corrected data that removes the spike would dismiss the metric-based alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect tracking and delivery evidence for recent orders, prioritizing disputed orders and orders during the volume ramp; confirm with carrier records where available.; Review the five dispute records for reasons, underlying order dates, delivery evidence and resolution status.; Reconcile recorded refunds with refund requests, support complaints and processor records to distinguish no refunds from missing or unprocessed refunds.; Request dated campaign records and compare campaign timing, attributed orders and historical holiday sales with the volume increase.; Check source-to-metric order counts, duplicates, baseline completeness and dispute/refund ingestion through the alert date.

## Merchant 80 — alert episode 2024-12-18
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 42%
**Recommended action: monitor**

Merchant 80 triggered volume and new-account-share alerts on December 18. Observed volume_z is 3.07, new-account GMV share is 42%, and ticket_drift is 1.35. The trailing window contains 54 orders and 694,751 cents in GMV. Recorded refunds and disputes are both zero; those counts do not establish successful fulfillment.

A bust-out is plausible but uncorroborated. Holiday demand or a documented acquisition campaign could explain the pattern. Account thinness and settlement extraction are not established.

Recommend monitoring the next window with prompt checks now. Sample fulfillment against promised delivery dates, reconcile refund and dispute records, verify campaigns, and reconcile source transactions and baseline completeness. Repeated overdue non-delivery combined with concentrated thin-account purchases and settlement extraction would corroborate bust-out risk and support payout controls. Verified delivery and a campaign or seasonal explanation would reduce concern; a corrected pipeline could dismiss the metric alert. A human owns any action.

Evidence gaps: Sample recent orders, especially high-value new-account purchases, and verify promised delivery dates, carrier acceptance and delivery evidence. Repeated overdue, unfulfilled orders would strengthen the bust-out hypothesis.; Reconcile reported zero refunds and disputes against payment-provider records, pending refund requests and customer complaints known by the alert cutoff; review any dispute reasons and supporting records.; Check campaign dates, acquisition sources and promotional offers against the sales increase; compare available holiday sales history and merchant category.; Reconcile daily order and GMV totals to source transactions; check baseline completeness, duplicates and the new-account classification.; Inspect buyer account histories and purchase concentration, then compare settlement activity with fulfillment progress for evidence of extraction preceding non-delivery.

## Merchant 47 — alert episode 2024-12-22
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: reserve**

Merchant 47 triggered volume and new-account-share alerts on December 22. Trailing 30-day GMV was 273,198 cents across 24 orders; the preceding 90-day baseline contained 37 orders and 379,618 cents. Volume z was 3.1085, and new accounts contributed 48.06% of recent GMV. Recorded refunds and disputes were zero as of the cutoff.

These observations support investigation but do not establish bust-out. Holiday demand or an acquisition campaign could explain the increase, and the sparse baseline limits confidence. Zero recorded adverse events does not verify fulfillment or complete reporting.

Recommend a temporary payout reserve, with the percentage set by the human risk owner, while checking delivery evidence, refund requests, dispute records, campaign attribution and source-data completeness. Overdue unfulfilled orders, coordinated buyer activity and unexplained settlement extraction would strengthen bust-out concerns. Verified delivery, reconciled records and a documented campaign or seasonal explanation would support dismissing the alert and releasing the reserve. Escalate to a reversible settlement pause if corroborating evidence emerges; termination requires corroborated bust-out evidence.

Evidence gaps: Check fulfillment for recent orders, prioritizing new-account and high-value purchases: compare promised delivery dates with carrier acceptance, tracking and delivery evidence.; Reconcile refund metrics with processor records, cancellations, pending refund requests and customer complaints known by December 22.; Reconcile dispute counts with processor case records and ingestion logs as of the cutoff; identify any missing or unresolved cases.; Request campaign dates, spend and attributed orders, plus available prior holiday sales; test whether these explain the observed increase and buyer mix.; Recompute both windows from source transactions, checking duplicates, missing days and account classification; inspect buyer concentration and shared identifiers, and compare new-account share with available history.

## Merchant 140 — alert episode 2024-12-28
Triggers: AUP-06.1 warn: 30d chargeback rate 1.5% (3 disputes / 195 orders); AUP-06.2: volume z=4.8 vs baseline
**Recommended action: reserve**

Merchant 140 triggered volume and chargeback alerts as of December 28, 2024. Observed: 195 orders and $37,026.36 GMV over 30 days, volume z=4.82, and three disputes (1.54%). New-GMV share is 30.89%; recorded refunds are zero.

These signals warrant investigation but do not establish bust-out. Holiday demand or a marketing campaign could explain the increase. Zero recorded refunds do not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human risk owner under applicable policy. Prioritize the three disputed orders, then sample recent and new-buyer orders for delivery evidence. Reconcile refund requests and processor records, inspect buyer concentration, and obtain campaign documentation. Validate ingestion and the baseline calculation.

Repeated overdue non-delivery combined with concentrated thin-account purchasing would strengthen bust-out concern and support considering a settlement pause. Verified fulfillment and documented campaign or seasonal demand would support releasing the reserve and monitoring. A confirmed pipeline defect would require correcting and reassessing the alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reason codes, linked orders, duplication, and merchant responses; verify fulfillment evidence for those orders.; Sample recent orders, including new-buyer orders, for promised delivery dates and carrier delivery scans or equivalent completion evidence. Repeated overdue non-delivery would strengthen bust-out concern; verified delivery would weaken it.; Reconcile recorded zero refunds against payment-processor refunds, pending refund requests, cancellations, and customer complaints.; Request campaign dates and attributed sales, and compare available prior seasonal activity. A documented campaign or seasonal pattern with successful fulfillment would support a benign explanation.; Reconcile source order, dispute, and refund counts with the alert aggregates and check ingestion completeness in both windows; verify the volume-z calculation.; Inspect buyer-account history and concentration among recent orders to determine whether the increase involves thin or connected accounts.

## Merchant 4 — alert episode 2025-01-03
Triggers: AUP-06.1 breach: 30d chargeback rate 5.6% (3 disputes / 54 orders)
**Recommended action: reserve**

Merchant 4 triggered AUP-06.1 on January 3: three disputes across 54 trailing-30-day orders, a 5.6% chargeback rate. Volume_z is 2.53. Recorded refunds are zero; this does not prove successful delivery. New GMV share is 16.57%, which alone does not establish thin buyer accounts.

Recommend a percentage reserve while the human owner reviews the evidence. The breach warrants protection, but bust-out is uncorroborated. Seasonal demand or a marketing campaign could explain increased volume.

First inspect the three disputes and linked fulfillment records, sample recent deliveries, reconcile refund requests and source counts, and request dated campaign evidence. Repeated non-delivery, linked thin accounts and payouts against unfulfilled orders would strengthen bust-out concerns and support pausing settlement. Verified delivery, legitimate buyers and documented sales activity would weaken that hypothesis. Corrected source data could dismiss a measurement-driven alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records: unique IDs, reason codes, linked orders, delivery evidence and current status.; Check fulfillment for disputed orders and a small sample of recent orders using carrier acceptance, delivery confirmation and customer complaints; reconcile overdue orders against promised delivery dates.; Reconcile order, dispute and refund counts with source systems, including pending refund requests, ingestion failures and duplicates.; Request dated campaign records and comparable seasonal sales; check whether incremental orders align with campaign timing.; Inspect buyer account history and links among recent orders, then compare settlements with fulfillment obligations to test the thin-account and extraction hypothesis.

## Merchant 64 — alert episode 2025-01-04
Triggers: AUP-06.1 warn: 30d chargeback rate 1.6% (7 disputes / 445 orders); AUP-06.2: volume z=4.8 vs baseline
**Recommended action: reserve**

Merchant 64 triggered volume and chargeback warnings as of January 4, 2025. The trailing 30 days show 445 orders, $79,932.17 GMV, volume z=4.81, and seven disputes (1.57%). Recorded refunds are zero in both the trailing window and baseline. New GMV share is 20.96%; this does not establish thin buyer accounts.

Recommend a human-approved reserve, with its percentage set under existing policy, while reviewing the alert. The combination warrants payout protection, but the supplied metrics do not corroborate bust-out or justify termination.

Prioritize fulfillment checks on recent orders, review all seven disputes, and reconcile refund requests with recorded refunds. Check campaign records, holiday comparisons, buyer concentration, and source-data completeness.

Repeated overdue nondelivery, related disputes, and corroborated payout extraction would strengthen the bust-out hypothesis and support pausing settlement pending review. Verified deliveries and documented campaign or seasonal demand would weaken it. A source-data discrepancy could explain the alert and should prompt recalculation.

Evidence gaps: Sample recent orders from the elevated-volume period: verify promised delivery dates, carrier acceptance and delivery, and buyer confirmation where tracking is inconclusive. Widespread overdue nondelivery would strengthen bust-out concerns; verified fulfillment would weaken them.; Review the seven dispute records for reasons, associated order dates, fulfillment evidence, and outcomes known by January 4. Determine whether they concern nondelivery, unauthorized purchases, or other causes without assuming a dispute lag.; Reconcile zero recorded refunds with refund requests, cancellations, merchant support records, and processor events. Identify unresolved requests or ingestion omissions.; Check campaign and promotion dates, attributable orders, and comparable holiday periods. A documented demand increase accompanied by fulfillment would support a benign explanation.; Reconcile order counts, GMV, disputes, and refunds to source records; check duplicates and baseline completeness. Review buyer concentration and account history, and confirm what 'new' means before interpreting new_gmv_share.

## Merchant 106 — alert episode 2025-01-05
Triggers: AUP-06.1 warn: 30d chargeback rate 1.8% (5 disputes / 281 orders); AUP-06.2: volume z=4.3 vs baseline
**Recommended action: reserve**

As of January 5, 2025, merchant 106 triggered volume and chargeback warnings: volume z=4.28 and five disputes across 281 trailing-30-day orders (1.78%). Trailing GMV was 1,787,226 cents; new-GMV share was 29.47%. Recorded refunds were zero in both windows.

These are warning signals, not corroborated bust-out evidence. Seasonal demand or a campaign could explain the volume increase. New-GMV share does not establish thin buyer accounts, and zero refunds does not establish successful delivery.

Recommend a temporary payout reserve, with the percentage determined by the human reviewer, while checking the five disputes, recent fulfillment and refund requests. Reconcile source records and baseline coverage, and obtain campaign evidence.

Repeated overdue non-delivery, corroborating dispute records and concentrated sales to thin or linked buyers would strengthen the alert and support considering a settlement pause. Verified fulfillment, reconciled refunds and campaign or seasonal evidence explaining the increase would support releasing the reserve and monitoring. Offboarding is unsupported by the supplied evidence.

Evidence gaps: Review the five dispute records for reason, underlying order date, fulfillment evidence and status; determine whether they corroborate non-delivery.; Sample recent orders, including new-buyer orders, for promised delivery dates, carrier acceptance and delivery confirmation. Repeated overdue, unfulfilled orders would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile zero recorded refunds against refund requests, cancellations and processor records; check for unresolved requests or missing events.; Request campaign dates and attributable sales, and compare available prior seasonal periods. Matching demand growth with verified fulfillment would support a benign explanation.; Reconcile daily order, dispute and refund totals with source records across both windows; check missing baseline days, duplicates and ingestion gaps.; Inspect available buyer-account history and order concentration to test whether new sales involve thin or linked accounts.

## Merchant 117 — alert episode 2025-01-14
Triggers: AUP-06.1 breach: 30d chargeback rate 4.1% (3 disputes / 73 orders)
**Recommended action: reserve**

As of January 14, merchant 117 breached the chargeback trigger: 3 disputes among 73 trailing-30-day orders, or 4.1%. Volume_z is -0.6774 and ticket_drift is 0.9677; these do not support a sales or ticket ramp. New-GMV share is 17.3%. Zero recorded refunds does not establish successful fulfillment.

Recommend a payout reserve, with its percentage set by the human reviewer, while checking the breach. The observed dispute signal warrants protection, but current evidence does not establish bust-out or justify termination.

First reconcile dispute records and the order denominator. Review delivery evidence for disputed orders and a small recent sample, plus refund requests and pending refunds. Check campaign dates and seasonal explanations against actual sales and buyer history.

Repeated verified non-delivery alongside settlement extraction would strengthen the alert and support pausing payouts. Reliable fulfillment, resolved disputes, normal comparable rates, or a corrected data error would weaken it and support returning to monitoring.

Evidence gaps: Reconcile the three disputes to unique transactions, reason codes and current outcomes; verify the 73-order denominator and window completeness.; Check fulfillment and delivery evidence for disputed orders and a small recent-order sample. Repeated verified non-delivery would strengthen the bust-out hypothesis; reliable delivery would weaken it.; Reconcile recorded refunds with refund requests, cancellations and pending refunds; determine whether affected consumers were remedied.; Request dated campaign and seasonal-sales records, then compare resulting orders and buyer-account history with the alert window.; Compare historical and category-peer chargeback rates using consistent definitions; inspect recent settlement and fulfillment records for evidence of extraction followed by delivery failure.

## Merchant 1 — alert episode 2025-01-19
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 120 orders)
**Recommended action: monitor**

Merchant 1 triggered AUP-06.1 on January 19: three disputes across 120 trailing-30-day orders, a 2.5% chargeback rate. GMV was 1,292,896 cents. Volume_z was -2.0 and ticket_drift was 0.9844637732903062; these do not show the sales ramp typical of the described bust-out pattern. New buyers contributed 27.08% of GMV, but their account quality and historical share are unknown. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window while reviewing the three disputes, checking delivery evidence and overdue orders, reconciling source counts, and inspecting pending refund requests. Campaign records could explain buyer-mix changes if supported by attributable orders.

Repeated overdue non-delivery, unresolved refund requests and corroborated settlement extraction would strengthen bust-out concern and justify considering a reserve or settlement pause. Verified fulfillment, resolved disputes or a corrected data error would weaken the alert. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Inspect the three dispute records: reasons, linked orders, status and merchant responses. Corroborated non-delivery would strengthen bust-out concern; documented delivery or unrelated dispute reasons would weaken it.; Check tracking, delivery acknowledgments and promised delivery dates for disputed orders and a small recent-order sample; distinguish overdue fulfillment from orders still within their delivery promises.; Reconcile order and dispute counts against source records, checking duplicates, event dates and missing ingestion. A corrected rate could dismiss the metric breach.; Check refund requests, pending refunds and support complaints against the zero recorded refunds; unresolved non-delivery requests would increase concern.; Request campaign dates and attributable orders, and compare new-buyer share with prior periods. Verify buyer-account characteristics before treating new buyers as thin accounts.

## Merchant 95 — alert episode 2025-01-20
Triggers: AUP-06.1 breach: 30d chargeback rate 5.7% (3 disputes / 53 orders)
**Recommended action: reserve**

Merchant 95 triggered AUP-06.1 on January 20: three disputes across 53 trailing-30-day orders, a reported 5.7% rate. GMV was 326,267 cents. Volume z-score (-0.1205) and ticket drift (0.9595) do not show acceleration; new buyers accounted for 22.56% of GMV. No refunds were recorded, which does not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage and release conditions set by the human reviewer. The breach supports limiting exposure while checking the underlying cases; these metrics do not corroborate bust-out or justify offboarding.

First reconcile dispute IDs, order counts and ingestion completeness. Review each disputed order’s reason, promised delivery date and delivery evidence, then sample recent fulfillment. Check refund requests against processor records and verify any sales campaign and buyer concentration.

Confirmed non-delivery combined with thin-buyer concentration and settlement extraction would support escalation to a reversible settlement pause. Verified fulfillment, benign dispute explanations or a corrected rate would weaken the alert and support monitoring.

Evidence gaps: Reconcile the three unique dispute records and 53 orders against source records; verify timestamps, window inclusion, denominator definition and ingestion completeness.; Review dispute reasons, status and linked orders; obtain promised delivery dates and fulfillment evidence for all three disputed orders, plus a small sample of recent orders.; Check refund requests, cancellations, complaints and payment-processor refund records; determine whether zero recorded refunds reflects no requests, unresolved requests or missing ingestion.; Verify campaign dates, promotions and acquisition channels against order timing; inspect relevant buyer-account history and concentration.; Match settlement records to disputed and unfulfilled orders. Corroborated non-delivery, thin-buyer concentration and payout extraction would strengthen bust-out concerns; verified delivery or corrected records would weaken them.

## Merchant 15 — alert episode 2025-01-26
Triggers: AUP-06.1 breach: 30d chargeback rate 12.0% (3 disputes / 25 orders)
**Recommended action: reserve**

As of 2025-01-26, merchant 15 triggered AUP-06.1: three disputes across 25 trailing-30-day orders, a reported 12% chargeback rate. GMV was 396,013 cents. Volume_z was -1.887 and ticket_drift was 1.022; neither supports a sales ramp. New-buyer GMV share was 14.58%, which does not establish thin buyer accounts. Zero recorded refunds does not prove delivery.

Recommend a temporary percentage reserve, with the percentage set by the human reviewer under policy, while promptly validating the disputes and fulfillment. The dispute signal warrants protection, but corroborated bust-out evidence is absent.

First reconcile orders and disputes to source records. Inspect dispute reasons, delivery evidence, refund requests and processor refund records. Obtain campaign dates and compare them with disputed orders. Confirmed non-delivery combined with coordinated thin-account purchases and payout extraction would strengthen bust-out concerns. Verified fulfillment and documented campaign activity would weaken that hypothesis; corrected ingestion or duplicate records could dismiss the reported breach. The human reviewer owns the action.

Evidence gaps: Reconcile the three dispute records and 25 orders to source systems; verify unique disputes, event dates, denominator definition and ingestion completeness. Missing orders or duplicate disputes could dismiss the reported breach.; Inspect dispute reasons and linked orders, then request shipment tracking, delivery confirmation or service-completion evidence. Repeated non-delivery would strengthen bust-out concerns; independently verified fulfillment would weaken them.; Reconcile refund requests, pending refunds and completed refunds against support and processor records. Zero recorded refunds does not establish fulfillment.; Request dated campaign and seasonal-sales records and match them to disputed orders and buyer cohorts. Check buyer-account history and settlement records for coordinated purchases followed by payout extraction.

## Merchant 34 — alert episode 2025-01-27
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (4 disputes / 148 orders)
**Recommended action: monitor**

Merchant 34 breached the reported chargeback threshold: 4 disputes across 148 trailing-30-day orders, or 2.7%. Volume_z is -0.595 and ticket_drift is 0.979; these do not show the sales acceleration associated with a bust-out. Reported refunds are zero, which does not establish successful fulfillment.

Recommend monitor for the next window, with prompt human review of the current disputes. The breach is observed; bust-out remains a low-likelihood hypothesis on the supplied evidence.

Confirm the alert by reconciling unique disputes and order counts. Corroborated non-delivery, unresolved refund requests and concentration in thin buyer accounts would strengthen the bust-out case and support payout controls. Valid delivery evidence and resolved disputes would weaken that case; corrected source counts could dismiss the rate breach. Check campaign and seasonal records for a benign explanation. A human owns any action; offboarding is unsupported without corroborated bust-out evidence.

Evidence gaps: Review the four dispute records for unique cases, reason codes, linked orders and available merchant responses; corroborated non-delivery would strengthen the bust-out hypothesis.; Check tracking and delivery evidence for disputed orders and a small sample of recent orders; consistent delivery would weaken the hypothesis.; Reconcile refund requests, pending refunds and completed refunds against the reported zero refunds; unresolved requests tied to non-delivery would increase concern.; Reconcile dispute and order counts with source records and confirm ingestion completeness; corrected counts could confirm or dismiss the rate breach.; Check campaign dates, promotions and prior comparable seasonal periods, then inspect available buyer-account history for recent orders; new_gmv_share alone does not establish thin accounts.

## Merchant 49 — alert episode 2025-01-27
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (3 disputes / 103 orders)
**Recommended action: monitor**

Merchant 49 breached the chargeback trigger: 3 disputes among 103 trailing-30-day orders (2.9%). Volume_z is -0.868 and ticket_drift is 0.988, so the supplied comparisons show no sales or ticket ramp. New GMV share is 17.05%; buyer-account quality is unknown. No refunds are recorded, which does not establish satisfactory fulfillment.

Recommend monitor for the next window, with prompt human review of the three disputes. Reconcile source counts, inspect dispute reasons and delivery evidence, and check refund requests and campaign records. Verified counts confirm the threshold breach; corrected counts below threshold dismiss it. Repeated non-delivery involving coordinated thin buyer accounts would strengthen bust-out concern and support considering a reserve or reversible settlement pause. Documented fulfillment and isolated dispute explanations would weaken that concern. Current evidence does not support offboarding.

Evidence gaps: Reconcile the three disputes and 103 orders against source records through January 27; verify unique cases, denominator completeness, dispute reasons and statuses. Corrected counts could dismiss the threshold breach.; Check fulfillment and delivery evidence for the disputed orders and a small sample of recent orders. Repeated verified non-delivery would strengthen bust-out concern; documented delivery would weaken it.; Reconcile refund requests, pending refunds and completed refunds with support and payment records. Zero recorded refunds does not establish absence of customer problems.; Check campaign and seasonal calendars against order patterns, and inspect buyer-account history and concentration. Documented promotions with fulfilled orders support a benign explanation; coordinated thin accounts with non-delivery support escalation.

## Merchant 6 — alert episode 2025-01-30
Triggers: AUP-06.1 breach: 30d chargeback rate 2.8% (5 disputes / 179 orders)
**Recommended action: monitor**

Merchant 6 triggered AUP-06.1 on January 30: five disputes across 179 trailing-30-day orders, a 2.8% chargeback rate. GMV was 1,074,780 cents; volume_z was -1.56 and ticket_drift was 0.96. These comparisons do not support the sales acceleration expected in the described bust-out pattern. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window, with prompt review of the five disputes, delivery evidence and refund requests. Bust-out remains a hypothesis, not an observed finding. Seasonal activity is possible but unsubstantiated; a pipeline issue also requires verification.

Distinct non-delivery disputes, unresolved refunds and concentrated thin buyer accounts would strengthen concern and support reconsidering payout controls. Verified delivery, resolved disputes or a corrected data error would weaken the alert. Check campaign records for context. A human owns any action; these metrics do not corroborate bust-out sufficiently to justify offboarding.

Evidence gaps: Review the five dispute records for reason, status, transaction date and shared buyers; confirm they are distinct and reconcile the numerator and denominator.; Check delivery evidence for disputed orders and a small sample of recent orders; corroborated non-delivery would strengthen concern, while verified fulfillment would weaken it.; Reconcile refund requests, pending refunds and processed refunds against the zero recorded refunds; check unresolved customer complaints.; Check order, dispute and refund ingestion completeness through the alert date and recompute the rate after any corrections.; Review existing campaign and seasonal-sales records alongside daily orders and buyer-account history; a documented campaign with verified delivery would support a benign explanation.

## Merchant 147 — alert episode 2025-01-31
Triggers: AUP-06.2: volume z=3.4 vs baseline; AUP-06.4: new-account GMV share 79%
**Recommended action: reserve**

Merchant 147 triggered volume and new-account concentration alerts as of January 31, 2025. Trailing 30-day GMV was $15,632.26 across 50 orders; new accounts contributed $12,351.14 (79.0%). Volume z was 3.38. The baseline contains only 45 days and 44 orders. Recorded refunds and disputes were zero; these counts do not establish successful fulfillment.

A bust-out is plausible but uncorroborated. A marketing campaign could explain the same pattern; seasonal demand and data errors also remain possible.

Recommend a proportionate payout reserve, with the percentage set by the human reviewer, pending prompt checks. Confirm delivery on a targeted order sample, reconcile refund requests and dispute records, verify campaign attribution, and check source-data completeness. Repeated overdue non-delivery combined with coordinated buyer accounts and settlement extraction would strengthen the bust-out hypothesis. Verified delivery, genuine campaign-driven buyers and reconciled records would support dismissing the alert and releasing the reserve. Offboarding is unsupported by the current evidence.

Evidence gaps: Sample recent orders, prioritizing new accounts and high-value purchases: compare promised delivery dates with carrier acceptance, delivery confirmation and customer complaints.; Reconcile refund requests, cancellations and pending refunds against the reported zero completed refunds; inspect dispute-provider records and ingestion completeness through the alert date.; Request campaign dates, spend, acquisition channels and attributed orders; check whether documented campaigns explain the timing and new-account GMV.; Review existing buyer-account linkage signals and payout records for coordinated purchasing and settlement extraction.; Reconcile daily order and GMV totals with source records; verify baseline coverage, account-age classification and missing or duplicated events.

## Merchant 37 — alert episode 2025-02-01
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (4 disputes / 124 orders)
**Recommended action: reserve**

Merchant 37 breached AUP-06.1: four disputes across 124 trailing-30-day orders, a 3.23% chargeback rate. GMV was 2,742,346 cents. Volume_z was -3.12, ticket_drift was 0.944, and new_gmv_share was 17.98%. These observations do not establish a bust-out sales ramp. Zero recorded refunds does not establish successful fulfillment.

Recommend a proportionate payout reserve, with the percentage determined by verified exposure and applicable policy, pending prompt human review. The dispute breach supports caution; the supplied metrics do not corroborate bust-out or justify termination.

Confirm the alert by validating distinct dispute records and the order denominator. Repeated missed fulfillment, credible non-delivery complaints, poor-quality buyer concentration and payout extraction would strengthen the bust-out hypothesis. Verified delivery, resolved disputes and documented campaign or seasonal explanations would weaken it. Duplicate disputes or missing order ingestion could dismiss the threshold breach after recalculation. Check fulfillment evidence, refund requests and processor logs before deciding whether to release the reserve or escalate.

Evidence gaps: Inspect the four dispute records for distinct transactions, reason codes, delivery allegations and outcomes; reconcile the 124-order denominator and ingestion completeness.; Check shipment, delivery or service-completion evidence for disputed orders and a small recent-order sample; compare promised dates with actual fulfillment.; Reconcile the zero recorded refunds against refund requests, pending refunds, processor records and customer-support complaints.; Review campaign dates, promotions and seasonal sales history; examine buyer-account quality and concentration behind recent orders.; Review recent payout and settlement records alongside fulfillment obligations to assess exposure and set a proportionate reserve percentage.

## Merchant 59 — alert episode 2025-02-02
Triggers: AUP-06.1 breach: 30d chargeback rate 3.3% (5 disputes / 151 orders)
**Recommended action: reserve**

Merchant 59 triggered AUP-06.1 on February 2, 2025: five disputes across 151 trailing-30-day orders, a 3.31% chargeback rate. Observed volume_z is -1.81, ticket_drift is 1.086, and new_gmv_share is 25.21%. Recorded refunds are zero; that does not establish successful fulfillment or absence of refund requests.

Recommend a temporary payout reserve, with its percentage set by the human reviewer under policy, while checking the five disputes and associated fulfillment records. The chargeback breach warrants protection, but the metrics do not establish a bust-out sales ramp.

Confirm concern through repeated overdue non-delivery, unresolved refund requests and corroborating buyer or settlement patterns. Weaken or dismiss the alert through verified deliveries, resolved or invalid disputes, or a corrected denominator that removes the breach. Check campaign records for a documented benign buyer-mix change. Broader corroborated fulfillment failures could justify pausing settlement; offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the five dispute records: verify unique cases, reason codes, associated orders and outcomes; reconcile the 151-order denominator with source records.; Check tracking, delivery confirmation and promised delivery dates for disputed orders and a small sample of recent orders. Repeated overdue non-delivery would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile refund requests, cancellations and pending refunds against the recorded zero refunds; check whether customer requests remain unresolved.; Review campaign dates, promotion records and acquisition sources for changes in buyer mix; compare with available seasonal history.; If fulfillment failures are corroborated, inspect linked buyer accounts and settlement withdrawals for coordinated purchasing and extraction.

## Merchant 143 — alert episode 2025-02-13
Triggers: AUP-06.1 breach: 30d chargeback rate 5.7% (3 disputes / 53 orders)
**Recommended action: reserve**

Merchant 143 triggered AUP-06.1 on February 13: three disputes across 53 trailing-30-day orders, a 5.66% reported chargeback rate. GMV was 2,541,576 cents. Volume_z is -0.963 and ticket_drift is 1.006; these comparisons do not show the ramp or ticket expansion expected in the described bust-out pattern. Recorded refunds are zero, which does not establish successful fulfillment.

Recommend a provisional payout reserve, with the percentage set by the human reviewer under applicable policy, while completing focused checks. The dispute breach supports caution, but the supplied evidence does not establish bust-out or justify termination.

First verify the three dispute records and fulfillment of those orders, then sample recent deliveries, reconcile refund requests, and check campaign records and transaction ingestion. Repeated verified non-delivery alongside linked thin buyer accounts would strengthen bust-out and support considering a settlement pause. Documented delivery, isolated disputes, or a corrected data denominator would weaken the alert and support returning to monitoring.

Evidence gaps: Inspect the three dispute records for distinct order IDs, reasons, amounts, status, and supporting evidence; reconcile them to processor records available by the alert date.; Check shipment, carrier delivery, and customer communications for disputed orders plus a small recent-order sample. Repeated verified non-delivery would support bust-out; documented fulfillment would weaken it.; Reconcile refund requests and pending or completed refunds against support tickets and processor records; zero recorded refunds does not establish zero customer complaints.; Reconcile the 53 orders and GMV to source transactions, checking ingestion completeness, timestamps, duplicates, and cancellations. Corrected counts could dismiss the metric breach.; Review dated campaign or promotion records and buyer-account histories for recent orders, checking whether legitimate acquisition explains activity or linked thin accounts support coordinated purchasing.

## Merchant 85 — alert episode 2025-02-16
Triggers: AUP-06.1 breach: 30d chargeback rate 5.0% (3 disputes / 60 orders)
**Recommended action: reserve**

As of 2025-02-16, merchant 85 breaches AUP-06.1: three disputes across 60 trailing-30-day orders produce a 5.0% chargeback rate. GMV is 507927 cents; volume_z is 1.79, ticket_drift is 1.06, and new-GMV share is 15.50%. No refunds are recorded.

Recommend a temporary payout reserve, with the percentage set by the human risk owner, while checking the three disputes and recent fulfillment. These observations warrant review but do not establish a bust-out.

Repeated non-delivery, unresolved refund requests and settlement extraction would corroborate the concern and support stronger action. Verified delivery, explained disputes and a documented campaign would weaken it. Reconcile source records before treating zero refunds as reassuring; missing orders or duplicate disputes could change the breach. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reasons, affected orders, duplicates and status; determine whether they concern non-delivery or another cause.; Check shipment tracking, delivery evidence and promised fulfillment dates for disputed orders and a small sample of recent orders. Repeated unfulfilled orders would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile the zero recorded refunds against processor records, refund requests and pending refunds; identify any unresolved non-delivery complaints.; Reconcile dispute and order source records to the trailing window, checking ingestion completeness, timestamps and denominator construction. Corrected counts could dismiss the metric breach.; Request dated campaign or seasonal-promotion records and compare them with the sales increase and buyer cohorts; inspect settlement withdrawals alongside fulfillment failures if those failures are confirmed.

## Merchant 26 — alert episode 2025-02-22
Triggers: AUP-06.1 breach: 30d chargeback rate 5.9% (3 disputes / 51 orders)
**Recommended action: reserve**

As of 2025-02-22, merchant 26 breaches the reported chargeback threshold: 3 disputes across 51 trailing-30-day orders (5.9%). GMV is 967,910 cents. Volume_z is −2.07, which argues against a sales ramp; ticket_drift is 1.095. Zero recorded refunds does not establish satisfactory fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer under policy, while checking the three disputes, delivery evidence and refund records. These metrics establish dispute exposure but do not corroborate bust-out.

Repeated overdue non-delivery, unsupported fulfillment claims or linked suspicious buyers would strengthen the bust-out hypothesis. Verified delivery, isolated non-fulfillment-unrelated disputes, or corrected ingestion errors would weaken it. Check campaign timing and affected orders for a benign explanation. Reconcile order, dispute and refund feeds before relying on the rate or refund zeros.

The human reviewer owns the action. Escalate to a reversible settlement pause if checks reveal ongoing non-delivery and payout exposure; offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for reasons, order linkage, dates and duplicates; reconcile the 51-order denominator and ingestion completeness.; Check promised delivery dates and tracking or customer receipt for disputed orders and a small sample of recent orders; identify overdue unfulfilled orders.; Reconcile refund requests, approvals, pending refunds and completed refunds against processor records to validate the reported zeros.; Check campaign dates, promotions and affected orders; compare dispute reasons and fulfillment within the campaign cohort.

## Merchant 3 — alert episode 2025-02-27
Triggers: AUP-06.1 breach: 30d chargeback rate 4.0% (3 disputes / 75 orders)
**Recommended action: reserve**

As of 2025-02-27, merchant 3 triggered AUP-06.1 with three disputes across 75 trailing-30-day orders (4.0%). Recorded refunds are zero. Volume_z is -1.22, so the metrics do not show the sales ramp expected in the described bust-out pattern.

Recommend a temporary payout reserve, with the percentage set by the human reviewer under policy, while completing a focused review. The breach supports precaution; it does not establish bust-out.

First reconcile dispute records and order ingestion, then verify fulfillment for disputed orders and a small recent-order sample. Check pending refund requests and campaign-linked sales. Confirmed non-delivery, coordinated thin buyers and settlement extraction would strengthen the bust-out hypothesis and support pausing settlement pending review. Validated delivery and an explained dispute cluster, or corrected source data removing the breach, would weaken the alert and support monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records for reason codes, order links, duplicate entries, status and merchant responses; verify the 75-order denominator and completeness of both comparison windows.; Check carrier-confirmed delivery or service completion for disputed orders and a small recent-order sample; compare promised fulfillment dates with actual outcomes.; Reconcile platform refunds with merchant refund requests, cancellations and pending refunds; zero recorded refunds does not establish customer satisfaction.; Request campaign dates and order attribution; examine available buyer history and linked-account patterns to test whether new buyers are thin or coordinated.; Review existing payout records alongside fulfillment failures for evidence of settlement extraction.

## Merchant 82 — alert episode 2025-02-28
Triggers: AUP-06.1 breach: 30d chargeback rate 5.9% (3 disputes / 51 orders)
**Recommended action: reserve**

Merchant 82 triggered AUP-06.1 at a reported 5.9% chargeback rate: three disputes across 51 trailing-30-day orders. GMV was 2,279,172 cents; volume_z was -1.5394. These observations establish dispute concern but do not show the sales ramp associated with the described bust-out pattern. Reported refunds were zero, which does not establish successful fulfillment.

Recommend a payout reserve, with the percentage set by the human reviewer under applicable policy, while conducting targeted checks. Current evidence does not justify irreversible offboarding.

Review all three disputes and verify delivery for disputed orders plus a small recent-order sample. Reconcile refund requests and processor records, campaign activity, buyer concentration and pipeline totals.

Verified non-delivery, unresolved refunds and concentrated thin buyer accounts alongside settlement extraction would strengthen the bust-out hypothesis and support considering a payout pause. Verified fulfillment and resolved disputes would reduce that concern. A corrected numerator or denominator could dismiss the metric breach; campaign evidence alone would not dismiss fulfillment risk.

Evidence gaps: Inspect all three dispute records: reasons, status, duplicates, linked orders and transaction dates; reconcile the reported 3/51 rate and confirm the policy denominator.; Check fulfillment for disputed orders and a small sample of recent orders using promised delivery dates, carrier delivery records and customer confirmation.; Reconcile refund requests, cancellations and processor refund records against the reported zero refunds; identify any unresolved requests.; Request dated campaign records and compare campaign-linked orders, buyer concentration and available account-history indicators.; Reconcile source order, GMV and dispute totals with the alert pipeline, checking missing events and window boundaries.

## Merchant 149 — alert episode 2025-03-06
Triggers: AUP-06.2: volume z=4.3 vs baseline; AUP-06.4: new-account GMV share 81%
**Recommended action: reserve**

As of March 6, merchant 149 has a volume z-score of 4.29 and 81.43% new-account GMV. Trailing sales total 1,770,600 cents across 49 orders, versus 678,172 cents across 24 baseline orders. The merchant is 59 days old, with only 30 baseline days available. One dispute and zero recorded refunds provide limited evidence about fulfillment.

Recommend a provisional payout reserve while conducting a focused review. The combined triggers warrant protection, but do not establish bust-out or justify termination. Set the reserve percentage through the human review process.

Verify delivery on recent high-value and new-account orders, reconcile refund requests and processor disputes, and inspect dated campaigns and source-data completeness. Coordinated buyers plus verified nonfulfillment or fabricated delivery evidence would corroborate bust-out and support escalation. Verified fulfillment, reconciled records and a documented acquisition campaign or seasonal explanation would weaken the alert. A confirmed ingestion or classification defect would support correcting and recalculating the metrics before reassessing.

Evidence gaps: Sample recent high-value and new-account orders: verify promised delivery dates, carrier acceptance and delivery, or independently verifiable service completion.; Reconcile refund requests, cancellations and support complaints with recorded refunds; determine whether requests remain unresolved.; Inspect the single dispute's reason, underlying order and fulfillment evidence; reconcile processor dispute records with ingestion.; Check dated campaign records, acquisition channels and category seasonality against the sales increase.; Reconcile order and settlement totals against source records, confirm baseline completeness, and validate the new-account definition and classification.

## Merchant 89 — alert episode 2025-03-10
Triggers: AUP-06.1 breach: 30d chargeback rate 6.2% (3 disputes / 48 orders)
**Recommended action: reserve**

As of March 10, merchant 89 triggered AUP-06.1 with three disputes across 48 trailing-30-day orders, a 6.25% chargeback rate. GMV was 243,571 cents. Volume_z was slightly negative and ticket_drift was below 1; the metrics do not show the sales ramp associated with the described bust-out pattern. Reported refunds were zero, which does not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human risk owner, while conducting a focused review. The chargeback signal warrants protection, but three disputes provide limited evidence about merchant intent.

First validate dispute records, order linkage and the denominator. Then check delivery against promised dates, pending refund requests and campaign records. Repeated overdue non-delivery, unresolved refunds and concerning buyer-account histories would strengthen bust-out concern and support considering a settlement pause. Verified fulfillment and legitimate campaign activity would weaken that hypothesis; a data correction removing the breach would dismiss the trigger. Offboarding lacks corroborated support.

Evidence gaps: Inspect the three dispute records for reason, status, order linkage and duplication; reconcile the 48-order denominator and ingestion completeness. Invalid records or a corrected denominator could dismiss the breach.; Check promised delivery dates and carrier or customer-confirmed fulfillment for disputed orders and a small sample of other recent orders. Repeated overdue non-delivery would strengthen bust-out concern; verified delivery would weaken it.; Reconcile refund requests, cancellations and processor refunds against the reported zero refunds. Unprocessed requests accompanying non-delivery would increase concern.; Request campaign dates and supporting sales records; inspect buyer-account history for the disputed orders. Documented acquisition activity with successful fulfillment would support a benign explanation.

## Merchant 14 — alert episode 2025-03-16
Triggers: AUP-06.1 breach: 30d chargeback rate 3.2% (5 disputes / 155 orders)
**Recommended action: monitor**

Merchant 14 triggered the chargeback breach on 2025-03-16: five disputes across 155 trailing-30-day orders (3.23%). Volume_z is -2.86, ticket_drift is 1.034, and new-GMV share is 20.97%. Recorded refunds are zero; this does not establish successful fulfillment.

The dispute signal merits review, but these metrics do not demonstrate the sales ramp or non-delivery pattern associated with bust-out. Recommend monitoring the next window while promptly validating this episode; a human owns the action.

Confirm the alert calculation by reconciling dispute and order records. Duplicates or incorrect window assignment could dismiss the calculated breach. Verified records would confirm it, without proving bust-out.

Review disputed-order delivery evidence, sample recent fulfillment, reconcile refund requests and processor records, and check campaign dates and buyer cohorts. Widespread non-delivery, unresolved refunds and suspicious buyer activity would strengthen bust-out concerns and support a reserve or reversible settlement pause. Verified deliveries and a documented seasonal or campaign explanation would weaken those concerns, although a valid chargeback breach would remain. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the five disputes and 155 orders to source records; verify uniqueness, window assignment, reason codes and ingestion completeness.; Check fulfillment and delivery evidence for the disputed orders, then sample recent undisputed orders for failed or overdue delivery.; Reconcile recorded zero refunds against refund requests, pending refunds and processor records.; Obtain campaign dates, acquisition channels and seasonal sales history; compare disputes and fulfillment across affected cohorts.; Check baseline and category chargeback rates, plus buyer-account history, to assess whether the rate and buyer mix are unusual.

## Merchant 29 — alert episode 2025-03-27
Triggers: AUP-06.1 breach: 30d chargeback rate 8.6% (3 disputes / 35 orders)
**Recommended action: reserve**

As of 2025-03-27, merchant 29 triggered AUP-06.1: three disputes across 35 trailing-30-day orders, an 8.6% rate. GMV was 804,468 cents. Volume_z was 0.78, ticket_drift was 1.052, and new-GMV share was 14.0%; these provide limited support for a bust-out sales ramp. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer after assessing exposure. The dispute breach merits protection, but the supplied evidence does not corroborate bust-out.

First inspect all three dispute records and reconcile their order links and the denominator. Check promised delivery dates, fulfillment proof, pending refund requests and campaign records.

Repeated overdue non-delivery, corroborated dispute reasons and thin or linked buyer activity would strengthen the bust-out hypothesis and could justify pausing settlement. Corrected source records or documented fulfillment with resolved disputes would weaken the alert. A legitimate campaign may explain sales changes but does not alone explain disputes. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: reason codes, linked orders, duplicate status, event dates and merchant responses; reconcile numerator and denominator to source records as of 2025-03-27.; Check promised delivery dates and shipment, delivery or service-completion evidence for disputed orders and a small sample of recent orders; distinguish overdue fulfillment from orders still within their promised dates.; Reconcile the zero recorded refunds against the refund ledger, pending requests and customer complaints, especially for disputed or overdue orders.; Request campaign dates and promotion records; compare resulting orders with fulfillment outcomes and check available category dispute benchmarks.; If fulfillment failures emerge, inspect buyer-account quality and concentration to determine whether sales involve thin or linked accounts.

## Merchant 69 — alert episode 2025-03-29
Triggers: AUP-06.1 breach: 30d chargeback rate 8.3% (3 disputes / 36 orders)
**Recommended action: reserve**

As of March 29, merchant 69 breached the reported chargeback threshold: three disputes across 36 trailing-30-day orders (8.3%). Volume_z is -0.635, so the metrics do not show a sales ramp. Ticket_drift is 1.253; new_gmv_share is 34.9%. Neither establishes thin buyer accounts. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary payout reserve, with its percentage set by the human reviewer, while completing inexpensive checks. Bust-out remains a low-likelihood hypothesis; campaign effects, seasonality and a reporting defect require verification.

First reconcile dispute cases and the order denominator, inspect dispute reasons and delivery evidence, and sample recent fulfillment. Check pending refunds, returns and complaints, then obtain campaign records.

Multiple verified non-delivery cases, overdue fulfillment and suspicious buyer concentration or settlement extraction would corroborate bust-out and support pausing settlement. Corrected reporting that removes the breach, or verified fulfillment with resolved disputes and a documented benign sales explanation, would support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for unique cases, linked orders, reasons, event dates, delivery evidence and outcomes; determine whether they indicate non-delivery or unrelated issues.; Reconcile the 36 orders and three disputes to source records, checking window boundaries, duplicates, missing ingestion and denominator eligibility.; Check fulfillment status and carrier delivery evidence for disputed orders and a small recent-order sample; identify overdue or unshipped orders.; Reconcile zero recorded refunds with return requests, cancellations, pending refunds and support complaints.; Request campaign dates and promoted products, then compare sales mix with campaign records and prior seasonal periods; inspect buyer-account concentration and settlement records if fulfillment concerns emerge.

## Merchant 104 — alert episode 2025-03-29
Triggers: AUP-06.1 breach: 30d chargeback rate 6.5% (3 disputes / 46 orders)
**Recommended action: reserve**

As of March 29, the alert reflects three disputes across 46 trailing-30-day orders, a 6.5% chargeback rate and stated AUP-06.1 breach. GMV was 258944 cents. Volume_z was -0.2165, ticket_drift was 0.8704, and new GMV share was 7.6%; these do not support a bust-out sales ramp. No refunds were recorded, which does not establish successful fulfillment.

Recommend a temporary, policy-sized payout reserve for human review because the dispute breach creates exposure, while bust-out remains uncorroborated. First reconcile the disputes and order denominator, then inspect fulfillment, refund requests and campaign records.

Verified non-delivery across recent orders, unresolved refunds and corroborated settlement extraction would strengthen the bust-out hypothesis and support pausing settlement. Documented fulfillment, explainable disputes and a reconciled benign campaign pattern would weaken it. A corrected rate below the trigger threshold would dismiss the metric breach. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes with processor records, checking unique cases, merchant attribution, reason codes, order linkage and completeness of the 46-order denominator.; Check delivery or service-completion evidence for the disputed orders and a small sample of recent orders; inspect overdue fulfillment and customer complaints.; Reconcile zero recorded refunds with processor refunds, cancellations and pending refund requests.; Check dated sales campaigns and category or seasonal comparisons for patterns explaining the affected orders.

## Merchant 120 — alert episode 2025-03-31
Triggers: AUP-06.2: volume z=3.3 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: monitor**

As of 2025-03-31, merchant 120 triggered volume z=3.303 and new-account GMV share=44.449%. The trailing 30 days contain 22 orders and 380015 cents GMV; the preceding 90-day baseline contains 33 orders and 548908 cents. Ticket drift is 1.0385. Reported trailing refunds and disputes are zero, but those counts do not establish successful fulfillment.

Recommend monitor, with prompt verification and review of the next window. The joint signals warrant investigation, but the small order count and absence of corroborated delivery failures do not currently justify stopping payouts. A human owns the action.

Check recent fulfillment, outstanding refund requests, processor disputes, campaign attribution and source-data completeness. Overdue or fictitious deliveries, linked thin buyers and settlement extraction accompanying the ramp would strengthen the bust-out hypothesis. Verified deliveries and reconciled records, together with campaign or seasonal attribution, would support dismissing the alert. A corrected pipeline that removes the triggers would support a data explanation. Consider reserve or reversible pause_settlement if checks reveal material exposure or corroborated nonfulfillment; offboarding requires corroborated bust-out evidence.

Evidence gaps: Sample recent orders, prioritizing new-account GMV: verify promised delivery dates, tracking, delivery confirmation and customer receipt; identify overdue or fictitious fulfillment.; Reconcile reported refunds with refund requests, cancellations and processor records; check whether unresolved requests are absent from the zero-refund aggregate.; Check processor dispute records and customer complaints against order IDs as of 2025-03-31; verify ingestion completeness without assuming a dispute-reporting delay.; Request campaign dates and order-level attribution; compare sales timing with promotions and relevant prior seasonal periods.; Reconcile daily source orders and GMV to both windows; verify baseline coverage and new-account classification, then inspect buyer concentration and linked-account indicators.

## Merchant 21 — alert episode 2025-04-02
Triggers: AUP-06.1 breach: 30d chargeback rate 3.0% (5 disputes / 168 orders)
**Recommended action: reserve**

Merchant 21 breached the chargeback trigger: 5 disputes across 168 trailing-30-day orders, a 2.98% rate. GMV was 1,202,675 cents. Volume_z was -0.96 and ticket_drift was 0.885; neither supports the sales ramp described in a bust-out. Recorded refunds were zero, which does not establish fulfillment.

Recommend a provisional payout reserve, with the percentage set by the human risk owner, while reviewing the five cases. The breach warrants protection, but the supplied evidence does not establish bust-out or justify termination.

First reconcile dispute IDs, order counts and ingestion completeness. Review dispute reasons, promised delivery dates, independent delivery records and customer communications; reconcile refund requests with processor records. Check campaign dates and promises for affected orders.

Repeated non-delivery, unresolved refunds and accelerated settlement extraction would strengthen the bust-out hypothesis and support considering a settlement pause. Verified fulfillment with campaign-related explanations would weaken it; corrected counts below the threshold would dismiss the reported rate breach. The human risk owner owns the action.

Evidence gaps: Reconcile the 5 disputes and 168 orders to source records as of the alert cutoff; verify unique dispute IDs, order associations, window definitions and ingestion completeness. Corrected counts below the breach would dismiss the reported rate alert.; Review reason codes and case records for all 5 disputes, alongside carrier-confirmed delivery, promised delivery dates and customer communications. Repeated non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Check refund requests, cancellations and processor refund records against the zero recorded refunds. Unresolved requests would increase concern; omitted completed refunds would identify a reporting gap.; Review existing campaign calendars, promotions and advertised delivery promises for affected orders. A documented campaign with verified fulfillment would support a benign explanation.; If non-delivery is corroborated, compare affected sales and payout records for accelerated settlement extraction before recommending stronger action.

## Merchant 31 — alert episode 2025-04-03
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (3 disputes / 117 orders)
**Recommended action: monitor**

As of 2025-04-03, merchant 31 triggered the reported AUP-06.1 chargeback breach: 3 disputes across 117 trailing-30-day orders (2.6%). Volume_z is -0.683 and ticket_drift is 0.963, providing no evidence of a sales or ticket ramp. Recorded refunds are zero; this does not establish that customers have no unresolved refund requests.

Recommend monitor, with prompt human review of the three disputes. Bust-out remains a low-likelihood hypothesis on the supplied evidence. A campaign-related service issue or recording error remains possible but unverified.

First reconcile dispute records and the order denominator, then inspect fulfillment evidence for disputed and sampled recent orders. Check refund requests against processing records and compare campaign dates and acquisition sources with affected orders. Verified non-delivery combined with settlement extraction and thin-account concentration would corroborate bust-out and support stronger action. Valid delivery evidence, resolved disputes or corrected source records would weaken or dismiss the alert. Repeated unresolved non-delivery would support considering a reversible settlement pause pending review; offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for unique IDs, merchant attribution, reason codes, order dates and resolution; reconcile the 117-order denominator and feed completeness.; Check delivery or service-completion evidence for disputed orders and a small recent-order sample. Repeated verified non-delivery would strengthen the bust-out hypothesis; verified fulfillment would weaken it.; Reconcile zero recorded refunds against refund requests, approvals and processing records; check for unresolved cancellations or refunds.; Check campaign dates, promotions and acquisition sources against orders and disputes. Documented campaigns with fulfilled orders would support a benign explanation.; If non-delivery is corroborated, inspect payout records and buyer-account history for settlement extraction and concentration in thin accounts.

## Merchant 35 — alert episode 2025-04-04
Triggers: AUP-06.1 breach: 30d chargeback rate 3.7% (3 disputes / 81 orders)
**Recommended action: reserve**

As of April 4, 2025, merchant 35 triggered B: three disputes across 81 trailing-30-day orders, a 3.7% chargeback rate. GMV was 4,307,447 cents. Volume z-score was −0.363, ticket drift 1.088, and new-buyer GMV share 18.9%. Recorded refunds were zero in both windows.

The dispute trigger warrants review, but the metrics do not establish a bust-out: there is no observed volume ramp, and fulfillment failures, thin buyer accounts and settlement extraction remain unverified. Zero recorded refunds does not prove satisfactory delivery.

Recommend a temporary, proportionate payout reserve, with percentage and implementation owned by the human reviewer. Verify the three dispute records, delivery evidence, pending refund requests and source-system completeness first; obtain campaign attribution alongside these checks.

Confirmed widespread overdue non-delivery, unresolved complaints and coordinated thin-account purchasing would strengthen the alert and support pausing settlement. Verified fulfillment, resolved disputes or corrected source counts would weaken it and support monitoring or reserve release. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three underlying dispute records for uniqueness, reason, amount, linked order, status and merchant response; confirmed non-delivery would strengthen concern, while duplicates or resolved delivery claims would weaken it.; Check promised delivery dates and tracking or delivery evidence for disputed orders and a small sample of recent orders; widespread overdue non-fulfillment would support escalation.; Reconcile the 81 orders, three disputes and zero refunds against processor and order-system records; inspect pending refund requests and complaints to distinguish absent refunds from missing or delayed recording.; Request recent campaign dates, promotion details and order attribution; documented campaigns paired with verified fulfillment would support a benign explanation.; Review unsettled payouts and unfulfilled-order exposure to size a proportionate reserve; inspect linked buyer histories before treating new-buyer share as thin-account evidence.

## Merchant 98 — alert episode 2025-04-04
Triggers: AUP-06.1 breach: 30d chargeback rate 7.1% (3 disputes / 42 orders)
**Recommended action: reserve**

Merchant 98 triggered a reported AUP-06.1 breach: three disputes among 42 trailing-30-day orders, a 7.1% rate. Volume_z is -2.2033 and ticket_drift is 0.9407, which do not support a sales ramp. Recorded refunds are zero; that does not establish successful fulfillment.

Recommend a temporary reserve, with the percentage determined by the human owner under applicable policy, while conducting a focused review. Current evidence does not corroborate bust-out or justify offboarding.

First reconcile dispute and order records, then inspect dispute reasons, delivery evidence, refund requests and associated settlements. Verify campaign dates and buyer-account patterns. Repeated substantiated non-delivery combined with coordinated thin accounts and settlement extraction would strengthen bust-out suspicion and support considering a payout pause. Verified delivery, explained disputes and documented campaigns would weaken that hypothesis. A corrected denominator or duplicate disputes could dismiss the metric breach; campaign activity alone would not dismiss genuine fulfillment failures.

Evidence gaps: Review the three dispute records for unique order IDs, reasons, dates, status and supporting evidence; distinguish non-delivery from other dispute causes.; Reconcile the 42 orders and three disputes to source records, checking ingestion completeness, duplicates and window assignment.; Check fulfillment evidence for disputed orders and a small sample of recent high-value and new-buyer orders: tracking, delivery confirmation and customer contacts.; Reconcile recorded zero refunds against refund requests, pending refunds, cancellations and processor records.; Request campaign dates and promotion records; compare affected orders with campaign cohorts and prior comparable seasonal periods.; Check disputed and recent orders for shared buyer identifiers and available account-history indicators; reconcile associated merchant settlements.

## Merchant 12 — alert episode 2025-04-08
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 118 orders)
**Recommended action: monitor**

Merchant 12 triggered AUP-06.1 on 2025-04-08: three disputes across 118 trailing-30-day orders, a 2.54% chargeback rate. GMV was 1,971,604 cents. Volume_z was -1.738 and ticket_drift was 0.979, providing no observed sales or ticket ramp. New GMV share was 21.18%; this does not establish thin buyer accounts. Zero recorded refunds do not prove delivery.

Recommend monitoring the next window while promptly reviewing existing records. The dispute breach is observed; bust-out remains uncorroborated. First inspect the three disputes and associated fulfillment evidence, reconcile refund requests with processor records, and validate order/dispute ingestion. Check campaign records for an explanation tied to the affected orders.

Repeated verified non-delivery, unresolved refund requests and suspicious buyer or settlement patterns would strengthen the alert and support a reserve or reversible settlement pause. Consistent delivery, resolved disputes, a documented campaign or a corrected data error would weaken or dismiss it. A human owns any action; irreversible offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: reason, order linkage, duplication, status and supporting evidence. Verified non-delivery would strengthen concern; documented delivery and resolved disputes would weaken it.; Check fulfillment and delivery evidence for disputed orders and a small sample of recent orders. Repeated unfulfilled orders would support escalation; consistent delivery would weaken the bust-out hypothesis.; Reconcile refund requests, cancellations and processor refunds against the zero-refund ledger. Unprocessed requests would strengthen concern; complete, consistent records would reduce it.; Reconcile dispute and order counts, timestamps and window assignments with source systems. Correcting a duplicate or missing denominator could dismiss the metric breach.; Review existing campaign and seasonal sales records against order dates; inspect buyer-account quality and settlement records if fulfillment concerns emerge. A documented campaign with fulfilled orders supports a benign explanation.

## Merchant 25 — alert episode 2025-04-10
Triggers: AUP-06.1 breach: 30d chargeback rate 5.1% (3 disputes / 59 orders)
**Recommended action: reserve**

Merchant 25 triggered AUP-06.1: three disputes across 59 trailing-30-day orders, a 5.1% chargeback rate. GMV was $3,661.01. Volume_z was 0.176 and ticket_drift was 1.1035; these do not establish a sharp sales ramp. New-GMV share was 16.8%, which does not establish thin buyers. No refunds were recorded.

Recommend a temporary percentage reserve under applicable policy while reviewing the three disputes and recent fulfillment. The breach supports payout protection, but the small dispute count and absent fulfillment evidence do not establish bust-out.

Confirmed non-delivery, linked thin buyers, and settlement extraction would strengthen the bust-out hypothesis and could justify pausing settlement. Verified delivery and disputes resolved in the merchant’s favor would weaken it. A documented campaign could explain buyer or ticket changes; corrected source records could dismiss a measurement-driven alert. Reconcile dispute and order records, inspect pending refunds, and verify campaign attribution before escalating. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: verify uniqueness, reason codes, underlying order dates, delivery evidence, and case outcomes.; Reconcile the 59 orders and three disputes against source records; verify event-window definitions and ingestion completeness.; Check fulfillment for disputed orders and a small recent-order sample, including tracking, promised delivery dates, and buyer confirmation where necessary.; Check refund requests, cancellations, pending refunds, and processor records; zero recorded refunds does not establish satisfied buyers.; Review recent campaign dates and attributable orders, then compare dispute history and relevant category peers to assess whether the rate is unusual.; Check whether recent buyers are thin or linked accounts and whether undelivered orders coincide with increased settlement withdrawals.

## Merchant 80 — alert episode 2025-04-25
Triggers: AUP-06.1 breach: 30d chargeback rate 8.1% (3 disputes / 37 orders)
**Recommended action: reserve**

As of 2025-04-25, merchant 80 triggered AUP-06.1 with 3 disputes across 37 trailing-30-day orders (8.1%). Recent GMV was 314,918 cents; reported refunds were zero. The preceding 90 days contained 110 orders and 1,089,227 cents of GMV. Volume_z of 0.055 provides little support for a sales ramp. New buyers contributed 37.6% of recent GMV, but account quality and a comparable baseline share are unknown.

Recommend a payout reserve, with its percentage set by the human reviewer under policy, while conducting targeted checks. The dispute concentration warrants protection, but these metrics do not corroborate bust-out or justify termination.

First reconcile dispute records and the order denominator, verify fulfillment against promised dates, review refund requests and processing, and obtain campaign records. Repeated overdue non-delivery, unsupported shipment claims, and unresolved refunds would strengthen the alert and support considering a settlement pause. Verified fulfillment, legitimate campaign activity, resolved disputes, or a corrected data defect would weaken it and support returning to monitoring.

Evidence gaps: Inspect the three dispute records for reason codes, linked orders, event dates, status, outcomes, and duplication; reconcile the 37-order denominator against source records.; Check promised delivery dates and fulfillment evidence for disputed orders, then sample other recent orders. Repeated overdue non-delivery with unsupported shipment claims would strengthen bust-out concern; verified delivery would weaken it.; Reconcile refund requests, approvals, and completed refunds against payment records. Determine whether the reported zero refunds reflects no requests, unresolved requests, or missing data.; Request campaign dates, promotion details, and acquisition sources, and compare them with recent order and buyer patterns. Documented campaigns with verified fulfillment would support a benign explanation.

## Merchant 151 — alert episode 2025-05-03
Triggers: AUP-06.2: volume z=4.3 vs baseline; AUP-06.4: new-account GMV share 66%
**Recommended action: reserve**

As of May 3, merchant 151 has 40 trailing-window orders and 3,418,593 cents GMV, versus 20 orders and 1,408,135 cents in the recorded baseline. Volume z is 4.33; new-account GMV share is 66.28%. Two disputes produce a reported 5% rate; recorded refunds are zero. Merchant age is 60 days, and baseline coverage is only 30 days.

These observations support concern but do not establish bust-out. A marketing campaign could explain the growth and buyer mix. Zero refunds do not establish successful fulfillment, and zero daily counters do not establish a data gap.

Recommend a provisional payout reserve, with its percentage set by the human reviewer. First verify delivery on sampled recent orders, inspect both disputes and pending refund requests, reconcile source records, and match sales to campaign records. Overdue non-delivery combined with coordinated buyers and settlement extraction would corroborate bust-out and support pausing payouts. Verified fulfillment, explained disputes and campaign-linked growth would support dismissing the alert and returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Sample recent high-value and new-account orders for promised delivery dates, carrier acceptance and delivery confirmation; distinguish overdue failures from orders still within their delivery commitments.; Inspect both dispute records for reason, order date, fulfillment evidence and resolution; reconcile refund requests, cancellations and pending refunds against the reported zero refunds.; Request dated campaign, promotion and acquisition-channel records and match them to the sales ramp and new-account orders.; Reconcile order, GMV, buyer-account and dispute source records with aggregates; verify baseline coverage, metric definitions and pipeline completeness.; Check whether new accounts share identifiers or concentrate purchases, and review payout records alongside delivery failures for corroboration of coordinated settlement extraction.

## Merchant 59 — alert episode 2025-05-04
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (4 disputes / 152 orders)
**Recommended action: reserve**

Merchant 59 triggered AUP-06.1 on May 4: four disputes across 152 trailing-30-day orders, a 2.63% chargeback rate. GMV was 1,140,901 cents. Volume_z was -0.027, providing no sales-ramp signal; ticket_drift was 1.074. New-buyer GMV share was 25.61%, but buyer-account quality is unknown. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary percentage reserve, with the percentage set by the human reviewer under policy, while validating the breach. Current evidence supports a chargeback concern, with limited support for bust-out.

First inspect all four disputes and reconcile order and refund records. Verify fulfillment for disputed orders and a small recent-order sample, then review campaign records and buyer quality. Verified non-delivery combined with coordinated thin accounts would strengthen the bust-out hypothesis and support considering a settlement pause. Verified fulfillment, resolved disputes or corrected data would weaken it and support returning to monitoring. Offboarding lacks corroborated evidence.

Evidence gaps: Inspect the four dispute records for unique orders, reason codes, transaction dates and resolution status; reconcile the 152-order denominator.; Check shipment, carrier delivery or service-completion evidence for disputed orders and a small sample of recent orders, including new buyers.; Reconcile refund requests, cancellations and processor refund records against the zero recorded refunds; identify unresolved customer requests.; Request campaign dates, promotions and acquisition-channel records to explain buyer mix and ticket changes; compare dispute rates with relevant category peers.; Check ingestion completeness and buyer-account quality. Verified non-delivery combined with coordinated thin accounts would strengthen bust-out; corrected records and verified fulfillment would weaken it.

## Merchant 105 — alert episode 2025-05-06
Triggers: AUP-06.1 breach: 30d chargeback rate 3.1% (3 disputes / 98 orders)
**Recommended action: monitor**

Merchant 105 breached the reported chargeback threshold: three disputes across 98 trailing-30-day orders, or 3.1%. This is an observed dispute signal, not corroborated bust-out evidence. Volume_z is 0.573 and ticket_drift is 0.961, providing little support for a pronounced sales ramp. Zero recorded refunds does not prove successful delivery.

Recommend monitor for the next window, with prompt review of the three disputes and their fulfillment records. Reconcile dispute uniqueness, the order denominator and refund requests against source systems. Check promised delivery dates and receipt evidence, then sample recent orders. Match any sales campaign to order timing and verified fulfillment.

Repeated overdue non-delivery, concentrated thin buyer accounts and unusual settlement extraction would strengthen the alert and support pausing settlement pending human review. Verified fulfillment, a documented campaign, or corrected source-data errors would weaken it. The supplied evidence does not justify offboarding; a human owns the action.

Evidence gaps: Inspect the three dispute records for reason, status, associated order and duplication; reconcile the 98-order denominator and window boundaries against source records.; Check promised delivery dates and carrier or customer receipt evidence for disputed orders, then sample recent orders. Repeated overdue non-delivery would strengthen the bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, cancellations and pending or completed refunds with payment records. Determine whether zero recorded refunds reflects no requests, unprocessed requests or missing ingestion.; Obtain campaign and seasonal promotion dates and match them to order changes. Verified campaigns with fulfilled orders would support a benign explanation.; Review recent buyer-account quality and settlement activity for concentrated thin accounts or unusual payout extraction.

## Merchant 75 — alert episode 2025-05-07
Triggers: AUP-06.1 breach: 30d chargeback rate 7.3% (3 disputes / 41 orders)
**Recommended action: reserve**

As of May 7, merchant 75 breached the reported AUP-06.1 chargeback threshold: three disputes across 41 trailing-30-day orders (7.3%). Volume_z is 2.94, new GMV share is 12.16%, and ticket_drift is 0.967. No refunds are recorded. These observations warrant review but do not establish bust-out or non-delivery.

Recommend a proportionate payout reserve while the human owner reviews the evidence. Prioritize the three dispute files, delivery confirmation and refund reconciliation, then verify campaign timing and source-data completeness. Marketing or seasonal demand could explain the volume increase if fulfillment is sound.

Confirmed non-delivery across recent orders, especially with coordinated thin buyers, would strengthen bust-out concerns and support pausing settlement pending review. Verified deliveries, resolved or invalid disputes, or a corrected data error would weaken the alert and support releasing the reserve and monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records: confirm unique cases, linked orders, reasons and current status. Non-delivery complaints would strengthen concern; invalid or duplicated records would weaken the alert.; Check fulfillment and delivery evidence for disputed orders and a small sample of recent orders; corroborate receipt with buyers where records are ambiguous. Widespread failed delivery would support escalation.; Reconcile refund requests, pending refunds and completed refunds against source records. Zero recorded refunds does not establish successful fulfillment.; Request campaign dates, promotion records and seasonal sales comparisons. A matching sales increase with verified fulfillment would support a benign explanation.; Reconcile the 41 orders and three disputes with source systems and check ingestion completeness, deduplication and window assignment.; Inspect buyer-account history and links among recent orders to determine whether the volume increase involves thin or coordinated accounts; new_gmv_share alone cannot establish this.

## Merchant 37 — alert episode 2025-05-17
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (4 disputes / 146 orders)
**Recommended action: monitor**

Merchant 37 triggered AUP-06.1 on May 17, 2025: four disputes across 146 trailing-window orders, a 2.74% chargeback rate. Thirty-day GMV was $32,247.75; volume_z was 1.61, ticket_drift was 0.965, and new-buyer GMV share was 21.21%. These metrics do not corroborate an abrupt bust-out ramp. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window, with prompt targeted checks now. Validate the four disputes and order denominator, inspect delivery evidence, and reconcile refund requests with recorded refunds. Obtain dated campaign records and review new-buyer account quality.

Verified non-delivery, thin or linked buyers, and continued sales despite fulfillment failure would strengthen the bust-out hypothesis and support a reserve or settlement pause. Verified delivery and resolved disputes would weaken it; a source-data correction could dismiss the metric breach. A documented campaign could explain sales activity but would not dismiss valid disputes. Offboarding requires corroborated bust-out evidence. The human reviewer owns the action.

Evidence gaps: Inspect the four dispute records for distinct transactions, reason codes, status and supporting evidence; reconcile the numerator and 146-order denominator to source records.; Check delivery evidence for disputed orders and a small sample of recent orders; compare promised delivery dates with tracking, receipt confirmation and outstanding fulfillment.; Reconcile zero recorded refunds against refund requests, cancellations, support complaints and processor records to distinguish no requests from unprocessed or missing refunds.; Request dated campaign records and compare promoted products and buyer cohorts with the sales change; check whether new buyers show thin histories or linked identities.

## Merchant 53 — alert episode 2025-05-17
Triggers: AUP-06.1 breach: 30d chargeback rate 10.3% (3 disputes / 29 orders)
**Recommended action: reserve**

Merchant 53 breached AUP-06.1 on May 17: three disputes across 29 trailing-30-day orders, a 10.3% rate. The denominator is small, so individual records materially affect the result. Ticket drift is 1.4286, while volume_z is 0.3188; the metrics do not establish a sharp sales ramp. New-buyer GMV share is 14.3%. Zero recorded refunds do not establish successful fulfillment.

Recommend a human-approved reserve holding a percentage of payouts while reviewing the three disputes, delivery evidence and unresolved refund requests. Select the percentage through the platform’s reserve process.

Bust-out remains a hypothesis. Verified repeated non-delivery, coordinated thin buyers and unresolved complaints would strengthen it and support considering a settlement pause. Credible delivery records, a documented campaign explaining ticket changes, or corrected dispute counts removing the breach would weaken or dismiss the alert. Reconcile source records before relying on the rate. Offboarding requires corroborated bust-out evidence, which is absent here.

Evidence gaps: Review the three dispute records for distinct transactions, reasons, status and underlying order dates; verify that the numerator and denominator follow the intended policy definition.; Check shipment, delivery and customer-contact records for all three disputed orders and a small sample of recent orders. Repeated verified non-delivery would strengthen bust-out concerns; credible delivery evidence would weaken them.; Reconcile refund requests, pending refunds and processed refunds with the reported zero refunds; identify unresolved cancellation or non-delivery complaints.; Ask for dated campaign records and promoted product prices to test whether a documented marketing push explains ticket drift.; Reconcile order, dispute and refund source records with the metric pipeline for missing or duplicated events. Corrected counts could dismiss the breach.; Inspect buyer account history and linked-account concentration for recent orders; new_gmv_share alone does not establish thin or coordinated buyers.

## Merchant 2 — alert episode 2025-05-20
Triggers: AUP-06.1 breach: 30d chargeback rate 3.4% (3 disputes / 87 orders)
**Recommended action: reserve**

Merchant 2 breached the chargeback threshold: three disputes across 87 trailing-30-day orders (3.45%). Volume z-score is 2.58; ticket drift is 1.078. New GMV accounts for 10.8% of sales. No refunds are recorded, but this does not establish successful delivery.

Bust-out remains uncorroborated. A marketing push or seasonal demand could explain increased volume; neither is documented. Recommend a temporary payout reserve, with percentage and release conditions set by the human reviewer, while checking existing records.

First reconcile dispute and order counts, then review all three dispute cases, fulfillment evidence and refund requests. Check campaign timing and buyer-risk concentration. Verified overdue non-delivery, unresolved refund requests and concentrated thin-buyer sales would strengthen the bust-out hypothesis and could justify pausing settlement. Verified deliveries, resolved disputes and documented campaign or seasonal demand would weaken it. A source-data correction removing the breach would dismiss the metric alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three dispute records and 87 orders against source records; check duplicates, window assignment and ingestion completeness, including the baseline.; Read dispute reasons, order dates, outcomes and supporting documents; determine whether cases concern non-delivery, unauthorized purchases or other causes.; Check existing shipment, tracking and delivery records against promised dates for disputed orders and a small sample of recent orders.; Reconcile refund records with cancellations, unfulfilled orders and pending refund requests; zero recorded refunds does not establish satisfactory fulfillment.; Check campaign calendars, attributed traffic and comparable seasonal sales; inspect existing buyer-risk indicators for concentration in thin accounts.

## Merchant 122 — alert episode 2025-05-25
Triggers: AUP-06.1 breach: 30d chargeback rate 3.7% (3 disputes / 81 orders)
**Recommended action: reserve**

Merchant 122 breached the chargeback threshold on May 25: three disputes across 81 trailing-30-day orders (3.7%). GMV was 1,327,279 cents, volume_z was 0.73 and ticket_drift was 1.14. Recorded refunds were zero; this does not establish satisfactory fulfillment.

Bust-out is a low-likelihood hypothesis on current evidence: the metrics do not show a pronounced volume ramp or establish failed delivery or coordinated buyers. Marketing and seasonality remain possible but unverified.

Recommend a temporary payout reserve, with the percentage set by the human reviewer, while checking the underlying records. First validate dispute uniqueness, dates, reasons and the order denominator. Check fulfillment against promised dates, reconcile pending refund requests, and obtain dated campaign evidence.

Verified disputes tied to repeated overdue nonfulfillment and concentrated thin buyer accounts would strengthen bust-out concern and support pausing settlement. Verified delivery, legitimate campaign attribution or corrected dispute records would weaken the alert and support monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes to processor records, checking unique IDs, event dates, reasons and outcomes; verify the 81-order denominator and pipeline completeness.; Check promised delivery dates, carrier scans or service-completion records for disputed orders and a small sample of recent orders. Repeated overdue nonfulfillment would strengthen bustout concern; verified timely delivery would weaken it.; Reconcile refund requests, cancellations and pending refunds against the recorded zero refunds. Unprocessed requests would increase concern; complete records would dismiss a refund-reporting gap.; Request dated campaign records and compare attributed orders with the observed sales pattern; check prior seasonal sales where available.; Inspect buyer-account age and concentration for disputed and recent orders, and reconcile settlements to those orders. New GMV share alone does not establish thin or coordinated buyers.

## Merchant 55 — alert episode 2025-05-26
Triggers: AUP-06.1 breach: 30d chargeback rate 5.3% (3 disputes / 57 orders)
**Recommended action: reserve**

Merchant 55 triggered AUP-06.1: three disputes across 57 trailing-30-day orders produce a 5.3% chargeback rate. GMV was 3,424,121 cents. Volume z-score was 0.224 and ticket drift was 1.071, providing little support for a sharp sales ramp. Recorded refunds were zero; that does not establish successful delivery.

Recommend a temporary payout reserve, with the percentage and release conditions set by the human reviewer. The breach merits protection while evidence is checked, but does not establish bust-out or justify termination.

First validate dispute records and the order denominator. Check disputed-order delivery, recent fulfillment, refund requests, and processor refunds. Obtain campaign records and inspect buyer-account quality where available.

Repeated verified non-delivery combined with thin or linked buyers and payout extraction would strengthen bust-out concerns and support pausing settlement. Complete delivery evidence, isolated explained disputes, or a corrected rate below the trigger would support dismissing the bust-out concern and returning to monitoring.

Evidence gaps: Reconcile the three disputes to unique processor records and orders; inspect reasons, statuses, and the completeness of the 57-order denominator.; Check delivery evidence and customer communications for the disputed orders, then a small sample of recent orders involving new buyers.; Reconcile recorded zero refunds against processor refunds, cancellations, and unresolved refund requests.; Request campaign dates, promotion details, and sales-channel records; compare associated orders with fulfillment and dispute records.; Review available buyer-account age and linkage indicators for disputed and recent orders; compare dispute rates with merchant history and relevant category peers.

## Merchant 6 — alert episode 2025-05-28
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (5 disputes / 173 orders)
**Recommended action: reserve**

Merchant 6 triggered AUP-06.1 on 2025-05-28: five disputes across 173 trailing-30-day orders, a 2.89% chargeback rate. GMV was 1,100,329 cents. Volume_z was 0.746 and ticket_drift 1.029; neither indicates a pronounced ramp. New-buyer GMV share was 22.66%, without a supplied baseline. Zero recorded refunds does not establish successful fulfillment.

Recommend a temporary percentage reserve under the team's applicable policy while checking the disputed orders and recent fulfillment. The breach supports payout protection, but bust-out is not corroborated; settlement suspension or termination is not supported by this episode alone. A human owns the action.

Confirm the dispute count, reasons and denominator against source records. Match orders to delivery or service evidence, reconcile refund requests and processor records, and obtain campaign dates. Verified non-delivery combined with coordinated thin buyer accounts and settlement extraction would strengthen bust-out and support escalation. Verified fulfillment and campaign-linked sales would weaken it; duplicate disputes or incomplete feeds could dismiss the metric alert after correction.

Evidence gaps: Review the five source dispute records for unique orders, reason codes, amounts, event dates and current outcomes; reconcile the 173-order denominator.; Check tracking, delivery confirmation or service completion for disputed orders and a small sample of recent orders.; Reconcile the zero recorded refunds with refund requests, pending refunds and processor records; check ingestion completeness.; Request campaign dates and sales-channel records; compare them with daily sales and fulfillment.; If non-delivery is found, examine buyer-account concentration and payout records for coordinated purchases and settlement extraction.

## Merchant 115 — alert episode 2025-06-07
Triggers: AUP-06.1 warn: 30d chargeback rate 2.0% (7 disputes / 351 orders); AUP-06.2: volume z=3.1 vs baseline
**Recommended action: reserve**

As of June 7, merchant 115 has a volume z-score of 3.10 and seven disputes across 351 trailing-30-day orders (1.99%). Recorded refunds are zero. Ticket drift is 0.964, and new GMV share is 18.75%. These are alert signals, not proof of bust-out or failed delivery.

Recommend a temporary payout reserve, with the percentage set by the human risk owner while reviewing fulfillment and disputes. The merchant's operating history does not resolve the current alert, but the supplied metrics do not justify termination.

Prioritize the seven dispute files and a small recent-order fulfillment sample. Repeated substantiated non-delivery, unresolved refund requests, and coordinated thin-account purchasing would strengthen the bust-out hypothesis and support considering a reversible settlement pause. Verified timely delivery, explained disputes, and a documented campaign or seasonal increase would weaken it. Reconcile source records and the volume calculation to rule out a pipeline artifact. Zero recorded refunds alone does not establish satisfactory fulfillment.

Evidence gaps: Inspect the seven dispute records for reasons, order dates, duplication, delivery evidence, and merchant responses; recurring substantiated non-delivery would strengthen the bust-out hypothesis.; Sample recent orders, including disputed orders, for promised delivery dates, carrier acceptance, delivery confirmation, or service completion; timely verified fulfillment would weaken the alert.; Reconcile the zero recorded refunds with refund requests, cancellations, processor records, and pending refunds; unresolved requests would increase concern.; Check campaign dates, attributed orders, and comparable seasonal periods; a documented demand increase with normal fulfillment would support a benign explanation.; Reconcile source order, dispute, and refund counts with the alert pipeline, and verify the volume_z calculation and window boundaries.; Review recent buyer account history and repeated purchasing patterns to determine whether buyers are thin or coordinated; new_gmv_share alone does not establish either.

## Merchant 137 — alert episode 2025-06-07
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 120 orders)
**Recommended action: monitor**

Merchant 137 triggered AUP-06.1 with a 2.5% trailing chargeback rate: 3 disputes across 120 orders. Trailing GMV is 947,448 cents. volume_z is -1.7164 and ticket_drift is 0.8834; these observations do not support the described sales-ramp pattern. Recorded trailing refunds are zero, which does not establish delivery or absence of refund requests.

Bust-out remains possible but is weakly supported. Ordinary transaction disputes or a reporting issue could explain the alert.

Recommend monitoring the next window while promptly reviewing the three dispute records, reconciling source counts, checking promised versus actual fulfillment and verifying refund requests. Check campaign dates and buyer-account patterns for a documented benign explanation.

Repeated overdue deliveries combined with coordinated buyer activity and payout extraction would corroborate bust-out and support stronger intervention. Verified delivery and isolated dispute causes would weaken that hypothesis; corrected source records could dismiss a reporting-driven alert. Do not offboard on these metrics alone. The human reviewer owns the action.

Evidence gaps: Inspect the three dispute records for reason codes, unique order IDs and merchant attribution; reconcile the 120-order denominator against source records.; Check promised delivery dates, tracking and delivery confirmation for disputed orders and a small sample of recent orders; repeated overdue, unfulfilled orders would strengthen the bust-out hypothesis.; Reconcile refund requests, pending refunds and processed refunds with support and payment records; zero recorded refunds does not establish successful fulfillment.; Check recent campaign and promotion dates against daily sales and buyer-account history; documented campaigns with verified fulfillment would support a benign explanation.; If fulfillment failures emerge, inspect settlement records and buyer concentration for coordinated purchases and payout extraction.

## Merchant 103 — alert episode 2025-06-11
Triggers: AUP-06.2: volume z=3.0 vs baseline; AUP-06.4: new-account GMV share 41%
**Recommended action: monitor**

As of June 11, 2025, merchant 103 triggered volume and new-account-share alerts: volume_z is 3.0137, and new accounts represent 41.34% of trailing GMV. The trailing window contains 43 orders and $2,484.93 GMV; the preceding 90-day baseline contains 78 orders and $5,383.59 GMV. These totals cover different durations. Ticket drift is 0.8373. Recorded trailing refunds and disputes are both zero; this does not establish successful delivery.

A bust-out ramp is plausible but uncorroborated. Seasonal demand and customer-acquisition campaigns remain credible explanations; source-data errors also need checking.

Recommend monitoring the next window while promptly sampling fulfillment, reconciling refund requests and dispute records, checking campaign attribution, and validating transaction completeness and buyer classification. Verified delivery with campaign or seasonal alignment would weaken the alert; corrected source data could dismiss it. Coordinated buyers, unexplained non-delivery and payout extraction would strengthen the bust-out hypothesis and support reconsidering settlement controls. A human owns any action.

Evidence gaps: Sample recent orders, including new-account purchases, for promised delivery dates, shipment tracking and delivery confirmation; unexplained overdue non-delivery would strengthen the alert.; Reconcile refund requests, cancellations and pending refunds against recorded refunds; inspect dispute records and ingestion completeness rather than treating zero recorded events as proof of fulfillment.; Request campaign dates and order attribution, and compare available prior seasonal sales; matching timing with verified delivery would support a benign explanation.; Reconcile order counts and GMV against source transactions in both windows, and verify new-account classification; corrected data that removes the signals would dismiss the metric alert.; Check flagged buyers for linked accounts or concentrated purchasing, and review corresponding settlement records; coordinated purchases plus failed delivery and extracted payouts would support bust-out.

## Merchant 140 — alert episode 2025-06-28
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (4 disputes / 152 orders)
**Recommended action: reserve**

As of June 28, merchant 140 triggered AUP-06.1: four disputes across 152 trailing-30-day orders, a reported rate of 2.63%. GMV was 2,476,510 cents; volume_z was 1.18, ticket_drift 0.9635 and new-GMV share 16.88%. Reported refunds were zero.

The breach warrants review, but these facts do not corroborate bust-out. Recommend a proportionate reserve for human approval while checking exposure and fulfillment. The metrics do not support selecting a reserve percentage.

First validate the four disputes and order denominator, then inspect fulfillment evidence and reconcile refunds, including pending requests. Check campaign records and buyer-account concentration. Verified non-delivery combined with coordinated thin buyers and settlement extraction would strengthen bust-out concern. Documented fulfillment and credible campaign activity would weaken it, while leaving any verified dispute breach actionable. Corrected records that remove the breach would support dismissing the alert. Offboarding is unsupported by the current evidence.

Evidence gaps: Review the four dispute records for unique cases, reason codes, order links and status; reconcile the 152-order denominator and reporting completeness.; Check delivery or service-completion evidence for disputed orders and a small recent-order sample, including overdue fulfillment and customer contacts.; Reconcile the zero reported refunds against processor records and pending refund requests.; Check campaign dates, promotions and acquisition channels against sales changes; inspect existing buyer-account and linkage records for concentration or thin accounts.; Use verified exposure and fulfillment findings to size any reserve; sustained non-delivery with coordinated buyers and settlement extraction would strengthen bust-out concern.

## Merchant 82 — alert episode 2025-06-30
Triggers: AUP-06.1 breach: 30d chargeback rate 5.0% (3 disputes / 60 orders)
**Recommended action: reserve**

As of June 30, merchant 82 breached AUP-06.1: three disputes across 60 trailing-30-day orders, a reported 5.0% chargeback rate. GMV was 2,773,121 cents. Volume_z was 0.6742 and ticket_drift was 0.9870, providing little support for a pronounced sales ramp. Recorded refunds were zero; that does not establish successful fulfillment.

Recommend a reserve, with the percentage set by the human reviewer under policy, while promptly reviewing the three disputes and delivery evidence. The breach supports payout protection, but these metrics do not corroborate bust-out or justify termination.

Confirm concern through verified overdue or undelivered orders, unresolved customer complaints, or coordinated thin-account purchases linked to payout extraction. Dismiss a calculation-driven alert if source reconciliation corrects the breach; reduce bust-out concern if fulfillment and refund records reconcile and disputes have supported explanations. Verify campaign or seasonal claims against actual sales records. Escalate to a settlement pause if review establishes ongoing non-delivery and payout exposure; offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes and 60 orders to source records, checking duplicates, missing ingestion, rate eligibility and calculation rules.; Read all three dispute records for reasons, linked orders, merchant responses and current outcomes.; Check promised delivery dates and carrier delivery evidence or service completion for disputed orders and a small sample of recent orders.; Reconcile refund requests, pending refunds, cancellations and processor refund records; zero recorded refunds does not establish zero customer problems.; Request campaign dates and offer details, and check any claimed seasonal pattern against available history.; If delivery failures appear, inspect buyer-account history and settlement records for coordinated purchasing and payout extraction.

## Merchant 118 — alert episode 2025-06-30
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (3 disputes / 117 orders)
**Recommended action: monitor**

As of June 30, merchant 118 triggered AUP-06.1 with three disputes across 117 trailing-30-day orders (2.56%). GMV was 836,017 cents; volume_z was -0.303 and ticket_drift was 0.985. These metrics do not show the sales ramp associated with the described bust-out pattern. Zero recorded refunds does not establish successful fulfillment.

Recommend monitoring the next window while promptly reviewing the three disputes and their fulfillment evidence. Reconcile dispute counts, order ingestion and refund records. Check campaigns and buyer concentration for explanations or corroboration.

Verified non-delivery, unresolved refund requests and concentrated thin-buyer orders would strengthen the bust-out hypothesis and support reconsidering payout controls. Documented fulfillment and resolved complaints would weaken it; duplicate disputes or missing orders would support a data explanation. Valid dispute records would confirm the reported breach even if bust-out is dismissed. A human owns the action; the supplied evidence does not support offboarding.

Evidence gaps: Inspect the three dispute records: verify distinct cases, reason codes, status, order linkage and event dates; reconcile the 117-order denominator with source records.; Check delivery or service-completion evidence for disputed orders and a small recent-order sample, including promised dates and buyer complaints.; Reconcile the zero reported refunds against refund requests, merchant logs and processor records; identify unresolved requests.; Review campaign calendars and comparable seasonal periods, matching promotions to disputed orders.; Check whether disputed and recent orders cluster among thin buyer accounts or linked buyers; compare concentration with the baseline.

## Merchant 1 — alert episode 2025-07-08
Triggers: AUP-06.1 breach: 30d chargeback rate 2.5% (3 disputes / 118 orders)
**Recommended action: monitor**

Merchant 1 triggered AUP-06.1 on July 8: three disputes across 118 trailing-30-day orders, a 2.54% chargeback rate. GMV was $13,555.03; volume_z was 0.748 and ticket_drift was 1.092. No refunds were recorded. These are observed facts; zero refunds does not establish successful fulfillment.

Bust-out is currently weakly supported: the metrics do not show a pronounced volume ramp, and buyer quality and delivery outcomes are unknown. A marketing push or reporting issue remains possible but unverified.

Recommend monitoring the next window while promptly reviewing the three disputes, delivery confirmations, overdue orders, refund requests and source-data completeness. Confirm campaign dates and inspect recent buyer concentration.

Linked thin buyer accounts, repeated non-delivery and settlement extraction would strengthen bust-out concerns and support pausing settlement pending human review. Verified deliveries, isolated disputes and documented campaign activity would weaken that hypothesis. A reconciliation error could dismiss the metric breach. Human review owns any payout restriction or termination.

Evidence gaps: Read the three dispute records: reasons, transaction dates, delivery evidence, status and any links between buyers; obtain the preceding baseline dispute rate.; Check carrier delivery confirmations for disputed orders and a small sample of recent orders; compare promised delivery dates with overdue or unfulfilled orders.; Reconcile zero recorded refunds with refund requests, cancellations, support complaints and processor refund records.; Reconcile the 118 orders and three disputes against source records, checking duplicates, missing events and window boundaries.; Ask for dated campaign records and comparable seasonal sales; inspect buyer-account quality and concentration in recent sales.

## Merchant 69 — alert episode 2025-07-16
Triggers: AUP-06.1 breach: 30d chargeback rate 7.5% (3 disputes / 40 orders)
**Recommended action: reserve**

Merchant 69 breached AUP-06.1: three disputes across 40 trailing-30-day orders produced a 7.5% chargeback rate. GMV was 1,195,744 cents; volume_z was 0.5694, ticket_drift was 1.3213, and new buyers represented 9.20% of GMV. No refunds were recorded.

These facts establish a dispute concern, but do not corroborate bust-out. The volume and new-buyer metrics offer limited evidence of a rapid ramp. Seasonal demand or a campaign could explain sales changes; neither is verified.

Recommend a temporary percentage reserve, sized by payout exposure, for human review. First inspect the three disputes, verify delivery against promised dates, and reconcile refund requests and processor records. Check campaign evidence and metric scopes, including the zero order count alongside trailing totals.

Repeated overdue non-delivery combined with thin-account concentration and payout extraction would strengthen bust-out suspicion and support pausing settlement. Verified fulfillment, resolved disputes or corrected source records would weaken the alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: unique order IDs, reasons, status and timestamps; verify inclusion in the 30-day window and the 40-order denominator.; Check fulfillment for disputed orders and recent unsettled orders using promised delivery dates, carrier delivery evidence or service-completion records. Repeated overdue non-delivery would strengthen the alert; verified fulfillment would weaken bust-out suspicion.; Reconcile recorded refunds with pending requests, cancellations and processor records. Zero recorded refunds does not establish an absence of dissatisfied customers.; Check campaign dates, promotions, product mix and comparable seasonal sales against the ticket and volume changes.; Reconcile metric scopes and source totals, especially n_orders=0 and n_disputes=1; inspect missing or delayed ingestion.; Review recent payout exposure and buyer-account concentration to size a temporary reserve and test whether sales are concentrated in thin accounts.

## Merchant 31 — alert episode 2025-07-18
Triggers: AUP-06.1 breach: 30d chargeback rate 2.9% (3 disputes / 105 orders)
**Recommended action: monitor**

Merchant 31 triggered a chargeback breach: 3 disputes across 105 trailing-30-day orders (2.9%). GMV was 951117 cents. Volume_z is -1.40 and ticket_drift is 0.895, so the observed pattern does not support a sales ramp. Recorded refunds are zero; that does not establish successful fulfillment.

Recommend monitor, with prompt review of the three disputes and a small fulfillment sample. Current evidence establishes a dispute-rate breach, not corroborated bust-out behavior.

Confirm concern through overdue or undelivered orders, consistent non-delivery disputes, and linked evidence of coordinated thin-account purchases and settlement extraction. Verified fulfillment, legitimate dispute explanations and reconciled order/refund records would weaken the bust-out hypothesis. Campaign records could support a benign explanation; missing orders or duplicate disputes could explain the alert through a data issue.

A human should reassess payout controls if these checks reveal broader non-delivery or coordinated extraction.

Evidence gaps: Inspect the three dispute records for reason, status, underlying order and duplication; reconcile the 105-order denominator against source records.; Check promised delivery dates, tracking and delivery confirmation for disputed orders and a small recent-order sample; inspect unresolved fulfillment complaints.; Reconcile refund requests, approvals and processor records to determine whether zero recorded refunds reflects actual activity or missing processing/data.; Check campaign and promotion dates against sales and disputed orders; compare relevant category patterns.; If fulfillment failures emerge, inspect associated buyer-account history and settlement records for coordinated purchases and payout extraction.

## Merchant 14 — alert episode 2025-07-19
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (5 disputes / 192 orders)
**Recommended action: reserve**

As of July 19, merchant 14 triggered AUP-06.1: five disputes across 192 trailing-30-day orders, a 2.6% chargeback rate. Recorded refunds are zero. Volume z-score is 1.687, ticket drift is 0.954, and new-GMV share is 19.3%; these facts do not establish a bust-out.

Recommend a temporary payout reserve, with the percentage set by the human risk owner, while checking the five disputes and recent fulfillment. The baseline dispute rate is missing, and zero refunds could reflect either actual activity or incomplete reporting.

Repeated verified non-delivery, thin-buyer concentration and unusual payout extraction would corroborate bust-out concerns and support considering a settlement pause. Verified delivery, resolved or invalid disputes, documented campaign or seasonal sales, and reconciled source records would weaken the alert and support returning to monitoring. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the five dispute records for unique IDs, linked orders, reason codes, status and event dates; obtain the preceding baseline dispute rate.; Check tracking and delivery evidence for disputed orders and a small sample of recent orders; unresolved non-delivery across orders would strengthen bust-out concerns.; Reconcile recorded refunds against payment-processor records and pending refund requests; verify whether zero reflects actual activity or incomplete ingestion.; Reconcile the 192 orders and five disputes against source records, checking ingestion completeness and duplicates.; Request campaign dates, attributed sales and seasonal explanations; compare buyer-account characteristics and payout activity with baseline.

## Merchant 56 — alert episode 2025-07-19
Triggers: AUP-06.1 breach: 30d chargeback rate 3.5% (3 disputes / 86 orders)
**Recommended action: reserve**

Merchant 56 breached the chargeback trigger on July 19: three disputes across 86 trailing-30-day orders (3.49%). GMV was $42,272.08. Volume_z was 0.346 and ticket_drift was 0.987, providing little evidence of a sales or ticket ramp. New GMV represented 17.66%; this does not establish thin buyer accounts. Reported refunds were zero, which does not establish successful fulfillment.

Recommend a temporary payout reserve for human review while validating the breach and checking delivery. The small dispute count makes individual case review especially useful; corroborated bust-out evidence is absent.

Confirm concern through verified non-delivery, unresolved refund requests, weak buyer histories, and settlement extraction inconsistent with fulfillment. Dismiss the breach if source reconciliation invalidates it; reduce bust-out concern if delivery is verified and disputes have unrelated explanations. Check campaign records for a benign sales explanation. Escalate to a reversible settlement pause if review reveals continuing non-delivery and payout exposure; offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the three disputes and 86 orders against source records; check duplicates, event dates, attribution, and ingestion completeness.; Read the three dispute records for reason codes, order dates, amounts, delivery evidence, and resolution status.; Check fulfillment for disputed orders and a small sample of recent orders using carrier delivery records or customer confirmations.; Reconcile the zero reported refunds with refund requests, pending refunds, cancellations, and processor records.; Request dated campaign or promotion records and compare associated orders, buyer histories, and fulfillment outcomes.; Check recent settlement and payout-account changes alongside outstanding undelivered orders; compare chargebacks with merchant history and relevant category peers.

## Merchant 135 — alert episode 2025-07-27
Triggers: AUP-06.1 breach: 30d chargeback rate 5.6% (4 disputes / 72 orders)
**Recommended action: reserve**

As of 2025-07-27, merchant 135 triggered the supplied chargeback breach: 4 disputes across 72 trailing-30-day orders (5.6%). Sales acceleration is not evident: volume_z is -0.194, and 72 orders in 30 days is approximately consistent with 221 over the preceding 90 days. New GMV share is 24.3%; no comparison or buyer-quality evidence is supplied. Zero recorded refunds do not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer under policy, while checking the four dispute records, delivery evidence, unresolved refund requests and campaign records. Reconcile the event feeds and counter definitions before relying on the counts.

Repeated verified non-delivery, thin buyer accounts and settlement extraction would strengthen a bust-out hypothesis and support pausing settlement. Documented delivery, resolved complaints, a credible campaign explanation or corrected erroneous records would weaken the alert and support monitoring. Current evidence does not corroborate bust-out sufficiently for offboarding. The human reviewer owns the action.

Evidence gaps: Review the four dispute records for reasons, associated orders, duplicates, status and merchant responses. Verified non-delivery would strengthen the alert; erroneous counts or documented delivery would weaken it.; Check fulfillment status and carrier delivery evidence for disputed orders and a small sample of recent orders. Look for overdue, unshipped orders and corroborating buyer complaints.; Reconcile zero recorded refunds against refund requests, support records and processor transactions. Identify unresolved requests or missing refund events.; Ask for campaign dates, promotion records and any seasonal fulfillment backlog; compare them with order and dispute dates. A documented campaign with completed deliveries would support a benign explanation.; Verify window definitions, event ingestion and the relationship between n_disputes: 3 and disputes_30d: 4; confirm that zero n_orders and gmv_cents reflect actual activity.; Check buyer-account history for recent and disputed orders, and compare new_gmv_share with its baseline. New GMV share alone does not establish thin buyer accounts.

## Merchant 62 — alert episode 2025-08-05
Triggers: AUP-06.1 breach: 30d chargeback rate 3.6% (4 disputes / 110 orders)
**Recommended action: reserve**

As of August 5, merchant 62 triggered AUP-06.1: four disputes across 110 trailing-30-day orders, a 3.64% chargeback rate. Recent GMV was $10,207.16 versus $31,104.14 over the preceding 90 days, providing little evidence of a revenue ramp. New GMV share was 22.66%; this does not establish thin buyer accounts. No refunds were recorded, which does not prove delivery.

Recommend a temporary, exposure-sized percentage reserve for human approval while reviewing the breach. The supplied evidence does not establish bust-out or justify termination.

First validate the four disputes and denominator, then check delivery on disputed orders and a small recent-order sample. Reconcile refunds and pending requests with source records, and inspect campaign attribution and buyer history. Repeated verified non-delivery alongside payout extraction and thin-account sales would corroborate bust-out and support pausing settlement. Verified fulfillment, a documented campaign and satisfactorily explained disputes would weaken that hypothesis; corrected source data could dismiss the metric breach. The human reviewer owns the action.

Evidence gaps: Inspect the four dispute records for unique cases, reason codes, linked orders and supporting evidence; reconcile the 110-order denominator and event timestamps against source records.; Check tracking and delivery evidence for disputed orders and a small sample of recent orders, including buyer confirmations where records are inconclusive. Repeated verified non-delivery would strengthen the bust-out hypothesis.; Reconcile recorded refunds with processor records, pending refund requests and support complaints. Confirm whether zero refunds reflects complete ingestion.; Check campaign dates, promotion terms and sales-channel attribution against the order increase; verify buyer-account history before treating new GMV as thin-account activity.; Review recent payouts and open fulfillment obligations to size any reserve. Verified delivery, legitimate disputes or a corrected metric would support releasing it.

## Merchant 34 — alert episode 2025-08-30
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (4 disputes / 146 orders)
**Recommended action: reserve**

Merchant 34 triggered AUP-06.1 with four disputes across 146 trailing-30-day orders (2.74%). GMV was 7,717,084 cents. Volume_z was -0.192, ticket_drift was 1.103, and new buyers represented 20.49% of GMV. These observations do not establish a sales ramp or coordinated thin-buyer activity. Zero recorded refunds does not establish successful fulfillment.

Recommend a percentage reserve, with the amount set by the human reviewer, while completing targeted checks. The dispute breach supports temporary payout protection; the supplied evidence does not establish bust-out.

First validate dispute uniqueness, attribution, reasons, and order-ingestion completeness. Check delivery evidence for disputed and recent orders, reconcile pending refund requests, and verify any acquisition campaign. Repeated verified non-delivery combined with coordinated buyer activity would corroborate bust-out and support escalation. Corrected data removing the breach, or documented delivery and legitimate acquisition explaining the disputed activity, would support dismissing or downgrading the alert. Verified delivery alone does not resolve every dispute reason.

Evidence gaps: Inspect the four dispute records for unique IDs, merchant attribution, underlying order dates, reasons, and status; compare prior dispute history to determine whether this is deterioration or recurring behavior.; Reconcile the 146 orders and dispute count against source records and ingestion completeness; a corrected rate below the trigger would support dismissing the alert.; Check shipment, delivery, cancellation, and customer-contact records for disputed orders and a small recent-order sample; repeated verified non-delivery would strengthen the bust-out hypothesis.; Reconcile refund requests and pending or failed refunds with the reported zero completed refunds; unresolved requests would increase concern.; Request campaign dates and acquisition-channel records, then inspect relevant buyer-account history; legitimate acquisition with verified delivery would weaken the bust-out hypothesis.

## Merchant 73 — alert episode 2025-09-03
Triggers: AUP-06.1 breach: 30d chargeback rate 3.1% (6 disputes / 193 orders)
**Recommended action: reserve**

Merchant 73 triggered AUP-06.1 on September 3, 2025: six disputes across 193 trailing-30-day orders, a 3.1% chargeback rate. GMV was 1,680,241 cents; new-buyer GMV share was 24.4%. Volume_z was -1.95 and ticket_drift was 0.955, so the supplied metrics do not show the sales ramp expected in a classic bust-out. Reported zero refunds do not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer based on verified exposure. The chargeback breach warrants protection while its cause is checked; current evidence does not justify termination.

Prioritize the six dispute files, delivery evidence, refund reconciliation and feed completeness. Repeated overdue non-delivery, linked thin-buyer orders and unexplained settlement extraction would strengthen the bust-out hypothesis and support pausing payouts. Verified delivery, resolved disputes, documented campaign activity or corrected source-data errors would weaken it and support returning to monitoring. Campaign evidence alone would not explain unresolved fulfillment failures.

Evidence gaps: Review the six dispute records for reason, purchase date, duplication, status and supporting evidence; verify the 193-order denominator against source records.; Check fulfillment and delivery evidence for disputed orders and a small sample of recent orders; compare promised delivery dates with actual status.; Reconcile refund requests, approvals and processor records with the reported zero refunds, including unresolved customer complaints.; Request campaign dates and attributable orders; compare new-buyer share and dispute reasons with merchant history and category peers.; Check feed freshness and completeness for orders, refunds and disputes before treating the trigger as merchant deterioration.

## Merchant 158 — alert episode 2025-09-05
Triggers: AUP-06.2: volume z=3.6 vs baseline; AUP-06.4: new-account GMV share 61%
**Recommended action: reserve**

As of 2025-09-05, merchant 158 triggered volume and new-account concentration alerts. Trailing GMV is 2,801,515 cents across 40 orders; new-account GMV share is 60.6%, and volume z is 3.64. The baseline contains only 22 orders across 31 days. One trailing dispute produces a reported 2.5% rate; zero recorded refunds does not establish successful fulfillment.

A bust-out is plausible but uncorroborated. Marketing or seasonal demand could explain the ramp, and the short baseline limits confidence.

Recommend a provisional payout reserve, with the percentage and release conditions set by the human reviewer. First sample recent high-value and new-account orders for delivery and customer receipt, reconcile refund requests and dispute records, and match campaign evidence to orders. Validate source ingestion and account classifications.

Repeated non-delivery, coordinated buyers and settlement extraction would strengthen the alert and support considering a payout pause. Verified fulfillment, reconciled records and campaign-linked demand would support releasing the reserve and monitoring the next window. Termination requires corroborated bust-out evidence.

Evidence gaps: Sample recent high-value and new-account orders for carrier acceptance, delivery confirmation and customer receipt; repeated non-delivery would strengthen bust-out concern, while verified delivery would weaken it.; Reconcile refund requests, cancellations and processed refunds against source records; determine whether the reported zero refunds omits pending or failed requests.; Review the single dispute's reason, order date, fulfillment evidence and status; reconcile dispute records with the reported trailing count and rate.; Request dated campaign records and match attributed orders to the ramp; check available category and seasonal comparators.; Reconcile daily orders, GMV, buyer-account classifications and baseline coverage with source systems, including the alert-day zeros.; Check whether new-account purchases cluster around shared buyer identifiers or other available links; new accounts alone do not establish thin or coordinated buyers.

## Merchant 37 — alert episode 2025-09-07
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (3 disputes / 112 orders)
**Recommended action: monitor**

Merchant 37 triggered AUP-06.1 on September 7: three disputes across 112 trailing-30-day orders produced a 2.68% chargeback rate. GMV was $24,218.25; volume_z was -2.64 and ticket_drift was 0.963. These comparisons do not support a sales ramp. New-buyer GMV share was 22.58%; account thinness is unknown. No refunds were recorded, which does not establish successful delivery or absence of refund requests.

Recommend monitor while promptly reviewing the three disputes, delivery evidence, refund requests and source-data completeness. Obtain campaign dates and seasonal context to test benign explanations.

Repeated non-delivery after promised dates, unresolved refund requests, thin buyer concentration and settlement extraction would corroborate bust-out risk and support reserve or reversible pause pending human review. Verified fulfillment, resolved disputes with documented causes, or a reconciled data error would weaken or dismiss the alert. Campaign evidence helps only if fulfillment also checks out. Current evidence does not justify offboarding.

Evidence gaps: Review the three dispute records: reasons, linked orders, transaction dates, duplication and merchant responses.; Check tracking and proof of delivery for disputed orders and a small recent-order sample; compare promised delivery dates with actual fulfillment.; Review refund requests, cancellations and support complaints against the refund ledger; zero recorded refunds does not establish zero unresolved requests.; Reconcile order and dispute counts with source records, checking ingestion completeness and reporting-window definitions.; Request campaign dates and seasonal context; inspect disputed buyers and new-buyer concentration, noting that new_gmv_share does not measure account thinness.; If fulfillment failures are found, check settlement receipts and unresolved delivery obligations for evidence of extraction.

## Merchant 115 — alert episode 2025-09-14
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (5 disputes / 195 orders)
**Recommended action: reserve**

Merchant 115 triggered the reported AUP-06.1 breach: five disputes across 195 trailing-30-day orders, a 2.56% rate. This merits review, but the supplied metrics do not show a bust-out ramp: volume_z is -6.73, ticket_drift is 1.03, and new_gmv_share is 11.8%. Zero recorded refunds does not establish satisfactory fulfillment.

Recommend a temporary percentage reserve, with the percentage and release criteria set by the human reviewer. The dispute breach supports caution; current evidence does not justify termination.

First reconcile the five disputes and order denominator, inspect delivery evidence and overdue orders, and compare refund requests with recorded refunds. Check campaign timing and buyer-account links. Zero daily counters alone do not prove missing data; verify ingestion against source records.

Repeated nondelivery, linked thin buyers and settlement extraction would strengthen the bust-out hypothesis and support considering a settlement pause. Verified fulfillment, a documented campaign explanation or corrected dispute counts would weaken the alert and support returning to monitoring.

Evidence gaps: Review the five dispute records for reason codes, distinct affected orders, transaction dates and duplicate counting; verify the 195-order denominator against source records.; Check fulfillment evidence for disputed orders and a small recent-order sample: promised delivery dates, tracking, delivery confirmation and customer contacts. Repeated overdue nondelivery would corroborate concern; verified delivery would weaken it.; Reconcile recorded refunds with refund requests, cancellations, support tickets and processor records. Determine whether zero recorded refunds reflects no requests, delayed processing or missing ingestion.; Ask for campaign dates and seasonal sales context, then match disputed orders to those cohorts; documented campaigns with normal fulfillment would support a benign explanation.; Inspect disputed and recent buyer accounts for thin histories or linked activity, and compare settlement extraction with fulfillment obligations.; Check ingestion completeness through 2025-09-14 and reconcile the zero daily counters with source activity.

## Merchant 91 — alert episode 2025-09-15
Triggers: AUP-06.1 breach: 30d chargeback rate 2.7% (3 disputes / 110 orders)
**Recommended action: reserve**

Merchant 91 triggered AUP-06.1 on September 15: three disputes across 110 trailing-30-day orders, a 2.73% chargeback rate. Volume_z is -8.50, indicating substantial contraction against baseline rather than a sales ramp. Recorded refunds are zero; that does not establish successful fulfillment or absence of refund requests.

Bust-out is currently a low-likelihood hypothesis, not a finding. The metrics do not establish thin buyers, settlement extraction or non-delivery. Seasonal contraction and incomplete order ingestion could affect the dispute rate, but neither explanation is verified.

Recommend a temporary percentage reserve, sized by a human using unsettled exposure and unfulfilled obligations. Reconcile the three disputes and order denominator, inspect fulfillment evidence, check pending refunds, and compare campaign dates and seasonal sales history.

Repeated verified non-delivery, concentrated thin-account purchases and settlement extraction would corroborate bust-out and support escalation. Verified fulfillment, resolved disputes or corrected data that removes the breach would support releasing the reserve and monitoring. Offboarding lacks corroborating evidence.

Evidence gaps: Review the three disputes' reason codes, underlying orders, event dates and outcomes; reconcile them with processor records and the 110-order denominator.; Check delivery or service-completion evidence for disputed orders and a small sample of recent unsettled orders. Repeated verified non-delivery would strengthen the bust-out hypothesis; documented fulfillment would weaken it.; Reconcile refund requests, cancellations and pending refunds against recorded refunds_30d: 0; determine whether unresolved requests concern non-delivery.; Compare source order and payment totals with the alert pipeline, including completeness and duplicate-dispute checks. Corrected counts that remove the breach would support dismissing the alert.; Request the merchant's campaign dates and seasonal sales history, then compare them with daily sales. Check buyer-account depth and concentration before attributing activity to thin accounts.; Quantify unsettled payouts and unfulfilled obligations to size a temporary reserve and establish release criteria.

## Merchant 63 — alert episode 2025-09-16
Triggers: AUP-06.1 breach: 30d chargeback rate 2.6% (4 disputes / 154 orders)
**Recommended action: monitor**

Merchant 63 triggered AUP-06.1 with four disputes across 154 trailing-30-day orders, a 2.6% chargeback rate. GMV was 981,348 cents; volume_z was -10.22, indicating contraction rather than a sales ramp. New GMV share was 20.15%, ticket_drift was 1.0774, and reported refunds were zero.

Bust-out remains possible but is weakly supported: these metrics do not establish failed delivery, thin buyer accounts, or payout extraction. Campaign effects and a reporting issue remain hypotheses requiring checks.

Recommend monitoring the next window while promptly reviewing the four disputes, promised versus actual fulfillment, refund requests and processor records, campaign dates, and feed completeness. Corroborated overdue non-delivery combined with coordinated buyer activity and settlement extraction would strengthen the alert and justify reconsidering payout controls. Verified delivery, reconciled refunds, and resolved or erroneous disputes would weaken it. Zero recorded refunds alone do not demonstrate successful fulfillment. A human owns any action.

Evidence gaps: Review the four dispute records: verify unique cases, associated orders, reasons, dates, amounts, and status; reconcile the 154-order denominator.; Check promised delivery dates, tracking, delivery confirmation, and buyer complaints for disputed orders plus a small recent-order sample. Repeated overdue non-delivery would strengthen bust-out concern; verified fulfillment would weaken it.; Reconcile refund requests, pending refunds, and processor refund records against the reported zero refunds.; Check campaign and seasonal-promotion records against affected order dates and buyer acquisition sources.; Verify alert-date feed completeness and trailing-window aggregation. If fulfillment concerns emerge, inspect linked buyer accounts and settlement records for coordinated purchasing and payout extraction.

## Merchant 64 — alert episode 2025-09-16
Triggers: AUP-06.1 breach: 30d chargeback rate 3.0% (5 disputes / 164 orders)
**Recommended action: reserve**

As of September 16, merchant 64 breaches the reported chargeback threshold: five disputes across 164 trailing-30-day orders (3.05%). GMV is $30,494.29. Order volume averages 5.47 per day versus 11.23 in the preceding 90 days; volume_z is -8.84. These observations do not show the sales ramp associated with the described bust-out pattern. Zero recorded refunds do not establish successful fulfillment.

Recommend a temporary payout reserve, with the percentage set by the human reviewer using unsettled exposure. The breach warrants protection and prompt investigation, but current evidence does not support termination.

Confirm the counts and inspect dispute reasons, promised delivery dates, tracking and pending refund requests. Repeated overdue non-delivery, concentrated thin or linked buyers and settlement extraction would strengthen the bust-out hypothesis. Verified timely fulfillment and resolved disputes would weaken it. Reconciled ingestion errors could dismiss the metric breach; documented campaigns or category patterns could support a benign explanation. Review the next window and adjust the action based on corroborated findings.

Evidence gaps: Review the five dispute records for unique order IDs, reason codes, status and outcomes; distinguish non-delivery from unrelated dispute causes.; Check promised delivery dates, carrier acceptance and delivery evidence for disputed orders and a small sample of other recent orders; verify any overdue fulfillment backlog.; Reconcile the 164 orders and five disputes with source records, ingestion completeness and window boundaries to confirm or dismiss a pipeline artifact.; Check refund requests, pending refunds and processor records against the reported zero refunds; identify unresolved customer requests.; Check campaign dates, promotion records, daily sales and available category or seasonal comparisons for an ordinary explanation.; Review recent buyer-account histories, linked-account patterns and unsettled exposure to assess thin-buyer concentration and size a temporary reserve.

## Merchant 66 — alert episode 2025-09-16
Triggers: AUP-06.1 breach: 30d chargeback rate 3.1% (4 disputes / 131 orders)
**Recommended action: monitor**

Merchant 66 breached the chargeback trigger: four disputes across 131 trailing-30-day orders, a 3.05% rate. GMV was 2,006,480 cents. Volume_z was -6.07 and ticket_drift was 0.855, which does not support the classic bust-out sales ramp. Recorded refunds were zero; that does not establish delivery or the absence of refund requests.

Recommend monitor for the next window, with prompt review of the four disputes and sampled fulfillment records. Current evidence supports investigating the chargeback breach, but does not corroborate bust-out or justify irreversible termination.

Verify dispute reasons, transaction links and source counts; check delivery against promised dates, refund requests and processing records, and campaign or seasonal context. Confirm feed completeness before interpreting the rate.

Undelivered orders, coordinated buyer activity and concentrated settlement extraction would strengthen the bust-out hypothesis and support a reversible payout pause pending human review. Verified delivery, resolved disputes, valid campaign context or a corrected data error would weaken it. Persistent genuine losses could justify a reserve. A human owns the action.

Evidence gaps: Review the four dispute records: reason codes, linked transactions, original order dates, duplicates and outcomes; verify the reported numerator and denominator.; Check fulfillment for disputed orders and a small recent-order sample using promised delivery dates, shipment tracking and delivery confirmations.; Reconcile recorded refunds with refund requests, pending or failed refunds, cancellations and customer complaints; zero recorded refunds does not establish successful delivery.; Ask for campaign dates and seasonal sales context, then compare affected orders with ordinary sales and available category benchmarks.; Reconcile order and dispute feeds with source records and settlement totals. Review buyer overlap and payout concentration if fulfillment or dispute checks reveal concerns.

## Merchant 121 — alert episode 2025-09-17
Triggers: AUP-06.1 breach: 30d chargeback rate 3.0% (3 disputes / 101 orders)
**Recommended action: reserve**

Observed: Trigger B flags three disputes across 101 trailing-30-day orders, a 2.97% chargeback rate. GMV is 609,149 cents; volume_z is -9.875, indicating contraction against baseline. New-buyer GMV share is 21.69%. Reported refunds are zero, which does not establish successful fulfillment.

Assessment: The breach merits review, but these aggregates do not corroborate bust-out. There is no current sales ramp; earlier extraction followed by declining activity remains untested. A seasonal spike has little support, and a data issue is possible but unproven.

Recommendation: A human should consider a temporary percentage reserve while reviewing the three disputes and recent fulfillment. Size the reserve using disputed amounts and outstanding delivery exposure.

Confirmation would require corroborated non-delivery alongside suspicious sales and settlement behavior. Verified deliveries, explained dispute outcomes and reconciled records would weaken the alert; corrected counts could dismiss the measured breach. Check refund requests and campaign records before deciding whether to release the reserve or escalate.

Evidence gaps: Inspect the three dispute records: verify unique transactions, reason codes, transaction dates, amounts and current outcomes; distinguish non-delivery from other causes.; Check fulfillment evidence for disputed orders and a small sample of recent orders: promised delivery dates, carrier acceptance and delivery confirmation. Repeated overdue, unfulfilled orders would strengthen the bust-out hypothesis.; Reconcile reported zero refunds against refund requests, merchant records and processor records; identify unprocessed requests or missing refund events.; Reconcile the 101 orders and three disputes to source records and ingestion logs; corrected counts or duplicates could dismiss the measured breach.; Compare recent order and settlement timing with campaign dates and seasonal history; verify any claimed promotion against actual sales and successful fulfillment.

## Merchant 157 — alert episode 2025-09-18
Triggers: AUP-06.1 breach: 30d chargeback rate 14.3% (3 disputes / 21 orders)
**Recommended action: reserve**

Merchant 157 breached the chargeback threshold on 2025-09-18: 3 disputes / 21 trailing-30-day orders (14.3%), with $1,657.79 GMV. Reported refunds are zero. Volume_z is -1.15, so the metrics do not show the sales ramp expected in a classic bust-out. Merchant history is short: age 79 days, with 50 baseline days and 45 baseline orders.

Recommend holding a percentage of payouts through a reserve while a human reviews the underlying records. The dispute rate warrants protection, but these aggregates do not establish bust-out or justify termination.

First reconcile disputes and the order denominator, then inspect fulfillment and refund records. Valid non-delivery disputes, overdue orders, concentrated thin buyer accounts, and settlement extraction would strengthen the bust-out hypothesis and support considering a settlement pause. Verified fulfillment, resolved dispute explanations, or corrected source data that removes the breach would weaken the alert and support monitoring. Campaign or seasonal records would support a benign explanation only alongside satisfactory fulfillment. Zero recorded refunds alone does not establish customer satisfaction.

Evidence gaps: Reconcile the three disputes to source records and unique orders; verify reasons, status, event dates, and the 21-order denominator.; Check delivery or service-completion evidence for disputed orders, then sample recent orders for overdue fulfillment and customer complaints.; Compare refund requests, pending refunds, cancellations, and payment-processor refund records with the reported zero refunds.; Check campaign dates, promotion terms, and historical seasonal patterns against order activity; verify associated orders were fulfilled.; Review buyer-account depth and concentration, linked accounts, and settlement exposure to test the thin-account and extraction hypotheses.

