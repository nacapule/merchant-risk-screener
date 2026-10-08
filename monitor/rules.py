"""Separate predicates from episode state so every rule uses the same daily facts."""

from __future__ import annotations

import pandas as pd

from monitor.rollup import REASONS

RULE_SETS = ("c0", "c1a", "c1b", "c1c", "c2", "c3")
# Iteration 2 (monitor/ITERATION.md §4): chargeback evidence over all disputes or only
# fulfilment-related ones, the young-merchant rule Y, and delivery confirmation X.
ITERATION2_SETS = {
    "k1": {"evidence": "all", "young": False, "delivery": False},
    "k2": {"evidence": "fulfilment", "young": False, "delivery": False},
    "x": {"evidence": None, "young": False, "delivery": True},
    "s1": {"evidence": "all", "young": True, "delivery": True},
    "s2": {"evidence": "fulfilment", "young": True, "delivery": True},
    "s3": {"evidence": "all", "young": True, "delivery": False},
    "s4": {"evidence": "fulfilment", "young": True, "delivery": False},
}
ALL_SETS = (*RULE_SETS, *ITERATION2_SETS)
# Iteration-1 sets keep their published record shape, so their alerts and memos replay.
ITERATION2_FIELDS = (
    *REASONS, *[f"{col.removeprefix('n_')}_30d" for col in REASONS], "disputes_fulfilment_30d",
    "cb_breach_p", "cb_warn_p", "cb_fulfilment_breach_p", "cb_fulfilment_warn_p",
    "ship_cohort_n", "ship_cohort_unconfirmed", "delivery_deadline_days", "delivery_p_ref",
    "delivery_p",
)


def needs_delivery(rule_set: str) -> bool:
    return ITERATION2_SETS.get(rule_set, {}).get("delivery", False)


def predicates(metrics: pd.DataFrame, cfg: dict, rule_set: str) -> pd.DataFrame:
    if rule_set not in ALL_SETS:
        raise ValueError(f"unknown monitor rule set: {rule_set}")
    m, g = cfg["monitor"], metrics
    spec = ITERATION2_SETS.get(rule_set)
    p = pd.DataFrame(index=g.index)
    if spec is None:
        floor = g.disputes_30d.ge(m["min_disputes"])
        p["B"] = g.cb_rate_30d.ge(m["chargeback_breach"]) & floor
        p["W"] = g.cb_rate_30d.ge(m["chargeback_warn"]) & floor & ~p.B
    elif spec["evidence"] is None:
        p["B"] = p["W"] = False
    else:
        prefix, count = (("cb", "disputes_30d") if spec["evidence"] == "all"
                         else ("cb_fulfilment", "disputes_fulfilment_30d"))
        floor = g[count].ge(m["min_disputes"])
        alpha = m["chargeback_evidence_max_p"]
        p["B"] = g[f"{prefix}_breach_p"].le(alpha) & floor
        p["W"] = g[f"{prefix}_warn_p"].le(alpha) & floor & ~p.B
    p["V"] = g.volume_z.ge(m["volume_zscore_alert"])
    p["T"] = g.ticket_drift.ge(m["ticket_drift_alert"])
    p["S"] = g.new_gmv_share.ge(m["new_account_gmv_share_alert"])
    p["Y"] = False
    variant = (m["iteration2_young"] if spec is not None
               else m["c3_young"] if rule_set == "c3" else rule_set)
    if (spec is not None and spec["young"]) or rule_set in m["young_variants"] \
            or rule_set == "c3":
        young = m["young_variants"][variant]
        p["Y"] = (g.merchant_age_days.lt(young["age_days"])
                  & g.new_gmv_share.ge(young["gmv_share"]))
    p["F"] = False
    if rule_set in ("c2", "c3"):
        p["F"] = (g.base_refund_rate.ge(m["refund_base_min"])
                  & g.refund_rate_30d.le(m["refund_recent_max"]) & floor)
    p["X"] = False
    if spec is not None and spec["delivery"]:
        if "delivery_p" not in g:
            raise ValueError(f"rule set {rule_set} needs shipments and a delivery calibration")
        d = m["delivery"]
        p["X"] = g.ship_cohort_unconfirmed.ge(d["min_unconfirmed"]) & g.delivery_p.le(d["max_p"])
    p["control"] = False
    if spec is None or spec["evidence"] is not None:
        p["control"] = p.B | p[["W", "B", "V", "T", "S"]].sum(axis=1).ge(m["min_triggers"])
    p["core"] = g.eligible & (p.control | p.Y | p.F | p.X)
    p["D"] = g.disputes_30d.ge(m["dispute_flag_min"])
    return p.fillna(False).astype(bool)


