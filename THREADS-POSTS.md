# Vonguul Picks — Threads Tracker

Account: **@offbahr** on Threads — same real personal account used for Vonguul
Clarity's Threads presence (see `../vonguul-clarity/THREADS-POSTS.md` for the
full process notes: composing, Community/topic field, posting quirks). Picks
had no Threads coverage before 2026-09-22; this file starts that coverage.

## Tracking ID

**Fixed 2026-09-24.** `vgpickthreads-20` is now a registered Amazon Associates
tracking ID, and `TAG_MAP` in `src/layouts/BaseLayout.astro` maps
`threads → vgpickthreads-20`. Every future **linked** Threads post must append
`?src=threads` to the article URL (e.g.
`https://vonguul-picks.vercel.app/articles/<slug>/?src=threads`) for the tag
swap to fire — opinion posts with no link don't need it.

Prior to this fix, linked posts used the site's default tag (`vonguul-20`, no
`?src=` param) since there was no `threads` entry in `TAG_MAP`. Per the
project's established pattern (tags aren't retroactively editable — see
[[pinterest-threads-tags-not-retroactively-editable]]), the one prior linked
post (`baking-supplies-bakeware-organization-ideas.md`, 2026-09-22) is left
as-is; this fix applies going forward only.

## Format

Same mix as X: mostly **opinion posts** (first-person take on a real
mechanism from the article, no link) with occasional **linked posts**. Always
compose and post in an interactive session — real account, real followers,
no undo. Set the "Community or topic" field to a relevant topic (e.g.
`organization`) on every post, same practice as Clarity's Threads posts.

## Status

| Article | Type | Posted |
|---|---|---|
| refrigerator-organization-ideas.md | opinion | posted 2026-09-22 |
| baking-supplies-bakeware-organization-ideas.md | linked | posted 2026-09-22 |
| spice-rack-organization-ideas.md | opinion | posted 2026-09-22 |
| gift-ideas-for-people-who-love-organizing.md | linked (`?src=threads`), topic "gift ideas" | posted 2026-09-30 |
| indoor-growing-systems-guide.md | linked (`?src=threads`), topic "gardening" | posted 2026-10-04 |
| iphone-15-pro-max-cases.md | linked (`?src=threads`), topic "iPhone" | posted 2026-10-04 |
| winter-gear-storage-ideas.md | linked (`?src=threads`), topic "organization" | posted 2026-10-05 |

First 3 Threads posts for Picks. 34 articles remain uncovered on this
platform.

## Catch-up batch 2026-10-17 (articles never posted to Threads)

All linked (`?src=threads`), one tip from the article plus the link. Verified once each on the
@offbahr profile. Spreading the rest over a few days rather than flooding the feed.

| Article | Type | Topic | Posted |
|---|---|---|---|
| holiday-seasonal-decor-storage-ideas.md | linked | Home Decor | 2026-10-17 |
| small-pantry-organization-ideas.md | linked | organization | 2026-10-17 |
| kitchen-counter-organization-ideas.md | linked | organization | 2026-10-17 |
| entryway-organization-ideas.md | linked | organization | 2026-10-17 |
| garage-organization-ideas.md | linked | organization | 2026-10-17 |
| home-office-organization-ideas.md | linked | organization | 2026-10-17 |
| small-bathroom-storage-ideas.md | linked | organization | 2026-10-17 |
| small-bedroom-closet-organization-ideas.md | linked | organization | 2026-10-17 |
| kids-toy-room-organization-ideas.md | linked | organization | 2026-10-17 |
| cord-cable-management-ideas.md | linked | organization | 2026-10-17 |

**Still never on Threads (24):** board-game, bookshelf, car-trunk, cleaning-supplies, coffee-bar,
craft-room, digital-privacy, dorm-room, food-storage, freezer, home-gym, jewelry, junk-drawer,
laundry, linen-closet, makeup-vanity, nursery, pet-supplies, recycling, shoe-storage, sock-drawer,
under-bed, under-sink, water-bottle, wine-bar-cart.

**Composer gotcha:** opening the composer and typing in the same browser batch as the previous
Post click can send keystrokes to the feed (triggers a "Save to drafts?" prompt and drops the
start of the text). Post, wait, then open the composer in a separate call and confirm the
focused element is "Empty text field" before typing. Pick topics via `find` for the exact option.
