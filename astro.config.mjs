import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Update `site` again if/when you attach a custom domain in Vercel — Astro
// uses it to generate correct canonical URLs and Rich Pin / Open Graph
// metadata, and Pinterest domain verification is tied to whatever's set here.
// Also update it in Google Search Console / Bing Webmaster Tools if you
// verify a new domain there later.
export default defineConfig({
  site: 'https://vonguul-picks.vercel.app',
  output: 'static',
  integrations: [sitemap()],
});
