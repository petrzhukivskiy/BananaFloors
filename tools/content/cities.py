"""Service-area page content. Local details are general and verifiable (geography, housing eras, climate).
No project claims, reviews or statistics."""
from .services import P, UL, H3, L

LVP = L("/flooring/lvp-flooring-portland.html", "LVP")
HW = L("/flooring/hardwood-flooring-portland.html", "solid hardwood")
EW = L("/flooring/engineered-wood-flooring-portland.html", "engineered wood")
LAM = L("/flooring/laminate-flooring-portland.html", "laminate")
TILE = L("/flooring/tile-flooring-portland.html", "tile")
CARPET = L("/flooring/carpet-installation-portland.html", "carpet")
STAIRS = L("/flooring/stair-flooring-installation-portland.html", "stair flooring")
PREP = L("/flooring/subfloor-prep-floor-leveling-portland.html", "subfloor preparation")
REMOVAL = L("/flooring/flooring-removal-portland.html", "removal")
REFINISH = L("/flooring/hardwood-floor-refinishing-portland.html", "hardwood floor refinishing")
TRIM = L("/flooring/baseboard-trim-installation-portland.html", "baseboards and transitions")
WATER = L("/flooring/waterproof-flooring-portland.html", "waterproof flooring")
RENTAL = L("/flooring/rental-turnover-flooring-portland.html", "rental flooring")
COMM = L("/flooring/commercial-flooring-installation-portland.html", "commercial flooring")
COST = L("/flooring-installation-cost-portland.html", "installation cost guide")

