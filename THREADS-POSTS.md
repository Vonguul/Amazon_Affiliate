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

First 3 Threads posts for Picks. 34 articles remain uncovered on this
platform.