def _chargeback(g: dict, code: str, cfg: dict, rule_set: str) -> str:
    m = cfg["monitor"]
    level = "breach" if code == "B" else "warn"
    spec = ITERATION2_SETS.get(rule_set)
    if spec is None:
        return (f"AUP-06.1 {level}: 30d chargeback rate {g['cb_rate_30d']:.1%} "
                f"({g['disputes_30d']} disputes / {g['orders_30d']} orders)")
    fulfilment = spec["evidence"] == "fulfilment"
    count = g["disputes_fulfilment_30d"] if fulfilment else g["disputes_30d"]
    what = "fulfilment-related disputes" if fulfilment else "disputes"
    p = g[f"cb{'_fulfilment' if fulfilment else ''}_{level}_p"]
    return (f"AUP-06.1 {level}: {count} {what} on {g['orders_30d']} orders in 30d "
            f"({count / g['orders_30d']:.1%}); a {m[f'chargeback_{level}']:.1%} rate gives "
            f">= {count} with p = {p:.2g}")


def describe(metrics: dict, codes: list[str], cfg: dict, rule_set: str) -> list[str]:
    """Include denominators so a rate alert can be assessed without guessing volume."""
    g, m = metrics, cfg["monitor"]
    spec = ITERATION2_SETS.get(rule_set)
    strings = []
    for code in codes:
        if code in ("W", "B"):
            strings.append(_chargeback(g, code, cfg, rule_set))
        elif code == "V":
            strings.append(f"AUP-06.2: volume z={g['volume_z']:.1f} vs baseline")
        elif code == "T":
            strings.append(f"AUP-06.3: avg ticket {g['ticket_drift']:.1f}x baseline")
        elif code == "S":
            strings.append(f"AUP-06.4: new-account GMV share {g['new_gmv_share']:.0%}")
        elif code == "Y":
            variant = (m["iteration2_young"] if spec is not None
                       else m["c3_young"] if rule_set == "c3" else rule_set)
            young = m["young_variants"][variant]
            label = "AUP-06.4b young merchant" if spec is not None else \
                "Young merchant concentration"
            strings.append(f"{label}: age {g['merchant_age_days']} days "
                           f"(< {young['age_days']}), new-account GMV share "
                           f"{g['new_gmv_share']:.0%} (>= {young['gmv_share']:.0%})")
        elif code == "F":
            strings.append(f"AUP-06.5: refund rate collapsed to {g['refund_rate_30d']:.1%} "
                           f"from {g['base_refund_rate']:.1%}; "
                           f"{g['disputes_30d']} disputes in 30d")
        elif code == "X":
            strings.append(f"AUP-06.6 delivery confirmation: {g['ship_cohort_unconfirmed']} of "
                           f"{g['ship_cohort_n']} shipments past the "
                           f"{g['delivery_deadline_days']}-day deadline unconfirmed "
                           f"(reference {g['delivery_p_ref']:.1%}; p = {g['delivery_p']:.2g})")
        elif code == "D":
            strings.append(f"Dispute-count surveillance: {g['disputes_30d']} disputes in 30d "
                           f"({g['orders_30d']} orders)")
    return strings
