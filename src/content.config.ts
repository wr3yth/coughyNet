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


const stories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories" }),
  schema: z.object({
  title: z.string().optional(),
  description: z.string().optional(),
  published: z.date().optional(),
  }),
});

const poetry = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./src/poems",
  }),
  schema: z.object({
    title: z.string(),
    poet: z.string().optional(),
    date: z.string().optional(),
    loyalty: z.string().optional(),
    image: z.string().optional(),
  }),
});

const storiesFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/stories-fa" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    file: z.string().optional(),
    image: z.string().optional(),
    link: z.string().optional(),
    date: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const wiki = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),   // perception, states, tools...
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});

const wikiFa = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/wiki" }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
  }),
});




export const collections = {
  blog,
  stories,
  poetry,
  storiesFa,
  wiki,
  wikiFa,
};
