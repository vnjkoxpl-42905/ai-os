# Margin

A student dashboard prototype built around a broad ink-coloured work surface, a compact editorial masthead, and actual contextual annotations instead of a letter to read.

## Design synthesis
- Marginalia: Newsreader typography, italic supporting voice, numbered margin notes and hairline dividers.
- Lamplight: one strongly contrasted next-task surface and a quiet warm-white action. The focus object changes its interior when the student selects another task.
- Carrel: a restrained surface shadow and lower-right folded silhouette, without stacking physical props.
- Research: labelled dark top rail; selectable week strip; relevant teacher preparation rather than a distant test countdown; local LR/RC queue filters.

The underlying near-white and ink palette remains familiar. Moss/sage is the sole accent family. All fonts and GSAP are served locally. Font licences accompany the files. No account, live data, external CDN, or installation is needed.

## Files
- index.html: complete student layout.
- style.css / app.js: responsive styling, real prototype interactions and GSAP motion.
- lib/gsap.min.js: installed local GSAP copy.
- fonts: Manrope, Newsreader and OFL licences.
- artifacts: actual browser screenshots and test reports.

## Verification
Ran headless Microsoft Edge through the existing Playwright install at 1440x1000 and 390x844. Both document widths exactly match the viewport, with no page errors. Inspected actual full-page captures at both widths, then refined mobile title wrapping, CTA containment, note width and text spacing. The primary mobile CTA is y518, height49, wholly within the initial viewport.

Clicked teacher note, closed it, selected Saturday, selected the guided task, and checked the RC filter. Keyboard tests confirm the skip link is first, Enter opens the note dialog, Escape closes it and focus returns to its opener. The mobile menu opens. Reduced-motion viewport matches its media preference and contains zero GSAP animations.

Natural task-swap screenshots were sampled at 0, 100, 250 and 500 ms. Independently inspected the 100 and 500 ms frames: persistent shell stays still while the interior fades/translates to the selected work. This proves the sampled states, not frame-rate smoothness or an exhaustive keyboard/screen-reader audit.

No sample data is persisted, practice screens are intentionally explanatory dialogs, and these files do not alter the application.
