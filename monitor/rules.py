"""Separate predicates from episode state so every rule uses the same daily facts."""

from __future__ import annotations

import pandas as pd

RULE_SETS = ("c0", "c1a", "c1b", "c1c", "c2", "c3")


def predicates(metrics: pd.DataFrame, cfg: dict, rule_set: str) -> pd.DataFrame:
    if rule_set not in RULE_SETS:
        raise ValueError(f"unknown monitor rule set: {rule_set}")
    m, g = cfg["monitor"], metrics
    p = pd.DataFrame(index=g.index)
    floor = g.disputes_30d.ge(m["min_disputes"])
    p["B"] = g.cb_rate_30d.ge(m["chargeback_breach"]) & floor
    p["W"] = g.cb_rate_30d.ge(m["chargeback_warn"]) & floor & ~p.B
    p["V"] = g.volume_z.ge(m["volume_zscore_alert"])
    p["T"] = g.ticket_drift.ge(m["ticket_drift_alert"])
    p["S"] = g.new_gmv_share.ge(m["new_account_gmv_share_alert"])
    p["Y"] = False
    if rule_set in m["young_variants"] or rule_set == "c3":
        variant = m["c3_young"] if rule_set == "c3" else rule_set
        young = m["young_variants"][variant]
        p["Y"] = (g.merchant_age_days.lt(young["age_days"])
                  & g.new_gmv_share.ge(young["gmv_share"]))
    p["F"] = False
    if rule_set in ("c2", "c3"):
        p["F"] = (g.base_refund_rate.ge(m["refund_base_min"])
                  & g.refund_rate_30d.le(m["refund_recent_max"]) & floor)
    control = p.B | p[["W", "B", "V", "T", "S"]].sum(axis=1).ge(m["min_triggers"])
    p["core"] = g.eligible & (control | p.Y | p.F)
    p["D"] = g.disputes_30d.ge(m["dispute_flag_min"])
    return p.fillna(False).astype(bool)


def describe(metrics: dict, codes: list[str], cfg: dict, rule_set: str) -> list[str]:
    """Include denominators so a rate alert can be assessed without guessing volume."""
    g, m = metrics, cfg["monitor"]
    strings = []
    for code in codes:
        if code in ("W", "B"):
            level = "breach" if code == "B" else "warn"
            strings.append(f"AUP-06.1 {level}: 30d chargeback rate {g['cb_rate_30d']:.1%} "
                           f"({g['disputes_30d']} disputes / {g['orders_30d']} orders)")
        elif code == "V":
            strings.append(f"AUP-06.2: volume z={g['volume_z']:.1f} vs baseline")
        elif code == "T":
            strings.append(f"AUP-06.3: avg ticket {g['ticket_drift']:.1f}x baseline")
        elif code == "S":
            strings.append(f"AUP-06.4: new-account GMV share {g['new_gmv_share']:.0%}")
        elif code == "Y":
            variant = m["c3_young"] if rule_set == "c3" else rule_set
            young = m["young_variants"][variant]
            strings.append(f"Young merchant concentration: age {g['merchant_age_days']} days "
                           f"(< {young['age_days']}), new-account GMV share "
                           f"{g['new_gmv_share']:.0%} (>= {young['gmv_share']:.0%})")
        elif code == "F":
            strings.append(f"AUP-06.5: refund rate collapsed to {g['refund_rate_30d']:.1%} "
                           f"from {g['base_refund_rate']:.1%}; "
                           f"{g['disputes_30d']} disputes in 30d")
        elif code == "D":
            strings.append(f"Dispute-count surveillance: {g['disputes_30d']} disputes in 30d "
                           f"({g['orders_30d']} orders)")
    return strings