CITIES = [
# ------------------------------------------------------------------ Portland
dict(slug="flooring-installation-portland-or", name="Portland", state="OR", image="hardwood",
 nearby=["flooring-installation-vancouver-wa", "flooring-installation-beaverton-or", "flooring-installation-gresham-or", "flooring-installation-lake-oswego-or", "flooring-installation-happy-valley-or", "flooring-installation-tigard-or", "flooring-installation-clackamas-or"],
 title="Portland Floors: Bungalows, Basements, Condos | Banana Floors",
 desc="Portland flooring installation: LVP, hardwood, laminate, tile and carpet for bungalows, basements and condos. Oregon CCB 209244. Free estimate.",
 h1="Flooring installation in Portland, Oregon",
 intro="Portland is our home base. Banana Floors installs LVP, hardwood, engineered wood, laminate, tile and carpet in Portland houses, condos and small commercial spaces, and plans the removal and preparation each home needs before the new floor goes in.",
 sections=[
  ("Portland homes and what's under their floors", P(
    "Portland's housing stock is unusually varied, and the right floor often depends on when the house was built. Inner neighborhoods are full of early-1900s Craftsman bungalows, Old Portland foursquares and Victorians, many with original fir or oak floors, plaster walls, wide painted trim and doorways that were never quite square. Those homes reward careful planning: floor heights at thresholds, how new flooring meets an original floor in the next room, and whether old trim can be reused. When an original floor is worth keeping, " + REFINISH + " can bring it back instead of replacing it.",
    "Further out, postwar ranches and split-levels in East and Southwest Portland often have carpet over plywood or particleboard, sometimes with sheet vinyl in kitchens and baths. Newer infill houses and townhomes tend to have open main floors where one continuous floor runs from the entry through the kitchen. In the Pearl District, South Waterfront and other condo areas, concrete slabs and building rules about sound control shape the product choice.")),
  ("Climate and moisture in Portland", P(
    "Portland's mild, wet climate brings most of its rain between fall and spring. For floors, the bigger issue is usually moisture from below rather than rain at the door. Many older houses sit over crawlspaces, and unfinished or partly finished basements are common. A crawlspace without an effective vapor barrier can raise moisture in wood subfloors, and basement slabs can release moisture into anything glued or floated on top.",
    "Before recommending a product we check moisture in wood subfloors and look at slab conditions. Wood floors also move with the seasons: small gaps between boards in winter, when the furnace is running, are normal. Cupping or buckling usually points to a moisture source that should be fixed first.")),
  ("Choosing the right floor for a Portland house", H3("Bungalows and older homes") + P(
    "If you love the look of the original floors, " + HW + " or " + EW + " in a compatible species and width can continue the character into a remodeled kitchen or addition. Where original floors are already damaged or covered, many homeowners choose LVP for kitchens and baths and wood or carpet in bedrooms.") +
    H3("Basements") + P(LVP + " and " + TILE + " are the usual choices on concrete. See our " + WATER + " guide for the details that keep water problems from reaching the floor.") +
    H3("Condos and apartments") + P("Check your HOA rules before you buy. Many buildings require an underlayment with a minimum sound rating, and some limit work hours, elevator use or disposal.") +
    H3("Rentals and investment properties") + P("Durable, repairable floors make turnovers easier. See " + RENTAL + " for owner-focused advice.")),
  ("How a Portland flooring project usually goes", UL(
    "Check material ranges in the Price Guide and narrow your choices",
    "Send room sizes, photos and the age of the home with your estimate request",
    "Get a preliminary quote that covers material planning, " + REMOVAL + ", " + PREP + " and " + TRIM,
    "Confirm measurements and site conditions in person, then schedule installation") + P(
    "Older homes deserve one extra step: if old sheet vinyl, vinyl tile or painted trim will be disturbed, tell us when the house was built so any testing happens before work begins. Our " + COST + " explains how these parts of a quote fit together.")),
 ],
 hoods_h2="Portland neighborhoods we serve",
 hoods_intro="We work across Portland's quadrants, including neighborhoods such as:",
 neighborhoods=["Laurelhurst, Irvington and Grant Park", "Sellwood-Moreland and Eastmoreland", "Hawthorne, Richmond and Sunnyside", "Alberta, Concordia and Woodlawn", "St. Johns, Kenton and Arbor Lodge", "Montavilla, Mt. Tabor and Hollywood", "Multnomah Village, Hillsdale and Southwest Hills", "Pearl District, South Waterfront and Downtown condos", "Outer East Portland, including Parkrose and Lents"],
 faqs=[
  ("Do you install flooring in older Portland homes?", "Yes. We plan around the things older homes bring, such as uneven subfloors, original trim, threshold heights and floors that meet original hardwood. Tell us the age of the home when you request an estimate."),
  ("What flooring works best in a Portland basement?", "LVP and tile are common choices over concrete. We check slab moisture and follow the product's vapor-barrier requirements before installation."),
  ("Can new flooring match my original fir or oak floors?", "An exact match is difficult, but a compatible species, width and finish can work well, especially with a deliberate transition at a doorway. Send photos of the existing floor."),
  ("Do Portland condos have special flooring rules?", "Often. Many HOAs require sound-rated underlayment for hard floors and set rules for work hours and disposal. Check your building's requirements before choosing a product."),
 ]),
# ------------------------------------------------------------------ Gresham
dict(slug="flooring-installation-gresham-or", name="Gresham", state="OR", image="lvp",
 nearby=["flooring-installation-portland-or", "flooring-installation-happy-valley-or", "flooring-installation-clackamas-or", "flooring-installation-oregon-city-or"],
 title="Flooring Installation Gresham, OR | Banana Floors",
 desc="Flooring installers serving Gresham: LVP, hardwood, laminate, tile and carpet, with removal and subfloor prep. Call (503) 421-1730 for a free estimate.",
 h1="Flooring installation in Gresham, OR",
 intro="Gresham sits on the east side of the Portland metro, between Portland and the Mt. Hood foothills. Banana Floors installs LVP, wood, laminate, tile and carpet in Gresham homes and reviews removal and preparation as part of every replacement project.",
 sections=[
  ("Gresham homes we see most often", P(
    "Gresham is one of Oregon's largest cities, and much of its housing was built in the second half of the 20th century. Single-level ranches, split-levels and two-story homes from the 1960s through the 1990s make up a large share of neighborhoods like Rockwood, Centennial and Powell Valley. Many of these houses still have their original carpet in living areas and bedrooms, with sheet vinyl or older laminate in kitchens and baths.",
    "Newer subdivisions toward Pleasant Valley and the southeast edge of the city were built more recently and often have open main floors where a single plank floor can run through the living room, dining area and kitchen. Gresham also has many apartments, duplexes and rental homes, where durability and easy repairs matter more than anything else.")),
  ("Split-levels, short stair runs and transitions", P(
    "Split-level houses are a Gresham staple, and they bring a specific planning challenge: short flights of stairs between levels, plus several doorways where carpet, vinyl and wood may all meet. When you replace one level, think about how the " + STAIRS + " and landings will match, and where each transition will sit (" + TRIM + ").",
    "Older ranch homes often have flooring layers stacked over the years. Removing the old layers (" + REMOVAL + ") usually gives a better result than covering them, and lets us check the subfloor for squeaks or soft spots before installation.")),
  ("East winds, wet winters and your floors", P(
    "Gresham shares the Portland area's wet fall-to-spring season, and it is also close enough to the Columbia River Gorge to feel the cold, dry east winds that blow through in winter. Those dry spells, combined with indoor heating, can open small gaps in wood floors; damp seasons do the opposite. Products with good dimensional stability, such as " + EW + " and rigid-core " + LVP + ", handle those swings well.",
    "For homes over crawlspaces, the vapor barrier underneath matters. We check subfloor moisture before installing wood and let you know if something below the floor should be addressed first.")),
  ("Flooring choices that suit Gresham homes", UL(
    "<strong>LVP</strong> for kitchens, baths, entries and rentals, where water and pets are part of daily life",
    "<strong>Laminate</strong> for bedrooms and living areas on a tighter budget (" + LAM + ")",
    "<strong>Carpet</strong> for bedrooms, family rooms and split-level stairs (" + CARPET + ")",
    "<strong>Hardwood or engineered wood</strong> for main living areas where you want real wood",
    "<strong>Tile</strong> for bathrooms, laundry rooms and mudrooms (" + TILE + ")") + P(
    "Landlords and property managers can read our " + RENTAL + " page for product and scheduling tips.")),
 ],
 hoods_h2="Gresham neighborhoods we serve",
 hoods_intro="Our Gresham service area includes neighborhoods such as:",
 neighborhoods=["Rockwood", "Centennial", "Powell Valley", "Pleasant Valley", "Gresham Butte", "Kelly Creek", "North Central and Historic Downtown", "Northeast and Northwest Gresham"],
 faqs=[
  ("Do you install flooring in Gresham?", "Yes. Gresham is part of our regular service area. Send your project details or call or text (503) 421-1730 to request a free preliminary estimate."),
  ("What flooring is good for a split-level home?", "Many split-level homeowners use one hard floor such as LVP across the main level and carpet or matching stair nosing on the short stair runs. Planning transitions between levels is the key."),
  ("Can you remove old carpet and vinyl before installing new floors?", "Removal can be part of your scope. Tell us what is on the floor now; older vinyl in homes built before 2004 may need testing before it is disturbed."),
  ("Is LVP a good choice for Gresham rentals?", "LVP is a popular rental floor because the planks resist water and scratches and damaged planks can often be replaced. Choose a thicker wear layer for high traffic."),
 ]),
# ------------------------------------------------------------------ Happy Valley
dict(slug="flooring-installation-happy-valley-or", name="Happy Valley", state="OR", image="engineered",
 nearby=["flooring-installation-clackamas-or", "flooring-installation-gresham-or", "flooring-installation-portland-or", "flooring-installation-oregon-city-or"],
 title="Flooring Installation Happy Valley, OR | Banana Floors",
 desc="Happy Valley flooring installation: LVP, hardwood, laminate, tile and carpet for newer and established homes. Free estimate: (503) 421-1730.",
 h1="Flooring installation in Happy Valley, OR",
 intro="Happy Valley has grown quickly over the past few decades, and many homes here are now ready for their first flooring upgrade. Banana Floors installs LVP, wood, laminate, tile and carpet in Happy Valley homes and plans each project around the way open, multi-level houses are built.",
 sections=[
  ("Replacing builder-grade flooring", P(
    "A large share of Happy Valley's homes were built from the 1990s onward, in subdivisions spread across the hills and ridges of Clackamas County. Many still have the flooring they were built with: carpet in living rooms, bedrooms and stairs, and sheet vinyl, laminate or entry-level wood in kitchens. After fifteen or twenty years of family life, those builder-grade floors are often the first thing owners want to upgrade.",
    "The upside of newer construction is that subfloors are usually in better shape than in older homes. Plywood or OSB subfloors still need to be checked for flatness and squeaks, but extensive repairs are less common. That leaves more of the budget for the floor itself.")),
  ("Open main floors and two-story stairs", P(
    "Happy Valley homes commonly have an open main floor where the entry, kitchen, dining and family areas flow together. A single continuous floor, often " + LVP + " or " + EW + ", makes those spaces feel larger. Long, uninterrupted runs need planning: floating floors have maximum run lengths before a transition is required, and kitchen islands and cabinets affect how the floor is installed.",
    "Two-story layouts also mean a main staircase, usually carpeted. Replacing stair carpet with a hard surface that matches the new main floor is one of the most common requests in newer homes; see " + STAIRS + " for the options and why stairs are priced per step.")),
  ("Hillside lots, garages and daylight basements", P(
    "Because much of Happy Valley is built on slopes, some homes have daylight basements or lower levels partly below grade, often on concrete. Those rooms are good candidates for rigid-core LVP or tile, with a moisture check and the manufacturer's vapor-barrier requirements followed (" + WATER + ").",
    "Rooms over garages can run colder in winter, which is worth mentioning if you are considering wood. Tell us about any room that feels noticeably colder or warmer than the rest of the house.")),
  ("HOAs and planning ahead", P(
    "Many Happy Valley neighborhoods have homeowners associations. Interior flooring usually is not regulated, but associations may have rules about work hours, contractor parking and dumpsters. Check before scheduling so the project runs smoothly.") + UL(
    "Check material ranges in the Price Guide and choose a tier",
    "Send room sizes, photos and the stair count with your estimate request",
    "Decide whether baseboards will be reused or replaced (" + TRIM + ")",
    "Confirm measurements on site, then schedule installation") + P("Our " + COST + " explains how material, removal, preparation and installation fit together.")),
 ],
 hoods_h2="Happy Valley areas we serve",
 hoods_intro="We serve homes throughout Happy Valley, including areas such as:",
 neighborhoods=["Scouters Mountain", "Rock Creek", "Pleasant Valley", "Sunnyside", "Mount Talbert", "Eagle Landing", "Happy Valley Town Center area", "Damascus and Carver (nearby)"],
 faqs=[
  ("Can you replace stair carpet with LVP or wood in a Happy Valley home?", "Often, yes. LVP with matching stair nosing or wood treads can match a new main floor. We review the stair construction and count when preparing the quote."),
  ("What flooring works best for an open-concept main floor?", "A continuous LVP or engineered wood floor is popular. Long runs may need a transition, and cabinets and islands affect installation, so we plan the layout first."),
  ("Do newer homes need subfloor preparation?", "Usually less than older homes, but flatness and squeaks are still checked before installation. Floating floors in particular need a flat subfloor."),
  ("Is there anything to check with my HOA?", "Interior flooring is rarely restricted, but HOAs may have rules on work hours, parking and dumpsters. Check before your installation date."),
 ]),
# ------------------------------------------------------------------ Clackamas
dict(slug="flooring-installation-clackamas-or", name="Clackamas", state="OR", image="laminate",
 nearby=["flooring-installation-happy-valley-or", "flooring-installation-oregon-city-or", "flooring-installation-portland-or", "flooring-installation-gresham-or", "flooring-installation-lake-oswego-or"],
 title="Flooring Installation Clackamas, OR | Banana Floors",
 desc="Flooring installers in Clackamas: LVP, hardwood, laminate, tile and carpet, plus removal and prep. Get a free estimate: (503) 421-1730.",
 h1="Flooring installation in Clackamas, OR",
 intro="Clackamas, the unincorporated community around Clackamas Town Center and the I-205 corridor, has a mix of single-family homes, townhomes, condos and apartments. Banana Floors installs LVP, wood, laminate, tile and carpet here and accounts for the whole installation, not just the material.",
 sections=[
  ("Clackamas housing: a little of everything", P(
    "Clackamas grew up around the Sunnyside Road and Highway 212 corridors, and its homes reflect several decades of building. You will find 1970s and 1980s ranches and split-levels, 1990s and 2000s two-story homes, and a large number of townhomes, condos and apartment communities near the Town Center and the MAX Green Line.",
    "That mix means very different flooring projects: a whole-house replacement in a single-family home, a quick turnover in a rental, or a condo where the HOA sets the rules for underlayment and work hours. We start by understanding which of those your project is.")),
  ("Condos, townhomes and shared walls", P(
    "In attached homes, sound travels. Many HOAs require hard floors to be installed over an underlayment with a minimum sound rating, and some require approval before work begins. Read your association's rules before buying material; the right underlayment is part of the material choice, not an afterthought.",
    "Townhomes are often multi-level with stairs between every floor, so " + STAIRS + " and landings usually belong in the plan. Condo buildings can also have rules about elevators, parking and where old flooring can be disposed of.")),
  ("Account for the whole installation", P(
    "A material price is only one part of a flooring budget. In Clackamas homes built across several decades, the other parts vary widely:") + UL(
    "<strong>Removal:</strong> carpet comes up quickly; glued vinyl or tile takes longer (" + REMOVAL + ")",
    "<strong>Subfloor:</strong> older homes may need squeak repairs or leveling; newer homes usually need less (" + PREP + ")",
    "<strong>Edges:</strong> baseboards, shoe molding and transitions at every doorway (" + TRIM + ")",
    "<strong>Moving and access:</strong> furniture, appliances, stairs and parking") + P(
    "Our " + COST + " walks through each of these so a quote is easy to compare.")),
  ("Moisture and the flooring you choose", P(
    "Like the rest of the Portland area, Clackamas has damp winters. Homes built on slabs or over crawlspaces benefit from a moisture check before wood or glue-down floors are installed. Rigid-core " + LVP + " and " + TILE + " are forgiving choices for kitchens, baths, laundry rooms and ground-floor condos; " + EW + " gives a real wood look with better stability than solid boards; and " + CARPET + " remains a comfortable choice for bedrooms and upper floors.",
    "Rental owners near the Town Center can find product and scheduling advice on our " + RENTAL + " page.")),
 ],
 hoods_h2="Clackamas-area neighborhoods we serve",
 hoods_intro="Our Clackamas service area includes communities such as:",
 neighborhoods=["Clackamas Town Center area", "Sunnyside Road corridor", "Mt. Scott area", "Highway 212 and Clackamas Industrial area", "Oak Grove and Jennings Lodge (nearby)", "Carver and Damascus (nearby)"],
 faqs=[
  ("Do you install flooring in Clackamas condos and townhomes?", "Yes. Share your HOA's flooring and underlayment requirements and any rules about work hours or disposal so they are included in the scope."),
  ("What underlayment does my condo need?", "Your HOA decides. Many require an underlayment with a minimum sound rating for hard floors. Check the rules before buying material."),
  ("What does a flooring quote include besides material?", "Usually removal, subfloor preparation, installation labor, trim and transitions, and any stairs. The material price guide covers material only."),
  ("Can you work on rental units in Clackamas?", "Yes. Tell us vacancy and move-in dates, access details and the rooms involved, and we will confirm timing after reviewing the scope."),
 ]),
# ------------------------------------------------------------------ Oregon City
dict(slug="flooring-installation-oregon-city-or", name="Oregon City", state="OR", image="hardwood",
 nearby=["flooring-installation-clackamas-or", "flooring-installation-lake-oswego-or", "flooring-installation-happy-valley-or", "flooring-installation-portland-or"],
 title="Flooring Installation Oregon City, OR | Banana Floors",
 desc="Oregon City flooring installation for historic homes, remodels and newer houses: LVP, hardwood, laminate, tile, carpet. Free estimate.",
 h1="Flooring installation in Oregon City, OR",
 intro="Oregon City, the Clackamas County seat at the end of the Oregon Trail, has some of the oldest homes in the region alongside newer neighborhoods on the hills above. Banana Floors installs LVP, wood, laminate, tile and carpet in Oregon City and coordinates flooring with the rest of your remodel.",
 sections=[
  ("Historic homes in McLoughlin and Canemah", P(
    "Oregon City was incorporated in 1844, and its historic neighborhoods show it. The McLoughlin neighborhood on the bluff above downtown and the Canemah historic district to the south have homes from the late 1800s and early 1900s, many with original fir floors, tall painted baseboards and framing that has settled over a century or more.",
    "In these homes, flooring decisions are as much about preservation as about style. Floors may slope, doorways may not be square, and original trim is often worth keeping. Before choosing a product, we look at how much the floor deviates, whether it should be flattened (" + PREP + "), and how a new floor will meet original wood in adjacent rooms (" + TRIM + ").")),
  ("Mid-century homes and newer neighborhoods", P(
    "Beyond the historic core, Oregon City has mid-century ranches and a wide band of newer subdivisions toward Park Place, the South End and Beavercreek Road. Those homes look more like the rest of the metro: carpet and vinyl that are ready for replacement, open kitchens, and two-story layouts with carpeted stairs.",
    "For these houses, " + LVP + " is a common choice for main floors and kitchens, " + CARPET + " for bedrooms, and " + EW + " where owners want real wood with good stability.")),
  ("Coordinate flooring with your remodel", P(
    "Flooring is often one part of a bigger project in Oregon City homes: a kitchen update, a bathroom remodel, or a whole-house refresh before a sale. The order of work matters. Many floating floors should not be installed under cabinets, tile floors may need to go in before a new vanity or toilet, and painting is usually easier before baseboards go back on.") + UL(
    "Tell us which trades are involved and the order you are planning",
    "Decide whether cabinets, islands or vanities go in before or after flooring",
    "Plan floor heights at doorways, dishwashers and exterior doors",
    "Leave time for removal and preparation before installation (" + REMOVAL + ")")),
  ("Older materials, moisture and the river", P(
    "Many Oregon City homes predate modern materials rules. If old sheet vinyl, vinyl tile or painted trim will be disturbed, tell us when the house was built so any testing happens before work starts. Homes near the Willamette and Clackamas rivers and on hillside lots can also have damp crawlspaces or lower levels; we check subfloor moisture before installing wood and recommend " + WATER + " options for basements and wet rooms.",
    "Use our " + COST + " to see how removal, preparation and installation fit alongside your material budget.")),
 ],
 hoods_h2="Oregon City neighborhoods we serve",
 hoods_intro="We work throughout Oregon City, including neighborhoods such as:",
 neighborhoods=["McLoughlin", "Canemah", "Park Place", "South End", "Hillendale", "Rivercrest", "Gaffney Lane", "Barclay Hills", "Beavercreek Road area"],
 faqs=[
  ("Can you install new flooring in a historic Oregon City home?", "Yes. Older homes need extra planning for uneven floors, original trim and transitions to original wood. Tell us the age of the home and send photos of the rooms."),
  ("Should flooring go in before or after new kitchen cabinets?", "It depends on the product. Many floating floors should not be installed under cabinets or islands, while some glue-down and tile floors can be. We match the sequence to the product requirements."),
  ("My floors slope. Can they be leveled?", "Some slope is normal in older homes. Flooring needs a flat surface more than a perfectly level one; we check flatness and recommend preparation that fits the product and the house."),
  ("Do I need to test old vinyl before removal?", "If your home was built before 2004 and has old sheet vinyl, vinyl tile or adhesive, testing for asbestos is generally required before it is disturbed. Licensed specialists handle testing and any abatement."),
 ]),
# ------------------------------------------------------------------ Beaverton
dict(slug="flooring-installation-beaverton-or", name="Beaverton", state="OR", image="lvp",
 nearby=["flooring-installation-portland-or", "flooring-installation-tigard-or", "flooring-installation-lake-oswego-or"],
 title="Flooring Installation Beaverton, OR | Banana Floors",
 desc="Beaverton flooring installers: LVP, hardwood, laminate, tile and carpet, with removal and subfloor prep. Request a free estimate today.",
 h1="Flooring installation in Beaverton, OR",
 intro="Beaverton, in Washington County just west of Portland, is a city of established neighborhoods, newer subdivisions and many apartment and townhome communities. Banana Floors installs LVP, wood, laminate, tile and carpet in Beaverton and helps you plan a complete flooring replacement.",
 sections=[
  ("Beaverton homes by era", P(
    "Much of Beaverton was built out from the 1950s through the 1980s, and neighborhoods such as Vose, Highland, Five Oaks and Central Beaverton have many ranches and split-levels from that period. Those homes often have hardwood hidden under carpet in older sections, sheet vinyl in kitchens, and a mix of materials added during past remodels.",
    "Hillside neighborhoods like Sexton Mountain and Murrayhill were largely built in the 1980s and 1990s, with two-story layouts, family rooms and carpeted stairs. On the south and west edges, newer townhomes and houses around South Cooper Mountain bring open plans and builder-grade finishes that owners often upgrade. Nearby unincorporated communities such as Cedar Hills, Cedar Mill and Aloha share many of the same housing types.")),
  ("Plan a flooring replacement", P(
    "In a replacement, the existing floor tells you a lot. Before we quote, it helps to know what is on the floor now and what might be underneath it:") + UL(
    "<strong>Carpet over hardwood:</strong> in some mid-century homes, original oak is hidden under carpet. Look under a floor vent or in a closet corner before you plan; sound oak can often be refinished (" + REFINISH + ")",
    "<strong>Layered vinyl:</strong> kitchens may have more than one layer of vinyl. Removal gives a flatter, lower floor at doorways (" + REMOVAL + ")",
    "<strong>Squeaks:</strong> common in older two-story homes and best fixed while the subfloor is exposed (" + PREP + ")",
    "<strong>Stairs:</strong> carpeted stairs in two-story homes often need a matching update (" + STAIRS + ")")),
  ("Apartments, townhomes and rentals", P(
    "Beaverton has a large rental market and many townhome communities. For rental owners and property managers, durable " + LVP + " in kitchens and living areas and stain-resistant " + CARPET + " in bedrooms make turnovers easier; see our " + RENTAL + " page. For townhomes and condos with shared walls, check HOA rules for sound-rated underlayment before choosing a hard floor.")),
  ("Choosing materials for Beaverton homes", P(
    "Washington County shares the Portland area's damp winters, and many Beaverton homes are built over crawlspaces. Rigid-core LVP and " + TILE + " handle kitchens, baths and entries well. " + EW + " is a good way to get real wood in open living areas with better seasonal stability than solid boards, and " + HW + " remains a strong choice above grade on wood subfloors. " + LAM + " keeps budgets down in bedrooms and offices.",
    "Small offices and shops in Beaverton can see our " + COMM + " page. Every quote is verified on site before scheduling, and our " + COST + " explains what goes into it.")),
 ],
 hoods_h2="Beaverton neighborhoods we serve",
 hoods_intro="We serve homes across Beaverton and nearby Washington County, including:",
 neighborhoods=["Central Beaverton", "Sexton Mountain and Murrayhill", "Highland and Vose", "Five Oaks and Triple Creek", "Greenway", "South Cooper Mountain", "Cedar Hills and Cedar Mill (nearby)", "Aloha (nearby)"],
 faqs=[
  ("Do you install flooring in Beaverton?", "Yes. Beaverton is part of our regular service area. Send your project details or call or text (503) 421-1730 for a free preliminary estimate."),
  ("I found hardwood under my carpet. Should I keep it?", "Possibly. Send photos of the exposed wood and the rooms involved. Whether it is worth keeping depends on its condition and your plans; tell us what you have in mind."),
  ("Do you remove old vinyl before installing LVP?", "Removal is often the better option, especially with multiple layers. Older vinyl may need testing before it is disturbed. We review the existing floor before confirming the scope."),
  ("What flooring is best for a Beaverton rental?", "LVP in kitchens, baths and living areas and durable carpet in bedrooms are common choices. Using the same product across units simplifies repairs."),
 ]),
# ------------------------------------------------------------------ Tigard
dict(slug="flooring-installation-tigard-or", name="Tigard", state="OR", image="carpet",
 nearby=["flooring-installation-beaverton-or", "flooring-installation-lake-oswego-or", "flooring-installation-portland-or"],
 title="Flooring Installation Tigard, OR | Banana Floors",
 desc="Tigard flooring installation, including occupied-home projects: LVP, hardwood, laminate, tile and carpet. Free estimate: (503) 421-1730.",
 h1="Flooring installation in Tigard, OR",
 intro="Tigard sits southwest of Portland along Highway 217 and I-5, with established neighborhoods, hillside homes on Bull Mountain and new construction in River Terrace. Banana Floors installs LVP, wood, laminate, tile and carpet in Tigard, including in homes where the family is living through the project.",
 sections=[
  ("From mid-century ranches to River Terrace", P(
    "Tigard's older neighborhoods around downtown Main Street and the Greenburg area include postwar ranches and 1960s–1970s homes, many with carpet over plywood and kitchens that have been remodeled more than once. Summerlake and other neighborhoods from the 1970s through the 1990s add split-levels and two-story homes with family rooms and carpeted stairs.",
    "On the western edge, River Terrace is one of the area's newer developments, with homes built in recent years. Bull Mountain's hillside homes, partly in the city and partly in unincorporated Washington County, range from 1990s two-story houses to larger custom homes, some with daylight basements.")),
  ("Planning a project in an occupied home", P(
    "Most flooring projects in Tigard happen while the household is still living there. A little planning keeps the home usable:") + UL(
    "<strong>Phase the work:</strong> do bedrooms on one day and main living areas on another, or one floor at a time",
    "<strong>Plan the kitchen:</strong> decide when the refrigerator, range and dishwasher will be moved and reconnected",
    "<strong>Clear the rooms:</strong> tell us which furniture you will move and which needs help, and where it can go",
    "<strong>Pets and kids:</strong> plan a safe space away from tools, dust and open doors",
    "<strong>Access:</strong> note parking, gate codes and where materials can be staged") + P(
    "Share any move-in date, event or rooms that must stay usable, and we will build the schedule around them after reviewing the scope.")),
  ("Materials that suit Tigard homes", P(
    LVP + " is a practical choice for open kitchens and family rooms where kids and pets are part of daily life, and it installs relatively quickly, which helps in occupied homes. " + CARPET + " remains popular for bedrooms and stairs. " + EW + " suits hillside homes with lower levels on concrete, and " + HW + " works well on above-grade wood subfloors. In bathrooms and laundry rooms, " + TILE + " is the most water-tolerant option.",
    "Daylight basements and slab-on-grade rooms should have the concrete checked for moisture before installation; see our " + WATER + " guide.")),
  ("Removal, preparation and finishing", P(
    "In older Tigard homes, removing the old floor often reveals squeaks, seams or soft spots that are best fixed while the subfloor is exposed (" + PREP + "). Decide early whether baseboards will be reused or replaced (" + TRIM + ") and whether stairs are part of the project (" + STAIRS + "). Our " + COST + " explains how those items appear in a quote.")),
 ],
 hoods_h2="Tigard neighborhoods we serve",
 hoods_intro="Our Tigard service area includes neighborhoods such as:",
 neighborhoods=["Downtown Tigard and Main Street", "Summerlake", "Bull Mountain", "River Terrace", "Greenburg", "Tigard Triangle", "Metzger and Durham (nearby)", "King City (nearby)"],
 faqs=[
  ("Can I stay in my home during flooring installation?", "Most homeowners do. Phasing the work by room or floor and planning around the kitchen helps. Share rooms that must stay usable and any deadlines."),
  ("How do you handle appliances and furniture?", "Tell us what needs to move when you request your estimate so it is included in the scope and schedule."),
  ("What flooring works best for hillside homes with daylight basements?", "LVP, tile or engineered wood are common on lower-level concrete. Slab moisture should be checked before installation."),
  ("Do you install flooring in River Terrace and Bull Mountain?", "Yes. Both are part of our Tigard service area."),
 ]),
# ------------------------------------------------------------------ Lake Oswego
dict(slug="flooring-installation-lake-oswego-or", name="Lake Oswego", state="OR", image="engineered",
 nearby=["flooring-installation-portland-or", "flooring-installation-tigard-or", "flooring-installation-oregon-city-or", "flooring-installation-beaverton-or"],
 title="Flooring Installation Lake Oswego, OR | Banana Floors",
 desc="Lake Oswego hardwood, engineered wood, LVP, tile and carpet installation with detail-focused finishing. Request a free estimate.",
 h1="Flooring installation in Lake Oswego, OR",
 intro="Lake Oswego's homes range from 1920s cottages near the lake to mid-century hillside houses and large custom homes. Banana Floors installs hardwood, engineered wood, LVP, laminate, tile and carpet here, with careful attention to wood floors, transitions and finishing details.",
 sections=[
  ("Wood floors and the details that make them work", P(
    "Wood is a common choice in Lake Oswego, and the details decide whether a new wood floor looks like it belongs. Board width and species should suit the house: narrower oak strip is typical of older homes, while wider planks in white oak are popular in remodeled and newer homes. Prefinished boards install with less disruption; site-finished floors allow custom stain and a flush surface but need drying time.",
    "Where a new floor meets an existing one, the transition should be deliberate: a flush seam, a threshold, or a change in direction at a doorway. We plan those locations, along with baseboards, shoe molding and door clearances, before installation begins (" + TRIM + ").")),
  ("Homes across Lake Oswego", P(
    "Neighborhoods such as First Addition, Evergreen and areas around Old Town include early-20th-century cottages and English-style homes, often with original oak or fir floors and character trim worth preserving. If the existing wood is sound, " + REFINISH + " is often the first option to consider. Mountain Park, Palisades and Forest Highlands have many homes from the 1960s through the 1980s, often on hillsides with split floor plans and daylight lower levels. Westlake, Lake Grove and the Lakewood area add a range of styles, including larger homes from more recent decades.",
    "That variety means very different subfloors: old planks with gaps and nails, plywood over joists, and concrete in lower levels. We check what is actually under your floor before recommending a product (" + PREP + ").")),
  ("Hillsides, lower levels and moisture", P(
    "Hillside lots are common in Lake Oswego, and many homes have daylight basements or lower levels partly below grade. Solid hardwood is generally not recommended on below-grade concrete; " + EW + " (glued or floated over the right underlayment), rigid-core " + LVP + " and " + TILE + " are better fits. Concrete moisture should be checked before anything is installed.",
    "Homes near the lake, creeks and wooded slopes can also have damp crawlspaces. A moisture check of the wood subfloor before installing " + HW + " helps avoid cupping later.")),
  ("Planning a Lake Oswego flooring project", UL(
    "Choose a wood species, width and finish that suit the house, and order samples to see them in your light",
    "Plan transitions to any floors that are staying, and decide on baseboards",
    "Check lower-level slabs and crawlspaces for moisture",
    "Include stairs in the plan if the flooring continues up or down (" + STAIRS + ")") + P(
    "Compare material tiers in the Price Guide, then read our " + COST + " for the installation side.")),
 ],
 hoods_h2="Lake Oswego neighborhoods we serve",
 hoods_intro="We work throughout Lake Oswego, including neighborhoods such as:",
 neighborhoods=["First Addition and Evergreen", "Old Town", "Lake Grove", "Westlake", "Palisades", "Forest Highlands", "Mountain Park", "Lakewood and Bryant", "Blue Heron and Holly Orchard"],
 faqs=[
  ("What wood flooring works best in Lake Oswego homes?", "Oak remains the most common choice. Narrow strip suits many older homes; wider white oak planks are popular in remodels. Engineered wood is a strong option for lower levels and over concrete."),
  ("Can new hardwood blend with my existing floors?", "A perfect match is difficult, but compatible species, width and finish, plus a well-placed transition, can blend new and existing floors. Send photos for a review."),
  ("Is solid hardwood OK in a daylight basement?", "Solid hardwood is generally not recommended below grade or directly on concrete. Engineered wood, LVP or tile are better choices there."),
  ("Do you install flooring in Mountain Park and Westlake?", "Yes. Both are part of our Lake Oswego service area."),
 ]),
# ------------------------------------------------------------------ Vancouver, WA
dict(slug="flooring-installation-vancouver-wa", name="Vancouver", state="WA", image="lvp",
 nearby=["flooring-installation-portland-or", "flooring-installation-gresham-or", "flooring-installation-beaverton-or", "flooring-installation-happy-valley-or"],
 title="Flooring Installation Vancouver, WA | Banana Floors",
 desc="Vancouver, WA flooring installation for LVP, hardwood, laminate, tile and carpet. Banana Floors is based in Portland, OR. Oregon CCB 209244.",
 h1="Flooring installation in Vancouver, WA",
 intro="Vancouver, Washington sits just north of Portland across the Columbia River and is part of the same metro. Banana Floors is based in the Portland, Oregon area and installs LVP, hardwood, engineered wood, laminate, tile and carpet in Vancouver homes, with removal and preparation planned before the new floor goes in.",
 sections=[
  ("Vancouver homes and what is under the floor", P(
    "Vancouver was incorporated in 1857, and the housing stock still shows that span of time. Neighborhoods such as Hough, Arnada, Shumway, Carter Park and Lincoln have many early-1900s houses, some with original fir or oak, plaster walls and floors that have settled. Downtown and the Esther Short area mix those older blocks with newer infill, townhomes and waterfront buildings on concrete.",
    "Farther out, central and west Vancouver include postwar ranches and 1970s–1990s two-story homes, often with carpet over plywood and sheet vinyl or older laminate in the kitchen. East-side neighborhoods such as Fisher's Landing, Cascade Park and Image, and the Orchards area to the northeast, grew later. Many of those houses still have builder-grade carpet on the stairs and bedrooms and a hard floor that is ready for its first replacement.")),
  ("Wet winters, gorge winds and the subfloor", P(
    "Vancouver shares Portland's wet fall-to-spring season, and it sits close enough to the Columbia River Gorge that winter east winds can turn the indoor air cold and dry for days at a time. Wood floors respond to both: small seasonal gaps when the heat is running are normal, while cupping usually means moisture from a crawlspace or a slab should be fixed first.",
    "A lot of Vancouver houses are built over crawlspaces, and newer homes, townhomes and waterfront buildings are often on concrete. We check moisture in wood subfloors and look at slab conditions before recommending a product. Rigid-core " + LVP + " and " + TILE + " are common on slabs and in entries; " + EW + " handles humidity swings better than solid boards when a real wood surface is the goal. See " + WATER + " for wet rooms and lower levels.")),
  ("Based in Portland, working in Vancouver", P(
    "Banana Floors is a Portland, Oregon flooring contractor. The license we publish is Oregon CCB 209244: insured, bonded and licensed under that Oregon number. We do not list a Washington contractor license. Vancouver is part of the service area because it is the city directly across the river, a short trip on the Interstate 5 or Interstate 205 bridge, and the same crews plan Portland and Vancouver floors.",
    "A Vancouver quote follows the same steps as a Portland one. Send room sizes, photos and the age of the home, and we review " + REMOVAL + ", " + PREP + " and " + TRIM + " before anyone is scheduled. Measurements and site conditions are confirmed in person. Our " + COST + " shows how those pieces sit next to the material price.")),
  ("Floors that suit Vancouver houses", UL(
    "<strong>LVP</strong> for kitchens, entries, rentals and slab-on-grade rooms",
    "<strong>Engineered wood</strong> for open living areas that need a real wood surface and better seasonal stability",
    "<strong>Solid hardwood</strong> above grade, on a dry wood subfloor, including where original fir or oak is worth continuing",
    "<strong>Laminate</strong> for bedrooms and offices on a tighter budget (" + LAM + ")",
    "<strong>Carpet</strong> for bedrooms and stairs (" + CARPET + ")",
    "<strong>Tile</strong> for bathrooms, laundry rooms and mudrooms") + P(
    "If an original wood floor is still sound, " + REFINISH + " is worth considering before a full replacement. Two-story homes should include " + STAIRS + " in the plan when the main floor changes. Landlords can read " + RENTAL + " for product and scheduling notes.")),
 ],
 hoods_h2="Vancouver neighborhoods we serve",
 hoods_intro="We install flooring in Vancouver, WA, including neighborhoods such as:",
 neighborhoods=["Downtown Vancouver and Esther Short", "Uptown Village", "Hough, Arnada and Shumway", "Carter Park and Lincoln", "Fisher's Landing", "Cascade Park and Image", "Fruit Valley, Minnehaha and Bagley Downs", "Orchards (nearby)", "Hazel Dell and Salmon Creek (nearby)", "Felida (nearby)"],
 faqs=[
  ("Do you install flooring in Vancouver, WA?", "Yes. Vancouver is part of our Portland–Vancouver service area. Banana Floors is based in the Portland, Oregon area. Call or text (503) 421-1730 for a free preliminary estimate."),
  ("Which contractor license covers the work?", "Banana Floors is insured, bonded and licensed under Oregon CCB 209244. We are based in Portland, Oregon, and we serve Vancouver, WA. We do not list a Washington contractor license number."),
  ("What flooring handles Vancouver's wet winters and dry east winds?", "Rigid-core LVP and engineered wood handle those seasonal swings well. Solid hardwood is a strong choice above grade on a dry wood subfloor. We check subfloor or slab moisture before installation."),
  ("Do you work in Fisher's Landing, Cascade Park and Orchards?", "Yes. Fisher's Landing and Cascade Park are in Vancouver. Orchards, just northeast of the city, is in the same service area."),
 ]),
]

