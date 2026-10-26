#!/usr/bin/env python3
"""Banana Floors static page builder (r31).

Generates the service, service-area, guide and info pages from the content
modules in tools/content/. The homepage (index.html), price guide
(flooring-prices.html) and thank-you page stay hand-edited.

Run from the repo root:  python3 tools/build.py
Then commit the regenerated .html files and sitemap.xml.
"""
import html, json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from content import services, cities, pages  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://bananafloors.com"
PHONE = "(503) 421-1730"
TEL = "+15034211730"
CCB = "209244"
GBP = "https://maps.app.goo.gl/qtWVZ1QcHdKnH6fg6"
TODAY = datetime.date.today().isoformat()
SHARE = SITE + "/images/banana-floors-share-r31.jpg"
LOGO = "/images/banana-floors-wordmark-r31.webp"

# Material ranges come from the same file the price guide uses.
_js = open(os.path.join(ROOT, "material-pricing-r20.js"), encoding="utf-8").read()
PRICING = {}
for name, body in re.findall(r"'([^']+)'\s*:\s*\{([^}]*)\}", _js):
    tiers = dict((k.strip("'"), (float(a), float(b))) for k, a, b in re.findall(r"('?[\w-]+'?)\s*:\s*\[([\d.]+),\s*([\d.]+)\]", body))
    PRICING[name] = tiers
assert len(PRICING) == 6, PRICING

def money(x):
    return "${:,.2f}".format(x).replace(".00", "") if x < 100 else "${:,.0f}".format(x)

def full_range(key):
    t = PRICING[key]
    return t["Entry"][0], t["Premium"][1]

IMAGES = {
    "hardwood": ("hardwood-living-room", "Hardwood flooring in a living room"),
    "lvp": ("kitchen-approved", "Luxury vinyl plank flooring in a kitchen"),
    "laminate": ("laminate-office", "Laminate flooring in a home office"),
    "tile": ("laundry-approved", "Tile flooring in a laundry room"),
    "carpet": ("carpet-living-room", "Carpet in a living room"),
    "engineered": ("engineered-wood-dining", "Engineered wood flooring in a dining room"),
}

def img_tag(key, alt=None, eager=True, sizes="(max-width: 800px) calc(100vw - 44px), 520px"):
    base, default_alt = IMAGES[key]
    alt = alt or default_alt
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="/images/{base}-r19.webp" alt="{html.escape(alt)}" width="1536" height="1024" {load} decoding="async" '
            f'srcset="/images/{base}-r19-small.webp 768w, /images/{base}-r19.webp 1536w" sizes="{sizes}">')

# ---------------------------------------------------------------- registry
SERVICE_LIST = services.SERVICES
CITY_LIST = cities.CITIES

def service_url(s): return f"/flooring/{s['slug']}.html"
def city_url(c): return f"/locations/{c['slug']}.html"

def nav_links(current=None):
    items = [("/#services", "Services"), ("/#areas", "Areas"), ("/flooring-prices.html", "Price Guide"),
             ("/flooring-installation-cost-portland.html", "Cost Guide"), ("/about.html", "About"), ("/reviews.html", "Reviews")]
    out = []
    for href, label in items:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(out)

THEME_TOGGLE = ('<button class="theme-toggle" type="button" data-theme-toggle hidden aria-label="Switch to dark mode" title="Switch to dark mode">'
    '<svg class="theme-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 13A8.6 8.6 0 0 1 11 3.5 8.7 8.7 0 1 0 20.5 13Z"/></svg>'
    '<svg class="theme-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.4 1.4m11.2 11.2L19 19M5 19l1.4-1.4M17.6 6.4 19 5"/></svg>'
    '<span data-theme-label>Dark</span></button>')

def logo(cls="brand-logo", alt="Banana Floors"):
    return (f'<span class="logo-frame"><img class="{cls}" src="{LOGO}" alt="{alt}" width="440" height="55">'
            f'<img class="{cls} logo-dark-part" src="{LOGO}" alt="" aria-hidden="true" width="440" height="55"></span>')

