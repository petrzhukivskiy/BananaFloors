"""Service page content. Keep claims factual; anything Pete must confirm is listed in the PR."""

def P(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)

def UL(*items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def H3(t):
    return f"<h3>{t}</h3>"

L = lambda href, text: f'<a href="{href}">{text}</a>'
PRICES = L("/flooring-prices.html", "Price Guide")
COST = L("/flooring-installation-cost-portland.html", "installation cost guide")
SUBFLOOR = L("/flooring/subfloor-prep-floor-leveling-portland.html", "subfloor preparation and leveling")
REMOVAL = L("/flooring/flooring-removal-portland.html", "flooring removal")
STAIRS = L("/flooring/stair-flooring-installation-portland.html", "stair flooring")
TRIM = L("/flooring/baseboard-trim-installation-portland.html", "baseboards and transitions")
WATERPROOF = L("/flooring/waterproof-flooring-portland.html", "waterproof flooring")
REFINISH = L("/flooring/hardwood-floor-refinishing-portland.html", "hardwood floor refinishing")

SERVICES = [
# ------------------------------------------------------------------ LVP
dict(slug="lvp-flooring-portland", nav="LVP installation", image="lvp", price_key="LVP / Vinyl",
 title="LVP Flooring Installation Portland, OR | Banana Floors",
 desc="Luxury vinyl plank installed in Portland homes: click-lock or glue-down, subfloor prep, removal and transitions. See LVP prices and get a free quote.",
 eyebrow="Portland Metro · Luxury vinyl plank (LVP)",
 h1="LVP flooring installation in Portland, Oregon",
 intro="Luxury vinyl plank is one of the most practical floors for Portland kitchens, basements, rentals and busy family rooms. Banana Floors installs click-lock and glue-down LVP and helps you compare wear layer, thickness and core construction before you buy.",
 schema_name="Luxury vinyl plank (LVP) flooring installation",
 glance_h2="LVP basics to compare",
 points=[("$2–$7 / sq ft", "Material planning range"), ("4–8 mm", "Common total thickness"), ("8–20 mil", "Typical wear layers"), ("Click-lock or glue-down", "Two installation methods")],
 sections=[
  ("Why LVP works well in Portland homes", P(
    "Portland gets most of its rain between fall and spring, and that moisture comes into the house on shoes, dogs and umbrellas. Rigid-core LVP is built around a vinyl or stone-polymer core that does not swell when it gets wet the way wood-based products can, which is why many homeowners choose it for entries, kitchens, laundry rooms and finished basements.",
    "It also suits remodels where budget matters. LVP gives a wood or stone look at a lower material cost than most hardwood, it is quieter underfoot than tile, and worn planks can often be replaced individually. The trade-off is that LVP cannot be sanded and refinished like real wood: when the wear layer is used up, the floor is replaced.")),
  ("What to compare before you buy LVP", H3("Wear layer") + P(
    "The clear top layer protects the printed design. Residential products commonly range from about 8 to 20 mil. Thicker wear layers generally hold up better to pets, rolling chairs and heavy traffic; a 20 mil product is a sensible target for kitchens, hallways and rentals.") +
    H3("Core and total thickness") + P(
    "Rigid-core products (often labeled SPC or WPC) are stiffer and bridge small subfloor imperfections better than flexible vinyl, but no LVP hides a wavy floor. Total thickness of 4–8 mm is common; thicker is not automatically better if the core is soft.") +
    H3("Attached pad and underlayment") + P(
    "Many planks come with an attached pad. Some manufacturers allow or require a separate underlayment or vapor barrier over concrete; others void the warranty if you add one. We check the exact product's installation guide before the floor goes down.") +
    H3("Waterproof claims") + P(
    "Most rigid-core LVP is marketed as waterproof, but the seams and perimeter are not sealed like a shower pan. Standing water from a leaking dishwasher or toilet can still reach the subfloor. Read the warranty wording and see our " + WATERPROOF + " guide if water is your main concern.")),
  ("How we install LVP", H3("Click-lock floating floors") + P(
    "Most residential LVP is a floating click-lock floor. Planks lock to each other rather than to the subfloor, with an expansion gap at walls that is hidden by baseboard or shoe molding. Floating floors are sensitive to flatness, so we check the subfloor with a straightedge and plan any " + SUBFLOOR + " before installation.") +
    H3("Glue-down LVP") + P(
    "Glue-down (dry-back) vinyl is bonded to the subfloor. It is common in commercial spaces and large open areas, and it can be a good option where a floating floor would run too far without a transition. It needs a clean, flat, dry substrate and the correct adhesive for the product.") +
    H3("Kitchens, islands and heavy items") + P(
    "Many manufacturers do not allow floating floors to be pinned under cabinets or kitchen islands. If you are remodeling a kitchen, tell us whether cabinets are going in before or after the floor so the sequence matches the product requirements.")),
  ("What affects an LVP installation quote", UL(
    "Removal of existing carpet, laminate, vinyl or tile, and haul-away (" + REMOVAL + ")",
    "Subfloor condition: high spots, low spots, squeaks, or concrete moisture",
    "Number of rooms, closets and doorways, and how many " + TRIM + " are needed",
    "Stairs, which are priced separately (" + STAIRS + ")",
    "Moving furniture and appliances, and access to the work area") + P(
    "Use the " + PRICES + " to set a material budget, then read our " + COST + " for the other line items. Send us room measurements and photos for a preliminary quote; the final scope is verified before scheduling.")),
 ],
 faqs=[
  ("Is LVP waterproof?", "Most rigid-core LVP is marketed as waterproof, but product specifications and installation requirements vary by manufacturer. The planks resist water; seams and edges are not a sealed barrier. We recommend checking the exact product data before purchase."),
  ("What affects the cost of LVP installation?", "The installation method, existing floor removal, subfloor condition, stairs, and transitions affect the quote. Send room measurements and photos so we can review the scope alongside your material budget."),
  ("Can LVP be installed over my current flooring?", "That depends on the selected product and the condition of the existing floor. Send photos of the current surface, doorways and any uneven areas. We review whether removal is needed and identify preparation and transition work before confirming the installation scope."),
  ("Are baseboards and transitions included in my LVP quote?", "Let us know whether you want existing baseboards reused or replaced, and show where LVP meets tile, carpet or another floor. Those edges, door openings and any stairs should be included in the scope so you can compare complete installation quotes."),
  ("Can LVP go in a basement on concrete?", "Often, yes. LVP is one of the most common choices for basements. Concrete should be checked for moisture and flatness first, and the manufacturer may require a vapor barrier. We review the slab and the product instructions before confirming the scope."),
  ("How is the LVP installation schedule confirmed?", "We confirm timing after reviewing the rooms, removal and preparation, access, and material availability. Share any move-in date or rooms that need to remain usable. Product requirements and the agreed scope guide the schedule; the material-budget calculator does not set an installation date."),
 ]),
# ------------------------------------------------------------------ Hardwood
dict(slug="hardwood-flooring-portland", nav="Hardwood installation", image="hardwood", price_key="Solid Hardwood",
 title="Hardwood Floor Installation Portland, OR | Banana Floors",
 desc="Solid hardwood flooring installed across the Portland metro. Compare species and price ranges, plan prep and transitions, and request a free estimate.",
 eyebrow="Portland Metro · Solid hardwood",
 h1="Hardwood floor installation in Portland, Oregon",
 intro="Solid hardwood is the traditional choice for Portland homes, from older bungalows to newer two-story houses. Banana Floors installs solid hardwood and helps you compare species, width, finish and the preparation your subfloor needs before you commit.",
 schema_name="Solid hardwood flooring installation",
 glance_h2="Solid hardwood basics",
 points=[("$6–$15 / sq ft", "Material planning range"), ("Refinishable", "Can be sanded multiple times"), ("Nail-down", "Typical over a wood subfloor"), ("Acclimation", "Per manufacturer instructions")],
 sections=[
  ("Is solid hardwood right for your room?", P(
    "Solid hardwood is milled from a single piece of wood, usually around 3/4 inch thick. Because the whole board is wood, it can be sanded and refinished several times over its life, which is why many original floors in older Portland homes are still in use a century later. If you already have hardwood that looks worn, ask about " + REFINISH + " before replacing it.",
    "It is best suited to above-grade rooms with a wood subfloor: living and dining rooms, bedrooms, hallways and many kitchens. It is generally not recommended for below-grade basements or directly over concrete, and it is a poor fit for bathrooms or laundry rooms where water is likely. In those areas we usually suggest " + L("/flooring/engineered-wood-flooring-portland.html", "engineered wood") + ", LVP or tile.")),
  ("Choosing species, width and finish", H3("Species") + P(
    "Red oak and white oak are the most common choices and are widely available. Maple is harder and has a tighter, quieter grain. Hickory is very hard with dramatic color variation. Harder species resist dents better but can be more expensive and harder to sand.") +
    H3("Board width") + P(
    "Narrow strip flooring (around 2 1/4 inches) is classic in older homes; wider plank is popular in newer interiors. Wider boards show seasonal movement more, so product choice and moisture control matter more as width increases.") +
    H3("Prefinished or site-finished") + P(
    "Prefinished boards arrive with a factory finish and can usually be walked on soon after installation. Site-finished floors are sanded and coated in place, which allows custom stain colors and a flush surface but adds drying time. Tell us which you are considering so the scope matches.")),
  ("Moisture, acclimation and Portland's seasons", P(
    "Wood expands when the air is humid and shrinks when it is dry. In the Portland area, damp winters outdoors and heated, drier air indoors mean small seasonal gaps between boards are normal. Problems such as cupping usually trace back to moisture from below, often a crawlspace without an effective vapor barrier.",
    "Before installation, hardwood should acclimate according to the manufacturer's instructions, and the subfloor's moisture should be within the range the manufacturer specifies. We check moisture levels and let you know if a crawlspace or subfloor issue should be addressed first.")),
  ("How hardwood installation works", UL(
    "Review rooms, doorways, stairs and transitions, and confirm the product and quantity (including waste allowance)",
    "Remove existing flooring if needed (" + REMOVAL + ") and inspect the subfloor",
    "Fix squeaks, loose panels and flatness problems (" + SUBFLOOR + ")",
    "Install underlayment as specified, then nail down the boards with proper expansion space",
    "Fit " + TRIM + ", clean up and walk the finished floor with you") + P(
    "Stairs, custom borders and site finishing add time and cost. Use the " + PRICES + " for a material budget and our " + COST + " for the other parts of the project.")),
 ],
 faqs=[
  ("Can hardwood be installed over concrete or in a basement?", "Solid hardwood is generally not recommended below grade or directly over concrete because of moisture. Engineered wood, LVP or tile are usually better choices there. Check the manufacturer's requirements for your exact product."),
  ("How long should hardwood acclimate before installation?", "Follow the manufacturer's instructions for your product. Acclimation time depends on the product, the home's conditions and the measured moisture of the wood and subfloor, so there is no single number for every job."),
  ("What affects the cost of hardwood installation?", "Removal of the old floor, subfloor repairs, the number of rooms and transitions, stairs, board width, and whether the floor is prefinished or site-finished. Send measurements and photos and we will review the scope with your material budget."),
  ("Should I choose solid or engineered hardwood?", "Solid hardwood can be refinished more times and works well above grade on wood subfloors. Engineered wood is more dimensionally stable and can often go over concrete or below grade. See our engineered wood page for a comparison."),
  ("Do you refinish existing hardwood floors?", "Yes. We refinish existing hardwood floors (sanding and refinishing, or a screen and recoat) as well as installing new hardwood. See our " + REFINISH + " page."),
 ]),
# ------------------------------------------------------------------ Engineered
dict(slug="engineered-wood-flooring-portland", nav="Engineered wood installation", image="engineered", price_key="Engineered Wood",
 title="Engineered Hardwood Installation Portland | Banana Floors",
 desc="Engineered wood floors installed in Portland: nail-down, glue-down or floating. Compare veneer thickness and prices, then get a free quote.",
 eyebrow="Portland Metro · Engineered hardwood",
 h1="Engineered hardwood flooring installation in Portland",
 intro="Engineered hardwood has a real wood surface on a layered core, which makes it more stable than solid wood when humidity changes. Banana Floors installs engineered wood by nail-down, glue-down or floating methods, depending on the product and your subfloor.",
 schema_name="Engineered hardwood flooring installation",
 glance_h2="Engineered wood basics",
 points=[("$4–$14 / sq ft", "Material planning range"), ("Real wood veneer", "Over a plywood or HDF core"), ("3 install methods", "Nail, glue or float"), ("More stable", "Than solid wood in changing humidity")],
 sections=[
  ("How engineered wood is built", P(
    "Each board has a top layer (the veneer or wear layer) of real hardwood bonded to a core of plywood or high-density fiberboard. The cross-layered core resists the expansion and shrinkage that solid boards experience, which is why engineered products are often available in wide, long planks.",
    "Because the surface is real wood, it looks and feels like hardwood. How many times it can be sanded depends on veneer thickness: thin veneers may not be refinishable at all, while thicker veneers can be sanded one or more times. Always check the product's specifications.")),
  ("Where engineered wood makes sense", P(
    "Engineered wood is a good fit when you want real wood but the room or subfloor is not ideal for solid hardwood. Many products are approved over concrete and below grade, and floating versions can go over some existing floors. That makes engineered wood a common choice for daylight basements, condos with concrete slabs, and main floors where a wide-plank look is the goal.",
    "It is still wood. It is not a waterproof floor, so full bathrooms and laundry rooms are usually better served by tile or " + WATERPROOF + ".")),
  ("Comparing engineered products", H3("Veneer thickness") + P(
    "Thicker veneers cost more but add refinishing potential and longevity. Ask for the measurement, not just the overall board thickness.") +
    H3("Core type") + P(
    "Multi-ply plywood cores are common in higher-end products; HDF cores are often found in click-lock floating products. Both can perform well when installed according to the manufacturer's instructions.") +
    H3("Finish") + P(
    "Factory finishes vary from matte oil-look to aluminum-oxide urethane. Matte and wire-brushed finishes hide scratches better in homes with pets and kids.")),
  ("Installation methods", UL(
    "<strong>Nail-down or staple-down</strong> over a wood subfloor, similar to solid hardwood",
    "<strong>Glue-down</strong> over concrete or wood with the adhesive the manufacturer specifies",
    "<strong>Floating</strong> click-lock installation over an approved underlayment") + P(
    "Every method depends on a flat, dry subfloor. We check flatness and moisture before installation and include any " + SUBFLOOR + ", " + REMOVAL + " and " + TRIM + " in the scope. Use the " + PRICES + " for material budgets.")),
 ],
 faqs=[
  ("Is engineered hardwood real wood?", "Yes. The top layer is real hardwood. Underneath is a layered core of plywood or fiberboard that makes the board more dimensionally stable than solid wood."),
  ("Can engineered wood go over concrete?", "Many engineered products are approved over concrete when glued down or floated over the right underlayment and vapor barrier. Concrete moisture should be checked first, and the manufacturer's instructions decide what is allowed."),
  ("Can engineered hardwood be refinished?", "It depends on the veneer thickness. Thicker veneers can usually be sanded at least once; very thin veneers may only allow a light screen-and-recoat. Check the product specifications before you buy."),
  ("Is engineered wood good for kitchens?", "It can be, as long as spills are wiped up quickly. It handles humidity changes better than solid wood, but it is not waterproof. Many homeowners choose it for open kitchen-living areas."),
  ("What affects the cost of engineered wood installation?", "Installation method, subfloor preparation, removal of the old floor, stairs, transitions and the number of rooms. Send measurements and photos for a preliminary quote."),
 ]),
# ------------------------------------------------------------------ Laminate
dict(slug="laminate-flooring-portland", nav="Laminate installation", image="laminate", price_key="Laminate",
 title="Laminate Flooring Installation Portland | Banana Floors",
 desc="Affordable, durable laminate installed in Portland-area homes. Compare AC ratings, waterproof options and price per sq ft. Free estimate.",
 eyebrow="Portland Metro · Laminate",
 h1="Laminate flooring installation in Portland, Oregon",
 intro="Laminate gives you a crisp wood look and a hard-wearing surface at one of the lowest material costs of any hard floor. Banana Floors installs laminate in bedrooms, living areas, offices and rentals across the Portland metro.",
 schema_name="Laminate flooring installation",
 glance_h2="Laminate basics",
 points=[("$1.50–$6 / sq ft", "Material planning range"), ("AC3–AC5", "Abrasion ratings"), ("7–12 mm", "Common thicknesses"), ("Click-lock", "Floating installation")],
 sections=[
  ("What laminate is and where it fits", P(
    "Laminate is a layered product: a wear-resistant top coat over a printed design layer, on a high-density fiberboard (HDF) core with a backing layer. The top layer is harder than many hardwood finishes, so laminate resists scratches from pets and furniture well.",
    "Traditional laminate cores can swell if water sits on them, so laminate is best in bedrooms, living rooms, offices and hallways. Many newer lines are sold as water-resistant or waterproof with sealed edges and tighter joints; if you are considering laminate for a kitchen or entry, compare those products with LVP and see our " + WATERPROOF + " guide.")),
  ("How to compare laminate products", H3("AC rating") + P(
    "The AC (abrasion class) rating describes surface durability. AC3 is generally rated for all residential rooms, AC4 for heavy residential and light commercial use, and AC5 for heavier commercial traffic.") +
    H3("Thickness and core") + P(
    "Thicker boards (10–12 mm) tend to feel more solid and sound less hollow, but a dense core and proper underlayment matter as much as thickness.") +
    H3("Water resistance") + P(
    "Look at what the warranty actually covers: surface spills for a set number of hours, or standing water. Those are different promises.") +
    H3("Underlayment") + P(
    "Some laminate has an attached pad; other products need a separate foam or acoustic underlayment, plus a vapor barrier over concrete. Condo buildings may require a specific sound rating.")),
  ("How laminate is installed", P(
    "Laminate is installed as a floating click-lock floor. The boards lock together over underlayment and are not fastened to the subfloor, leaving an expansion gap at the walls that is covered by baseboard or shoe molding. Floating floors need a flat subfloor, so high and low spots are addressed first with " + SUBFLOOR + ".",
    "Laminate cannot be sanded or refinished. Individual boards can sometimes be replaced, so keep a box of leftover planks after installation.")),
  ("Planning your laminate project", UL(
    "Measure each room and add a waste allowance (the " + PRICES + " lets you choose 5–15%)",
    "Decide what happens to the existing floor (" + REMOVAL + ")",
    "Note where laminate meets tile, carpet or other floors, and whether baseboards will be reused (" + TRIM + ")",
    "Ask about stairs separately (" + STAIRS + ")") + P(
    "Send us measurements and photos for a preliminary quote. Final scope is verified on site before scheduling. Our " + COST + " explains the parts of a quote that are not material.")),
 ],
 faqs=[
  ("Is laminate waterproof?", "Standard laminate is not waterproof because the core is fiberboard. Some newer laminate lines are marketed as water-resistant or waterproof; check what the warranty covers before using laminate in kitchens, bathrooms or entries."),
  ("What AC rating do I need for my home?", "AC3 is generally suitable for residential rooms. AC4 is a good choice for busy households, pets and rentals. Commercial spaces may need AC4 or AC5."),
  ("Laminate or LVP: which should I choose?", "Laminate often has a sharper wood-look surface and good scratch resistance at a lower price. LVP handles water better and is quieter underfoot. In wet areas we usually suggest LVP or tile."),
  ("Can laminate be installed over existing flooring?", "Sometimes, over a flat, solid hard floor. Carpet and pad must be removed. Send photos so we can review the existing surface and any height changes at doorways."),
  ("What affects the cost of laminate installation?", "Removal, subfloor preparation, underlayment, transitions, baseboards, stairs and the number of rooms. Use the Price Guide for material and send project details for a preliminary installation quote."),
 ]),
# ------------------------------------------------------------------ Tile
dict(slug="tile-flooring-portland", nav="Tile installation", image="tile", price_key="Tile",
 title="Tile Floor Installation Portland, OR | Banana Floors",
 desc="Porcelain and ceramic tile floors for Portland bathrooms, kitchens and laundry rooms, with proper underlayment and membranes. Request a free quote.",
 eyebrow="Portland Metro · Ceramic & porcelain tile",
 h1="Tile floor installation in Portland, Oregon",
 intro="Tile is the most water-tolerant floor you can choose, which makes it the standard for bathrooms, laundry rooms, mudrooms and many kitchens. Banana Floors installs ceramic and porcelain floor tile and plans the substrate, membrane and layout before setting the first piece.",
 schema_name="Ceramic and porcelain tile floor installation",
 glance_h2="Tile basics",
 points=[("$1–$15+ / sq ft", "Material planning range"), ("Porcelain or ceramic", "Two main tile types"), ("Substrate first", "Backer board or membrane"), ("Layout matters", "Grout lines and cuts")],
 sections=[
  ("Porcelain or ceramic tile?", P(
    "Both are fired clay products. Porcelain is denser and absorbs less water, which makes it the usual choice for floors, entries and areas that see heavy use. Ceramic tile is often less expensive and easier to cut, and many ceramic tiles are rated for residential floors.",
    "Check that any tile you choose is rated for floor use, and look at slip resistance for bathrooms and entries. Large-format tiles look clean and modern but need a flatter substrate to avoid uneven edges (lippage).")),
  ("Why the layers under tile matter most", P(
    "Tile and grout are rigid. If the floor underneath flexes or moves, tile and grout can crack. A durable tile floor starts with a stiff, flat structure and the right underlayment.") +
    H3("Over a wood subfloor") + P(
    "Common approaches include cement backer board or an uncoupling membrane installed over plywood. Industry guidance calls for a stiffer floor under natural stone than under ceramic or porcelain, so we look at joist span and subfloor thickness before recommending a system.") +
    H3("Over concrete") + P(
    "Tile can often be set directly on sound concrete. Cracks in the slab may need a crack-isolation membrane so they do not telegraph through the tile.") +
    H3("Wet areas") + P(
    "Bathroom floors benefit from a waterproofing membrane, especially over living space. Tell us about showers, tubs and floor drains so we can define exactly what is and is not in the flooring scope.")),
  ("Planning layout, grout and transitions", P(
    "Before tile is set, we plan where full tiles and cuts will land, how grout lines align with walls and doorways, and how the tile height meets adjacent floors. Tile plus backer or membrane is often taller than the floor next to it, so " + TRIM + " and door clearances are part of the plan.",
    "Cement-based grout is common and economical; urethane and epoxy grouts resist stains better. Wider grout joints are more forgiving with handmade or rustic tile, while rectified porcelain allows tighter joints.")),
  ("What affects a tile installation quote", UL(
    "Removal of the existing floor, which can be slow for old tile set in mortar (" + REMOVAL + ")",
    "Subfloor repair, leveling and the underlayment or membrane system (" + SUBFLOOR + ")",
    "Tile size, pattern (straight, offset, herringbone), and the number of cuts",
    "Toilets, vanities and appliances that need to be pulled and reset") + P(
    "Use the " + PRICES + " for a material range and our " + COST + " for the rest. Send room sizes and photos for a preliminary quote.")),
 ],
 faqs=[
  ("Is porcelain or ceramic better for a bathroom floor?", "Both can work. Porcelain is denser and absorbs less water, so it is the more common floor choice. Whatever you choose, make sure it is rated for floors and has adequate slip resistance."),
  ("Can tile go over a wood subfloor?", "Yes, when the floor structure is stiff enough and the right underlayment, such as cement backer board or an uncoupling membrane, is used. We review the subfloor before recommending a system."),
  ("Why does my tile floor need a membrane?", "Membranes can separate tile from minor movement in the substrate, isolate slab cracks, and add waterproofing in wet areas. Which one is needed depends on the room and the substrate."),
  ("Can new tile go over old tile?", "Sometimes, if the old tile is well bonded and flat and the added height works at doorways. In many cases removal is the better long-term option. Send photos for a review."),
  ("What affects the cost of tile installation?", "Removal, substrate preparation, membranes, tile size and pattern, the number of cuts, and fixtures that need to be removed and reset. Send details for a preliminary quote."),
 ]),
# ------------------------------------------------------------------ Carpet
dict(slug="carpet-installation-portland", nav="Carpet installation", image="carpet", price_key="Carpet",
 title="Carpet Installation Portland, OR | Banana Floors",
 desc="Carpet and pad installed in Portland homes, with old carpet removal available. Compare fibers, face weight and price per sq ft. Free estimate.",
 eyebrow="Portland Metro · Residential carpet",
 h1="Carpet installation in Portland, Oregon",
 intro="Carpet is still the most comfortable, quiet floor for bedrooms, family rooms and many stairways. Banana Floors installs residential carpet and pad and helps you compare fiber, construction and pad before you buy.",
 schema_name="Residential carpet installation",
 glance_h2="Carpet basics",
 points=[("$1.50–$7 / sq ft", "Material planning range"), ("Nylon, polyester, wool", "Common fibers"), ("Pad matters", "Density and thickness"), ("Stretch-in", "Tack strip and power stretching")],
 sections=[
  ("Choosing a carpet fiber", H3("Nylon") + P("Resilient and durable, nylon springs back well in high-traffic areas and on stairs. It is a common choice for busy households.") +
    H3("Polyester and PET") + P("Soft and stain-resistant, often at a lower price. It may mat down faster than nylon in heavy traffic.") +
    H3("Triexta") + P("A newer fiber family with good softness and stain resistance.") +
    H3("Wool") + P("A natural, premium fiber with a rich feel. It costs more and needs appropriate cleaning methods.")),
  ("Construction, face weight and pad", P(
    "Cut-pile carpet (plush, textured, frieze) feels soft; loop carpet (Berber-style) is durable but can snag with pets. Face weight, measured in ounces per square yard, tells you how much fiber is on the surface; density and twist matter too, so compare samples side by side rather than relying on one number.",
    "Pad is easy to overlook and makes a big difference to comfort and wear. Many carpet manufacturers specify a minimum pad density and a maximum thickness for warranty coverage. We match the pad to the carpet's requirements.")),
  ("How carpet is installed", P(
    "Wall-to-wall carpet is typically stretched over pad and held on tack strip around the room. Power stretching pulls the carpet tight so it is less likely to ripple later. Seams are planned so they fall in low-traffic areas and run in the direction of light where possible.",
    "Before new carpet goes in, old carpet, pad and damaged tack strip are removed (" + REMOVAL + "), squeaks are addressed, and the subfloor is cleaned. Where carpet meets hard flooring, a transition strip finishes the edge (" + TRIM + ").")),
  ("Carpet on stairs and in rentals", P(
    "Stairs take more time than open floor and are quoted separately. Tell us the number of steps and whether any are open-sided, curved or have landings. See " + STAIRS + " for options, including replacing stair carpet with a hard surface.",
    "For " + L("/flooring/rental-turnover-flooring-portland.html", "rental turnovers") + ", durable, stain-resistant carpet in a consistent color across units can simplify future repairs. Use the " + PRICES + " to compare tiers.")),
 ],
 faqs=[
  ("What is the best carpet fiber for pets and kids?", "Nylon is a durable, resilient choice for busy homes. Stain-resistant polyester and triexta carpets are also popular. Avoid loop carpet if pets tend to scratch or snag."),
  ("Do I need new pad with new carpet?", "In most cases, yes. Old pad is often compressed or soiled, and many carpet warranties require pad that meets specific density and thickness standards."),
  ("Is old carpet removal included?", "Removal of old carpet, pad and tack strip can be included in your quote. Tell us how many rooms and whether there are stairs so it is part of the scope."),
  ("How long does carpet installation take?", "Timing depends on the number of rooms, stairs, furniture moving and removal. We confirm the schedule after reviewing the scope."),
  ("What affects the cost of carpet installation?", "The carpet and pad you choose, removal of the old floor, stairs, seams, furniture moving and the room layout. Send measurements and photos for a preliminary quote."),
 ]),
]

_MORE = {
 "carpet-installation-portland": ("Carpet care and getting the most from your new carpet", P(
   "New carpet lasts longer with a few habits: vacuum high-traffic areas regularly, use mats at exterior doors (especially during Portland's wet months), blot spills rather than rubbing them, and follow the manufacturer's recommendations for professional cleaning, which some warranties require.",
   "Furniture can leave dents in new carpet; moving pieces slightly from time to time and using furniture cups helps. Some shedding of loose fibers is normal in the first weeks with cut-pile carpet. If you have pets, ask about carpets with pet-related stain and moisture protection, and consider a hard floor such as LVP in the rooms where accidents are most likely.")),
 "engineered-wood-flooring-portland": ("Engineered wood versus solid hardwood and LVP", P(
   "Compared with " + L("/flooring/hardwood-flooring-portland.html", "solid hardwood") + ", engineered wood is usually the better choice over concrete, below grade, and in wide planks where seasonal movement is a concern. Solid hardwood wins on long-term refinishing potential. Compared with " + L("/flooring/lvp-flooring-portland.html", "LVP") + ", engineered wood offers the feel, sound and natural variation of real wood but is less tolerant of water and costs more per square foot.",
   "Many Portland homeowners mix materials: engineered wood through the main living areas, LVP or tile in bathrooms and laundry rooms, and carpet in bedrooms. Planning the transitions between them at the start keeps the finished floors looking consistent.")),
 "laminate-flooring-portland": ("Living with laminate", P(
   "Laminate is easy to care for: sweep or vacuum regularly and clean with a lightly damp (not wet) mop or the cleaner the manufacturer recommends. Avoid steam mops and standing water. Felt pads under furniture and mats at entries help the surface last.",
   "Because laminate floats, it moves slightly with temperature and humidity. That is why expansion gaps at the walls and at fixed objects such as kitchen islands are important, and why very long runs may need a transition. If a board is damaged, it can often be replaced, which is another reason to keep a few spare boards from the original order.")),
 "tile-flooring-portland": ("Tile in Portland kitchens, entries and basements", P(
   "Beyond bathrooms, tile is a strong choice for entries and mudrooms that see wet shoes and gravel during the rainy season, for laundry rooms, and for basements on concrete. Porcelain tile is also used in kitchens where homeowners want a surface that resists water, heat and stains.",
   "Tile is hard and can feel cool underfoot. Some homeowners add electric radiant floor heat under bathroom tile; if you are considering it, plan it before the floor goes in. For large open areas where you want warmth and lower cost, " + L("/flooring/lvp-flooring-portland.html", "LVP") + " in a stone look is another option.")),
}
for _s in SERVICES:
    if _s["slug"] in _MORE:
        _s["sections"].append(_MORE[_s["slug"]])

from .services_extra import EXTRA  # noqa: E402
SERVICES += EXTRA
