Adds consistent GSAP entrances, scroll reveals, moving sidebar selection, and mobile panel transitions across student, Practice, Progress, Reading Center and teacher navigation. The reveal matches the current LexPrep section preset, with bounded async readiness, stable heading/item identities, reduced-motion support and active-session exclusions.

Validation: 277 relevant tests, typecheck and production build passed. Real signed-in browser verification covered major navigation, LR/RC, scrolling, mobile panels and 320/390/768/980/1440px widths. Two Claude Opus comparison rounds completed; the final refinement was approved with four low-priority polish notes. Static review does not replace the host's browser checks; rare teacher editor/payment states and active student sessions were not exercised to completion.

Local evidence and detailed coverage are recorded in docs/verification/platform-motion-20261022.md. No backend or student-data migration is included.