_SVG = '<svg class="ico" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
ICONS = {
    "shield": _SVG.format('<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>'),
    "tag": _SVG.format('<path d="M3 12V4a1 1 0 011-1h8l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>'),
    "star": _SVG.format('<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8L3.5 9.7l5.9-.9z"/>'),
    "home": _SVG.format('<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>'),
    "layers": _SVG.format('<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>'),
    "phone": _SVG.format('<path d="M5 3h4l2 5-3 2a12 12 0 006 6l2-3 5 2v4a2 2 0 01-2 2A18 18 0 013 5a2 2 0 012-2z"/>'),
    "clock": _SVG.format('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
}

def header(current=None):
    return (f'<a class="skip-link" href="#main">Skip to content</a><header class="site-nav"><div class="site-nav-inner">'
            f'<a class="site-brand" href="/" aria-label="Banana Floors home">{logo()}</a>'
            f'<nav class="site-links" aria-label="Main navigation">{nav_links(current)}</nav>'
            f'<div class="site-nav-actions"><a class="site-call" href="tel:{TEL}">Call {PHONE}</a>{THEME_TOGGLE}</div></div></header>')

def footer():
    svc = "".join(f'<li><a href="{service_url(s)}">{html.escape(s["nav"])}</a></li>' for s in SERVICE_LIST)
    area = "".join(f'<li><a href="{city_url(c)}">{html.escape(c["name"])}, {c["state"]}</a></li>' for c in CITY_LIST)
    return f'''<footer class="site-footer">
  <div class="footer-top">
    <details class="footer-dd"><summary>Flooring services <span class="dd-count">{len(SERVICE_LIST)}</span></summary><ul>{svc}</ul></details>
    <details class="footer-dd"><summary>Service areas <span class="dd-count">{len(CITY_LIST)}</span></summary><ul>{area}</ul></details>
    <nav class="footer-quick" aria-label="Footer"><a href="/flooring-prices.html">Price guide</a><a href="/flooring-installation-cost-portland.html">Cost guide</a><a href="/#estimate">Free estimate</a><a href="/about.html">About</a><a href="/reviews.html">Reviews</a><a href="/gallery.html">Gallery</a></nav>
  </div>
  <div class="footer-inner">
    <a class="footer-brand" href="/">{logo("footer-logo", "Banana Floors home")}</a>
    <div class="footer-info">
      <span><a class="footer-phone" href="tel:{TEL}">Call or text {PHONE}</a> · Oregon CCB {CCB}</span>
      <span><a class="footer-gbp" href="{GBP}" target="_blank" rel="noopener">Google profile ↗</a> · © <span id="year">{TODAY[:4]}</span> Banana Floors</span>
    </div>
  </div>
</footer>'''

BUSINESS_REF = {"@type": "HomeAndConstructionBusiness", "@id": SITE + "/#business", "name": "Banana Floors",
                "legalName": "Banana Floors", "url": SITE + "/", "telephone": "+1-503-421-1730"}

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"

def breadcrumb_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}

def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()

def breadcrumb_html(trail):
    parts = []
    for i, (n, u) in enumerate(trail):
        if i == len(trail) - 1:
            parts.append(f'<span aria-current="page">{html.escape(n)}</span>')
        else:
            parts.append(f'<a href="{u}">{html.escape(n)}</a>')
    return '<nav class="page-breadcrumb" aria-label="Breadcrumb">' + '<span aria-hidden="true"> / </span>'.join(parts) + "</nav>"

def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", strip_tags(t).lower()).strip("-")[:60]

def aside_card(sections, cta_label="Get a free estimate"):
    toc = "".join(f'<li><a href="#{slugify(h)}">{html.escape(strip_tags(h))}</a></li>' for h in sections)
    return (f'<aside class="article-aside" aria-label="Estimate and page contents"><div class="aside-card">'
            f'<p class="aside-title">Free preliminary estimate</p><p>Send your rooms, rough square footage and a few photos.</p>'
            f'<a class="btn" href="/#estimate">{cta_label}</a><a class="aside-phone" href="tel:{TEL}">{ICONS["phone"]}Call or text {PHONE}</a>'
            f'<p class="aside-meta">Oregon CCB {CCB} · Banana Floors</p></div>'
            f'<nav class="toc" aria-label="On this page"><p class="aside-title">On this page</p><ol>{toc}</ol></nav></aside>')

