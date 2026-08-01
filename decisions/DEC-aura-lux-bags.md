# DEC-aura-lux-bags — Aura Lux Bags

**Decision: DECLINE** · score 65 · reason codes: AUP-01.7, AUP-02.3, AUP-02, AUP-04.CF

## Application
Claimed category: fashion_accessories · country US · domain age 380d · TLS ok

## LLM screening (advisory)
Category: luxury_goods (confidence 0.95) · overall: prohibited · NPS proxy: 44

Verdicts with evidence:
- **AUP-01.7 → prohibited** — "Logos and packaging are indistinguishable from boutique originals." Site explicitly markets counterfeit/replica goods, not merely inspired-by designs.
- **AUP-01.7 → prohibited** — "LV-style monogram tote, 1:1 mirror quality — $129" "1:1 mirror quality" is standard replica-market terminology for a counterfeit matching the original.
- **AUP-01.7 → prohibited** — "Birkin-style 30cm, same hardware as the original — $189" Explicit claim of matching a specific trademarked luxury product's hardware, i.e. a knockoff.
- **AUP-02.3 → prohibited** — "Direct-from-factory luxury-style accessories." Would otherwise be restricted high-ticket luxury goods, but AUP-01.7 counterfeit evidence overrides to a hard decline.
- **AUP-H1 → pass** — "Returns accepted within 30 days of delivery in original condition. Refunds are issued to the original payment method within 5–7 business days of receiving the return." Refund/return policy present and findable.
- **AUP-H2 → pass** — "Orders ship within 1–2 business days via tracked carrier. Standard delivery 3–5 days." Shipping policy with stated timeframes present.
- **AUP-H3 → pass** — "Email: support@aura-lux-bags.example · Phone: (555) 010-7606" Email and phone contact both present.
- **AUP-H4 → pass** — "By purchasing you agree to our terms of sale, privacy policy, and applicable consumer protection law of US." Terms of service present.
- **AUP-H5 → insufficient-info** No checkout page or TLS-related text provided in the site evidence to assess.
- **AUP-H6 → pass** — "Aura Lux Bags — about" Business name "Aura Lux Bags" used consistently across index, about, policies, and contact pages.

Review themes (verbatim, verified):
- [counterfeit] "Customs seized my order as counterfeit and I got nothing back."
- [quality] "The logo peeled off the tote after two weeks."
- [counterfeit] "Looks just like the real one, my friends can't tell the difference."
- [quality] "Ordered the Birkin-style, quality is insane for 189."

## Scorecard breakdown
| factor | points | code | why |
|---|---|---|---|
| restricted_category | 25 | AUP-02 | category luxury_goods is restricted-tier |
| review_counterfeit_any | 40 | AUP-04.CF | counterfeit theme share 58% |

**Hard overrides:** prohibited verdict (AUP-01.7, AUP-02.3)

## What would change this decision
Removal of the prohibited content/category, or (for reputational declines) a sustained reversal of the non-delivery/refund-refusal pattern over 90+ days on another processor, with evidence.
