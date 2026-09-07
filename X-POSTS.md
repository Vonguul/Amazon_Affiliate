# Vonguul Picks — X (Twitter) Tracker

Account: **@OffbahrV** on X — same real personal account as Threads' @offbahr.
Bio is tied to a separate "Community USA Vonguul" movement project; by
decision (2026-09-08), Picks/Clarity content on X ignores that framing and
matches the Threads voice instead: first-person, skeptical-but-engaged,
direct — not neutral marketing copy, not the movement/reciprocity framing.

## Tracking ID status

X does not have a dedicated Amazon Associates tracking ID, and per decision
(2026-09-08) it isn't getting one for now — registering `vgpicksx-20` via
Associates Central failed 5+ times across two sessions with "Error occurred
while creating tracking id. Please try again later." (consistent server-side
error, not a validation issue). Rather than keep retrying, links posted to
X use each site's **default** tag (`vonguul-20` for Picks, no `?src=` param)
going forward, indefinitely — this is the settled approach, not a temporary
placeholder.

**If a tracking ID ever does get created** (e.g. the user registers it
manually on Amazon's side and asks to wire it up): add `x: 'vgpicksx-20'` to
`TAG_MAP` in `src/layouts/BaseLayout.astro` (mirrors the pinterest/reddit/
instagram entries already there), update this file, and use `?src=x` on
links in new posts from that point on. Don't attempt this unprompted — the
user closed this out; only revisit if they raise it again.

## Format

Same mix as Threads: mostly **opinion posts** (first-person take on a real
mechanism from the article, no link) with occasional **linked posts** (ties
a specific claim/product to the article URL). Always draft and show for
review before posting — real account, real followers, no undo on X.

## Status

| Article | Type | Posted |
|---|---|---|
| refrigerator-organization-ideas.md | opinion | posted 2026-09-08 |
| pet-supplies-organization-ideas.md | linked | posted 2026-09-08 |