def prose_section(h2, content):
    return f'<section class="prose" id="{slugify(h2)}"><h2>{h2}</h2>{content}</section>'

def faq_html(faqs, heading, eyebrow="Questions"):
    items = "".join(f"<details><summary>{html.escape(q)}</summary><p>{a}</p></details>" for q, a in faqs)
    return f'<section class="planning-faq faq-list" id="{slugify(heading)}"><div class="eyebrow">{eyebrow}</div><h2>{heading}</h2><div class="planning-questions">{items}</div></section>'

def page(path, title, desc, body, schema=(), robots="index,follow,max-image-preview:large", current=None, og_type="website"):
    assert len(title) <= 62, (path, len(title), title)
    assert len(desc) <= 160, (path, len(desc), desc)
    canon = SITE + ("/" if path == "/index.html" else path)
    head = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{"" if path == "/404.html" else f'<link rel="canonical" href="{canon}">'}
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#ffd84d">
<link rel="icon" href="/favicon-r31.ico" sizes="any"><link rel="icon" href="/favicon-r21.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon-r21.png" sizes="180x180">
<meta property="og:site_name" content="Banana Floors">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SHARE}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Banana Floors: Portland flooring installation">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SHARE}">
<script src="/theme-r30.js"></script>
<link rel="stylesheet" href="/theme-r34.css">
<link rel="stylesheet" href="/page-r34.css">
{"".join(ld(s) for s in schema)}
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
</body>
</html>
'''
    out = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(head)
    return path

def cta_box(heading="Get a free preliminary quote.", text=None):
    text = text or ("Send your rooms, approximate square footage, current flooring and a few photos. "
                    "We review the scope, then verify measurements and site conditions before anything is scheduled.")
    return (f'<section class="cta-box"><h2>{heading}</h2><p>{text}</p><div class="actions">'
            f'<a class="btn" href="/#estimate">Request a free estimate</a><a class="btn secondary" href="tel:{TEL}">Call or text {PHONE}</a></div></section>')

def link_row(items, current=None):
    cur = ' aria-current="page"'
    return '<div class="links">' + "".join(
        f'<a href="{u}"{cur if u == current else ""}>{html.escape(n)}</a>' for n, u in items) + "</div>"

def service_links(current=None):
    return link_row([(s["nav"], service_url(s)) for s in SERVICE_LIST], current)

def city_links(current=None, only=None):
    lst = [c for c in CITY_LIST if (only is None or c["slug"] in only)]
    return link_row([(f'{c["name"]}, {c["state"]}', city_url(c)) for c in lst], current)

def price_table(keys=None):
    rows = []
    labels = {"LVP / Vinyl": ("LVP / vinyl plank", "/flooring/lvp-flooring-portland.html"),
              "Laminate": ("Laminate", "/flooring/laminate-flooring-portland.html"),
              "Engineered Wood": ("Engineered wood", "/flooring/engineered-wood-flooring-portland.html"),
              "Solid Hardwood": ("Solid hardwood", "/flooring/hardwood-flooring-portland.html"),
              "Carpet": ("Carpet", "/flooring/carpet-installation-portland.html"),
              "Tile": ("Tile", "/flooring/tile-flooring-portland.html")}
    for k in (keys or PRICING.keys()):
        t = PRICING[k]; lab, u = labels[k]
        rows.append(f'<tr><td><a href="{u}">{lab}</a></td>' + "".join(
            f"<td>{money(t[tier][0])}–{money(t[tier][1])}</td>" for tier in ("Entry", "Mid-range", "Premium")) + "</tr>")
    return ('<div class="table-wrap"><table class="price-table"><thead><tr><th scope="col">Material</th><th scope="col">Good · Entry</th>'
            '<th scope="col">Better · Mid-range</th><th scope="col">Best · Premium</th></tr></thead><tbody>' + "".join(rows) +
            '</tbody></table></div><p class="note">Material-only planning ranges per square foot from the <a class="inline-link" href="/flooring-prices.html">Banana Floors Price Guide</a>. '
            'Installation, removal, floor preparation, underlayment, trim, transitions, delivery and taxes are not included.</p>')

# ---------------------------------------------------------------- page types
def build_service(s):
    url = service_url(s)
    trail = [("Home", "/"), ("Flooring services", "/#services"), (s["nav"], url)]
    price = ""
    if s.get("price_key"):
        lo, hi = full_range(s["price_key"])
        price = f'<span>{ICONS["layers"]}Material {money(lo)}–{money(hi)}/sq ft</span>'
    hero = f'''{breadcrumb_html(trail)}
