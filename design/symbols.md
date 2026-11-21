---
type: reference
subject: Symbols and icons, where to get them and how to make them
created: 2026-10-26
updated: 2026-10-26
aliases: [Icons, Symbols, Glyphs, Icon sources, Replace an icon]
tags: [design, icons, svg]
sources:
  - ../wiki/sources/25-claude-design-tricks-robonuggets.md
  - ../wiki/sources/claude-design-fifteen-hacks-jack.md
contradictions: []
---

# Symbols and icons: use this page before drawing or replacing one

Read this whenever a design needs a symbol, or Joshua asks to replace one. It lists where good icons come from, the method for making our own, and the symbols already made, so the next design reuses them instead of starting over.

## The method, in order

1. **Reuse what we already made.** Check [symbols we have made](#symbols-we-have-made) first. One meaning keeps one symbol everywhere.
2. **Draw a task-shaped symbol when the idea is specific to us.** A generic library icon for a course idea reads as stock. Draw it from the thing it means (a drill is one condition leading to another, so its symbol is exactly that). Use SVG, the same 24px grid and stroke weight as the surrounding icon set, and check it at the real display size, not only zoomed.
3. **Otherwise take icons from one pack in one style.** Download a whole pack from one source rather than mixing single icons from different sets, and give Claude the folder as a reference so new icons match it. (RoboNuggets, tip 16, 8:20.)
4. **Always ask for SVG.** SVG scales without blurring and stays editable: colour can be changed by hand and the icon can be animated. (RoboNuggets, tip 17, 8:51 to 9:06.)
5. **Animated icons:** take a Lottie file from Lordicon, where the motion is already built in. Motion must have a static fallback and stop under reduced motion. (RoboNuggets, tip 18, 9:16.)
6. **Check the licence and attribution before shipping.** Some free tiers require attribution; paid tiers remove it. (Jack, Hack 6, 16:04 and 16:51.) Record the source and licence beside the asset.

## Where to get them

| Source | What it is good for | Source claim | Check before use |
|---|---|---|---|
| [Iconify](https://iconify.design) | Whole open-source icon sets in one consistent style | RoboNuggets tip 16 | Each set carries its own licence |
| [Flaticon](https://www.flaticon.com) | Large packs in many styles, illustrated and line | RoboNuggets tip 16; Jack Hack 6 | Free use requires attribution; check the plan |
| [Icons8](https://icons8.com) | Icons and matching illustrations in shared styles | Jack Hack 6 | Free use requires attribution or a subscription |
| [Lordicon](https://lordicon.com) | Animated icons as Lottie files | RoboNuggets tip 18 | Free and paid tiers differ |
| [Creators Toolbox](https://creatorstoolbox.com) (resources section) | Directory of 150+ free resources: SVG icons, logo galleries, animated components, mock-up kits | RoboNuggets tip 19 | A directory; check each linked resource's own licence |
| `lucide-react` | LSAT U's installed icon library, used for general interface icons | `PRODUCT.md` | Already installed; no new dependency |

Counts and free-tier descriptions are the creators' dated claims (October 2026), not verified. Account access and licences were not checked when this page was written.

## Symbols we have made

| Symbol | Means | Where | File |
|---|---|---|---|
| lucide `route`: two stops joined by a path | A drill: a route from one condition to its result | Conditional bootcamp: sidebar Practice drills, Home practice tile, chapter path stations, Practice page, lesson list | `ai-os-projects/lsatu-conditional-full-20261025/src/bootcamps/conditionals/components/CourseGlyphs.tsx` (`DrillGlyph`) |
| lucide `gallery-vertical-end`: front card with a stack behind | Flashcards | Same surfaces as above | Same file (`CardsGlyph`) |

History, 2026-10-26: Joshua rejected the stock Sparkles (the generic "AI" symbol), Bookmark (unrelated to flashcards) and Dumbbell (a gym icon for drills). A first pair of hand-drawn symbols replaced them, but the drill mark was illegible at 14px path-station size. Following this page's method, candidates were pulled from Iconify across lucide, Tabler, Phosphor and Hugeicons and compared side by side at 14px, 20px and 36px. `route` read most clearly at 14px; both final picks come from lucide, the app's existing pack (ISC licence, already installed as `lucide-react`), so they match every other icon without a new dependency. Rendered at 1.75 stroke; 20px in a soft square well where they need presence, 18px in navigation, 14px on drill path stations. `DrillGlyph`/`CardsGlyph` stay the one definition, so changing a meaning's symbol is a one-file edit. Local branch only: not committed or live at the time of writing.

Runners-up worth reusing: Phosphor `cards` / `cards-three` (cleanest stacked cards, but a different pack from lucide), Tabler `target-arrow` (a goal, not a conditional).

When you make a new symbol, add a row here with its meaning and file.

## Replacing a symbol

1. Find every place the meaning appears, not only the one Joshua pointed at, and replace them all so one meaning keeps one symbol.
2. Prefer a symbol from the table above. If none fits, follow the method.
3. Check it beside the neighbouring icons at real size, in light and dark themes.

## Avoid

- Sparkles or stars for anything that is not about AI. It is the stock "AI" mark and reads as AI slop.
- Icons from mixed packs on one surface.
- Raster icons (PNG) where an SVG exists.
- An icon whose usual meaning differs from ours (a bookmark for flashcards, a dumbbell for logical practice).
