# Notes for Claude when working on this repository

This is the professional website of Dr Michael Salmony (payments-innovation.com). He edits it by asking Claude; he does not write code. Read README.md for the layout. The personal site and cookbook are in the sister repository `mgs49/salmony-website`. The project log `00_Statuslog.md` lives only in the "Websites" project on claude.ai (since 25th November 2026); update it there when something material changes here.

## House rules

- British English spelling and grammar. No Americanisms.
- Dates in prose as "7th April 2027". The lectures and publications lists keep their compact style (`**15-16.6.27**`); follow the surrounding entries.
- Never use the em dash character in new text; use a hyphen.
- This is the serious site. No jokes, and never the tongue-in-cheek title string ("Prof. h.c. Dr. rer. nat. ... VIP (Colbert), L.I.V.R."); that belongs on salmony.co.uk only. Here he is "Dr Michael Salmony".
- The biography on `src/profile.md` is his authoritative text (file "Bio Michael Salmony PI"). Change it only when he supplies a new version. Never state a specific number of years of experience; say "decades".
- The board positions on `src/boards.md` follow his file "Boards Salmony". Keep the two in step.
- Only LinkedIn. He does not use X, Twitter or Facebook; do not add links to them. The old Twitter links already in Lectures, Publications and Media may stay (his decision, 27th November 2026).
- Impressum: by his decision it shows the business name, "Germany and London" and the VAT ID, plus office@paymentsinnovation.consulting (assembled by script, 26th November 2026). Do not add his home address, other e-mail addresses or phone number unless he asks. Never publish his personal tax identification number.
- Publications (his rule, 27th November 2026): list only work that was actually published (journals, books, articles, blogs and interviews that appeared somewhere). His folders also hold notes, drafts, working papers and other people's texts; those stay off the site. Fuller or extended versions of a published paper may be offered on the site beside the published version, but never as separate entries on ResearchGate, where only properly published research belongs.
- Client logos: add or remove only on his instruction; some engagements are confidential. G3 may be named (his decision, 27th November 2026).
- No trackers, analytics, cookie banners, external fonts or embedded social-media widgets.

## Working method

- Links to other websites open in a new window (his rule, 23rd November 2026). `eleventy.config.js` adds `target="_blank" rel="noopener"` to every external link when the site is built, so write links normally; links within the site stay in the same window.

- Internal links and picture addresses start with `/`. Eleventy adds the `/payments-innovation-website/` preview prefix while there is no `src/CNAME`; never write that prefix by hand.
- YouTube videos: never embed the player directly. Use the click-to-play pattern already on `src/videos.md` (a still picture in `src/assets/video/yt/` and a link with `data-yt`), so nothing is loaded from YouTube until the visitor presses play. The privacy policy says so. Long recordings belong on his YouTube channel, not in the repository.
- Videos: convert to H.264 MP4 before adding, at most 720 pixels high for short clips and smaller for long recordings, and keep every file under 95 MB (GitHub refuses files over 100 MB). Add a poster picture beside each video.
- After any change run `npm run build` and `npm run check`; both must pass. Look at the changed page before saying it is done.
- Commit to `main` with a plain-English message and push. Publishing is automatic. Never push to `gh-pages` yourself except to repair a failed publish.
- When an address changes, add a line to `src/_data/redirects.json`.

## Look

- Michael chose the navy look on 25th November 2026 (navy bands, a ribbon of engraved banknote lines that turns into tokens, dated lists drawn as a chain of blocks). The clean look and the switch were removed the same day.
- `site.css` holds the base styles; `alt.css` holds the navy look, written as `.alt ...` rules on top of them. `src/_includes/base.njk` sets `class="alt"` on every page. Keep both files; change the look in `alt.css`.
- The ribbon is drawn by `python3 tools/make-ribbon.py`, which writes `src/_includes/ribbon.svg` (home page) and `src/assets/img/ribbon-strip.svg` (page titles). Change the script, not the two files.
- Still the serious site: no jokes.
