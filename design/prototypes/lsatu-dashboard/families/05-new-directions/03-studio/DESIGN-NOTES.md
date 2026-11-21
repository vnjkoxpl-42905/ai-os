# Studio: a composed study workspace

## Intent
Retain the near-white and ink foundation; let a muted sage express structure and material depth. A dark top rail provides the familiar navigation rhythm Joshua preferred. The central folio borrows Carrel's paper layering and deadline stamp, while removing the competing envelope, clock, ticket and spiral objects. Marginalia contributes considered serif hierarchy and quiet rules. Lamplight contributes one dominant task surface, not its literal lamp.

The queue stays visible as three numbered tabs below the sheet. The coach note and next-session preparation form a narrow, aligned supporting column. A compact seven-day strip preserves the original dashboard's clarity. A daily study budget replaces the exam countdown.

## Actual references used
- Visually inspected prior `carrel-student-1440.png`, `lamplight-student-1440.png`, and original `student-dashboard.png`.
- Read the user's original three-directions brief at `C:/Users/Joshu/.codex/attachments/614486b3-1ac4-49fb-848c-b0e275f72813/Pasted text.txt`.
- Read the parent research `C:/Users/Joshu/dev/ai-os/research/2026-10-23-dashboard-next-directions/references.md`: Sunsama daily workload grouping and estimates inform the study budget. 21st tab-state principle informs a single active line under the task choice. This worker did not independently operate those external websites.
- Consulted design-taste-frontend as optional restraint/materiality guidance and gsap-core for transitions. Preset framework/font restrictions were not adopted over the explicit standalone brief and existing editorial identity.

## Verification actually performed
- Headless Microsoft Edge via installed Playwright.
- Desktop 1440×1050 and mobile 390×844, full-page screenshots opened and visually inspected. Increased supporting type after first inspection. Re-rendered and inspected both final layouts.
- No horizontal overflow, no page script errors at either width.
- Primary Continue fully inside initial viewport at both widths.
- Assignment swap, day selection, coach dialog and close, mobile menu / Practice destination exercised.
- Reduced-motion 390px context confirms immediately visible work (opacity1) without entrance animation.
- Keyboard first Tab confirms skip link. Native dialog supports focus/escape. This is not a complete accessibility certification.
- Natural GSAP clock advanced .314→.597→.881 seconds; work opacity .8478→.9987→1. No timeline seek or forced finish. Natural-frame screenshots recorded. This establishes playback and state progression, not quantitative frame pacing.

## Files
`index.html`, `style.css`, `app.js`; local GSAP `lib/`; Manrope and Newsreader fonts with OFL licences `fonts/`. `verify.cjs` and `motion.cjs` reproduce bounded checks, with JSON reports and screenshots alongside.

All actions are interactive sample-data previews, not backend-connected. Global destinations show a clearly labelled preview or scroll to an applicable section. No live app files, existing v2 designs, shared configs or deployment altered.
