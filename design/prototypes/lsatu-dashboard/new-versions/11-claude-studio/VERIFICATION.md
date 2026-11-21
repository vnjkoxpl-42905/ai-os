Current homepage status, 2026-10-26: see [surface hierarchy changes and review limits](HOME-SURFACES-20261026.md). [Before/after comparison](surface-comparison.html). Earlier statuses below are historical.

Current status, 2026-10-26: **charcoal and off-white**, with the Claude neutral polish applied. See [latest review and proof](POLISH-20261026.md). Earlier palette descriptions and verdicts below are historical.

# Version 11: what was actually checked

2026-10-25. Local synthetic prototype, not a production release. Open index.html directly or use http://127.0.0.1:5203/#home while the preview server is running. comparison.html links 09, 10 and 11.

## Authorship and model

Claude Code 2.1.309 designed and built the new HTML/CSS/JS/README with explicit `--model claude-opus-5-5 --effort medium`; completed results observed `claude-opus-5-5`. Claude also made two bounded enlarged-text fix rounds. Codex copied nine licensed local assets unchanged and hash-verified them, ran host checks, registered the archive entry and authored only the final calendar container-query compatibility rules. The palette/design direction is Claude's, not a claim that production was inspected or surpassed.

This was the user's explicitly requested standalone implementation work order, not an implementation of the earlier reviewed apricot-only plan. The main workspace was left intact; work was isolated in C:/Users/Joshu/dev/ai-os-projects/lsatu-design-11-claude. No commit, push, deployment, real message, assignment or account write occurred.

## Host results

- JavaScript syntax check passed.
- 13 inherited interaction groups passed: assignment/resume identity, focus return, drill/timed preview boundaries, subject filters, calendar/notes, replies/read state, finder, bookmarks, review, curriculum, teacher draft preview, mobile navigation and storage failure handling.
- 21 feature groups passed. Test selectors were adapted for numbered statement spans and day-name spans; the intentional two-Escape unsaved guard was tested rather than bypassed. Earlier failed old-selector runs are not runtime defects.
- Four direct-file offline/focus groups passed: Home/local fonts, exact reference, protected/restored unsaved modal text and reduced motion. These passed before the final calendar-only CSS change; no JS, fonts or offline asset paths changed afterward.
- Final 23 layout/capture cases passed at 1440,1048,768,390,320, including student routes at desktop/phone, enlarged text at1048/390/320 and a DPR2 capture. Animations were allowed to settle before captures. No detected page errors, missing HTTP assets or document overflow in those cases.
- Twenty additional calendar cases checked document and internal text bounds at320,360,380,384,388,390,641,700,720,1048, each at100/200% root text size. All passed; the narrow calendar switches layout based on its own width and text size.
- Final archive readback passed:28 entries, one Latest filter result, direct-file new-version loading and all three comparison images.
- Six prior 09/10 runtime hashes matched their pre-build values. All13 delivered source/asset files were copy/hash-verified before registration. Final runtime hashes are in artifacts/final-runtime-hashes.json.

The full interaction/feature checks preceded the final CSS-only compatibility correction. Final affected layouts were rerun afterward; unchanged behaviour tests were not gratuitously repeated. Capture scripts reference installed local Playwright and the temporary test server5202; adjust the server URL if rerunning against5203. Enlarged text means root font-size200%, not a certification of browser zoom or every OS text setting.

## Review coverage and deviations

The intended fresh Codex CLI inspection failed before review launch because MCP discovery failed. It is recorded as failed, not approved. Two separate native read-only Codex reviewers supplied fallback evidence: the first inspected all four authored files, compared10, viewed seven renders and ran64 student route/layout cases; the second rechecked the text fixes, teacher/student layouts and preparation dialog. They found the enlarged-text problems that were corrected.

After Codex took over the narrow compatibility CSS, a fresh Claude Opus5.5 medium artifact review independently inspected that host-authored change. Round1 requested stronger width-dependent handling; round2 APPROVED with no material findings. This is approval of the host integration fix, not independent Claude certification of Claude's own design. The reviewer read source and host measurements, did not run a browser and did not independently inspect production. Whole response records are preserved in reviews/.

One low cosmetic finding remains: the session event dot may sit on a separate line in the seven-column week at some normal widths. Nothing is clipped and session text remains visible. It was retained rather than silently changing the reviewed CSS again.

## Limits

No signed-in current production dashboard was accessible, so no live superiority claim is made. User visual acceptance remains pending. No full contrast certification, screen-reader audit, old-browser/container-query compatibility proof or production-data acceptance was performed. The local preview uses synthetic people, assignments, questions and results, with browser-local notes/drafts only.


## Palette correction, 2026-10-26

Joshua reaffirmed charcoal and off-white. Navy, gold, claret and blue accents were replaced with charcoal, off-white and muted neutral shades across default/hover states, progress, chips, notices, sidebar and dialogs. Layout, fonts and JavaScript remain unchanged. The previous stylesheet is preserved in reviews/initial-navy-gold-style.css. Earlier review verdicts describe the earlier stylesheet; this correction is separately browser-checked.
