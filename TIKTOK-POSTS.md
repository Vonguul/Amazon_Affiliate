# Vonguul Picks — TikTok Tracker

Account: **@offbahrvonguul** on TikTok (the existing "Vonguul Movement" personal-brand
account: bio "Anomaly by birth, Vonguulian by choice... Support the Movement", link
`vonguul.com`, ~1382 followers before this batch). Same account is shared with
Vonguul Clarity, matching the precedent already set for Instagram/Threads/X.

## Format: Photo Mode, not video

TikTok's "Photos" upload tab (`tiktokstudio/upload?tab=photo`) accepts a static
image post instead of video — same 1200x750 canvas cards already built for the
Instagram feed pipeline (see `INSTAGRAM-POSTS.md` for the render process),
uploaded as-is via TikTok's own file input. No video/audio production needed.

Each post has a **Title** (max 90 chars, short and punchy — this is TikTok's
own "catchy title" field, separate from the caption) and a **Description**
(the caption, max 4000 chars) with inline hashtags. Posting mode: "Now" /
"Everyone" visibility.

**Link-in-bio only** — same constraint as Instagram, TikTok captions can't
carry a working link. Bio points to `vonguul.com`.

**Gotcha (2026-09-22): TikTok's own content moderation holds every first-time
post as "Content under review" with visibility silently downgraded to "Only
me", even though "Everyone" was selected at posting.** Not an error on the
posting side — every post in this batch cleared review and flipped to
"Everyone" within a few minutes on its own. No action needed; just don't be
alarmed if a freshly-posted TikTok photo shows "Only me" immediately after
posting.

**Gotcha (2026-09-22): title/description fields sometimes don't take the
first `type()` call right after a photo finishes uploading** (silently stays
at 0/90, 0/4000, as if nothing landed) — happened intermittently, roughly
every other post. Fix: re-run `find` for the field and retry the click+type;
the second attempt always worked. Always screenshot after typing to confirm
the field actually shows the new character count before moving to the next
field or clicking Post.

## Status

| Article | Title | Posted |
|---|---|---|
| baking-supplies-bakeware-organization-ideas.md | "The Baking Cabinet Organizer Nobody Tells You to Buy" | posted 2026-09-22 |
| car-trunk-organization-ideas.md (2nd post, tire inflator angle) | "A Tire Inflator That Lives in Your Trunk for Emergencies" | posted 2026-09-22 |
| spice-rack-organization-ideas.md (2nd post, uniform jars angle) | "Why Matching Spice Jars Actually Save You Time" | posted 2026-09-22 |
| winter-gear-storage-ideas.md | "Wet boots by the door are still wet in the morning. Fix that." (sound: "Floating Dreams (Lofi)") | posted 2026-10-05, confirmed "Everyone" |

First 3 TikTok Photo Mode posts for Picks. 34 articles remain uncovered on
this platform (same backlog size as Threads' first-batch note, since TikTok
started at zero same as Threads did).

## How to apply for new articles

1. Reuse an existing rendered `ig-card-*.png` from the scratchpad if one
   already exists for the article (same visual works for both platforms);
   otherwise render a new one via `canvas-card.html` following the
   `INSTAGRAM-POSTS.md` process.
2. Navigate to `tiktokstudio/upload?tab=photo`, upload via the file input.
3. Fill Title (punchy, <90 chars) and Description (caption + 4-5 hashtags).
   Verify both landed via screenshot before proceeding (see gotcha above).
4. Leave "Now" / "Everyone" selected, click Post.
5. Expect "Content under review" / "Only me" immediately after — this
   self-resolves, don't attempt to fix it.
6. Update this table, commit/push.

## Repost round 2026-10-16 (articles already on Instagram, first time on TikTok)

