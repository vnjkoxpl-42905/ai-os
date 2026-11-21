# Plan: three top-tier versions of the "Next seven days" student strip

## Goal
Joshua rejected the current strip in `design/prototypes/teacher-home/home-mockup.html` (section `.studs.cal`, lines ~103-118) as too plain, flat and not the "Claude Design studio" feel he remembers. Deliver three distinct, more sophisticated directions, shown side by side in the real Home context, so he can pick one.

## Deliverable
- `design/prototypes/teacher-home/strip-versions/compare.html`: one self-contained page (inline CSS/JS, no CDN). It reproduces the Home mockup context around the strip (copy the mockup's tokens, grid and neighbouring widgets above it) and swaps the strip section between A / B / C with a segmented switcher (keys 1/2/3 also work). A "Side by side" mode stacks all three full-width for comparison. Remember the last choice in localStorage inside try/catch.
- `home-mockup.html` is not modified.

## Shared data (identical in all three)
Wed 18 (today): Lydia 3:00, homework done. Thu 19: Celia 1:00, homework half done. Fri 20: Zoë 5:00, homework done. Sat 21 to Tue 24: no session. Gone quiet: Ivory Chen 6 days, Avneet Singh 9 days, Dakota Reyes no session booked and homework not started. Header "Next seven days", range "Nov 18 to 24 · 6 students".

## Locked rules (from brainstorms/2026-11-18-teacher-side-visual-direction.md and memory)
- Near-white ground, one charcoal anchor (today), serif numerals, hairlines, at most one muted dot. Beige only as a faint streak, never a surface. No crayon colours.
- Status in one ink tone through shape and weight, never hue (homework done / half / not started = full, half, empty glyph + text).
- Studio lineage: `design/prototypes/lsatu-dashboard/new-versions/11-claude-studio/style.css` `.days/.day` (serif `day-num`, muted `day-name`, charcoal selected day with lamp text).
- Tactile 6B: restrained contact + ambient shadow, pressed state reduces shadow; visible keyboard focus.
- No em dashes in copy. Text never smaller than 12px.

## The three directions
- **A. Studio ledger, refined.** Faithful to the studio strip: 7 columns, serif numerals large (about 28px), hairline column rules instead of boxed cells, today as a raised charcoal tablet with a soft contact shadow. Session line shows student + time; homework shown as a small one-ink fill glyph. Empty days recede to a hairline and "Open".
- **B. Timeline rail.** A single horizontal hairline rail across the week with day ticks and serif dates beneath; sessions sit on the rail as pressed-paper tokens at their time-of-day height (time scale 9am to 9pm in a faint band). Today's segment is a charcoal band. Reads as an instrument, matching the eclipse hero.
- **C. Agenda cards with gone-quiet merged.** Booked days become three tactile session cards (avatar initial in a circle, name, time, homework glyph with label), empty days collapse into one quiet "Sat to Tue open" pill, and the gone-quiet students render as a fourth muted card set in the same row. Most information per pixel.

Each version: hover and pressed states on day/session items, focus-visible ring, and a <=820px layout that turns into a vertical list without horizontal scroll.

## Acceptance criteria
1. compare.html opens from file:// with no console errors and no network requests.
2. Switcher shows exactly one version at a time; Side by side shows all three; keys 1/2/3 work.
3. All three show the same data above; homework status is never conveyed by hue alone (grep CSS for status colours: only ink/mute/night/lamp tokens).
4. No horizontal page scroll at 375px wide; strip readable at 375 and 1280.
5. No em dash characters in the file.
6. Visually distinct: a reviewer can name each direction's layout from a screenshot.

## Verification
- `grep -c "—" compare.html` returns 0.
- Open in the in-app browser at 1280 and 375 widths; read console (expect none); screenshot each version; check `document.documentElement.scrollWidth <= innerWidth` at 375.
- Codex inspects the final file fresh.

## Non-goals
No LSAT U code, no real data, no changes to the rest of the Home design or the dock.

## Revisions after Codex round 1
- **Dock (STRIP-01):** compare.html omits the dock entirely. The comparison is about the strip; the dock is unchanged and out of scope.
- **Scoping (STRIP-02):** every strip style is scoped under `.sv-a`, `.sv-b`, `.sv-c`. The copied Week load widget uses its own `.wk-labels` class; no bare `.days`/`.day` selectors exist in compare.html.
- **Shared content (STRIP-03):** all three versions render from one JS fixture and each shows every session, homework status as glyph plus visible text label ("Done", "Half done", "Not started"), and all three gone-quiet students. A: a hairline "Gone quiet" ledger row under the columns. B: quiet students as muted tokens parked on a dashed "no session booked" lane beneath the rail. C: the fourth card set as specified.
- **Interaction (STRIP-04):** each session item is a `<button>` that opens a small inline detail line beneath the strip (student, time, homework status, "Open dossier" link to #). Enter/Space activate; Escape closes. Empty days are static text, not focusable, no pressed state.
- **Switcher (STRIP-05):** storage key `strip-compare-mode`, values validated against `a|b|c|all`, default `a`; switching works if storage throws. Number keys are ignored when focus is in an input/textarea/contenteditable. Switcher is a `role=tablist` with `aria-selected` synced to visibility.
- **Times (STRIP-06):** fixture start times are 24h: Lydia 15:00, Celia 13:00, Zoë 17:00; display "3:00 pm" etc. derived from them; B positions from these on a 09:00 to 21:00 scale.
- Acceptance criterion 4 now reads: no horizontal page scroll at 375px, with no clipped strip content.

## Revisions after Codex round 2
- **STRIP-07:** B's lane is labelled "Gone quiet"; each token shows its own fact (Ivory 6 days, Avneet 9 days, Dakota no session booked, homework not started).
- **STRIP-08:** the inline detail has no dossier link; it shows student, time and homework status only.
- **STRIP-09:** the switcher uses native `<button>`s with `aria-pressed`, not tablist roles. If a shortcut or switch hides the element holding focus, focus moves to the newly pressed switcher button. Verified from a session button in Side by side mode.
