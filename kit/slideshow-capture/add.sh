#!/bin/bash
# usage: add.sh handle screenshot-suffix A|B|json
cd /home/claude/sher-kol-scraper/kit/slideshow-capture
J="$3"
[ "$J" = A ] && J='{"iw":1704,"R":[[220,4,312,416],[532,4,312,416],[845,4,312,416],[1158,4,312,416],[220,420,312,416],[532,420,312,416],[845,420,312,416]]}'
[ "$J" = B ] && J='{"iw":1704,"R":[[220,4,312,416],[532,4,312,416],[845,4,312,416],[1158,4,312,416],[220,421,312,416],[532,421,312,416],[845,421,312,416]]}'
S="$2"; [ -f "$S" ] || S=/tmp/claude-chrome-screenshots-dHyJiz/screenshot-$2.jpg
cp "$S" "caps/$1.jpg" && printf '%s\tcaps/%s.jpg\t%s\n' "$1" "$1" "$J" >> log.tsv && echo "ok $1 ($(wc -l < log.tsv))"
