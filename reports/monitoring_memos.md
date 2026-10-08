# Merchant monitoring memos (model-drafted, advisory)

Provenance: rule set s1 · as_of 2025-12-29 · model gpt-6.1-sol

## Merchant 132 — alert episode 2024-03-17
Triggers: AUP-06.4: new-account GMV share 69%; AUP-06.4b young merchant: age 48 days (< 90), new-account GMV share 69% (>= 60%)
**Recommended action: monitor**

As of March 17, merchant 132 triggered new-account concentration and young-merchant alerts: 69.03% of trailing-30-day GMV came from new accounts, and merchant age is 48 days. The window contains 24 orders and 575,223 cents of GMV. The baseline has only six orders across 18 days; null volume and ticket comparisons cannot establish a sales ramp or dismiss risk.

No disputes were learned of in the window, and no refunds were recorded. All 12 deadline-eligible shipments have carrier confirmation. These observations weaken a current fulfillment-failure hypothesis but do not establish fulfillment across every order.

Recommend monitoring the next window; settlement should continue on this evidence. First reconcile carrier, refund and dispute records, then check campaign attribution and buyer linkage. Verified delivery, complete feeds and a documented acquisition campaign would support dismissing the alert. Linked buyer activity combined with verified unfulfilled orders or unresolved refund obligations would strengthen bust-out concerns and support pausing settlement pending review. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Reconcile shipment records to carrier events and sample delivery evidence for recent orders, including orders outside the 12-shipment cohort; check outstanding fulfillment obligations.; Reconcile refund requests, cancellations and processed refunds to the zero reported refunds; identify unresolved requests.; Verify dispute-feed completeness and reconcile processor records, including customer-stated reasons, to the zero reported disputes.; Check campaign dates and acquisition attribution against new-account orders; inspect buyer-account linkage and shared payment or delivery identifiers.; Reconcile approved orders and GMV to source transactions and verify account-age classification before interpreting growth against the six-order baseline.

## Merchant 43 — alert episode 2024-04-03
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: monitor**

Merchant 43 triggered volume and new-account-share alerts: volume z=3.11 and new-account GMV share=48.33%. Trailing 30-day GMV was $1,941.62 across 29 orders, versus $1,523.38 across 35 orders in the 64-day baseline. Ticket drift was 1.54.

These are growth and buyer-mix signals, not corroborated bust-out evidence. All eight deadline-eligible shipments were carrier-confirmed. Known disputes and recorded refunds were zero; those observations do not establish that every order was fulfilled or every complaint captured. The merchant has only 64 cumulative orders despite a recorded age of 1,026 days.

Recommend monitoring the next window, with prompt validation of fulfillment, refund requests, processor disputes and campaign records. Verified delivery and a documented acquisition campaign would weaken the alert. Coordinated new buyers combined with failed fulfillment or unresolved non-delivery complaints would strengthen it. Reconcile source data to exclude a distorted baseline or account classification error. Current evidence does not justify pausing settlement or offboarding; the human reviewer owns any action.

Evidence gaps: Verify carrier scans for the eight eligible shipments and sample recent high-value new-account orders against shipment and customer receipt records; genuine fulfillment would weaken the bust-out hypothesis.; Reconcile refund requests, cancellations and pending refunds with recorded refunds; unresolved non-delivery complaints would strengthen concern despite zero recorded refunds.; Match processor dispute records to approved orders, checking reason codes and ingestion completeness; validate that the reported zero disputes is accurate.; Request campaign dates, acquisition channels and promotion records matching the sales increase; corroborated acquisition activity would support a benign explanation.; Reconcile source orders, GMV and account creation dates with the metric pipeline, including the 64-day baseline; inspect concentrated buyer, address or payment overlaps for coordinated purchasing.

## Merchant 132 — settlement-pause escalation 2024-04-04 (case opened 2024-03-17)
Triggers: AUP-06.6 delivery confirmation: 5 of 7 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 5e-06)
**Recommended action: pause_settlement**

Merchant 132 has a delivery-confirmation escalation in the case opened March 17. As of April 4, five of seven eligible shipments remain unconfirmed after the five-day deadline. At the portfolio reference share of 4.82%, the probability of at least this many is approximately 0.000005. This supports urgent review, but does not establish non-delivery.

The trailing window contains 48 orders and 1,593,320 cents GMV; the available baseline contains 14 orders and 280,769 cents over 36 days. No disputes or refunds are recorded. Null volume and ticket comparisons provide no reassurance.

Recommend a reversible settlement pause pending human review. Carrier-confirmed delivery and corrected ingestion would dismiss the confirmation alert; documented campaigns could explain the sales increase. Buyer-confirmed nonreceipt, absent carrier acceptance, unresolved refund requests or coordinated buyer activity would strengthen the bust-out hypothesis. Reconcile fulfillment, refund and dispute records promptly, then reassess the pause. Current evidence does not justify offboarding.

Evidence gaps: Check carrier tracking directly for all five unconfirmed shipments; reconcile delivery timestamps, tracking identifiers and ingestion errors.; Review fulfillment records for the seven-shipment cohort, including carrier acceptance; contact affected buyers where carrier evidence remains inconclusive.; Check refund requests, cancellations and support complaints against recorded refunds, including pending or failed refunds.; Reconcile processor dispute records and reason codes with the zero recorded disputes.; Request dated campaign or promotion records matching the sales increase; inspect buyer-account history and concentration for evidence of coordinated thin accounts.; Review the existing case findings and settlement history for corroborated extraction or continuing fulfillment failures.

## Merchant 4 — alert episode 2024-04-11
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 41%
**Recommended action: monitor**

Merchant 4 — April 11, 2024. Volume z=3.05 and new-account GMV share=41.0% triggered review. The window contains 52 orders and 2,480,666 cents of GMV; the 72-day baseline contains 82 orders and 4,195,354 cents. These signals warrant investigation but do not establish bust-out.

Recorded outcomes are reassuring: zero disputes across all stated reasons, zero refunds, and carrier confirmation for all 12 deadline-eligible shipments. That shipment cohort is limited; confirmation alone does not establish customer satisfaction.

Recommend monitor through the next window. Settlement should continue on the supplied evidence. Validate carrier tracking and customer receipt for sampled new-account orders, reconcile refund requests and processor disputes, and obtain campaign attribution. Check baseline ingestion and buyer classification.

A documented campaign with dispersed buyers, verified fulfillment and complete records would support dismissing the alert. Invalid tracking, customer nonreceipt, unresolved refunds or coordinated suspicious buyers would strengthen concern and justify reconsidering payout controls. Offboarding lacks corroborated bust-out evidence.

Evidence gaps: Verify carrier records for the 12 eligible shipments and sample high-value new-account orders for tracking, delivery dates and customer acknowledgment; genuine delivery dismisses fulfillment concerns, while invalid tracking or customer-reported nonreceipt strengthens them.; Reconcile refund requests, cancellations and outstanding refunds with the reported zero refunds; unresolved requests would weaken the clean-outcome evidence.; Reconcile processor dispute records and stated reasons with the reported zero disputes, checking ingestion completeness and duplicate handling.; Request campaign dates, spend and order attribution, plus any documented seasonal promotion; matching acquisition and sales uplift would support a benign explanation.; Check order-feed completeness across the baseline and alert window, new-account classification, and buyer concentration or shared identifiers; corrected metrics could dismiss the alert, while concentrated suspicious buying would strengthen it.

## Merchant 98 — alert episode 2024-04-16
Triggers: AUP-06.1 breach: 4 disputes on 50 orders in 30d (8.0%); a 2.5% rate gives >= 4 with p = 0.038
**Recommended action: reserve**

Merchant 98 breached AUP-06.1: four disputes learned of in 30 days against 50 approved orders (8%). At the 2.5% policy rate, the probability of at least four is 0.0383. Two complaints concern non-receipt and two concern description; none alleges unauthorized use. No refunds are recorded.

Recommend a policy-sized payout reserve, with the human owner setting the percentage. Settlement should not pause on this evidence alone. All 16 deadline-eligible shipments have carrier confirmation; that cohort does not necessarily cover the disputed orders or establish satisfactory delivery. Volume_z is 1.04, and new GMV share is 23.81%; neither establishes a bust-out ramp or thin buyers.

Reconcile the four disputes, inspect disputed-order fulfillment and product evidence, and verify requested or promised refunds. Check campaign timing, buyer concentration, and settlement withdrawals. Authentic unresolved fulfillment failures coupled with payout extraction or stopped delivery would strengthen bust-out suspicion and support a reversible pause. Corrected dispute records could dismiss the breach; verified fulfillment, resolved complaints, and documented campaigns could reduce concern. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the four underlying dispute records for unique cases, stated reasons, order links, and evidence; correct duplicates or misclassification and recompute the breach.; Match the two item-not-received orders to carrier records and recipient/address evidence; determine whether those orders fall outside the 16-shipment confirmation cohort.; Inspect product listings, customer complaints, and merchant responses for the two not-as-described disputes.; Reconcile refund requests and promised refunds with processor transactions and the zero-refund aggregate.; Check campaign dates and order sources against sales changes; inspect buyer-account history and concentration before treating new GMV as thin-account activity.; Review recent settlement withdrawals and fulfillment records together for evidence of payout extraction followed by stopped delivery.

## Merchant 56 — alert episode 2024-05-07
Triggers: AUP-06.1 breach: 5 disputes on 49 orders in 30d (10.2%); a 2.5% rate gives >= 5 with p = 0.0084
**Recommended action: reserve**

Merchant 56 breaches AUP-06.1: five disputes on 49 approved orders (10.2%); the probability of this count at the 2.5% policy rate is 0.0084. Three disputes concern fulfillment and two unauthorized use. No refunds are recorded.

Recommend a payout reserve, with the percentage set by the human owner, while reviewing the disputed orders. Bust-out remains a hypothesis: volume_z is negative and ticket size is near baseline, providing no corroborating sales ramp. One of ten deadline-eligible shipments lacks confirmation; delivery_p = 0.3899 provides weak evidence of an unusual confirmation shortfall and does not prove non-delivery.

First reconcile dispute and approved-order records, then inspect tracking, complaint evidence, refund requests and campaign records. Verified unresolved non-delivery, linked thin buyer accounts and settlement extraction would strengthen bust-out concern and support pausing settlement. Valid delivery and product evidence, resolved complaints, or corrected records that remove the breach would weaken it and support returning to monitoring. A campaign alone would not dismiss valid disputes. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the five disputes and 49 approved orders to source records: verify unique disputes, learned-of dates, reason codes and complete order ingestion; recompute the breach if corrected.; Check carrier tracking and proof of delivery for the two item-not-received orders and the overdue unconfirmed shipment; establish whether they overlap. Review the not-as-described complaint against the listing and customer evidence.; Inspect refund requests, approvals, failures and customer communications to distinguish no refund demand from unresolved or unrecorded refunds.; Compare campaign dates and promoted products with affected orders; inspect buyer-account history and links among disputed buyers, then reconcile settlements with fulfilled orders.

## Merchant 65 — alert episode 2024-05-21
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: reserve**

As of May 21, merchant 65 shows elevated volume (z=3.07), 48.07% new-account GMV and ticket drift of 1.397. The trailing 30 days contain 54 orders and 1,230,039 cents GMV, versus 107 orders and 1,744,638 cents across the preceding 90 days.

These signals support a bust-out hypothesis, but do not establish it. Recorded disputes and refunds are zero. All nine shipments past the five-day confirmation deadline have carrier confirmation; that small cohort offers limited reassurance about broader fulfillment.

