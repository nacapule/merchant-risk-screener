"""Generate the fixture merchant sites + review corpora from manifest briefs.

Deterministic (seed from config), no network, no LLM: pages are assembled from
templates plus per-merchant authored content blocks (the distinctive evidence —
counterfeit vocabulary, health claims, missing policies — is intentional and
hand-written below). All merchants are fictional; brands are invented.

Run: python fixtures/generate_fixtures.py
"""

from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
FIX = REPO / "fixtures"

PAGE = """<!doctype html><html><head><title>{title}</title></head>
<body><header><h1>{name}</h1><nav>{nav}</nav></header>
<main>{main}</main>
<footer>{footer}</footer></body></html>"""

REFUND_OK = """<h2>Refund &amp; Return Policy</h2><p>Returns accepted within 30 days of
delivery in original condition. Refunds are issued to the original payment method within
5–7 business days of receiving the return. Return shipping is free for defective items.</p>"""
SHIPPING_OK = """<h2>Shipping Policy</h2><p>Orders ship within {ship_days} business days
via tracked carrier. Standard delivery {delivery}. Tracking is emailed at dispatch.</p>"""
TERMS_OK = """<h2>Terms of Service</h2><p>By purchasing you agree to our terms of sale,
privacy policy, and applicable consumer protection law of {jurisdiction}.</p>"""
CONTACT_FULL = """<h2>Contact</h2><p>Email: support@{domain} · Phone: {phone} ·
{address}</p>"""
CONTACT_EMAIL_ONLY = """<h2>Contact</h2><p>Email: support@{domain}</p>"""

# ---------------------------------------------------------------------------
# per-merchant authored content: products/about text and review banks.
# (m = manifest entry; blocks reference policy-relevant vocabulary on purpose)
# ---------------------------------------------------------------------------

