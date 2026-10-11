# Necessary and must-arrow visual revision

2026-10-11. Local preview only. ASTRA implements; Codex coordinates browser verification; Claude Opus independently inspects the finished code and saved screenshots. No commit, push or deployment.

## Authorized scope

- State the actual law-school rule inside the necessary-condition case comparison.
- Group 2 explicitly identifies necessary conditions. Preserve the displayed order: only, only if, only when, only where, always, requires, must. Examples follow the same order.
- Make the indicator explorer engaging and ordered, with keyboard and touch equivalents to hover.
- Redesign necessary and must-arrow presentation with generous spacing, aligned conditions, clear roles, refined depth and purposeful motion. Preserve approved definition, complete conditions, rule-versus-fact boundaries, media and practice.
- Three rendered inspection and refinement passes. Responsive and reduced-motion checks.

## Inspection instructions

Review only the scoped new lesson UI and its styles/tests. Existing unrelated checkout changes are outside this task. Inspect current necessary lesson, indicator explorer, case panel, must-arrow note and scoped CSS. Read saved teaching preferences at C:/Users/Joshu/dev/ai-os/.agents/skills/bootcamp-builder/references/teaching-preferences.md and source comparison at 2026-10-11-must-arrow-review.md in this folder. Compare wording with the retained examples and approved definition. Check accessible interactions, small-width layout, motion, semantic logic and complete conditions. Do not claim live browser operation or tests: host supplies those separately.

## Evidence and iteration record

Baseline inspected in the live Codex browser: necessary indicator list and examples were differently ordered; generic case-panel instruction omitted the local rule; arrow hierarchy emphasized labels and unevenly aligned the actual conditions. Implementation and final evidence pending.

Fresh screenshot evidence for reviewer (open these images):
- C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/astra-arrow-final.png
- C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/astra-indicators-final.png
- C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/astra-necessary-rule-final.png

Pass 1: rendered desktop baseline and new balanced condition panels; ordered explorer. Found excess indicator-row spacing and excessive arrow lead gap.
Pass 2: tighter gaps, removed panel opacity fade. Rendered docked/narrow arrow holds direction. Found indicators splitting words on 320px CSS viewport.
Pass 3: whole-word indicator labels and single-column controls at smallest width, preserving keyboard/touch and all seven indicators. Final host checks underway.

## Claude round 1 disposition
claude-opus-5-5, high effort, standard speed: REVISE. Accepted AL1-7. ASTRA fixes local diagram colors for dark theme, gates hover selection to wide hover-capable layouts, adopts real tabs with roving keyboard navigation, replaces index/title coupling with explicit ordered example data, clarifies instruction, relocates case CSS, adds behavior regressions. Host verified dark-theme diagram visually then restored original light class; keyboard End focuses/selects Must. Additional screenshot: C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/astra-arrow-dark-final.png. Host 320px CSS viewport: no document overflow, full-width 269x48px indicator buttons preserve all words. Reduced-motion stops arrow animation. Video readyState4/errornull. Build and 36 tests passed before review fixes; affected checks rerun after fixes.

## Final verification
Final Claude inspection APPROVED, observed claude-opus-5-5/high effort/standard speed. Result: C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/claude-astra-lessons-final/claudex-z70gnobq/result.json. No material defects. Final 38 focused tests and typecheck passed; production build passed with existing bundle/tooling warnings. Host verified desktop, docked, 320px and390px CSS viewport, keyboard, feedback, reduced motion, retained media load and dark diagram. Browser original theme/viewport restored, arrow page open. No deployment.

Low-note dispositions: AL2-1 measured390px buttons clientWidth=scrollWidth164, no overflow; retain. AL2-2 wide-hover selection is intentional requested exploration; narrow accidental traversal fixed; committed-preview refinement remains optional. AL2-3 recaptured settled indicator screenshot. AL2-4 adjacent necessary-words supplement still lists standalone then; outside two-page scope, record for its next content review. Reviewer compared saved source findings and approved copy, not original corpus in this run; no reviewer live-browser/test claim. No app edits after final approval.
