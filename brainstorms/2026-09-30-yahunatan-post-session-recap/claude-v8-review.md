# V8 Claude review: approved

2026-09-30. Observed model: `claude-opus-5-5`. Verdict: **APPROVED**. Source-level teaching approval; live layout and interactions remain unverified.

I re-checked the current V8 Markdown, the V8 builder and the HTML. All eleven earlier findings are resolved in both the editable source and the HTML.

- **V8-1 and V8-2:** CHAIN-LAB now follows the requires-vs-received worked answer in section 08. The source uses #### for Fact 1-4, and the builder turns these into h4. HTML grep confirms both.
- **V8-3:** All four mixed problems are new scenarios. They cover a hidden chain with a negative fact, an "only if" with an OR, a requirement-vs-completion non-match, and a shared start. The worked answers hold up against counterexamples.
- **V8-4:** Accepted under the stated user request. The upfront definitions now appear in both source and HTML. Sections 01 and 02 no longer repeat them as a glossary.
- **V8-5:** The chain is restated, with Application R as a worked negative fact.
- **V8-6:** The early contrapositive clause is removed from section 06.
- **V8-7:** The FACT-LAB title is now h3.
- **V8-8:** The group-scope paragraph comes before the table.
- **V8-9:** The duplicate hidden-chain paragraph is removed.
- **V8-10:** MODALITY follows the "should" example, and a correct should-contrapositive is added.
- **V8-11:** The full rejected-copy list and the 500 KB guard are back.

The heading and interactive-block order in the HTML matches the source exactly. The teaching criteria are met:
- Apply and link are adjacent and numbered.
- Adding a fact is taught on its own.
- Each boundary is taught before it is tested.
- Contraposition, the four fact cases, the hidden chain, AND/OR negation, should/may/requires and existence limits are all kept.
- Assigned work is still drills, then LSAT questions.

Two low-severity polish items remain. Neither is a material defect.

## V8R-1 (low)

Practice 1 (line 329) calls the person 'Instructor Q', while the rule's condition is 'certified instructor' and the worked answer (line 331) concludes 'Q is not a certified instructor'. This is logically consistent, since Q can be an uncertified instructor. But the label invites a mismatch exactly where the lesson teaches matching the complete condition. A reader could take 'Instructor Q' as meeting the first rule's condition and see a contradiction.

Optional fix: Rename the person to 'Q' or 'Applicant Q'. Alternatively, add one clause to the worked answer: 'Being called an instructor does not establish certification.'

## V8R-2 (low)

Line 19 hardcodes the HTML definitions text. Line 17 strips the matching '**Fact means:**' and '**Rule means:**' lines out of the source before rendering the opening. The two currently match (lines 5-7 of the source and the HTML grep), but a later edit to the source definitions would not reach the HTML.

Optional fix: Build the intro-definitions block from the two '**... means:**' lines in the source, or assert that the hardcoded strings appear in the source.

## Coverage

- Re-read all of the current concept-lesson-v8.md (lines 1-350) and all of build-preview-v8.py (lines 1-43).
- Checked each earlier finding (V8-1 to V8-11) against the current source and HTML.
- Checked the V7 ORD findings against the current order. ORD-1 to ORD-5 and ORD-7 to ORD-9 are resolved. ORD-6 is acceptably resolved: requires-vs-received has moved, and the 'some' existence Try-it stays in 01 to support the existence limits.
- Grepped conditional-reasoning-v8.html for the full order of h2/h3/h4 headings, every interactive block class, data-check 1-7, the intro links, the intro-definitions text, the start of the practice JSON, the Application R text, the should-contrapositive text, and the group paragraph placed before the table.
- Interactive blocks inspected in the HTML: fact-scope, rule-parts, application-proof, output-comparison, fork (SHARED-TRIGGER), pop-quiz 2, two-moves, fact-lab (h3 title), hidden-chain, chain-lab, word-contrast (MODALITY), negation, 7 typed checks, mixed practice. Their content comes from the builder modules read in the previous round (v3/v6).
- Tried a counterexample against each new worked answer: Practice 1-4, the Application R chain, and the should-contrapositive.
- Confirmed by grep that the canonical recap has a V8 marker block (lines 1594-1946) containing the new Application R and Practice 1 text.

## Limits

- No live or visual inspection. The host reports that browser policy blocked the local preview, and I have no browser either. Layout, contrast, mobile behaviour and interaction were not verified.
- I could not compute SHA256. The frozen hashes and the 94,740-byte package size are taken from the host record, not verified by me.
- The HTML is minified onto one line and was inspected through targeted grep only. I did not compare its full text line by line with the source.
- I compared the canonical recap V8 block by markers and spot text only, not line by line.
- I did not read the Must Be True Core transcript/teleprompter. No claim needed it.
- I did not run the builder, any tests or a publish dry-run. No files were modified.

## Codex disposition

Accept approval of the frozen V8 teaching artifact. Leave the two nonblocking polish suggestions visible for the next edit; no post-review changes. Canonical Markdown equality, heading/anchor checks, JavaScript syntax and the publisher dry-run passed. Nothing posted.
