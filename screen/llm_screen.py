"""Three structured Claude calls per merchant application: categorize, policy
screen (verdicts with verbatim quotes), review-theme extraction.

Quote discipline is mechanical: every quote the model returns is string-checked
against its source text (``verify_quotes``); an unverifiable quote invalidates
the verdict it supports (AUP-05.1). Model per task from config ``llm.tasks``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from llm.client import complete_cached, load_config

REPO = Path(__file__).resolve().parent.parent
PROMPTS = Path(__file__).resolve().parent / "prompts"


def _render(task: str, mapping: dict[str, str], prompt_version: str | None = None) -> str:
    cfg = load_config()["llm"]["tasks"][task]
    version = prompt_version or cfg["prompt_version"]
    text = (PROMPTS / f"{version}.md").read_text()
    for k, v in mapping.items():
        text = text.replace("{" + k + "}", v)
    return text


def _norm(s: str) -> str:
    return " ".join(s.split()).lower()


def verify_quotes(quotes: list[str], source: str) -> dict[str, Any]:
    """Whitespace-normalized substring check: quote must appear in source."""
    src = _norm(source)
    missing = [q for q in quotes if q and _norm(q) not in src]
    return {"n_quotes": len(quotes), "n_unverifiable": len(missing), "missing": missing}


def categorize(slug: str, site_text: str, *, model: str | None = None,
               offline: bool = False) -> dict[str, Any]:
    prompt = _render("merchant_categorize", {"site_text": site_text[:24000]})
    resp = complete_cached(prompt, task="merchant_categorize", model=model, offline=offline)
    out = resp.parsed_json()
    out["_verify"] = verify_quotes([out.get("evidence_quote", "")], site_text)
    out["_meta"] = {"model": resp.model, "cached": resp.cached, "cost_usd": resp.cost_usd}
    return out


def policy_screen(slug: str, site_text: str, *, model: str | None = None,
                  prompt_version: str | None = None, offline: bool = False) -> dict[str, Any]:
    # The policy as screened and cached; later AUP-06 changes are out of screening scope.
    policy_text = (PROMPTS / "acceptable-use_2026-08.md").read_text()
    prompt = _render(
        "policy_screen",
        {"policy_text": policy_text, "site_text": site_text[:24000]},
        prompt_version,
    )
    resp = complete_cached(prompt, task="policy_screen", model=model, offline=offline)
    out = resp.parsed_json()
    quotes = [v.get("quote", "") for v in out.get("verdicts", [])
              if v.get("verdict") in ("restricted", "prohibited")]
    ver = verify_quotes(quotes, site_text)
    # AUP-05.1: an unverifiable quote voids its verdict
    if ver["missing"]:
        kept = []
        for v in out.get("verdicts", []):
            flagged = v.get("verdict") in ("restricted", "prohibited")
            if flagged and v.get("quote") in ver["missing"]:
                v = {**v, "verdict": "insufficient-info",
                     "note": "quote failed verbatim verification; verdict voided (AUP-05.1)"}
            kept.append(v)
        out["verdicts"] = kept
    out["_verify"] = ver
    out["_meta"] = {"model": resp.model, "cached": resp.cached, "cost_usd": resp.cost_usd}
    return out


def review_themes(slug: str, reviews: list[dict], *, model: str | None = None,
                  offline: bool = False) -> dict[str, Any]:
    if not reviews:
        return {
            "theme_shares": {k: 0.0 for k in
                             ("non_delivery", "counterfeit", "refund_refusal", "quality",
                              "subscription_trap", "positive")},
            "recent_half_shares": {},
            "representative_quotes": [],
            "nps_proxy": 0,
            "summary": "no review data",
            "_verify": {"n_quotes": 0, "n_unverifiable": 0, "missing": []},
            "_meta": {"model": None, "cached": True, "cost_usd": 0.0},
        }
    csv_text = "\n".join(f"{r['date']},{r['rating']},{r['text']}" for r in reviews)
    prompt = _render("review_themes", {"reviews_csv": csv_text[:32000]})
    resp = complete_cached(prompt, task="review_themes", model=model, offline=offline)
    out = resp.parsed_json()
    source = " ".join(r["text"] for r in reviews)
    out["_verify"] = verify_quotes(
        [q.get("quote", "") for q in out.get("representative_quotes", [])], source
    )
    out["_meta"] = {"model": resp.model, "cached": resp.cached, "cost_usd": resp.cost_usd}
    return out


def screen_merchant(slug: str, site_text: str, reviews: list[dict], *,
                    offline: bool = False) -> dict[str, Any]:
    cat = categorize(slug, site_text, offline=offline)
    pol = policy_screen(slug, site_text, offline=offline)
    themes = review_themes(slug, reviews, offline=offline)
    return {
        "category": cat.get("category"),
        "category_confidence": cat.get("confidence"),
        "mcc_guess": cat.get("mcc_guess"),
        "verdicts": pol.get("verdicts", []),
        "overall": pol.get("overall"),
        "geo_claim_inconsistent": bool(pol.get("geo_claim_inconsistent")),
        "policy_summary": pol.get("summary"),
        "review_themes": themes.get("theme_shares", {}),
        "review_recent_half": themes.get("recent_half_shares", {}),
        "review_quotes": themes.get("representative_quotes", []),
        "nps_proxy": themes.get("nps_proxy"),
        "quote_verification": {
            "categorize": cat.get("_verify"),
            "policy": pol.get("_verify"),
            "reviews": themes.get("_verify"),
        },
        "_meta": [cat.get("_meta"), pol.get("_meta"), themes.get("_meta")],
    }


if __name__ == "__main__":  # pragma: no cover
    import sys

    from collect.content import collect_content, load_reviews

    slug = sys.argv[1]
    sc = collect_content(slug)
    print(json.dumps(screen_merchant(slug, sc.full_text, load_reviews(slug)), indent=1))