User asked for "as many reposts as you can with the remaining limit available". Every article
already posted to Instagram but never to TikTok got a new vertical card (1080x1350, 3 products,
rendered with PIL; Picks charcoal/amber, Clarity indigo/gold) and a Photo Mode post. Sounds:
Picks "Lofi Chill" (Alberto Lofi), Clarity "Ambient-style emotional piano" (MoppySound).
Captions end "Full guide on the Vonguul Picks site, link in bio." plus 5 hashtags.
No prices anywhere.

**Limit hit:** after 60 posts in about an hour across both sites, TikTok returned
"Too many uploading attempts. Try again later." That is the TikTok upload cap for the day.
All 60 showed visibility "Everyone" in TikTok Studio at the end of the round.

**Gotchas:** the "Schedule" option asks to "Allow your video to be saved for scheduled posting"
(a consent prompt) so it was not used. Clicking Post then navigating in the same browser batch
sometimes drops the batch; split post and next-upload into separate batches. The viewport
height changed mid-run, which moved the Post button (779px tall: y=740; 737px: y=698).

| Article | Title | Status |
|---|---|---|
| indoor-growing-systems-guide.md | "Want to grow food indoors? Start with how much you actually want to grow" | posted 2026-10-16 |
| iphone-15-pro-max-cases.md | "iPhone 15 Pro Max cases, sorted by how you actually use your phone" | posted 2026-10-16 |
| gift-ideas-for-people-who-love-organizing.md | "Gifts for the person who loves an organized home" | posted 2026-10-16 |
| holiday-seasonal-decor-storage-ideas.md | "Stop storing ornaments in a garbage bag" | posted 2026-10-16 |
| small-pantry-organization-ideas.md | "12 small pantry ideas that fit a tiny kitchen" | posted 2026-10-16 |
| small-bedroom-closet-organization-ideas.md | "Small closet? You don't need a renovation" | posted 2026-10-16 |
| small-bathroom-storage-ideas.md | "Small bathroom storage with zero drilling into tile" | posted 2026-10-16 |
| kitchen-counter-organization-ideas.md | "Get your kitchen counter back" | posted 2026-10-16 |
| entryway-organization-ideas.md | "The chaos right inside your front door, fixed" | posted 2026-10-16 |
| garage-organization-ideas.md | "Your garage has walls and a ceiling. Use them." | posted 2026-10-16 |
| home-office-organization-ideas.md | "7 fixes for a desk that actually works" | posted 2026-10-16 |
| laundry-room-organization-ideas.md | "Cut the weekly laundry time down" | posted 2026-10-16 |
| kids-toy-room-organization-ideas.md | "Toy storage a kid can actually use on their own" | posted 2026-10-16 |
| linen-closet-organization-ideas.md | "Sheets, towels and the off-season pile" | posted 2026-10-16 |
| under-sink-organization-ideas.md | "Under-sink organizers that fit around the pipes" | posted 2026-10-16 |
| craft-room-organization-ideas.md | "Craft supplies that actually have a home" | posted 2026-10-16 |
| dorm-room-organization-ideas.md | "Dorm organization for a room you move out of every year" | posted 2026-10-16 |
| nursery-organization-ideas.md | "Nursery storage for clothes they outgrow every few months" | posted 2026-10-16 |
| home-gym-organization-ideas.md | "A home gym that doubles as a living room" | posted 2026-10-16 |
| jewelry-organization-ideas.md | "When all your jewelry is in one tangled bowl" | posted 2026-10-16 |
| food-storage-container-organization-ideas.md | "The container cabinet everyone dreads opening" | posted 2026-10-16 |
| cleaning-supplies-closet-organization-ideas.md | "The cleaning closet that's just a pile" | posted 2026-10-16 |
| under-bed-storage-organization-ideas.md | "The space under your bed is wasted storage" | posted 2026-10-16 |
| sock-drawer-organization-ideas.md | "The drawer that's just a pile" | posted 2026-10-16 |
| cord-cable-management-ideas.md | "Cable management that actually stays neat" | posted 2026-10-16 |
| junk-drawer-organization-ideas.md | "A junk drawer fix that doesn't just move the mess" | posted 2026-10-16 |
| wine-bar-cart-organization-ideas.md | "Your bar cart is wasting its top shelf" | posted 2026-10-16 |
| shoe-storage-organization-ideas.md | "Shoe storage when there's no entryway bench" | posted 2026-10-16 |
| coffee-bar-station-organization-ideas.md | "A coffee station sized for a counter, not a cafe" | posted 2026-10-16 |
| freezer-organization-ideas.md | "Your freezer is a deep, cold junk drawer" | posted 2026-10-16 |
| board-game-puzzle-storage-ideas.md | "Storage for a shelf full of board games" | posted 2026-10-16 |
| recycling-trash-bin-organization-ideas.md | "A kitchen that actually sorts its trash" | posted 2026-10-16 |
| water-bottle-tumbler-organization-ideas.md | "The water bottle cabinet that won't close" | posted 2026-10-16 |
| bookshelf-home-library-organization-ideas.md | "Organizing a book collection that keeps growing" | posted 2026-10-16 |
| refrigerator-organization-ideas.md | "The fridge shelf that's always a mess" | posted 2026-10-16 |
| makeup-vanity-organization-ideas.md | "The vanity counter that's always cluttered" | posted 2026-10-16 |
| pet-supplies-organization-ideas.md | "Pet gear taking over the house?" | posted 2026-10-16 |
| digital-privacy-security-essentials.md | "Privacy tools that actually protect you" | posted 2026-10-16 |

