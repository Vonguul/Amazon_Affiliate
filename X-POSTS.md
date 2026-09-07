# Vonguul Picks — X (Twitter) Tracker

Account: **@OffbahrV** on X — same real personal account as Threads' @offbahr.
Bio is tied to a separate "Community USA Vonguul" movement project; by
decision (2026-09-08), Picks/Clarity content on X ignores that framing and
matches the Threads voice instead: first-person, skeptical-but-engaged,
direct — not neutral marketing copy, not the movement/reciprocity framing.

## Tracking ID status

X does not yet have a dedicated Amazon Associates tracking ID. Attempted to
register `vgpicksx-20` (and `vgclarityx-20` for Clarity) on 2026-09-08 via
Associates Central — failed 3x with "Error occurred while creating tracking
id. Please try again later." (server-side error, not a validation issue).
Stopped retrying to avoid hammering the endpoint. Until this is resolved,
links posted to X use each site's **default** tag (`vonguul-20` /
`vgclarity-20`, no `?src=` param) rather than a channel-specific one.

**Once the tracking ID exists:** add `x: 'vgpicksx-20'` to `TAG_MAP` in
`src/layouts/BaseLayout.astro` (mirrors the pinterest/reddit/instagram
entries already there), update this file, and use `?src=x` on all links in
new posts going forward. Already-posted links keep their default tag —
same precedent as PIN-BATCH-04 being left untouched after the Pinterest tag
fix, since a live post's link can't be retroactively retagged.

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
