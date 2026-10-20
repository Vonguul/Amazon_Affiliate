# Research queue (started 2026-10-20)

Owner approved research in this order. Research only: verify on live Amazon pages, write the
findings file, then stop for owner approval before building any article. Same rules as before:
no prices in articles, in stock, rating about 4.3 or better with a real review count, ASIN not
already used on either site (`grep -rho 'asin: "[A-Z0-9]*"'` across both repos' articles),
honest caveats, Clarity gets "Worth being direct about".

Method: built-in browser (mcp__Claude_Browser__*), navigate to https://www.amazon.com/robots.txt,
then fetch('/s?k=...') and fetch('/dp/ASIN') from page JS and parse with DOMParser.

| # | Topic | Site | Status | Output |
|---|---|---|---|---|
| 1a | Gift-wrap station and storage (beyond the wrapping-paper organizer already in holiday-seasonal-decor-storage-ideas) | Picks | done | research/RESEARCH-HOLIDAY-2026-10-20.md |
| 1b | Holiday entertaining and hosting (extra seating, folding tables, beverage tubs, guest coat storage, serving organization) | Picks | done | same file |
| 1c | Guest room prep (air mattress or folding bed, luggage rack, guest bath and bedside basics) | Picks | done | same file |
| 2 | Scrying (obsidian mirrors, crystal or glass balls, stands, books) | Clarity | done | ../vonguul-clarity/research/RESEARCH-SCRYING-2026-10-20.md |
| 3a | Air purifiers by room size (RTINGS / CR picks) | Picks | todo | research/RESEARCH-HIGH-TICKET-2-2026-10-20.md |
| 3b | Mattresses and bedding (RTINGS / CR picks available on Amazon) | Picks | todo | same file |

When every row is done: tell the owner, with a recommended build list, and wait for approval.

## Progress log
- 2026-10-20 12:05 CDT: rows 1a-1c done, findings in research/RESEARCH-HOLIDAY-2026-10-20.md (21 products verified, 3 builds recommended).
- 2026-10-20 12:20 CDT: row 2 done, findings in ../vonguul-clarity/research/RESEARCH-SCRYING-2026-10-20.md (12 products verified, 1 article recommended).
