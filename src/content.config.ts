// Import the glob loader
import { glob } from "astro/loaders";
// Import utilities from `astro:content`
import { z, defineCollection } from "astro:content";

// =========================
// BLOG COLLECTION (existing)
// =========================
const blog = defineCollection({
  loader: glob({ pattern: "**/[^_]*.md", base: "./src/blog" }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    description: z.string(),
    author: z.string(),
    image: z.object({
      url: z.string(),
      alt: z.string(),
    }),
    tags: z.array(z.string()),
  }),
});

// =========================
// FICTION COLLECTION (new)
// =========================
const fiction = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/fiction" }),
  schema: z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  published: z.date().optional(),
  }),
});


// Export BOTH
export const collections = {
  blog,
  fiction,
};
