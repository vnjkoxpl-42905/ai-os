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

## Direct video and HTML comparison, 2026-10-11
Reviewed the clipped transcript at0:31,1:02-2:56,8:19-9:49 and original preserved HTML lines322-388 directly.

The video supplies the clearest spoken meaning: if left is true, right must be true (0:31); left requires right (8:19). Its changing geographic facts distinguish a valid forward inference from an invalid reverse. The HTML explains why notation helps: different sentences can express the same relationship. Its Sufficient → Necessary diagram (line326) is followed by identifying an indicator, drawing the arrow, placing the indicator's condition on its appropriate side, and filling the other condition (334-344). The breathing/air example demonstrates progressive construction (348-356). It then separately introduces contrapositive negation, not reading the original arrow backward unchanged (358-388).

Combined recommendation for the current page: meaning first; familiar complete-condition example; labels sufficient/enough and necessary/required; explicit left guarantees right and left requires right readings; demonstrate placement; then have the learner choose and explain a direction. Preserve complete conditions when abbreviating. Do not import the video's geographic/admissions examples or HTML breathing example when the existing law-school/raffle anchors already serve the purpose. Contraposition remains a later lesson.

Distinguish source from convention: the must relationship is logical implication; left-to-right is this course's drawing convention. A differently oriented arrow could represent implication if labels and direction were deliberately arranged accordingly, but this course consistently uses sufficient left and necessary right. The rule alone does not assert either condition. Do not copy the video's loose rule-disappears metaphor.

No additional app changes in this comparison pass. Current arrow draft is implemented and tested, pending Joshua's wording review.
