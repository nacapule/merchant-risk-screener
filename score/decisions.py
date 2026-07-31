"""Run the full pipeline over the fixture manifest and write decision records.

Run: python -m score.decisions [--offline]

Per merchant: collect signals → LLM screening (cached) → scorecard → decision +
DEC-<slug>.md record. Ends with an accuracy table vs the manifest's expected
decisions (the fixture set doubles as the screener's ground truth).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

from collect.content import collect_content, load_reviews
from collect.technical import as_dict, collect_technical
from score.scorecard import score_merchant
from screen.llm_screen import screen_merchant

REPO = Path(__file__).resolve().parent.parent


def decide_one(entry: dict, cfg: dict, offline: bool) -> dict:
    slug = entry["slug"]
    tech = as_dict(collect_technical(slug))
    content = collect_content(slug)
    screening = screen_merchant(slug, content.full_text, load_reviews(slug), offline=offline)
    result = score_merchant(
        slug, cfg, tech,
        {"policy_pages": content.policy_pages, "has_phone": content.has_phone,
         "has_address": content.has_address, "tls_ok": tech.get("tls_ok")},
        screening,
    )
    record = {
        "slug": slug, "name": entry["name"], "claimed_category": entry["claimed_category"],
        "expected_decision": entry["expected_decision"], "decision": result.decision,
        "score": result.score, "reason_codes": result.reason_codes,
        "overrides": result.overrides, "conditions": result.conditions,
        "category_llm": screening.get("category"), "nps_proxy": screening.get("nps_proxy"),
        "quote_verification": screening.get("quote_verification"),
    }
    _write_record(entry, tech, screening, result)
    return record


def _write_record(entry: dict, tech: dict, screening: dict, result) -> None:
    slug = entry["slug"]
    lines = [
        f"# DEC-{slug} — {entry['name']}",
        "",
        f"**Decision: {result.decision.upper()}** · score {result.score} · reason codes: "
        + (", ".join(result.reason_codes) or "none"),
        "",
        "## Application",
        f"Claimed category: {entry['claimed_category']} · country {entry.get('country', '?')} · "
        f"domain age {tech.get('domain_age_days')}d · "
        f"TLS {'ok' if tech.get('tls_ok') else 'MISSING'}",
        "",
        "## LLM screening (advisory)",
        f"Category: {screening.get('category')} (confidence "
        f"{screening.get('category_confidence')}) · overall: {screening.get('overall')} · "
        f"NPS proxy: {screening.get('nps_proxy')}",
        "",
        "Verdicts with evidence:",
    ]
    for v in screening.get("verdicts", []):
        q = f' — "{v.get("quote")}"' if v.get("quote") else ""
        lines.append(f"- **{v.get('section')} → {v.get('verdict')}**{q} {v.get('note', '')}")
    if screening.get("review_quotes"):
        lines += ["", "Review themes (verbatim, verified):"]
        for q in screening["review_quotes"][:4]:
            lines.append(f"- [{q.get('theme')}] \"{q.get('quote')}\"")
    lines += ["", "## Scorecard breakdown", "| factor | points | code | why |", "|---|---|---|---|"]
    for b in result.breakdown:
        lines.append(f"| {b['factor']} | {b['points']} | {b['code']} | {b['why']} |")
    if result.overrides:
        lines += ["", "**Hard overrides:** " + "; ".join(result.overrides)]
    if result.conditions:
        lines += ["", "**Conditions:** " + "; ".join(result.conditions)]
    if result.decision == "decline":
        lines += ["", "## What would change this decision",
                  "Removal of the prohibited content/category, or (for reputational "
                  "declines) a sustained reversal of the non-delivery/refund-refusal "
                  "pattern over 90+ days on another processor, with evidence."]
    (REPO / "decisions").mkdir(exist_ok=True)
    (REPO / "decisions" / f"DEC-{slug}.md").write_text("\n".join(lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    cfg = yaml.safe_load(open(REPO / "config.yaml"))
    manifest = yaml.safe_load(open(REPO / "fixtures" / "manifest.yaml"))["merchants"]

    records = [decide_one(e, cfg, args.offline) for e in manifest]
    n = len(records)
    exact = sum(r["decision"] == r["expected_decision"] for r in records)
    prohibited_slugs = [r for r in records
                        if any(c.startswith("AUP-01") for c in r["reason_codes"])
                        or r["expected_decision"] == "decline"]
    exp_declines = [r for r in records if r["expected_decision"] == "decline"]
    caught_declines = sum(r["decision"] == "decline" for r in exp_declines)

    summary = {
        "n_merchants": n,
        "decision_accuracy": round(exact / n, 3),
        "expected_declines": len(exp_declines),
        "declines_caught": caught_declines,
        "decline_recall": round(caught_declines / len(exp_declines), 3) if exp_declines else None,
        "records": records,
    }
    (REPO / "reports").mkdir(exist_ok=True)
    (REPO / "reports" / "decisions_summary.json").write_text(json.dumps(summary, indent=1))
    print(f"{exact}/{n} exact decisions; decline recall "
          f"{caught_declines}/{len(exp_declines)}")
    for r in records:
        flag = "✓" if r["decision"] == r["expected_decision"] else "✗"
        print(f" {flag} {r['slug']:24s} expected {r['expected_decision']:14s} "
              f"got {r['decision']:14s} score {r['score']}")
    _ = prohibited_slugs


if __name__ == "__main__":
    main()
