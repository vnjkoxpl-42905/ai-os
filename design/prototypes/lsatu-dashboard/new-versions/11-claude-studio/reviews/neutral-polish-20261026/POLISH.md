# Version 11 neutral polish: review and disposition

2026-10-26. Work order: `CLAUDE-11-NEUTRAL-POLISH.md` (SHA256 552b83fe…71d2). Candidate replacement for `11-claude-studio/style.css`. Not yet integrated, browser-checked or visually approved.

## Author

Requested as Claude Opus 5.5, medium effort. The runtime reports its model as `claude-opus-5-5`; the effort level was not observable from inside the session, so "medium" is the requested flag, not a confirmed one. Claude designed the original version 11. This is a second pass by the same model family, not an independent review of that design.

## What was actually reviewed

- `11-claude-studio/style.css`, read in full (457 lines, current neutral values).
- `11-claude-studio/app.js` lines 50 to 81 (Home markup: desk head, resume, statement track, coach, session, ledger, week) plus targeted searches for feedback, answer-strip, error and guard markup.
- `artifacts/neutral-1048.png` and `artifacts/neutral-390.png`, viewed. The navy/gold `home-*` and `final-preview-*` captures were deliberately not used.
- `VERIFICATION.md` in full (palette correction, prior host checks, the open cosmetic finding).
- `design/README.md` router only. No further design-hub files were needed.

Not done: no browser run, no screenshots of the candidate, no contrast measurement tool, no other routes viewed as images. Subpage findings below come from source reading only.

## Findings and decisions

1. **Home took too long to reach the work at 1048.** Below 1100px the finder and the three quick actions stacked under the greeting, so the head used about 300px before the resume card, and the assignment ledger sat two screens down. *Changed:* at ≤1100px the finder and quick actions share one wrapping row (`flex:1 1 16rem` / `1 1 22rem`). At 1048 they fit side by side; at 390, or at 200% text, they wrap back to the current stacked layout. Desk-head bottom margin 26→22px, dateline and h1 gaps tightened by 2px each, resume padding and heading margins tightened by 2px. The hero keeps its size, art and character. A reorder (ledger above coach/session) was considered and rejected: it would need `display:contents` on the labelled `.desk` section, which risks dropping its accessible name.

2. **Two effects on the resume card read as metal or glow.** The 3px top bar ran a lamp→brass gradient, and the Continue button had a pale bloom under it. *Changed:* the top edge is now a 2px off-white hairline that fades out. The button gets a tight dark drop shadow and an inner bottom edge instead of a light halo. Same off-white key on charcoal, no blur.

3. **Several state pairs differed only by near-identical tints.** The neutral correction mapped "right" and "missed" to `#e7ebe4` vs `#e9ece5`, and errors to the same family as ordinary notices. Text and glyphs still told them apart, but visually they merged. *Changed, palette unchanged:*
   - Missed answer-strip chips: white fill, ink-2 border, bold. Correct chips stay soft.
   - `.result-label.missed` uses ink, so it is darker than a correct label.
   - `.feedback`: 3px left edge, grey for "Look again", ink for "fits the reasoning".
   - `.error` and `.guard`: 3px ink left edge, ink text, weight 600. The greenish `#374b3b` text is gone.
   - `.count.is-new` ("1 new"): ink and bold instead of a grey that matched "All read".
   - Statement track `.next` (both themes): numeral weight 800, and on light surfaces an ink ring instead of the mid-grey one. Five done, six next, twelve cells and auto-fit wrapping are unchanged.

4. **The focus ring had a green cast.** `--focus` was `#465a49`. *Changed* to near-ink `#2c322d`, which is neutral and gives higher contrast on linen and sheet. On the charcoal resume card the ring uses `--lamp-2` (off-white).

5. **Hover states were uneven.** Tabs changed fill but not border or text. Pressed tabs had no hover response. Inputs, review chips and the reference-fields summary had no hover at all. *Changed:* these now use the same neutral grey border, white or `--night-3` fill and ink text as the base button hover.

6. **Small inconsistencies.**
   - At ≤380px the current-assignment rule sat at `left:-18px` while the card padding was 16px, so it poked 2px outside the card. Now `-16px`.
   - `.ledger-no` numerals `#7e877a` → `#6c7469` for steadier contrast on sheet.
   - `.question-tools` pressed state: ink-2 border and ink text instead of a mid-grey pair.
   - The phone mobile bar gets a faint neutral bottom shadow so content scrolling under it reads as underneath. No blur.

7. **Open cosmetic from VERIFICATION.md: the session dot sometimes sat on its own line in the seven-column week.** *Changed:* in the ≤1279px media block, `.day-note` is `display:block` and the dot is `inline-block`, so it flows with the first word. This mirrors what the calendar container query already does. Nothing is hidden or clipped. **The host should recheck calendar internal bounds**, since this touches the calendar.

## Left alone on purpose

- Newsreader headings, Manrope work text, the type scale, font files and asset paths.
- The resume card, its art and the overall layout.
- Sidebar, drawer, dialogs, the scrollable teacher table and reduced motion.
- The calendar container queries at the end of the file are byte-for-byte unchanged: `.week` inline-size container, the 36rem list threshold and the 12rem note-row threshold.
- The phone quick-actions row, where Inbox wraps alone at 390. Forcing three columns would split "Timed section" across two lines. The wrap is honest, so it stays.
- LR and RC chips stay near-identical in tint, because their text labels carry the meaning.

## Palette commitment

No new colour values outside the existing charcoal, off-white and neutral-grey family. No gold, brass, navy, blue, claret, orange or apricot hues, no metallic gradients, no new coloured chips, no backdrop blur. The historical variable names keep their current neutral values. A comment in `:root` now says so.

## Limits

- No browser verification by the author. Host captures at 1440, 1048, 390 and 320, with enlarged text and calendar bounds, are still required.
- The `.day-note` change in item 7 and the head-tools row in item 1 are the two layout-affecting edits. Everything else is colour weight, border or spacing within existing tokens.
- `app.js` and `index.html` were not touched. The stylesheet assumes their current markup.
- No user visual approval is claimed.
