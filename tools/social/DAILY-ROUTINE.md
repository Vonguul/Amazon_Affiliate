# Daily social routine (Threads, Instagram Stories, Pinterest, TikTok)

Runs every day at 10:00 AM as the scheduled task `vonguul-daily-social`. Owner: offbahr@vonguul.com.
Sites: Vonguul Picks (`C:\Users\laker\Downloads\vonguul-picks`, https://vonguul-picks.vercel.app)
and Vonguul Clarity (`C:\Users\laker\Downloads\vonguul-clarity`, https://vonguulian-clarity.vercel.app).
Browser: Claude in Chrome (the user's Chrome, already signed in to Threads, Instagram and Meta
Business Suite). Work in a new tab and close it at the end.

**Shell: use the Bash tool only, never PowerShell.** The run's permission allow rules cover these
Bash forms: `python /c/Users/laker/Downloads/vonguul-picks/tools/social/render_motion.py ...` (and `render_card.py ...`),
`git -C /c/Users/laker/Downloads/vonguul-picks <pull/fetch/status/log/diff/add/commit/push ...>` (or `vonguul-clarity`),
`ls`, `grep`, `date`, and `tail`, `head`, `wc`, `sort` as pipe filters. Read files with the Read tool and change trackers with the Edit tool.
Anything else will stop the run on an approval prompt. **Never write `cd <repo> && git ...`**: a
cd followed by git always asks for approval, which stalled the 2026-10-23 run for six hours. Use
`git -C <repo>` and one git command per Bash call.

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
4. **Pinterest: up to 5 fresh pins** and **TikTok: up to 5 video posts** (added 2026-10-18; videos since 2026-10-25).
   Order for both: articles that have never had one first (new articles go first: check
   `src/content/articles/` in both repos for anything with no `PIN-BATCH-*.md` / no row in
   `TIKTOK-POSTS.md`), then articles whose most recent pin or TikTok is oldest. Alternate Picks
   and Clarity where both have backlog. Use a fresh angle (a different product or tip) for a
   repeat pin; never reuse the same title or text.
5. The quota is per calendar day. Before posting, count rows already logged with today's date in
   the trackers (Threads, Stories, Pinterest PIN-BATCH status lines, TikTok) and post only the remainder, so a manual "Run now" plus the 10:00 run never
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

## Videos (since 2026-10-25: Stories, TikTok and Pinterest use motion videos, not still cards)

The owner switched visuals from still cards to 9-second vertical videos. Render ONE video per
article per day and reuse it on every platform it goes to (each render takes about 75 s; give the
Bash call a 300000 ms timeout):

`python /c/Users/laker/Downloads/vonguul-picks/tools/social/render_motion.py <picks|clarity> <slug> "<headline>" <scratchpad>/<slug>.mp4 [--bg auto|none]`

It also writes `<slug>.png` (the last frame) next to the MP4. Write both into the session
scratchpad (`file_upload` only reads there). Headline: a short hook from the article, under 70
characters, no prices. Check the printed `background:` / `symbol:` line.

- **Clarity:** no `--bg`. A sacred-geometry or esoteric figure matched to the topic draws itself,
  then the real product photos rise in. It is computed geometry, not AI: no AI label. Format: `motion-geometry`.
- **Picks: two-week test (2026-10-25 to 2026-11-08), alternate the two looks** across the day's
  Picks videos: the first Picks video of the day `--bg auto`, the next `--bg none`, and so on.
  - `--bg auto` puts an AI-generated room scene behind the real products (`tools/social/backgrounds/`).
    Format `motion-ai`. **This post MUST carry the AI label** on TikTok and Pinterest (see those
    procedures). If the printed line says `background: none`, no scene matched: treat it as `motion-plain`.
  - `--bg none` uses a blurred real product photo. Format `motion-plain`. No label.
  - For Instagram Stories, always render Picks with `--bg none` unless Business Suite shows an
    "AI info"/AI label option you can switch on (Meta labeling is not verified in this workflow).
- Log the format with every TikTok row, Story row and PIN-BATCH file (see Logging), so the weekly
  review can compare `motion-ai` and `motion-plain` views. The still-card renderer `render_card.py`
  is only a fallback if a video render fails.

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

1. Render (or reuse) the article's video as in "Videos" above (Picks Stories: `--bg none`).
   `file_upload` only reads files in the session's scratchpad, so the MP4 must be there.
2. Open `https://business.facebook.com/latest/story_composer/?asset_id=109580998478548&business_id=123462012162006`.
3. Share to: click the dropdown (600,105). It defaults to BOTH `offbar1` (Facebook Page) and
   `offbahr`. Click `offbar1` (410,168) to uncheck it, zoom to confirm only `offbahr` is checked,
   click empty space (1100,500) to close.
4. Before clicking "Add photo/video", run this in the page so no native file dialog opens:
   `if(!window.__patched){const o=HTMLInputElement.prototype.click;HTMLInputElement.prototype.click=function(){if(this.type==='file'){if(!this.isConnected){document.body.appendChild(this)}return}return o.call(this)};window.__patched=true}`
   Then `find` and click "Add photo/video", `find` "file input element (type=file)", and
   `file_upload` the MP4 to it. Wait 15 s for the video to process (screenshot to confirm the
   preview shows it). If the video will not load after a retry, upload the matching `.png` instead.
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

## Pinterest procedure (added 2026-10-18; no verified coordinates yet, screenshot before clicking)

Accounts: Picks = @lakeramw (the Chrome session is normally signed in as this one); Clarity =
@vonguulian, reached via the account menu > "Your accounts" > Vonguul Clarity. Switch BACK to
Picks when done. Confirm the account name before every pin; stop if it is not the expected one.

1. Draft first. For each article create the next `PIN-BATCH-NN.md` in that site's repo (copy the
   layout of `vonguul-picks/PIN-BATCH-41.md`): Board, Article, Destination URL, then one pin with
   Title (under 100 chars, no prices), Description (the article's tip + 2-3 hashtags, no prices;
   Clarity: reflection framing, never proof) and the product image from `public/images/products/`.
2. Destination URL: `https://<site>/articles/<slug>/?src=pinterest` (the tag is mandatory).
3. Board: verify the real board name in the pin builder's board search (names in
   `PINTEREST-BOARDS.md` and `PIN-REFRESH.md` have been wrong before). Click into the board search
   box first, then pick the exact match. If no existing board fits (e.g. a new Clarity practice
   like Palmistry), create one (added 2026-10-22 at the user's request): "Create board" at the
   bottom of the board picker, named after the practice or topic in the style of the existing
   boards (e.g. "Palmistry", "Tea Leaf Reading"), public (not secret), on the account you are
   pinning to. Confirm the account first, never create a duplicate of an existing board, and log
   the new board in the PIN-BATCH file (and add a row to Clarity's `PINTEREST-BOARDS.md`).
4. Tagged topic: set it at creation (it cannot be edited later). Never accept Pinterest's first
   suggestion. Wait for suggestions to settle, read the option list, and choose an exact or clearly
   relevant match (e.g. "Baking Organization", "Spice Storage"). If none is clearly right, use a
   safe generic one and log it. A wrong topic ("Computer", "Dog Tattoo") has happened before.
5. Publish immediately (do not use Schedule). Upload the article's MP4 with `file_upload` (the pin
   builder accepts MP4; the video must be in the scratchpad) and wait for it to process. If it
   will not process within about 60 s, use the matching `.png` still instead. **If the video is
   `motion-ai`, switch on "Mark as AI-modified"** in the pin builder before publishing (screenshot
   to confirm). Clarity and `motion-plain` pins: leave it off. Pin pages only hydrate after a screenshot,
   so take one after navigating. JS-clicking `[role=option]` and `button[role=menuitem]` works for
   tags and menus.
6. Verify the pin appears on the board and its link is the tagged URL (check from the pin page).
   Output containing URLs with query strings can be blocked in the JS tool: return booleans.
7. Log: set the PIN-BATCH status line (`Pins posted (date), verified linking with ?src=pinterest`),
   and in Clarity's `PINTEREST-BOARDS.md` set the row to `posted` if all its pins are live.

## TikTok procedure (added 2026-10-18; account @offbahrvonguul, shared by Picks and Clarity)

Video posts since 2026-10-25 (Photo Mode before that). Older gotchas are in `TIKTOK-POSTS.md`
(read its "Gotcha" and "Repost round" sections before the first post of the day).

1. Video: render (or reuse) the article's MP4 as in "Videos" above.
2. Open `https://www.tiktok.com/tiktokstudio/upload` (the Videos tab), confirm the account is
   @offbahrvonguul, then `find` "file input for video upload (type=file)" and `file_upload` the MP4.
   If the call reports a lost connection, screenshot first; retry only if the upload did not land.
   Wait 8 s. Pop-ups after upload (verified 2026-10-25): **"Turn on automatic content checks?" ->
   click Cancel, never "Turn on"** (it changes account settings); "New editing features added" ->
   "Got it".
3. The video form has ONE Description field (no separate title; it starts filled with the file
   name). Select all and replace it with: a punchy first line (under 90 characters, no prices), a
   short caption ending "Full guide on the Vonguul Picks site, link in bio." (Clarity: "Vonguul
   Clarity") and 5 hashtags. Screenshot to confirm the text. Sound (optional): "Sounds" in the
   editor on the right; Picks lofi, Clarity ambient piano, if offered.
   **`motion-ai` videos:** click "Show more" and switch ON "AI-generated content"; zoom to confirm.
   Clarity (`motion-geometry`) and `motion-plain`: leave it off.
4. Leave "Now" / "Everyone" selected. Never use "Schedule" (it triggers a consent prompt that must
   not be accepted). The Post button moves with viewport height: screenshot, then click it.
   Click Post in its own batch, then start the next upload in a separate batch.
5. "Content under review" / "Only me" right after posting is normal and clears by itself.
6. After the round, open TikTok Studio's content list and confirm each new post is listed.
7. Log: add rows to the newest dated table in `vonguul-picks/TIKTOK-POSTS.md` or
   `vonguul-clarity/TIKTOK-POSTS.md` (article, title, posted date, format).

## Logging

- Threads: add rows to the dated catch-up table in `vonguul-picks/THREADS-POSTS.md` or
  `vonguul-clarity/THREADS-POSTS.md` (article, type, topic, date) and update the "Still never on
  Threads" list.
- Stories: add rows to the newest dated table in each `INSTAGRAM-STORIES.md` (article, date,
  sticker text, format) and update the "Never had a Story yet" lists.
- Format values: `motion-geometry` (Clarity), `motion-ai` / `motion-plain` (Picks test), `still`
  (fallback card). Add a `**Format:**` line to each new PIN-BATCH file.
- Pinterest: the new `PIN-BATCH-NN.md` files and, for Clarity, `PINTEREST-BOARDS.md`. TikTok: the
  two `TIKTOK-POSTS.md` files.
- In each repo, with `git -C <repo>` (never `cd`): `pull --rebase`, `add` only the tracker files you changed, commit with a
  message ending in `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, push.

## Content pipeline (last step of every run, added 2026-10-26)

So the backlog never runs dry, end every run by keeping researched topics waiting for the owner.
Do this AFTER posting and logging are pushed, and skip it if the run hit a stop condition.

1. Read `vonguul-picks/research/PIPELINE.md`. Count the rows in "Researched, waiting for the
   owner's approval" per site. If both sites have 3 or more, stop here (nothing to do).
2. Otherwise research ONE new topic for each site that is short (at most 2 topics per run). Take the
   first fitting row from "Ideas" (seasonal window first), or a "Hold" row whose recheck date has
   passed, or a spin-off of a recently published article. Skip anything an existing article already
   covers: `grep -ril "<keyword>" /c/Users/laker/Downloads/vonguul-picks/src/content/articles /c/Users/laker/Downloads/vonguul-clarity/src/content/articles`.
3. Verify products on live Amazon pages with the built-in browser (`mcp__Claude_Browser__*`):
   navigate to https://www.amazon.com/robots.txt, then from page JS `fetch('/s?k=...')` for search and
   `fetch('/dp/<ASIN>')` for each product page, parsed with DOMParser (rating `#acrPopover
   .a-icon-alt`, reviews `#acrCustomerReviewText`, stock `#availability`, seller
   `#merchantInfoFeature_feature_div`, buy box `#add-to-cart-button`). Keep each JS call under ~8
   product fetches (45 s timeout). If the built-in browser is unavailable or asks for approval, use
   Claude in Chrome on an amazon.com tab with the same fetch method; if that is blocked too, skip
   research today and say so in the report.
4. Quality bar (same as every batch): in stock, rating about 4.3 or better with a real review count,
   an Amazon-sold or reputable seller, and an ASIN not already on either site (check with
   `grep -rh 'asin: "' /c/Users/laker/Downloads/vonguul-picks/src/content/articles /c/Users/laker/Downloads/vonguul-clarity/src/content/articles`).
   Aim for 5 to 9 passing products. No prices in anything meant for an article (prices may appear in
   the research file as internal notes). Clarity: plan a "Worth being direct about" angle; no health
   or efficacy claims.
5. Write the findings with the Write tool to `vonguul-picks/research/RESEARCH-AUTO-<YYYY-MM-DD>-<topic-slug>.md`
   (Clarity: `vonguul-clarity/research/...`), in the same table format as
   `RESEARCH-QUEUE-E-PICKS-2026-10-26.md`: product, ASIN, rating (reviews), seller, verdict, plus
   writing notes and a recommendation (BUILD, ADD to an existing article, or HOLD with a reason).
6. Update `PIPELINE.md`: move the topic from Ideas/Hold to "Researched, waiting for the owner's
   approval" (or to Hold with a recheck date if it failed the bar). Commit only the research files
   and PIPELINE.md with `git -C` (pull --rebase, add, commit, push), message ending in the
   Co-Authored-By line.
7. **Never build, draft or publish an article in this routine.** Building needs the owner's approval
   in a session. In the final report, list every topic waiting for approval (site, topic, product
   count, recommendation) so the owner can reply "build X".

## Stop conditions

Stop posting (log what was done, report it) if: the wrong account is signed in; a platform shows
a limit or "try again later" message (TikTok "Too many uploading attempts" ends TikTok for the day;
Pinterest rate or spam warnings end Pinterest for the day); a post fails to appear after a retry; or anything asks for
a password, consent, terms or payment. Never accept consent prompts (for example TikTok's
"Allow your video to be saved for scheduled posting"). Pinterest and TikTok stop independently:
if one platform hits a stop condition, finish the others and report it.