PRODUCTS: dict[str, str] = {
    "lumen-apparel": """<h2>Featured</h2><ul><li>Organic cotton crewneck — $48</li>
<li>Linen overshirt — $89</li><li>Merino cardigan — $120</li><li>Everyday chino — $64</li>
</ul><p>Designed in Minneapolis, made responsibly. Fits true to size.</p>""",
    "maya-ceramics": """<h2>The studio</h2><p>Hand-thrown stoneware from our Oaxaca
workshop. Each piece is unique; glazes are food-safe and lead-free. Made-to-order pieces
ship in 1–2 weeks — handmade takes time and we say so up front.</p>
<ul><li>Mezcal copitas (set of 2) — $38</li><li>Serving bowl — $72</li></ul>""",
    "casadecor-mx": """<h2>Catálogo</h2><p>Decoración para el hogar: lámparas artesanales,
textiles de Chiapas, espejos de hojalata. Showroom en Roma Norte, CDMX — visítanos.
Envíos a todo México y EE.UU.</p><ul><li>Lámpara de barro — $1,150 MXN</li>
<li>Tapete de lana 2x1.5m — $3,400 MXN</li></ul>
<h3>Política de devoluciones</h3><p>Devoluciones dentro de 30 días. Reembolso al método
de pago original. Envío: 3–7 días hábiles con guía rastreable.</p>""",
    "bloom-stem": """<h2>Fresh today</h2><ul><li>Market bouquet — $35</li>
<li>Peony dozen (seasonal) — $58</li><li>Orchid planter — $75</li></ul>
<p>Same-day local delivery ordered before 1pm. Flowers are perishable: delivery issues
must be reported within 24h with a photo and we will replace or refund.</p>""",
    "technest-deals": """<h2>This week's deals</h2><ul>
<li>Renewed flagship phone (unlocked) — $389 <s>$629</s></li>
<li>Wireless earbuds — $39</li><li>4K action cam — $95</li>
<li>GAME KEYS: latest releases from $19 — instant email delivery</li></ul>
<p>Why so cheap? We buy overstock and open-box lots. All sales ship from our warehouse.</p>""",
    "stellar-tickets": """<h2>On sale now</h2><ul><li>Stadium tour — from $89</li>
<li>Playoff seats — from $140</li><li>Festival weekend passes — from $210</li></ul>
<p>All-in pricing shown at checkout: our service fee (12%) and delivery are itemized
before you pay. E-tickets transfer to your wallet app; some venues release paper tickets
only 48h before the event — we say so on the listing.</p>""",
    "pixelforge-games": """<h2>Instant keys</h2><ul><li>AAA new releases — $59.99</li>
<li>Indie bundles — from $9.99</li><li>DLC and season passes</li></ul>
<p>Keys are region-locked as listed (NA/EU/GLOBAL badges on every product). Delivery is
instant to your account library and email. Revoked-key protection: replacement or refund
within 90 days with proof.</p>""",
    "flashfone-repairs": """<h2>Repairs</h2><ul><li>Screen replacement — from $79</li>
<li>Battery — from $49</li><li>Mail-in service: $25 deposit, quote before work</li></ul>
<p>Most repairs done same day in-store.</p>""",
    "quickdrop-gadgets": """<h2>Trending now</h2><ul><li>Mini projector — $59</li>
<li>Smart posture band — $34</li><li>Galaxy star lamp — $27</li><li>Ice maker — $89</li>
</ul><p>Viral gadgets at factory prices. Ships from our partner facilities in 4–6 weeks.
Limited stock — order now!</p>""",
    "titan-supps": """<h2>Best sellers</h2><ul>
<li>Whey isolate 2kg — $54. Supports muscle recovery after training.</li>
<li>Creatine monohydrate — $29. Supports strength and performance.</li>
<li>JointShield Pro — $46. Clinically studied ingredients for joint comfort.</li>
<li>GlucoBalance — $39. Helps maintain healthy blood sugar levels already in normal range.</li>
<li>Omega-3 — $22. Supports heart health.</li></ul>""",
    "heritage-watches": """<h2>Current consignments</h2><ul>
<li>1968 chronograph, gilt dial — $8,400</li><li>Dress watch, 18k — $3,900</li>
<li>Dive watch, patina lume — $2,850</li><li>Field watch — $820</li></ul>
<p>Curated vintage timepieces on consignment. Serious inquiries only.</p>""",
    "aura-lux-bags": """<h2>New arrivals</h2><ul>
<li>LV-style monogram tote, 1:1 mirror quality — $129</li>
<li>Inspired by Gucci marmont, top-grain leather — $99</li>
<li>Birkin-style 30cm, same hardware as the original — $189</li>
<li>CC-pattern quilted crossbody — $85</li></ul>
<p>Luxury looks without the luxury markup. Our factory sources the same materials as the
big houses. Logos and packaging are indistinguishable from boutique originals.</p>""",
    "giftcardhub-mx": """<h2>Discounted gift cards</h2><ul>
<li>Retail giants — 8% off face value</li><li>Gaming and app-store cards — 10% off</li>
<li>Streaming subscriptions — 12% off</li><li>Bulk orders welcome — contact sales</li>
</ul><p>Codes delivered instantly by email. We buy unwanted cards and resell them —
that's the discount. Full refund policy, shipping policy (digital), terms, and 24/7
contact center.</p>""",
    "greenleaf-wellness": """<h2>Botanical wellness</h2><ul>
<li>Full-spectrum CBD tincture 1000mg — $64</li><li>CBD sleep gummies with melatonin —
$38</li><li>Muscle-relief CBD balm — $29</li></ul>
<p>Third-party lab reports on every batch (COA links on product pages). Customers tell
us our tincture cured their insomnia — read the reviews. Hemp-derived, under 0.3% THC.</p>""",
    "nova-vape": """<h2>Shop</h2><p class="age-gate">You must be 21+ to enter this site.</p>
<ul><li>Pod systems — from $24</li><li>E-liquid 60ml, 40+ flavors — $16</li>
<li>Disposables, 5000 puffs — $19</li><li>Coils and tanks</li></ul>
<p>Adult signature required on delivery.</p>""",
    "urban-threads-outlet": """<h2>Outlet steals</h2><ul><li>Denim from $19</li>
<li>Hoodies from $24</li><li>Sneakers from $39</li></ul>
<p>Overstock from major brands at outlet prices. Because these are final-lot goods,
processing can take longer than usual.</p>""",
}

