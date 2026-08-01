# DEC-flashfone-repairs — FlashFone Repairs

**Decision: MANUAL_REVIEW** · score 60 · reason codes: AUP-05.II, AUP-H1, AUP-H2, AUP-H4, AUP-02

## Application
Claimed category: repair_services · country US · domain age 420d · TLS ok

## LLM screening (advisory)
Category: repair_services (confidence 0.95) · overall: restricted · NPS proxy: 73

Verdicts with evidence:
- **AUP-01 → pass** No content in weapons, tobacco, cannabis, adult, gambling, crypto, counterfeit, MLM, medical-cure, or credential-mill categories found on any page.
- **AUP-02.6 → restricted** — "Mail-in service: $25 deposit, quote before work" Deposit collected before work/quote is delivered fits AUP-02.6 deposit-and-disappear exposure for repair services.
- **AUP-H1 → insufficient-info** No refund/return policy text appears on index, about, or contact pages.
- **AUP-H2 → insufficient-info** — "Most repairs done same day in-store." In-store timeframe is stated, but no shipping/turnaround timeframe is given for the mail-in deposit service.
- **AUP-H3 → pass** — "Email: support@flashfone-repairs.example · Phone: (612) 555-0142 · 88 Lyndale Ave S" Email, phone, and street address are all present and consistent across about.html and contact.html.
- **AUP-H4 → insufficient-info** No terms-of-service text or link appears anywhere in the provided pages.
- **AUP-01.9 → pass** No medical/treatment/cure claims in the repair-service copy.

Review themes (verbatim, verified):
- [positive] "Screen fixed in two hours, looks brand new."
- [positive] "Honest quote, they even waived the deposit when I picked it up."
- [positive] "Fair price for the battery swap."
- [non_delivery] "Mail-in took two weeks and nobody answered the phone."

## Scorecard breakdown
| factor | points | code | why |
|---|---|---|---|
| missing_refund_policy | 20 | AUP-H1 | no refund/return policy found |
| missing_shipping_policy | 10 | AUP-H2 | no shipping policy found |
| missing_terms | 5 | AUP-H4 | no terms of service |
| restricted_category | 25 | AUP-02 | category repair_services is restricted-tier |

**Hard overrides:** insufficient-info verdict (AUP-05.II)
