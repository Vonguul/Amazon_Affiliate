import { defineConfig } from 'astro/config';

// Update `site` again if/when you attach a custom domain in Vercel — Astro
// uses it to generate correct canonical URLs and Rich Pin / Open Graph
// metadata, and Pinterest domain verification is tied to whatever's set here.
export default defineConfig({
  site: 'https://vonguul-picks.vercel.app',
  output: 'static',
});
