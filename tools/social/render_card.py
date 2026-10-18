"""Render a vertical 1080x1350 social card (headline + 3 product photos) for one article.

Used for TikTok Photo Mode posts and Instagram Stories. Reads the article's frontmatter
directly, so it works for both sites.

    python render_card.py picks small-pantry-organization-ideas "12 small pantry ideas" out.png
    python render_card.py clarity numerology-for-beginners "Numerology: start free" out.png
"""
import os
import sys

import yaml
from PIL import Image, ImageDraw, ImageFont

DOWNLOADS = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
FONT = 'C:/Windows/Fonts/arialbd.ttf'
W, H = 1080, 1350
THEME = {
    'picks':   dict(bg=(24, 30, 34), acc=(242, 190, 92), brand='VONGUUL PICKS'),
    'clarity': dict(bg=(28, 22, 46), acc=(214, 182, 110), brand='VONGUUL CLARITY'),
}


def product_images(site, slug):
    root = os.path.join(DOWNLOADS, f'vonguul-{site}')
    text = open(os.path.join(root, 'src', 'content', 'articles', slug + '.md'), encoding='utf-8').read()
    fm = yaml.safe_load(text.split('---')[1])
    paths = [os.path.join(root, 'public') + p['image'] for p in fm.get('products', [])]
    return [p for p in paths if os.path.exists(p)][:3]


def wrap(d, text, f, width):
    lines, cur = [], ''
    for w in text.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def tile(path, w, h):
    t = Image.new('RGB', (w, h), (255, 255, 255))
    im = Image.open(path).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    bg.alpha_composite(im)
    im = bg.convert('RGB')
    im.thumbnail((w - 40, h - 40), Image.LANCZOS)
    t.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], 22, fill=255)
    return t, m


def card(site, slug, headline, out):
    th = THEME[site]
    img = Image.new('RGB', (W, H), th['bg'])
    d = ImageDraw.Draw(img)
    d.text((60, 58), th['brand'], font=ImageFont.truetype(FONT, 30), fill=th['acc'])
    size = 74
    while True:
        f = ImageFont.truetype(FONT, size)
        lines = wrap(d, headline, f, W - 120)
        if len(lines) <= 4 or size <= 52:
            break
        size -= 4
    y = 118
    for ln in lines:
        d.text((60, y), ln, font=f, fill=(255, 255, 255))
        y += int(size * 1.17)
    top = max(y + 30, 420)
    imgs = product_images(site, slug)
    bottom = H - 120
    big_h = int((bottom - top) * 0.58)
    small_h = bottom - top - big_h - 24
    t, m = tile(imgs[0], W - 120, big_h)
    img.paste(t, (60, top), m)
    sw = (W - 120 - 24) // 2
    for i, p in enumerate(imgs[1:3]):
        t, m = tile(p, sw, small_h)
        img.paste(t, (60 + i * (sw + 24), top + big_h + 24), m)
    d.text((60, H - 82), 'FULL GUIDE  \u2192  LINK IN BIO', font=ImageFont.truetype(FONT, 34), fill=th['acc'])
    img.save(out, optimize=True)


if __name__ == '__main__':
    card(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print('wrote', sys.argv[4])