# Additional city-specific planning sections (appended to each page's sections).
_EXTRA = {
 "Portland": ("Matching a new floor to an older house", P(
   "In older Portland homes, the hardest part of a flooring project is often the meeting point between old and new. A remodeled kitchen may sit next to a dining room with original fir; a bathroom may be a half inch higher than the hallway after tile and backer go down. We plan where each material starts and stops, how the floor height changes at each doorway, and whether thresholds, reducers or a change in plank direction will look most natural.",
   "Plaster walls and old trim also affect the finish. Original baseboards can often be removed carefully and reinstalled, or left in place with new shoe molding. Tell us which trim you want to keep, and we will build the plan around it.")),
 "Gresham": ("Rentals, duplexes and multi-unit homes in Gresham", P(
   "Gresham has a large share of rental housing, from single-family rentals to duplexes and apartment communities. For those properties, the goal is a floor that survives several tenancies and can be repaired without replacing a whole room. Rigid-core LVP with a thicker wear layer, durable stain-resistant carpet in bedrooms, and a consistent product across units are common choices.",
   "When you request an estimate for a rental, include the vacancy dates, the number of units and rooms, access instructions and whether other trades are scheduled. Turnover timing is usually the tightest part of the project, so the earlier we see the scope, the easier it is to plan.")),
 "Happy Valley": ("Kitchens, mudrooms and busy entries", P(
   "In many Happy Valley homes the garage opens into a mudroom or laundry area, and the kitchen is just a few steps away. Those rooms see wet shoes, sports gear and pets every day, so they benefit from water-tolerant floors such as rigid-core LVP or porcelain tile.",
   "If you are updating the kitchen at the same time, decide early whether the floor will run under the cabinets and island or stop at them. Many floating floors should not be pinned under heavy cabinets, and appliance heights matter around dishwashers and refrigerators. We match the order of work to the product's installation requirements so the manufacturer's warranty stays intact.")),
 "Clackamas": ("Moving furniture and keeping your home usable", P(
   "Many Clackamas projects are in occupied homes and apartments where there is not much space to move furniture. Before installation, it helps to decide which rooms will be done first, where furniture and boxes can go, and which items need help moving. Appliances such as refrigerators, ranges and washers may need to be disconnected and reset.",
   "In condos and apartments, plan for parking, elevator access and where old flooring and packaging will be removed. Share those details when you request a quote, and we will reflect them in the scope and schedule.")),
 "Oregon City": ("Floors on the bluff and in the hills", P(
   "Oregon City's geography, with downtown along the river and neighborhoods on the bluff and the hills above, means a mix of foundations. Older homes may have low crawlspaces with limited access, while newer hillside homes can have lower levels on concrete. Each affects which floor is a good fit.",
   "For a crawlspace home, we check the wood subfloor for moisture and soft spots before installing anything. For lower-level slabs, rigid-core LVP, tile or engineered wood approved for concrete are common choices, with a vapor barrier if the manufacturer requires one. The floor you see is only as good as what is under it.")),
 "Beaverton": ("Open living areas and one continuous floor", P(
   "Many Beaverton homeowners want to replace a patchwork of carpet, vinyl and older laminate with one continuous floor across the main level. Running one product from the entry through the kitchen and living areas makes the house feel larger and simplifies cleaning.",
   "A continuous floor needs planning. Floating floors have maximum run lengths and may need a transition in a doorway, kitchen islands and cabinets affect where the floor goes, and the height has to work at stairs, fireplaces and exterior doors. We map the layout first so transitions, if needed, land in sensible places.")),
 "Tigard": ("Two-story homes and stair updates", P(
   "Two-story homes from the 1980s and 1990s are common in Tigard, usually with carpeted stairs between a main floor and bedrooms upstairs. When the main floor gets a new hard surface, the stairs often stand out. Options include new stair carpet, LVP with matching stair nosing, or wood treads with painted risers.",
   "Stairs are quoted per step, and changing materials can change the height of the top and bottom steps, so they belong in the plan from the start. Count the steps, note any landings or open sides, and include photos from the top and bottom of the stairs with your estimate request.")),
 "Vancouver": ("Older blocks and newer east-side houses", P(
   "A flooring plan in Vancouver usually starts with which side of the city the house is on. In Hough, Arnada, Shumway and the other older neighborhoods, doorways may be out of square, original trim may be worth saving, and a new floor often has to meet fir or oak that is staying in the next room. Floor height at those thresholds matters more than the plank color.",
   "In Fisher's Landing, Cascade Park, Image and other newer east-side houses, the usual job is replacing builder carpet and entry-level hard floors across an open main level, plus a carpeted stair. Floating floors have run-length limits, and kitchen islands change where the floor can go. Tell us the year the house was built and what is on the floor now so removal, preparation and transitions are in the quote from the start.")),
 "Lake Oswego": ("Carpet, tile and the rest of the house", P(
   "Wood gets most of the attention, but Lake Oswego homes need other floors too. Bedrooms and media rooms are often carpeted for comfort and quiet, with pad matched to the carpet manufacturer's warranty requirements. Bathrooms, laundry rooms and mudrooms do best with porcelain or ceramic tile over the right underlayment or membrane.",
   "Where several materials meet, such as a tiled entry next to a wood hallway and a carpeted stair, the heights and transitions need to be planned together. We include those edges in the scope so the finished floors read as one project rather than separate rooms.")),
}
for _c in CITIES:
    _c["sections"].insert(len(_c["sections"]) - 1, _EXTRA[_c["name"]])
