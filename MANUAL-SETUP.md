# Manual Setup Checklist

Everything in this repo is scaffolded and ready. These are the steps that
have to happen on accounts I can't create or log into on your behalf.

## 1. GitHub
- [ ] Create a GitHub account if you don't have one, or confirm the account
      you want this tied to.
- [ ] Create a new **private** repo (e.g. `vonguul-picks`).
- [ ] From this folder, run:
  ```bash
  git remote add origin https://github.com/<your-username>/vonguul-picks.git
  git branch -M main
  git push -u origin main
  ```

## 2. Node.js (needed to build/preview locally)
- [ ] Install Node.js LTS from https://nodejs.org (this machine doesn't have
      it yet — Vercel/Cloudflare will still build fine without it since they
      run their own Node in the cloud, but you'll want it locally to preview
      changes before pushing).
- [ ] Once installed: `npm install` then `npm run dev` to preview at
      http://localhost:4321

## 3. Vercel (or Cloudflare Pages)
- [ ] Create a Vercel account (https://vercel.com), sign in with GitHub.
- [ ] "Import Project" → select the `vonguul-picks` repo.
- [ ] Framework preset: Astro (auto-detected). No config changes needed.
- [ ] Deploy. You'll get a live `*.vercel.app` URL immediately.
- [ ] (Optional) Add a custom domain under Project → Settings → Domains.
- [ ] Once you have a real domain, update `site:` in `astro.config.mjs` to
      match it — this affects canonical URLs and Rich Pin metadata.

## 4. Pinterest
- [ ] Create a Pinterest **Business** account (not a personal one — business
      accounts unlock analytics and Rich Pins): https://business.pinterest.com
- [ ] Claim your website domain: Settings → Claim → enter your domain →
      Pinterest gives you a verification meta tag or DNS record.
  - If meta tag: paste it into `src/layouts/BaseLayout.astro` where the
    `<!-- Pinterest Rich Pin verification -->` comment is, then redeploy.
- [ ] Apply for Rich Pins: https://developers.pinterest.com/docs/rich-pins/overview/
      (validates against the Open Graph tags already in `BaseLayout.astro`).
- [ ] Create boards matching your content categories (the Pinterest
      Strategist agent will propose the initial board map once you tell it
      to run).

## 5. Amazon Associates
- [ ] Confirm your Associate ID is `Vonguul-20` and which marketplace
      (assumed amazon.com — tell me if different).
- [ ] Add this site's actual domain to your Associates account under
      "Manage Websites" once it's live — required by the Associates
      operating agreement.
- [ ] Note: Amazon requires **3 qualifying sales within 180 days** of
      signup to keep the account active, and Product Advertising API access
      also requires this threshold. Until then, links are built manually
      (which the `AffiliateLink` component already handles) — no API access
      needed for this phase.

## 6. Ongoing manual step (can't be automated)
- [ ] Final approval of each batch of drafted articles/pins before they go
      live — this is the one checkpoint that stays manual by design.
