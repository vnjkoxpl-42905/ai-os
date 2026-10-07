---
type: brainstorm
subject: Main Hub Layout / Spacing Brainstorm / Discovery Notes
updated: 2026-07-19
aliases: []
---

# Main Hub Layout / Spacing: Brainstorm / Discovery Notes
Date: 2026-07-19 · Goal: Define what the lsatprep.study main hub layout is SUPPOSED to look like (especially with the Messages side panel open) so we can fix the spacing.

## Summary / key decisions
(running synthesis, updated as you go)

## Code findings (pre-interview, from repo)
- Main hub page: `src/pages/AcademyMainhub.tsx`. Shell: `src/components/mainhub/StudentShell.tsx`. Messages panel: `src/components/mainhub/StudySidecar.tsx`.
- The sidecar IS docked (not an overlay): StudentShell puts main + sidecar in a flex row; main flexes down, sidecar has a user-resizable width (localStorage `lsatu:sidecarWidth`, min-clamped).
- **Likely root cause:** AcademyMainhub's grids use *viewport* Tailwind breakpoints (`md:` `lg:` `xl:` `2xl:` grid-cols with hard `minmax(560px,…)` etc.). When the sidecar eats ~380–450px, the viewport is still `xl` so the page keeps its wide 3-column layout inside a much narrower container → cramped hero, cut-off "Today" card. Fix direction: container queries (`@container`) or measuring the main pane width instead of viewport breakpoints.

## Q&A log

### Q1 — Target layout with Messages panel open
- Asked: what should the hero do when the sidecar is docked open?
- Captured: Joshua supplied a reference screenshot of the CORRECT state. With the panel open, the page keeps its full desktop composition — hero with date/greeting + robot + practice-search card all visible, and below it Practice Tools (left) + Today card (right) side by side — but **everything resizes/reflows to fit the narrower container**. Nothing gets cut off, nothing overlaps, no columns dropped. "Things should be resized to fit like this."
- Implication: fix = make the page respond to its container width (fluid/container-query sizing), not drop to a tablet layout.

### Q2 — Behavior across sidecar widths
- Asked: fluid at every panel width, or step down at some floor?
- Captured: Confirmed recommendation — scale fluidly to fit the container at any panel width, down to ~900px content width; below that, step to the existing stacked tablet layout instead of shrinking further. ("ok")

### Q3 — Scope
- Asked: fix Home only, or sweep every shell page next to the panel?
- Captured: "fix home now." Home page (AcademyMainhub) is the scope of this pass. Other pages: check later, fix only if broken.

## Summary / key decisions (final)
1. Messages sidecar is docked; Home must reflow to its container, keeping the full desktop composition (hero 3-col + two body cards) resized to fit — per reference screenshot.
2. Fluid at any sidecar width down to ~900px container; below that, step to stacked tablet layout.
3. Scope: Home page only, built as container-query pattern reusable later.
4. Next step: implement in projects/lsatu (AcademyMainhub.tsx), verify in browser with panel open/closed/resized.

## Open flags (pending input)
