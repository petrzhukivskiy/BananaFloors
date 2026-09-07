RELEASE r10 — VERSIONED IMAGE FILENAMES
Every current image now has -r10 in its name, including responsive sizes and full-quality gallery images. All HTML, CSS background, social metadata and dynamic material-guide references match. This changes URLs to avoid stale cached images; it does not bypass GitHub upload failures.

GITHUB UPLOAD
Extract this ZIP. Open the ROOT of the BananaFloors repository on GitHub. Upload index.html, flooring-prices.html, thank-you.html, favicon.svg, robots.txt, sitemap.xml, and the images/, flooring/ and locations/ folders together. Do not upload the outer extracted folder or ZIP. Wait until all uploads finish, then commit. The images folder must contain 25 files with -r10 in their names. Older files in GitHub can remain; the updated pages use the new names.

DROPLET
git -C /var/www/html pull --ff-only
ls -lh /var/www/html/images/kitchen-approved-r10.webp

All local image references, dynamic image paths, and JavaScript syntax verified before packaging. Live upload is not performed here.

BANANA FLOORS — WEBSITE PACKAGE
Domain: https://bananafloors.com
Phone: 503-421-1730
Oregon CCB 209244

LATEST UPDATE
Ask Banana removed, including the floating button, chat panel, browser code and optional AI server/deployment files. Mobile call and estimate controls remain.

UPLOAD
Publish index.html, flooring-prices.html, thank-you.html, flooring/, locations/, images/, favicon.svg, sitemap.xml and robots.txt. Keep README.txt, _design-reference/ and _image-originals/ out of the public document root.

ESTIMATE REQUESTS — EMAIL DELIVERY
Destination: petrzhukivskiy@gmail.com via FormSubmit.
The form now posts directly to the service, with spam protection enabled. It includes name, phone, optional customer email, city, material choice, area, notes and the material planning budget. No browser-side API key is needed. After submission the service redirects to https://bananafloors.com/thank-you.html.

REQUIRED ONE-TIME ACTIVATION
1. Upload the website files, including thank-you.html, to bananafloors.com.
2. Submit a test estimate from the live site.
3. Open the FormSubmit activation email at petrzhukivskiy@gmail.com (check Spam) and confirm the address.
4. Submit another test and confirm it reaches the inbox and returns to the thank-you page.
Email delivery has not been activated or tested here. The initial test triggers activation; do not assume it is delivered as a normal lead. Leave spam protection enabled. Reference: https://formsubmit.co/

IMAGES
Approved kitchen and laundry included. All six materials have responsive image sizes and lossless native-quality gallery files. Native originals are 1536 x 1024; 3072 x 2048 exports are upscaled, not native 4K. Original PNGs are in _image-originals/.

VALIDATION
Local JavaScript syntax and gallery/menu interaction checks performed. Live site not deployed or browser-tested here.
