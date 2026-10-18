# Daily social routine (Threads + Instagram Stories)

Runs every day at 10:00 AM as the scheduled task `vonguul-daily-social`. Owner: offbahr@vonguul.com.
Sites: Vonguul Picks (`C:\Users\laker\Downloads\vonguul-picks`, https://vonguul-picks.vercel.app)
and Vonguul Clarity (`C:\Users\laker\Downloads\vonguul-clarity`, https://vonguulian-clarity.vercel.app).
Browser: Claude in Chrome (the user's Chrome, already signed in to Threads, Instagram and Meta
Business Suite). Work in a new tab and close it at the end.

## Daily quota

1. **Threads: up to 8 posts.** First the backlog of articles that have never had a Threads post
   (see "Still never on Threads" in `vonguul-picks/THREADS-POSTS.md`, plus any article in either
   `src/content/articles/` folder that is not in either THREADS-POSTS.md). Once the backlog is
   empty, drop to 4 a day and post a fresh angle for the articles whose most recent thread is
   oldest. Never post the same text twice.
2. **Instagram Stories: up to 6.** First articles that have never had a Story (lists at the end of
   both `INSTAGRAM-STORIES.md` files). Once empty, keep 5 a day cycling through all articles,
   oldest Story first. Stories expire after 24 hours, so this keeps something live every day.
3. Alternate Picks and Clarity where both have backlog. Skip any article marked `unlisted: true`.
4. The quota is per calendar day. Before posting, count rows already logged with today's date in
   the four trackers and post only the remainder, so a manual "Run now" plus the 10:00 run never
   doubles a day.

## Content rules (non-negotiable)

- Read the article body before writing. Every claim in a post must be in the article. Do not
  invent product features, counts or results.
- No prices or dollar amounts anywhere.
- Clarity: never present tarot, astrology, crystals, Human Design, etc. as proven. Frame them as
  tools for reflection, matching the article's "Worth being direct about" section. No health claims.
- Voice on Threads: first person, lowercase, casual, one concrete tip from the article, under
  400 characters, ending with the link. Example:
  `small pantry tip: the back of every shelf is dead space until you can see into it. a turntable and clear bins with handles do more than buying another set of matching containers. 12 picks for tight kitchens and awkward cabinets: <link>`
- Links: Picks Threads `?src=threads`; Clarity Threads `?src=instagram`; every Story link
  sticker `?src=instagram`. Format: `https://<site>/articles/<slug>/?src=...`
- Do not post Support Vonguul posts, replies, DMs or anything else. Those need the user's approval.

## Threads procedure (https://www.threads.com/)

1. Confirm the signed-in account is @offbahr (the "Profile" link points to `/@offbahr`). Stop if not.
2. Click the "What's new?" composer at the top of the feed (about x=680, y=87 at a 1568x779
   viewport). In a separate call, confirm `document.activeElement.getAttribute('aria-label')` is
   "Empty text field. Type to compose a new post." before typing. Never type in the same batch as
   the previous Post click: keystrokes can land on the feed and open a "Save to drafts?" prompt.
   If that prompt appears, choose Cancel, select all the composer text and retype it.
3. Type the post, wait 3 s for the link preview.
4. `find` "Community or topic add button in New thread dialog", click it, type the topic
   (`organization` for Picks; a fitting one for Clarity, e.g. Spirituality, Tarot, Astrology,
   Psychology, Meditation), then `find` the option with exactly that name and click it.
5. Zoom on the composer to check text + topic, `find` "Post button inside the New thread dialog",
   click it, wait 8 s.
6. After the round, open https://www.threads.com/@offbahr, scroll, and confirm each new post
   appears exactly once (the list is virtualized; check by scrolling and screenshots).

## Instagram Stories procedure (Meta Business Suite)

Instagram's website cannot create Stories; use Business Suite.

1. Render the card: `python C:\Users\laker\Downloads\vonguul-picks\tools\social\render_card.py <picks|clarity> <slug> "<headline>" <scratchpad>\<slug>.png`.
   Headline: a short hook based on the article (under 70 characters). `file_upload` only reads
   files in the session's scratchpad, so write the PNG there.
2. Open `https://business.facebook.com/latest/story_composer/?asset_id=109580998478548&business_id=123462012162006`.
3. Share to: click the dropdown (600,105). It defaults to BOTH `offbar1` (Facebook Page) and
   `offbahr`. Click `offbar1` (410,168) to uncheck it, zoom to confirm only `offbahr` is checked,
   click empty space (1100,500) to close.
4. Before clicking "Add photo/video", run this in the page so no native file dialog opens:
   `if(!window.__patched){const o=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'){if(!this.isConnected){document.body.appendChild(this)}return}return o.call(this)};window.__patched=true}`
   Then `find` and click "Add photo/video", `find` "file input element (type=file)", and
   `file_upload` the PNG to it. Wait 7 s.
5. Edit (715,214) → More stickers (393,347) → Link sticker (628,213) → click the link field
   (620,358) and type the URL → click the sticker text field (610,428) and type the sticker text
   (25 characters max, e.g. "See full breakdown") → zoom to check both fields, and read the
   input values with JS to confirm the URL → Apply (727,468) → editor Apply (1198,605).
6. Zoom on "Share to" (still only `offbahr`), then Share (1243,530). Business Suite moves to the
   Planner and shows "Your story is being published".
7. After the round, open https://www.instagram.com/stories/offbahr/ and count the progress
   segments to confirm the new Stories are live.

Coordinates are for a 1568x779 viewport. If the layout looks different, take a screenshot and
adjust instead of clicking blind.

## Logging

- Threads: add rows to the dated catch-up table in `vonguul-picks/THREADS-POSTS.md` or
  `vonguul-clarity/THREADS-POSTS.md` (article, type, topic, date) and update the "Still never on
  Threads" list.
- Stories: add rows to the newest dated table in each `INSTAGRAM-STORIES.md` (article, date,
  sticker text) and update the "Never had a Story yet" lists.
- In each repo: `git pull --rebase`, `git add` only the tracker files you changed, commit with a
  message ending in `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, push.

## Stop conditions

Stop posting (log what was done, report it) if: the wrong account is signed in; a platform shows
a limit or "try again later" message; a post fails to appear after a retry; or anything asks for
a password, consent, terms or payment. Never accept consent prompts (for example TikTok's
"Allow your video to be saved for scheduled posting").
