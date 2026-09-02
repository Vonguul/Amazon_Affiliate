import { defineConfig } from 'astro/config';

// Update `site` again if/when you attach a custom domain in Vercel — Astro
// uses it to generate correct canonical URLs and Rich Pin / Open Graph
// metadata, and Pinterest domain verification is tied to whatever's set here.
// Also update it in Google Search Console / Bing Webmaster Tools if you
// verify a new domain there later.
//
// Sitemap is hand-rolled at src/pages/sitemap.xml.ts rather than via
// @astrojs/sitemap — that package hit a real incompatibility with this
// Astro version ("Cannot read properties of undefined (reading 'reduce')"
// in its astro:build:done hook) that reproduced identically across two
// different package versions. A ~15-line custom endpoint avoids the
// dependency entirely.
export default defineConfig({
  site: 'https://vonguul-picks.vercel.app',
  output: 'static',
});