ABOUT: dict[str, str] = {
    "lumen-apparel": "<p>Founded 2023 in Minneapolis. 40+ styles, sizes XS–3XL.</p>",
    "maya-ceramics": "<p>Family workshop, three generations of Oaxacan pottery.</p>",
    "casadecor-mx": ("<p>Desde 2021. Showroom: Córdoba 87, Roma Norte, CDMX. "
                     "Tel +52 55 5525 1187.</p>"),
    "bloom-stem": "<p>Neighborhood florist since 2024. Cooler-fresh guarantee.</p>",
    "technest-deals": "<p>Overstock and open-box electronics. Warehouse direct.</p>",
    "stellar-tickets": "<p>Licensed resale marketplace; seller verification since 2023.</p>",
    "pixelforge-games": "<p>Authorized key distributor; 200k+ orders delivered.</p>",
    "flashfone-repairs": ("<p>Two locations. Certified technicians. Tel (612) 555-0142, "
                          "88 Lyndale Ave S.</p>"),
    "quickdrop-gadgets": "<p>We find viral products before they trend.</p>",
    "titan-supps": ("<p>Formulated with transparency. cGMP facility. Contact: "
                    "hello@titan-supps.example, (480) 555-0114, 2200 E Camelback Rd.</p>"),
    "heritage-watches": "<p>Private consignment gallery. By appointment.</p>",
    "aura-lux-bags": "<p>Direct-from-factory luxury-style accessories.</p>",
    "giftcardhub-mx": ("<p>Registered reseller. Av. Insurgentes Sur 1425, CDMX. "
                       "Tel +52 55 5601 0930.</p>"),
    "greenleaf-wellness": ("<p>Colorado-grown hemp. COAs published for every lot. Contact: "
                           "care@greenleaf.example, (720) 555-0163, 1310 Pearl St.</p>"),
    "nova-vape": ("<p>Independent vape shop since 2019. Tel (503) 555-0177, "
                  "921 SE Division St.</p>"),
    "urban-threads-outlet": ("<p>Online-only outlet. Support: help@urbanthreads.example, "
                             "(312) 555-0128, 400 W Superior St.</p>"),
}

