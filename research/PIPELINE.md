# Content pipeline (both sites)

One list of article topics from idea to live, so there is always researched material waiting for the
owner's approval. The daily routine reads this file at the end of every run (see "Content pipeline"
in `tools/social/DAILY-ROUTINE.md`) and researches a new topic whenever a site has fewer than 3
topics in `researched`.

Statuses: `idea` -> `researched` (findings written, waiting for the owner) -> `approved` -> `live`.
`hold` = researched but failed the quality bar; recheck after the date given.
Only the owner moves a topic to `approved`; the routine never builds or publishes articles.

## Researched, waiting for the owner's approval

| Topic | Site | Researched | Findings | Note |
|---|---|---|---|---|

## Approved and built, waiting for a publish date

Built on a draft branch (pushed to GitHub as backup, NOT on main). On the date: rebase the branch on
main, set `pubDate` to that day, build, push the branch to main, verify the live page, delete the
branch, and move the row to Live. Only these two rows are approved for publishing on their dates.

| Topic | Site | Branch | Publish on |
|---|---|---|---|
| New-year reset: label maker, closet system, clear bins | Picks | vonguul-picks `draft/approved-2026-10-30` (new-year-reset-label-maker-closet-system-bins) | 2026-12-20 |
| Imbolc for beginners | Clarity | vonguul-clarity `draft/approved-2026-10-30` (imbolc-for-beginners-brigids-day) | 2027-01-04 |

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
| Jung and archetypes for beginners (Man and His Symbols etc.) | Clarity | evergreen |
| Paper and document organization (tax season) | Picks | Jan to Mar |
| Crystal storage and display | Clarity | evergreen |
| Spring cleaning tools (steam mop, carpet cleaner, caddies) | Picks | Feb to Mar |
| Ostara / spring equinox | Clarity | publish by early Mar |
| Patio and garden storage | Picks | Mar to Apr |
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
