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

20 earlier batches (1-20) not yet done — this was a pilot batch of 4
(the most recent), per user direction. Continue with the remaining batches
in order when asked.

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
