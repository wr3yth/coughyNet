import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  output: "static",
  vite: { 
    plugins: [tailwindcss()],
    // Remove the entire server.watch section or set usePolling to false
    server: {
      watch: {
        usePolling: false, // Or remove this entire block
      },
    },
  },
});