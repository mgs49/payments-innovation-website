# Notes for Claude when working on this repository

This is the professional website of Dr Michael Salmony (payments-innovation.com). He edits it by asking Claude; he does not write code. Read README.md for the layout. The personal site and cookbook are in the sister repository `mgs49/salmony-website`, which also holds the project log `00_Statuslog.md`; update that log when something material changes here.

## House rules

- British English spelling and grammar. No Americanisms.
- Dates in prose as "7th April 2027". The lectures and publications lists keep their compact style (`**15-16.6.27**`); follow the surrounding entries.
- Never use the em dash character in new text; use a hyphen.
- This is the serious site. No jokes, and never the tongue-in-cheek title string ("Prof. h.c. Dr. rer. nat. ... VIP (Colbert), L.I.V.R."); that belongs on salmony.co.uk only. Here he is "Dr Michael Salmony".
- The biography on `src/profile.md` is his authoritative text (file "Bio Michael Salmony PI"). Change it only when he supplies a new version. Never state a specific number of years of experience; say "decades".
- The board positions on `src/boards.md` follow his file "Boards Salmony". Keep the two in step.
- Only LinkedIn. He does not use X, Twitter or Facebook; do not add links to them.
- Impressum: by his decision it shows the business name and VAT ID with "address and e-mail to follow". Do not add his address, e-mail or phone number unless he asks. Never publish his personal tax identification number.
- Client logos: add or remove only on his instruction; some engagements are confidential.
- No trackers, analytics, cookie banners, external fonts or embedded social-media widgets.

## Working method

- Links to other websites open in a new window (his rule, 23rd November 2026). `eleventy.config.js` adds `target="_blank" rel="noopener"` to every external link when the site is built, so write links normally; links within the site stay in the same window.

- Internal links and picture addresses start with `/`. Eleventy adds the `/payments-innovation-website/` preview prefix while there is no `src/CNAME`; never write that prefix by hand.
- YouTube videos: never embed the player directly. Use the click-to-play pattern already on `src/media.md` (a still picture in `src/assets/video/yt/` and a link with `data-yt`), so nothing is loaded from YouTube until the visitor presses play. The privacy policy says so. Long recordings belong on his YouTube channel, not in the repository.
- Videos: convert to H.264 MP4 before adding, at most 720 pixels high for short clips and smaller for long recordings, and keep every file under 95 MB (GitHub refuses files over 100 MB). Add a poster picture beside each video.
- After any change run `npm run build` and `npm run check`; both must pass. Look at the changed page before saying it is done.
- Commit to `main` with a plain-English message and push. Publishing is automatic. Never push to `gh-pages` yourself except to repair a failed publish.
- When an address changes, add a line to `src/_data/redirects.json`.

## Two looks (temporary)

- The site has two looks while he decides: the clean one (`site.css`, the default) and an alternative (`alt.css`) with more payments and fintech character: navy bands, a ribbon of engraved banknote lines that turns into tokens, and dated lists drawn as a chain of blocks. Only the look differs; pages and texts are shared. Still the serious site: no jokes in either look.
- A link in the footer switches, as does adding `?look=alt` or `?look=clean` to any address. The choice is kept in the visitor's browser only (no cookie, nothing sent anywhere).
- The ribbon is drawn by `python3 tools/make-ribbon.py`, which writes `src/_includes/ribbon.svg` (home page) and `src/assets/img/ribbon-strip.svg` (page titles). Change the script, not the two files.
- When changing the design, check both looks: view the page with and without `?look=alt`.
- Once he has chosen, remove the other look and the switch (the two blocks marked in `src/_includes/base.njk`). The switch must be gone before the site goes live on payments-innovation.com.

