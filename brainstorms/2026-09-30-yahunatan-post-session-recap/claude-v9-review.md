# V9 Claude review: approved

2026-09-30. Observed model `claude-opus-5-5`. Verdict **APPROVED**. Static teaching and code review only; no live visual verification.

All five round-1 findings are fixed, and I checked each one in the current source, the builder and the HTML. V9-1: the HTML now reads "This application needs a supervisor's signature" and "Submitted late → Needs a supervisor's signature". It no longer contains "J needs", and the rejected-string list blocks it. V9-2: the button handler now calls joinReplay.focus() after the new rule is shown. V9-3: the quiz feedback now reads "Correct. A shared starting condition does not connect the two results." V9-4: the Match paragraph now follows the JOIN-RULES demo. V9-5: "Given rule:" is singular, and the source and imported diagrams use "Is trained →" (the builder replaces "Trained →" in every visual). These changes introduce no new defects. The two given rules in the join demo stay fixed. The shared phrase is an exact match, and the result does not claim that any application exists. The demo's motion plays once per click and stops when motion is paused or reduced. The checks say they are not graded. The reasoning sequence, the 7 checks, the 4 practice problems and the assigned work all match approved V8. The canonical recap's V9 block (lines 1950-2324) contains the revised text. One optional consistency item remains. This is a static source approval only: it is not visual or interaction verification, and it does not give permission to publish.

## V9R2-1 (low)

Optional consistency item, not a material defect. Line 185 (also in the canonical recap at line 2136) still writes the invalid reversal as **Has a badge → Trained**, while V9-5 standardized the rule as 'Is trained → Has a badge'. In the fact explorer, the static HTML still says '<strong id="proof-rule">Late → Requires approval</strong>' (build-preview-v6.py:60). proofUpdate() replaces this on load with 'Submitted late → Requires approval', so readers only see it if JavaScript fails. Both are short descriptive phrases, not single letters, so correction 6 is still met.

Optional fix: Optionally change line 185 to **Has a badge → Is trained**. Optionally also replace 'Late → Requires approval' with 'Submitted late → Requires approval' in the V9 body, so the no-JavaScript fallback matches.

## Coverage

- Re-read build-preview-v9.py in full (lines 1-127). This covers: the TWO-OUTPUTS override (line 39); the 'Trained →' to 'Is trained →' replacement in every visual (40-41); the 'Given rule' label (45-48); joinReplay.focus() (79); the quiz verdict replacement (112); and the 'J needs' guard (114).
- Re-read concept-lesson-v9.md lines 85-267 (sections 04 to 07, including the hidden chain). This range covers every place touched by V9-4 and V9-5. I checked lines 1-84 and 268-372 in full in round 1, and the host says no other changes were made. I grepped the whole source for 'Trained' variants.
- Grepped conditional-reasoning-v9.html. Present: 'This application needs a supervisor's signature', the new quiz verdict and joinReplay.focus. Absent: 'J needs' and any stale 'Trained →'. The only 'Late →' is the static fact-explorer text that the script replaces on load, and the only '→ Trained' is the reversal on source line 185.
- Grepped the canonical recap students/yahunatan-zetvy/recaps/2026-09-16-recap.md. It has one V9 marker block (lines 1950-2324). In that block, Match comes after JOIN-RULES (lines 2046 and 2048), and 'Given rule:' and 'Is trained → Has a badge' appear at lines 2076, 2128 and 2203.
- Read in full the three references missed in round 1: .agents/skills/post-session-recap/SKILL.md, wiki/teaching-voice.md, and brainstorms/2026-09-28-recap-format/07-quantity-statements-lesson.md. Checked V9 against them: the concept-first opening, the idea → example → guarantees → limits → why → check order, given/what follows/why kept visually separate, honest wording on non-graded checks, no em or en dashes, no internal labels, the teaching register, and neutral should/may examples. V9 meets them; it also states existence limits explicitly, as the Some/Most/All lesson does.
- Round-1 coverage still holds for code that has not changed: the inherited V3, V6, V7 and V8 builders and their JavaScript state (practiceIndex and listener order, check submit and edit, the fact explorer, motion pause and reduced motion), the narrow-width CSS, the shared-end SVG aria-label, and the logic checks on every worked answer.

## Limits

- Static review only. I have no browser and the host reports that browser policy blocks the local preview. Layout at each width, contrast, the actual motion, keyboard focus behaviour and screen-reader announcements were not verified live.
- I did not run the builder, any tests, a JavaScript syntax check or a publish dry-run. I could not compute SHA256, so the frozen hashes and the host's build checks (7 checks, 4 practice problems, guards, canonical exact-text match) are reported by the host, not verified by me.
- The HTML is minified and was checked through targeted greps, not line by line.
- I compared the canonical recap's V9 block with the source by markers and spot lines, not a full diff.
- I did not inspect the Some/Most/All rendered preview (08-*.html) or the screenshots in research/. The plan asked for the reference lesson Markdown, which I read.
- I did not read skills/reference/session-recap-quality-reference.md or the session transcript. The plan does not list them, and no V9 claim depended on them. This approval does not give permission to publish.

## Codex disposition

Accept static approval. Optional shorthand consistency suggestion retained for future edits; no changes after approval. V9 is current in canonical recap. Nothing posted.
