---
name: kol-scraper
description: Find and vet KOLs (human or AI creators) for SHER on IG/TikTok, then log them with photos in the KOL Scout tab. Use for หาอินฟลู, scout KOL, or KOL scraper requests.
---

# KOL Scraper

Find creators SHER could hire, check that they fit, and log them with photos in the team sheet. A round works from a brief: who we want (for example, foreign creators living in Thailand, or AI personas we can hire), the look, and the budget. If the brief is unclear, state the reading you took and carry on.

## Where to look (most useful first)

1. **Snowball from people already on the shortlist.** Run `apify/instagram-scraper` (resultsType `posts`, about 30 per account) and collect `taggedUsers`, `mentions` and `coauthorProducers`. People with a similar style tag each other.
2. **Marketplaces such as Collabstr.** Use them for handles only. The public pages list about 60 creators per city. The slug on a Collabstr profile is often not the IG handle: open `collabstr.com/<slug>` (Chrome, same-origin `fetch`) and read the `instagram.com/...` link.
3. **Venues and similar brands.** Collect tagged users from beach clubs, rooftop bars, and brands that use foreign models, then drop business accounts.
4. **Model agency rosters.** One example is the agencies a shortlisted model is signed with.
5. **AI creators: web research.** Find the persona, the studio or agency that runs it, and how to contact them. Check the date of the last post, because many Thai AI personas have gone dormant.

Hashtag scraping mostly returns businesses, and AI hashtags (#aiinfluencer, #aimodel) return tiny accounts. Use them only as a last resort.

## Vet each candidate

- **Profile data:** run `apify/instagram-profile-scraper`. Work out ER as average (likes + comments) / followers over the latest posts; `likesCount = -1` means likes are hidden. Count how many recent posts carry a Thailand location tag, and note the date of the last post.
- **Look:** download the 6 latest `displayUrl` images with curl (the IG CDN is reachable from the shell), make a contact sheet, and look at it. Judge fit with SHER, not looks: neutral palette, strapless/corset styling, and Casual/Beach/Resort or hi-fashion mood. Drop anyone mostly posting from outside Thailand (for human briefs), men, and accounts with no fashion angle.
- **Tier:** A for a strong fit to contact first, B for possible, C for weak.

## Log it

Use the **KOL Scout** tab in "SHER Content Plan – TEST". Columns: Photo, Tier, IG, Name / Nationality, City, Followers, ER, Niche, Fit with SHER / To check, Rate ($) / Contact, Deal status, Lookbook, Type (Human/AI), Source. Write all cell text in English.

- **Photo:** pick one hero image, shrink it to about 360px, and upload it to the Drive folder "SHER influencer photos" (shared as anyone-with-link). Use `=IMAGE("https://drive.google.com/uc?export=view&id=<fileId>")`. Do not hotlink IG URLs, because they expire.
- **Formats:** copy row 2's format onto new rows, set row height 180, and use the Deal status dropdown (To do / DM sent / In talks / Deal closed / Declined).
- **Allow access:** the first `IMAGE()` in a spreadsheet shows `#REF!` until someone clicks Allow access in the browser.
- **Check:** open the tab to make sure the photos show.

## Working notes

- Cap every Apify call with `maxTotalChargeUsd` and tell Stamp what the round cost (about $1 per round so far).
- Apify results are large: save them to a file and parse with Python, requesting only the fields you need.
- Chrome `javascript_tool` output is cut off at about 1,000 characters, so read long lists in chunks.
- In the reply, list the Tier A picks with one line each on why, say what was tried and didn't work, and give one next step (for example, drafting outreach).
- Hiring foreigners for paid work in Thailand raises work-permit questions. Gifting or affiliate deals carry less risk; flag this before anyone signs a paid contract.
