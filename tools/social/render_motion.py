"""Render a 9-second vertical (1080x1920) motion video for one article, plus a still of the last frame.

Clarity: a sacred-geometry or esoteric figure (chosen from the article slug) draws itself in gold on a
starfield, then the real product photos rise in. The geometry is computed exactly, not AI-generated.
Picks: a background photo with a slow zoom (--bg: an AI-generated room scene from tools/social/backgrounds/;
without --bg, a blurred, enlarged real product photo), then the real product photos rise in. Product
photos are never AI.

    python render_motion.py clarity kabbalah-for-beginners "Kabbalah is not the red string" out.mp4
    python render_motion.py picks humidifiers-by-room-size "Measure first, then buy" out.mp4
    python render_motion.py clarity numerology-for-beginners "..." out.mp4 --symbol metatron

Writes out.mp4 and out.png (the final frame, for Pinterest or a still Story). Silent audio track;
add music in the TikTok app.
"""
import argparse
import hashlib
import math
import os
import random
import subprocess
import sys

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
import yaml  # noqa: E402
from render_card import DOWNLOADS, wrap  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, SECONDS = 1080, 1920, 30, 9
FONTS = 'C:/Windows/Fonts/'
GOLD = (222, 190, 120)
THEME = {
    'picks':   dict(acc=(242, 190, 92), brand='VONGUUL PICKS', head='segoeuib.ttf', cta='Full guide on Vonguul Picks · link in bio'),
    'clarity': dict(acc=GOLD, brand='VONGUUL CLARITY', head='georgiab.ttf', cta='Full guide on Vonguul Clarity · link in bio'),
}

# ---------------------------------------------------------------- geometry
# Every figure is a list of strokes; a stroke is a list of (x, y) points in unit space
# (centre 0,0, radius about 1). Strokes are revealed in order by cumulative length.


def circle(cx, cy, r, n=180, start=0.0):
    return [(cx + r * math.cos(start + 2 * math.pi * i / n), cy + r * math.sin(start + 2 * math.pi * i / n)) for i in range(n + 1)]


def poly(pts, closed=True):
    return list(pts) + ([pts[0]] if closed else [])


def ngon(n, r, rot=-math.pi / 2):
    return [(r * math.cos(rot + 2 * math.pi * i / n), r * math.sin(rot + 2 * math.pi * i / n)) for i in range(n)]


def hex_centres(r, rings):
    out = {(0.0, 0.0)}
    for q in range(-rings, rings + 1):
        for s in range(-rings, rings + 1):
            t = -q - s
            if max(abs(q), abs(s), abs(t)) <= rings:
                out.add((r * (q + s / 2), r * s * math.sqrt(3) / 2))
    return sorted(out, key=lambda p: (round(math.hypot(*p), 3), math.atan2(p[1], p[0])))


def seed_of_life():
    r = 0.33
    return [circle(0, 0, r * 2.02)] + [circle(x, y, r) for x, y in hex_centres(r, 1)]


def flower_of_life():
    r = 0.24
    cs = [c for c in hex_centres(r, 2) if math.hypot(*c) < 2 * r + 1e-6]
    return [circle(0, 0, r * 3.05), circle(0, 0, r * 3.15)] + [circle(x, y, r) for x, y in cs]


def metatron():
    r = 0.15
    cs = [(0.0, 0.0)] + [(2 * r * math.cos(a), 2 * r * math.sin(a)) for a in [math.pi / 6 + k * math.pi / 3 for k in range(6)]] \
        + [(4 * r * math.cos(a), 4 * r * math.sin(a)) for a in [math.pi / 6 + k * math.pi / 3 for k in range(6)]]
    lines = [[cs[i], cs[j]] for i in range(13) for j in range(i + 1, 13)]
    return [circle(x, y, r) for x, y in cs] + lines


def merkaba():
    a, b = ngon(3, 0.9), ngon(3, 0.9, rot=math.pi / 2)
    return [circle(0, 0, 0.92), poly(a), poly(b), circle(0, 0, 0.45), poly(ngon(6, 0.52, rot=0))]


