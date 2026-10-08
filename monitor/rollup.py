"""Dated inputs and a complete calendar make missing event days auditable."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import pandas as pd

REPO = Path(__file__).resolve().parent.parent
DEFAULT_DSN = "mysql+pymysql://fraud:fraudpw@127.0.0.1:3306/bnpl"
REASONS = {"n_disputes_unauthorized": "unauthorized",
           "n_disputes_not_received": "item_not_received",
           "n_disputes_not_as_described": "not_as_described"}
VALUES = ["n_orders", "gmv_cents", "n_new_orders", "new_gmv_cents", "n_disputes", "n_refunds",
          *REASONS]
COLUMNS = ["merchant_id", "d", *VALUES]
COUNT_COLUMNS = ["n_orders", "n_disputes", "n_refunds", *REASONS]
SHIPMENT_COLUMNS = ["merchant_id", "order_id", "amount_cents", "shipped_d", "confirmed_d"]
ONBOARDING_SQL = "SELECT merchant_id, created_at FROM merchants"


class ReconciliationError(ValueError):
    """A missing join parent or event day must stop the replay."""


def day(value: str | pd.Timestamp) -> pd.Timestamp:
    return pd.Timestamp(value).normalize()


def db_url() -> str:
    return os.environ.get("MONITOR_DB_URL", DEFAULT_DSN)


def source_info(url: str) -> dict:
    """Keep connection provenance without persisting credentials."""
    parsed = urlsplit(url)
    return {"host": parsed.hostname, "port": parsed.port or 3306,
            "database": parsed.path.lstrip("/")}


def source_as_of(conn: Any) -> str:
    """Source dates keep the cutoff from hiding events lost by extraction joins."""
    from sqlalchemy import text

    queries = [
        "SELECT MAX(DATE(ts)) FROM orders WHERE status='approved'",
        "SELECT MAX(DATE(opened_ts)) FROM chargebacks",
        "SELECT MAX(DATE(known_at)) FROM cash_events WHERE kind='refund'",
        "SELECT MAX(DATE(known_at)) FROM fulfilments",
        "SELECT MAX(DATE(known_at)) FROM deliveries",
    ]
    dates = [conn.execute(text(sql)).scalar_one() for sql in queries]
    return str(max(day(date) for date in dates if date is not None).date())


def source_counts(conn: Any, as_of: str | pd.Timestamp) -> dict[str, int]:
    """Independent source totals expose rows lost by extraction joins."""
    from sqlalchemy import text

    queries = {
        "n_orders": "SELECT COUNT(*) FROM orders WHERE status='approved' AND ts < :end",
        "n_disputes": "SELECT COUNT(*) FROM chargebacks WHERE opened_ts < :end",
        "n_refunds": """SELECT COUNT(DISTINCT order_id, merchant_id, DATE(known_at))
                        FROM cash_events WHERE kind='refund' AND known_at < :end""",
        **{col: f"SELECT COUNT(*) FROM chargebacks WHERE opened_ts < :end AND reason = '{reason}'"
           for col, reason in REASONS.items()},
    }
    end = (day(as_of) + pd.Timedelta(days=1)).to_pydatetime()
    return {key: int(conn.execute(text(sql), {"end": end}).scalar_one())
            for key, sql in queries.items()}


def shipment_source_counts(conn: Any, as_of: str | pd.Timestamp) -> dict[str, int]:
    """Count shipped and carrier-confirmed orders independently of the extraction join."""
    from sqlalchemy import text

    queries = {
        "n_shipments": "SELECT COUNT(DISTINCT order_id) FROM fulfilments WHERE known_at < :end",
        "n_confirmed": """SELECT COUNT(DISTINCT dl.order_id) FROM deliveries dl
                          JOIN fulfilments f ON f.order_id = dl.order_id
                          WHERE dl.known_at < :end AND f.known_at < :end""",
    }
    end = (day(as_of) + pd.Timedelta(days=1)).to_pydatetime()
    return {key: int(conn.execute(text(sql), {"end": end}).scalar_one())
            for key, sql in queries.items()}


def event_totals(events: pd.DataFrame) -> dict[str, int]:
    return {col: int(events[col].sum()) for col in COUNT_COLUMNS}


def _canonical(events: pd.DataFrame) -> pd.DataFrame:
    attrs = events.attrs.copy()
    events = events[COLUMNS].copy()
    events["d"] = pd.to_datetime(events["d"]).dt.normalize()
    if events["d"].isna().any():
        raise ValueError("event dates must be present")
    for col in ["merchant_id", *VALUES]:
        numeric = pd.to_numeric(events[col])
        if numeric.isna().any() or (numeric % 1 != 0).any() or (numeric < 0).any():
            raise ValueError(f"{col} must contain nonnegative integers")
        events[col] = numeric.astype("int64")
    if events.duplicated(["merchant_id", "d"]).any():
        raise ValueError("events must have one row per merchant-day")
    if not events[list(REASONS)].sum(axis=1).eq(events.n_disputes).all():
        raise ReconciliationError("dispute reasons must sum to n_disputes on every row")
    events = events.sort_values(["merchant_id", "d"]).reset_index(drop=True)
    events.attrs = attrs
    return events


def load_events(source: str | Path | None = None) -> pd.DataFrame:
    """File exports carry onboarding and independently reconciled source counts."""
    if source is not None and "://" not in str(source):
        path = Path(source)
        meta = json.loads(Path(f"{path}.meta.json").read_text())
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != meta["sha256"]:
            raise ValueError(f"event export SHA-256 mismatch: {path}")
        events = _canonical(pd.read_csv(path, parse_dates=["d"]))
        events.attrs["meta"] = {**meta, "source": {"file": str(path), "sha256": digest}}
        if not events.empty and events.d.max() > day(meta["as_of"]):
            raise ValueError("event export contains dates after its as_of")
        return events

    import sqlalchemy as sa

    url = str(source) if source is not None else db_url()
    engine = sa.create_engine(url)
    try:
        with engine.connect() as conn:
            events = _canonical(pd.read_sql(sa.text((REPO / "monitor/events.sql").read_text()),
                                           conn, coerce_float=False))
            if events.empty:
                raise ValueError("no events; specify an exported history")
            as_of = source_as_of(conn)
            onboarding = {str(mid): str(created) for mid, created in
                          conn.execute(sa.text(ONBOARDING_SQL))}
            counts = source_counts(conn, as_of)
    finally:
        engine.dispose()
    events.attrs["meta"] = {"as_of": as_of, "onboarding": onboarding,
                            "counts": counts, "source": source_info(url),
                            "database_source": source_info(url)}
    events.attrs["db_url"] = url
    return events


def counts_at(events: pd.DataFrame, as_of: str | pd.Timestamp) -> dict[str, int]:
    """Earlier file cutoffs can reconcile only against the exported event rows."""
    meta = events.attrs["meta"]
    if "file" in meta["source"]:
        return (meta["counts"] if day(as_of) == day(meta["as_of"])
                else event_totals(events.loc[events.d <= day(as_of)]))
    import sqlalchemy as sa

    engine = sa.create_engine(events.attrs.get("db_url", db_url()))
    try:
        with engine.connect() as conn:
            return source_counts(conn, as_of)
    finally:
        engine.dispose()


def export_events(path: str | Path, events: pd.DataFrame | None = None,
                  as_of: str | pd.Timestamp | None = None) -> pd.DataFrame:
    """Fixed CSV order and a zero gzip timestamp make repeated exports byte-identical."""
    events = load_events() if events is None else events
    cutoff = day(as_of or events.attrs["meta"]["as_of"])
    if "file" in events.attrs["meta"]["source"] and cutoff > day(events.attrs["meta"]["as_of"]):
        raise ValueError("export as_of cannot exceed the source observation date")
    counts = counts_at(events, cutoff)
    exported = _canonical(events.loc[events.d <= cutoff])
    reconcile(build_spine(exported, cutoff), exported, counts)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    csv = exported.to_csv(index=False, date_format="%Y-%m-%d", lineterminator="\n")
    with path.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(csv.encode("utf-8"))
    meta = {**events.attrs["meta"], "as_of": str(cutoff.date()), "counts": counts,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    Path(f"{path}.meta.json").write_text(
        json.dumps(meta, indent=1, sort_keys=True, allow_nan=False))
    exported.attrs["meta"] = meta
    return exported


def build_spine(events: pd.DataFrame, as_of: str | pd.Timestamp) -> pd.DataFrame:
    """Continue every merchant calendar through the cutoff, including quiet days."""
    cutoff = day(as_of)
    clipped = _canonical(events.loc[events.d <= cutoff])
    calendars = [pd.DataFrame({"merchant_id": mid, "d": pd.date_range(g.d.min(), cutoff)})
                 for mid, g in clipped.groupby("merchant_id", sort=True)]
    if not calendars:
        result = clipped.copy()
    else:
        result = pd.concat(calendars, ignore_index=True).merge(
            clipped.astype(dict.fromkeys(VALUES, "Int64")),
            on=["merchant_id", "d"], how="left")
        result[VALUES] = result[VALUES].fillna(0).astype("int64")
    result.attrs = events.attrs.copy()
    return result


def reconcile(spine: pd.DataFrame, events: pd.DataFrame, counts: dict[str, int]) -> dict:
    """Check both extraction and calendar completion; neither may drop events."""
    spine_counts, events_counts = event_totals(spine), event_totals(events)
    for col in COUNT_COLUMNS:
        if spine_counts[col] != events_counts[col]:
            raise ReconciliationError(
                f"{col}: spine total {spine_counts[col]} != event total {events_counts[col]}")
        if events_counts[col] != counts[col]:
            raise ReconciliationError(
                f"{col}: event total {events_counts[col]} != source total {counts[col]}")
    return {"spine": spine_counts, "events": events_counts, "source": counts}


def _canonical_shipments(shipments: pd.DataFrame) -> pd.DataFrame:
    attrs = shipments.attrs.copy()
    shipments = shipments[SHIPMENT_COLUMNS].copy()
    for col in ("shipped_d", "confirmed_d"):
        shipments[col] = pd.to_datetime(shipments[col]).dt.normalize()
    if shipments["shipped_d"].isna().any():
        raise ValueError("shipment dates must be present")
    for col in ("merchant_id", "order_id", "amount_cents"):
        numeric = pd.to_numeric(shipments[col])
        if numeric.isna().any() or (numeric % 1 != 0).any() or (numeric < 0).any():
            raise ValueError(f"{col} must contain nonnegative integers")
        shipments[col] = numeric.astype("int64")
    if shipments.order_id.duplicated().any():
        raise ValueError("shipments must have one row per order")
    shipments = shipments.sort_values(["merchant_id", "order_id"]).reset_index(drop=True)
    shipments.attrs = attrs
    return shipments


def clip_shipments(shipments: pd.DataFrame, as_of: str | pd.Timestamp) -> pd.DataFrame:
    """Keep what was known by the end of as_of; a later confirmation stays unknown."""
    cutoff = day(as_of)
    clipped = shipments.loc[shipments.shipped_d.le(cutoff)].copy()
    clipped["confirmed_d"] = clipped.confirmed_d.where(clipped.confirmed_d.le(cutoff))
    clipped.attrs = shipments.attrs.copy()
    return clipped


def shipment_totals(shipments: pd.DataFrame) -> dict[str, int]:
    return {"n_shipments": len(shipments), "n_confirmed": int(shipments.confirmed_d.notna().sum())}


def reconcile_shipments(shipments: pd.DataFrame, counts: dict[str, int]) -> dict:
    totals = shipment_totals(shipments)
    for key, value in totals.items():
        if value != counts[key]:
            raise ReconciliationError(f"{key}: export total {value} != source total {counts[key]}")
    return {"shipments": totals, "source": counts}


def load_shipments(source: str | Path | None = None) -> pd.DataFrame:
    """One row per shipped order with the days the shipment and confirmation became known."""
    if source is not None and "://" not in str(source):
        path = Path(source)
        meta = json.loads(Path(f"{path}.meta.json").read_text())
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != meta["sha256"]:
            raise ValueError(f"shipment export SHA-256 mismatch: {path}")
        shipments = _canonical_shipments(pd.read_csv(path))
        shipments.attrs["meta"] = {**meta, "source": {"file": str(path), "sha256": digest}}
        if not shipments.empty and shipments.shipped_d.max() > day(meta["as_of"]):
            raise ValueError("shipment export contains dates after its as_of")
        return shipments

    import sqlalchemy as sa

    url = str(source) if source is not None else db_url()
    engine = sa.create_engine(url)
    try:
        with engine.connect() as conn:
            shipments = _canonical_shipments(pd.read_sql(
                sa.text((REPO / "monitor/shipments.sql").read_text()), conn,
                coerce_float=False))
            as_of = source_as_of(conn)
            counts = shipment_source_counts(conn, as_of)
    finally:
        engine.dispose()
    shipments.attrs["meta"] = {"as_of": as_of, "counts": counts, "source": source_info(url)}
    shipments.attrs["db_url"] = url
    return shipments


def shipment_counts_at(shipments: pd.DataFrame, as_of: str | pd.Timestamp) -> dict[str, int]:
    """Earlier file cutoffs can reconcile only against the exported rows."""
    meta = shipments.attrs["meta"]
    if "file" in meta["source"]:
        return (meta["counts"] if day(as_of) == day(meta["as_of"])
                else shipment_totals(clip_shipments(shipments, as_of)))
    import sqlalchemy as sa

    engine = sa.create_engine(shipments.attrs.get("db_url", db_url()))
    try:
        with engine.connect() as conn:
            return shipment_source_counts(conn, as_of)
    finally:
        engine.dispose()


def export_shipments(path: str | Path, shipments: pd.DataFrame | None = None,
                     as_of: str | pd.Timestamp | None = None) -> pd.DataFrame:
    """Fixed CSV order and a zero gzip timestamp make repeated exports byte-identical."""
    shipments = load_shipments() if shipments is None else shipments
    meta = shipments.attrs["meta"]
    cutoff = day(as_of or meta["as_of"])
    if "file" in meta["source"] and cutoff > day(meta["as_of"]):
        raise ValueError("export as_of cannot exceed the source observation date")
    counts = shipment_counts_at(shipments, cutoff)
    exported = _canonical_shipments(clip_shipments(shipments, cutoff))
    reconcile_shipments(exported, counts)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    csv = exported.to_csv(index=False, date_format="%Y-%m-%d", lineterminator="\n")
    with path.open("wb") as raw, gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as gz:
        gz.write(csv.encode("utf-8"))
    meta = {**meta, "as_of": str(cutoff.date()), "counts": counts,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    Path(f"{path}.meta.json").write_text(
        json.dumps(meta, indent=1, sort_keys=True, allow_nan=False))
    exported.attrs["meta"] = meta
    return exported
