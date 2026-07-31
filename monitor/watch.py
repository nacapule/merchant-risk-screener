"""Portfolio monitoring: roll up daily merchant metrics (metrics.sql against
the companion workbench DB, or a CSV export), apply AUP-06 thresholds, and emit
merchant alerts. Thresholds are modeled on publicly known card-network
monitoring-program *concepts*; values are illustrative (config `monitor`).

Run: python -m monitor.watch [--csv path]   (CSV: metrics.sql column layout)
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

REPO = Path(__file__).resolve().parent.parent


def load_metrics(csv: str | None) -> pd.DataFrame:
    if csv:
        return pd.read_csv(csv, parse_dates=["d"])
    import sqlalchemy as sa

    url = "mysql+pymysql://fraud:fraudpw@127.0.0.1:3306/bnpl"
    sql = (REPO / "monitor" / "metrics.sql").read_text()
    with sa.create_engine(url).connect() as c:
        return pd.read_sql(sa.text(sql), c, parse_dates=["d"])


def evaluate(df: pd.DataFrame, cfg: dict) -> list[dict]:
    m = cfg["monitor"]
    alerts: list[dict] = []
    for mid, g in df.groupby("merchant_id"):
        g = g.sort_values("d").set_index("d")
        if len(g) < 14 or g.n_orders.sum() < 30:
            continue
        # trailing 30d aggregates vs merchant baseline (first 60 observed days).
        # cb rate = disputes OPENED in the window / orders in the window — the
        # honest, lagging version (metrics.sql attributes by opened date).
        roll_cb = g.n_cbs_opened.rolling("30D").sum() / g.n_orders.rolling("30D").sum()
        roll_vol = g.n_orders.rolling("30D").sum()
        roll_ticket = (g.avg_ticket * g.n_orders).rolling("30D").sum() / g.n_orders.rolling(
            "30D"
        ).sum()
        roll_new = (g.new_buyer_share * g.n_orders).rolling("30D").sum() / g.n_orders.rolling(
            "30D"
        ).sum()
        base = g.iloc[: min(60, len(g) // 2)]
        base_vol_mean = base.n_orders.mean() * 30
        base_vol_std = max(base.n_orders.std() * np.sqrt(30), 1.0)
        base_ticket = max(base.avg_ticket.mean(), 1.0)

        latest = g.index.max()
        window = g.index >= latest - pd.Timedelta(days=60)
        for d in g.index[window]:
            cb = float(roll_cb.get(d, 0) or 0)
            vol_z = float((roll_vol.get(d, 0) - base_vol_mean) / base_vol_std)
            drift = float(roll_ticket.get(d, base_ticket) / base_ticket)
            new_share = float(roll_new.get(d, 0) or 0)
            triggers = []
            if cb >= m["chargeback_breach"]:
                triggers.append(f"AUP-06.1 breach: 30d chargeback rate {cb:.1%}")
            elif cb >= m["chargeback_warn"]:
                triggers.append(f"AUP-06.1 warn: 30d chargeback rate {cb:.1%}")
            if vol_z >= m["volume_zscore_alert"]:
                triggers.append(f"AUP-06.2: volume z={vol_z:.1f} vs baseline")
            if drift >= m["ticket_drift_alert"]:
                triggers.append(f"AUP-06.3: avg ticket {drift:.1f}x baseline")
            if new_share >= m["new_account_gmv_share_alert"]:
                triggers.append(f"AUP-06.4: new-account share {new_share:.0%}")
            if len(triggers) >= 2 or any("breach" in t for t in triggers):
                alerts.append(
                    {"merchant_id": int(mid), "date": str(d.date()), "triggers": triggers,
                     "cb_rate_30d": round(cb, 4), "volume_z": round(vol_z, 1),
                     "ticket_drift": round(drift, 2), "new_share": round(new_share, 3)}
                )
                break  # first alerting day per merchant is the story
    return alerts


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=None)
    args = ap.parse_args()
    cfg = yaml.safe_load(open(REPO / "config.yaml"))
    df = load_metrics(args.csv)
    alerts = evaluate(df, cfg)
    (REPO / "reports").mkdir(exist_ok=True)
    out = REPO / "reports" / "monitoring_alerts.json"
    out.write_text(json.dumps(alerts, indent=1))
    print(f"{len(alerts)} merchant alerts -> {out}")
    for a in alerts:
        print(f"  merchant {a['merchant_id']} on {a['date']}: " + "; ".join(a["triggers"]))


if __name__ == "__main__":
    main()
