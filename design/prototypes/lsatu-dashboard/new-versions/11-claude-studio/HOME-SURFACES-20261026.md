# A distinct role for each homepage surface

2026-10-26. Local implementation complete. Final independent Claude approval remains outstanding: the last small corrections were host-tested after the two-inspection budget was used. Do not describe the final stylesheet as Claude-approved.

[Open current Home](index.html) · [Compare before and after](surface-comparison.html) · [Open the preserved before-version](reviews/home-surfaces-before-20261026/index.html)

## What changed

- Full-bleed neutral ground distinguishes the content from the shell, including1920px gutters. Charcoal/off-white remains the palette.
- The resume workspace keeps its original geometry, artwork and light edge, with a shorter ambient shadow.
- Assignments form the single primary off-white sheet, with aligned numbered rows, a contained current-row wash and a crisp border.
- Coach/session form one quiet flat rail, separated by a rule instead of two independently floating cards.
- Calendar is frameless; its agenda uses a simple dividing rule. Day selection, visible hover/focus and enlarged-text wrapping remain intact.
- Baseline text sizes are preserved; ledger numerals and rail metadata use stronger neutral contrast. Headings line up at tested desktop, intermediate and phone widths.

Only stylesheet refinements were made to runtime. The complete baseline stylesheet remains an unchanged prefix; added component rules are Home-scoped, with Home-route-guarded html/body ground exceptions. HTML/JavaScript, font files and assets are unchanged. No card wrappers, features or production integration were added.

## What was checked

-27settled layout/capture cases, including1366user-scale,1920wide,1440/1048desktop,700/800intermediate and390/320phone, plus enlarged text and DPR2.
-20calendar internal-text-bound cases over10widths at normal/200% root text.
-13interaction groups passed before the final CSS-only geometry corrections. Affected layouts/surfaces/calendar bounds were rerun after those corrections; HTML/JS remained unchanged.
-9non-Home route/role style samples matched their saved pre-change values exactly. Home DOM/card counts also match.
-Rendered screenshot pixels measured assignment-sheet/ground separation4.8205L*. Rail metadata contrast4.9619:1;12scoped metadata/action/numeral samples passed4.5:1.
-Five heading x-alignments and a real calendar-strip hover edge change passed.
-Desktop rail bottom-band measurements were0px at1366 and1440, with empty and saved prep notes.
-Readable1366/1048desktop,390phone and1920wide renders were directly viewed by the host. The reviewer did not claim browser or visual inspection.

Proofs, screenshots, scripts and final hashes: [artifacts/home-surfaces-20261026](artifacts/home-surfaces-20261026/). The interactive before-version includes its own local assets and remains independently openable.

## Claudex loop record and limits

Codex planned/built; Claude Code2.1.309 independently reviewed the plan and inspected source through fresh CLI sessions. Requested model/effort: claude-opus-5-5 / medium; completed results observed claude-opus-5-5. Five plan rounds ended APPROVED. The two implementation inspections each returned REVISE, not approval.

The first inspection's text-size, edge, preview-rule, alignment and hover findings were corrected. The second identified remaining resume geometry outside the narrow plan scope, plus lower-priority finder/rail questions. Final host corrections restored original resume border/ring/padding behaviour and gave the finder a clearly raised white resting surface. The possible rail band was tested in four desktop states and measured0px, so no speculative layout change was made for it. Updated browser proofs pass. These final corrections have not had another independent inspection.

The [claudex-loop skill](../../../../../.agents/skills/claudex-loop/SKILL.md) says: "If the inspection budget is exhausted, report remaining findings and unreviewed edits explicitly for the user's decision." The configured two rounds are exhausted; no third approval was invented or silently run. Review history is in [reviews/home-surfaces-20261026](reviews/home-surfaces-20261026/) and the append-only archive review log.

No full accessibility/contrast certification, current signed-in production comparison, old-browser compatibility proof, publication, commit or push. Synthetic local data only. User visual acceptance remains pending.
