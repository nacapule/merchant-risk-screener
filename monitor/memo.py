"""Claude merchant-investigation memos for monitoring alerts.

Run: python -m monitor.memo [--offline]
Reads reports/monitoring_alerts.json (from monitor.watch) plus the metric
context, drafts one memo per alerted merchant via the configured model
(config llm.tasks.monitor_memo), writes reports/monitoring_memos.md.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from llm.client import complete_cached, load_config

REPO = Path(__file__).resolve().parent.parent


def draft(alert: dict, offline: bool) -> dict:
    cfg = load_config()["llm"]["tasks"]["monitor_memo"]
    template = (REPO / "screen" / "prompts" / f"{cfg['prompt_version']}.md").read_text()
    prompt = template.replace("{metrics_json}", json.dumps(alert, indent=1, sort_keys=True))
    resp = complete_cached(prompt, task="monitor_memo", offline=offline)
    memo = resp.parsed_json()
    memo["_meta"] = {"model": resp.model, "cached": resp.cached}
    return memo


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    alerts = json.loads((REPO / "reports" / "monitoring_alerts.json").read_text())
    lines = ["# Merchant monitoring memos (Claude-drafted, advisory)\n"]
    for a in alerts:
        memo = draft(a, args.offline)
        lines += [
            f"## Merchant {a['merchant_id']} — first alerting day {a['date']}",
            f"Triggers: {'; '.join(a['triggers'])}",
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