def vesica():
    return [circle(-0.3, 0, 0.6), circle(0.3, 0, 0.6), circle(0, 0, 0.92), [(0, -0.52), (0, 0.52)], [(-0.9, 0), (0.9, 0)]]


def tree_of_life():
    s = 0.27
    pts = {1: (0, -3.2), 2: (1, -2.6), 3: (-1, -2.6), 4: (1, -1.4), 5: (-1, -1.4), 6: (0, -0.8), 7: (1, 0.2), 8: (-1, 0.2), 9: (0, 0.8), 10: (0, 2.0)}
    pts = {k: (x * 0.55 * s * 3.2, (y + 0.6) * s) for k, (x, y) in pts.items()}
    paths = [(1, 2), (1, 3), (1, 6), (2, 3), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (4, 6), (4, 7), (5, 6), (5, 8),
             (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
    return [[pts[a], pts[b]] for a, b in paths] + [circle(x, y, 0.085, 60) for x, y in pts.values()]


def enneagram():
    p = ngon(9, 0.85)  # p[0] is the top point, then clockwise
    pt = {n: p[n % 9] for n in range(1, 10)}  # 9 at the top, 1-8 clockwise
    return [circle(0, 0, 0.85), poly([pt[3], pt[6], pt[9]]), poly([pt[n] for n in (1, 4, 2, 8, 5, 7)])] + [circle(x, y, 0.04, 30) for x, y in p]


def pentagram():
    p = ngon(5, 0.85)
    return [circle(0, 0, 0.9), poly([p[0], p[2], p[4], p[1], p[3]]), circle(0, 0, 0.36)]


def wheel_of_year():
    spokes = [[(0.22 * math.cos(a), 0.22 * math.sin(a)), (0.9 * math.cos(a), 0.9 * math.sin(a))] for a in [k * math.pi / 4 for k in range(8)]]
    knots = [circle(0.9 * math.cos(a), 0.9 * math.sin(a), 0.06, 40) for a in [k * math.pi / 4 for k in range(8)]]
    return [circle(0, 0, 0.9), circle(0, 0, 0.22)] + spokes + knots


def golden_spiral():
    phi = (1 + 5 ** 0.5) / 2
    strokes, pts = [], []
    for i in range(400):
        th = i / 400 * 4.2 * math.pi
        r = 0.9 * phi ** (-2 * (4.2 * math.pi - th) / math.pi)
        pts.append((r * math.cos(th), r * math.sin(th)))
    return [circle(0, 0, 0.92), pts]


def bagua():
    out = [circle(0, 0, 0.92), poly(ngon(8, 0.62, rot=math.pi / 8))]
    trigrams = ['111', '011', '101', '001', '110', '010', '100', '000']
    for k, tri in enumerate(trigrams):
        a = -math.pi / 2 + k * math.pi / 4
        ux, uy = math.cos(a), math.sin(a)
        tx, ty = -uy, ux
        for j, bit in enumerate(tri):
            d = 0.7 + j * 0.07
            cx, cy = d * ux, d * uy
            if bit == '1':
                out.append([(cx - 0.12 * tx, cy - 0.12 * ty), (cx + 0.12 * tx, cy + 0.12 * ty)])
            else:
                out.append([(cx - 0.12 * tx, cy - 0.12 * ty), (cx - 0.03 * tx, cy - 0.03 * ty)])
                out.append([(cx + 0.03 * tx, cy + 0.03 * ty), (cx + 0.12 * tx, cy + 0.12 * ty)])
    return out


def chakras():
    ys = [0.85 - i * 0.283 for i in range(7)]
    return [[(0, 0.95), (0, -0.95)]] + [circle(0, y, 0.11, 70) for y in ys] + [circle(0, y, 0.17, 90) for y in ys[::2]]


def cymatics():
    return [circle(0, 0, 0.12 * k, 200) for k in range(1, 8)] + [poly(ngon(6, 0.84, rot=0))]


def zodiac_wheel():
    out = [circle(0, 0, 0.92), circle(0, 0, 0.7), circle(0, 0, 0.25)]
    for k in range(12):
        a = k * math.pi / 6
        out.append([(0.7 * math.cos(a), 0.7 * math.sin(a)), (0.92 * math.cos(a), 0.92 * math.sin(a))])
    return out


ZODIAC = '♈♉♊♋♌♍♎♏♐♑♒♓'

# 3D solids (vertices, edges) for a slow tumble
PHI = (1 + 5 ** 0.5) / 2
ICOSA_V = [(-1, PHI, 0), (1, PHI, 0), (-1, -PHI, 0), (1, -PHI, 0), (0, -1, PHI), (0, 1, PHI), (0, -1, -PHI), (0, 1, -PHI),
           (PHI, 0, -1), (PHI, 0, 1), (-PHI, 0, -1), (-PHI, 0, 1)]
OCTA_V = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def edges_by_length(vs):
    d = sorted({round(math.dist(a, b), 4) for i, a in enumerate(vs) for b in vs[i + 1:]})[0]
    return [(i, j) for i in range(len(vs)) for j in range(i + 1, len(vs)) if abs(math.dist(vs[i], vs[j]) - d) < 1e-3]


SOLIDS = {'icosahedron': (ICOSA_V, edges_by_length(ICOSA_V)), 'octahedron': (OCTA_V, edges_by_length(OCTA_V))}

FIGURES = {f.__name__: f for f in (seed_of_life, flower_of_life, metatron, merkaba, vesica, tree_of_life, enneagram, pentagram,
                                    wheel_of_year, golden_spiral, bagua, chakras, cymatics, zodiac_wheel)}

TOPIC_SYMBOL = [  # first keyword found in the slug wins
    ('kabbalah', 'tree_of_life'), ('akashic', 'tree_of_life'), ('enneagram', 'enneagram'), ('astrology', 'zodiac_wheel'),
    ('telescope', 'zodiac_wheel'), ('stargaz', 'zodiac_wheel'), ('moon', 'wheel_of_year'), ('wheel-of-the-year', 'wheel_of_year'),
    ('yule', 'wheel_of_year'), ('sacred-geometry', 'metatron'), ('chakra', 'chakras'), ('reiki', 'chakras'), ('aura', 'chakras'),
    ('yoga', 'chakras'), ('crystal', 'octahedron'), ('candle', 'pentagram'), ('herb', 'pentagram'), ('sage', 'pentagram'),
    ('i-ching', 'bagua'), ('feng-shui', 'bagua'), ('human-design', 'bagua'), ('manifest', 'golden_spiral'),
    ('numerolog', 'golden_spiral'), ('sound', 'cymatics'), ('meditation', 'flower_of_life'), ('astral', 'merkaba'),
    ('lucid', 'icosahedron'), ('tarot', 'merkaba'), ('oracle', 'merkaba'), ('relationship', 'vesica'), ('manipulation', 'vesica'),
    ('shadow', 'vesica'), ('pendulum', 'vesica'), ('scry', 'seed_of_life'), ('tea-leaf', 'seed_of_life'), ('hermetic', 'metatron'),
    ('kybalion', 'metatron'), ('rune', 'flower_of_life'), ('palm', 'seed_of_life'), ('gift', 'flower_of_life'),
]
FALLBACK = ['flower_of_life', 'metatron', 'seed_of_life', 'merkaba', 'icosahedron']


def pick_symbol(slug):
    for key, sym in TOPIC_SYMBOL:
        if key in slug:
            return sym
    return FALLBACK[int(hashlib.md5(slug.encode()).hexdigest(), 16) % len(FALLBACK)]


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def stroke_reveal(strokes, frac):
    """Return the strokes cut to the first `frac` of total length."""
    lens = [sum(math.dist(s[i], s[i + 1]) for i in range(len(s) - 1)) for s in strokes]
    budget = frac * sum(lens)
    out = []
    for s, L in zip(strokes, lens):
        if budget <= 0:
            break
        if budget >= L:
            out.append(s)
            budget -= L
            continue
        part = [s[0]]
        for i in range(len(s) - 1):
            d = math.dist(s[i], s[i + 1])
            if budget >= d:
                part.append(s[i + 1])
                budget -= d
            else:
                t = budget / d
                part.append((s[i][0] + t * (s[i + 1][0] - s[i][0]), s[i][1] + t * (s[i + 1][1] - s[i][1])))
                budget = 0
                break
        out.append(part)
        break
    return out


def project_solid(name, t):
    vs, es = SOLIDS[name]
    m = max(math.hypot(*v) for v in vs)
    a, b = 0.6 + t * 0.35, 0.3 + t * 0.22
    pts = []
    for x, y, z in vs:
        x, y, z = x / m, y / m, z / m
        x, z = x * math.cos(a) + z * math.sin(a), -x * math.sin(a) + z * math.cos(a)
        y, z = y * math.cos(b) - z * math.sin(b), y * math.sin(b) + z * math.cos(b)
        s = 2.6 / (3.2 - z)
        pts.append((x * s * 0.95, y * s * 0.95))
    return [[pts[i], pts[j]] for i, j in es]


UPRIGHT = {'tree_of_life', 'chakras', 'enneagram', 'pentagram'}  # orientation carries meaning: no spin
SYM = 860   # symbol panel size on screen
SS = 2      # supersampling for anti-aliased lines


def draw_symbol(name, t, reveal):
    size = SYM * SS
    layer = Image.new('L', (size, size), 0)
    d = ImageDraw.Draw(layer)
    if name in SOLIDS:
        strokes = project_solid(name, t)
        rot = 0.0
    else:
        strokes = FIGURES[name]()
        rot = 0.0 if name in UPRIGHT else t * 0.08  # slow turn, radians per second
    strokes = stroke_reveal(strokes, reveal)
    c, sc = size / 2, size * 0.46
    cr, sr = math.cos(rot), math.sin(rot)
    for s in strokes:
        pts = [(c + sc * (x * cr - y * sr), c + sc * (x * sr + y * cr)) for x, y in s]
        if len(pts) > 1:
            d.line(pts, fill=255, width=3 * SS, joint='curve')
    if name == 'zodiac_wheel' and reveal > 0.6:
        f = ImageFont.truetype(FONTS + 'seguisym.ttf', 44 * SS)
        alpha = int(255 * ease((reveal - 0.6) / 0.4))
        for k, g in enumerate(ZODIAC):
            a = math.pi - (k + 0.5) * math.pi / 6 + rot  # Aries at the left, signs run counterclockwise
            x, y = c + sc * 0.81 * math.cos(a), c + sc * 0.81 * math.sin(a)
            d.text((x, y), g, font=f, fill=alpha, anchor='mm')
    return layer.resize((SYM, SYM), Image.LANCZOS)


# ---------------------------------------------------------------- backgrounds

BG_DIR = os.path.join(HERE, 'backgrounds', 'picks')
BG_TOPICS = [  # first keyword found in the slug wins; scene files live in backgrounds/picks/
    ('kitchen', ['kitchen', 'pantry', 'spice', 'coffee', 'espresso', 'baking', 'refrigerator', 'freezer', 'food-storage',
                 'under-sink', 'wine', 'water-bottle', 'knife', 'knives', 'pots-and-pans', 'cookware']),
    ('closet', ['closet', 'bedroom', 'shoe', 'sock', 'jewelry', 'makeup', 'under-bed', 'linen', 'guest-room', 'dorm', 'nursery']),
    ('entryway', ['entryway', 'winter-gear', 'garage', 'car-', 'pet', 'laundry', 'recycling', 'cleaning', 'travel']),
    ('home-office', ['office', 'desk', 'cord', 'cable', 'bookshelf', 'craft', 'digital', 'iphone', 'board-game', 'junk-drawer']),
    ('winter-living-room', ['humidifier', 'purifier', 'heater', 'holiday', 'christmas', 'robot-vacuum', 'gift', 'hosting',
                            'living-room', 'game-room', 'home-gym', 'indoor-growing', 'bathroom']),
]


def auto_background(slug):
    for name, keys in BG_TOPICS:
        if any(k in slug for k in keys):
            path = os.path.join(BG_DIR, name + '.jpg')
            if os.path.exists(path):
                return path
    return None



def starfield(seed):
    rnd = random.Random(seed)
    bg = Image.new('RGB', (W, H))
    top, bot = (16, 12, 34), (44, 26, 70)
    px = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H
        px.line([(0, y), (W, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    stars = [(rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(0.6, 2.2), rnd.uniform(0, 6.28)) for _ in range(260)]
    return bg, stars


def photo_background(path):
    im = Image.open(path).convert('RGB')
    s = max(W / im.width, H / im.height) * 1.12
    return im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)


def gradient_overlay():
    g = Image.new('L', (1, H))
    for y in range(H):
        t = y / H
        g.putpixel((0, y), int(200 * max(0, 1 - t / 0.38) ** 1.4 + 210 * max(0, (t - 0.55) / 0.45) ** 1.3))
    return g.resize((W, H))


# ---------------------------------------------------------------- product tiles


def product_images(site, slug):
    """All product photos on the article, in article order (render_card stops at three)."""
    root = os.path.join(DOWNLOADS, f'vonguul-{site}')
    text = open(os.path.join(root, 'src', 'content', 'articles', slug + '.md'), encoding='utf-8').read()
    fm = yaml.safe_load(text.split('---')[1])
    paths = [os.path.join(root, 'public') + p['image'] for p in fm.get('products', []) if p.get('image')]
    return [p for p in paths if os.path.exists(p)]



def product_tile(path, w, h):
    t = Image.new('RGBA', (w, h), (255, 255, 255, 255))
    im = Image.open(path).convert('RGBA')
    bg = Image.new('RGBA', im.size, (255, 255, 255, 255))
    bg.alpha_composite(im)
    im = bg.convert('RGB')
    im.thumbnail((w - 36, h - 36), Image.LANCZOS)
    t.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    m = Image.new('L', (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], 26, fill=255)
    t.putalpha(m)
    return t


def shadow_text(base, xy, text, font, fill, anchor='la', blur=6):
    sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((xy[0] + 3, xy[1] + 4), text, font=font, fill=(0, 0, 0, 190), anchor=anchor)
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(base).text(xy, text, font=font, fill=fill, anchor=anchor)


# ---------------------------------------------------------------- frames


def render(site, slug, headline, out, symbol=None, bg_path=None):
    th = THEME[site]
    prods = product_images(site, slug)
    n = len(prods)
    tw = 300 if n >= 3 else 360
    gap = 30
    hfont = ImageFont.truetype(FONTS + th['head'], 76)
    lines = wrap(ImageDraw.Draw(Image.new('RGB', (1, 1))), headline, hfont, W - 150)
    text_bottom = 210 + len(lines) * 92 + 40
    hero_size = max(360, min(620, 1180 - 40 - text_bottom))
    hero = product_tile(prods[0], hero_size, hero_size) if site == 'picks' and prods else None
    row = prods[1:4] if hero is not None and len(prods) >= 4 else prods[:3]
    tiles = [product_tile(p, tw, tw) for p in row]
    sfont = ImageFont.truetype(FONTS + 'segoeuib.ttf', 34)
    cfont = ImageFont.truetype(FONTS + 'segoeui.ttf', 38)

    if site == 'clarity':
        name = symbol or pick_symbol(slug)
        base, stars = starfield(int(hashlib.md5(slug.encode()).hexdigest(), 16) % 10 ** 6)
        photo = None
    else:
        if bg_path == 'auto':
            bg_path = auto_background(slug)
            print('background:', os.path.basename(bg_path) if bg_path else 'none (no scene matches; blurred product)')
        if bg_path and bg_path != 'none' and os.path.exists(bg_path):
            photo = photo_background(bg_path)
        else:  # no AI scene: a blurred, enlarged real product photo behind everything
            photo = photo_background(prods[0]).filter(ImageFilter.GaussianBlur(38))
        shade = gradient_overlay()

    ff = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-shortest', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
           '-crf', '20', '-preset', 'medium', '-c:a', 'aac', '-movflags', '+faststart', out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    total = FPS * SECONDS
    tiles_top = 1290 if site == 'clarity' else 1180
    last = None
    for f in range(total):
        t = f / FPS
        if site == 'clarity':
            frame = base.copy().convert('RGBA')
            sd = ImageDraw.Draw(frame)
            for x, y, r, ph in stars:
                a = int(120 + 120 * math.sin(ph + t * 1.7))
                sd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 245, 225, a))
            reveal = ease(t / 4.2)
            sym = draw_symbol(name, t, reveal)
            glow = sym.filter(ImageFilter.GaussianBlur(14))
            pulse = 0.75 + 0.25 * math.sin(t * 2.1)
            sx, sy = (W - SYM) // 2, 390 if n else 600
            gl = Image.new('RGBA', (SYM, SYM), th['acc'] + (0,))
            gl.putalpha(glow.point(lambda v: int(v * 0.9 * pulse)))
            frame.alpha_composite(gl, (sx, sy))
            ln = Image.new('RGBA', (SYM, SYM), (250, 226, 170, 0))
            ln.putalpha(sym)
            frame.alpha_composite(ln, (sx, sy))
        else:
            z = 1.0 + 0.07 * (t / SECONDS)
            cw, ch = int(W * 1.12 / z), int(H * 1.12 / z)
            ox, oy = (photo.width - cw) // 2, (photo.height - ch) // 2 - int(30 * t / SECONDS)
            frame = photo.crop((ox, max(0, oy), ox + cw, max(0, oy) + ch)).resize((W, H), Image.BILINEAR).convert('RGBA')
            dark = Image.new('RGBA', (W, H), (10, 12, 16, 0))
            dark.putalpha(shade)
            frame.alpha_composite(dark)

        # Picks hero: the lead product, enlarged, drifting slightly
        if hero is not None:
            hp = ease((t - 0.4) / 0.8)
            if hp > 0:
                z = 1.0 + 0.05 * (t / SECONDS)
                hs = int(hero_size * z)
                hh = hero.resize((hs, hs), Image.LANCZOS)
                hh.putalpha(hh.getchannel('A').point(lambda v: int(v * hp)))
                frame.alpha_composite(hh, ((W - hs) // 2, text_bottom - (hs - hero_size) // 2 + int(60 * (1 - hp))))

        # brand + headline
        hk = ease((t - 0.2) / 0.8)
        if hk > 0:
            layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            shadow_text(layer, (75, 150), th['brand'], sfont, th['acc'] + (255,))
            y = 210
            for ln_ in lines:
                shadow_text(layer, (75, y), ln_, hfont, (255, 255, 255, 255))
                y += 92
            layer.putalpha(layer.getchannel('A').point(lambda v: int(v * hk)))
            frame.alpha_composite(layer, (0, int(40 * (1 - hk))))

        # products rise in one by one
        x0 = (W - (len(tiles) * tw + (len(tiles) - 1) * gap)) // 2
        for i, tl in enumerate(tiles):
            p = ease((t - 3.4 - i * 0.45) / 0.7)
            if p <= 0:
                continue
            tt = tl.copy()
            tt.putalpha(tt.getchannel('A').point(lambda v: int(v * p)))
            frame.alpha_composite(tt, (x0 + i * (tw + gap), tiles_top + int(120 * (1 - p))))

        # call to action
        c = ease((t - 6.6) / 0.7)
        if c > 0:
            layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
            shadow_text(layer, (W // 2, 1660), th['cta'], cfont, (255, 255, 255, 255), anchor='mm')
            layer.putalpha(layer.getchannel('A').point(lambda v: int(v * c)))
            frame.alpha_composite(layer)

        last = frame.convert('RGB')
        proc.stdin.write(last.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        sys.exit('ffmpeg failed')
    still = os.path.splitext(out)[0] + '.png'
    last.save(still)
    print('wrote', out, 'and', still, '| symbol:' if site == 'clarity' else '', name if site == 'clarity' else '')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('site', choices=['picks', 'clarity'])
    ap.add_argument('slug')
    ap.add_argument('headline')
    ap.add_argument('out')
    ap.add_argument('--symbol', choices=sorted(list(FIGURES) + list(SOLIDS)))
    ap.add_argument('--bg', help="Picks background: 'auto' (AI room scene matched to the topic), 'none' (blurred product photo), or a file path")
    a = ap.parse_args()
    render(a.site, a.slug, a.headline, a.out, a.symbol, a.bg)
