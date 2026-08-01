# DEC-heritage-watches — Heritage Watches

**Decision: MANUAL_REVIEW** · score 65 · reason codes: AUP-02.7, AUP-H1, AUP-H2, AUP-H3, AUP-H4, AUP-02

## Application
Claimed category: luxury_goods · country US · domain age 150d · TLS ok

## LLM screening (advisory)
Category: luxury_goods (confidence 0.85) · overall: restricted · NPS proxy: 78

Verdicts with evidence:
- **AUP-02.3 → restricted** — "1968 chronograph, gilt dial — $8,400" High-ticket luxury watch consignment triggers counterfeit/ticket-size condition requiring invoice/authentication checks and a transaction cap.
- **AUP-H3 → restricted** — "Email: support@heritage-watches.example" Only an email address is given; no phone or physical address appears anywhere in the site text, so the email-plus-one requirement is not met.
- **AUP-H1 → restricted** — "index · about · contact" Site navigation lists only these three pages on every page, with no refund/return policy page linked or referenced.
- **AUP-H2 → restricted** — "index · about · contact" Same three-page navigation recurs sitewide with no shipping/timeframe policy page present.
- **AUP-H4 → restricted** — "index · about · contact" No terms-of-service page is linked in the recurring site navigation.
- **AUP-H6 → pass** — "© 2026 Heritage Watches — all merchants on this fixture set are fictional." Business name is identical and consistent across index, about, and contact pages.

Review themes (verbatim, verified):
- [positive] "Smooth transaction on a five-figure piece."
- [positive] "The chronograph was exactly as photographed, superb condition."
- [positive] "The chronograph was exactly as photographed, superb condition."
- [positive] "The chronograph was exactly as photographed, superb condition."

## Scorecard breakdown
| factor | points | code | why |
|---|---|---|---|
| domain_age_under_180d | 15 | AUP-02.7 | domain 150d old |
| missing_refund_policy | 20 | AUP-H1 | no refund/return policy found |
| missing_shipping_policy | 10 | AUP-H2 | no shipping policy found |
| missing_contact | 15 | AUP-H3 | no usable contact info |
| missing_terms | 5 | AUP-H4 | no terms of service |
| hygiene_cap | -25 | AUP-03 | hygiene points capped at 25 |
| restricted_category | 25 | AUP-02 | restricted-tier category (luxury_goods) |
