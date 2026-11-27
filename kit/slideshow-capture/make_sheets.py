"""Build sprite sheets for the KOL artifact's hover slideshow from Chrome profile screenshots.

Usage: python3 make_sheets.py <log.tsv> <out_dir> <more_index>
log.tsv lines: handle<TAB>screenshot_path<TAB>js_json   (js_json = {"iw":..,"R":[[x,y,w,h],...]})
Writes <out_dir>/sh/m<more_index>-<k>.jpg and <out_dir>/more-<more_index>.json
"""
import json, os, sys
from PIL import Image, ImageStat

W, H, PER_SHEET, MAXF = 432, 540, 12, 7
log, out, idx = sys.argv[1], sys.argv[2], int(sys.argv[3])
os.makedirs(f'{out}/sh', exist_ok=True)


def fit(t):
    if t.width / t.height > 0.8:
        w = round(t.height * 0.8); x = (t.width - w) // 2; t = t.crop((x, 0, x + w, t.height))
    else:
        h = round(t.width * 1.25); y = (t.height - h) // 2; t = t.crop((0, y, t.width, y + h))
    return t.resize((W, H), Image.LANCZOS)


users = []
for line in open(log, encoding='utf-8'):
    p = line.rstrip('\n').split('\t')
    if len(p) < 3 or not os.path.exists(p[1]):
        continue
    try:
        js = json.loads(p[2])
    except Exception:
        print('bad js', p[0]); continue
    img = Image.open(p[1]).convert('RGB')
    s = img.width / js['iw']
    frames = []
    for x, y, w, h in js['R'][:MAXF]:
        x0, y0, x1, y1 = x * s + 2, y * s + 2, (x + w) * s - 2, (y + h) * s - 2
        if y0 < 0 or x1 > img.width + 2:
            continue
        y1 = min(y1, img.height)
        if y1 - y0 < (x1 - x0) * 1.0:  # mostly cut off at the bottom
            continue
        t = img.crop((round(x0), round(y0), round(x1), round(y1)))
        if max(ImageStat.Stat(t).stddev) >= 8:
            frames.append(fit(t))
    if frames:
        users.append((p[0], frames))
    else:
        print('no usable tiles', p[0])

meta = {}
for k in range(0, len(users), PER_SHEET):
    chunk = users[k:k + PER_SHEET]
    name = f'sh/m{idx}-{k // PER_SHEET}.jpg'
    sheet = Image.new('RGB', (W * len(chunk), H * MAXF))
    for c, (u, frames) in enumerate(chunk):
        for r, f in enumerate(frames):
            sheet.paste(f, (c * W, r * H))
        meta[u] = {'f': name, 'cols': len(chunk), 'col': c, 'rows': MAXF, 'n': len(frames)}
    sheet.save(f'{out}/{name}', quality=78)
json.dump(meta, open(f'{out}/more-{idx}.json', 'w'))
print('users', len(meta), 'sheets', (len(users) + PER_SHEET - 1) // PER_SHEET)
