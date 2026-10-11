# Must arrow page review, 2026-10-11

Local preview only. No commit, push or deployment.

## Teaching evidence and changes
The preserved conditional-reasoning HTML at lines 326, 339-340 specifies Sufficient → Necessary, with sufficient on the left and necessary on the right. Renamed title to Must arrow. Introduced meaning through law-school enrollment, visibly labelled both roles, retained the raffle walkthrough and moved-if transfer question. Enlarged explanatory text and separated teaching sections.

## Scoped Impeccable audit
Read installed impeccable SKILL.md, audit/product references, and product/design context. Code review covered MustArrowNote, its stylesheet and path title; browser review covered the actual light-theme page.

- Fixed: light-only background literals replaced with existing light/dark lesson tokens.
- Fixed: cramped mobile must label given a wider arrow column.
- Positive: semantic headings, native controls, existing focus treatment, explicit arrow meaning, no new dependency or animation.
- Browser evidence: 320, 960, 1600px layouts have no document overflow; inspected narrow and docked screenshots. Completed all four diagram steps and observed reset focus at completion, then reset lesson.
- 33 focused tests passed; typecheck passed. Final production build recorded in must-arrow-build.log.
- Limits: no full WCAG certification, screen-reader session, performance profiling or live dark-theme contrast measurement. The walkthrough remains guided reveals; the following question tests independent direction choice.

Screenshot: C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/must-arrow-updated.png

## Source-driven correction, 2026-10-11
Joshua rejected the abstract opening and asked for explicit direction. New local draft: The must arrow points from left to right. If the left side is true, the right side must be true. The LSAT Lab clip jeDnykOrswY at0:31 supports this certainty reading;8:19 supports left requires right. Retained rule-versus-fact boundary. This exact new wording is implemented, not yet expressly approved by Joshua.14 focused tests and production build passed; actual browser DOM verified. Screenshot: C:/Users/Joshu/.codex/visualizations/2026/10/10/01a1282c-ac7e-7380-90fe-9ca58e32512f/must-arrow-source-wording.png
