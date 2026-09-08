BANANA FLOORS — COMPLETE RELEASE r15

Contains every website page and all required images. All 25 image filenames are new and the pages reference those new names. No earlier ZIP is needed.

WINDOWS / GITHUB UPLOAD
1. Download this ZIP completely. Right-click and choose Extract All.
2. Open your BananaFloors repository on GitHub, on main, at the top level.
3. Choose Add file > Upload files. Drag the CONTENTS of the extracted folder into the upload area: images, flooring, locations, and the root files including index.html. Do not upload this ZIP or the enclosing folder.
4. Wait until ALL uploads finish, then commit the changes.
5. In your droplet console run:
git -C /var/www/html pull --ff-only
6. Refresh your website.

Uploading the ZIP itself does not deploy the site. Matching page files are replaced by the GitHub upload; old differently named images may remain, but this release does not reference them. You do not need to delete the site first.

Full gallery photos retain native 1536 x 1024 detail. Larger responsive versions are resized copies.
