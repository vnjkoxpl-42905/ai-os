# 10: Type refinement

Built 2026-10-25. [Open version10](index.html), [compare preserved09](../09-focus-studio/index.html), or [browse all27 archive entries](../../index.html). Local server preview: http://127.0.0.1:5201/#home while the server remains running.

This implements Joshua's Impeccable/font-guidance cleanup of the rejected09 typography, including the selected mixed-platform keyboard badge. The existing paper/ink family, Home/sidebar architecture and working demo features remain.

## What changed

- Manrope carries task titles, navigation, controls, messages, dates and metadata with consistent weights. Newsreader is reserved for main page headings.
- Body text is1rem; metadata is13px equivalent on desktop and14px on phone. Tracked mono capitals, italic greeting/name styling and a redundant italic announcement were removed.
- The finder shows Ctrl K on Windows or Command-K notation on Apple platforms. Optional hints hide on narrow/touch layouts. The shortcut matches its advertised modifier and leaves open dialogs untouched, preserving unsaved text.
- Labels and buttons reflow as whole units; assignment words stay intact, calendar columns respond to text size, and sidebar width grows with enlarged type. Chips, dots and avatars scale with text.
- Enlarged teacher tables scroll within a keyboard-focusable labelled region rather than widening the page. All columns and actions remain available.

The [brief](BRIEF.md) records the saved25-tip resources and official Apple typography/accessibility/keyboard references. These are selective web applications of legibility and hierarchy principles, not a claim of native Apple compliance. Existing licensed fonts were reused without downloads or new dependencies.

## Current verification

**Claude round4: APPROVED, zero findings.** Read the [full verdict](reviews/round-4.json), [review log](REVIEW-LOG.md), [source hashes](reviews/round-4-source-hashes.json) and artifacts/proof-summary.json. Runtime hashes were checked unchanged after approval. Earlier verdicts and rejected-state captures remain in reviews/.

Host checks passed:13 interaction groups,21 feature groups, platform-specific shortcuts, student/teacher/dialog layouts, enlarged text, nav containment, whole assignment words, local-table keyboard reachability and avatar containment. Exact1048x858, phone, tablet and enlarged-text captures were inspected. The capture report contains21 cases, plus a supplementary exact-viewport screenshot. The reviewer read source/static images, not a live browser, and did not run tests or measure contrast. No complete contrast certification or production acceptance is claimed.

One offline exact-lookup run timed out; the cause was not confirmed. Four fresh file/offline contexts then passed, plus another check after the final avatar CSS change. The latest report records a genuine pass, and offline-investigation.json preserves the earlier failure and diagnostic limits. Do not call this a proven runtime-race fix.

All people, assignments, dates, questions and results are synthetic fixtures. Notes and drafts use browser-local storage; nothing is sent or assigned to a real account. No production application was changed or published.