Recommend holding a percentage of payouts through a reserve while conducting a prompt review; the supplied evidence does not justify pausing settlement or offboarding. A human should set the reserve percentage.

First verify delivery for recent high-value and new-account orders, reconcile refund requests and processor disputes, and inspect campaign records and source-data completeness. Failed deliveries, unresolved refunds or coordinated buyers would strengthen the concern. Verified fulfillment and a documented campaign or seasonal explanation matching the increase would support releasing the reserve and monitoring.

Evidence gaps: Sample recent high-value and new-account orders; match order records to carrier scans and customer receipt confirmations. Nonfulfillment would strengthen the alert; verified delivery would weaken it.; Reconcile refund requests, cancellations and merchant support tickets with recorded refunds; identify unresolved requests or omitted records.; Reconcile processor dispute records and ingestion completeness with the zero counts, retaining customer-stated reasons.; Check campaign dates, acquisition channels, promotions and advertised products against the sales increase; compare available seasonal sales history.; Reconcile order and settlement totals with source records, verify baseline completeness and new-account classification, and inspect concentrated or linked buyers.

## Merchant 136 — alert episode 2024-05-23
Triggers: AUP-06.4: new-account GMV share 80%; AUP-06.4b young merchant: age 50 days (< 90), new-account GMV share 80% (>= 60%)
**Recommended action: monitor**

Merchant 136 triggered the new-account concentration and young-merchant rules: age 50 days, with 80.16% of trailing GMV from new accounts. The window contains 23 orders and 657,222 cents of GMV. Baseline history is limited to 20 days and seven orders; null volume and ticket comparisons cannot establish abnormal growth.

There are zero recorded disputes and refunds. All four deadline-passed shipments have carrier confirmation, but this small cohort does not establish fulfillment across all orders. Zero disputes and refunds also do not prove satisfactory delivery.

Recommend monitoring the next window while completing targeted checks. Current evidence does not justify pausing settlement. A marketing campaign is a plausible benign explanation, pending verification.

Check tracking and customer receipt, refund requests and complaints, dispute-feed completeness, campaign attribution, and new-account buyer legitimacy. Verified fulfillment and campaign-driven independent buyers would weaken the alert. Corroborated non-delivery, false tracking or coordinated buyers would strengthen it and warrant reassessing a reserve or settlement pause. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Verify carrier tracking for the four deadline-passed shipments and sample recent orders for fulfillment. Confirmed receipt would weaken the alert; false tracking or corroborated non-delivery would strengthen it.; Check refund requests, cancellations and support complaints against recorded refunds_30d of 0. Unresolved non-delivery complaints or withheld refunds would strengthen concern.; Reconcile dispute records and ingestion completeness with the 23 approved orders, retaining customer-stated reasons. Missing disputes would change the assessment; a complete zero-dispute record would support monitoring.; Request campaign dates and order attribution, and sample new-account orders for buyer legitimacy and shared identifiers. A documented campaign with independent buyers would support a benign explanation; coordinated accounts would strengthen bust-out concern.; Validate new-account classification and GMV totals against source orders, and confirm why volume_z, ticket_drift and base_refund_rate are null.

## Merchant 110 — alert episode 2024-06-17
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: monitor**

Merchant 110 triggered volume (z=3.07) and new-account GMV share (43.84%) alerts. The trailing 30 days contain 79 approved orders and 737,656 cents GMV; the preceding 90-day baseline contains 168 orders and 1,422,580 cents GMV.

One dispute alleges item not received. Its breach probability is 0.8612, providing weak evidence of exceeding the policy rate. All 15 shipments past the five-day confirmation deadline have carrier confirmation. Confirmation does not resolve the individual complaint. Recorded refunds are zero.

Recommend monitoring the next window; settlement should continue on current evidence. Acquisition or seasonal demand remain plausible, unverified explanations. Review the dispute and sample recent new-account orders for fulfillment and buyer links. Reconcile refund requests with the ledger, campaign-attributed sales with the surge, and source data with the baseline.

Corroborated non-delivery combined with coordinated purchasing would strengthen the bust-out hypothesis and support pausing settlement pending review. Verified fulfillment and campaign attribution, or a corrected data error, would support dismissing the alert. A human owns the action.

Evidence gaps: Inspect the non-receipt dispute, matching order, carrier delivery record and customer communication; determine whether it reflects actual non-delivery.; Sample recent high-value and new-account orders for carrier-confirmed fulfillment and buyer-account links; corroborated non-delivery or coordinated purchasing would increase concern.; Reconcile refund requests, cancellations and completed refunds against the zero-refund ledger; check for unresolved customer requests.; Match campaign records and comparable-period sales to the surge; attributable, fulfilled sales would support dismissing the alert.; Reconcile source orders, baseline ingestion and new-account classification to rule out missing or duplicated data.

## Merchant 136 — settlement-pause escalation 2024-06-21 (case opened 2024-05-23)
Triggers: AUP-06.6 delivery confirmation: 10 of 20 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 8e-09)
**Recommended action: pause_settlement**

As of June 21, merchant 136 has an existing case opened May 23. Of 20 recent shipments past the five-day confirmation deadline, 10 lack carrier confirmation, versus a 4.82% reference share (p = 8.02e-09). This is strong evidence of an unusual confirmation pattern, not proof of non-delivery.

Thirty-day GMV is 1,826,095 cents across 50 orders; volume_z is 7.13 and new-GMV share is 83.19%. The baseline contains only 49 days and 28 orders. Recorded disputes and refunds are zero; those observations do not establish successful fulfillment.

Recommend that the human case owner pause settlement pending prompt review. The fulfillment anomaly alongside growth warrants a reversible stop; bust-out remains uncorroborated.

First reconcile the 10 shipments against carrier scans, tracking identifiers and ingestion logs, then sample customer receipt confirmations. Verified deliveries or a feed defect would dismiss the delivery alert. Corroborated non-receipt or fabricated fulfillment would strengthen concern. Reconcile refund requests and dispute records, inspect campaign evidence and buyer histories, and review prior case findings. Resume payouts when the anomaly is resolved and fulfillment is verified; reassess controls if unresolved.

Evidence gaps: Check carrier tracking and deadline calculations for all 10 unconfirmed shipments; reconcile delivery scans with platform ingestion. Verified timely deliveries or a feed defect would dismiss the confirmation alert.; Obtain fulfillment records and contact a small sample of affected customers. Corroborated non-receipt, fabricated tracking or absent dispatch records would strengthen the bust-out hypothesis.; Reconcile refund requests, cancellations, issued refunds and dispute records with processor and support logs. Determine whether the reported zeros reflect complete records and whether affected customers received remedies.; Review dated campaign records, sales sources and buyer-account histories. A documented campaign with credible purchases and verified fulfillment would support benign growth.; Read the case opened on 2024-05-23 for prior findings, merchant responses and unresolved fulfillment issues; the case-opening date alone does not establish misconduct.

## Merchant 37 — alert episode 2024-06-25
Triggers: AUP-06.1 breach: 7 disputes on 116 orders in 30d (6.0%); a 2.5% rate gives >= 7 with p = 0.029
**Recommended action: reserve**

Merchant 37 breached AUP-06.1: seven disputes learned in 30 days against 116 approved orders (6.03%); the probability of this count at the 2.5% policy rate is 0.0287. All seven allege unauthorized use; none allege non-receipt or misdescription.

The supplied metrics do not show the classic bust-out ramp: volume_z is -1.12 and ticket_drift is 1.016. One of 15 deadline-eligible shipments lacks carrier confirmation, with delivery_p 0.5235; this is not strong evidence of excess missing confirmations or proof of non-delivery. Zero recorded refunds and fulfillment disputes do not establish successful fulfillment.

Recommend a temporary percentage reserve, with the human risk owner setting the percentage. Settlement need not pause on current evidence; termination is unsupported.

First verify dispute uniqueness, reasons, dates, and order completeness. Reconcile refunds and complaints, check tracking and receipt evidence, and review campaigns and disputed buyers' histories. Corrected records could dismiss the breach. Verified unauthorized disputes confirm payment risk; coordinated buyers plus corroborated fulfillment failures would support escalation to a settlement pause.

Evidence gaps: Reconcile the seven dispute records with processor records: unique IDs, learned dates, unauthorized-use reasons, and completeness of the 116 approved orders. Corrected counts could dismiss the breach; verified counts would confirm it.; Check carrier tracking and delivery evidence for the one overdue unconfirmed shipment, then sample disputed orders for shipment, receipt, and customer complaints. Tracking gaps may dismiss fulfillment concerns; corroborated non-delivery would strengthen them.; Reconcile refunds, cancellations, and pending refund requests with the payment ledger and support queue; determine whether unresolved fulfillment complaints exist despite zero recorded refunds.; Request campaign dates and acquisition sources, then inspect disputed buyers' account histories and merchant links. Documented legitimate acquisition would support a benign explanation; coordinated thin accounts and corroborated fulfillment failures would strengthen bust-out concerns.

## Merchant 82 — alert episode 2024-06-25
Triggers: AUP-06.1 warn: 3 disputes on 54 orders in 30d (5.6%); a 1.5% rate gives >= 3 with p = 0.049; AUP-06.4: new-account GMV share 56%
**Recommended action: monitor**

Merchant 82, June 25: W and S flag three disputes among 54 orders (5.6%) and 55.8% of GMV from new accounts. At the 1.5% warning rate, the probability of at least three disputes is 0.049; this is not a probability of bust-out. Disputes comprise one unauthorized, one not received, and one not as described.

Recommend monitoring the next window while promptly checking source records. Volume_z is 1.16 and ticket_drift is 1.126. One of 18 deadline-eligible shipments lacks confirmation; delivery_p of 0.589 provides little evidence of an abnormal confirmation rate. Missing confirmation alone does not prove non-delivery. Reported zero refunds does not establish that refund requests were resolved.

A marketing push could explain new-account sales, but remains unverified. Review disputed-order fulfillment, carrier tracking, refund requests, campaign records, and buyer concentration. Documented campaigns and confirmed deliveries would weaken the alert; verified non-delivery, unresolved refunds, and coordinated buyers would strengthen it.

Settlement need not pause on this evidence. Escalate for a human decision on reserve or reversible pause if checks establish ongoing fulfillment failures or coordinated extraction. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for duplicate counting, stated reasons, order linkage, merchant responses, and fulfillment evidence; verify the 54-order denominator and event timestamps.; Check carrier tracking and confirmation-feed completeness for the one overdue unconfirmed shipment, plus delivery evidence for the disputed orders. Confirmed delivery would weaken the fulfillment concern; verified failures would strengthen it.; Reconcile refund requests, approvals, and completed refunds against the reported zero refunds. Unresolved requests tied to failed fulfillment would materially increase concern.; Obtain dated campaign or promotion records and compare the new-account orders with campaign timing, buyer concentration, and fulfillment. A documented campaign with delivered orders supports a benign explanation; coordinated buyers and failed fulfillment support escalation.

## Merchant 88 — alert episode 2024-07-17
Triggers: AUP-06.1 breach: 4 disputes on 53 orders in 30d (7.5%); a 2.5% rate gives >= 4 with p = 0.046
**Recommended action: reserve**

Merchant 88, July 17, 2024: four disputes were learned of in 30 days against 53 approved orders (7.55%). At the policy rate of 2.5%, the probability of at least four is 0.0456, supporting the chargeback breach—not proving bust-out.

The dispute mix is two unauthorized and two not-as-described, with none for item not received. All 14 deadline-eligible shipments have carrier confirmation. Volume_z is −0.355 and ticket_drift is 1.018, offering little support for a sales ramp. Zero recorded refunds does not establish satisfactory resolution.

