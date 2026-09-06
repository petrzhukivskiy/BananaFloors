BANANA FLOORS — FULL WEBSITE UPGRADE
====================================
Domain: https://bananafloors.com
Phone: 503-421-1730

WHAT'S INCLUDED
- Compact photo-first homepage
- Trust strip
- Price-aware flooring cards
- Live material planning range in estimate form
- Flooring style gallery
- Flooring Price Guide with Good / Better / Best, specs, layers, and full-screen detail modal
- SEO service pages + sitemap.xml + robots.txt
- Ask Banana flooring assistant
- Static fallback answers if the AI backend is not configured
- Optional secure OpenAI backend in /server (API key is never placed in browser code)

IMPORTANT ABOUT REVIEWS / PROJECT PHOTOS
No customer reviews have been invented. The site contains a hidden review-ready placeholder that should only be enabled after verified review text is supplied. Room scenes are visualizations, not completed Banana Floors projects. Replace them with real project photos over time.

BASIC DEPLOYMENT (YOUR CURRENT GITHUB + DIGITALOCEAN SETUP)
1. Extract this ZIP into the BananaFloors Git repository.
2. git add .
3. git commit -m "Full Banana Floors website upgrade"
4. git push origin main
5. On the Droplet: cd /var/www/html && git pull

The site works immediately as a static site. Ask Banana will use its built-in local fallback until the optional AI server is configured.

OPTIONAL: ENABLE REAL ASK BANANA AI
The backend uses the official OpenAI JavaScript SDK and the Responses API.

On the Droplet:
  sudo apt update
  sudo apt install -y nodejs npm
  cd /var/www/html/server
  sudo npm install --omit=dev

Create a server-only environment file (do NOT commit your API key to GitHub):
  sudo nano /etc/banana-floors-ai.env

Put in:
  OPENAI_API_KEY=YOUR_OPENAI_API_KEY
  OPENAI_MODEL=gpt-5.5
  PORT=3001

Secure it:
  sudo chmod 600 /etc/banana-floors-ai.env

Install the provided systemd unit:
  sudo cp /var/www/html/deploy/banana-ai.service /etc/systemd/system/banana-ai.service
  sudo systemctl daemon-reload
  sudo systemctl enable --now banana-ai
  sudo systemctl status banana-ai

Then add the contents of deploy/nginx-ai-location.conf INSIDE the HTTPS server block for bananafloors.com. Test and reload:
  sudo nginx -t
  sudo systemctl reload nginx

Check:
  curl https://bananafloors.com/api/health

SECURITY
- Never put OPENAI_API_KEY in index.html or any browser JavaScript.
- Keep /etc/banana-floors-ai.env server-only.
- The API includes a basic per-IP rate limit and limits customer questions to 500 characters.

GOOGLE SEARCH CONSOLE
Submit: https://bananafloors.com/sitemap.xml

SEPTEMBER 2026 REFRESH
- Two new generated architectural room visualizations, optimized as WebP.
- Oregon CCB 209244 supplied by owner, displayed on every page.
- Updated headline, mobile menu, clearer contact flow and keyboard focus.
- Estimate requests are reviewed and sent by the customer through their messaging app. No submission server is connected. Desktop visitors can copy the request or call.
- Price-guide quote button transfers flooring type and square footage into the homepage form.
- Existing material planning prices retained, not reverified against supplier quotes.
- Local links, anchors, JSON-LD and JavaScript syntax checked. Live domain and actual SMS delivery were not tested.

DEPLOYMENT CONTENTS
Publish index.html, flooring-prices.html, flooring/, locations/, images/, favicon.svg, sitemap.xml and robots.txt. Keep README.txt, _design-reference/, server/ and deploy/ outside the public document root unless configuring the optional backend separately.
After uploading, check the site on your phone and send yourself an estimate text to confirm delivery.

LATEST VISUAL UPDATE
All six flooring room images replaced with new coordinated AI-generated room visualizations. Optimized WebP files are in images/. Full-resolution PNGs are included in _image-originals/ for your use; do not upload that folder to your public document root. These illustrate flooring styles, not particular stocked products or completed jobs.
Spec panels now include numbered interactive construction diagrams, category facts, and simplified budget comparisons. Construction is illustrative and not to scale; check the chosen manufacturer product specifications.
Oregon CCB 209244 is the exact displayed text on all pages.
Checks: all six panel generators, layer control counts, local file references, page JavaScript syntax and JSON-LD passed. Live browser and domain have not been tested.
Image briefs: PNW oak living room; light oak-look LVP kitchen; smoked oak engineered dining room; wood-look laminate office; pale porcelain laundry room; warm gray carpet family room. Generated using built-in image generation with natural daylight, prominent floors, charcoal/white interiors and restrained yellow accents.
