# Research queue B (started 2026-10-20): spin-offs from live articles

Owner asked for research on spin-off products and related branches (no building). Same rules as
queue A: verify on live Amazon pages, no prices in articles, in stock, rating about 4.3 or better
with a real review count, ASIN not already used on either site, honest caveats, Clarity gets
"Worth being direct about". Stop for owner approval before building.

Method: built-in browser (mcp__Claude_Browser__*), navigate to https://www.amazon.com/robots.txt,
then fetch('/s?k=...') and fetch('/dp/ASIN') from page JS and parse with DOMParser.

| # | Topic | Spins off | Site | Status | Output |
|---|---|---|---|---|---|
| 1a | Humidifiers by room size (winter) | air-purifiers-by-room-size | Picks | done | research/RESEARCH-SPINOFFS-2026-10-20.md |
| 1b | Cordless stick vacuums (high-ticket) | robot-vacuum-buying-guide | Picks | done | same |
| 1c | Holiday baking upgrades (stand mixer etc.) | baking-supplies, holiday-hosting | Picks | done | same |
| 1d | Bedding: verify topper, sheets, comforter | guest-room, linen-closet | Picks | done | same |
| 2a | Altar setup (cloth, candle holders, offering bowls, small table) | scrying, candle-magic | Clarity | done | ../vonguul-clarity/research/RESEARCH-SPINOFFS-CLARITY-2026-10-20.md |
| 2b | Yule / winter solstice | moon-phases, candle-magic | Clarity | done | same |
| 2c | Tea leaf reading (tasseography) | scrying | Clarity | done | same |

## Progress log
- 2026-10-20: queue created.
- 2026-10-20 evening: rows 1a-1d done (humidifiers BUILD, stick vacuums HOLD, baking BUILD, bedding ADD to guest room).
- 2026-10-20 evening: rows 2a-2c done (altar MERGE into Yule, Wheel of the Year/Yule BUILD, tea leaf reading BUILD). All rows done; waiting for owner approval on builds.
