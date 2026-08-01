# DEC-greenleaf-wellness — GreenLeaf Wellness

**Decision: DECLINE** · score 25 · reason codes: AUP-01.3, AUP-01.9, AUP-02.4, AUP-02

## Application
Claimed category: wellness · country US · domain age 460d · TLS ok

## LLM screening (advisory)
Category: wellness (confidence 0.85) · overall: prohibited · NPS proxy: 94

Verdicts with evidence:
- **AUP-01.3 → prohibited** — "Full-spectrum CBD tincture 1000mg — $64" Merchant sells CBD tincture, gummies, and balm — hard-override prohibited category regardless of hygiene or local legality.
- **AUP-01.9 → prohibited** — "Customers tell us our tincture cured their insomnia — read the reviews." "Cured" is disease-treatment language (explicitly the failing case per AUP-02.4's supports/treats-cures line), a second independent hard override.
- **AUP-02.4 → prohibited** — "Hemp-derived, under 0.3% THC." Claim review resolves against the merchant: the 'cured' language pushes this past borderline structure/function claims into AUP-01.9 territory, so restricted status does not apply.
- **AUP-H1 → pass** — "Returns accepted within 30 days of delivery in original condition." Refund/return policy present and findable.
- **AUP-H2 → pass** — "Orders ship within 1–2 business days via tracked carrier." Shipping policy states timeframes.
- **AUP-H3 → pass** — "Contact: care@greenleaf.example, (720) 555-0163, 1310 Pearl St." Email, phone, and address all present.
- **AUP-H4 → pass** — "By purchasing you agree to our terms of sale, privacy policy, and applicable consumer protection law of US." Terms of service present.
- **AUP-H5 → insufficient-info** No text asserts TLS/HTTPS on checkout or site generally; cannot be assessed from provided evidence.
- **AUP-H6 → restricted** — "Contact Email: support@greenleaf-wellness.example · Phone: (555) 010-7499" Contact details conflict with the about page's "Contact: care@greenleaf.example, (720) 555-0163" — different email domain and phone number for the same merchant, an identity-consistency gap.

Review themes (verbatim, verified):
- [positive] "The tincture cured my insomnia, I sleep through the night now."
- [positive] "Gummies are gentle and the COA link is right on the page."
- [positive] "Balm helps my knees after runs."
- [quality] "Subtle effect, might need a stronger dose."

## Scorecard breakdown
| factor | points | code | why |
|---|---|---|---|
| restricted_category | 25 | AUP-02 | category wellness is restricted-tier |

**Hard overrides:** prohibited verdict (AUP-01.3, AUP-01.9, AUP-02.4)

## What would change this decision
Removal of the prohibited content/category, or (for reputational declines) a sustained reversal of the non-delivery/refund-refusal pattern over 90+ days on another processor, with evidence.
