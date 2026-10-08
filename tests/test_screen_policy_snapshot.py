"""The screening snapshot must keep every cached screening prompt reproducible."""

from __future__ import annotations

import yaml

from collect.content import collect_content
from llm.client import CACHE_DIR, cache_key, resolve_model
from screen.llm_screen import PROMPTS, REPO, _render

SNAPSHOT = PROMPTS / "acceptable-use_2026-08.md"
# Cached before commit 1e65782 changed this fixture's site; history, not reproducible.
STALE = {("titan-supps", "screen_v1")}


def _sections_before_monitoring(text: str) -> str:
    return text.split("## AUP-06")[0]


def test_cached_screening_prompts_render_from_snapshot() -> None:
    policy = SNAPSHOT.read_text()
    model = resolve_model("policy_screen")
    merchants = yaml.safe_load((REPO / "fixtures" / "manifest.yaml").read_text())["merchants"]
    misses = set()
    for entry in merchants:
        site_text = collect_content(entry["slug"]).full_text
        for version in ("screen_v1", "screen_v2"):
            prompt = _render("policy_screen",
                             {"policy_text": policy, "site_text": site_text[:24000]}, version)
            if not (CACHE_DIR / f"{cache_key(model, prompt)}.json").exists():
                misses.add((entry["slug"], version))
    assert len(merchants) == 16
    assert misses == STALE


def test_screened_sections_match_live_policy() -> None:
    live = (REPO / "policy" / "acceptable-use.md").read_text()
    assert _sections_before_monitoring(SNAPSHOT.read_text()) == _sections_before_monitoring(live)
