---
name: react-bits
description: Use when adding an animated UI component, text effect, cursor/hover effect, or WebGL/canvas background to a React project via React Bits (reactbits.dev), including when asked to recall or write a component from memory.
---

# React Bits

Fetches current component source from the React Bits public registry instead of recalling it from training data. React Bits (reactbits.dev, MIT + Commons Clause, by David Haz) publishes animated components in 4 variants (JS/TS × CSS/Tailwind). Its component license is separate from this helper's license; see `LICENSE`.

## The hard rule

**Never write React Bits component code from memory. Always fetch it live.**

Verified failure mode (baseline test, no skill): asked for Aurora + BlurText, an agent hallucinated plausible-looking code, guessed `framer-motion` as a dependency (the live package is `motion`), invented prop defaults, and only disclosed the guessing when explicitly asked. The code looked complete and shippable. It wasn't current.

Training data goes stale; this library updates variants in sync. If you can't reach the registry, say so — don't fall back to recalled code.

## Fetch

Resolve `<resolved-skill-directory>` to this installed skill's absolute directory. Keep the target application as the working directory so `--dest` stays app-relative. Quote the helper path when it contains spaces. Catalog refresh writes this skill's catalog, not the application.

```bash
node "<resolved-skill-directory>/scripts/rb-add.mjs" <Component> [<Component>...] --variant <JS|TS>-<CSS|TW> --dest <path>
node "<resolved-skill-directory>/scripts/rb-add.mjs" --list                      # print current registry names
```

Writes source files to `--dest` (default `src/components`) only if each destination is inside that folder and does not already exist. It prints the exact dependency command (default variant: `TS-TW`). Do not use `--install` unless the user has authorized changing the target project's dependencies.

No script access? Fetch directly — same registry, same rules:
```bash
curl -s https://reactbits.dev/r/<Name>-<JS|TS>-<CSS|TW>.json   # one component, files[].content = source
curl -s https://reactbits.dev/r/registry.json                  # current index, no source or category field
```
**reactbits.dev is an SPA** — an unknown path still returns HTTP 200 with an HTML shell. A 200 status proves nothing; parse the body as JSON and check it before trusting it.

## Workflow

1. **Confirm the variant** — JS or TS, CSS or Tailwind. Default to matching the project's existing files; ask if genuinely ambiguous.
2. **Find the component** — search [references/catalog.md](references/catalog.md), a 172-entry offline snapshot with categories, descriptions and dependencies, or use `--list` for current registry names. The snapshot is not a complete live index; verify the chosen component and variant against the registry.
3. **Fetch it** with `rb-add.mjs` (above). Never hand-write the file.
4. **Read the fetched file's own prop type/interface before wiring it up.** Don't guess prop names or defaults even for a component you fetched — read what's actually in the file.
5. **Show the printed dependency command.** Install dependencies only when the user has authorized changing the target project's package files.

## Gotchas

- **Scoped-package deps break naive parsing.** 10 components depend on scoped packages, e.g. `PixelTrail` → `@react-three/fiber@^9.3.0`. Splitting a dep string on `@` to get the name yields `""` for these. `rb-add.mjs` parses correctly (`/^(@[^/]+\/[^@]+|[^@]+)@?(.*)$/`); don't reimplement this by hand.
- **CSS variants are multi-file.** `JS-CSS`/`TS-CSS` ship a component file *and* a sibling `.css` file (both must be written). `JS-TW`/`TS-TW` are single-file with Tailwind utility classes.
- **No category field in the registry.** `registry.json` has name/title/deps/files only. Category (Text Animations / Animations / Components / Backgrounds) lives only in `references/catalog.md` (sourced from `reactbits.dev/llms.txt`).
- **`verbatimModuleSyntax` TS projects**: some fetched files import types alongside values in one `import {...}` statement (e.g. `import { motion, Transition } from 'motion/react'`) — split into a separate `import type {...}` if the project's tsconfig has `verbatimModuleSyntax: true`. This is a mechanical fix, not a reason to rewrite the component.

## Categories

The offline snapshot groups 32 Text Animations, 38 Animations, 45 Components and 57 Backgrounds in [references/catalog.md](references/catalog.md). It does not include every current registry entry. Use `--list` for the live index; this installed package has no catalog generator, so do not assume automatic refresh.

## After installing

For motion craft review, use the installed GSAP and Impeccable guidance as appropriate. Verification on 2026-10-23 found that the previously cited `DavidHDev/react-bits/AGENTS/SKILLS/` path returns 404 and the current upstream tree does not list `review-animations`, `improve-animations`, `find-animation-opportunities` or `apple-design`. Do not assume those skills exist or are installed. Component fetching and motion critique remain separate concerns.

<!-- BEGIN GENERATED DESIGN HUB ROUTE -->
For design work, first read the shared Claude Code/Codex design hub at
`C:/Users/Joshu/dev/ai-os/design/README.md` for relevant principles, sources,
skills, repositories and research. Keep this skill in its required runtime home.
<!-- END GENERATED DESIGN HUB ROUTE -->