# review banks: (weight, rating, text). Weights steer sampling; dates spread by index.
REVIEWS: dict[str, list[tuple[int, int, str]]] = {
    "lumen-apparel": [
        (30, 5, "Quality is excellent and the fit was exactly as the size chart said."),
        (15, 4, "Nice fabric, shipped in three days, would buy again."),
        (6, 3, "Runs slightly small for me, exchange was easy though."),
        (4, 4, "Shipping took a bit longer than promised but the sweater is great."),
        (2, 2, "Color faded a little after several washes."),
    ],
    "maya-ceramics": [
        (18, 5, "Beautiful craftsmanship, you can feel the hand of the maker."),
        (5, 5, "Arrived carefully packed, even more beautiful in person."),
        (2, 4, "One copita arrived chipped and they replaced it the same week."),
    ],
    "casadecor-mx": [
        (25, 5, "La lámpara llegó perfecta, empaque muy cuidado."),
        (12, 4, "Buena calidad, el envío tardó una semana."),
        (5, 3, "El tapete tardó en llegar por aduana, pero llegó bien."),
        (3, 2, "El espejo llegó con un rayón pequeño."),
    ],
    "bloom-stem": [
        (20, 5, "Flowers arrived fresh and gorgeous, made her whole week."),
        (10, 4, "Delivery was on time, arrangement slightly smaller than the photo."),
        (3, 2, "Bouquet arrived wilted; they refunded after I sent a photo."),
        (2, 5, "Same-day delivery saved my anniversary."),
    ],
    "technest-deals": [
        (14, 5, "Phone was genuinely like new, unbeatable price."),
        (10, 4, "Good deal on the earbuds, packaging was generic but they work."),
        (8, 2, "Took three weeks to arrive with zero updates."),
        (5, 1, "The seal was broken on the box and the charger was missing."),
        (4, 2, "Game key didn't activate, support took a week to replace it."),
        (9, 3, "You get what you pay for. Slow shipping, decent product."),
    ],
    "stellar-tickets": [
        (30, 5, "Tickets transferred instantly, seats were exactly as listed."),
        (18, 4, "Fees are visible before checkout which I appreciate."),
        (8, 3, "Tickets arrived the day of the show, stressful but valid."),
        (6, 2, "Event got cancelled and the refund took three weeks."),
        (8, 5, "Second time buying playoff seats here, flawless both times."),
    ],
    "pixelforge-games": [
        (40, 5, "Key delivered in seconds and activated first try."),
        (20, 4, "Great bundle price. Region badge was accurate."),
        (8, 3, "Bought the wrong region by mistake, exchange took two days."),
        (4, 1, "Key was revoked a month later, replaced under their protection policy."),
        (8, 5, "Cheapest legit keys I've found."),
    ],
    "flashfone-repairs": [
        (10, 5, "Screen fixed in two hours, looks brand new."),
        (5, 4, "Fair price for the battery swap."),
        (2, 1, "Mail-in took two weeks and nobody answered the phone."),
        (3, 5, "Honest quote, they even waived the deposit when I picked it up."),
    ],
    "quickdrop-gadgets": [],  # no reviews on purpose (insufficient-info lever)
    "titan-supps": [
        (18, 5, "Mixes clean, tastes great, recovery feels faster."),
        (10, 4, "Solid creatine, standard results."),
        (6, 3, "The joint supplement did nothing for me."),
        (4, 4, "Fast shipping, tubs sealed properly."),
        (2, 1, "Didn't work as advertised."),
    ],
    "heritage-watches": [
        (3, 5, "The chronograph was exactly as photographed, superb condition."),
        (2, 5, "Smooth transaction on a five-figure piece."),
        (1, 3, "Shipping insurance paperwork took longer than expected."),
    ],
    "aura-lux-bags": [
        (16, 5, "Looks just like the real one, my friends can't tell the difference."),
        (10, 4, "Amazing copy for the price, hardware feels heavy and solid."),
        (6, 2, "Customs seized my order as counterfeit and I got nothing back."),
        (4, 1, "The logo peeled off the tote after two weeks."),
        (5, 3, "Stitching is good, smell took a week to air out."),
        (4, 5, "Ordered the Birkin-style, quality is insane for 189."),
    ],
    "giftcardhub-mx": [
        (30, 5, "Code arrived instantly and worked, saved 8% on my groceries."),
        (14, 4, "Second bulk order, all codes valid."),
        (6, 1, "One card had zero balance, support replaced it after two days."),
        (8, 5, "Been using monthly for a year, never a bad code."),
    ],
    "greenleaf-wellness": [
        (20, 5, "The tincture cured my insomnia, I sleep through the night now."),
        (12, 5, "Gummies are gentle and the COA link is right on the page."),
        (6, 4, "Balm helps my knees after runs."),
        (4, 3, "Subtle effect, might need a stronger dose."),
    ],
    "nova-vape": [
        (14, 5, "Huge flavor selection, fast shipping."),
        (8, 4, "Pods arrived well packed, prices beat the local shop."),
        (4, 3, "One coil was dead on arrival."),
        (2, 1, "They didn't even check my age at delivery, my nephew signed for it."),
    ],
    "urban-threads-outlet": [
        # recent-half dominated by non-delivery + refund refusal (decline lever)
        (25, 1, "Ordered six weeks ago and it never arrived. Support ghosted me."),
        (15, 1, "Never got my package and they refuse to refund, avoid this store."),
        (12, 1, "No tracking, no reply to four emails, had to dispute with my bank."),
        (10, 2, "One hoodie of three arrived. No refund answer for the missing two."),
        (18, 4, "Older order: jeans came in ten days and were fine."),
        (10, 5, "Bought last year, good prices back then."),
        (10, 2, "Sizing was wrong and returns page just loops, gave up."),
    ],
}