Recommend a temporary payout reserve, with the percentage set by the human owner after exposure review. Settlement need not pause on this evidence; no case-opening escalation is supplied.

First reconcile disputes and approved-order ingestion, then check disputed-order fulfillment, customer complaints, refund requests, and campaign records. Validated disputes confirm the breach; corrected records could dismiss it. Verified fulfillment and documented acquisition would weaken bust-out concerns. Thin-account concentration, extraction, and corroborated fulfillment failures would strengthen them and justify reconsidering a settlement pause.

Evidence gaps: Reconcile the four disputes to processor records: unique cases, dates learned, stated reasons, and order links; verify all 53 approved orders were ingested. Corrections could dismiss the threshold breach; validated records confirm it.; Review fulfillment evidence and customer communications for disputed orders, plus tracking for recent unshipped or deadline-ineligible orders. Corroborated non-delivery would strengthen bust-out concerns; verified fulfillment would weaken them.; Check refund requests, cancellations, pending refunds, and processor refund records. Zero recorded refunds does not establish that customers received satisfactory resolutions.; Request campaign dates and acquisition-channel records; inspect recent buyer-account histories and concentration. Documented promotions with ordinary buyers would support a benign explanation; concentrated thin accounts and settlement extraction alongside fulfillment failures would support bust-out.

## Merchant 139 — alert episode 2024-08-09
Triggers: AUP-06.4: new-account GMV share 64%; AUP-06.4b young merchant: age 36 days (< 90), new-account GMV share 64% (>= 60%)
**Recommended action: monitor**

Merchant 139 triggered new-account concentration and young-merchant rules on August 9. New accounts generated 63.54% of 2,226,683 cents in trailing GMV across 30 orders; merchant age is 36 days. The baseline contains only one order across six days, so growth and ticket comparisons are unavailable. Nulls do not indicate zero risk.

Bust-out is plausible, but concentration alone is insufficient corroboration. No disputes or refunds were recorded in 30 days, and all seven deadline-eligible shipments have carrier confirmation. These observations provide limited reassurance; they do not establish fulfillment for every order.

Monitor the next window. Settlement should continue on the supplied evidence; there is no case-opening or delivery-confirmation escalation here. Verify tracking, refund requests, dispute ingestion and campaign attribution now. Coordinated buyer activity combined with verified fulfillment failures or unresolved refunds would strengthen the bust-out hypothesis and support a settlement pause pending review. Verified deliveries, complete records and documented campaign-driven acquisition would weaken it. A human owns the action.

Evidence gaps: Check carrier tracking and delivery scans for the seven eligible shipments, then sample other recent orders against order and shipment records; unexplained failures would strengthen the alert.; Reconcile refund requests, cancellations and processing records with the reported zero refunds; unresolved requests would change the assessment.; Reconcile processor dispute records and ingestion completeness with the reported zero disputes, preserving customer-stated reasons.; Request dated campaign records and referral sources; compare campaign-attributed orders with the new-account GMV.; Review existing buyer-account linkage and payment checks for coordinated purchasing, and reconcile new-account classification and GMV totals with source orders.

## Merchant 139 — settlement-pause escalation 2024-08-29 (case opened 2024-08-09)
Triggers: AUP-06.6 delivery confirmation: 6 of 12 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 9e-06)
**Recommended action: pause_settlement**

Recommend a reversible settlement pause pending expedited review within the case opened August 9. The current alert is dated August 29.

Observed: six of 12 shipments past the five-day confirmation deadline remain unconfirmed, versus a 4.82% portfolio reference share (p = 0.00000902). Recent volume is 43 orders and 3,572,624 cents, compared with 16 orders and 937,467 cents across 26 baseline days. No disputes or refunds are recorded in the trailing 30 days. Null volume and ticket comparisons leave those changes unquantified.

Bust-out is plausible but uncorroborated. Missing confirmation is not proof of non-delivery; a carrier-data gap or campaign-related fulfillment pressure could explain the pattern. Recorded dispute zeros do not resolve fulfillment concerns.

First verify the six tracking records directly with carriers, reconcile ingestion, and obtain fulfillment evidence and targeted customer confirmation. Reconcile refund and dispute records, inspect campaign evidence and buyer/order links, and review case remediation. Verified delivery or corrected data would support releasing the pause. Corroborated non-receipt, fabricated tracking or coordinated orders would strengthen escalation. Offboarding requires corroborated bust-out evidence. A human owns the decision.

Evidence gaps: Check tracking directly with carriers for the six unconfirmed shipments; verify shipment dates, carrier acceptance, deadline calculation and delivery scans against platform ingestion records.; Request fulfillment records for the 12-shipment cohort and contact customers on unresolved orders. Verified deliveries would weaken the alert; corroborated non-receipt or fabricated tracking would strengthen it.; Reconcile processor dispute records and merchant refund requests, approvals and payments through August 29; check whether the reported zeros reflect complete ingestion.; Review campaign dates, spend, promotions and order timing; inspect buyer-account and order links for concentrated or coordinated purchasing.; Review the August 9 case notes and subsequent remediation to establish whether this delivery issue persists and whether earlier concerns were corroborated.

## Merchant 97 — alert episode 2024-09-18
Triggers: AUP-06.1 breach: 3 disputes on 32 orders in 30d (9.4%); a 2.5% rate gives >= 3 with p = 0.047; AUP-06.4: new-account GMV share 42%
**Recommended action: reserve**

As of September 18, merchant 97 has three disputes learned in 30 days against 32 approved orders (9.375%). At the policy’s 2.5% rate, the probability of at least three is 0.0474. Two disputes concern items not as described; one concerns unauthorized use. None concern nonreceipt.

New accounts represent 42.19% of GMV, but volume_z is 0.059, providing little evidence of a sales ramp. One of 13 deadline-eligible shipments lacks carrier confirmation; delivery_p is 0.474, offering little evidence of unusual delivery failure. Zero recorded refunds does not establish successful fulfillment.

Recommend a payout reserve, with its percentage set by the human owner. Current evidence does not justify pausing settlement or offboarding. Bust-out remains a hypothesis; legitimate acquisition could explain the customer mix.

Validate dispute records and order counts, inspect disputed goods and overdue tracking, reconcile refund requests and payments, and check campaign sources and buyer links. Verified fulfillment, resolved complaints, and legitimate acquisition would weaken the alert. Corroborated buyer coordination, false fulfillment, or settlement extraction would support escalation.

Evidence gaps: Validate the three dispute records, their learned dates, unique IDs, stated reasons, and the 32 approved-order denominator; reconcile source records and ingestion completeness.; Review the two not-as-described cases against listings, shipment contents, customer communications, and resolutions; inspect tracking for the one overdue unconfirmed shipment and obtain carrier confirmation.; Reconcile refund requests, issued refunds, and pending refunds against processor records; determine whether zero recorded refunds reflects complete data and actual merchant handling.; Check campaign dates, acquisition sources, and new-account purchase patterns for linked buyers or concentrated activity. Legitimate acquisition and verified fulfillment would weaken bust-out; corroborated linked buying, false fulfillment, and settlement extraction would strengthen it.

## Merchant 75 — alert episode 2024-09-24
Triggers: AUP-06.2: volume z=3.0 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: monitor**

Merchant 75 — as of September 24, 2024.

Volume triggered at z=3.01: 37 approved orders and 772,812 cents GMV in 30 days, versus 68 orders and 1,298,243 cents over the preceding 90 days. New accounts contributed 44.50% of recent GMV. Ticket drift is 1.094.

No disputes or refunds are recorded in the recent window. All seven deadline-eligible shipments have carrier confirmation. This small cohort is reassuring but does not establish fulfillment across all orders or eliminate emerging risk.

Recommend monitoring the next window. The triggers justify investigation, but current evidence does not support stopping payouts. Marketing or seasonal demand remains plausible and unverified.

First verify campaign-linked sales and buyer independence, sample fulfillment, and reconcile refund requests and processor disputes. Check baseline completeness and account classification. Verified receipts, independent campaign buyers and complete feeds would weaken the alert. Coordinated thin buyers combined with corroborated non-delivery would strengthen bust-out concern and support a human decision to pause settlement pending review. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Verify campaign dates and order attribution, and inspect new-account orders for shared payment, device or shipping identifiers. Independent campaign-acquired buyers would weaken bust-out concern; coordinated buyers would strengthen it.; Check carrier scans for the seven eligible shipments and sample recent high-value orders for dispatch and customer receipt. Verified fulfillment would weaken concern; corroborated non-delivery would support escalation.; Reconcile refund requests, cancellations and unresolved customer complaints with refund records; zero recorded refunds does not establish zero requests.; Reconcile processor dispute records and stated reasons with the supplied counts; inspect any newly identified disputes for unauthorized use or fulfillment failures.; Check order-feed completeness, duplicate orders and buyer-account classification across both windows; compare available prior seasonal sales and category peers.

## Merchant 145 — alert episode 2024-10-09
Triggers: AUP-06.4: new-account GMV share 76%; AUP-06.4b young merchant: age 37 days (< 90), new-account GMV share 76% (>= 60%)
**Recommended action: monitor**

Merchant 145 triggers review because it is 37 days old and new accounts contribute 75.95% of trailing GMV ($20,140.18 across 29 orders). These are exposure signals, not proof of bust-out.

One dispute alleges an item was not as described; none alleges non-receipt or unauthorized use. The chargeback breach probability is 0.516, providing weak evidence of an elevated underlying rate. All five deadline-eligible shipments have carrier confirmation. Recorded refunds are zero. The baseline contains only two orders over five days, and null comparisons cannot establish stability.

Recommend monitoring the next window; current evidence does not justify pausing settlement. Verify carrier records, the dispute, pending refunds and campaign attribution now. Independent campaign-driven buyers and verified fulfillment would reduce concern. Linked buyers combined with invalid tracking, verified non-delivery or unresolved refund failures would strengthen bust-out suspicion and support a reversible settlement pause. A human owns the action; offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the five eligible shipments to carrier records and spot-check high-value new-account orders. Confirmed fulfillment would reduce concern; invalid tracking or customer-confirmed non-delivery would strengthen it.; Read the single not-as-described dispute and reconcile dispute-feed completeness. Establish whether it is an isolated product issue or supported evidence of broader fulfillment problems.; Check pending refund requests, cancellations and refund processing against order records; zero recorded refunds does not establish zero customer complaints.; Match campaign dates, spend and referral sources to new-account orders; check for repeated buyer contact, payment or delivery details. Campaign-attributable independent buyers would support benign acquisition.; Reconcile GMV and account-age classifications to source orders and inspect ingestion completeness; corrected classifications or missing records could dismiss a measurement-driven alert.

## Merchant 145 — settlement-pause escalation 2024-10-31 (case opened 2024-10-09)
Triggers: AUP-06.6 delivery confirmation: 6 of 8 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 3.2e-07)
**Recommended action: pause_settlement**

As of October 31, six of eight shipments past the five-day confirmation deadline remain unconfirmed, versus a 4.82% portfolio reference (p=3.23e-07). The case opened October 9. Recommend that the human case owner pause settlement pending prompt review; the hold is reversible.

Missing confirmation is not proof of non-delivery. The sole 30-day dispute is not as described; its chargeback breach probability of 0.583 provides weak evidence of a policy-rate breach. Zero recorded refunds do not establish successful fulfillment. Null volume and ticket comparisons cannot support a growth anomaly, and the baseline contains only 27 days.

