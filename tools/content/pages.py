"""Guide and info pages: cost guide, about, reviews, gallery, 404."""
import html
from .services import P, UL, H3, L

# Verbatim Google Business Profile reviews. Do not edit wording, even where a
# reviewer wrote "Banana Floors, LLC". The profile aggregate is 5.0 from 8
# reviews. The list view did not show per-review stars; every review is part of
# that aggregate, so each card and Review node uses ratingValue 5.
# Relative dates are shown as collected. No absolute dates are invented.
GOOGLE_REVIEWS = [
    {
        "name": "Slavic Stasyuk",
        "when": "a month ago",
        "featured": True,
        "text": "\n\n".join((
            "Peter and his team at Banana Floors did an exceptional job on the hardwood floors in our new home. Our designer recommended them, and after seeing the finished product, we completely understand why.",
            "We installed wide-plank Monarch oak throughout the house, including a herringbone pattern in the entry that required a high level of precision and attention to detail. We are extremely particular when it comes to craftsmanship and finishes, and Peter and his team absolutely delivered. The layout, cuts, transitions, and overall installation were beautifully done.",
            "We've worked with a lot of contractors throughout our home build, and Banana Floors has genuinely been one of the best teams we've worked with. They were professional, skilled, dependable, and clearly take pride in the quality of their work.",
            "The hardwood is one of the standout features of our home, and we couldn't be happier with how everything turned out. We would highly recommend Peter and his team to anyone looking for a truly high-quality hardwood flooring installer.",
        )),
    },
    {
        "name": "Yana Tsurkan",
        "when": "3 weeks ago",
        "text": "First off amazing customer service and second professionals! They answered all my questions and concerns right off the bat and didn't pressure me when I needed to think about it and commit.  They were quick clean!!! So happy we went with Banana Floors!!! Would recommend to family and friends!",
    },
    {
        "name": "PDX_R3",
        "when": "3 weeks ago",
        "text": "Banana Floors did a fantastic job on our home's flooring, from the subfloor to engineered hardwood and baseboards. Peter and his crew are skilled and pay close attention to detail. Highly recommend!",
    },
    {
        "name": "Alex B",
        "when": "a month ago",
        "text": "Absolutely impressed with Banana Floors, LLC! The flooring turned out amazing and completely transformed the space. The quality of the work is excellent, everything looks clean and professionally done, and I couldn't be happier with the final result. I'm so excited with how it turned out. Highly recommend Banana Floors, LLC to anyone looking for great flooring work!",
    },
    {
        "name": "Richard Rusnak",
        "when": "a month ago",
        "text": "We hired Banana as part of a large remodel and had them installed hardwood flooring. They did excellent work and reasonably priced. Will use them again in the future.",
    },
    {
        "name": "Eugene Mikityuk",
        "when": "a month ago",
        "text": "My go to provider. Always knows what to do, and I can trust him with the costs.  5/5",
    },
    {
        "name": "Tony Mikityuk",
        "when": "a month ago",
        "text": "Reliable crew - quality work - good value pricing",
    },
    {
        "name": "Craw Drago",
        "when": "a month ago",
        "text": "Good price and great quality. What else could you ask for?",
    },
]
assert len(GOOGLE_REVIEWS) == 8


