"""Supporting service pages (all confirmed offered by Banana Floors, Oct 2026)."""
from .services import P, UL, H3, L, PRICES, COST, SUBFLOOR, REMOVAL, STAIRS, TRIM, WATERPROOF

LVP = L("/flooring/lvp-flooring-portland.html", "LVP")
HARDWOOD = L("/flooring/hardwood-flooring-portland.html", "hardwood")
CARPET = L("/flooring/carpet-installation-portland.html", "carpet")
TILE = L("/flooring/tile-flooring-portland.html", "tile")
LAMINATE = L("/flooring/laminate-flooring-portland.html", "laminate")

EXTRA = [
# ------------------------------------------------------------------ Refinishing
dict(slug="hardwood-floor-refinishing-portland", nav="Hardwood refinishing", image="hardwood",
 img_alt="Refinished-look hardwood floor in a living room",
 title="Hardwood Floor Refinishing Portland, OR | Banana Floors",
 desc="Hardwood floor refinishing in Portland: sanding, stain and new finish, or a screen and recoat for worn finishes. Oak, fir and engineered floors. Free estimate.",
 eyebrow="Portland Metro · Hardwood refinishing",
 h1="Hardwood floor refinishing in Portland",
 intro="Many Portland-area homes already have a good wood floor under a worn finish, old carpet or decades of scratches. Banana Floors refinishes hardwood floors as well as installing new ones: full sanding and refinishing to bare wood, or a screen and recoat when only the finish is tired.",
 schema_name="Hardwood floor refinishing",
 glance_h2="Refinishing at a glance",
 points=[("Sand and refinish", "Back to bare wood"), ("Screen and recoat", "Renews a worn finish"), ("Stain or natural", "Change the color"), ("Oak, fir, engineered", "Wood type decides the plan")],
 sections=[
  ("Refinish, recoat or replace?", P(
    "Refinishing is often the most practical way to bring back a solid hardwood floor. Solid boards are usually around 3/4 inch thick, and the wood above the tongue can be sanded several times over the life of the floor. If the boards are sound and there is enough wood left, sanding and new finish can make an old floor look close to new.",
    "Not every floor is a refinishing candidate. Boards that have been sanded many times, deep pet stains that run into the wood, water damage that has cupped or softened boards, and very thin engineered veneers can limit what sanding can fix. In those cases a partial repair, board replacement or new " + HARDWOOD + " may make more sense. We look at the floor and tell you what we see.")),
  ("Two kinds of refinishing", H3("Full sand and refinish") + P(
    "The floor is sanded to bare wood in several passes with progressively finer abrasives, edges and corners are sanded separately, and the floor is vacuumed before stain (if you want a new color) and several coats of finish. A full sand removes most scratches, dents in the finish, old discolored finish and minor unevenness between boards.") +
    H3("Screen and recoat") + P(
    "If the finish is dull and lightly scratched but the wood itself is not worn through, the existing finish can be abraded (screened) and a fresh coat applied. It does not change the color or remove deep scratches, but it costs less, takes less time and can extend the life of a floor between full refinishes. It only works over a compatible, clean finish; floors that have been waxed or treated with some polish products may need a full sand instead.")),
  ("Wood floors in Portland-area homes", P(
    "Older Portland homes often have Douglas fir or oak floors. Fir is a softer wood, so it dents more easily and sands differently from oak, and it can look blotchy with some stains; many owners choose a clear finish that shows its warm color. Oak is harder and takes stain more evenly. Mid-century homes in the suburbs sometimes have oak strip flooring hidden under carpet.",
    "If you have found wood under carpet, the condition varies: tack strips leave nail holes around the edges, pad can stain the surface, and areas that were never covered may differ in color from the rest. Removing the carpet first, or lifting a corner in a closet, helps us judge what refinishing can do (" + REMOVAL + ").")),
  ("Stain color and finish choices", P(
    "A full sand gives you the chance to change color. Sample stains on the sanded floor itself, because the same stain looks different on oak and fir and on boards from different eras. A natural finish with no stain is also a popular choice and makes future recoats simpler.",
    "Finish sheen (matte, satin or semi-gloss) changes how much scratches and dust show; lower sheens hide more everyday wear. Water-based and oil-based finishes differ in color, odor and drying time. We go over the options and the product's recoat and cure guidance with you before work starts.")),
  ("Repairs, stairs and the rest of the room", P(
    "Refinishing is often combined with other work. Damaged or missing boards can be replaced and woven in before sanding so the patch blends after finishing. Stair treads can be refinished to match the floors (" + STAIRS + "). Baseboards and shoe molding are often removed, replaced or repainted around a refinish (" + TRIM + ").",
    "If you are refinishing some rooms and installing new floors in others, we can plan the transitions so the old and new floors meet cleanly.")),
  ("Planning your refinishing project", UL(
    "Plan for the rooms to be empty of furniture and off-limits while sanding and finishing are under way",
    "Ask about drying and cure times before moving furniture back or putting down rugs",
    "Pets and people should stay off fresh finish for the time the finish manufacturer specifies",
    "Sanding makes dust and finishing makes odor; plan ventilation and access for the household",
    "Homes built before 1978 may have lead paint on nearby trim, so tell us your home's age before work around painted surfaces") + P(
    "Send photos of the floors, the approximate square footage and what bothers you about the current finish, and we will follow up with a preliminary quote. Final scope is confirmed after we see the wood in person.")),
 ],
 faqs=[
  ("Do you refinish hardwood floors?", "Yes. Banana Floors refinishes existing hardwood floors, including full sanding and refinishing and screen-and-recoat work, as well as installing new hardwood."),
  ("How do I know if my floor can be refinished?", "Solid hardwood can usually be sanded several times. Look at a floor vent or threshold to see the board thickness, and send photos. Very thin engineered veneers and boards that have been sanded many times may not be candidates."),
  ("What is the difference between refinishing and a screen and recoat?", "Refinishing sands the floor to bare wood and applies new stain and finish. A screen and recoat lightly abrades the existing finish and adds a new coat; it renews the surface but does not remove deep scratches or change color."),
  ("Can I change the color of my hardwood floors?", "Yes, with a full sand. The new stain is applied to bare wood. Sample colors on your floor first, because oak and fir take stain differently."),
  ("Can fir floors be refinished?", "Yes. Fir is softer than oak, so it is sanded with care, and many owners prefer a clear finish that shows its natural color."),
 ]),
# ------------------------------------------------------------------ Stairs
dict(slug="stair-flooring-installation-portland", nav="Stair flooring", image="hardwood",
 img_alt="Hardwood-look flooring in a living room", show_prices=True, price_keys=["LVP / Vinyl", "Solid Hardwood", "Carpet"],
 price_h2="Material ranges for common stair materials",
 title="Stair Flooring Installation Portland, OR | Banana Floors",
 desc="Plan new stair flooring in Portland: carpet, LVP stair nosing or hardwood treads to match your floors. Learn what affects stair quotes. Free estimate.",
 eyebrow="Portland Metro · Stairs",
 h1="Stair flooring installation in Portland",
 intro="Stairs connect the floors you have chosen, and they are the most detailed part of many flooring projects. When you replace flooring upstairs or down, we help you plan how the stairs will match, whether that means new carpet, LVP with matching stair nosing, or hardwood treads.",
 schema_name="Stair flooring installation",
 glance_h2="Stair flooring options",
 points=[("Carpet", "Soft, quiet, budget-friendly"), ("LVP with stair nosing", "Matches LVP floors"), ("Hardwood treads", "Classic and refinishable"), ("Quoted per stair", "Count, shape and landings")],
 sections=[
  ("Why stairs are quoted separately", P(
    "A flight of stairs has a small floor area but a lot of cutting, fitting and fastening. Every tread and riser is measured and fit individually, nosings have to line up, and the finished stairs need to feel solid and safe. That is why stairs are usually priced by the step rather than by the square foot.",
    "When you request an estimate, tell us how many steps there are, whether the stairs are open on one or both sides, and whether there are landings, winders or a curve. Photos from the bottom and the top of the flight help a lot.")),
  ("Common ways to update stairs", H3("New carpet on stairs") + P(
    "Carpet is quiet and comfortable and usually the simplest update. Stair carpet can be installed in a waterfall style, which rolls over the nose, or wrapped tightly around each nose. Durable nylon carpet holds up well on stairs. See our " + CARPET + " page for fiber and pad advice.") +
    H3("LVP with matching stair nosing") + P(
    "If your main floors are " + LVP + ", many product lines offer a matching stair nose trim so the stairs continue the same look. The tread surface is covered with plank and finished with the nosing. Matching trim is product-specific, so check availability before choosing a floor.") +
    H3("Hardwood treads and risers") + P(
    "Solid wood treads, often paired with painted risers, give a classic look and can be refinished later. They work with " + HARDWOOD + " floors and can complement other materials.")),
  ("Safety and consistency", P(
    "Changing stair materials can change the height of the first and last step. Residential building codes limit how much riser heights may vary within a flight, so we look at how the new material affects the top and bottom steps before work begins.",
    "We also look for loose treads, squeaks and damaged stringers when the old covering comes off. If repairs are needed beyond the flooring, we will tell you what we found before proceeding.")),
  ("Planning stairs with the rest of your floor", UL(
    "Choose the floor product first, then confirm that matching stair nosing or trim is available",
    "Decide whether risers will be covered, painted or left as they are",
    "Note any railings, balusters or skirt boards that meet the treads",
    "Include stair removal and disposal in the scope (" + REMOVAL + ")") + P(
    "Use the " + PRICES + " for material budgets and send us your stair count and photos for a preliminary quote.")),
 ],
 faqs=[
  ("Do you install flooring on stairs?", "Yes. Stair flooring is one of our services. Tell us the number of steps, the shape of the stairs and the material you are considering so your quote covers them."),
  ("Can I put LVP on my stairs?", "Often, yes, using the manufacturer's matching stair nose trim where it is available. Check that the product line you like offers stair nosing before you buy."),
  ("Why are stairs priced per step?", "Each tread and riser is measured, cut and fit individually, which takes far more time than open floor area. Pricing per step reflects that work."),
  ("Can stair carpet be replaced with hardwood?", "In many homes, yes. The condition of the treads underneath, the stair construction and the railing details decide how it is done. Photos help us review the options."),
 ]),
# ------------------------------------------------------------------ Subfloor
dict(slug="subfloor-prep-floor-leveling-portland", nav="Subfloor prep & leveling", image="laminate",
 img_alt="Flooring installed in a home office",
 title="Subfloor Prep & Floor Leveling Portland | Banana Floors",
 desc="Flatness, moisture and squeaks decide how long a new floor lasts. How we review and prepare subfloors before Portland flooring installs.",
 eyebrow="Portland Metro · Floor preparation",
 h1="Subfloor preparation and floor leveling in Portland",
 intro="Most flooring problems start underneath the floor. Banana Floors reviews the subfloor as part of every replacement and identifies the preparation a new floor needs, from fixing squeaks to flattening high and low spots, before installation begins.",
 schema_name="Subfloor preparation and floor leveling",
 glance_h2="What floor prep covers",
 points=[("Flatness", "Grinding high spots, filling low spots"), ("Squeaks", "Re-fastening loose subfloor"), ("Moisture", "Checking wood and concrete"), ("Repairs", "Damaged panels identified early")],
 sections=[
  ("Flat versus level", P(
    "A floor can be flat without being perfectly level, and for most floor coverings flatness is what matters. Manufacturers publish flatness tolerances, commonly expressed as a maximum deviation over a set distance. Floating " + LVP + " and " + LAMINATE + " floors are especially sensitive: if the subfloor dips, the planks flex at the joints and can click, separate or wear out early.",
    "Before installation we check the subfloor with a long straightedge and mark high and low areas, so the preparation plan is based on what the floor actually needs.")),
  ("Common preparation work", H3("Fixing squeaks and loose panels") + P(
    "Squeaks usually come from subfloor panels moving against joists or fasteners. With the old floor removed, loose areas can be re-fastened before the new floor covers them.") +
    H3("Grinding and patching") + P(
    "High spots on concrete can be ground down; seams and low areas on wood or concrete can be filled with a patching compound designed for the purpose.") +
    H3("Self-leveling underlayment") + P(
    "Larger dips may call for a pourable self-leveling underlayment. It needs proper priming, the right thickness and time to cure before flooring goes on top.") +
    H3("Replacing damaged subfloor") + P(
    "Water-damaged or delaminated panels, often near toilets, tubs, dishwashers and exterior doors, may need to be cut out and replaced. The full extent is sometimes only visible after the old floor is removed (" + REMOVAL + ").")),
  ("Moisture in Portland-area homes", P(
    "Many homes in the Portland area sit over crawlspaces or concrete slabs and basements. Crawlspaces without an effective vapor barrier can push moisture up into wood subfloors, and concrete can release moisture for a long time. Too much moisture can cause wood floors to cup and can affect adhesives under resilient floors.",
    "We check moisture in wood subfloors and look at concrete conditions before recommending a product or underlayment. If a crawlspace, drainage or plumbing problem needs attention first, we will tell you rather than covering it up.")),
  ("How preparation shows up in your quote", P(
    "Some preparation can be estimated from photos and measurements; some can only be confirmed once the existing floor is up. We describe the visible conditions in your preliminary quote and discuss any additional preparation with you before proceeding. Our " + COST + " explains how prep fits alongside material and installation.")),
 ],
 faqs=[
  ("Why does my new floor need subfloor prep?", "Most floor coverings require a flat, solid, dry subfloor for warranty coverage and long-term performance. Preparation addresses squeaks, uneven areas and damage before they are covered."),
  ("Can you tell how much leveling is needed from photos?", "Photos help start the conversation, but flatness is measured on site, and some issues only show once the old floor is removed. Any added preparation is discussed with you before work continues."),
  ("What is self-leveling underlayment?", "A pourable cement-based product that flattens larger low areas. It needs primer, the correct thickness and cure time before flooring is installed."),
  ("Do concrete basement floors need moisture testing?", "Concrete moisture should be checked before installing most flooring on a slab, especially wood products and glue-down floors. The flooring manufacturer specifies the acceptable range."),
 ]),
# ------------------------------------------------------------------ Removal
dict(slug="flooring-removal-portland", nav="Flooring removal", image="carpet",
 img_alt="Carpet in a living room",
 title="Old Flooring Removal Portland, OR | Banana Floors",
 desc="Carpet, laminate, vinyl, wood and tile removal as part of a Portland flooring replacement. What to expect, older-home precautions and disposal.",
 eyebrow="Portland Metro · Removal & haul-away",
 h1="Old flooring removal in Portland",
 intro="Most flooring replacements start with taking the old floor out. Banana Floors handles removal as part of replacement projects, so the subfloor can be inspected and prepared properly before the new floor goes in.",
 schema_name="Flooring removal",
 glance_h2="What removal involves",
 points=[("Carpet & pad", "Plus tack strip and staples"), ("Floating floors", "Laminate and click-lock LVP"), ("Glued & nailed floors", "Vinyl, wood and tile"), ("Inspection", "Subfloor reviewed after removal")],
 sections=[
  ("Why removal matters", P(
    "Installing over an old floor can save time, but it often hides problems: soft spots, old water damage, squeaks and uneven areas. Removing the existing floor lets us see the subfloor, fix what needs fixing (" + SUBFLOOR + ") and install the new floor at the right height for doorways and appliances.",
    "Some products can go over certain existing hard floors. When that is an option, we will discuss it. Carpet and pad always come out first.")),
  ("What different floors take to remove", H3("Carpet and pad") + P(
    "Usually the quickest: carpet and pad are cut and rolled, and tack strip and staples are pulled.") +
    H3("Laminate and floating LVP") + P(
    "Floating floors come up board by board along with the underlayment.") +
    H3("Glue-down vinyl, sheet vinyl and LVT") + P(
    "Adhered floors take longer, and adhesive residue may need to be removed or covered depending on the new product.") +
    H3("Nailed hardwood and tile") + P(
    "Nailed wood and mortar-set tile are the most labor-intensive to remove and can produce dust and debris that need containment.")),
  ("Older homes: asbestos and lead", P(
    "Many Portland-area homes were built long before current materials rules. Some older sheet vinyl, vinyl tiles and their adhesives can contain asbestos, and painted trim in homes built before 1978 may contain lead paint. These materials should not be torn out until they have been evaluated.",
    "Oregon has asbestos survey requirements for many renovation projects in older homes, and Washington has its own rules. If your home is older and has old resilient flooring or painted trim that will be disturbed, tell us the year it was built so the right steps are taken first. Testing and abatement, when needed, are done by licensed specialists.")),
  ("Disposal and cleanup", P(
    "Tell us whether you want the old flooring hauled away so it can be included in your scope. We leave the work area cleared and ready for preparation and installation. Removal is a line item in most quotes; our " + COST + " explains how it fits with material and installation.")),
 ],
 faqs=[
  ("Is old flooring removal included in a quote?", "Yes, we remove old flooring and can include it in your quote. Tell us what is on the floor now, how many rooms and whether there are stairs."),
  ("Can new flooring go over my old floor?", "Sometimes, depending on the new product and the condition of the existing floor. Carpet must always be removed. Send photos so we can review the options."),
  ("What if my old vinyl might contain asbestos?", "Do not disturb it. Some older vinyl flooring and adhesives contain asbestos. Tell us the age of your home; testing and any abatement must be handled by licensed specialists before removal."),
  ("Do you haul away the old flooring?", "Haul-away can be part of your scope. Let us know when you request your estimate."),
 ]),
# ------------------------------------------------------------------ Trim
dict(slug="baseboard-trim-installation-portland", nav="Baseboards & transitions", image="engineered",
 img_alt="Engineered wood flooring in a dining room",
 title="Baseboards, Trim & Transitions Portland | Banana Floors",
 desc="Baseboards, shoe molding, transitions and stair nosing finish a new floor. How we plan trim and doorways on Portland flooring projects.",
 eyebrow="Portland Metro · Finishing details",
 h1="Baseboards, trim and floor transitions in Portland",
 intro="The edges are what you notice in a finished floor: where it meets the walls, the doorways and the next room. Banana Floors plans baseboards, shoe molding and transitions as part of the flooring scope so the result looks complete.",
 schema_name="Baseboard, trim and floor transition installation",
 glance_h2="Finishing details we plan for",
 points=[("Baseboards", "Reuse or replace"), ("Shoe / quarter round", "Covers expansion gaps"), ("Transitions", "Between rooms and materials"), ("Door clearance", "Undercut jambs and doors")],
 sections=[
  ("Reuse or replace baseboards?", P(
    "Floating floors such as " + LVP + " and " + LAMINATE + " need an expansion gap at the walls. That gap is covered either by removing and reinstalling baseboards, or by leaving baseboards in place and adding shoe molding or quarter round.",
    "Reusing existing baseboards keeps costs down and preserves original trim, which matters in older Portland homes with wide, painted base. Replacing baseboards gives a fresh, clean line and is common when the old base is damaged or the floor height is changing. Tell us your preference so it is in the scope.")),
  ("Transitions between floors", P(
    "Wherever the new floor meets another surface (tile, carpet, an existing hardwood floor) or ends at a door, a transition piece finishes the edge.") +
    H3("T-molding") + P("Joins two floors of similar height, often used in doorways between floating floors.") +
    H3("Reducer") + P("Steps down from a thicker floor to a thinner one, such as hardwood to vinyl.") +
    H3("End cap or threshold") + P("Finishes the floor at sliding doors, fireplaces or exterior doors.") +
    H3("Carpet edge") + P("Ties carpet to a hard floor cleanly.") + P(
    "Many floor lines sell color-matched transitions. Matching trim is product-specific, so we check availability before you order.")),
  ("Door jambs and clearances", P(
    "To get a clean edge at doors, door casings and jambs are typically undercut so the new floor slides underneath instead of being scribed around them. A thicker floor may also require trimming interior doors so they swing freely. We look at floor height changes at every doorway, including exterior doors and appliance openings such as dishwashers.")),
  ("Painted trim in older homes", P(
    "If your home was built before 1978, painted baseboards and casings may contain lead paint. Work that disturbs it is subject to lead-safe practices. Let us know the age of your home when requesting an estimate (see " + REMOVAL + ").")),
 ],
 faqs=[
  ("Are baseboards included in a flooring quote?", "Yes, we install baseboards and trim and can include them in your flooring quote. Tell us whether you want to reuse existing baseboards, add shoe molding, or replace them so the quote matches what you expect."),
  ("What is the difference between shoe molding and quarter round?", "Both are small trim pieces that cover the gap between the floor and baseboard. Shoe molding is slimmer and more upright; quarter round is a true quarter circle."),
  ("Why do floating floors need an expansion gap?", "Floating floors expand and contract with temperature and humidity. The gap at the walls lets the floor move without buckling; trim covers it."),
  ("Can transitions match my new floor?", "Many flooring lines sell color-matched transition pieces and stair nosing. Availability varies by product, so check before ordering."),
 ]),
# ------------------------------------------------------------------ Waterproof
dict(slug="waterproof-flooring-portland", nav="Waterproof flooring", image="tile",
 img_alt="Tile flooring in a laundry room", show_prices=True, price_keys=["LVP / Vinyl", "Tile", "Laminate"],
 price_h2="Material ranges for water-tolerant floors",
 title="Waterproof Flooring Installation Portland | Banana Floors",
 desc="Waterproof and water-resistant flooring for Portland kitchens, baths, basements and entries. Compare LVP, tile and laminate. Free estimate.",
 eyebrow="Portland Metro · Wet and high-moisture rooms",
 h1="Waterproof flooring for Portland homes",
 intro="Rainy seasons, muddy entries, basements and busy kitchens all ask a lot of a floor. Here is how the water-tolerant floors we install compare, and what waterproof really means on the box.",
 schema_name="Waterproof flooring installation",
 glance_h2="Water-tolerant flooring options",
 points=[("Rigid-core LVP", "Waterproof planks, floating install"), ("Porcelain tile", "The most water-tolerant surface"), ("Water-resistant laminate", "Check the warranty terms"), ("Prep and seams", "Where water actually gets in")],
 sections=[
  ("Waterproof versus water-resistant", P(
    "<strong>Waterproof</strong> on a flooring box usually means the plank or tile itself will not swell or break down when wet. It does not mean the installed floor is a sealed barrier: water can still travel through seams and around the edges to the subfloor. <strong>Water-resistant</strong> typically means the product tolerates surface spills for a limited time if they are wiped up.",
    "Read the warranty for what is covered (topical spills, standing water for a certain number of hours, or neither) and how the product must be installed to keep that coverage.")),
  ("Best choices by room", H3("Kitchens") + P(LVP + " is popular because it is waterproof, comfortable and affordable; " + TILE + " is the most durable option. Plan the floor with cabinets and dishwasher heights in mind.") +
    H3("Bathrooms") + P("Porcelain or ceramic tile with the right underlayment is the standard. LVP is common in powder rooms and some full baths; avoid exposed seams where water pools.") +
    H3("Basements") + P("Rigid-core LVP and tile handle concrete well. Concrete moisture should be checked and the manufacturer's vapor-barrier requirements followed.") +
    H3("Entries, mudrooms and laundry") + P("Tile and LVP handle wet shoes and pets. Pair the floor with a good mat at exterior doors.")),
  ("The installation details that keep water out", UL(
    "A flat, dry, sound subfloor, with damaged areas replaced (" + SUBFLOOR + ")",
    "Vapor barriers or underlayments required by the manufacturer over concrete",
    "Perimeter expansion gaps covered by trim, with appropriate sealing where the product allows it (" + TRIM + ")",
    "Waterproofing membranes under tile in wet areas") + P(
    "No floor fixes an active leak. If you have a plumbing, drainage or crawlspace moisture problem, it should be repaired before new flooring goes in.")),
  ("Portland moisture considerations", P(
    "The Portland area gets most of its rain between fall and spring, and many homes have crawlspaces or basements. Moisture from below is often more of a threat to floors than spills from above. We check subfloor and slab conditions before recommending a product, and use the " + PRICES + " to keep your material budget in view.")),
 ],
 faqs=[
  ("What is the most waterproof flooring?", "Porcelain tile installed over the right underlayment is the most water-tolerant floor. Rigid-core LVP is the most common waterproof plank option."),
  ("Is waterproof LVP really waterproof?", "The planks are, but seams and edges are not sealed like a shower pan. Standing water can reach the subfloor, so leaks should still be cleaned up quickly."),
  ("Can I put laminate in a kitchen?", "Some newer laminate lines are rated water-resistant or waterproof. Check the warranty terms; standard laminate with a fiberboard core can swell if water sits on it."),
  ("What flooring is best for a Portland basement?", "Rigid-core LVP and tile are common choices over concrete. Check slab moisture first and follow the product's vapor barrier requirements."),
 ]),
# ------------------------------------------------------------------ Commercial
dict(slug="commercial-flooring-installation-portland", nav="Commercial flooring", image="laminate",
 img_alt="Flooring in a bright office",
 title="Commercial Flooring Installation Portland | Banana Floors",
 desc="Flooring installation for Portland-area offices, shops and small commercial spaces: LVP, laminate, tile and carpet. Request a preliminary quote.",
 eyebrow="Portland Metro · Commercial",
 h1="Commercial flooring installation in the Portland metro",
 intro="Banana Floors works on residential and commercial projects. For offices, shops, studios and other small commercial spaces, we help you choose floors rated for the traffic and plan the installation around your business.",
 schema_name="Commercial flooring installation",
 glance_h2="What to plan for in commercial spaces",
 points=[("Commercial ratings", "Wear layers and AC ratings"), ("Glue-down options", "For large open areas"), ("Scheduling", "Around business hours"), ("Clear scope", "Verified before scheduling")],
 sections=[
  ("Choosing floors for commercial traffic", H3("LVP and LVT") + P(
    "Commercial-rated " + LVP + " typically has a thicker wear layer (often 20 mil or more). Glue-down vinyl is common in commercial spaces because it handles rolling loads and large areas without the expansion joints a floating floor may need.") +
    H3("Laminate") + P("AC4 and AC5 " + LAMINATE + " is rated for light to heavier commercial traffic in dry areas such as offices.") +
    H3("Tile") + P("Porcelain " + TILE + " suits entries, restrooms and break rooms where water and grit are common.") +
    H3("Carpet") + P("Carpet softens sound in offices and meeting rooms. Durable, stain-resistant fibers are best for commercial wear.")),
  ("Planning around your business", P(
    "Commercial projects often need to be phased so part of the space stays usable, or scheduled around opening hours. Tell us your hours, any deadlines, and whether furniture, fixtures or equipment need to be moved, so the schedule in your quote reflects how your space actually works.",
    "If you lease your space, check with your property manager about building rules for work hours, deliveries, elevators and disposal before scheduling.")),
  ("Preparation in commercial buildings", P(
    "Many commercial spaces are on concrete slabs that need moisture checks and flattening before resilient flooring or tile goes down (" + SUBFLOOR + "). Removing old glue-down floors and adhesive is often the biggest variable (" + REMOVAL + "). We describe the visible conditions in a preliminary quote and confirm the full scope on site.")),
  ("Getting a commercial quote", P(
    "Send the approximate square footage, a floor plan or photos, the current flooring, and your preferred material. Use the " + PRICES + " to set a material range, and see the " + COST + " for the other items most quotes include.")),
 ],
 faqs=[
  ("Do you install commercial flooring?", "Yes. Banana Floors installs flooring for residential and commercial projects. Tell us about the space, the traffic and your schedule so we can prepare your quote."),
  ("What wear layer does commercial LVP need?", "Commercial-rated LVP often has a wear layer of 20 mil or more. Check the product's commercial rating and warranty."),
  ("Can work be done outside business hours?", "Tell us your hours and constraints when you request a quote, and we will discuss scheduling options for your project."),
  ("Is glue-down or floating flooring better for commercial spaces?", "Glue-down vinyl is common for large commercial areas and rolling loads. Floating floors can work in smaller spaces. The right choice depends on the product, the slab and the use."),
 ]),
# ------------------------------------------------------------------ Rentals
dict(slug="rental-turnover-flooring-portland", nav="Rental & turnover flooring", image="lvp",
 img_alt="Luxury vinyl plank flooring in a kitchen",
 title="Rental Property Flooring Portland, OR | Banana Floors",
 desc="Durable flooring for Portland-area rentals and unit turnovers. LVP, laminate and carpet choices that are easy to maintain and repair. Free estimate.",
 eyebrow="Portland Metro · Rentals and property owners",
 h1="Rental and turnover flooring in the Portland metro",
 intro="For landlords and property managers, flooring has to look good at move-in, survive tenants and pets, and be easy to repair between leases. Banana Floors helps you choose durable, practical floors for rentals and plan the work around vacancies.",
 schema_name="Rental property flooring installation",
 glance_h2="What matters for rental flooring",
 points=[("Durability", "Thicker wear layers and AC4 laminate"), ("Repairability", "Keep spare planks on hand"), ("Consistency", "Same product across units"), ("Timing", "Planned around vacancies")],
 sections=[
  ("Durable choices for rentals", H3("LVP") + P(
    LVP + " is a common rental choice: it is waterproof as a plank, resists scratches, and damaged planks can often be replaced. A 20 mil wear layer is a sensible target for rental traffic.") +
    H3("Laminate") + P("AC4-rated " + LAMINATE + " is scratch-resistant and economical for bedrooms and living areas; keep it away from wet areas unless the product is rated for them.") +
    H3("Carpet") + P("Stain-resistant " + CARPET + " in bedrooms keeps units quieter for neighbors. A neutral color across units makes replacement easier.")),
  ("Make repairs and future turnovers easier", UL(
    "Use one product and color across units where possible so leftover planks can patch damage later",
    "Store a few boxes of spare flooring and matching trim",
    "Choose mid-tone colors and textured finishes that hide wear and pet scratches",
    "Use the same transitions and stair nosing details across units") + P(
    "The " + PRICES + " shows Good, Better and Best tiers so you can compare budgets per unit.")),
  ("Planning around vacancies", P(
    "Turnovers are time-sensitive. Tell us when the unit will be vacant, the move-in date, the rooms involved, and any other trades (painting, cleaning) on the schedule. We confirm timing after reviewing removal, preparation and material availability.",
    "Multi-family buildings and condos may have rules about work hours, parking, disposal and sound-rated underlayment. Share the building's requirements so they are part of the scope.")),
  ("What affects a rental flooring quote", UL(
    "Removal of old carpet or flooring and haul-away (" + REMOVAL + ")",
    "Subfloor repairs common after leaks or pet damage (" + SUBFLOOR + ")",
    "Number of units, rooms and stairs",
    "Baseboards and transitions (" + TRIM + ")") + P("See the " + COST + " for how these items fit together.")),
 ],
 faqs=[
  ("What is the best flooring for a rental property?", "Many owners choose LVP for kitchens, baths and living areas because it is waterproof as a plank and easy to repair, with durable carpet in bedrooms. The best fit depends on the unit and your budget."),
  ("Can you work around a tight turnover schedule?", "Tell us the vacancy and move-in dates when you request a quote. We confirm timing after reviewing the scope and material availability."),
  ("Should I use the same flooring in every unit?", "Using one product and color across units simplifies repairs, because spare planks from one job can patch another."),
  ("Do you work with property managers?", "Yes. We handle rental turnovers for owners and property managers. Include unit details, access instructions and building rules when you request an estimate."),
 ]),
]
