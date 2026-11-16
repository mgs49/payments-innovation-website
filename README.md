# payments-innovation-website

The source of **payments-innovation.com**: the professional site of Dr Michael Salmony and Payments Innovation Consulting. It replaces the GoDaddy Website Builder site and the Work, Boards, Lectures, Publications and Media pages that used to be on salmony.co.uk.

- Preview (until the domain is switched): https://mgs49.github.io/payments-innovation-website/
- Sister site (personal site and cookbook): repository `mgs49/salmony-website`, where the remake report, the proposal and the project log `00_Statuslog.md` are kept.

## Changing the site with Claude

Every page is a plain text file. Ask Claude, with GitHub connected, in ordinary words, for example:

- "In my payments-innovation-website repository, add this to the 2027 lectures: ..."
- "Add this award to the announcements: ..."
- "Add the logo of client X to the clients page" (attach the logo).

Claude edits the file, saves it to GitHub, and the live site updates by itself about a minute later.

## Where things are

| What | Where |
|---|---|
| Home page (consulting pitch, geographies) | `src/index.njk` |
| Profile (the authoritative biography) | `src/profile.md` |
| Boards | `src/boards.md` |
| Lectures, older lectures | `src/lectures.md`, `src/lectures/` |
| Publications, older publications | `src/publications.md`, `src/publications/` |
| Media, with the videos | `src/media.md`, videos in `src/assets/video/` |
| Events (Transaction Innovation Forum, Istanbul, masterclasses) | `src/events.njk`, files in `src/assets/events/` |
| Announcements (awards and nominations) | `src/_data/announcements.json` |
| Clients and partners | `src/_data/clients.json`, logos in `src/assets/work/clients/` |
| Contact, Impressum, Privacy policy | `src/contact.md`, `src/impressum.md`, `src/privacy-policy.md` |
| Menu | `src/_data/nav.json` |
| Old addresses that now redirect | `src/_data/redirects.json` |
| Colours, fonts, layout | `src/assets/css/site.css` |

On the lectures and publications pages a heading that is just a year (`## 2027`) automatically becomes a jump target for the row of years at the top; when a new year starts, add it to that row as well.

## How it is built

[Eleventy](https://www.11ty.dev/) turns `src/` into the finished site in `_site/`. On every push to `main` the workflow in `.github/workflows/deploy.yml` builds the site, checks every internal link and picture, and publishes to the `gh-pages` branch, which GitHub Pages serves.

The site sets no cookies and uses no trackers. Its own videos are stored in the repository. The only outside content is YouTube videos on the media, lectures and events pages. Each shows a still picture stored in `src/assets/video/yt/`; the YouTube player (no-cookie address) is loaded only when the visitor presses play.

Links to the personal site are written as `https://www.salmony.co.uk/...`. While that site is still a preview they are pointed at the preview automatically; set `personalUrl` in `src/_data/site.json` to `https://www.salmony.co.uk` when it goes live.

## Switching the real domain to this site

Add a file `src/CNAME` containing `payments-innovation.com`, point the domain's DNS at GitHub Pages (leaving the e-mail records untouched) and switch on HTTPS in the repository's Pages settings. The site then stops using the `/payments-innovation-website/` preview prefix by itself.

## Two looks

While Michael decides, the site can be seen in two looks: the clean one and an alternative with more payments and fintech character. Use the link at the bottom of any page to switch, or add `?look=alt` to the address. Details are in CLAUDE.md.