def build(c):
    page, bc, bld, faq_html, faq_ld = c["page"], c["breadcrumb_html"], c["breadcrumb_ld"], c["faq_html"], c["faq_ld"]
    PR, money, SITE, PHONE, TEL, CCB, GBP = c["PRICING"], c["money"], c["SITE"], c["PHONE"], c["TEL"], c["CCB"], c["GBP"]
    out = []

    # ---------------------------------------------------------- cost guide
    url = "/flooring-installation-cost-portland.html"
    trail = [("Home", "/"), ("Flooring installation cost guide", url)]
    def material_cost(key, sqft, waste=0.10, tier=None):
        t = PR[key]
        lo, hi = (t[tier] if tier else (t["Entry"][0], t["Premium"][1]))
        q = sqft * (1 + waste)
        return q, lo * q, hi * q
    names = {"LVP / Vinyl": "LVP", "Laminate": "Laminate", "Engineered Wood": "Engineered wood",
             "Solid Hardwood": "Solid hardwood", "Carpet": "Carpet", "Tile": "Tile"}
    rows = ""
    for k in PR:
        q, lo, hi = material_cost(k, 500, tier="Mid-range")
        rows += f"<tr><td>{names[k]}</td><td>{money(PR[k]['Mid-range'][0])}–{money(PR[k]['Mid-range'][1])}</td><td>{q:,.0f} sq ft</td><td>{money(lo)}–{money(hi)}</td></tr>"
    ex_table = ('<div class="table-wrap"><table class="price-table"><thead><tr><th scope="col">Material</th><th scope="col">Mid-range / sq ft</th>'
                '<th scope="col">Quantity to buy</th><th scope="col">Material budget</th></tr></thead><tbody>' + rows + "</tbody></table></div>"
                '<p class="note">Example: 500 sq ft of floor plus a 10% waste allowance (550 sq ft purchased), using the mid-range tier from the Price Guide. Material only.</p>')
    rq, rlo, rhi = material_cost("Carpet", 144, tier="Entry")
    kq, klo, khi = material_cost("LVP / Vinyl", 200, tier="Mid-range")
    bq, blo, bhi = material_cost("Tile", 60, waste=0.15, tier="Mid-range")
    examples = UL(
        f"<strong>12 × 12 ft bedroom, entry-level carpet:</strong> 144 sq ft + 10% waste = {rq:,.0f} sq ft → {money(rlo)}–{money(rhi)} in material",
        f"<strong>200 sq ft kitchen, mid-range LVP:</strong> 200 sq ft + 10% waste = {kq:,.0f} sq ft → {money(klo)}–{money(khi)} in material",
        f"<strong>60 sq ft bathroom, mid-range tile with 15% waste for cuts:</strong> {bq:,.0f} sq ft → {money(blo)}–{money(bhi)} in material")
    faqs = [
        ("How much does flooring installation cost in Portland?", "It depends on the material, the size of the job and the work around it: removal, subfloor preparation, stairs, trim and transitions. Use the Price Guide for material ranges and request a free preliminary quote for installation."),
        ("Why don't you list installation prices per square foot?", "Installation cost varies widely with removal, subfloor condition, stairs, room layout and transitions. We review your rooms, measurements and photos and give a preliminary quote, then verify the scope on site."),
        ("How much extra flooring should I buy for waste?", "A 10% allowance is common for straightforward rooms. Diagonal or herringbone layouts, many small rooms, or tile with lots of cuts may need 15%. Follow the manufacturer's guidance for your product."),
        ("Do the price ranges include tax and delivery?", "No. The ranges are material-only planning estimates and exclude taxes, delivery, underlayment, adhesives, trim, transitions, removal, preparation and installation."),
        ("What's the cheapest flooring to install?", "By material cost, laminate, entry-level carpet and entry-level LVP have the lowest ranges in our Price Guide. Total cost also depends on removal and preparation, which can matter more than the material."),
    ]
    body = bc(trail) + f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">Portland Metro · Planning guide</div>
<h1>Flooring installation cost in Portland: what goes into a quote</h1>
<p class="lead">A flooring quote has more parts than the price on the box. This guide uses the material ranges from our <a class="inline-link" href="/flooring-prices.html">Price Guide</a> to show how a budget comes together, and explains the installation items that change from home to home.</p>
<div class="trust-row"><span>Oregon CCB {CCB}</span><span>Material ranges updated with the Price Guide</span><span>Free preliminary quotes</span></div>
<div class="actions"><a class="btn" href="/flooring-prices.html#calculator">Open the material calculator</a><a class="btn secondary" href="/#estimate">Request a free estimate</a></div></div></section>
<section class="prose"><h2>The five parts of a flooring budget</h2>
{UL("<strong>Material:</strong> the flooring itself, plus a waste allowance for cuts and pattern matching",
    "<strong>Installation supplies:</strong> underlayment or pad, vapor barrier, adhesive, fasteners, grout and thinset for tile",
    "<strong>Removal and disposal:</strong> taking out the existing floor and hauling it away (" + L('/flooring/flooring-removal-portland.html', 'flooring removal') + ")",
    "<strong>Preparation:</strong> fixing squeaks, flattening high and low spots, replacing damaged subfloor (" + L('/flooring/subfloor-prep-floor-leveling-portland.html', 'subfloor prep and leveling') + ")",
    "<strong>Installation and finishing:</strong> laying the floor, plus " + L('/flooring/baseboard-trim-installation-portland.html', 'baseboards, transitions') + " and " + L('/flooring/stair-flooring-installation-portland.html', 'stairs'))}
