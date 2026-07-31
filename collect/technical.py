"""Technical signals for a merchant application: domain age, DNS/TLS posture,
reachability. Fixture-first — live lookups (RDAP, DNS, HTTPS probe) exist behind
``--live`` and are read-only.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import UTC
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


@dataclass
class TechnicalSignals:
    slug: str
    domain_age_days: int | None
    mx_present: bool
    tls_ok: bool
    reachable: bool
    source: str  # fixture | live


def collect_technical(slug: str, live: bool = False, domain: str | None = None
                      ) -> TechnicalSignals:
    if live and domain:
        return _collect_live(slug, domain)
    fx = REPO / "fixtures" / "whois" / f"{slug}.json"
    if not fx.exists():
        return TechnicalSignals(slug, None, False, False, False, "fixture-missing")
    d = json.loads(fx.read_text())
    return TechnicalSignals(
        slug=slug,
        domain_age_days=d.get("domain_age_days"),
        mx_present=bool(d.get("mx_present", True)),
        tls_ok=bool(d.get("tls_ok", True)),
        reachable=bool(d.get("reachable", True)),
        source="fixture",
    )


def _collect_live(slug: str, domain: str) -> TechnicalSignals:  # pragma: no cover
    """Read-only live probes; used for the illustrative live demo only."""
    import socket
    import ssl
    from datetime import datetime

    import requests

    age = None
    try:
        r = requests.get(f"https://rdap.org/domain/{domain}", timeout=10)
        if r.ok:
            events = {e["eventAction"]: e["eventDate"] for e in r.json().get("events", [])}
            reg = events.get("registration")
            if reg:
                dt = datetime.fromisoformat(reg.replace("Z", "+00:00"))
                age = (datetime.now(UTC) - dt).days
    except requests.RequestException:
        pass
    mx = False
    try:
        import subprocess

        out = subprocess.run(["dig", "+short", "MX", domain], capture_output=True,
                             text=True, timeout=10)
        mx = bool(out.stdout.strip())
    except Exception:  # noqa: BLE001
        pass
    tls = False
    reachable = False
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=10) as sock, ctx.wrap_socket(
            sock, server_hostname=domain
        ):
            tls = True
            reachable = True
    except OSError:
        pass
    return TechnicalSignals(slug, age, mx, tls, reachable, "live")


def as_dict(t: TechnicalSignals) -> dict:
    return asdict(t)
