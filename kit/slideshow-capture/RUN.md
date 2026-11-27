# Continue: hover slideshows for the "KOLs found in competitor tags" artifact

Artifact: slug 14e965b0-a9a0-46e9-ada2-e2623362d3de (https://claude.ai/artifact/3amkFRYFNcQsj6gEfcw9Gy).
The page already loads extra slideshows from `more-1.json` … `more-9.json` (sprite sheets under `sh/`).
`more-9.json` is taken (test). Use the lowest free number 1–8: check with the artifact `list_files` tool.

## Rules
- Chrome is the user's personal IG (Claude in Chrome). Read-only: never click Follow, Message, Like or anything that changes the account. One profile at a time, in ONE tab you create yourself; close it at the end.
- Never re-tier, cut or rewrite anyone. Only add slideshow images.
- Do the capture yourself (no subagents) — screenshot saving has a per-session cap that subagents share.

## Steps
1. `git clone https://github.com/stamp44101/sher-kol-scraper` and work in `kit/slideshow-capture/`. Handles to do: `remaining.txt` minus any handle already in a published `more-*.json` (read them with the artifact `read_file` tool).
2. Load Chrome tools in one ToolSearch: tabs_context_mcp, tabs_create_mcp, browser_batch, computer, javascript_tool, navigate, tabs_close_mcp.
3. Per handle, one browser_batch:
   - navigate `https://www.instagram.com/<handle>/`, wait 3
   - javascript_tool (returns JSON — do NOT change it to key=value text, the extension blocks that):
     `(()=>{const a=[...document.querySelectorAll('main a')].filter(x=>/\/(p|reel)\//.test(x.getAttribute('href')||''));if(!a.length)return JSON.stringify({none:(document.body.innerText.match(/This account is private|Sorry, this page isn't available/)||['no posts'])[0]});const r=a[0].getBoundingClientRect();window.scrollBy(0,r.top-4);return JSON.stringify({iw:innerWidth,R:a.slice(0,7).map(x=>{const b=x.getBoundingClientRect();return [b.left,b.top,b.width,b.height].map(Math.round)})})})()`
   - computer hover [40, 400]
   - computer screenshot, save_to_disk true (plain screenshot; zoom does not save)
4. Copy the screenshot right away: the result ends with `[Image source: <path>]` — `cp` THAT exact path to `caps/<handle>.jpg` and append `handle<TAB>caps/<handle>.jpg<TAB><js json>` to `log.tsv`. Private / no posts: log nothing, note it for the report.
5. If 3 screenshots in a row give no `[Image source: …]` line, the save cap is hit: stop capturing.
6. Build and publish:
   `python3 make_sheets.py log.tsv out <N>` → `out/sh/m<N>-*.jpg` + `out/more-<N>.json`. Copy `out/` under /home/claude if needed, then `publish_files` (patch, base_version from `get_artifact`) with the sheet files as `sh/...` and `more-<N>.json` at the root. Do not touch index.html or other files.
7. Open the artifact in Chrome, search one new handle, hover it, confirm it plays.
8. Remove the done handles from `remaining.txt`, commit and push.
9. Do NOT schedule another run (scheduled runs can't create tasks without approval; the next runs are already scheduled). If `remaining.txt` is empty when you start, just tell the user it's all done and stop. Tell the user (SendUserMessage) how many were added, how many remain, and any private accounts.

Pace: keep going until the list is done or the save cap is hit (3 screenshots in a row with no saved path). Do NOT stop early because the run feels long — publish in batches of ~30 (one more-<N>.json per batch, next free N) so nothing is lost if the run ends.

## Notes from continuation run 1 (2026-11-27)
- Published `more-1.json` (36 creators, sheets `sh/m1-0..2.jpg`). Next free index is 2. `continuation_runs.txt` counts runs done.
- Chrome screenshot results now end with `Screenshot saved to: <path>` instead of `[Image source: …]`; that path is on the cloud workspace — treat it the same. Do NOT pass `scale` on the capture screenshot (it saves the small image).
- The Artifact publish needs `file_path`: read `index.html` with action read + path, publish that unchanged file plus `files`; the first try is refused as "not viewed", the immediate retry goes through.
