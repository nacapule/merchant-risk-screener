# DEC-giftcardhub-mx — GiftCardHub MX

**Decision: DECLINE** · score 40 · reason codes: AUP-01.6, AUP-02, AUP-H6

## Application
Claimed category: gift_cards · country MX · domain age 700d · TLS ok

## LLM screening (advisory)
Category: gift_cards (confidence 0.98) · overall: prohibited · NPS proxy: 75

Verdicts with evidence:
- **AUP-01.6 → prohibited** — "We buy unwanted cards and resell them — that's the discount." Core business model is gift-card resale, a hard-override prohibited category regardless of other signals.
- **AUP-02.5 → restricted** — "Gaming and app-store cards — 10% off" Digital game-key/app-store card inventory would independently be restricted (velocity caps), but is subsumed by the AUP-01.6 override.
- **AUP-H1 → pass** — "Returns accepted within 30 days of delivery in original condition." Refund/return policy present and findable on policies.html.
- **AUP-H2 → pass** — "Orders ship within 1–2 business days via tracked carrier." Shipping policy states timeframes, though it describes carrier shipping while the product is instant email delivery.
- **AUP-H3 → pass** — "Email: support@giftcardhub-mx.example · Phone: (555) 010-9123" Email and phone both present on contact.html.
- **AUP-H4 → pass** — "By purchasing you agree to our terms of sale, privacy policy, and applicable consumer protection law of MX." Terms of service present on policies.html.
- **AUP-H5 → insufficient-info** No TLS/checkout security statement appears anywhere in the provided site text.
- **AUP-H6 → restricted** — "Tel +52 55 5601 0930." about.html gives a Mexico-format (+52) number while contact.html lists "(555) 010-9123", a US-style area code inconsistent with the claimed CDMX identity.

Review themes (verbatim, verified):
- [positive] "Code arrived instantly and worked, saved 8% on my groceries."
- [quality] "One card had zero balance, support replaced it after two days."
- [positive] "Been using monthly for a year, never a bad code."
- [positive] "Second bulk order, all codes valid."

## Scorecard breakdown
| factor | points | code | why |
|---|---|---|---|
| restricted_category | 25 | AUP-02 | category gift_cards is restricted-tier |
| geo_claim_inconsistency | 15 | AUP-H6 | claimed geography inconsistent |

**Hard overrides:** prohibited verdict (AUP-01.6)

## What would change this decision
Removal of the prohibited content/category, or (for reputational declines) a sustained reversal of the non-delivery/refund-refusal pattern over 90+ days on another processor, with evidence.