First check all six tracking records directly with carriers and reconcile confirmation ingestion. Verified deliveries or a corrected feed would dismiss the delivery alert. Invalid tracking, customer-confirmed nonreceipt, unresolved refunds and coordinated thin buyers would strengthen bust-out concern. Review the existing case, dispute record and campaign evidence before deciding whether to resume payouts or retain the hold. Current evidence does not justify offboarding.

Evidence gaps: Check tracking IDs, carrier scans, shipment dates and deadline calculations for all six unconfirmed shipments; compare with ingestion logs. Verified deliveries would dismiss the confirmation alert, while invalid tracking or customer-confirmed nonreceipt would strengthen it.; Review the October 9 case notes and request fulfillment evidence for affected orders. Establish what was previously investigated and whether any promised remediation was completed.; Inspect the single not-as-described dispute and reconcile refund requests, cancellations and processed refunds against source records. Documented unresolved fulfillment failures would strengthen concern; resolved complaints and verified delivery would weaken it.; Check campaign dates, attributable orders and buyer-account concentration. A documented campaign with independent buyers and verified fulfillment would support a benign explanation; coordinated thin accounts with failed fulfillment would support bust-out.

## Merchant 12 — alert episode 2024-11-29
Triggers: AUP-06.1 warn: 6 disputes on 162 orders in 30d (3.7%); a 1.5% rate gives >= 6 with p = 0.038; AUP-06.2: volume z=3.2 vs baseline
**Recommended action: reserve**

As of 2024-11-29, merchant 12 has a volume alert (z=3.207) and six disputes learned of over 30 days against 162 approved orders (3.70%). Three allege nonreceipt and three allege goods not as described; none allege unauthorized use. The probability of at least six disputes at the warning's 1.5% rate is 0.0375; the supplied breach probability is 0.2227.

Recent delivery confirmations do not independently corroborate widespread failure: one of 40 deadline-eligible shipments is unconfirmed, versus a 4.82% reference share (p=0.8615). Confirmation also does not resolve product-quality complaints. Zero recorded refunds does not establish customer satisfaction.

Recommend a temporary percentage reserve, with the human owner setting its size against unresolved exposure. Settlement need not pause on this evidence. Seasonal demand or a marketing campaign remains plausible, but neither dismisses the complaints.

Prioritize disputed-order fulfillment and product checks, refund reconciliation, campaign attribution and source-data completeness. Verified widespread failures, linked thin buyers and settlement extraction would support escalation to a reversible pause. Verified fulfillment, resolved complaints and reconciled campaign-driven sales would support returning to monitoring.

Evidence gaps: Review the six dispute records for distinct orders, stated reasons, merchant responses and supporting evidence; duplicates or miscoding would weaken the warning.; Match the disputed orders to carrier scans, delivery evidence and product descriptions. Documented failures would strengthen concern; verified fulfillment and accurate products would weaken it.; Check refund requests, pending refunds and processor records against the reported zero refunds; unresolved valid requests would increase concern.; Request campaign dates, spend and order attribution, plus comparable seasonal sales records; a matching campaign and verified fulfillment would support a benign explanation.; Reconcile order ingestion and baseline completeness with source records, and inspect buyer-account age and linked purchasing patterns before inferring thin-account concentration.

## Merchant 88 — alert episode 2024-12-15
Triggers: AUP-06.1 warn: 4 disputes on 84 orders in 30d (4.8%); a 1.5% rate gives >= 4 with p = 0.039; AUP-06.2: volume z=3.4 vs baseline
**Recommended action: monitor**

Merchant 88 triggered chargeback warning W and volume alert V on December 15. Four disputes on 84 orders imply 4.76%; the probability of at least four at the 1.5% warning rate is 0.0392. Volume z is 3.41.

Two disputes concern unauthorized use; one each concerns non-receipt and description. Two of 24 deadline-eligible shipments lack confirmation, with delivery p = 0.3232. This offers limited corroboration of fulfillment failure; missing confirmation is not proof of non-delivery. Zero recorded refunds also does not establish satisfactory fulfillment.

Recommend monitoring the next window with prompt targeted review. Current evidence does not justify pausing settlement or offboarding. Seasonal demand or a campaign could explain growth, but neither is verified.

Validate dispute and order records, check disputed and overdue shipments, inspect refund requests, and obtain campaign evidence. Verified deliveries and attributable sales growth would weaken the alert. Confirmed non-delivery, unresolved refunds, or linked thin buyers behind the ramp would strengthen bust-out concern and support reconsidering a reserve or settlement pause. A human owns the action.

Evidence gaps: Check carrier tracking and delivery evidence for the two overdue unconfirmed shipments and the two fulfillment disputes; confirmed delivery weakens concern, while verified non-delivery strengthens it.; Validate the four dispute records, stated reasons, learned dates and unique order links; reconcile the 84 approved orders and inspect disputed buyers for linked or thin accounts.; Inspect refund requests, cancellations and unresolved support tickets; zero recorded refunds does not establish satisfied customers.; Request campaign dates and sales reports, and compare available prior seasonal periods; a matching uplift with completed fulfillment supports benign demand.; Reconcile recent and baseline order totals with source records and ingestion logs; corrected counts that remove the spike would dismiss the volume alert.

## Merchant 80 — alert episode 2024-12-18
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 42%
**Recommended action: reserve**

Merchant 80 triggered volume and new-account-share alerts on December 18. The trailing window contains 54 orders and 694,751 cents GMV; volume_z is 3.07, new-account GMV share is 42%, and ticket_drift is 1.35.

These observations justify checking buyer quality and settlement exposure, but do not establish a bust-out. Recorded disputes and refunds are zero; neither establishes absence of risk. Only one of 16 deadline-eligible shipments lacks carrier confirmation. delivery_p of 0.546 provides little evidence of an unusual confirmation shortfall, and missing confirmation does not prove non-delivery.

Recommend a temporary partial payout reserve, with the percentage set by the human reviewer according to exposure. Current evidence does not justify pausing all settlement or offboarding.

Prioritize carrier verification, pending refund and complaint records, processor dispute reconciliation, and campaign documentation. Linked suspicious buyers plus corroborated fulfillment failures would strengthen the bust-out hypothesis and support a settlement pause. Verified fulfillment, legitimate acquisition or seasonal demand, and complete source records would support releasing the reserve and monitoring the next window.

Evidence gaps: Verify carrier scans for the one overdue unconfirmed shipment and sample delivered orders; confirmed delivery would weaken the fulfillment concern.; Reconcile refund requests, cancellations and pending refunds against the zero recorded refunds; inspect unresolved customer complaints.; Reconcile processor dispute records and stated reasons with the zero dispute counts, checking ingestion completeness without assuming a dispute lag.; Request campaign dates, acquisition channels and comparable seasonal sales; match them to the order increase and new-account purchases.; Check new buyers for linked identities, payment instruments or addresses and compare their GMV share with prior periods; new accounts alone do not establish thin or fraudulent buyers.; Reconcile baseline and current orders with source records, then compare settlement exposure with verified fulfillment.

## Merchant 147 — alert episode 2024-12-19
Triggers: AUP-06.4: new-account GMV share 74%; AUP-06.4b young merchant: age 37 days (< 90), new-account GMV share 74% (>= 60%)
**Recommended action: monitor**

Merchant 147 triggered new-account concentration and young-merchant rules: 74.0% of $6,964.75 in trailing-30-day GMV came from new accounts, at merchant age 37 days. The window contains 29 orders. The preceding baseline has only one order across two days; null volume and ticket comparisons cannot establish acceleration or absence of risk.

Recorded disputes and refunds are zero. All 11 shipments eligible under the five-day confirmation deadline have carrier confirmation. These observations weaken immediate fulfillment concerns but do not validate every order or exclude unrecorded complaints.

Recommend monitoring the next window; settlement should continue. Current evidence does not justify a pause or offboarding. Human review owns the action.

Verify carrier events and outstanding fulfillment promises, pending refunds and complaints, processor disputes, and feed completeness. Match new-account purchases to dated campaigns and inspect buyer-account links. Verified fulfillment and attributable acquisition would support dismissing the alert; corroborated delivery failures, linked buyers and unexplained sales growth would support escalation.

Evidence gaps: Inspect carrier delivery events for the 11 eligible shipments and sample remaining orders against promised fulfillment dates; corroborated delivery failures would strengthen concern, while verified fulfillment would weaken it.; Check pending refund requests, cancellations and support complaints against the refund ledger; zero completed refunds does not establish absence of customer problems.; Reconcile processor dispute records, including stated reasons, with the zero-count feed and verify ingestion completeness.; Request dated campaign records and acquisition attribution; matching promotions and independent buyers would support benign demand, while unexplained linked buyer accounts would strengthen bust-out concern.; Recompute new-account GMV share from order records and check feed coverage; corrected classification or missing records could dismiss the concentration alert.

## Merchant 47 — alert episode 2024-12-22
Triggers: AUP-06.2: volume z=3.1 vs baseline; AUP-06.4: new-account GMV share 48%
**Recommended action: monitor**

Merchant 47 triggered volume and new-account-share alerts on December 22. Trailing 30-day orders total 24 versus 37 across the preceding 90 days; volume z is 3.1085. GMV is 273,198 cents, with 48.06% from new accounts.

Monitor the next window; settlement should continue. The observed evidence does not currently justify a reserve or pause. No disputes or refunds are recorded, and all eight shipments in the deadline-passed cohort have carrier confirmation. These findings reduce concern but do not establish fulfillment for every order or rule out later complaints.

Holiday demand or a marketing campaign could explain the increase; neither is verified. Reconcile dispute and refund feeds, review unresolved customer requests, sample recent high-value/new-account orders against carrier and fulfillment records, and obtain campaign attribution. Check buyer histories and shared identifiers for coordination.

Verified fulfillment, complete feeds and attributable sales would support dismissing the alert. Corroborated failed fulfillment, coordinated buyers or unresolved refund/dispute evidence would strengthen the bust-out hypothesis and warrant reconsidering a reserve or reversible settlement pause. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Check carrier tracking and fulfillment records for recent high-value and new-account orders, including orders outside the eight-shipment cohort; confirmed delivery supports dismissal, while verified failed fulfillment strengthens concern.; Reconcile refund requests, cancellations and completed refunds with support and payment records; identify unresolved requests or missing feed records.; Verify dispute-feed completeness and inspect any newly learned disputes by stated reason and underlying order.; Match campaign and holiday-promotion dates to the sales increase and new-account acquisition sources.; Review buyer account history and shared identifiers among spike orders, and reconcile order totals and timestamps against source records.

## Merchant 15 — alert episode 2025-01-26
Triggers: AUP-06.1 breach: 3 disputes on 25 orders in 30d (12.0%); a 2.5% rate gives >= 3 with p = 0.026
**Recommended action: reserve**

Merchant 15 triggered AUP-06.1 on January 26: three disputes learned in 30 days against 25 approved orders (12%), all for item not received. At the policy rate of 2.5%, the probability of at least three disputes is 0.026; this supports a rate breach, not a finding of fraud.

The broader pattern does not show a sales ramp: volume_z is -1.887 and ticket_drift is 1.022. All four deadline-eligible recent shipments have carrier confirmation, but that small cohort may not cover the disputed orders. Zero recorded refunds does not establish whether customers requested them.

Recommend a temporary payout reserve, with its percentage set by the human risk owner. Current evidence supports fulfillment review but does not corroborate bust-out or justify termination.

First reconcile dispute identities and the approved-order denominator, then inspect tracking, customer communications and refund records for the three claims. Verified overdue non-delivery, concentrated thin buyers and settlement extraction would strengthen bust-out concerns. Corrected records or verified fulfillment would weaken the alert. Check campaign records for a benign explanation and reassess after reconciliation and the next window.

