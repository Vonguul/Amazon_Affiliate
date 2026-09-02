import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

// Hand-rolled sitemap — see the note in astro.config.mjs for why this
// isn't using @astrojs/sitemap. Add any new static (non-article) page
// here manually when one gets added.
export const GET: APIRoute = async ({ site }) => {
  const base = site?.toString().replace(/\/$/, '') ?? '';
  const articles = await getCollection('articles');

  const paths = ['/', ...articles.map((a) => `/articles/${a.slug}/`)];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${paths.map((path) => `  <url><loc>${base}${path}</loc></url>`).join('\n')}
</urlset>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
};
