---
name: brutal-palette-opacity
description: "Abstract bootcamp's brutal-* Tailwind colors silently dropped opacity shorthands (bg-brutal-green/40) until wrapped in color-mix on 2026-10-12; preview Abstract at /dev/abstract-preview."
metadata:
  node_type: memory
  type: project
  originSessionId: e73e83bf-cdd9-4e5c-a7ed-0a7661973760
  modified: 2026-10-13T02:53:06.119Z
---

The Abstract bootcamp (`src/topics/abstract`) palette is oklch CSS variables. As bare `var(--brutal-*)` Tailwind tokens, any opacity shorthand like `bg-brutal-green/40` generated no CSS, so every tinted right/wrong box rendered blank. Fixed in tailwind.config.ts on branch `claude/abstract-bootcamp-fix` by mapping each token to `color-mix(in oklch, var(--brutal-x) calc(<alpha-value> * 100%), transparent)`.

**Why:** found during the 2026-10-12 Abstract audit; invisible in code review, only visible in the rendered page.

**How to apply:** if tints vanish on any bootcamp whose tokens are `var(...)`, check this first. For local QA without sign-in, the same branch adds dev-only `/dev/abstract-preview` (progress writes skip with no user). Capture: `brainstorms/2026-10-12-abstract-bootcamp-fix.md`. Related: [[in-app-browser-scales-css-widths]].
