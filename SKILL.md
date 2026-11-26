---
name: kol-scraper
description: Find and vet KOLs (human or AI creators) for SHER on IG/TikTok, then log them with photos in the KOL Scout tab. Use for หาอินฟลู, scout KOL, or KOL scraper requests.
---

# KOL Scraper

Find creators SHER could hire, check that they fit, and log them with photos in the team sheet. A round works from a brief: who we want (for example, foreign creators living in Thailand, or AI personas we can hire), the look, and the budget. If the brief is unclear, state the reading you took and carry on.

## Where to look (most useful first)

1. **Snowball from Stamp's hand picks and yellow rows.** Free route: in Chrome on his logged-in IG, open a profile, click the "Similar accounts" button once (use `find` for its ref), then read the handles from the links. IG groups these by who follows whom, not by look, so the chain drifts toward local celebrities after two hops. Drop celebrities and stop following a branch once it turns into them. Paid route: run `apify/instagram-scraper` (resultsType `posts`, about 30 per account) and collect `taggedUsers`, `mentions` and `coauthorProducers`. People with a similar style tag each other.
2. **Marketplaces such as Collabstr.** Use them for handles only. The public pages list about 60 creators per city. The slug on a Collabstr profile is often not the IG handle: open `collabstr.com/<slug>` (Chrome, same-origin `fetch`) and read the `instagram.com/...` link.
3. **Venues and similar brands.** Collect tagged users from beach clubs, rooftop bars, and brands that use foreign models, then drop business accounts.
4. **Model agency rosters.** One example is the agencies a shortlisted model is signed with.
5. **AI creators: web research.** Find the persona, the studio or agency that runs it, and how to contact them. Check the date of the last post, because many Thai AI personas have gone dormant.

Hashtag scraping mostly returns businesses, and AI hashtags (#aiinfluencer, #aimodel) return tiny accounts. Use them only as a last resort.

## Vet each candidate

Judge from her photos only. Captions, bios, followers, ER and likes never decide who is picked or her tier; record the numbers in the sheet but leave them out of the reasoning.

**Learn from Stamp first.** Before vetting, read his feedback in KOL Scout: the row colour (yellow = interested, red = not) and his reason in the **Note** column. His reasons are the brief. Weigh the red ones most; they show what he cuts.

**What he has cut so far, and why** (from his notes; keep this list current):
- Too revealing: a large bust or styling that reads adult-content, not fashion.
- Looks older or tired.
- Reads too Thai, or not Western at all, when the brief is "ดู ฝ" (Western-looking).
- The feed has turned into family content: kids, husband, home life. Even a few kid/family posts count, and together with an older look it is a firm no.
- Not striking enough to front a fashion brand.
- Body that won't carry a fitted strapless mini: too muscular, too thin, too full, or so inconsistent across photos that you can't tell.
- A facial feature that dominates every shot.
- Her style is unclear: you can't picture her in SHER because the feed has no clear look (costumes, mixed themes). This is a cut even when nothing is revealing.
- Celebrities: actresses, singers, pageant titleholders and other famous names. No celebrities at all, even if the look fits.

**What makes him interested:** she looks like a model; the feed is chic (เก๋) or high-fashion; she can carry more than one style; she has worked with brands like SHER's (e.g. malimarea).

**Soft minus, still yellow:** a sporty/active tone; a look that is only middling.

**How to look:**
1. **Judge the latest 9-post grid as a whole.** That is what Stamp sees. Don't let one or two swimwear or sexy shots further down decide the verdict; ask what the grid as a whole says.
2. **Read the feed's visual register, not its places.** Is it editorial/high-fashion, minimal studio, or casual phone-shot, and how consistent? Ask: would her photos sit next to SHER's ads and look like the same brand? Owning a corset is not the test.
3. **Picture her in SHER** (strapless corset/bustier minis, neutral palette): frame, posture, how she poses, how restrained the styling is. Does it look expensive or does it look revealing? Think it through for each person; it is not a checklist.
4. **Examples are a direction, not a template.** A reference account (e.g. @foamlumm) shows the feeling Stamp wants. Don't narrow it to one trait (e.g. "mixed-race face") and fill the list with that.
5. **Compare against the seeds every time.** When snowballing, hold each candidate next to Stamp's hand-picked seeds, not just a minimum bar.
6. Drop men, accounts with no fashion angle, private accounts, and (for human briefs) people mostly posting from outside Thailand.

**Tier (visual fit only):** A = would look right in SHER today, contact first; B = possible with a styling brief; C = weak. Never re-tier Stamp's hand picks below A.

**Profile data:** `apify/instagram-profile-scraper` fills the sheet columns only (followers, ER, location tags, last post date).

## Log it

Use the **KOL Scout** tab in "SHER Content Plan – TEST". Columns: Photo, Tier, IG, Name / Nationality, City, Followers, ER, Niche, Fit with SHER / To check, Rate ($) / Contact, Deal status, Lookbook, Type (Human/AI), Source, Note (Stamp's feedback; leave it to him). Rows 2–6 are Stamp's hand picks (green highlight); keep them on top. Followers and ER columns are hidden; still fill them. Write all cell text in English.

- **Photo:** pick the one image that shows why she fits (a fitted or strapless look, a clean full-body shot), not simply her latest post; avoid group shots, swimwear and close-up selfies. Shrink it to about 360px and upload it to the Drive folder "SHER influencer photos" (shared as anyone-with-link). Use `=IMAGE("https://drive.google.com/uc?export=view&id=<fileId>")`. Do not hotlink IG URLs, because they expire.
- **Formats:** copy the format of an existing new-candidate row onto new rows, set row height 180, and use the Deal status dropdown (To do / DM sent / In talks / Deal closed / Declined).
- **Allow access:** the first `IMAGE()` in a spreadsheet shows `#REF!` until someone clicks Allow access in the browser.
- **Check:** open the tab to make sure the photos show.

## Working notes

- Cap every Apify call with `maxTotalChargeUsd` and tell Stamp what the round cost (about $1 per round so far).
- Apify results are large: save them to a file and parse with Python, requesting only the fields you need.
- Chrome `javascript_tool` output is cut off at about 1,000 characters, so read long lists in chunks.
- In the reply, list the Tier A picks with one line each on why (visual reasons only), say what was tried and didn't work, and give one next step (for example, drafting outreach).
- Hiring foreigners for paid work in Thailand raises work-permit questions. Gifting or affiliate deals carry less risk; flag this before anyone signs a paid contract.
