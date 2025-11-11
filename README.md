# Coughy.Net

## 🚀 Project Structure



```text
/
├── public/
│   └── favicon.svg
├── src
│   ├── assets
│   │   └── astro.svg
│   ├── components
│   │   └── Welcome.astro
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       └── index.astro
└── package.json
```



## 🧞 Commands



| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `pnpm install`             | Installs dependencies                            |
| `pnpm dev`             | Starts local dev server at `localhost:4321`      |
| `pnpm build`           | Build your production site to `./dist/`          |
| `pnpm preview`         | Preview your build locally, before deploying     |
| `pnpm astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `pnpm astro -- --help` | Get help using the Astro CLI                     |

[Astro's documentation](https://docs.astro)

## Bug fixes

after installing tailwindcss there was a strange bug inside astro.js.config `./astro.js.config`  and I got it fixed.
if same thing happened, press ```shortcut ctrl+shift+p``` (if you use vscode) and run this command below: 

```vscode TypeScript: Restart TS server```