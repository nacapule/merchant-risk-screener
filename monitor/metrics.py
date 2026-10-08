"""Backward-looking metrics use row windows on the completed daily calendar."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import binom, poisson

from monitor.rollup import REASONS, clip_shipments


def divide(numerator: pd.Series, denominator: pd.Series, defined: pd.Series) -> pd.Series:
    """Undefined or zero denominators stay null, including quiet trailing windows."""
    return numerator.div(denominator.where(defined & denominator.gt(0)))


def rolling_sum(values: pd.Series, window: int) -> pd.Series:
    """Integer cumulative differences keep monetary sums exact through zero-filled days."""
    total = values.cumsum()
    return total - total.shift(window, fill_value=0)


def evidence_p(disputes: pd.Series, orders: pd.Series, rate: float) -> pd.Series:
    """Chance that a merchant at exactly the policy rate learns of this many disputes or more."""
    return pd.Series(poisson.sf(disputes - 1, rate * orders), index=disputes.index)


def delivery_cohorts(g: pd.DataFrame, shipments: pd.DataFrame, deadline: int,
                     cohort_days: int) -> tuple[np.ndarray, np.ndarray]:
    """Shipments that reached the deadline in the last cohort_days, and those still unconfirmed.

    A shipment counts on days shipped + deadline .. + cohort_days - 1, and as unconfirmed on
    those days before its confirmation became known.
    """
    first, n_days = g.d.iloc[0], len(g)
    n_delta, u_delta = np.zeros(n_days + 1, "int64"), np.zeros(n_days + 1, "int64")
    start = (shipments.shipped_d - first).dt.days.to_numpy() + deadline
    end = start + cohort_days
    confirmed = (shipments.confirmed_d - first).dt.days.to_numpy(dtype=float, na_value=np.inf)
    for lo, hi, delta in [(start, end, n_delta), (start, np.minimum(end, confirmed), u_delta)]:
        lo, hi = np.clip(lo, 0, n_days), np.clip(hi, 0, n_days).astype("int64")
        keep = lo < hi
        np.add.at(delta, lo[keep], 1)
        np.add.at(delta, hi[keep], -1)
    return np.cumsum(n_delta)[:-1], np.cumsum(u_delta)[:-1]


def compute_metrics(spine: pd.DataFrame, cfg: dict, shipments: pd.DataFrame | None = None,
                    calibration: dict | None = None) -> pd.DataFrame:
    """Delivery metrics need both the shipments and a frozen calibration; otherwise null."""
    m = cfg["monitor"]
    window, baseline = m["window_days"], m["baseline_days"]
    onboarding = spine.attrs.get("meta", {}).get("onboarding", {})
    delivery = shipments is not None and calibration is not None and not spine.empty
    if delivery:
        by_merchant = dict(tuple(clip_shipments(shipments, spine.d.max())
                                 .groupby("merchant_id", sort=True)))
    groups = []
    for mid, group in spine.groupby("merchant_id", sort=True):
        g = group.sort_values("d").copy()
        for source, target in [("n_orders", "orders_30d"), ("gmv_cents", "gmv_30d"),
                               ("new_gmv_cents", "new_gmv_30d"),
                               ("n_disputes", "disputes_30d"), ("n_refunds", "refunds_30d"),
                               *[(col, f"{col.removeprefix('n_')}_30d") for col in REASONS]]:
            g[target] = rolling_sum(g[source], window)
        prior = g.n_orders.shift(window).rolling(baseline, min_periods=1)
        g["base_days"] = prior.count().fillna(0).astype("int64")
        g["base_mu"], g["base_var"] = prior.mean(), prior.var(ddof=1)
        for source, target in [("n_orders", "base_orders"), ("gmv_cents", "base_gmv"),
                               ("n_refunds", "base_refunds")]:
            g[target] = rolling_sum(g[source].shift(window, fill_value=0), baseline)
        enough = g.orders_30d.ge(m["min_orders_30d"])
        base = (g.base_days.ge(m["min_base_days"]) & g.base_orders.ge(m["min_base_orders"])
                & g.base_mu.notna() & g.base_var.notna())
        g["cb_rate_30d"] = divide(g.disputes_30d, g.orders_30d, enough)
        variance = pd.Series(np.maximum(g.base_mu, g.base_var), index=g.index)
        g["volume_z"] = divide(g.orders_30d - window * g.base_mu,
                               np.sqrt(window * variance), base)
        ticket = divide(g.gmv_30d, g.orders_30d, enough)
        base_ticket = divide(g.base_gmv, g.base_orders, base)
        g["ticket_drift"] = divide(ticket, base_ticket, enough & base)
        g["new_gmv_share"] = divide(g.new_gmv_30d, g.gmv_30d, enough)
        g["refund_rate_30d"] = divide(g.refunds_30d, g.orders_30d, enough)
        g["base_refund_rate"] = divide(g.base_refunds, g.base_orders, base)
        created = onboarding.get(str(mid), onboarding.get(mid))
        if created is None:
            raise ValueError(f"missing onboarding date for merchant {mid}")
        g["merchant_age_days"] = (g.d - pd.Timestamp(created).normalize()).dt.days
        first = g.loc[g.n_orders.gt(0), "d"].min()
        g["cum_orders"] = g.n_orders.cumsum()
        g["days_since_first_order"] = (g.d - first).dt.days.where(g.cum_orders.gt(0))
        g["eligible"] = (g.days_since_first_order.ge(m["min_days_since_first_order"])
                         & g.cum_orders.ge(m["min_cum_orders"]))
        if delivery:
            mine = by_merchant.get(mid)
            n, u = ((np.zeros(len(g), "int64"),) * 2 if mine is None else
                    delivery_cohorts(g, mine, calibration["deadline_days"],
                                     m["delivery"]["cohort_days"]))
            g["ship_cohort_n"], g["ship_cohort_unconfirmed"] = n, u
        groups.append(g)
    if not groups:
        result = spine.copy()
        result["eligible"] = pd.Series(dtype=bool)
        return result
    result = pd.concat(groups, ignore_index=True)
    enough = result.orders_30d.ge(m["min_orders_30d"])
    fulfilment = [f"disputes_{REASON_COLUMNS[r].removeprefix('n_disputes_')}_30d"
                  for r in m["fulfilment_reasons"]]
    result["disputes_fulfilment_30d"] = result[fulfilment].sum(axis=1)
    for prefix, count in [("cb", "disputes_30d"), ("cb_fulfilment", "disputes_fulfilment_30d")]:
        for level in ("breach", "warn"):
            result[f"{prefix}_{level}_p"] = evidence_p(
                result[count], result.orders_30d, m[f"chargeback_{level}"]).where(enough)
    if delivery:
        n, u = result.ship_cohort_n, result.ship_cohort_unconfirmed
        result["delivery_deadline_days"] = calibration["deadline_days"]
        result["delivery_p_ref"] = calibration["p_ref"]
        result["delivery_p"] = pd.Series(binom.sf(u - 1, n, calibration["p_ref"]),
                                         index=result.index).where(n.gt(0))
    result.attrs = spine.attrs.copy()
    return result


REASON_COLUMNS = {reason: col for col, reason in REASONS.items()}