Evidence gaps: Reconcile the three disputes to unique case IDs, stated reasons, dates learned and order IDs; verify the 25 approved orders and completeness of the window.; Check carrier tracking, promised delivery dates and customer communications for each disputed order. Verified overdue non-delivery would strengthen the alert; delivery evidence or corrected dispute records would weaken it.; Match disputed orders to refund requests, refund issuance and payment-ledger entries; establish whether unresolved customer claims explain the zero recorded refunds.; Review campaign dates and order-level buyer concentration around disputed sales. Documented campaign activity with verified fulfillment would support a benign explanation; concentrated thin accounts with failed fulfillment would strengthen bust-out concerns.; Confirm shipment-feed completeness and whether the disputed orders overlap the four eligible shipments.

## Merchant 147 — settlement-pause escalation 2025-02-02 (case opened 2024-12-19)
Triggers: AUP-06.6 delivery confirmation: 6 of 10 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 2.2e-06)
**Recommended action: pause_settlement**

Recommend that the human case owner pause settlement pending expedited review. This February 2 alert escalates the case opened December 19: six of ten shipments past the five-day confirmation deadline remain unconfirmed, versus a 4.82% reference share (p = 2.23e-06). The anomaly is strong, although the cohort is small and missing confirmation does not prove non-delivery.

The trailing window contains 53 orders and $16,659.82 GMV; volume_z is 3.88, ticket_drift is 1.24 and new_gmv_share is 77.39%. These support investigation but do not establish thin buyer accounts. Zero recorded disputes and refunds do not resolve the fulfillment concern.

First verify the six shipments directly with carriers and check tracking ingestion and deadline calculations. Review merchant fulfillment evidence, affected customer reports, pending refunds and dispute records. Compare sales with documented campaigns and buyer-account characteristics.

Verified delivery or a corrected data defect could dismiss the alert; documented campaigns with sound fulfillment could explain the sales increase. Verified nonreceipt, fabricated tracking or corroborated settlement extraction would strengthen bust-out concern. The proposed pause is reversible; current evidence does not justify offboarding.

Evidence gaps: Check the six shipments directly against carrier tracking, validating shipment dates, the five-day deadline, tracking joins and ingestion health. Confirmed delivery or corrected records would weaken or dismiss the alert.; Request fulfillment evidence for those orders and contact affected customers where tracking remains unresolved. Verified nonreceipt, fabricated tracking or absent shipment evidence would strengthen the bust-out hypothesis.; Reconcile refund requests, cancellations and pending refunds with the zero recorded refunds; inspect dispute intake and reason records against the reported zero disputes.; Check campaign dates, promotions, product mix and buyer-account characteristics against the sales increase. Documented campaigns, legitimate buyers and verified fulfillment would support a benign explanation.

## Merchant 149 — alert episode 2025-02-10
Triggers: AUP-06.4: new-account GMV share 75%; AUP-06.4b young merchant: age 35 days (< 90), new-account GMV share 75% (>= 60%)
**Recommended action: monitor**

As of 2025-02-10, merchant 149 triggered new-account concentration alerts: 608761 of 815146 cents in trailing-30-day GMV (74.68%) came from new accounts. Merchant age is 35 days. The baseline contains only six days and three orders; null volume and ticket comparisons do not establish a spike or imply zero risk.

One unauthorized-use dispute was learned of against 27 approved orders (3.70%). The breach probability of 0.491 provides weak evidence against the policy-rate benchmark. There are no recorded fulfillment disputes or refunds. All 11 deadline-eligible shipments have carrier confirmation; this supports fulfillment but does not independently prove customer receipt.

Recommend monitoring the next window; current evidence does not justify pausing settlement. Review tracking, buyer links, the dispute record, refund requests and campaign attribution now. Correlated buyers plus corroborated fulfillment failures would strengthen bust-out concerns and warrant reconsidering payouts. Valid fulfillment and documented acquisition activity would weaken the alert. A human owns any action.

Evidence gaps: Spot-check carrier tracking and delivery destinations for recent high-value orders; corroborated non-delivery or mismatched tracking would strengthen bust-out concerns, while valid fulfillment would weaken them.; Inspect the unauthorized-use dispute record and check whether high-value new buyers share payment instruments, devices or delivery addresses.; Reconcile refund requests, cancellations and support complaints with the zero recorded refunds; unresolved fulfillment complaints would change the decision.; Request campaign dates, acquisition channels and order attribution; a documented campaign with independently fulfilled purchases would support a benign explanation.; Reconcile order, account-age, dispute, refund and shipment feeds against source records to identify missing events or classification errors.

## Merchant 143 — alert episode 2025-02-15
Triggers: AUP-06.1 breach: 4 disputes on 52 orders in 30d (7.7%); a 2.5% rate gives >= 4 with p = 0.043
**Recommended action: reserve**

As of February 15, merchant 143 breached AUP-06.1: four disputes learned of in 30 days against 52 approved orders (7.7%). At the 2.5% policy rate, the probability of at least four is 0.043. Two complaints concern nonreceipt, one product description, and one unauthorized use.

Recommend a payout reserve while a human reviews the records. Bust-out is uncorroborated: volume_z is -1.126, ticket_drift is 0.974, and new_gmv_share is 15.5%. One of nine deadline-eligible shipments lacks confirmation; delivery_p of 0.359 provides weak evidence of an unusual confirmation shortfall and does not prove non-delivery. Zero recorded refunds does not establish that customers have no unresolved refund requests.

Prioritize dispute and order reconciliation, carrier evidence, refund queues, and campaign records. Verified fulfillment, resolved complaints, or corrected source data would reduce concern. Repeated verified non-delivery, unresolved refunds, and evidence of payout extraction would strengthen it. Pause settlement if review corroborates ongoing fulfillment failure and exposure; offboarding requires corroborated bust-out evidence. No case_opened escalation is supplied.

Evidence gaps: Review the four dispute records, deduplicate them, and reconcile the 52 approved orders and event timestamps to source records; corrected counts could dismiss the breach.; Check tracking, carrier acceptance and delivery evidence for the two item-not-received disputes and the overdue unconfirmed shipment; inspect the not-as-described complaint and merchant response.; Reconcile refund requests, cancellations, issued refunds and pending refunds against the reported zero refunds; unresolved requests would strengthen concern.; Request the campaign calendar and sales breakdown by product and buyer cohort; verify whether promotions explain disputed orders and whether thin buyer accounts are concentrated.; Compare recent settlements with outstanding fulfillment obligations and obtain evidence that disputed orders were fulfilled or remedied; corroborated extraction of payouts while abandoning delivery would support escalation.

## Merchant 149 — settlement-pause escalation 2025-03-06 (case opened 2025-02-10)
Triggers: AUP-06.6 delivery confirmation: 6 of 9 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 9.3e-07)
**Recommended action: pause_settlement**

Recommend a reversible settlement pause pending human review under AUP-1 §06. The March 6 alert occurs in a record with a case opened February 10; review that case's disposition.

Observed: six of nine shipments remain unconfirmed past five days, versus a 4.82% reference share (p = 9.3e-07). Thirty-day sales total 49 orders and 1,770,600 cents; volume_z is 4.29 and new-GMV share is 81.4%. The baseline contains only 30 days. One dispute alleges unauthorized use; none allege nonreceipt or misdescription. Chargeback probabilities provide weak evidence of a rate breach. Recorded refunds are zero.

Bust-out is plausible but uncorroborated. Campaign growth, fulfillment strain or missing carrier data could explain the pattern. Missing confirmation alone is not proof of non-delivery.

First reconcile all nine shipments with direct carrier records and sample buyer receipt checks. Review refund requests, dispute records, campaign attribution and buyer-account concentration. Verified non-delivery combined with coordinated buyers or false shipping evidence would strengthen bust-out concerns. Verified receipt and a corrected feed would dismiss the delivery alert; campaign attribution would help explain growth. Resume settlement if checks resolve the concern. Offboarding is not supported by current evidence.

Evidence gaps: Check the existing case's findings and disposition; establish whether this delivery alert repeats an earlier unresolved problem.; Reconcile all nine shipments against direct carrier tracking, order IDs and deadline timestamps; check feed outages, duplicates and matching errors.; Request dispatch and delivery evidence for the six unconfirmed shipments and contact a small buyer sample to verify receipt.; Review pending, rejected and completed refund requests and reconcile refunds to payment records; zero recorded refunds does not establish zero requests.; Validate the unauthorized dispute's reason and linked order, and review available fulfillment complaints and dispute records.; Verify campaign dates, spend and attributable orders; inspect buyer-account history and linked-account concentration before inferring thin or coordinated buyers.

## Merchant 37 — alert episode 2025-03-14
Triggers: AUP-06.1 breach: 7 disputes on 128 orders in 30d (5.5%); a 2.5% rate gives >= 7 with p = 0.045
**Recommended action: reserve**

Merchant 37 breaches AUP-06.1: seven disputes learned of in 30 days against 128 approved orders (5.47%); the probability of reaching that count at the 2.5% policy rate is 0.0446. Four allege unauthorized use, two non-receipt, and one misdescription.

Recommend a payout reserve, with the percentage set by the human reviewer under policy. Settlement should not pause on this record: no case_opened escalation is supplied, volume_z is negative (-2.53), and none of 23 deadline-eligible shipments lacks carrier confirmation. Confirmation does not establish satisfactory fulfillment of every order. Zero recorded refunds is also inconclusive.

Bust-out is currently a low-likelihood hypothesis. Reconcile dispute and order records first, then inspect disputed-order tracking, customer communications, refund requests, and unauthorized-use buyer links. Obtain campaign records to assess benign explanations. Verified non-delivery together with suspicious buyer links would strengthen the alert; valid fulfillment or corrected dispute data would weaken it. Neither termination nor a bust-out finding is supported without corroboration. The human reviewer owns the action.

Evidence gaps: Reconcile the seven disputes to processor records and unique orders; verify reason codes, learned dates, and the completeness of the 128-order denominator.; Inspect tracking and customer communications for the two item-not-received disputes and the not-as-described dispute; verify carrier confirmations independently.; Check refund requests, cancellations, pending refunds, and processor refund records; zero recorded refunds does not establish satisfied customers.; Review the four unauthorized-use cases for shared buyer, device, address, or payment patterns and any merchant connection.; Request dated campaign records and compare daily sales with the baseline. Corroborated delivery failures plus linked suspicious buyers would strengthen bust-out concerns; valid fulfillment, independent buyers, or corrected data would weaken them.

## Merchant 120 — alert episode 2025-03-31
Triggers: AUP-06.2: volume z=3.3 vs baseline; AUP-06.4: new-account GMV share 44%
**Recommended action: reserve**

As of March 31, volume z=3.30 and new-account GMV share=44.45% triggered review. The merchant recorded 22 orders and $3,800.15 GMV in 30 days versus 33 orders and $5,489.08 across the preceding 90 days. Ticket drift is 1.038.

Recommend a temporary percentage reserve while completing targeted checks; size it against unsettled exposure. Settlement should not pause on this evidence. One of four deadline-past shipments lacks carrier confirmation; delivery_p=0.179 is weak evidence against the reference share, and missing confirmation does not establish non-delivery. Known disputes and refunds are zero, subject to feed verification.

Bust-out remains a hypothesis. Corroborated fulfillment failures, linked buyer accounts and unresolved complaints would strengthen it. Verified deliveries, complete dispute/refund records and campaign-attributed sales would support releasing the reserve and monitoring. Obtain carrier evidence, inspect refund requests and dispute records, and validate campaign attribution. Offboarding is unsupported.

