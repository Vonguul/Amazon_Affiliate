# Content pipeline (both sites)

One list of article topics from idea to live, so there is always researched material waiting for the
owner's approval. The daily routine reads this file at the end of every run (see "Content pipeline"
in `tools/social/DAILY-ROUTINE.md`) and researches a new topic whenever a site has fewer than 3
topics in `researched`.

Statuses: `idea` -> `proposed` (topic and product slots written, the owner checks products on Amazon)
-> `researched` (products verified, waiting for the owner) -> `approved` -> `live`.
`hold` = researched but failed the quality bar; recheck after the date given.
Only the owner moves a topic to `approved`; the routine never builds or publishes articles.

## Researched, waiting for the owner's approval

| Topic | Site | Researched | Findings | Note |
|---|---|---|---|---|
| Beltane for beginners (4 products) | Clarity | 2026-11-03 | vonguul-clarity `research/RESEARCH-AUTO-2026-11-03-beltane-for-beginners.md` | BUILD by mid-April 2027 after adding a reputable fire-safety pick and one more item |

## Proposed, waiting for the owner's product check

Since 2026-11-04 the routine does not open amazon.com (Amazon blocks AI agents). It writes a proposal
with product slots and search terms; the owner checks the products on Amazon and fills the table, and
the topic then moves to "Researched".

| Topic | Site | Proposed | Proposal file |
|---|---|---|---|
| Winter power outage prep: lighting, power, one kit (9 slots) | Picks | 2026-11-05 | vonguul-picks `research/PROPOSAL-2026-11-05-winter-power-outage-prep.md` |
| Breathwork / pranayama for beginners (7 slots) | Clarity | 2026-11-05 | vonguul-clarity `research/PROPOSAL-2026-11-05-breathwork-pranayama-for-beginners.md` |
| Winter bedding: a warmer bed without heating the house (8 slots) | Picks | 2026-11-06 | vonguul-picks `research/PROPOSAL-2026-11-06-winter-bedding-warm-bed.md` |
| A small home altar or practice space (7 slots) | Clarity | 2026-11-06 | vonguul-clarity `research/PROPOSAL-2026-11-06-home-altar-practice-space.md` |

## Approved and built, waiting for a publish date

Built on a draft branch (pushed to GitHub as backup, NOT on main). On the date: rebase the branch on
main, set `pubDate` to that day, build, push the branch to main, verify the live page, delete the
branch, and move the row to Live. Only rows with a date are approved for publishing on that date.

| Topic | Site | Branch | Publish on |
|---|---|---|---|
| New-year reset: label maker, closet system, clear bins | Picks | vonguul-picks `draft/approved-2026-10-30` (new-year-reset-label-maker-closet-system-bins) | 2026-12-20 (scheduled task `vonguul-publish-new-year-reset`) |
| Imbolc for beginners | Clarity | vonguul-clarity `draft/approved-2026-10-30` (imbolc-for-beginners-brigids-day) | 2027-01-04 (scheduled task `vonguul-publish-imbolc`) |
| Paper and document organization | Picks | vonguul-picks `draft/paper-document-organization` (paper-document-organization-ideas) | 2027-01-04 (scheduled task `vonguul-publish-paper-organization`) |
| Patio and garden storage (8 products) | Picks | vonguul-picks `draft/patio-garden-storage` (patio-garden-storage-ideas) | 2027-03-01 (scheduled task `vonguul-publish-patio-storage`) |
| Ostara for beginners (5 products) | Clarity | vonguul-clarity `draft/ostara-spring-equinox` (ostara-for-beginners-spring-equinox) | 2027-03-01 (scheduled task `vonguul-publish-ostara`) |
| Spring cleaning tools | Picks | vonguul-picks `draft/spring-cleaning-tools` (spring-cleaning-tools-steam-mop-carpet-cleaner) | 2027-02-01 (scheduled task `vonguul-publish-spring-cleaning`) |

## Hold (recheck after the date)

| Topic | Site | Why held | Recheck after |
|---|---|---|---|
| Video doorbells and package boxes | Picks | only Ring Battery passes; boxes have thin reviews | 2026-11-15 |
| Cordless stick vacuums | Picks | brand sticks 4.0 to 4.2 or thin relistings | 2026-12-01 |
| Mattresses | Picks | tester picks not on Amazon or thin there | 2027-01-15 |
| Le Creuset Dutch oven (cookware add) | Picks | no Amazon-sold offer | 2026-11-15 |
| Samhain (Llewellyn Sabbat Essentials) | Clarity | Oct 31 too close | 2027-08-15 |

## Ideas (research in this order; add new ones as articles suggest them)

Seasonal first, then evergreen. Skip anything an existing article already covers (check both
`src/content/articles/` folders).

| Idea | Site | Best window |
|---|---|---|
| Camping and outdoor gear storage | Picks | Apr to Jun |

## Live

Built and published topics are in each repo's `src/content/articles/`; the research files in
`research/` hold their product evidence.

| Topic | Site | Live | Article |
|---|---|---|---|
| Thanksgiving prep | Picks | 2026-10-26 | thanksgiving-turkey-tools-roaster-thermometer |
| Winter car and driveway | Picks | 2026-10-26 | winter-car-driveway-snow-tools |
| Air fryers by household size | Picks | 2026-10-26 | air-fryers-by-household-size |
| 2027 astrology and moon planners | Clarity | 2026-10-26 | 2027-astrology-moon-planners-calendars |
| Incense for beginners | Clarity | 2026-10-26 | incense-for-beginners-sticks-cones-holders |
| Stocking stuffers that organize | Picks | 2026-10-30 | stocking-stuffers-that-organize |
| Dream interpretation books | Clarity | 2026-10-30 | dream-interpretation-books |
| Jung and archetypes for beginners | Clarity | 2026-10-30 | jung-archetypes-for-beginners |
| Crystal storage section | Clarity | 2026-11-02 | crystals-for-beginners |
| Coat closet organization | Picks | 2026-11-03 | coat-closet-organization-ideas |
