# KOL Scraper skill

A Claude skill for scouting KOLs for SHER: human creators (for example, foreigners living in Thailand) and AI personas that can be hired through their studio or agency.

Each round finds candidates, checks their profile data and recent photos, and adds them to the **KOL Scout** tab of the SHER Content Plan sheet with a photo, tier, fit notes and deal status.

## What you need

- Apify connector (Instagram scrapers; each call is capped by cost)
- Claude in Chrome (to read handles from marketplace pages)
- Google Drive and Google Sheets connectors (photos and the KOL Scout tab)

## How to use

Ask Claude something like "scout 10 more foreign creators in Phuket for SHER Resort" or "find hireable AI fashion creators". The full procedure is in [SKILL.md](SKILL.md).

## Status

v0.1. Two rounds run in November 2026: 8 creators from Collabstr, then 12 more from snowballing and AI-creator research.