<p>The Price Guide covers only the first part. The rest depends on your home, which is why we quote installation after reviewing your rooms.</p></section>
<section><div class="eyebrow">Material ranges</div><h2>Flooring material prices per square foot</h2>{c["price_table"]()}</section>
<section class="prose"><h2>Example material budgets</h2><p>Here is what the mid-range tier looks like for a 500 sq ft project, and a few common room sizes. These are material-only figures calculated from the Price Guide ranges.</p>{ex_table}{examples}</section>
<section class="prose"><h2>What changes the installation side of a quote</h2>
{H3("Removal")}<p>Carpet comes up quickly; glued vinyl, nailed wood and mortar-set tile take much longer. Older resilient flooring and adhesives may need testing before removal.</p>
{H3("Subfloor condition")}<p>Floating floors need a flat subfloor, wood floors need dry subfloors, and tile needs a stiff one. Some preparation is visible in photos; some only shows once the old floor is up.</p>
{H3("Layout and rooms")}<p>Many small rooms, closets, hallways and doorways mean more cuts and transitions than one open room of the same size. Diagonal and herringbone layouts add labor and waste.</p>
{H3("Stairs")}<p>Stairs are priced per step because each tread and riser is fit individually.</p>
{H3("Furniture, appliances and access")}<p>Moving furniture, disconnecting appliances, stairs to the work area and parking all affect time on site.</p>
{H3("Product requirements")}<p>Some products require specific underlayments, vapor barriers or adhesives to keep the manufacturer's warranty. We follow the manufacturer's installation instructions. Banana Floors installation and workmanship are covered by a 1-year warranty. Flooring materials are covered by the manufacturer's warranty, commonly about 10–25 years, and the length varies by product.</p></section>
<section class="prose"><h2>How to get an accurate quote</h2>
{UL("Measure each room (length × width) and note closets and hallways", "Take photos of each room, doorways, the current floor and any stairs", "Tell us the age of your home and what is under the current floor, if you know", "Choose a material and tier in the Price Guide, or tell us you are undecided", "Send it all through the estimate form or by text to " + PHONE)}
<p>We send a preliminary quote, then verify measurements and site conditions in person before scheduling.</p></section>
<section><div class="eyebrow">Compare materials</div><h2>Flooring installation guides</h2>{c["service_links"]()}</section>
{faq_html(faqs, "Flooring cost questions")}
{c["cta_box"]("Ready for a real number?")}'''
    # datePublished: cost guide first shipped 2026-10-15 (generator 8ed9e69, page ccfe673).
    # dateModified: last prose edit 2026-10-25 (warranty wording, 35b3743). Adding these
    # fields does not change the article body, so dateModified stays on that edit.
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": "Flooring installation cost in Portland: what goes into a quote",
               "url": SITE + url, "mainEntityOfPage": SITE + url, "image": SITE + "/images/banana-floors-share-r31.jpg",
               "datePublished": "2026-10-15", "dateModified": "2026-10-25",
               "author": {"@id": SITE + "/#business"},
               "publisher": {"@id": SITE + "/#business"}, "about": "Flooring installation cost"},
              faq_ld(faqs), bld(trail)]
    out.append(page(url, "Flooring Installation Cost Portland, OR | Banana Floors",
                    "What flooring installation costs in Portland: material ranges per sq ft, example budgets and the removal, prep and labor items in every quote.", body, schema,
                    current="/flooring-installation-cost-portland.html", og_type="article"))

    # ---------------------------------------------------------- about
    url = "/about.html"
    trail = [("Home", "/"), ("About", url)]
    body = bc(trail) + f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">About Banana Floors</div>
<h1>About Banana Floors, a Portland flooring contractor</h1>
<p class="lead">Banana Floors is a Portland-area flooring installation company. We install hardwood, engineered wood, LVP, laminate, tile and carpet in homes and businesses across the Portland, OR metro, including Vancouver, WA, with removal and floor preparation when needed.</p>
<div class="trust-row"><span>Insured, bonded &amp; licensed · Oregon CCB {CCB}</span><span>Residential &amp; commercial</span><span>Free preliminary estimates</span></div></div></section>
<section class="prose"><h2>How we work</h2>
<p>Banana Floors is built around making flooring projects easier to plan. Most people shopping for new floors want two answers early: what the material will cost, and what the installation will involve. That is why the site includes a material <a href="/flooring-prices.html">Price Guide</a> and a <a href="/flooring-installation-cost-portland.html">cost guide</a>, and why every quote separates material from installation, removal and preparation.</p>
{UL("<strong>Simple estimates:</strong> clear scope and realistic expectations",
    "<strong>Detail-focused installation:</strong> clean cuts, transitions and final cleanup",
    "<strong>Practical material guidance:</strong> options that fit the project and the budget",
    "<strong>Verified before scheduling:</strong> measurements and site conditions are confirmed in person")}</section>
<section class="prose"><h2>Our process</h2>
<ol><li><strong>Choose and price:</strong> browse floors and check material ranges.</li><li><strong>Send details:</strong> square footage, photos and project location.</li><li><strong>Get a preliminary quote:</strong> we review your scope.</li><li><strong>Verify and confirm:</strong> measurements and site conditions.</li><li><strong>Schedule and install:</strong> we lock in the date and get it done.</li></ol></section>
<section class="prose"><h2>Licensing</h2><p>Banana Floors is a DBA of Apex Builders, Inc and part of the Apex Builders, Inc family. Banana Floors is insured, bonded and licensed under Oregon CCB {CCB}. You can look up any Oregon contractor's license on the <a href="https://search.ccb.state.or.us/search/" target="_blank" rel="noopener">Oregon CCB license search ↗</a>.</p>
<h3>Warranty</h3><p>Banana Floors installation and workmanship are covered by a 1-year warranty. Flooring materials are covered by the manufacturer's warranty, commonly about 10–25 years, and the length varies by product.</p></section>
<section><div class="eyebrow">What we install</div><h2>Flooring services</h2>{c["service_links"]()}</section>
<section><div class="eyebrow">Where we work</div><h2>Service areas</h2>{c["city_links"]()}</section>
{c["cta_box"]("Talk to us about your floors.")}'''
    schema = [{"@context": "https://schema.org", "@type": "AboutPage", "url": SITE + url, "name": "About Banana Floors", "about": {"@id": SITE + "/#business"}}, bld(trail)]
    out.append(page(url, "About Banana Floors | Portland Flooring Contractor",
                    "Banana Floors is a Portland-area flooring installation company (Oregon CCB 209244) serving the Portland–Vancouver metro. How we work.", body, schema, current="/about.html"))

    # ---------------------------------------------------------- reviews (indexable: real Google reviews only)
    url = "/reviews.html"
    trail = [("Home", "/"), ("Reviews", url)]

    def review_cards():
        cards = []
        for r in GOOGLE_REVIEWS:
            paras = "".join(f"<p>{html.escape(part)}</p>" for part in r["text"].split("\n\n"))
            featured = " is-featured" if r.get("featured") else ""
            when = f'<span class="review-when">{html.escape(r["when"])}</span>' if r.get("when") else ""
            cards.append(
                f'<article class="review-card{featured}">'
                f'<div class="review-stars" role="img" aria-label="5 out of 5 stars"><span aria-hidden="true">★★★★★</span></div>'
                f"<blockquote>{paras}</blockquote>"
                f'<footer class="review-by"><cite>{html.escape(r["name"])}</cite>'
                f'<a href="{GBP}" target="_blank" rel="noopener">Google</a>{when}</footer>'
                f"</article>"
            )
        return "".join(cards)

    # datePublished is omitted. The page only stores relative Google labels
    # ("a month ago", "3 weeks ago"), which are not calendar dates. Do not invent them.
    review_nodes = [{
        "@type": "Review",
        "author": {"@type": "Person", "name": r["name"]},
        "reviewBody": r["text"],
        "reviewRating": {"@type": "Rating", "ratingValue": 5, "bestRating": 5},
        "publisher": {"@type": "Organization", "name": "Google"},
    } for r in GOOGLE_REVIEWS]
    business_ld = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE + "/#business",
        "name": "Banana Floors",
        "legalName": c["LEGAL_NAME"],
        "parentOrganization": {"@type": "Organization", "name": c["LEGAL_NAME"]},
        "url": SITE + "/",
        "telephone": "+1-503-421-1730",
        "image": c["BUSINESS_IMAGE"],
        "address": c["BUSINESS_ADDRESS"],
        "sameAs": [GBP],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": 5.0,
            "reviewCount": 8,
            "bestRating": 5,
        },
        "review": review_nodes,
    }
    body = bc(trail) + f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">Reviews on Google</div>
