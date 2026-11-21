# Lumen

Daylight study space. A near-white foundation and dark top rail hold together an illuminated primary task, editorial coach note and compact seven-day planner. Sage appears only in the study surface, selected dates and quiet progress; ink remains the action colour. No exam countdown.

## Sources actually consulted

- Original creative brief in the 614486b3 Claude handoff attachment.
- Rendered Lamplight student desktop screenshot and original student dashboard handoff screenshot.
- Root's rendered-reference findings in `research/2026-10-23-dashboard-next-directions/references.md`, especially Sunsama's finite daily plan, 21st's restrained navigation indicator, and Recent's local filters. I did not independently operate those live reference sites.
- Installed design-resource-library, design-taste-frontend (selective, current brief takes priority), gsap-core, gsap-timeline and gsap-performance guidance.

## Interactive pieces

Work filters, selecting a task into the main study surface, reading and replying to the coach note, session preparation checkboxes, selecting days, and practice time dialog. Actions are simulated; reply text is a local unsent draft and is not persisted across reloads. Global navigation leads to related regions within this prototype rather than app routes.

## Visual verification

Rendered in actual headless Microsoft Edge through Playwright at 1440 and 390px. Personally inspected both full-page screenshots and natural-animation frames 1 and 3. No horizontal overflow or page errors. Main CTA bottom at 600px desktop / 630px phone, within the initial 844px phone screen. Verified RC filter returns one row, row selection swaps the hero title, note and preparation expansion, practice dialog open and Escape close. Static reduced-motion heading visible. Four natural timed frames show GSAP's clock advancing 0.143 to 1.61 seconds; hero finishes within about 1.1 seconds with no forced timeline completion.

Evidence: `artifacts/checks.json`, `artifacts/student-1440.png`, `artifacts/student-390.png`, `artifacts/motion.json`, `artifacts/motion-*.png`.

Not a complete keyboard, screen-reader or device performance audit. Sample data is visual context. Backend integration is outside scope.

Local Newsreader / Manrope font files retain OFL notices. GSAP is copied locally from the prepared design lab. No CDN or network asset dependency.

Refinement: direct personal greeting, removed ghost initial, increased secondary contrast. Mobile rail uses a 14px-label Menu disclosure; opening and Escape dismissal verified. Refreshed screenshots after the changes.
