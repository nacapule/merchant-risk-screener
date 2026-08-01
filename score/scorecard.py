"""Transparent, config-driven merchant scorecard.

Inputs: technical signals + content signals + LLM screening verdicts.
Output: decision ∈ {approve, conditional, manual_review, decline} + ordered
reason codes + a full score breakdown. Hard overrides (AUP-1 §5): any
`prohibited` verdict declines regardless of score; any `insufficient-info`
verdict forces manual review (fail-safe direction).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

RESTRICTED_CATEGORIES = {
    "event_tickets", "preorder", "luxury_goods", "supplements", "digital_goods",
    "repair_services", "dropship",
}


@dataclass
class ScoreResult:
    slug: str
    decision: str
    score: int
    reason_codes: list[str]
    breakdown: list[dict[str, Any]] = field(default_factory=list)
    overrides: list[str] = field(default_factory=list)
    conditions: list[str] = field(default_factory=list)


def _add(res: ScoreResult, w: dict, key: str, code: str, why: str) -> None:
    pts = int(w[key])
    res.score += pts
    res.reason_codes.append(code)
    res.breakdown.append({"factor": key, "points": pts, "code": code, "why": why})


def score_merchant(
    slug: str,
    cfg: dict,
    technical: dict[str, Any],
    content: dict[str, Any],
    screening: dict[str, Any],
) -> ScoreResult:
    """
    technical: from collect.technical.as_dict
    content:   {policy_pages: {refund_policy,shipping_policy,terms,contact: bool},
                has_phone, has_address, tls_ok override optional}
    screening: {category: str, category_confidence: float,
                verdicts: [{section, verdict, quote}],
                review_themes: {non_delivery, counterfeit, refund_refusal,
                               subscription_trap, positive: float shares},
                geo_claim_inconsistent: bool}
    """
    w = cfg["scorecard"]["weights"]
    bands = cfg["scorecard"]["bands"]
    res = ScoreResult(slug=slug, decision="approve", score=0, reason_codes=[])

    verdicts = screening.get("verdicts", [])
    v_levels = {v.get("verdict") for v in verdicts}

    # ---- hard overrides first
    if "prohibited" in v_levels:
        secs = sorted({str(v.get("section")) for v in verdicts if v.get("verdict") == "prohibited"})
        res.decision = "decline"
        res.overrides.append(f"prohibited verdict ({', '.join(secs)})")
        res.reason_codes.extend(secs)
    core_insufficient = any(
        v.get("verdict") == "insufficient-info"
        and str(v.get("section", "")).startswith(("AUP-01", "AUP-02"))
        for v in verdicts
    )
    if core_insufficient and res.decision != "decline":
        # category-level unassessable -> fail safe to a human (AUP-05.2)
        res.decision = "manual_review"
        res.overrides.append("insufficient-info on core category sections (AUP-05.II)")
        res.reason_codes.append("AUP-05.II")

    # ---- additive factors (always computed: the breakdown is the audit trail)
    age = technical.get("domain_age_days")
    if age is not None and age < 30:
        _add(res, w, "domain_age_under_30d", "AUP-02.7", f"domain {age}d old")
    elif age is not None and age < 180:
        _add(res, w, "domain_age_under_180d", "AUP-02.7", f"domain {age}d old")

    pp = content.get("policy_pages", {})
    if not pp.get("refund_policy"):
        _add(res, w, "missing_refund_policy", "AUP-H1", "no refund/return policy found")
    if not pp.get("shipping_policy"):
        _add(res, w, "missing_shipping_policy", "AUP-H2", "no shipping policy found")
    if not pp.get("contact") or not (content.get("has_phone") or content.get("has_address")):
        _add(res, w, "missing_contact", "AUP-H3", "no usable contact info")
    if not pp.get("terms"):
        _add(res, w, "missing_terms", "AUP-H4", "no terms of service")
    if technical.get("tls_ok") is False:
        _add(res, w, "no_tls", "AUP-H5", "TLS absent/broken")

    if screening.get("category") in RESTRICTED_CATEGORIES or "restricted" in v_levels:
        _add(res, w, "restricted_category", "AUP-02",
             f"category {screening.get('category')} is restricted-tier")

    themes = screening.get("review_themes", {}) or {}
    if float(themes.get("non_delivery", 0)) > 0.20:
        _add(res, w, "review_nondelivery_over_20pct", "AUP-04.ND",
             f"non-delivery theme share {themes['non_delivery']:.0%}")
    if float(themes.get("counterfeit", 0)) > 0:
        _add(res, w, "review_counterfeit_any", "AUP-04.CF",
             f"counterfeit theme share {themes['counterfeit']:.0%}")
    if float(themes.get("refund_refusal", 0)) > 0.15:
        _add(res, w, "review_refund_refusal_over_15pct", "AUP-04.RR",
             f"refund-refusal theme share {themes['refund_refusal']:.0%}")
    if float(themes.get("subscription_trap", 0)) > 0:
        _add(res, w, "review_subscription_trap", "AUP-04.ST", "subscription-trap theme present")
    if screening.get("geo_claim_inconsistent"):
        _add(res, w, "geo_claim_inconsistency", "AUP-H6", "claimed geography inconsistent")

    # ---- band decision (unless overridden)
    if not res.overrides:
        if res.score <= bands["approve_max"]:
            res.decision = "approve"
        elif res.score <= bands["conditional_max"]:
            res.decision = "conditional"
        elif res.score <= bands["manual_max"]:
            res.decision = "manual_review"
        else:
            res.decision = "decline"

    if res.decision == "conditional":
        res.conditions = [
            "transaction cap until 90-day performance review",
            "rolling reserve (suggested 10%) against future chargebacks",
        ]
    # dedupe reason codes, preserve order
    seen: set[str] = set()
    res.reason_codes = [c for c in res.reason_codes if not (c in seen or seen.add(c))]
    return res