Evidence gaps: Check carrier scans and delivery evidence for the unconfirmed shipment, then sample fulfillment of recent high-value and new-account orders. Verified delivery would weaken the alert; corroborated failed fulfillment would strengthen it.; Reconcile dispute and refund feeds to source records, including pending customer complaints and refund requests. Confirm completeness before relying on the reported zeros.; Request campaign dates, promotion details and order attribution; compare the sales increase with campaign activity and available seasonal or category history.; Check recent buyers for linked accounts, repeat addresses and concentrated spending, and reconcile order totals and new-account classification to source transactions.

## Merchant 151 — alert episode 2025-04-09
Triggers: AUP-06.4: new-account GMV share 63%; AUP-06.4b young merchant: age 36 days (< 90), new-account GMV share 63% (>= 60%)
**Recommended action: monitor**

Merchant 151 triggered the new-account concentration and young-merchant rules on April 9. At 36 days old, it recorded 32 trailing-30-day orders and 2,156,075 cents of GMV; 63.47% came from new accounts. The baseline contains only two orders across six days. Null volume and ticket comparisons do not establish a sales spike.

Bust-out is plausible but uncorroborated. No disputes or refunds are recorded, and all eight deadline-eligible shipments have carrier confirmation. These observations weaken a fulfillment-failure hypothesis but do not prove every buyer received the promised goods. A marketing campaign could explain the acquisition mix.

Recommend monitor through the next window while checking tracking, buyer receipt, refund requests, dispute ingestion and campaign attribution. Verified fulfillment and campaign-linked sales would support dismissing the alert. Fabricated shipment evidence, corroborated non-delivery or coordinated buyer accounts would strengthen it and could justify a reversible settlement pause pending human review. The current evidence does not support offboarding.

Evidence gaps: Check carrier tracking and order-to-shipment linkage for the eight deadline-eligible shipments; sample buyer receipt confirmations. Verified receipt weakens bust-out, while fabricated tracking or corroborated non-delivery strengthens it.; Reconcile refund requests, cancellations and pending refunds against the zero recorded refunds; check for unresolved fulfillment complaints.; Reconcile dispute records and ingestion completeness, including the three stated reason categories; zero disputes known by the alert date does not establish successful fulfillment.; Request campaign dates and acquisition sources, then match them to new-account orders. Check sampled accounts for shared payment, contact or shipping identifiers.; Reconcile order and GMV totals, new-account definitions and feed completeness. Establish a longer usable baseline before interpreting growth.

## Merchant 151 — settlement-pause escalation 2025-04-26 (case opened 2025-04-09)
Triggers: AUP-06.6 delivery confirmation: 6 of 12 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 9e-06)
**Recommended action: pause_settlement**

Merchant 151’s April 26 alert falls within the case opened April 9. Pause settlement pending prompt review; this is a reversible response to the fulfillment concern.

Observed: 6 of 12 shipments past the five-day confirmation deadline remain unconfirmed (50%), versus a 4.82% portfolio reference; p = 9.02e-06. This strongly flags an unusual confirmation count, but does not prove non-delivery. The trailing window contains 48 orders and 3,810,749 cents GMV; the available 23-day baseline contains 11 orders and 929,916 cents. Volume z-score and ticket drift are unavailable. Reported disputes and refunds are zero; those counts do not resolve the delivery concern.

Bust-out is plausible but uncorroborated. Carrier-feed gaps or a marketing-driven fulfillment backlog remain benign possibilities. Check the six shipments directly with carriers and customers, reconcile ingestion and deadlines, inspect refund requests and dispute-feed completeness, and obtain campaign records. Verified receipt or corrected confirmation data would support lifting the pause. Corroborated non-delivery combined with coordinated buyer activity or settlement extraction would strengthen bust-out. A human owns the action; current evidence does not justify offboarding.

Evidence gaps: Check all six unconfirmed shipments directly with carriers for acceptance, tracking events and delivery proof; seek customer receipt confirmation where records remain unclear. Verified receipt would dismiss the fulfillment concern; absent handoff and customer reports of nonreceipt would strengthen it.; Reconcile carrier-source events with ingestion logs, deadline calculations and shipment eligibility. Missing imported confirmations or misclassified deadlines would support a data issue.; Inspect pending refund requests, cancellations and processing records against the reported zero refunds; determine whether customers are being refunded for fulfillment failures.; Verify dispute-feed completeness and review any available customer complaints or dispute records by stated reason. Confirm whether the reported zero counts reflect complete records.; Request dated campaign records and promotion-linked orders, and review buyer-account history and shared identifiers. A documented campaign with verified fulfillment supports a benign explanation; coordinated thin accounts plus corroborated non-delivery supports bust-out.

## Merchant 53 — alert episode 2025-05-17
Triggers: AUP-06.1 breach: 3 disputes on 29 orders in 30d (10.3%); a 2.5% rate gives >= 3 with p = 0.037
**Recommended action: reserve**

Merchant 53 breached AUP-06.1 on May 17: three disputes learned of in 30 days against 29 approved orders (10.3%). At the 2.5% policy rate, the probability of at least three is 0.0373. All three customers reported item not received.

This supports a fulfillment investigation, but does not establish bust-out. Volume_z is 0.319. All three shipments in the eligible delivery cohort have carrier confirmation; that small cohort may not cover the disputed orders. Zero recorded refunds does not establish that no customers requested refunds.

Recommend a human-approved percentage reserve pending prompt review. The supplied record has no case_opened delivery escalation; current evidence does not warrant pausing settlement or offboarding.

Match disputes to orders and carrier evidence, check outstanding fulfillment and refund requests, and reconcile source records. Corroborated non-delivery with continued payout exposure would support a settlement pause. Verified delivery, invalid disputes, or corrected data would weaken the alert. Campaign and product-mix records could explain the ticket change, but cannot alone dismiss the fulfillment complaints.

Evidence gaps: Review the three item-not-received dispute records for distinct orders, customer statements, merchant responses, and matched carrier delivery evidence; verified delivery or invalid disputes would weaken the alert.; Check fulfillment status and tracking for disputed orders and other recent orders; corroborated non-delivery across orders would strengthen the alert and support pausing settlement.; Inspect refund requests, pending or failed refunds, and processor records; determine whether the recorded zero refunds reflects no requests or unresolved customer claims.; Check campaign dates, promotion records, and SKU mix against the ticket change; documented legitimate sales activity with verified fulfillment would support a benign explanation.; Reconcile the 29 approved orders and three disputes to source records, and establish whether the three eligible shipments include any disputed orders.

## Merchant 103 — alert episode 2025-06-11
Triggers: AUP-06.2: volume z=3.0 vs baseline; AUP-06.4: new-account GMV share 41%
**Recommended action: monitor**

As of June 11, merchant 103 has two alerts: volume z=3.01 and new-account GMV share of 41.3%. The trailing 30 days contain 43 orders and $2,484.93 GMV, versus 78 orders and $5,383.59 across the preceding 90 days. These totals cover different durations.

There are zero known disputes and refunds in the trailing window. This does not establish successful fulfillment. One of 12 deadline-eligible shipments lacks carrier confirmation after five days; delivery_p=0.447 provides weak evidence of an abnormal confirmation shortfall and does not prove non-delivery.

Recommend monitor, with prompt targeted checks and reassessment next window. Current evidence does not justify pausing settlement or offboarding; no case-opening escalation is supplied.

Verify the overdue shipment, sample fulfillment, reconcile refund requests and dispute records, and check campaign attribution and new-buyer links. Verified delivery, clean source reconciliation and campaign-attributed sales would support dismissing the alert. Corroborated fulfillment failures, connected buyers and unexplained sales acceleration would strengthen bust-out concerns and warrant reconsidering a reserve or reversible settlement pause. A human owns the action.

Evidence gaps: Check carrier tracking for the one overdue unconfirmed shipment; sample recent confirmed shipments against orders and customer receipt evidence.; Reconcile recent orders and new-account classifications to source records; check ingestion completeness for both comparison windows.; Review refund requests, cancellations, support complaints and pending dispute records, including stated reasons, against the reported zero counts.; Request campaign dates and order attribution; inspect new buyers for linked identities, payment instruments or delivery addresses.

## Merchant 55 — alert episode 2025-07-20
Triggers: AUP-06.1 warn: 3 disputes on 46 orders in 30d (6.5%); a 1.5% rate gives >= 3 with p = 0.033; AUP-06.4: new-account GMV share 41%
**Recommended action: reserve**

Merchant 55, 2025-07-20: recommend a temporary partial payout reserve, with the percentage set by the human reviewer. Settlement should not pause on current evidence.

Three disputes learned of in 30 days against 46 approved orders produce a 6.5% ratio; at the 1.5% warning rate, the probability of at least three is 0.033. Two concern unauthorized use and one concerns description; none concerns nonreceipt. New-account GMV share is 41%. Volume_z is −1.77, which does not support a sales ramp.

Two of 12 deadline-eligible shipments lack carrier confirmation (reference share 4.82%; p=0.111). This warrants checking, not a finding of non-delivery. Zero recorded refunds does not establish satisfied customers.

Review dispute files, buyer links, tracking, unresolved refund requests, campaign records, and source-system reconciliation. Linked buyers plus corroborated fulfillment failures would strengthen bust-out concerns and support pausing settlement. Verified delivery, legitimate acquisition, and reconciled records would weaken the alert and support releasing the reserve. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records and underlying orders: verify reason codes, duplicates, authorization evidence, and links among buyers or to the merchant.; Check carrier tracking and deadline calculations for the two unconfirmed shipments; sample recent fulfilled orders for independent delivery evidence.; Reconcile refund requests, cancellations, support complaints, and processed refunds; determine whether the zero recorded refunds conceals unresolved requests.; Request dated campaign records and acquisition sources, then reconcile them with new-account orders and check account classification.; Reconcile order, dispute, refund, and carrier records against source systems to identify missing or delayed ingestion.

## Merchant 69 — alert episode 2025-07-24
Triggers: AUP-06.1 breach: 3 disputes on 32 orders in 30d (9.4%); a 2.5% rate gives >= 3 with p = 0.047
**Recommended action: reserve**

Merchant 69 breached AUP-06.1: three disputes learned of in 30 days against 32 approved orders (9.375%). At the 2.5% policy rate, the probability of at least three disputes is 0.0474; this is not the probability of bust-out. Two complaints concern items not as described and one concerns non-receipt.

Recommend holding a percentage of payouts through a reserve while reviewing these cases. Current evidence does not justify pausing settlement or offboarding. Volume_z is negative, so the episode lacks an observed sales ramp. None of five deadline-eligible recent shipments lacks carrier confirmation, although that small cohort cannot establish fulfillment across all orders. Zero recorded refunds does not establish that customers received satisfactory goods.

Confirm dispute uniqueness and substance, inspect tracking for disputed orders, and reconcile refund requests with actual refunds. Repeated verified non-delivery, product mismatches and unresolved valid refunds would strengthen the alert. Duplicate disputes, corrected records or documented satisfactory fulfillment would weaken it. Check campaign and product-mix records for a benign explanation of ticket drift, and reconcile source feeds before escalating.

Evidence gaps: Inspect the three dispute records for unique cases, underlying orders, customer statements and merchant responses; duplicates or corrected classifications could weaken the breach.; Check carrier tracking and delivery evidence for the disputed orders and a small recent-order sample; repeated verified non-delivery would strengthen concern, while verified delivery would weaken it.; Compare the two not-as-described complaints with listings and actual products; substantiated mismatches would confirm a product-quality problem.; Reconcile zero recorded refunds with support requests, pending refunds and payment records; unresolved valid requests would strengthen concern.; Review campaign dates, promotions and product mix against order records to explain ticket drift and identify any concentrated buyer activity.; Reconcile dispute, approved-order and carrier-feed totals with source records to confirm completeness as of the alert date.