<section class="hero"><div><div class="eyebrow">{s["eyebrow"]}</div><h1>{s["h1"]}</h1><p class="lead">{s["intro"]}</p>
<div class="trust-row"><span>{ICONS["shield"]}Oregon CCB {CCB}</span><span>{ICONS["tag"]}Free preliminary estimates</span>{price}<a class="trust-gbp" href="{GBP}" target="_blank" rel="noopener">{ICONS["star"]}Google profile</a></div>
<div class="actions"><a class="btn" href="/#estimate">Get a free estimate</a><a class="btn secondary" href="/flooring-prices.html">See the material price guide</a></div></div>
<figure>{img_tag(s["image"], s.get("img_alt"))}<figcaption>Room visualization. Product colors and finishes vary.</figcaption></figure></section>'''
    points = "".join(f'<div class="point">{a}<span>{b}</span></div>' for a, b in s["points"])
    body = hero + f'<section><div class="eyebrow">At a glance</div><h2>{s["glance_h2"]}</h2><div class="grid">{points}</div></section>'
    if s.get("confirm"):
        body += f'<div class="callout"><p>{s["confirm"]}</p></div>'
    art, heads = "", []
    for h2, content in s["sections"]:
        art += prose_section(h2, content); heads.append(h2)
    if s.get("price_key") or s.get("show_prices"):
        keys = [s["price_key"]] if s.get("price_key") else s.get("price_keys")
        ph = s.get("price_h2", "Material price ranges"); heads.append(ph)
        art += f'<section class="table-section" id="{slugify(ph)}"><div class="eyebrow">Planning first</div><h2>{ph}</h2>{price_table(keys)}</section>'
    fh = s.get("faq_h2", f'{s["nav"]} questions'); heads.append(fh)
    art += faq_html(s["faqs"], fh)
    body += f'<div class="article-layout"><div class="article-body">{art}</div>{aside_card(heads)}</div>'
    body += (f'<div class="related-grid"><section class="related"><div class="eyebrow">Explore more</div><h2>Other flooring services</h2>{service_links(url)}</section>'
             f'<section class="related"><div class="eyebrow">Service areas</div><h2>{s["nav"]} across the Portland metro</h2><p>We work in Portland and nearby communities in Oregon, plus Vancouver, Washington.</p>{city_links()}</section></div>')
    body += cta_box()
    schema = [{"@context": "https://schema.org", "@type": "Service", "@id": SITE + url + "#service", "url": SITE + url,
               "name": s["schema_name"], "serviceType": s["schema_name"], "provider": BUSINESS_REF,
               "areaServed": [{"@type": "City", "name": f'{c["name"]}, {c["state"]}'} for c in CITY_LIST],
               "description": strip_tags(s["intro"])},
              faq_ld(s["faqs"]), breadcrumb_ld(trail)]
    return page(url, s["title"], s["desc"], body, schema)

def build_city(c):
    url = city_url(c)
    trail = [("Home", "/"), ("Service areas", "/#areas"), (f'{c["name"]}, {c["state"]}', url)]
    hero = f'''{breadcrumb_html(trail)}