<h1>Banana Floors reviews</h1>
<p class="lead">These comments are from our Google Business Profile, where Banana Floors is rated 5.0 from 8 reviews. Read them here, then open Google for the full profile or to leave your own.</p>
<div class="review-summary">
  <div class="review-summary-copy">
    <p class="review-score"><span class="review-num">5.0</span><span class="review-stars" role="img" aria-label="Rated 5.0 out of 5 on Google"><span aria-hidden="true">★★★★★</span></span></p>
    <p class="review-count">5.0 from 8 reviews</p>
  </div>
  <a class="btn" href="{GBP}" target="_blank" rel="noopener">Read all reviews on Google ↗</a>
</div>
<div class="actions"><a class="btn secondary" href="/#estimate">Request a free estimate</a></div></div></section>
<section class="review-list" aria-labelledby="review-list-heading"><h2 id="review-list-heading">What customers say</h2>
<div class="review-grid">{review_cards()}</div></section>
<section class="prose"><h2>Had us install your floors?</h2><p>Reviews help Portland-area homeowners choose a contractor, and they help us improve. If you have a minute, please share your experience on <a href="{GBP}" target="_blank" rel="noopener">Google</a>.</p></section>
{c["cta_box"]()}'''
    out.append(page(url, "Reviews | Banana Floors",
                    "Read real Google reviews of Banana Floors, a Portland-area flooring installer. Rated 5.0 from 8 reviews.",
                    body, [business_ld, bld(trail)], current="/reviews.html", extra_css=("/reviews-r35.css",)))

    # ---------------------------------------------------------- gallery (indexable; style visualizations, not completed jobs)
    url = "/gallery.html"
    trail = [("Home", "/"), ("Gallery", url)]
    shots = [
        ("hardwood", "Hardwood look", "/flooring/hardwood-flooring-portland.html",
         "Style visualization of hardwood flooring in a living room. Not a photograph of a completed Banana Floors job."),
        ("lvp", "LVP look", "/flooring/lvp-flooring-portland.html",
         "Style visualization of luxury vinyl plank in a kitchen. Not a photograph of a completed Banana Floors job."),
        ("laminate", "Laminate look", "/flooring/laminate-flooring-portland.html",
         "Style visualization of laminate flooring in a home office. Not a photograph of a completed Banana Floors job."),
        ("tile", "Tile look", "/flooring/tile-flooring-portland.html",
         "Style visualization of tile flooring in a laundry room. Not a photograph of a completed Banana Floors job."),
        ("carpet", "Carpet look", "/flooring/carpet-installation-portland.html",
         "Style visualization of carpet in a living room. Not a photograph of a completed Banana Floors job."),
        ("engineered", "Engineered wood look", "/flooring/engineered-wood-flooring-portland.html",
         "Style visualization of engineered wood in a dining room. Not a photograph of a completed Banana Floors job."),
    ]
    figs, images_ld = "", []
    for key, cap, href, desc in shots:
        figs += (f'<figure>{c["img_tag"](key, eager=False, sizes="(max-width: 520px) calc(100vw - 36px), (max-width: 800px) 50vw, 360px")}'
                 f'<figcaption><a href="{href}">{html.escape(cap)}</a> · style visualization</figcaption></figure>')
        base = c["IMAGES"][key][0]
        images_ld.append({"@type": "ImageObject", "contentUrl": SITE + f"/images/{base}-r19.webp",
                          "caption": cap, "description": desc})
    gallery_ld = {"@context": "https://schema.org", "@type": "ImageGallery", "@id": SITE + url + "#gallery",
                  "name": "Flooring style gallery",
                  "description": "Style visualizations of hardwood, LVP, laminate, tile, carpet and engineered wood. These are not photographs of completed Banana Floors jobs.",
                  "url": SITE + url, "about": {"@id": SITE + "/#business"}, "image": images_ld}
    body = bc(trail) + f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">Style gallery</div>
<h1>Flooring style gallery</h1>
<p class="lead">These images are style visualizations for comparing flooring looks. They are not photographs of finished Banana Floors jobs. Product colors and finishes vary.</p></div></section>
<section><h2>Flooring styles</h2><div class="gallery-grid">{figs}</div></section>
<section class="prose"><h2>Style visualizations, not job photos</h2>
<p>Every image on this page is a style visualization. It is a typical room put together so you can compare color, grain, plank width and how a floor sits in a space. These are not photographs of finished Banana Floors jobs. Colors and finishes vary by brand, dye lot and the light in the room. Use the pictures to narrow a direction, then open the installation page for how that floor is actually put in.</p>
<h3>Match a look to a floor we install</h3>
<p>{L("/flooring/hardwood-flooring-portland.html", "Solid hardwood")} is the living-room look: wide planks, visible grain and a finish meant to stay. In older Portland bungalows an original fir or oak floor is sometimes worth {L("/flooring/hardwood-floor-refinishing-portland.html", "refinishing")} instead of covering. {L("/flooring/engineered-wood-flooring-portland.html", "Engineered wood")}, shown in the dining scene, has a real wood surface on a layered core, so it stays more stable when indoor humidity swings between a wet winter and a dry heated summer.</p>
<p>{L("/flooring/lvp-flooring-portland.html", "Luxury vinyl plank")} is the kitchen visualization, a wood look that handles spills and a basement slab. We install click-lock and glue-down LVP and talk through wear layer and thickness before you buy. {L("/flooring/laminate-flooring-portland.html", "Laminate")}, in the office scene, is the crisp printed-wood surface at a lower material cost, floated over a flat subfloor. {L("/flooring/tile-flooring-portland.html", "Tile")} is the laundry-room look and the usual choice for baths, mudrooms and other wet rooms. {L("/flooring/carpet-installation-portland.html", "Carpet")} is the soft living-room look still used in bedrooms and on stairs, with pad and transitions planned where it meets a hard floor.</p>
<p>When a style is close, check material ranges in the {L("/flooring-prices.html", "Price Guide")} and what else goes into a quote in the {L("/flooring-installation-cost-portland.html", "installation cost guide")}. We install these floors in Portland and the nearby cities on this site: Gresham, Happy Valley, Clackamas, Oregon City, Beaverton, Tigard, Lake Oswego and Vancouver, WA.</p></section>
<section><div class="eyebrow">Explore</div><h2>Learn about each floor</h2>{c["service_links"]()}</section>
{c["cta_box"]()}'''
    out.append(page(url, "Flooring Style Gallery | Banana Floors",
                    "Style visualizations of hardwood, LVP, laminate, tile, carpet and engineered wood. Not job photos. Compare a look, then open the installation page.",
                    body, [gallery_ld, bld(trail)], current="/gallery.html"))

    # ---------------------------------------------------------- thank-you (form _next target)
    body = f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">Thank you for reaching out</div>
