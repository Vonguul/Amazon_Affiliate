# Vonguul Picks — Instagram Stories Tracker (VG-52)

Account: **@offbahr** on Instagram — same account as the feed post tracker
(`INSTAGRAM-POSTS.md`). Stories are a separate, additive channel: a traffic
experiment (per the Vonguul Operations Command Framework, Section 22.3) to
send viewers straight to a specific article via a link sticker, without
touching the mission-first `vonguul.com/support` bio link used by every feed
caption.

## Why this exists

Analytics review on 2026-09-09/10 found the Instagram feed → bio link path
converting almost nobody (2 external link taps in 30 days on 284 views,
across dozens of feed posts). Stories support a **link sticker** that jumps
straight to a specific article — no bio-link detour, no scrolling past
movement framing first. This is the fix being tested for that funnel gap.

## Posting process (Instagram web does NOT support Story creation —
## use Meta Business Suite instead)

1. Go to `business.facebook.com` → log in with "Continue with Instagram"
   (requires the user to complete this login step interactively; the
   session doesn't carry over silently from instagram.com).
2. Home → **Create story**.
3. Select the **Instagram story** tab (not Facebook story — the composer
   defaults to showing both, but only check the `offbahr` row under "Share
   to", leaving the Facebook Page unchecked, since the Page has 0 followers
   and isn't part of this operation).
4. Click **Add photo/video**. **This opens a native OS file picker that
   cannot be automated** — the user has to select the file themselves.
   Reuse the existing canvas-card PNGs already rendered for feed posts
   (1200×750, in the scratchpad) rather than building new art per Story.
5. Click **Edit** on the uploaded photo.
   - Crop: "Original" keeps the whole card (headline + branding) intact,
     letterboxed top/bottom on a vertical screen. "Fullscreen vertical
     (9:16)" crops in tight and cuts off the headline/branding — avoid it
     for these landscape feed-card assets.
   - Stickers → **More stickers** → **Link**. This is the actual Instagram
     link sticker (the top-level "Add link" button next to the photo
     thumbnail is Facebook-only — it's disabled/grayed when only Instagram
     is selected as the destination, and the tooltip literally says "swipe
     up link to your **Facebook** story").
   - Paste the article URL with `?src=instagram` (same convention as feed
     posts — see [[vonguul-affiliate-tracking-ids]]).
   - Custom sticker text: 25-character limit. Something like "See full
     breakdown" fits; don't let it get truncated mid-word.
   - Apply.
6. Confirm "Share to" still shows only `offbahr`, Schedule = "Share now",
   then **Share**.
7. Verify: go to instagram.com/offbahr/, click the profile picture — it
   opens `/stories/offbahr/` and the Story (with tappable link sticker)
   should be visible there.

## Status

| Article | Posted | Link sticker text | Notes |
|---|---|---|---|
| under-sink-organization-ideas.md | posted 2026-09-10 | "See full breakdown" | Pilot post — process above written from this run. Confirmed live via /stories/offbahr/. |
| craft-room-organization-ideas.md | posted 2026-09-10 | "See full breakdown" | Second Picks Story, scaling past the pilot. Confirmed live via /stories/offbahr/, ~31s after posting. Also accidentally cross-posted to the unused Facebook Page `offbar1` (misread the "Share to" checkbox state) — 0 views, auto-expired after 24h. Root cause and fix logged below. |
| small-bathroom-storage-ideas.md | posted 2026-09-12 | "See full breakdown" | VG-52 scale-up batch, approved via Result→Decision review (see [[vonguul-operations-command-framework]]). Confirmed Instagram-only. |
| small-bedroom-closet-organization-ideas.md | posted 2026-09-12 | "See full breakdown" | VG-52 scale-up batch. Confirmed Instagram-only. |
| entryway-organization-ideas.md | posted 2026-09-12 | "See full breakdown" | VG-52 scale-up batch. Confirmed Instagram-only. |
| kitchen-counter-organization-ideas.md | posted 2026-09-12 | "See full breakdown" | VG-52 scale-up batch. Confirmed Instagram-only. |
| shoe-storage-organization-ideas.md | posted 2026-09-15 | "See full breakdown" | Batch 29 Story, same-day follow-up to the feed post. Confirmed Instagram-only via checkbox-zoom. |
| coffee-bar-station-organization-ideas.md | posted 2026-09-15 | "See full breakdown" | Batch 30 Story. Confirmed Instagram-only. |
| freezer-organization-ideas.md | posted 2026-09-15 | "See full breakdown" | Batch 31 Story. Confirmed Instagram-only. |
| car-trunk-organization-ideas.md | posted 2026-09-15 | "See full breakdown" | Batch 32 Story. Confirmed Instagram-only. |
| board-game-puzzle-storage-ideas.md | posted 2026-09-17 | "See full breakdown" | Batch 33 Story, same-day follow-up to the feed post. Confirmed Instagram-only via Share-to check. |
| recycling-trash-bin-organization-ideas.md | posted 2026-09-17 | "See full breakdown" | Batch 34 Story. Confirmed Instagram-only. |
| water-bottle-tumbler-organization-ideas.md | posted 2026-09-17 | "See full breakdown" | Batch 35 Story. Confirmed Instagram-only. |
| bookshelf-home-library-organization-ideas.md | posted 2026-09-17 | "See full breakdown" | Batch 36 Story, last of this week's Picks batches. Confirmed Instagram-only. |
| baking-supplies-bakeware-organization-ideas.md | posted 2026-09-22 | "See full breakdown" | Reused `ig-card-baking.png`. Confirmed live via /stories/offbahr/, link sticker tappable. First attempt (before fixing process) used a new vertical no-link asset and was deleted/redone correctly — see "Process correction" note below. |
| car-trunk-organization-ideas.md (2nd post, tire inflator angle) | posted 2026-09-22 | "See full breakdown" | Reused `ig-card-cartrunk2.png`. Confirmed Instagram-only, Original crop. |
| spice-rack-organization-ideas.md (2nd post, uniform jars angle) | posted 2026-09-22 | "See full breakdown" | Reused `ig-card-spicerack2.png`. Confirmed Instagram-only, Original crop. |

## Checkbox gotcha (found 2026-09-10, confirmed 2026-09-12)

The "Share to" list under Create Story **always defaults to both accounts
checked** (the linked Facebook Page `offbar1` + Instagram `offbahr`) every
time the composer opens — it is not sticky from a prior session, and a quick
glance can misread a checked box as unchecked if the cursor happens to sit
over the checkmark in a screenshot (this is exactly how the craft-room
cross-post above happened). Fix, applied from 2026-09-12 onward: open the
"Share to" dropdown, move the mouse away from the checkboxes, then
screenshot/zoom on just that region before trusting what it shows — do this
both before unchecking the Facebook Page and again after, to positively
confirm only `offbahr` remains checked.

## Evidence

- 2026-09-10: Story posted, confirmed live at instagram.com/stories/offbahr/
  ~46s after posting, link sticker visible and pointing to
  `vonguul-picks.vercel.app/articles/under-sink-organization-ideas/?src=instagram`.
  Baseline metrics before this experiment (30-day): Instagram external link
  taps = 2, Vercel Analytics visitors = 12, Amazon Associates clicks = 24,
  revenue = $0. Re-check these after a few more Story posts to see if the
  link-sticker path moves any of them (framework Section 22.3 experiment
  structure: Hypothesis → Metric → Baseline → Experiment → Result →
  Decision — this row is the Baseline/Experiment start).
- 2026-09-10: Second Story (craft-room-organization-ideas) posted and
  confirmed live ~31s after posting, link sticker pointing to
  `vonguul-picks.vercel.app/articles/craft-room-organization-ideas/?src=instagram`.
  "VONGUUL PICKS" branding and full card intact (Original crop).
- 2026-09-11: Analytics re-check (7-day Vercel window) showed the first real
  signal: 1 visitor referred via `l.instagram.com` (Instagram's external-link
  redirect domain) — consistent with a Story link-sticker tap. Amazon
  Associates clicks unchanged at 24/30 days, $0 revenue — too early/thin a
  sample to call a result either way. Full breakdown in the "Vonguul Content
  Ops" artifact.
- 2026-09-12: Per the framework's Result→Decision gate (Section 22.3), the
  user approved scaling VG-52 up rather than holding or killing it. Posted 4
  more Stories (small-bathroom-storage, small-bedroom-closet, entryway,
  kitchen-counter) — all confirmed Instagram-only via the checkbox-zoom
  method above, no repeat of the Facebook cross-post.
- 2026-09-17: Analytics re-check (7-day Vercel window, checked immediately
  after posting Batch 33-36 Stories): 18 visitors (+29% WoW), 1 referred via
  `l.instagram.com`. This reflects the Sep 15 batch (shoe-storage,
  coffee-bar-station, freezer, car-trunk) and earlier — too soon after
  posting for the board-game-puzzle-storage/recycling-trash-bin/
  water-bottle-tumbler/bookshelf-home-library batch to register any clicks
  yet. Re-check in a few days for that batch's signal.

## Process correction (2026-09-22)

A resumed session (after a multi-day gap, driven partly by the user relaying
instructions from a native file-picker dialog it couldn't see) initially
posted the baking/car-trunk/spice-rack batch as plain static images on a
**new vertical 9:16 template**, with no link sticker at all — missing the
entire point of VG-52. Caught before any real traffic accrued, all 3 were
deleted and reposted correctly per the process above (existing 1200×750
feed cards, Original crop, Link sticker with `?src=instagram` + "See full
breakdown"). Lesson: always re-read this file's posting process before
resuming Stories work in a new session — don't rebuild the workflow from
memory or general Instagram/Meta Business Suite familiarity.
