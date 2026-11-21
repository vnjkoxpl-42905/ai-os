# Conditional opening needs keyboard and contrast repairs before release

## 2026-10-03 repair checkpoint supersedes the findings below

Joshua authorized the recommended repairs. All five original findings are now resolved in the local preview: stable keyboard focus, measured label contrast, 44px lesson targets, semantic tokens for the audited visuals and two flattened nested structures. Bounded re-audit: **16/20**, with broader device, screen-reader and performance acceptance still open. [Repair evidence and limits](visual-proof/voice-application/2026-10-03-impeccable-repairs/README.md). The original 12/20 audit below remains the historical baseline; its statement that no application files changed applies to that read-only audit.

Audited2026-10-03. Scope: current local opening preview, orientation and supplementary sufficient/necessary, Group1 and Group2 units. Technical audit only. No application files changed. The prior174-test/build checkpoint verifies functional integration, not complete accessibility or design compliance.

## Anti-pattern verdict: fail on remaining nested frames

The interface has a distinctive teaching-room identity, with no observed gradient text, glass default or hero metrics. However, the construction area and family explorer retain redundant frames within frames. These fail Impeccable's nested-card rule. This is a specific structural finding, not a claim that the whole interface looks generic or AI-generated.

## Audit health score

| Dimension | Score | Key finding |
|---|---:|---|
| Accessibility |2/4|Keyboard focus is lost at construction completion; several labels miss contrast target.|
| Performance |3/4|Reference connector uses transform; route remains a roughly202KB JS/67KB CSS artifact. Real-user performance is unmeasured.|
| Responsive design |3/4|Four opening units reflow at narrow width; several secondary targets remain below44px height.|
| Theming |2/4|Scoped tokens coexist with active hardcoded teaching-visual colors.|
| Anti-patterns |2/4|Two remaining nested-frame structures.|
| **Total** |**12/20**|**Acceptable: significant work remains.**|

Scores are bounded audit judgments, not certification. Total5 consolidated issues: P0=0, P1=2, P2=3, P3=0. No task-completion blocker found. Physical-device, complete screen-reader and production performance acceptance remain unverified.

## P1: construction completion drops keyboard focus

- Location: [ConditionalReferenceSequence.tsx:124](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/ConditionalReferenceSequence.tsx:124). Similar disappearing reset/clear controls occur at19,71 and148; only final construction was reproduced in this audit.
- Category: Accessibility.
- Verified: Enter on Find the indicator, Draw the must arrow, Place the complete target and Fill the remaining condition completes the construction. The final focused button unmounts. activeElement becomes BODY; the next Tab reaches the preview's first orientation button rather than the nearby reset/next interaction.
- Impact: Keyboard learners lose their position within a long lesson and must recover navigation. Production chrome differs, so its exact next focus target is not claimed.
- Standard: Focus continuity and logical navigation, relevant to WCAG2.4.3; no formal conformance ruling from this bounded test.
- Recommendation: Keep a stable completion control mounted or explicitly focus the completed diagram/readback or adjacent reset control. Audit equivalent clear/retry actions together.
- Suggested command: `$impeccable harden`.

## P1: small instructional labels still have insufficient contrast

- Locations: [reference-sequence.css:20](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/reference-sequence.css:20), [reference-sequence.css:21](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/reference-sequence.css:21), [opening.css:11](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/opening.css:11).
- Category: Accessibility.
- Verified: Four-case ordinal labels measure3.60:1 on selected mint and4.13:1 on unselected fill. The14px Our diagram label, rgb106/123/97 on the writing-sheet paper rgb250/248/239, measures4.27:1. Group1/2 expression numbers measure4.10 to4.25:1 and render at12px on the narrow layout.
- Impact: Low-vision readers have less legible labels. The diagram label is instructional text. If ordinals are purely decorative, mark that intention semantically; their decorative exemption must not be extended to instructional labels.
- Standard: [WCAG1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) requires4.5:1 for ordinary text, with large/decorative exceptions.
- Recommendation: Use the darker scoped muted/ink role for readable labels and hide genuinely decorative numbers from assistive technology where appropriate. Recheck default, selected and alternate chapter fills.
- Suggested command: `$impeccable harden`, then `$impeccable colorize`.
- False positive excluded: The overview set labels sit over light SVG rectangles. An ancestor-background-only scan incorrectly reported1.2:1 against the dark section; these labels are not counted as failures.