## Daily round 2026-10-18 (new high-ticket guides, first time on TikTok)

Vertical 1080x1350 cards from `tools/social/render_card.py`, sound "Lofi Chill" (Alberto Lofi).
All showed "Everyone" in TikTok Studio's content list after the round.

| Article | Title | Status |
|---|---|---|
| home-espresso-machine-and-gear-guide.md | "The grinder matters as much as the espresso machine" | posted 2026-10-18 |
| robot-vacuum-buying-guide.md | "Pick a robot vacuum by your floors, not the hype" | posted 2026-10-18 |
| home-office-upgrade-chair-desk-guide.md | "Home office upgrades: chair first, then the rest" | posted 2026-10-18 |

Every Picks article now has at least one TikTok.

## Daily round 2026-10-20 (repeats, oldest TikTok first)

Vertical cards from `tools/social/render_card.py`, sound "Lofi Chill" (Alberto Lofi), Now / Everyone.
Both listed once in TikTok Studio's content list as "Everyone". The baking post replaced a stale
unsaved photo draft left in Studio from an earlier session (an old baking card with no caption).
Clarity's 3 posts from this round are in `../vonguul-clarity/TIKTOK-POSTS.md`.

| Article | Title | Status |
|---|---|---|
| baking-supplies-bakeware-organization-ideas.md | "Baking pans should stand, not stack" | posted 2026-10-20 |
| car-trunk-organization-ideas.md | "Your trunk holds three different kinds of stuff" | posted 2026-10-20 |

## Daily round 2026-10-21 (new 2026-10-20 guides, first time on TikTok)

Vertical cards from `tools/social/render_card.py`, sound "Lofi Chill" (Alberto Lofi), Now / Everyone.
All listed once in TikTok Studio's content list (holiday hosting still "Content under review" at
check time, which clears by itself). Clarity's 2 posts from this round are in
`../vonguul-clarity/TIKTOK-POSTS.md`.

| Article | Title | Status |
|---|---|---|
| air-purifiers-by-room-size.md | "Air purifier boxes overstate room size. Divide by 5." | posted 2026-10-21 |
| humidifiers-by-room-size.md | "Measure your humidity before you buy a humidifier" | posted 2026-10-21 |
| holiday-hosting-seating-serving-storage.md | "Holiday hosting gear that folds away for the other 11 months" | posted 2026-10-21 |

Still never on TikTok: guest-room-ready-for-holiday-visitors, holiday-baking-setup-mixer-tools-storage.
