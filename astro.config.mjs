// @ts-check
import { defineConfig } from "astro/config";

import preact from "@astrojs/preact";

import tailwindcss from "@tailwindcss/vite";

import shadcnRegistry from "astro-shadcn-registry";

// https://astro.build/config
export default defineConfig({
  site: "https://coughy.net",
  integrations: [preact(), shadcnRegistry({
      paths: {
        registry: "src/registry",
        contentCollection: "src/content",
        outputRegistry: "registry.json",
      },
      componentTypes: ["ui", "component", "hook", "lib"],
      registry: {
        name: "my-registry",
        homepage: "https://mycomponents.com",
      },
      preCommitHook: {
        enabled: false,
        paths: ["src/registry/**/*"],
      },
      advanced: {
        defaultLanguage: "react",
        registryURL: "https://mycomponents.com",
        deleteRegistryAfterBuild: true,
      },
    })],

  vite: {
    plugins: [tailwindcss()]
  }
});