## Merchant 158 — alert episode 2025-08-10
Triggers: AUP-06.4: new-account GMV share 73%; AUP-06.4b young merchant: age 39 days (< 90), new-account GMV share 73% (>= 60%)
**Recommended action: monitor**

As of August 10, merchant 158 is 39 days old. New accounts generated 72.6% of trailing-30-day GMV: 1,052,767 of 1,449,395 cents across 28 orders. These are the two triggered concerns. The baseline contains only two orders over five days; null volume and ticket comparisons do not establish either normality or acceleration.

One of five deadline-eligible shipments lacks carrier confirmation after the five-day deadline. Delivery p = 0.219 provides weak evidence against the portfolio reference share; missing confirmation does not prove non-delivery. Recorded disputes and refunds are zero, but neither establishes successful fulfillment.

Recommend monitor, with prompt targeted checks. Verify tracking and customer receipt, reconcile refund requests and dispute records, and match campaign evidence to new-account sales. Check buyer linkage and source-feed completeness. Verified fulfillment and attributable acquisition would support dismissing the alert. Corroborated non-delivery, coordinated buyers or concealed complaints would strengthen bust-out concern and support a reversible settlement pause pending human review. Current evidence does not justify offboarding.

Evidence gaps: Check carrier tracking for the overdue shipment and sample confirmed shipments; verified delivery would reduce concern, while corroborated non-delivery would strengthen it.; Reconcile refund requests, cancellations and completed refunds against the zero recorded refunds; check for unresolved customer complaints.; Verify dispute-feed completeness and inspect any underlying dispute records and stated reasons.; Request dated launch or campaign records and match them to new-account orders; check sampled buyers for account linkage or coordination.; Reconcile order, account-classification and carrier-ingestion records; confirm whether null comparisons reflect insufficient history.

## Merchant 158 — settlement-pause escalation 2025-08-29 (case opened 2025-08-10)
Triggers: AUP-06.6 delivery confirmation: 5 of 9 shipments past the 5-day deadline unconfirmed (reference 4.8%; p = 2.8e-05)
**Recommended action: pause_settlement**

Merchant 158 has an existing case opened August 10. On August 29, five of nine shipments past the five-day confirmation deadline remain unconfirmed, versus a 4.82% portfolio reference. The delivery tail probability is 0.0000279; it measures the unusual confirmation count, not the probability of bust-out.

Pause settlement pending expedited human review. This reversible step is warranted by the delivery escalation; termination lacks corroborated bust-out evidence. Missing confirmation alone does not prove non-delivery.

The trailing window contains 47 orders and 3,092,987 cents GMV. Zero recorded disputes and refunds do not resolve the delivery concern. The baseline covers only 24 days; null volume and ticket comparisons leave growth uncertain. Zero orders on the alert date does not establish cessation.

First verify the five shipments with carriers and reconcile tracking events, ingestion, and deadlines. Verified timely deliveries or a corrected pipeline would support dismissing the alert and resuming payouts. Confirmed non-delivery, unresolved refund requests, customer complaints, or fabricated orders would strengthen concern. Reconcile refund and dispute records, and check dated campaign evidence against sampled orders and deliveries.

Evidence gaps: Check the five unconfirmed shipments directly with carriers: validate tracking, shipment dates, deadline calculations, and delivery evidence. Verified timely delivery would dismiss the fulfillment concern; confirmed non-delivery would strengthen it.; Reconcile carrier events with ingestion logs and recompute the nine-shipment cohort. Missing events or incorrect eligibility could explain the alert.; Review refund requests, cancellations, merchant responses, and completed refunds against payment records; zero recorded refunds does not establish zero requests.; Reconcile dispute records with processor notifications and inspect any customer complaints for unauthorized use, non-receipt, or misdescription.; Request dated campaign or seasonal-sales evidence and sample orders for buyer authenticity and fulfillment. A documented campaign with verified deliveries supports a benign explanation; fabricated orders or deliberate non-fulfillment would corroborate bust-out.

## Merchant 14 — alert episode 2025-09-14
Triggers: AUP-06.1 breach: 6 disputes on 102 orders in 30d (5.9%); a 2.5% rate gives >= 6 with p = 0.045
**Recommended action: reserve**

Merchant 14 breaches AUP-06.1 as of September 14: six disputes learned of in 30 days against 102 approved orders (5.9%). At the 2.5% policy rate, the probability of at least six is 0.0454. Reasons comprise three item-not-received, one not-as-described and two unauthorized-use disputes.

Recommend a payout reserve, with the percentage set by the human risk owner, pending prompt review. The breach warrants protection, but bust-out is uncorroborated: volume_z is -5.716, and no evidence establishes thin-account concentration or settlement extraction. Zero recorded refunds does not establish that customers have no refund requests. The shipment cohort is empty and delivery_p is null, so delivery performance is unknown.

Reconcile dispute and order records, inspect fulfillment evidence for the disputed orders, and reconcile requested and pending refunds. Check shipment-feed coverage and campaign records. Verified fulfillment failures plus linked buyer abuse would support escalation to a reversible settlement pause. Reliable delivery evidence, resolved complaints or a corrected dispute count would weaken the alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the six dispute records and 102 approved orders to source records; check duplicates, dates and stated reasons. A corrected count below the breach would weaken the alert.; For the three item-not-received disputes, inspect order promises, tracking and carrier scans; review the not-as-described complaint and the two unauthorized-use records. Verified failed fulfillment and linked buyer abuse would strengthen concern; documented delivery and resolved complaints would weaken it.; Reconcile refund requests, pending refunds and payment-processor records against the zero recorded refunds; identify unresolved customer requests.; Verify shipment-feed completeness and why no shipments qualify for the delivery cohort; null delivery_p cannot establish successful delivery.; Check campaign dates, seasonal/category patterns and recent buyer-account concentration against approved orders. A documented legitimate campaign would support a benign explanation; concentrated thin accounts would strengthen bust-out concern.

## Merchant 157 — alert episode 2025-09-18
Triggers: AUP-06.1 breach: 3 disputes on 21 orders in 30d (14.3%); a 2.5% rate gives >= 3 with p = 0.016
**Recommended action: reserve**

As of September 18, three disputes were learned of against 21 approved orders in the trailing 30 days (14.3%). At the 2.5% policy rate, the probability of at least three is 0.01635. All three concern fulfillment: two not as described and one not received. These are customer-stated reasons, not verified failures.

Recommend a payout reserve, with the percentage set by the human reviewer. The breach warrants protection while records are checked; negative volume_z does not support a sales ramp. Bust-out remains uncorroborated. Zero recorded refunds does not establish whether customers requested remedies. The empty shipment cohort and null delivery_p cannot assess delivery performance.

Verified unresolved fulfillment failures across disputed and sampled orders would strengthen the alert and support pausing settlement. Valid fulfillment evidence, corrected dispute records and completed remedies would weaken it and support monitoring. Check campaign and seasonal explanations against actual order activity. Offboarding requires corroborated bust-out evidence; the human reviewer owns the action.

Evidence gaps: Reconcile the three dispute records to distinct approved orders, reason codes, customer statements and notification timestamps; verify the 21-order denominator and remove duplicates or ingestion errors.; For the disputed orders, inspect carrier scans, delivery evidence, promised dates, product listings and customer communications. Check a small sample of other recent orders for similar fulfillment failures.; Reconcile the zero recorded refunds with the payment ledger, refund requests and pending refunds; establish whether unresolved complaints are being remedied.; Confirm shipment-feed completeness and why no shipments qualified for the deadline-passed cohort; do not interpret delivery_p = null as reassuring.; Request campaign dates, promotions and seasonal product changes, then compare them with order activity and complaints.

## Merchant 34 — alert episode 2025-09-19
Triggers: AUP-06.1 breach: 4 disputes on 50 orders in 30d (8.0%); a 2.5% rate gives >= 4 with p = 0.038
**Recommended action: reserve**

Merchant 34 breaches AUP-06.1: four disputes learned of in 30 days against 50 approved orders (8%). At the 2.5% policy rate, the probability of at least four is 0.038; this supports reviewing the rate breach, not a fraud conclusion. Two disputes concern non-receipt, one description, and one unauthorized use. No refunds are recorded.

Bust-out remains uncorroborated: volume_z is -7.71, inconsistent with a sales ramp. The shipment cohort is empty and delivery_p is null, so delivery cannot be assessed from these metrics.

Recommend a percentage reserve under applicable policy while a human reviews the evidence. Settlement should not pause on this record alone; no case_opened escalation is supplied.

First reconcile disputes and approved orders, inspect carrier evidence and customer contacts, and verify refund requests and processing. Check shipment-feed completeness and documented campaigns. Valid fulfillment or corrected counts could dismiss the alert; repeated unfulfilled orders, unresolved refunds, and associated payouts would support escalation to a reversible settlement pause. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Reconcile the four dispute records and 50 approved orders with source systems; verify uniqueness, reasons, and dates learned. Corrected counts could dismiss the breach.; Inspect order-level tracking and carrier delivery evidence for the disputed purchases, plus a small recent-order sample. Verified delivery would weaken non-delivery concerns; repeated unfulfilled orders would strengthen them.; Check refund requests, processing records, and customer contacts to distinguish no refunds requested from unresolved requests or missing refund data.; Confirm whether the zero shipment cohort reflects no deadline-eligible shipments or a shipment-feed gap.; Request campaign dates and affected orders, and compare disputes with category peers. A documented campaign with verified fulfillment or ordinary peer-level dispute patterns would support a benign explanation.; Review recent settlement records alongside fulfillment status; payouts against repeatedly unfulfilled orders would strengthen the case for pausing settlement.

## Merchant 73 — alert episode 2025-09-19
Triggers: AUP-06.1 breach: 5 disputes on 76 orders in 30d (6.6%); a 2.5% rate gives >= 5 with p = 0.044
**Recommended action: reserve**

As of 2025-09-19, merchant 73 has five disputes against 76 approved orders in 30 days (6.58%). At the 2.5% policy rate, the probability of at least five disputes is 0.044; this supports the breach, not a probability of fraud. Three disputes allege item not received, one not as described, and one unauthorized use.

Recommend a payout reserve, with the percentage set by the human risk owner. Fulfillment complaints warrant protection during review, but the strongly negative volume signal does not show a bust-out ramp. Zero recorded refunds requires reconciliation. The shipment cohort is empty and delivery_p is null, so delivery confirmation offers no comparison. This record is not a case-opened delivery escalation; settlement need not pause on this evidence alone.

Validate dispute and approved-order records, inspect carrier evidence and complaint resolution, reconcile refunds, and check ingestion completeness. Review campaign records, buyer histories and settlements. Corroborated unresolved fulfillment failures plus extraction patterns would strengthen the bust-out hypothesis and support pausing payouts. Verified fulfillment, resolved complaints or corrected data would weaken the alert. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Validate the five dispute records for duplicates, reason codes, order linkage and merchant responses; reconcile the 76 approved orders with source records.; Check carrier tracking and delivery evidence for the three item-not-received disputes and inspect the not-as-described complaint. Corroborated unresolved failures strengthen the alert; valid delivery and satisfactory resolution weaken it.; Reconcile refund requests, cancellations and issued refunds against processor records; determine whether zero recorded refunds reflects no requests, unresolved requests or missing ingestion.; Check order, dispute, refund and shipment pipeline completeness, including why the eligible shipment cohort is empty; recompute metrics after any correction.; Request campaign dates, promotion records and seasonal sales comparisons; inspect associated buyer-account history and settlement records for concentrated thin-account purchasing or extraction.