<h1>Your estimate request has been submitted.</h1>
<p class="lead">We’ll review your project details and contact you using the information you provided. Final pricing follows a review of your measurements and site conditions.</p>
<p>Have a question in the meantime? Call or text <a class="inline-link" href="tel:{TEL}">{PHONE}</a>.</p>
<div class="actions"><a class="btn" href="/">Back to home</a><a class="btn secondary" href="/flooring-prices.html">Explore flooring prices</a></div></div></section>
<section><h2>While you wait: plan your floor</h2>{c["service_links"]()}</section>'''
    page("/thank-you.html", "Thank You | Banana Floors", "Your Banana Floors estimate request has been submitted.", body, (), robots="noindex,follow")

    # ---------------------------------------------------------- 404
    body = f'''<section class="hero" style="grid-template-columns:1fr"><div><div class="eyebrow">Page not found</div>
<h1>Sorry, we couldn't find that page.</h1>
<p class="lead">The page may have moved. Try one of these instead, or call or text <a class="inline-link" href="tel:{TEL}">{PHONE}</a>.</p>
<div class="actions"><a class="btn" href="/">Go to the homepage</a><a class="btn secondary" href="/flooring-prices.html">Open the Price Guide</a></div></div></section>
<section><h2>Flooring services</h2>{c["service_links"]()}</section>
<section><h2>Service areas</h2>{c["city_links"]()}</section>'''
    page("/404.html", "Page Not Found | Banana Floors", "The page you were looking for could not be found. Browse Banana Floors flooring services and service areas.", body, (), robots="noindex,follow")

    return out
