Current homepage status, 2026-10-26: see [surface hierarchy changes and review limits](HOME-SURFACES-20261026.md). [Before/after comparison](surface-comparison.html). Earlier statuses below are historical.

Current status, 2026-10-26: **charcoal and off-white**, with the Claude neutral polish applied. See [latest review and proof](POLISH-20261026.md). Earlier palette descriptions and verdicts below are historical.

# 11 · Claude studio

2026-10-25. Local design study for the LSAT U student dashboard, built by Claude (Opus 5.5) from the work order `CLAUDE-11-WORK-ORDER.md`. Standalone HTML, CSS and JS. No build step, no network, no account.

## The direction: a reading room with one lit desk

Version 10 was rejected as bland, flat, too white and blurry. This version answers with material and contrast rather than more paint.

- **Ground and sheets.** The page is warm linen (`#ebe5d9`) with a faint paper grain. Every working surface is an opaque paper sheet (`#fcfaf5`) with a crisp hairline and a short, soft drop shadow. No backdrop blur anywhere, including the dialog backdrop.
- **One lit desk.** The resume card is night ink (`#161d2b`), not near-black green. A parchment lamp tone (`#f1d594`) does three jobs only: the Continue button, the filled statement cells, and a thin lit edge along the top of the card. The paper-landscape image sits in the right half at luminosity blend, masked, so it reads as texture behind the desk, never behind text.
- **The next action is the work itself.** The resume card shows the actual next statement, "Some of the books are illustrated.", in serif, with the instruction under it and a numbered 12-cell track (5 filled, 6 outlined as next). Continue names its target: "Continue at statement 6".
- **Two inks, not orange.** Logical Reasoning is ink blue and Reading Comprehension is claret, each a tinted chip with a matching inset line. Claret also marks the unread state and the active navigation item. Brass marks progress and the in-progress assignment. Apricot and orange are not used.
- **Type.** Newsreader carries the page title, card titles, the coach's note, the session time and question passages. Manrope carries the interface at 15 to 16px. Plex Mono appears only where a reference is an identifier (PT 155 · Section 1 · Question 1, the typed-reference field, answer-strip buttons, `kbd`). Labels are sentence case at 14px, not tracked uppercase.
- **Motion with a reason.** Page sections rise in a short stagger when you arrive on a route. The completed statement cells fill one after another and the next cell lands last, so the saved place is the thing that moves. Changing the selected day swaps the agenda with a short slide. Dialogs and the phone drawer ease in. Navigation never animates. `prefers-reduced-motion` removes all of it.

## What changed substantially from 10

| Area | Version 10 | Version 11 |
|---|---|---|
| Palette | Sage green and grey on off-white | Linen ground, opaque paper sheets, night-ink desk, parchment lamp, blue and claret subject inks |
| Shell | Floating bordered sidebar card | Full-height linen rail, active item as a lifted sheet with a claret edge |
| Home hero | Greeting left, small dark card right | Greeting with a one-line plain summary; the dark desk card is the largest object on the page and previews the actual next statement |
| Progress | 12 thin dashes | 12 numbered cells, distinguishable by fill, outline and numeral |
| Coach note | Sans quote in a small panel | Serif note with a claret margin rule, task link underlined in claret |
| Session | Date tile and small text | Large serif 7:15 p.m. with day and duration, preparation as a secondary button |
| Assignments | Plain rows | Numbered ledger (01 to 04), brass marker and meter on the in-progress row, header link to My Work |
| Week | Seven bordered tiles | Vertical day list beside the ledger on wide screens; seven columns in mid widths; list again on phones |
| Dialog backdrop | 3px blur | Solid ink tint, no blur |
| Escape in a dialog with unsaved text | Closed and discarded | First Escape shows a notice; second closes. Unsaved note and rewrite text are kept in memory and restored on reopen |

## What I borrowed, and from where

- Charcoal next-action card with one clear Continue: Lamplight, Margin, Refined (adoption report priority 1).
- Paper-landscape art inside the compact card: 07 Atmosphere, kept out from behind text.
- Numbered rows and serif hierarchy: 02 Margin. Contextual note linked to a task: Marginalia.
- Large session time with duration: later 05 Studio passes.
- Reference console, saved and recent questions, LR/RC controls in Practice: 05 and 06 Studio.
- Warm paper and a light rail with a contrasting dark Continue: the canonical app Home source (`ClassroomHomeView.tsx`, `home.css`). I kept the principle and dropped the orange.

## Behaviour carried over from 10

`app.js` is adapted from version 10. Home markup and the shell were rebuilt; other views keep their logic with new markup classes.

- Routes: Home, My Work, Practice, Review, Progress, Library, Reading Center, Messages; teacher preview and student roster through the workspace switcher.
- Resume dialog for Negation Station with sample-answer comparison. Assignment previews never change the resume task.
- My Work subject, status and title filtering.
- Practice: typed exact reference (`PT155 S1 Q1`, `155 / 1 / 1`, `PrepTest 155 Section 1 Question 1`), separate fields, sample reference buttons, search, All/Saved/Recent and subject filters. Unknown references say so and never substitute a different question.
- Question page with bookmark, answer check, hints and retry.
- Review answer strips and rows open the exact matching question.
- Coach note with Reply (to the Messages draft) and Mark as read; local reply draft with dirty, saved and failed states.
- Session preparation note saved locally, with preview on Home.
- Ctrl K / ⌘ K opens the finder, but never while a dialog is open.
- Labelled native dialogs, focus return to the trigger, Escape, phone drawer, skip link, focus moved to each page title with a route announcement.
- Day selector is a tablist; arrow keys on either axis, Home and End.

