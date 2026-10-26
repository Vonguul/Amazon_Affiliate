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
| Thanksgiving prep (roaster, thermometers, carving, gravy) | Picks | 2026-10-26 | research/RESEARCH-QUEUE-E-PICKS-2026-10-26.md (7a) | publish by early Nov |
| Winter car and driveway (brush, cover, shovel, ice melt) | Picks | 2026-10-26 | same (7b) | publish early Nov |
| Air fryers by household size | Picks | 2026-10-26 | same (7d) | evergreen |
| 2027 astrology and moon planners and calendars | Clarity | 2026-10-26 | ../vonguul-clarity/research/RESEARCH-QUEUE-E-CLARITY-2026-10-26.md (8a) | publish by mid-Nov |
| Incense for beginners | Clarity | 2026-10-26 | same (8b) | evergreen |

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
| Stocking stuffers that organize (small gifts, no prices) | Picks | Nov to mid-Dec |
| Imbolc (Llewellyn Sabbat Essentials + candles), next Wheel of the Year festival | Clarity | publish by mid-Jan |
| New-year reset: label makers, drawer systems, closet systems | Picks | late Dec to Jan |
| Dream interpretation books and dream journals | Clarity | evergreen |
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
