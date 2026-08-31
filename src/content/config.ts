import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
    heroImage: z.string().optional(), // used for OG/Rich Pin image + Pinterest hero
    category: z.string(), // maps to a Pinterest board
    keywords: z.array(z.string()).default([]),
    products: z
      .array(
        z.object({
          name: z.string(),
          asin: z.string(),
          note: z.string().optional(),
          image: z.string().optional(),
        })
      )
      .default([]),
  }),
});

export const collections = { articles };
