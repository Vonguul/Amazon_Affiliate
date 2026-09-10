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
