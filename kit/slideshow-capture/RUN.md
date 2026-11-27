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
9. If handles remain and this was not already the 5th continuation run, create a one-shot scheduled task (send_later is not available in a new session — use create_trigger with run_once_at ~3 minutes ahead, same prompt) to continue. Tell the user (SendUserMessage) how many were added, how many remain, and any private accounts.
