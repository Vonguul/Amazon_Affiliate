# Research queue D (2026-10-23): new product research for both sites

Owner asked to "research more new products to make articles for". Queues A, B and C are built and
live, so this queue picks new topics with no existing article. Research only: stop for owner
approval before building.

Same rules as queues A to C: verify on live Amazon pages, no prices in articles, in stock, rating
about 4.3 or better with a real review count, ASIN not already used on either site (checked
against 571), honest caveats, no health claims, Clarity gets "Worth being direct about".

Method: built-in browser, navigate to https://www.amazon.com/robots.txt, then fetch('/s?k=...')
and fetch('/dp/ASIN') from page JS and parse with DOMParser.

| # | Topic | Spins off | Site | Status | Output |
|---|---|---|---|---|---|
| 5a | Pots, pans and lids: storage plus a cookware upgrade | kitchen-counter, baking-supplies | Picks | done | research/RESEARCH-QUEUE-D-PICKS-2026-10-23.md |
| 5b | Kitchen knives and knife storage | kitchen-counter | Picks | done | same |
| 5c | Holiday travel: luggage and packing | guest-room, jewelry-organization | Picks | done | same |
| 6a | Chakras for beginners | meditation, reiki, crystals | Clarity | done | ../vonguul-clarity/research/RESEARCH-QUEUE-D-CLARITY-2026-10-23.md |
| 6b | The Enneagram for beginners | human-design-101, recognizing-manipulation | Clarity | done | same |
| 6c | Yoga gear for a sitting practice | meditation | Clarity | done | same |

## Progress log
- 2026-10-23: queue created and all rows researched. All six recommended BUILD (6c could be a
  meditation section instead). Waiting for owner approval on builds.
- 2026-10-23: owner approved all six. Built on branch `draft/queue-d-2026-10-23` in both repos:
  Picks pots-and-pans-organization-and-cookware-guide (12 products),
  kitchen-knives-and-knife-storage-guide (10), holiday-travel-packing-luggage-guide (11, new
  category "Travel & Packing"); Clarity chakras-for-beginners (4, new category "Chakras"),
  enneagram-for-beginners (4, new category "Enneagram"), yoga-gear-for-meditation-practice (8,
  category "Meditation"). Dropped at build: Tramontina Sicilia, McCook set, Bellemain block,
  chakra stones (healing claims). Added at build: McGeough "A Beginner's Guide to the Chakras".
