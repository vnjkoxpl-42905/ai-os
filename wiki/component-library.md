---
type: reference
subject: Saved UI component library (21st.dev and others)
created: 2026-11-18
updated: 2026-11-18
aliases: [component library, saved components, 21st.dev components, UI components]
tags: [design, components, 21st, claude, codex]
sources: []
---

# Component library: where the saved UI components live

Joshua's saved UI components sit in one folder outside this vault: `C:\Users\Joshu\dev\component-library`. Like app code, it stays outside the vault on purpose. This page is the pointer and the catalog, so a design session finds the right component without searching the disk.

**Before building or restyling any UI, check this page first.** If a saved component fits, start from its source instead of writing a new one.

## What is in the library

Each component is one folder holding one `component.md`. The markdown is the source of truth: front matter (name, description, tags, height, source), the component source in a fenced `tsx` block, a `demo.tsx` block, and a Notes list.

| Component | What it is | Tags | Source | Open |
|---|---|---|---|---|
| 3D Curved Carousel | Photo carousel seen through a curved lens; WebGL cards bend and split into colour fringe toward the edges. Drag, flick, arrows. | carousel, webgl, hero, gallery | 21st.dev | [component.md](../../component-library/components/3d-curved-carousel/component.md) |
| Journal Spread Carousel | Scrapbook of open double pages in 3D, with polaroid photos, washi tape and handwritten notes. Pure CSS 3D. | carousel, 3d, scrapbook, hero | 21st.dev | [component.md](../../component-library/components/journal-spread-carousel/component.md) |
| Section Progress Stepper | Segmented progress for submitted, current and upcoming sections. Adapted from Origin UI (MIT). Fits timed-section UI. | progress, stepper, assessment | 21st.dev (`@originui`) | [component.md](../../component-library/components/section-progress-stepper/component.md) |
| Tumble Deck Showcase | Stack of website screenshots on edge; the front card tips forward, the next one falls. Needs `gsap`. | showcase, 3d, scroll, gsap, hero | 21st.dev | [component.md](../../component-library/components/tumble-deck-showcase/component.md) |

Added 2026-11-11 (the stepper's added date is not recorded in its file).

## Already adapted into LSAT U

These came from 21st.dev and are live code in the LSAT U checkout (`C:\Users\Joshu\dev\lsatu\src\`), not in the library folder:

| Component | File |
|---|---|
| Animated button (from "Animated Vercel-like Button") | `components/ui/animated-button.tsx` |
| Orbital loader (from "CoreSpin Loader") | `components/ui/orbital-loader.tsx` |
| Story scroll (stacked covering scenes) | `components/ui/story-scroll.tsx` |
| Choice response timeline (from Timeline-02, `@ruixen.ui`) | `topics/abstract/components/views/ChoiceResponseTimeline.tsx` |

## Loose 21st.dev references outside the library

Retrieved during earlier design runs and kept as reference files, not library entries. Promote one into the library (Add a component, below) before reusing it.

| Reference | File |
|---|---|
| Segmented progress (20 animated segments, count-up %) | `projects/lsatu-score-light/docs/agent/21st-progress-reference.tsx` (copied into most `ai-os-projects/lsatu-*` worktrees) |
| Animated tabs (sliding highlight), demo 1962 | `brainstorms/2026-10-25-amanda-post-session/component-references/21st-animated-tabs.tsx` |
| Animated beam (framer-motion connector), demo 919 | `brainstorms/2026-10-25-amanda-post-session/component-references/21st-animated-beam.tsx` |
| Origin UI radio group card (pattern only, no code kept) | `../ai-os-projects/lsatu-conditional-full-20261025/.taste-skill/practice-preview-prototype/21st-reference.md` |
| 21st theme study (Modern Minimal, Vercel) | `research/2026-10-24-charcoal-palette/` |

## Finding a component fast

Folder names in the library do not contain "21st"; the source is in each file's front matter. So never search the disk by path name. Search content instead:

```bash
grep -l "21st" C:/Users/Joshu/dev/component-library/components/*/component.md
```

Online 21st.dev bookmarks are separate: `npx @21st-dev/cli bookmarks` (needs a valid `21st login`; it returned HTTP 401 on 2026-11-18).

## See them rendered

```bash
node C:/Users/Joshu/dev/component-library/serve.mjs
```

Then open http://localhost:4321 (needs Node and internet for React and Babel from cdnjs). `start.bat` in that folder does the same by double-click.

## Add a component

1. Copy `_template/component.md` to `components/<slug>/component.md`.
2. Fill the front matter, paste the source in a block tagged `tsx file=<name>.tsx` and the usage in a block tagged `tsx file=demo.tsx`.
3. Refresh the gallery. There is no index to update.
4. **Then add a row to the table above**, so this page stays the searchable catalog.

Keep source blocks exactly as received; record changes in the Notes list. Full rules: the library's `README.md`.

## Using one in a product

- Read the component's Notes first (dependencies, CORS, aspect ratios).
- Product use, project conventions and verification: `lsatu/docs/agents/component-library.md`. Any change under `src/components/` still needs running-app verification.
- Design principles, the LSAT U palette and quality checks still apply: [design hub](../design/README.md). A saved component is a starting point, not a finished design.

## 21st.dev tooling

21st.dev is set up as an MCP server (`21st`), a Claude Code plugin (`21st@21st`) and eight `21st-*` skills, from 2026-11-11. Search and install new items with `21st-cli-use`; see `lsatu/docs/agents/component-library.md` for the setup and key handling. Browse by hand at 21st.dev.

## Limits, as of 2026-11-18

- Backup: the folder has a local git history (one commit, 2026-11-18) and `setup/backup/backup.ps1` now mirrors it to `G:\My Drive\CLAUDE-CODE-BACKUP - START HERE\current\component-library\` every 10 minutes. **Google Drive was not mounted on 2026-11-18** (G: missing), so no Drive copy exists until Drive is signed in. It is not on GitHub.
- This page lists what existed on disk on 2026-11-18. The folder, not this page, is the authority if they disagree.
- Origin: the setup session was "21st MCP HTTP transport setup" (2026-11-14, cwd `dev\lsatu`).
