"""Backward-looking metrics use row windows on the completed daily calendar."""

from __future__ import annotations

import numpy as np
import pandas as pd


def divide(numerator: pd.Series, denominator: pd.Series, defined: pd.Series) -> pd.Series:
    """Undefined or zero denominators stay null, including quiet trailing windows."""
    return numerator.div(denominator.where(defined & denominator.gt(0)))


def rolling_sum(values: pd.Series, window: int) -> pd.Series:
    """Integer cumulative differences keep monetary sums exact through zero-filled days."""
    total = values.cumsum()
    return total - total.shift(window, fill_value=0)


def compute_metrics(spine: pd.DataFrame, cfg: dict) -> pd.DataFrame:
    m = cfg["monitor"]
    window, baseline = m["window_days"], m["baseline_days"]
    onboarding = spine.attrs.get("meta", {}).get("onboarding", {})
    groups = []
    for mid, group in spine.groupby("merchant_id", sort=True):
        g = group.sort_values("d").copy()
        for source, target in [("n_orders", "orders_30d"), ("gmv_cents", "gmv_30d"),
                               ("new_gmv_cents", "new_gmv_30d"),
                               ("n_disputes", "disputes_30d"), ("n_refunds", "refunds_30d")]:
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
        groups.append(g)
    if not groups:
        result = spine.copy()
        result["eligible"] = pd.Series(dtype=bool)
        return result
    result = pd.concat(groups, ignore_index=True)
    result.attrs = spine.attrs.copy()
    return result
