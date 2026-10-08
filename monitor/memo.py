"""Draft one advisory investigation memo per core alert episode, in replay order."""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from llm.client import complete_cached, load_config, resolve_model

REPO = Path(__file__).resolve().parent.parent


def draft(alert: dict, offline: bool) -> dict:
    cfg = load_config()["llm"]["tasks"]["monitor_memo"]
    template = (REPO / "screen" / "prompts" / f"{cfg['prompt_version']}.md").read_text()
    prompt = template.replace("{metrics_json}", json.dumps(alert, indent=1, sort_keys=True,
                                                         allow_nan=False))
    resp = complete_cached(prompt, task="monitor_memo", offline=offline)
    memo = resp.parsed_json()
    memo["_meta"] = {"model": resp.model, "cached": resp.cached}
    return memo


def draft_all(alerts: list[dict], offline: bool, jobs: int = 4) -> list[dict]:
    """Executor.map preserves episode order even when completions finish out of order."""
    if jobs < 1:
        raise ValueError("jobs must be at least 1")
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        return list(pool.map(lambda alert: draft(alert, offline), alerts))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()
    if args.jobs < 1:
        ap.error("--jobs must be at least 1")
    report = json.loads((REPO / "reports" / "monitoring_alerts.json").read_text())
    alerts, meta = report["alerts"], report["meta"]
    memos = draft_all(alerts, args.offline, args.jobs)
    lines = ["# Merchant monitoring memos (model-drafted, advisory)", "",
             f"Provenance: rule set {meta['rule_set']} · as_of {meta['as_of']} · "
             f"model {resolve_model('monitor_memo')}", ""]
    for alert, memo in zip(alerts, memos, strict=True):
        lines += [
            f"## Merchant {alert['merchant_id']} — alert episode {alert['date']}",
            f"Triggers: {'; '.join(alert['triggers'])}",
            f"**Recommended action: {memo.get('recommended_action')}**",
            "",
            memo.get("memo_markdown", ""),
            "",
            "Evidence gaps: " + "; ".join(memo.get("evidence_gaps", [])),
            "",
        ]
    out = REPO / "reports" / "monitoring_memos.md"
    out.write_text("\n".join(lines) + "\n")
    print(f"wrote {out} ({len(alerts)} memos)")


if __name__ == "__main__":
    main()
