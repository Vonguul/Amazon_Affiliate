# Vonguul Picks/Clarity — X Community Replies Tracker

Account: **@OffbahrV** — same real account as `X-POSTS.md`'s original posts,
now also used to reply into other people's threads (not just post original
content). Distinct from `X-POSTS.md`, which only tracks posts made BY this
account.

## House rule: same 9:1 discipline as Reddit

This is the Reddit approach (`REDDIT-POSTS.md`) applied to X, not a separate
process. Search for genuine, real, recent conversations; reply helpfully
first; a link goes in only when it's a real match for what was actually
asked or said — never the same canned copy reused, never dropped into a
thread just because it's topically adjacent. Threads get skipped, not
forced, when nothing in Picks/Clarity actually fits.

**Explicitly rejected 2026-09-29:** searching many threads and dropping a
product link in every comment. That's the mechanical version of this the 9:1
rule exists to avoid — it's also close to what X's own spam policy exists to
catch (repetitive self-promotional replies across many threads), which is a
real risk to an account this doesn't have room to take (2 followers as of
this session — see `vonguul-analytics-baseline` memory).

## Reality check on X vs. Reddit for this

X's search surface is much sparser and noisier than Reddit's for finding
genuine "someone is asking for a recommendation" moments — no subreddit-style
structure where that's the expected content type. Across ~12 varied search
queries this session (organization/home for Picks; Human Design, tarot,
numerology for Clarity), the overwhelming majority of results were: years-old
dead threads (2016-2023, replying now would be necroposting), fan-culture
noise (celebrities/characters holding tarot decks, K-pop chart readings),
unrelated brand/business accounts, or metaphorical language ("my closet"
meaning something spiritual). Only 3 genuine matches surfaced. Budget for a
low hit rate — this is a "check back periodically" channel, not a
high-volume one like Reddit's subreddits.

## Tracking ID

`?src=x` (mapped to `vgpickx-20` / `vgclarityx-20` in each site's
`BaseLayout.astro` `TAG_MAP` — see [[vonguul-affiliate-tracking-ids]]),
appended by hand on every linked reply.

## Activity log (2026-09-29 session)

| Thread (OP) | Context | Reply type | Link used? |
|---|---|---|---|
| [@ChildOfSophia92](https://x.com/ChildOfSophia92/status/2101462601909604797) — "I have this in my human design chart. Not sure what it all means yet but I'm curious." (Sep 19) | Genuine curiosity, real person, no promo angle | 2 replies (own reply chain) | **Yes** — `human-design-101-free-chart` (Clarity), then a follow-up reply mentioning The Alignment Zone app (`vonguul.com/app`) |
| [@littleredrosies](https://x.com/littleredrosies/status/2104364310424395981) — "I need to organize my little bookshelf" (Sep 27) | Confirmed genuine book collector (recent "GOT NEW BOOKS" post with real photos) | 1 reply, specific tip (slumping books/bookends) + link | **Yes** — `bookshelf-home-library-organization-ideas` (Picks) |
| [@suziesdime](https://x.com/suziesdime/status/2103949063955657112) — "got my first tarot deck if anyone has any tips" (Sep 26) | Explicit ask for tips, 8 existing replies read first to avoid repeating advice (daily 1-card pull wasn't already suggested — Pinterest, an app, and the deck's own booklet were) | 1 reply, specific practice tip + link | **Yes** — `tarot-for-beginners` (Clarity) |

All 3 were genuine fits for what was actually asked/said, not forced. No
threads were skipped-with-no-reply this session — the ~9 other candidates
found via search were rejected before drafting anything (too old, wrong
context, or not actually a question) rather than replied-to without a link,
so this session doesn't have a clean 9:1 sample yet — that ratio holds over
time, same as Reddit's did.

## Gotchas (found 2026-09-29)

- **X reply boxes need explicit focus verification before typing** — a click
  that looks right can land on the wrong element (once landed on the "Home
  timeline" div, once triggered the keyboard-shortcuts page instead of
  typing). Check `document.activeElement`'s `data-testid` is
  `tweetTextarea_0` before typing; if not, re-click and re-check.
- **Free-tier 280 char limit applies to replies too**, and t.co shortens any
  link to ~23 chars regardless of real length — budget for that, not the
  raw URL length. A two-part genuine tip + link easily runs over; trim the
  prose, not the link.
- **Splitting a longer thought into two sequential replies** (reply to the
  OP, then reply to your own reply) reads naturally on X and avoids
  cramming multiple links into one message — used for the Human Design
  app mention.