## Merchant 31 — alert episode 2025-09-20
Triggers: AUP-06.1 breach: 3 disputes on 32 orders in 30d (9.4%); a 2.5% rate gives >= 3 with p = 0.047
**Recommended action: reserve**

Merchant 31 breaches AUP-06.1: three disputes among 32 approved orders (9.375%). At the 2.5% policy rate, the probability of at least three is 0.0474. All three concern fulfillment: two item-not-received and one not-as-described.

This supports reviewing fulfillment, but does not establish bust-out. Volume is sharply below baseline (z = -7.21), and reported new-buyer GMV is zero. No refunds are recorded; whether customers requested refunds is unknown. The eligible shipment cohort is empty and delivery_p is null, so delivery performance cannot be assessed from that metric.

Recommend a temporary payout reserve, with the human reviewer setting the percentage. Settlement should not pause on the supplied evidence alone.

Confirm the alert by validating the dispute records and finding missing fulfillment, unresolved refunds or corroborating extraction activity. Corrected order/dispute counts could dismiss the statistical breach; verified fulfillment and resolved complaints could reduce concern. Check tracking, refund requests and processor records first, then reconcile data coverage and campaign dates. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Inspect the three dispute records: confirm uniqueness, reason codes, order linkage and supporting customer evidence.; Check carrier tracking and delivery evidence for the disputed orders, plus current outstanding fulfillment; establish why the eligible shipment cohort is empty.; Review refund requests, promised refunds and processor records to distinguish no requests from unresolved or unrecorded refunds.; Reconcile approved orders, disputes and shipment ingestion against source records; corrected counts could dismiss the statistical breach.; Check campaign dates and seasonal sales records against the disputed orders; inspect buyer concentration and settlement records for any corroborating extraction pattern.

## Merchant 64 — alert episode 2025-09-24
Triggers: AUP-06.1 breach: 5 disputes on 67 orders in 30d (7.5%); a 2.5% rate gives >= 5 with p = 0.028
**Recommended action: reserve**

Merchant 64 breached AUP-06.1: five disputes on 67 approved orders (7.46%). At the 2.5% policy rate, the probability of at least five is 0.028; this supports a rate breach, not a probability of fraud. All five concern fulfillment: three item-not-received and two not-as-described.

Recommend holding a percentage of payouts as a reserve pending prompt review. Settlement should not pause on the present evidence. Sales contracted sharply against baseline (volume_z −13.95), weakening the sales-ramp bust-out hypothesis. No refunds are recorded. The delivery cohort is empty and delivery_p is null, so carrier-confirmation metrics cannot assess fulfillment.

First reconcile disputes and the order denominator, then inspect tracking, customer correspondence, refund requests and campaign records. Verified fulfillment failures, unresolved refunds and corroborated payout extraction would support escalation to a reversible settlement pause. Corrected records or credible fulfillment and resolution evidence would reduce concern. Offboarding is unsupported without corroborated bust-out evidence. A human owns the action.

Evidence gaps: Reconcile the five disputes to distinct orders and source records; verify reasons, notification dates and the completeness of the 67-order denominator. Duplicates or missing orders could dismiss the breach.; Check carrier tracking, delivery scans and customer correspondence for the five disputed orders. Verified delivery failures or misdescribed goods would corroborate fulfillment problems; credible resolution would reduce concern.; Review refund requests, issued refunds and processor reconciliation. Determine whether zero recorded refunds reflects no requests, unresolved requests or missing records.; Request dated seasonal and sales-campaign records, and reconcile the recent sales decline with order records.; Review settlement history and buyer-account concentration for evidence of payout extraction or coordinated purchasing; corroborated findings would strengthen the bust-out hypothesis.

## Merchant 63 — alert episode 2025-09-25
Triggers: AUP-06.1 breach: 5 disputes on 55 orders in 30d (9.1%); a 2.5% rate gives >= 5 with p = 0.013
**Recommended action: reserve**

As of September 25, merchant 63 breaches AUP-06.1: five disputes on 55 approved orders (9.1%). At the 2.5% policy rate, the probability of at least five is 0.0133. Reasons comprise two unauthorized-use, two item-not-received, and one not-as-described dispute.

Recommend a payout reserve pending targeted review; a human owns the action. The breach warrants protection, but bust-out is not corroborated: volume_z is −15.56, indicating contraction rather than a ramp. Zero reported refunds does not establish resolved complaints. The delivery cohort is empty and delivery_p is null, so delivery performance cannot be assessed.

First reconcile orders and disputes, verify the three fulfillment complaints against tracking and customer correspondence, and check requested or pending refunds. Review campaigns and seasonal context alongside buyer/payment links and settlement activity. Validated disputes plus corroborated fulfillment failures and extraction patterns would strengthen bust-out concern and support pausing settlement. Corrected records or verified delivery and resolved complaints would weaken the alert. Current evidence does not justify offboarding.

Evidence gaps: Reconcile the 55 approved orders and 5 disputes to source records; verify ingestion completeness, deduplication, reason codes, and order linkage.; Review fulfillment records for the three fulfillment-related disputes and a small recent-order sample: tracking, promised dates, carrier confirmation, and customer correspondence. Confirmed receipt would weaken non-delivery concerns; corroborated missed delivery would strengthen them.; Check refund requests, cancellations, support complaints, and pending or failed refunds; reconcile them with the reported zero completed refunds.; Request campaign dates, promotions, and seasonal sales context; compare their timing and order mix with the observed volume decline and ticket drift.; Review the two unauthorized-use disputes and associated buyer/payment links, then inspect settlement withdrawals for corroborating concentration or extraction patterns.

## Merchant 115 — alert episode 2025-09-26
Triggers: AUP-06.1 breach: 4 disputes on 45 orders in 30d (8.9%); a 2.5% rate gives >= 4 with p = 0.028
**Recommended action: reserve**

As of September 26, four disputes were learned of against 45 approved orders in 30 days (8.9%). At the 2.5% policy rate, the probability of at least four is 0.0276. All concern fulfillment: three item-not-received and one not-as-described. No refunds are recorded.

Recommend a temporary percentage reserve, with the size set by the human reviewer after checking outstanding obligations. Settlement should not pause on this record alone. There is no case_opened escalation, and the empty shipment cohort provides no delivery-confirmation assessment; delivery_p is null, not evidence of successful delivery.

Fulfillment problems are credible, but bust-out remains uncorroborated. Volume_z is strongly negative, so this window does not demonstrate a sales ramp. Seasonal demand changes or incomplete data could explain parts of the pattern.

Review the four dispute files, carrier evidence, refund requests, source-system counts, campaign dates, and recent settlements. Verified undelivered orders combined with settlement extraction would strengthen bust-out concern and support pausing payouts. Verified delivery, resolved complaints, or corrected ingestion that removes the breach would support dismissing or reducing the alert. A campaign explanation alone would not resolve the fulfillment complaints.

Evidence gaps: Review all four dispute records against their underlying orders: verify uniqueness, stated reasons, supporting evidence, and resolution status.; Check carrier tracking and delivery evidence for the three item-not-received orders; inspect the product listing and complaint evidence for the not-as-described order.; Reconcile approved-order counts, disputes, refunds, and shipment feeds to source systems; confirm whether the empty shipment cohort is valid or reflects missing data.; Inspect pending refund requests and cancellations, then verify whether promised refunds were actually issued despite refunds_30d = 0.; Obtain campaign dates and seasonal sales history to explain the contraction; check whether campaign orders generated the disputed fulfillment promises.; Review recent settlements and outstanding fulfillment obligations for evidence of payout extraction alongside undelivered orders.

## Merchant 66 — alert episode 2025-09-27
Triggers: AUP-06.1 breach: 3 disputes on 32 orders in 30d (9.4%); a 2.5% rate gives >= 3 with p = 0.047
**Recommended action: reserve**

Merchant 66 — 2025-09-27. The supplied AUP-06.1 trigger reports three disputes on 32 approved orders (9.375%); at the 2.5% policy rate, the probability of at least three is 0.0474. All concern fulfillment: two item-not-received and one not-as-described. This warrants review despite the small count.

A bust-out is uncorroborated. Volume_z is −12.287 and ticket_drift is 1.028, offering no sales-ramp signal. Zero recorded refunds does not establish that complaints were resolved. The shipment cohort is empty and delivery_p is null, so delivery risk cannot be assessed from confirmation metrics.

Recommend a temporary percentage reserve, with the human owner setting its size and release conditions. Settlement should not pause on this evidence alone; no case_opened escalation is supplied. Verify dispute records, carrier evidence, outstanding fulfillment, refund requests and ledger entries, shipment-feed completeness, and campaign timing. Valid delivery or resolved complaints would weaken the alert; corroborated widespread non-delivery or coordinated payout extraction would support pausing settlement. Offboarding requires corroborated bust-out evidence.

Evidence gaps: Review the three dispute records for duplicates, order linkage, customer statements, merchant responses and outcomes; corrections could dismiss the breach, while verified unresolved complaints would confirm concern.; Check carrier tracking and fulfillment records for the disputed orders, then outstanding approved orders; verified delivery or resolution supports release, while corroborated widespread non-delivery supports pausing settlement.; Reconcile refund requests, approvals and payment-ledger entries; determine whether the reported zero refunds reflects no requests, unresolved requests or missing records.; Verify shipment-feed completeness and deadline eligibility to explain ship_cohort_n = 0; delivery_p = null provides no delivery-risk comparison.; Check campaign and seasonal sales records, buyer-account quality and settlement history; legitimate demand with verified fulfillment weakens bust-out, while coordinated thin buyers and payout extraction strengthen it.

## Merchant 121 — alert episode 2025-09-27
Triggers: AUP-06.1 breach: 3 disputes on 27 orders in 30d (11.1%); a 2.5% rate gives >= 3 with p = 0.031
**Recommended action: reserve**

Merchant 121 breaches AUP-06.1: three disputes learned of in 30 days against 27 approved orders (11.1%); at the 2.5% policy rate, the probability of at least three is 0.031. Two concern description and one non-receipt; none allege unauthorized use. No refunds are recorded.

Recommend a temporary payout reserve, sized to unresolved exposure. Settlement need not pause on the current evidence. Volume is sharply below baseline, so the observed pattern does not establish a sales-ramp bust-out. The empty eligible shipment cohort and null delivery probability provide no delivery clearance.

Verify dispute records, tracking/customer receipt and refund requests first; reconcile order ingestion and dated campaign records. Valid disputes with unresolved fulfillment failures support retaining or increasing protection. Duplicate disputes, corrected ingestion, verified receipt and resolved refunds would weaken the alert. Corroborated non-delivery combined with settlement extraction or linked thin buyer accounts would support pausing settlement. Offboarding requires corroborated bust-out evidence. A human owns the action.

Evidence gaps: Inspect the three dispute records for unique cases, stated reasons, notification dates, associated orders and resolution evidence; reconcile the 27 approved orders against source records.; Check carrier tracking and customer receipt evidence for the disputed orders, then sample outstanding paid orders. Verified receipt would weaken non-delivery concerns; repeated missed fulfillment would strengthen them.; Reconcile refund requests, returns, attempted refunds and completed refunds with the zero-refund ledger; identify unresolved customer exposure to size the payout reserve.; Request dated campaign and seasonal-sales records and compare daily orders with source-system totals; these could explain sales changes or reveal ingestion gaps.; Review recent settlements and buyer-account histories for concentrated purchases, linked accounts and unusually thin histories; combine any findings with verified fulfillment failures before escalating.

