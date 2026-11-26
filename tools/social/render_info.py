"""Informational post video: one background image, a slow zoom, captions timed to a voiceover, and a music bed.

Used for the "pure informational" posts (a fact or tip, not a product pitch). The background is usually one
AI-generated image (ElevenLabs), so the post MUST carry the AI label on TikTok and Pinterest; pass --ai-label
to also print a small "AI-generated image" note on the video itself.

  python render_info.py <picks|clarity> <background.jpg|png|.url> <out.mp4> --title "..." --line "..." --line "..."
         [--voice vo.mp3|vo.url] [--music bed.mp3] [--ai-label] [--title-y 620]

The background and the voice can each be a .url/.txt file holding the ElevenLabs download link. The music defaults
to the site's bed in tools/social/audio/.

Captions: the title shows the whole time; each --line appears in turn, spread over the voiceover. The video runs
for the voiceover plus 1.2 s (at least 8 s). Writes <out>.png (the last frame) next to the MP4.
"""
import argparse
import os
import subprocess
import sys
import tempfile
import urllib.request

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(__file__))
from render_motion import (FONTS, FPS, H, MUSIC_BED, THEME, VOICE_LEAD, W, add_audio, ease, fetch_voice,  # noqa: E402
                           gradient_overlay, media_seconds, photo_background, shadow_text)
from render_card import wrap  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()


def fetch_image(src):
    url = open(src, encoding='utf-8').read().strip()
    if not url.startswith('https://elevenlabsusercontent.com/'):
        sys.exit('image link must be an elevenlabsusercontent.com URL')
    dst = os.path.join(tempfile.mkdtemp(), 'bg' + (os.path.splitext(url.split('?')[0])[1] or '.png'))
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=60) as r, open(dst, 'wb') as f:
        f.write(r.read())
    keep = os.path.splitext(OUT_HINT[0])[0] + '-bg' + os.path.splitext(dst)[1] if OUT_HINT else None
    if keep:
        with open(dst, 'rb') as a, open(keep, 'wb') as b:
            b.write(a.read())
    return dst


OUT_HINT = []


def render(site, bg, out, title, lines, voice=None, music=None, ai_label=False, title_y=210):
    th = THEME[site]
    voice = fetch_voice(voice)
    music = music or (MUSIC_BED[site] if os.path.exists(MUSIC_BED[site]) else None)
    vo_len = media_seconds(voice) if voice else 0
    seconds = max(8.0, vo_len + VOICE_LEAD + 0.9)
    lead = VOICE_LEAD
    if bg.lower().endswith(('.url', '.txt')):
        bg = fetch_image(bg)
    photo = photo_background(bg)
    shade = gradient_overlay()
    tfont = ImageFont.truetype(FONTS + th['head'], 72)
    lfont = ImageFont.truetype(FONTS + 'segoeuib.ttf', 58)
    sfont = ImageFont.truetype(FONTS + 'segoeuib.ttf', 34)
    nfont = ImageFont.truetype(FONTS + 'segoeui.ttf', 26)
    d = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    tlines = wrap(d, title, tfont, W - 150)
    cap = [wrap(d, ln, lfont, W - 170) for ln in lines]
    span = (vo_len or seconds - 1.5) / max(1, len(cap))

    silent = os.path.join(tempfile.mkdtemp(), 'v.mp4')
    proc = subprocess.Popen([FF, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                             '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', silent],
                            stdin=subprocess.PIPE)
    last = None
    for f in range(int(seconds * FPS)):
        t = f / FPS
        z = 1.0 + 0.08 * (t / seconds)
        cw, ch = int(W * 1.12 / z), int(H * 1.12 / z)
        ox, oy = (photo.width - cw) // 2, (photo.height - ch) // 2
        frame = photo.crop((ox, oy, ox + cw, oy + ch)).resize((W, H), Image.BILINEAR).convert('RGBA')
        dark = Image.new('RGBA', (W, H), (8, 10, 18, 0))
        dark.putalpha(shade)
        frame.alpha_composite(dark)

        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        k = ease((t - 0.1) / 0.7)
        shadow_text(layer, (75, title_y - 60), th['brand'], sfont, th['acc'] + (int(255 * k),))
        y = title_y
        for tl in tlines:
            shadow_text(layer, (75, y), tl, tfont, (255, 255, 255, int(255 * k)))
            y += 88
        # one caption at a time, low on the screen
        i = min(len(cap) - 1, int(max(0.0, t - lead) / span)) if cap else -1
        if i >= 0:
            a = ease((t - lead - i * span) / 0.35)
            yy = 1330
            for cl in cap[i]:
                shadow_text(layer, (W // 2, yy + int(30 * (1 - a))), cl, lfont, (255, 255, 255, int(255 * a)), anchor='mm')
                yy += 74
        if ai_label:
            shadow_text(layer, (W - 40, H - 60), 'AI-generated image', nfont, (235, 235, 235, 200), anchor='rm', blur=3)
        frame.alpha_composite(layer)
        last = frame.convert('RGB')
        proc.stdin.write(last.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        sys.exit('ffmpeg failed (video)')

    add_audio(silent, out, seconds, voice, music)
    still = os.path.splitext(out)[0] + '.png'
    last.save(still)
    print(f'wrote {out} ({seconds:.1f} s) and {still}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('site', choices=['picks', 'clarity'])
    ap.add_argument('background')
    ap.add_argument('out')
    ap.add_argument('--title', required=True)
    ap.add_argument('--line', action='append', default=[])
    ap.add_argument('--voice')
    ap.add_argument('--music')
    ap.add_argument('--ai-label', action='store_true')
    ap.add_argument('--title-y', type=int, default=210, help='top of the title (move it down when the picture has its subject up top)')
    a = ap.parse_args()
    OUT_HINT.append(a.out)  # a downloaded background is also kept as <out>-bg.png
    render(a.site, a.background, a.out, a.title, a.line, a.voice, a.music, a.ai_label, a.title_y)