<section class="hero"><div><div class="eyebrow">{c["name"]}, {c["state"]} · Flooring installation</div><h1>{c["h1"]}</h1><p class="lead">{c["intro"]}</p>
<div class="trust-row"><span>{ICONS["shield"]}Oregon CCB {CCB}</span><span>{ICONS["tag"]}Free preliminary estimates</span><span>{ICONS["layers"]}LVP · Wood · Laminate · Tile · Carpet</span><a class="trust-gbp" href="{GBP}" target="_blank" rel="noopener">{ICONS["star"]}Google profile</a></div>
<div class="actions"><a class="btn" href="/#estimate">Get a free {c["name"]} estimate</a><a class="btn secondary" href="tel:{TEL}">Call or text {PHONE}</a></div></div>
<figure>{img_tag(c["image"], c.get("img_alt"))}<figcaption>Room visualization, not a completed {c["name"]} project.</figcaption></figure></section>'''
    body = hero
    art, heads = "", []
    for h2, content in c["sections"]:
        art += prose_section(h2, content); heads.append(h2)
    hoods = "".join(f"<li>{html.escape(n)}</li>" for n in c["neighborhoods"])
    art += prose_section(c["hoods_h2"], f'<p>{c["hoods_intro"]}</p><ul class="hood-list">{hoods}</ul>'); heads.append(c["hoods_h2"])
    ph = f'Compare material prices before your {c["name"]} quote'; heads.append(ph)
    art += f'<section class="table-section" id="{slugify(ph)}"><div class="eyebrow">Planning first</div><h2>{ph}</h2>{price_table()}</section>'
    fh = f'{c["name"]} flooring questions'; heads.append(fh)
    art += faq_html(c["faqs"], fh)
    body += f'<div class="article-layout"><div class="article-body">{art}</div>{aside_card(heads, "Get a free " + c["name"] + " estimate")}</div>'
    body += (f'<div class="related-grid"><section class="related"><div class="eyebrow">Flooring we install in {c["name"]}</div><h2>{c["name"]} flooring services</h2>{service_links()}</section>'
             f'<section class="related"><div class="eyebrow">Nearby</div><h2>Other areas we serve near {c["name"]}</h2>{city_links(only=c["nearby"])}</section></div>')
    body += cta_box(f'Planning new floors in {c["name"]}?')
    schema = [{"@context": "https://schema.org", "@type": "Service", "@id": SITE + url + "#service", "url": SITE + url,
               "name": f'Flooring installation in {c["name"]}, {c["state"]}', "serviceType": "Flooring installation",
               "provider": BUSINESS_REF, "areaServed": {"@type": "City", "name": f'{c["name"]}, {c["state"]}'},
               "description": strip_tags(c["intro"])},
              faq_ld(c["faqs"]), breadcrumb_ld(trail)]
    return page(url, c["title"], c["desc"], body, schema)

def build_sitemap(paths):
    urls = "".join(f"  <url>\n    <loc>{SITE}{'/' if p == '/' else p}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n" for p in paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("<?xml version='1.0' encoding='utf-8'?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + urls + "</urlset>\n")

if __name__ == "__main__":
    ctx = dict(page=page, breadcrumb_html=breadcrumb_html, breadcrumb_ld=breadcrumb_ld, faq_html=faq_html, faq_ld=faq_ld,
               cta_box=cta_box, price_table=price_table, service_links=service_links, city_links=city_links, img_tag=img_tag,
               PRICING=PRICING, money=money, SERVICE_LIST=SERVICE_LIST, CITY_LIST=CITY_LIST, service_url=service_url,
               city_url=city_url, BUSINESS_REF=BUSINESS_REF, SITE=SITE, PHONE=PHONE, TEL=TEL, CCB=CCB, GBP=GBP, link_row=link_row)
    indexable = ["/", "/flooring-prices.html"]
    for s in SERVICE_LIST:
        indexable.append(build_service(s))
    for c in CITY_LIST:
        indexable.append(build_city(c))
    indexable += pages.build(ctx)
    build_sitemap(indexable)
    print(f"Built {len(indexable)} sitemap URLs")