def build_site(m: dict, rng: random.Random) -> None:
    slug = m["slug"]
    d = FIX / "sites" / slug
    d.mkdir(parents=True, exist_ok=True)
    domain = f"{slug}.example"
    nav_pages = ["index", "about"]
    footer = f"© 2026 {m['name']} — all merchants on this fixture set are fictional."

    complete = slug in {
        "lumen-apparel", "maya-ceramics", "bloom-stem", "stellar-tickets",
        "pixelforge-games", "giftcardhub-mx", "greenleaf-wellness", "nova-vape",
        "urban-threads-outlet", "titan-supps", "aura-lux-bags",
    }  # aura is polished on purpose: counterfeit shops often are; the decline
       # must come from content (AUP-01.7), not hygiene points
    partial = slug in {"technest-deals", "flashfone-repairs", "heritage-watches"}
    # casadecor keeps policies inline on index (bilingual completeness test)

    pages: dict[str, str] = {
        "index": PRODUCTS[slug],
        "about": ABOUT[slug],
    }
    ship_days = "1–2" if slug != "quickdrop-gadgets" else "5–10"
    delivery = {"maya-ceramics": "1–2 weeks (made to order)",
                "quickdrop-gadgets": "4–6 weeks from partner facilities"}.get(slug, "3–5 days")
    if complete:
        pages["policies"] = (
            REFUND_OK
            + SHIPPING_OK.format(ship_days=ship_days, delivery=delivery)
            + TERMS_OK.format(jurisdiction=m.get("country", "US"))
        )
        pages["contact"] = CONTACT_FULL.format(
            domain=domain, phone="(555) 010-" + str(rng.randint(1000, 9999)),
            address="See about page for our address.",
        ) if slug != "bloom-stem" else CONTACT_EMAIL_ONLY.format(domain=domain)
        nav_pages += ["policies", "contact"]
    elif partial:
        if slug == "technest-deals":
            pages["policies"] = "<h2>Refunds</h2><p>Contact us about refunds.</p>"
            pages["contact"] = CONTACT_EMAIL_ONLY.format(domain=domain)
            nav_pages += ["policies", "contact"]
        elif slug == "flashfone-repairs":
            pages["contact"] = CONTACT_FULL.format(
                domain=domain, phone="(612) 555-0142", address="88 Lyndale Ave S")
            nav_pages += ["contact"]
        else:  # heritage-watches: elegant but thin
            pages["contact"] = CONTACT_EMAIL_ONLY.format(domain=domain)
            nav_pages += ["contact"]
    # quickdrop: index+about only, no policy pages at all

    nav = " · ".join(f'<a href="{p}.html">{p}</a>' for p in nav_pages)
    for pname, body in pages.items():
        html = PAGE.format(title=f"{m['name']} — {pname}", name=m["name"], nav=nav,
                           main=body, footer=footer)
        (d / f"{pname}.html").write_text(html)


def build_reviews(m: dict, rng: random.Random) -> None:
    slug = m["slug"]
    bank = REVIEWS.get(slug, [])
    out = FIX / "reviews" / f"{slug}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    total = sum(w for w, _, _ in bank)
    start = date(2025, 7, 15)
    if bank:
        pool = [(r, t) for w, r, t in bank for _ in range(w)]
        rng.shuffle(pool)
        for _i, (rating, text) in enumerate(pool):
            # urban-threads: complaints concentrate in the recent half
            if slug == "urban-threads-outlet":
                recent = rating <= 2
                day = rng.randint(200, 350) if recent else rng.randint(0, 199)
            else:
                day = rng.randint(0, 350)
            rows.append({"date": str(start + timedelta(days=day)),
                         "rating": rating, "text": text})
        rows.sort(key=lambda r: r["date"])
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "rating", "text"])
        w.writeheader()
        w.writerows(rows)
    _ = total


def build_whois(m: dict) -> None:
    out = FIX / "whois" / f"{m['slug']}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    import json

    out.write_text(json.dumps(
        {"domain_age_days": m["domain_age_days"], "mx_present": True,
         "tls_ok": m["slug"] != "quickdrop-gadgets", "reachable": True}, indent=1))


def main() -> None:
    cfg = yaml.safe_load(open(REPO / "config.yaml"))
    manifest = yaml.safe_load(open(FIX / "manifest.yaml"))["merchants"]
    rng = random.Random(cfg["seed"])
    for m in manifest:
        build_site(m, rng)
        build_reviews(m, rng)
        build_whois(m)
    print(f"built fixtures for {len(manifest)} merchants")


if __name__ == "__main__":
    main()
