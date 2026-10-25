# Picks video backgrounds (AI-generated)

Room scenes used behind the real product photos in Picks motion videos (`render_motion.py --bg auto`).
They are AI-generated, so any post that uses one must carry the platform's AI label (TikTok
"AI-generated content", Pinterest "Mark as AI-modified"). Product photos are never AI.

| File | Scene | Used for slugs containing |
|---|---|---|
| `picks/kitchen.jpg` | Bright kitchen, empty counter | kitchen, pantry, spice, coffee, baking, fridge, freezer, knives, cookware... |
| `picks/closet.jpg` | Tidy bedroom closet | closet, bedroom, shoe, sock, jewelry, makeup, under-bed, linen, guest-room, dorm, nursery |
| `picks/entryway.jpg` | Entryway with bench | entryway, winter-gear, garage, car, pet, laundry, recycling, cleaning, travel |
| `picks/home-office.jpg` | Home office, clear desk | office, desk, cord, cable, bookshelf, craft, digital, iphone, board-game, junk-drawer |
| `picks/winter-living-room.jpg` | Cozy winter living room | humidifier, purifier, heater, holiday, gift, hosting, robot-vacuum, living/game room, home-gym, bathroom |

The keyword list lives in `BG_TOPICS` in `render_motion.py`. A slug that matches nothing falls back to
the blurred product photo (no AI, no label needed).

## Adding scenes

Generated 2026-10-25 with Canva's AI image generator (prompts: photorealistic, vertical 9:16, softly
blurred room, empty centre, no people/text/logos/products). Canva only exports full-size files from a
saved design, and saving needs the owner's approval, so new scenes are added in a session with the
owner present, not by the unattended daily routine. Library design in Canva: "Vonguul Picks
backgrounds (AI)" (DAHZC74lYjU): add a page per scene, export as JPG 1080x1920, save here, add the
keywords to `BG_TOPICS`. The 2026-10-25 holiday-table scene failed on Canva's credit limit; add it
next refresh.
