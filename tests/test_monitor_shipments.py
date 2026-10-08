"""Synthetic shipments test what the platform knew of each delivery on each day."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import pytest

from monitor.rollup import (
    ReconciliationError,
    clip_shipments,
    export_shipments,
    load_shipments,
    reconcile_shipments,
    shipment_totals,
)


def shipments(rows: list[tuple], as_of: str = "2024-02-29") -> pd.DataFrame:
    df = pd.DataFrame(rows, columns=["merchant_id", "order_id", "amount_cents", "shipped_d",
                                     "confirmed_d"])
    for col in ("shipped_d", "confirmed_d"):
        df[col] = pd.to_datetime(df[col])
    df.attrs["meta"] = {"as_of": as_of, "counts": shipment_totals(df),
                        "source": {"file": "synthetic", "sha256": "synthetic"}}
    return df


ROWS = [(1, 10, 1000, "2024-01-02", "2024-01-04"),
        (1, 11, 2500, "2024-01-03", None),
        (1, 12, 1500, "2024-01-05", "2024-01-20"),
        (2, 20, 900, "2024-01-09", "2024-01-10")]


def test_clip_keeps_only_what_was_known_by_the_cutoff() -> None:
    clipped = clip_shipments(shipments(ROWS), "2024-01-08")
    assert clipped.order_id.tolist() == [10, 11, 12]
    assert clipped.set_index("order_id").confirmed_d.isna().to_dict() == {
        10: False, 11: True, 12: True}
    assert shipment_totals(clipped) == {"n_shipments": 3, "n_confirmed": 1}


def test_export_round_trip_is_byte_identical(tmp_path: Path) -> None:
    first, second = tmp_path / "a.csv.gz", tmp_path / "b.csv.gz"
    export_shipments(first, shipments(ROWS))
    export_shipments(second, shipments(ROWS))
    assert first.read_bytes() == second.read_bytes()
    loaded = load_shipments(first)
    assert shipment_totals(loaded) == {"n_shipments": 4, "n_confirmed": 3}
    assert loaded.confirmed_d.isna().sum() == 1


def test_export_at_an_earlier_cutoff_recounts_the_clipped_rows(tmp_path: Path) -> None:
    path = tmp_path / "s.csv.gz"
    export_shipments(path, shipments(ROWS), "2024-01-08")
    meta = json.loads(Path(f"{path}.meta.json").read_text())
    assert meta["as_of"] == "2024-01-08"
    assert meta["counts"] == {"n_shipments": 3, "n_confirmed": 1}


def test_load_rejects_a_changed_export(tmp_path: Path) -> None:
    path = tmp_path / "s.csv.gz"
    export_shipments(path, shipments(ROWS))
    path.write_bytes(path.read_bytes() + b"\0")
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        load_shipments(path)


def test_one_row_per_order(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="one row per order"):
        export_shipments(tmp_path / "s.csv.gz", shipments([*ROWS, ROWS[0]]))


def test_reconcile_names_the_mismatch() -> None:
    with pytest.raises(ReconciliationError, match="n_confirmed: export total 3 != source total 4"):
        reconcile_shipments(shipments(ROWS), {"n_shipments": 4, "n_confirmed": 4})
