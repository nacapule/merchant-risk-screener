"""Site-content signals: extract text from fixture HTML, detect policy pages,
assemble the corpus the LLM screening reads.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup

REPO = Path(__file__).resolve().parent.parent

POLICY_MARKERS = {
    "refund_policy": ("refund", "return policy", "returns", "devolucion", "reembolso"),
    "shipping_policy": ("shipping", "delivery", "envío", "envio"),
    "terms": ("terms of service", "terms and conditions", "términos", "terminos"),
    "contact": ("contact", "contacto"),
}


@dataclass
class SiteContent:
    slug: str
    pages: dict[str, str] = field(default_factory=dict)  # filename -> extracted text
    policy_pages: dict[str, bool] = field(default_factory=dict)
    has_phone: bool = False
    has_address: bool = False
    full_text: str = ""


def _page_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return " ".join(soup.get_text(" ").split())


def collect_content(slug: str) -> SiteContent:
    site_dir = REPO / "fixtures" / "sites" / slug
    sc = SiteContent(slug=slug)
    if not site_dir.exists():
        return sc
    corpus: list[str] = []
    for f in sorted(site_dir.glob("*.html")):
        text = _page_text(f.read_text())
        sc.pages[f.name] = text
        corpus.append(f"[page:{f.name}] {text}")
    sc.full_text = "\n".join(corpus)
    low = sc.full_text.lower()
    for key, markers in POLICY_MARKERS.items():
        sc.policy_pages[key] = any(m in low for m in markers)
    sc.has_phone = any(
        tok in low for tok in ("tel:", "phone", "teléfono", "telefono", "+1-", "+52")
    )
    sc.has_address = any(
        tok in low for tok in ("suite ", " st.", " ave", "street", "col. ", "cp ", "zip")
    )
    return sc


def load_reviews(slug: str) -> list[dict]:
    import csv

    path = REPO / "fixtures" / "reviews" / f"{slug}.csv"
    if not path.exists():
        return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))
