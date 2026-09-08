# Vonguul Picks — Instagram Feed Posts Tracker

Account: **@offbahr** on Instagram — same real personal account/login used for
Vonguul Clarity's Instagram and Threads presence (see vonguul-clarity's
`INSTAGRAM-POSTS.md` / `THREADS-POSTS.md`). As of 2026-09-08, this account is
shared across both Picks and Clarity content, matching the precedent already
set for X (`@OffbahrV`) posting both.

Bio link: `vonguul.com/support` (movement/support funnel, not article-specific
— captions point to "link in bio" since Instagram captions don't support
real clickable links).

## Format

Pinterest-pin-style static image: reuse the article's existing `PIN-BATCH-XX.md`
Pin 1 title + hero image, laid out as a dark title bar (bold white headline)
over the product photo, with a "VONGUUL PICKS / FULL BREAKDOWN → BIO" footer.
Built as an HTML page, rendered via a local screenshot, uploaded directly to
Instagram's composer from the screenshot's imageId (no intermediate file).

Caption pulls from the same pin's description, ends with "link in bio", and
closes with 4-5 relevant hashtags. Crop step: always select "Original" aspect
ratio (default crop is square and will cut off a landscape card's sides).

**Rendering gotcha (2026-09-08):** don't rely on a full-viewport-filling HTML
page + browser screenshot for the source image — the browser's actual
viewport can silently be an unsafe aspect ratio (seen: 1568x737 = 2.13:1,
over Instagram's 1.91:1 max) that `resize_window` doesn't reliably fix, and
Instagram rejects the upload with "isn't in an allowed aspect ratio." Fix:
render onto a fixed-pixel `<canvas>` (1200x750, a safe 1.6:1) via JS, extract
with `toBlob()`, and POST it to a same-origin local save endpoint (custom
Python `http.server` handling `POST /save?name=...`) rather than triggering
a file download — Chrome blocks repeated script-triggered downloads from the
same origin, and cross-port fetch trips Private Network Access preflight
failures. See vonguul-clarity's `canvas-card.html` for the working template.
Threads cross-post toggle left OFF for every post (Picks has no tailored
Threads presence, but keeping it off avoids surprise duplicate posting until
that's a deliberate decision).

Always draft and show the rendered image + caption for review before
posting — real account, real followers.

## Status

| Batch | Article | Posted |
|---|---|---|
| 21 | refrigerator-organization-ideas.md | posted 2026-09-08 |
| 22 | spice-rack-organization-ideas.md | posted 2026-09-08 |
| 23 | makeup-vanity-organization-ideas.md | posted 2026-09-08 |
| 24 | pet-supplies-organization-ideas.md | posted 2026-09-08 |
| 1 | small-pantry-organization-ideas.md | posted 2026-09-08 |
| 2 | small-bedroom-closet-organization-ideas.md | posted 2026-09-08 |
| 3 | small-bathroom-storage-ideas.md | posted 2026-09-08 |
| 4 | kitchen-counter-organization-ideas.md | posted 2026-09-08 |
| 5 | entryway-organization-ideas.md | posted 2026-09-08 |
| 6 | garage-organization-ideas.md | posted 2026-09-08 |
| 7 | home-office-organization-ideas.md | posted 2026-09-08 |
| 8 | laundry-room-organization-ideas.md | posted 2026-09-08 |

12 batches remain (9-20): Kids'/Toy Room, Linen Closet, Under-Sink, Craft
Room, Dorm Room, Nursery, Home Gym, Jewelry, Food Storage, Cleaning
Supplies, Under-Bed Storage, Sock/Drawer Organization. Continue in order
when asked.

**Additional note from batches 5-8 (2026-09-08):** the claude-in-chrome
browser tab occasionally loses its actual viewport (screenshot calls fail
with "Cannot take screenshot with 0 width" and `read_page` returns an empty
tree, even though `find` and `javascript_tool` keep working and clicks still
land). If this happens mid-post, don't keep fighting the stuck tab — close
it and open a fresh one (`tabs_create_mcp`), then restart that post's upload
from scratch rather than trying to resume blind.

**Reliability notes from batches 1-4 (2026-09-08):**
- The canvas page's download button is unreliable via the `computer` tool's
  synthetic click (silently no-ops on some renders); triggering it via
  `document.getElementById('dlbtn').click()` through `javascript_tool` works
  every time — prefer that method going forward.
- Always pass `&brand=VONGUUL PICKS` explicitly in the canvas URL — the
  template defaults to "VONGUUL CLARITY" if the param is omitted, which
  silently produces a mislabeled card for this site.
- Instagram's composer view sometimes renders zoomed/shifted between clicks
  (a `Note...` tooltip element pushes the whole layout down), which can make
  a stale-coordinate click land on the wrong control (e.g. the X/close
  button instead of Next) and trigger a "Discard post?" prompt — always
  re-screenshot immediately before clicking Next/Share rather than reusing
  coordinates from an earlier screenshot, and hit Cancel if a discard dialog
  appears unexpectedly.

## How to apply for new/remaining batches

1. Find the article's `PIN-BATCH-XX.md`, reuse Pin 1's title + description
   as headline/caption basis.
2. Build the HTML card (dark title bar + product hero image + footer),
   using the article's actual hero image from `public/images/products/`.
3. Serve locally (`python -m http.server` in the scratchpad dir), screenshot,
   upload directly from the screenshot's imageId to Instagram's composer —
   note screenshot IDs expire, so take a fresh one right before each upload.
4. Crop: select "Original" aspect ratio. Skip filters.
5. Caption: pin description + "link in bio" + hashtags. Leave Threads
   toggle off.
6. Update this table, commit/push.
