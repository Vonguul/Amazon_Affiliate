# Support Vonguul — Recurring Movement Post Tracker

Account: **@offbahr** (Instagram, Threads), **@OffbahrV** (X), **@offbahrvonguul**
(TikTok) — the shared personal/movement account across all platforms, not the
Picks/Clarity product-review voice. This tracker lives in `vonguul-picks`
since that's where the account's other cross-platform trackers
(`THREADS-POSTS.md`, `X-POSTS.md`) already live, but the content itself is
Vonguul-movement content, not Picks product content. **Not posted to
Pinterest** — that's Picks/Clarity product boards only, movement content
doesn't fit there.

## What this is

A recurring reminder post (target cadence: **at least once a week**)
explaining "Support in Passing" — the mechanism described on
`vonguul.com/support` in its own words: *"When you choose to explore or
purchase through one of those recommendations, you can support the work
here in passing... There is no pressure and no extra cost to you."*

The post also references Vonguul's direct-support tiers (Supporter/Builder/
Pioneer subscriptions on vonguul.com, concrete disclosed benefit: early
access to the Human Design app in development) without inventing additional
promises beyond what's actually published on the site.

**Every post includes a two-way ask**: comment or DM if something you want
isn't already set up through the Vonguul recommendation links, so it can be
added.

## Process for each week's post

This is **not** a copy-paste-forever template — the exact wording should
vary week to week. **At the start of each week's post, ask the user how they
want to proceed** (new angle, adjust tone, highlight something specific,
or reuse last week's wording) rather than silently reposting the same copy.
Draft, show for approval, then post once approved — same rule as every other
real-account post in this operation.

**Tone calibration (learned 2026-09-22, first post):** the user's audience
responds to belief/faith framing — several have compared Vonguul to a
"Black Jesus" figure unprompted. Copy that dismisses or downplays belief
("we don't need your belief, we need resources") tested badly with the
user's own read of their audience. The version that landed: treat belief as
the starting point, and frame support as what belief looks like in action
("if you believe in what Vonguul is building, this is where that belief
becomes useful/momentum").

## Asset

Text-only branded card (no product photo needed): `support-card.html` in
the scratchpad, same local-server render pipeline as `canvas-card.html`
(1200×750, same save-server on port 8791). Params: `headline`, `subtext`,
`brand`, `outname`. Reuse or regenerate per week's variant.

## Platform notes

- **Instagram feed**: full long-form version, all paragraphs. Original crop.
- **Threads**: short version (~500 char Threads limit), with the
  "Community or topic" tag set — used **Community Over Competition** for
  the first post since it matched the theme better than a generic search.
- **X**: short version, but X's free-tier limit is **280 characters**, not
  Threads' ~500 — the long-form draft (387 chars) triggered the
  "Upgrade to Premium to write longer posts" block and had to be trimmed to
  268 chars. Always check length before posting to X specifically; don't
  assume the Threads-length version fits.
- **TikTok (Photo Mode)**: short version + hashtags, **with a sound track**
  (see gotcha below) — this is now standard for all TikTok posts going
  forward, not just this recurring post.

## Gotchas (found 2026-09-22, first post)

- **TikTok sound is addable and automatable.** "Add sound" opens a
  searchable library (`Royalty-free sounds` in the sidebar has the same
  catalog) with real tracks and a one-click "Use" button. Search by mood/
  genre (e.g. "chill lofi" for product content, "inspiring cinematic" for
  movement content) and pick a result — fully scriptable, no native picker
  involved. **Apply this to every TikTok post from now on**, not just this
  recurring one.
- **Instagram Stories has no Music sticker in Meta Business Suite's web
  composer** — only Link, Mention, and emoji stickers are available
  (checked the full "More stickers" list, confirmed no scroll-hidden Music
  option). Instagram's real Music sticker is native-mobile-app-only; there
  is no workaround from Business Suite's web composer.
- **TikTok's description field: appending text via `key: End` after the
  cursor click does NOT reliably move to the true end of a multi-line
  field** — it moved to the end of the visual line the cursor happened to
  be on, and hashtags typed after got inserted mid-sentence instead of
  appended. Fix: don't try to append after the fact — type title, then
  clear+retype the full description INCLUDING hashtags in one single
  `type()` call, and verify via `innerText` readback before posting.
- **X's composer sometimes doesn't receive the first `type()` call after
  page load** (same intermittent issue documented in `X-POSTS.md`) — a
  second attempt via fresh `find` + click always worked.

## Status

| Week of | Angle | Platforms | Notes |
|---|---|---|---|
| 2026-09-22 | "Support in Passing" — the affiliate-link mechanism as low-effort support, contrasted with take-only businesses, tied to Vonguul's stated plan/resources need, softened toward belief-affirming language, closes with a comment/DM invite for missing products | Instagram feed, Threads, X, TikTok (with sound: "Epic Cinematic Inspirational" by Alex Chernykh) | First post of this recurring series. All 4 confirmed live. Went through 3 rounds of tone editing with the user before lock-in (see tone calibration note above) — this history matters for future variants, don't re-litigate from scratch. |

## How to apply for the next week's post

1. Ask the user how they want to proceed for that week's post (new angle,
   same wording, highlight something specific).
2. Draft copy per platform (mind the X 280-char limit specifically).
3. Build/reuse a `support-card.html` render if the visual needs to change;
   reuse the existing card if not.
4. Post: Instagram feed → Threads (set a topic tag) → X (verify char count)
   → TikTok (with sound).
5. Update this table, commit/push.
