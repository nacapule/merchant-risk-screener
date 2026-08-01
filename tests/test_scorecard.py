from __future__ import annotations

from pathlib import Path

import yaml

from score.scorecard import score_merchant

CFG = yaml.safe_load(open(Path(__file__).resolve().parent.parent / "config.yaml"))

CLEAN_TECH = {"domain_age_days": 900, "tls_ok": True}
CLEAN_CONTENT = {
    "policy_pages": {"refund_policy": True, "shipping_policy": True, "terms": True,
                     "contact": True},
    "has_phone": True, "has_address": True,
}
CLEAN_SCREEN = {"category": "apparel", "verdicts": [{"section": "AUP-01", "verdict": "pass"}],
                "review_themes": {"non_delivery": 0.02, "counterfeit": 0.0,
                                  "refund_refusal": 0.03, "positive": 0.9}}


def test_clean_merchant_approves() -> None:
    r = score_merchant("clean", CFG, CLEAN_TECH, CLEAN_CONTENT, CLEAN_SCREEN)
    assert r.decision == "approve" and r.score <= 25


def test_prohibited_overrides_perfect_hygiene() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["verdicts"] = [{"section": "AUP-01.6", "verdict": "prohibited",
                           "quote": "discounted gift cards"}]
    r = score_merchant("giftcards", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert r.decision == "decline"
    assert "AUP-01.6" in r.reason_codes
    assert r.overrides


def test_core_insufficient_info_forces_manual() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["verdicts"] = [{"section": "AUP-01", "verdict": "insufficient-info"}]
    r = score_merchant("thin", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert r.decision == "manual_review"
    assert "AUP-05.II" in r.reason_codes


def test_noncore_insufficient_info_does_not_override() -> None:
    # v1->v2 lesson: a hygiene-section insufficient-info must not hijack an
    # otherwise-clean merchant into manual review
    screen = dict(CLEAN_SCREEN)
    screen["verdicts"] = [{"section": "AUP-03", "verdict": "insufficient-info"},
                          {"section": "AUP-01", "verdict": "pass"}]
    r = score_merchant("cleanish", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert r.decision == "approve"


def test_reputational_decline_despite_good_pages() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["review_themes"] = {"non_delivery": 0.55, "counterfeit": 0.0,
                               "refund_refusal": 0.20, "positive": 0.2}
    tech = dict(CLEAN_TECH, domain_age_days=150)
    r = score_merchant("badrep", CFG, tech, CLEAN_CONTENT, screen)
    # 55 (ND severe) + 20 (RR) + 15 (age<180) = 90 -> decline band (>= 85)
    assert r.decision == "decline" and r.score == 90


def test_mid_nondelivery_stays_subdecline() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["review_themes"] = {"non_delivery": 0.30, "counterfeit": 0.0,
                               "refund_refusal": 0.20, "positive": 0.4}
    r = score_merchant("midrep", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    # 20 (ND mid) + 20 (RR) = 40 -> conditional, not a reputational decline
    assert r.decision == "conditional" and r.score == 40


def test_restricted_category_floor_never_plain_approves() -> None:
    screen = dict(CLEAN_SCREEN, category="event_tickets")
    r = score_merchant("tickets", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert r.score == 25 and r.decision == "conditional" and r.conditions


def test_single_ambiguous_counterfeit_mention_needs_corroboration() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["review_themes"] = {"non_delivery": 0.0, "counterfeit": 0.05,
                               "refund_refusal": 0.0, "positive": 0.9}
    r = score_merchant("onemention", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert "AUP-04.CF" not in r.reason_codes


def test_band_edges() -> None:
    screen = dict(CLEAN_SCREEN)
    content = {"policy_pages": {"refund_policy": False, "shipping_policy": True,
                                "terms": True, "contact": True},
               "has_phone": True, "has_address": True}
    r = score_merchant("edge", CFG, CLEAN_TECH, content, screen)
    # missing refund policy alone = 20 -> approve band (<=25), with the code recorded
    assert r.score == 20 and r.decision == "approve" and "AUP-H1" in r.reason_codes


def test_conditional_gets_conditions() -> None:
    screen = dict(CLEAN_SCREEN, category="digital_goods")
    tech = dict(CLEAN_TECH, domain_age_days=100)
    r = score_merchant("cond", CFG, tech, CLEAN_CONTENT, screen)
    # 25 (restricted) + 15 (age) = 40 -> conditional, with reserve conditions
    assert r.decision == "conditional" and r.conditions


def test_breakdown_is_complete_audit_trail() -> None:
    screen = dict(CLEAN_SCREEN)
    screen["review_themes"] = {"non_delivery": 0.25, "counterfeit": 0.1,
                               "refund_refusal": 0.0, "positive": 0.5}
    r = score_merchant("audit", CFG, CLEAN_TECH, CLEAN_CONTENT, screen)
    assert sum(b["points"] for b in r.breakdown) == r.score
    assert all(b["why"] for b in r.breakdown)