## P2: secondary touch targets are shorter than the44px product guideline

- Locations: [opening.css:19](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/opening.css:19), [opening.css:11](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/opening.css:11).
- Category: Responsive design.
- Verified: Start with the meaning / Begin reading links are24.5px high across all4 units. Orientation's Two more Group1 expressions and More Group2 forms disclosures are42px high.
- Impact: These targets are less forgiving for touch than the main practice controls.
- Standard: Impeccable44px guideline. This is not automatically a [WCAG2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) failure, which uses a24px baseline and exceptions.
- Recommendation: Expand the activation area with block padding/min-height while preserving the restrained link treatment.
- Suggested command: `$impeccable adapt`.

## P2: token coverage stops before several active teaching visuals

- Locations: [reference-sequence.css:15](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/reference-sequence.css:15), lines16,20,21,24; [opening-polish.css:168](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/opening-polish.css:168); [ConditionalOpeningMedia.tsx:71](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/ConditionalOpeningMedia.tsx:71).
- Category: Theming.
- Verified: Enough/required exhibits, family-reading pane, case fact, diagram, writing sheet and practice legend retain hardcoded colors. The active overview SVG retains hardcoded fills/strokes. The polish layer changes several borders/radii without replacing each background.
- Impact: A room-palette change requires multiple stylesheet/markup edits and can reintroduce contrast inconsistencies.
- Standard: Impeccable scoped token consistency. The approved light-paper teaching room itself is intentional; absence of an app-wide dark theme is not filed as a defect.
- Recommendation: Name semantic exhibit roles and route active surfaces/SVG fills to the room token system. Preserve their teaching distinctions.
- Suggested command: `$impeccable document`, then `$impeccable colorize`.

## P2: redundant nested frames remain in two interactions

- Locations: [ConditionalReferenceSequence.tsx:121](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/ConditionalReferenceSequence.tsx:121), lines67 to70; [reference-sequence.css:21](C:/Users/Joshu/dev/ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/components/reference-sequence.css:21); opening-polish.css148 to164.
- Category: Anti-patterns.
- Verified: Construction nests bordered/rounded cr-writer, cr-writing-sheet and cr-diagram. The family explorer nests its outer panel and tinted rounded reading pane.
- Impact: Redundant boundaries compete with the meaningful separation of sentence, diagram and explanation.
- Standard: Impeccable nested-card prohibition.
- Recommendation: Keep the paper/diagram affordance but remove a redundant outer border/background layer. Keep controls and explanations visibly associated.
- Suggested command: `$impeccable layout`.

## Systemic pattern

The polish overlay repaired the highest-visibility orientation styles while older live styles continue underneath. Remaining contrast, small labels and hardcoded visual colors cross both layers. Resolve semantic roles in the owning styles rather than adding another broad override file.

## What is working

- Native inline contents with real ordered anchors and location state, no floating overlay in this variant.
- Named question groups/fieldsets, pressed selection states, polite feedback and clear English explanations.
- No unnamed buttons in the orientation DOM; heading levels follow H1/H2/H3.
- Four units have equal document client/scroll widths at301px content width. A doubled root-font reflow probe also shows no horizontal overflow. This is not a substitute for actual browser200% zoom/full text-resize conformance.
- Reference paired practice stacks below900px and narrow symbolic choices use full width.
- Both manual/system reduced-motion handling remain present; connector keyframes now use transforms.
- Main dark kicker and selected-answer checks from the preceding polish pass measure8.91:1 and10.81:1. Broader scanning is what exposed the remaining label exceptions.
- No verified major performance defect from source inspection. The build route sizes are201,950 bytes JS and66,869 bytes CSS before compression; no production network/CPU/Core Web Vitals claim.

## Recommended action order

1. `$impeccable harden`: focus continuity and label contrast.
2. `$impeccable adapt`: secondary touch areas.
3. `$impeccable document` and `$impeccable colorize`: semantic token coverage.
4. `$impeccable layout`: remove redundant frames.
5. `$impeccable polish`: finish with a regression/visual pass, then re-run `$impeccable audit`.

You can ask me to run these one at a time, all at once, or in any order you prefer. Re-run `$impeccable audit` after fixes to see your score improve.

Audit artifact: opening-audit-measurements.json next to this report. Findings combine a read-only independent source audit and parent browser verification. No fixes, publication, paid action, commit or student writes performed.