## New behaviour in 11

- **Escape guard.** Any dialog textarea marked `data-saved` is compared with its saved value. If it differs, the first Escape shows a notice and keeps the dialog open; typing clears the notice; a second Escape closes.
- **Draft retention.** Closing the preparation dialog with unsaved changes, or the resume dialog with a rewrite, keeps that text in memory. Reopening restores it and says so. It is not written to storage until you save. The teacher assignment draft stays dialog-only, as in 10, and the guard says it will be discarded.

## Local and synthetic limits

- Every person, assignment, session, message and result is sample data. The five questions are original synthetic items labelled as such; their PT references demonstrate lookup only.
- Nothing is sent, assigned or submitted. Drafts and notes stay in this browser under `localStorage` key `lsatu-claude-studio-v1`, separate from 09 and 10.
- Smart Drill and Timed section open one sample question; they do not generate a drill or start a timer.
- No signed-in capture of the live lsatprep.study dashboard exists for this task (unauthenticated `/classroom` redirects to `/auth`). This study does not claim to match or beat production.

## Files

Authored in this directory: `index.html`, `style.css`, `app.js`, `README.md`.

Required from the host (copied unchanged from `10-type-refinement/assets/`): `assets/fonts/manrope.ttf`, `newsreader.ttf`, `newsreader-italic.ttf`, `mono.ttf`, their OFL licence files, `assets/paper-landscape.png` and `assets/manifest.json`. No other assets are referenced. The page also uses an inline SVG noise texture and no external URLs.

## Fix round 1 (2026-10-25): enlarged text

Host checks at 200% root text found two layout defects. The design is otherwise unchanged.

1. **Home tools overflowed the page at 390px and 320px.** `.head-tools` now has one contained track (`minmax(0,1fr)`). The finder label can wrap instead of being held on one line. Quick actions are a wrapping flex row: each control keeps its natural width and moves whole to the next line when the row is full, and a label wraps inside its control only when one control is wider than the column. The fixed two-column phone grid for quick actions is gone. Nothing is hidden, clipped or shrunk.
2. **Statement cells squeezed their numerals.** The track had a fixed 12 columns. It now uses `repeat(auto-fit, minmax(1.75em, 1fr))`, with the em measured from the numeral size, and cell height in em. At normal text, all 12 cells still sit on one row. At enlarged text, the sequence 1 to 12 wraps onto further rows in reading order. The five done cells and the outlined statement 6 keep their styling in both the dark resume card and the light Progress card, which share the same rule. The phone sizes now change the track's font size rather than fixed cell heights.

## Fix round 2 (2026-10-25): week card at 320px, 200% text

The host found that the Home page was 376px wide at 320px with 200% text. The single-column `.desk-lower` track used `1fr`, whose automatic minimum let the week card grow to fit the day rows' natural width. That widened the assignment card with it.

- `.desk`, `.desk-lower`, `.days` and every `.day` track now use `minmax(0,1fr)`, so a card never grows wider than its column.
- In the list layout, the day-note column is `minmax(0,1fr)`. The note itself (`Session 7:15`, `No session`, `Today`) wraps by whole words onto a second line when the row is short of room.
- No content is clipped, overflow is not hidden, and type sizes are unchanged. No JS changes.

## Verification

- **Not run:** `node --check design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/app.js`. The shell call was denied by the session's permission layer, so I have no syntax-check output. I re-read the template literals and handlers by hand; that is not a substitute for the check.
- **Not run:** any browser render, screenshot, contrast measurement, overflow check or keyboard test. The assets directory was not yet present in this checkout, and no server or browser was started.
- Host verification after the first build (reported to me, not run by me): syntax check passed, 21 feature groups passed, and an independent review of all four files plus route and layout cases found only the two enlarged-text defects above.
- Fix round 1 was a CSS-only change. I did not run a browser or measure the result; the host recaptures 200% text at 390px and 320px.
- Fix round 1 then passed host checks at 320px and 390px, at normal and 200% text.
- Fix round 2 was CSS only and matches the containment a fresh reviewer verified in the browser. I did not render or measure it myself.
- Contrast values were chosen against the intended pairs (for example muted `#575c68` on sheet `#fcfaf5`, and the lamp button's night-ink text on `#f1d594`), but they are not measured here.


## Host verification and final integration

See [VERIFICATION.md](VERIFICATION.md) for host-run browser results, the narrow Codex calendar compatibility fix, independent-review limits and the remaining cosmetic note. [Compare09/10/11](comparison.html). The earlier builder proof limitations above are preserved as historical statements.


## Palette correction, 2026-10-26

Joshua reaffirmed charcoal and off-white. Navy, gold, claret and blue accents were replaced with charcoal, off-white and muted neutral shades across default/hover states, progress, chips, notices, sidebar and dialogs. Layout, fonts and JavaScript remain unchanged. The previous stylesheet is preserved in reviews/initial-navy-gold-style.css. Earlier review verdicts describe the earlier stylesheet; this correction is separately browser-checked.
