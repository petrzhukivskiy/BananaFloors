BANANA FLOORS WEBSITE: r31 (seo-overhaul)

LAYOUT
  index.html, flooring-prices.html ... hand-edited pages (homepage, price guide)
  flooring/*.html ..................... service pages        (GENERATED)
  locations/*.html .................... city pages           (GENERATED)
  about.html, reviews.html, gallery.html, flooring-installation-cost-portland.html,
  thank-you.html, 404.html, sitemap.xml  (GENERATED)
  theme-r35.css ....................... shared header/footer/theme styles
  page-r34.css ........................ styles for generated pages
  theme-r30.js ........................ light/dark toggle
  material-pricing-r20.js ............. price-guide data (also feeds the cost guide)
  images/ ............................. live images (versioned names, e.g. -r31)
  _image-originals/, _design-reference/ source masters, NOT public (blocked in nginx)
  server/ ............................. optional AI assistant (Node), env.example lives here
  deploy/ ............................. nginx + systemd config
  tools/ .............................. page generator

EDITING GENERATED PAGES
  Text lives in tools/content/services.py, services_extra.py, cities.py, pages.py.
  Shared header/footer/schema live in tools/build.py.
  After editing run from the repo root:
      python3 tools/build.py
  Commit the regenerated HTML and sitemap.xml together with the source change.
  Do not hand-edit generated HTML: it is overwritten on the next build.

URL RULES
  Links are root-relative and keep .html (e.g. /flooring/lvp-flooring-portland.html).
  Home is "/". Do not link to index.html or add ?v= cache-busting query strings.
  When an asset changes, give it a new file name (e.g. -r32) instead.

DEPLOY
  1. Merge the change on GitHub (pull request -> merge).
  2. On the droplet:  git -C /var/www/html pull --ff-only
  3. One-time nginx upgrade: see deploy/nginx-bananafloors.conf and the PR checklist.
  Uploading files through the GitHub website never deletes old files; delete
  retired files in the same commit, or they stay public.

Prices in material-pricing-r20.js are material-only retail references checked
September 8, 2026. They do not include installation, preparation, accessories,
delivery or tax.
