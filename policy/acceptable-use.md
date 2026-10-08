# Merchant Acceptable Use & Underwriting Policy

**Document AUP-1** · Applies to merchant applications and ongoing portfolio monitoring on
the simulated BNPL platform. Screening verdicts, scorecard reason codes, and decision
records cite this document by section id (e.g. AUP-03, AUP-H2). Verdict levels used by
the screener: **pass / restricted / prohibited / insufficient-info**.

BNPL context, in one paragraph: the platform pays the merchant up front and collects from
the consumer in four installments, so a bad merchant is not a bystander to fraud — it is
a counterparty exposure. Merchant failure modes that cost the platform money: selling
what card networks or law prohibit (fines, MATCH-listing, bank scrutiny), not delivering
goods (chargebacks the platform eats after paying the merchant), counterfeit (brand
liability + chargebacks), and bust-out (ramp volume, extract settlement, disappear).

---

## AUP-01 — Prohibited categories

Applications in these categories are **declined regardless of other signals** (hard
override; no score can rescue them). Detection is content-based: product listings,
descriptions, imagery text, and customer reviews all count as evidence.

1. Weapons, ammunition, weapon parts and accessories.
2. Tobacco, vaping/e-cigarette products, nicotine delivery.
3. Cannabis, CBD, and derivative products (regardless of local legality — network rules).
4. Adult content and services.
5. Gambling, betting, lotteries, raffles, skill-game cash contests.
6. Cryptocurrency sales/exchange, gift-card resale, currency-like stored value,
   money-service activity. (Transaction-laundering magnet categories.)
7. Counterfeit or "replica"/"inspired-by" branded goods; unauthorized resale of
   trademarked goods at implausible discounts.
8. Multi-level marketing, pyramid-adjacent recruitment offers.
9. Medical claims products: "miracle" cures, disease-treatment claims outside approved
   pharma channels; prescription drugs.
10. Documents and credentials: IDs, diplomas, licenses; essay-writing mills.

## AUP-02 — Restricted categories (allowed with conditions)

Approval possible with limits, reserves, or enhanced monitoring; screener verdict
**restricted**, scorecard adds category weight, decision record states the condition.

1. Event tickets and experiences (delivery-window risk → rolling reserve).
2. Pre-orders / made-to-order with fulfillment > 3 weeks (INR exposure → volume cap).
3. High-ticket luxury goods (watches, designer bags) — counterfeit + ticket-size
   exposure → invoice/authentication checks, transaction cap.
4. Dietary supplements with structure/function claims (borderline of AUP-01.9 —
   requires claim review; "supports" language passes, "treats/cures" fails).
5. Digital goods and game keys (fraud-magnet, zero marginal cost → velocity caps).
6. Services with deposits (repairs, custom work) — deposit-and-disappear risk.
7. Dropshipping-signature stores (no inventory signals: stock-photo catalogs, 4–6 week
   shipping, no physical address) — conditional pending fulfillment evidence.

## AUP-03 — Merchant hygiene requirements

Missing hygiene is not prohibited-level, but each gap raises score (H-codes):

- **AUP-H1** Refund/return policy page present and findable.
- **AUP-H2** Shipping policy with stated timeframes.
- **AUP-H3** Contact information: at least email + one of phone/address.
- **AUP-H4** Terms of service present.
- **AUP-H5** TLS on checkout (and site generally).
- **AUP-H6** Business identity consistent across pages (name, jurisdiction).

## AUP-04 — Reputational evidence standards

Customer reviews are evidence about *future chargebacks*. The screener extracts themes;
underwriting weighs them as follows:

- **Non-delivery theme** (orders never arrived) — strongest predictor; >20% of recent
  reviews → decline-leaning regardless of category.
- **Counterfeit theme** ("fake", "replica", "not authentic") — any credible volume
  triggers AUP-01.7 review.
- **Refund-refusal theme** — pairs with AUP-H1 gaps; predicts disputes escalating to
  chargebacks.
- **Subscription-trap theme** (unwanted recurring charges) — restricted-level concern.
- Volume and recency matter: 3 bad reviews in a 2,000-review base ≠ 30% of last quarter.
  The screener reports theme share and a recency-weighted NPS proxy.

Review evidence must be **quoted verbatim** in verdicts; paraphrase is not evidence
(mechanically enforced — quotes are string-checked against the corpus).

## AUP-05 — Verdict and evidence rules for automated screening

1. Every section verdict cites the section id and quotes the exact site/review text it
   relies on. A verdict whose quote does not appear in the source is invalid (harness
   fails it).
2. **insufficient-info** is a first-class verdict: thin sites do not get benefit of the
   doubt; they get a manual-review outcome (fail-safe direction).
3. Prohibited detection is recall-critical: the acceptable operating point misses zero
   fixture-set prohibited merchants; false prohibited flags are tolerable (a human
   reviews declines).
4. The screener is advisory. The scorecard applies policy deterministically; a human
   owns final approval of conditional/manual cases.

## AUP-06 — Ongoing monitoring triggers (portfolio side)

Thresholds are config-driven and modeled on publicly known card-network monitoring
program *concepts* (values illustrative, not any network's actual numbers):

- **06.1 Chargeback rate**: warn at 1.5%, breach at 2.5% of approved orders over 30
  days. A level is reached when the disputes learned of in the last 30 days are more than
  that level would plausibly produce at the merchant's 30-day order volume: a Poisson
  count with mean level × orders reaches at least that many disputes with probability at
  most 5%. The window needs at least 3 disputes and 20 approved orders. A breach alerts
  alone; a warning needs a second trigger.
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

Actions ladder: monitor → reserve → settlement pause → offboard; memos cite the
triggering metric values.

## Reason-code index

AUP-01.x prohibited category · AUP-02.x restricted category · AUP-H1..H6 hygiene gaps ·
AUP-04.ND non-delivery theme · AUP-04.CF counterfeit theme · AUP-04.RR refund-refusal ·
AUP-04.ST subscription-trap · AUP-05.II insufficient info · AUP-06.x monitoring trigger.
