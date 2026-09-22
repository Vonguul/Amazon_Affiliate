# Vonguul Picks — TikTok Tracker

Account: **@offbahrvonguul** on TikTok (the existing "Vonguul Movement" personal-brand
account: bio "Anomaly by birth, Vonguulian by choice... Support the Movement", link
`vonguul.com`, ~1382 followers before this batch). Same account is shared with
Vonguul Clarity, matching the precedent already set for Instagram/Threads/X.

## Format: Photo Mode, not video

TikTok's "Photos" upload tab (`tiktokstudio/upload?tab=photo`) accepts a static
image post instead of video — same 1200x750 canvas cards already built for the
Instagram feed pipeline (see `INSTAGRAM-POSTS.md` for the render process),
uploaded as-is via TikTok's own file input. No video/audio production needed.

Each post has a **Title** (max 90 chars, short and punchy — this is TikTok's
own "catchy title" field, separate from the caption) and a **Description**
(the caption, max 4000 chars) with inline hashtags. Posting mode: "Now" /
"Everyone" visibility.

**Link-in-bio only** — same constraint as Instagram, TikTok captions can't
carry a working link. Bio points to `vonguul.com`.

**Gotcha (2026-09-22): TikTok's own content moderation holds every first-time
post as "Content under review" with visibility silently downgraded to "Only
me", even though "Everyone" was selected at posting.** Not an error on the
posting side — every post in this batch cleared review and flipped to
"Everyone" within a few minutes on its own. No action needed; just don't be
alarmed if a freshly-posted TikTok photo shows "Only me" immediately after
posting.

**Gotcha (2026-09-22): title/description fields sometimes don't take the
first `type()` call right after a photo finishes uploading** (silently stays
at 0/90, 0/4000, as if nothing landed) — happened intermittently, roughly
every other post. Fix: re-run `find` for the field and retry the click+type;
the second attempt always worked. Always screenshot after typing to confirm
the field actually shows the new character count before moving to the next
field or clicking Post.

## Status

| Article | Title | Posted |
|---|---|---|
| baking-supplies-bakeware-organization-ideas.md | "The Baking Cabinet Organizer Nobody Tells You to Buy" | posted 2026-09-22 |
| car-trunk-organization-ideas.md (2nd post, tire inflator angle) | "A Tire Inflator That Lives in Your Trunk for Emergencies" | posted 2026-09-22 |
| spice-rack-organization-ideas.md (2nd post, uniform jars angle) | "Why Matching Spice Jars Actually Save You Time" | posted 2026-09-22 |

First 3 TikTok Photo Mode posts for Picks. 34 articles remain uncovered on
this platform (same backlog size as Threads' first-batch note, since TikTok
started at zero same as Threads did).

## How to apply for new articles

1. Reuse an existing rendered `ig-card-*.png` from the scratchpad if one
   already exists for the article (same visual works for both platforms);
   otherwise render a new one via `canvas-card.html` following the
   `INSTAGRAM-POSTS.md` process.
2. Navigate to `tiktokstudio/upload?tab=photo`, upload via the file input.
3. Fill Title (punchy, <90 chars) and Description (caption + 4-5 hashtags).
   Verify both landed via screenshot before proceeding (see gotcha above).
4. Leave "Now" / "Everyone" selected, click Post.
5. Expect "Content under review" / "Only me" immediately after — this
   self-resolves, don't attempt to fix it.
6. Update this table, commit/push.
