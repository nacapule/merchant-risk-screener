from __future__ import annotations

from screen.llm_screen import verify_quotes


def test_verbatim_quote_passes() -> None:
    src = "We sell LV-style handbags with 1:1 mirror quality at great prices."
    v = verify_quotes(["1:1 mirror quality"], src)
    assert v["n_unverifiable"] == 0


def test_whitespace_and_case_normalized() -> None:
    src = "Premium   Vape\nHardware and e-liquids."
    v = verify_quotes(["premium vape hardware"], src)
    assert v["n_unverifiable"] == 0


def test_paraphrase_caught() -> None:
    src = "We sell designer-inspired handbags."
    v = verify_quotes(["they sell counterfeit designer bags"], src)
    assert v["n_unverifiable"] == 1
    assert v["missing"]


def test_empty_quote_ignored() -> None:
    assert verify_quotes([""], "anything")["n_unverifiable"] == 0
