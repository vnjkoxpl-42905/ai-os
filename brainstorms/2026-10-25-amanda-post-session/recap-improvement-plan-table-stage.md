# Amanda recap: explain the sentence types and show the two reasoning tasks

Date: 2026-10-25. Host/builder: Codex. Independent plan reviewer and final inspector: Claude CLI default model (observed model to be recorded). Mode: review. Maximum plan rounds: 5. Maximum fix/inspection rounds: 2. No publication, assignments, commits or changes to other students.

## Authorized result

Joshua selected Amanda's actual recap and asked for: (1) second-brain-backed explanations of fact, rule, causal, correlation, normative and quantity in a visual interactive table; (2) much clearer linking/application scenarios; (3) better visual teaching throughout using existing design-folder components; (4) Claude review to refine the note. The earlier interview is not restarted. The user comments separately authorize the draft revisions; the claude-review invocation alone does not authorize posting.

Improve the existing Session Manual document, not the application or its renderer. Preserve its lesson marker `amanda-2026-10-21-rules-and-facts`, date, direct voice, specific student credit and homework commitments. Preserve the approved cream/serif Session Manual family while making content more useful. Static labels, letter variables and color alone must not carry explanations.

## Source-backed teaching

Vault root: `C:/Users/Joshu/dev/ai-os`. Second-brain-query followed the wiki/schema/corpus routes and read the full Amanda transcript. New examples below are illustrative drafts, not claimed session quotations.

- `students/amanda/sessions/2026-10-21-conditional-rules-facts-and-parallel-flaws/transcript.md`: 240-258, 278-319, 395-428, 479-536, 631-673, 737-747. Sentence categories, facts and rules, linking/application and active reading.
- `corpus/Curriculum/Conditional Logic/Notes/_megadoc_reference_conditionals.md`: 36-59. Complete conditions, guarantee, no existence/cause/time smuggled into an arrow.
- `corpus/Curriculum/Principle/Homework/Principle-Conform + Principle in Stimulus HWK.md`: 18-30. Preserve normative modality.
- `corpus/Curriculum/Causation/Homework/Answer Key - Correlation vs Causation Drill_dup1_dup1.md`: 13-43, 113-127. Association versus production/influence, not necessarily sole cause.
- Existing note's supported AND/contrapositive teaching, SA/MBT comparison and student credit remain grounded in its private source map. No official test stimulus is reproduced.

Explain the six types visibly in a semantic table: type, ordinary meaning, example, reading question. Fact: what is true in the situation. Rule: if one full condition is true, another must be true. Causal: produces or influences. Correlation: association without itself claiming causation. Normative: should/right/wrong/permitted/required; preserve modality. Quantity: some/most/all/none/count/percentage; preserve amount and individual scope. Explain that types can overlap; categorizing does not replace premise/conclusion analysis. Do not import broad older-corpus causal verb heuristics.

## Existing components to reuse

- `.agents/skills/post-session-recap/references/session-manual/session-manual.css`: `.t`, `.kinds/.kind`, `.opposite`, `.steps`, `.drill`, `.callout`, hero and section hierarchy.
- `brainstorms/2026-10-25-note-inventory/posted/2026-08-24_Asia_75133805.html`: named trigger/requirement diagram composition (`.cs-figure/.cs-half`, 75-125). Adapt composition using Session Manual tokens; do not copy unrelated teaching or React dependencies.
- `design/README.md` and relevant library/method routes were inspected. Retain existing components rather than adding an external component package.

Use a small Amanda-only CSS extension inside recap.src.html after the shared `/*CSS*/` slot. Do not modify the shared builder or stylesheet, Yahunathan notes, runtime skill copies, app code or unrelated design prototypes. A semantic table remains understandable with CSS/JS unavailable. Responsive cards may restyle cells but retain meaningful headers and reading order.

## Page sequence and interactions

1. Hero: two useful tasks conditional reasoning often requires; a problem may require both. Do not claim an exhaustive either/or classification.
2. Sentence-reading section: visible six-type table; type names, clear meanings and fresh short examples. An explicit overlap example and a pointer to keep tracking evidence/conclusion. A small native disclosure can reveal why an example fits. Do not hide essential definitions behind interaction or duplicate the later full practice set. Retain the session's but/yet/however observation as a qualified reading clue: check how the ideas on either side relate; it does not guarantee the correct answer's location.
3. Two worked scenarios with complete words:
   - Link two rules: library open -> lights on; lights on -> main circuit has power. Visually match the repeated lights condition. Derived conclusion is another conditional, not a fact: if library open, circuit has power. Also show its contrapositive: if the main circuit has no power, the library is not open. Neither derived rule asserts that a condition occurs.
   - Apply a rule: library open -> lights on, plus one separately supplied fact. Fact library open entails lights on. Show input and resulting fact, and distinguish this from linking.
4. Four clearly separate fact cases under the same rule. Open -> lights on; lights not on -> library not open; lights on -> unknown whether open; not open -> unknown whether lights on. Use four separate native details/summary disclosures with reasoned feedback. No JavaScript-dependent switching panel. With JavaScript disabled, each fact and its answer must remain reachable using the native disclosure. Never display incompatible facts as a single supplied case. A possible closed library with lights for cleaners explains both invalid inferences. Avoid causal wording for noncausal arrows.
5. SA/MBT comparison: same rule/fact/conclusion pieces, presented as a simple teaching model rather than all possible question forms. SA answer works with the given evidence. Replace the fence/property illustration with the same neutral library rule and a stated supplied fact. Label this privately as a new illustrative example, not a session quotation; update the earlier Session examples used description through a dated superseding note. Keep the useful session distinction.
6. AND trap: full conditions joined by `and` point to result. Show valid forward inference and contrapositive; distinguish one trigger plus result from having both triggers. No letters, plus-sign ambiguity or incomplete negation.
7. Two practice blocks: sort sentences and decide what follows. Ask the reader to think/explain before a native answer reveal; show why in hidden feedback, not just a label. No score, timer, compulsory typing or completion machinery. These remain teaching examples in a recap.
8. Short checklist and complete homework list. Preserve pending teacher tasks privately and no false claims that new assignments were sent. Existing promise wording can remain future-facing if it does not assert completed delivery. No exact unapproved drill/set is invented.

Keep a readable 800px measure, generous type/spacing, restrained color and complete prose labels. Stack scenario cards/diagrams/tables on phones without horizontal page scrolling. Native details/summary disclosures must work with pointer, Tab, Enter and Space as appropriate; define explicit summary:focus-visible and button:focus-visible outlines in the Amanda extension and honor reduced-motion. Keep the shared CSS replacement token only once in recap.src.html. Essential teaching remains visible without JS.

## Files and preservation

Authorized deliverable edits:
- `brainstorms/2026-10-25-amanda-post-session/recap.src.html`
- `brainstorms/2026-10-25-amanda-post-session/recap.html` (actual builder output)
- `students/amanda/recaps/2026-10-21-recap.md` (sync current student-facing text and all reveal answers; preserve YAML draft/posted:false and private history/source map)
- Focused source/review/evidence records in Amanda's existing brainstorm folder and wiki log after checks. The brainstorm-local recap-review-log.md is the calibration checkpoint for this task. Do not modify the six skill copies or archived example copies. Privately flag that the skill's approved-example snapshot still contains the older label-only version and does not represent Joshua's new corrections.

Snapshot pre-revision source, built HTML and canonical recap for reversible comparison under the existing Amanda folder. Preserve original evidence and prior archived text. No deletion. Source snapshots are review artifacts, not competing canonical notes.

Pre-build Git baseline: `7e3a37c49aad80bc3d36352b796612425fe9b051`. The vault contains extensive unrelated edits. Use an isolated sparse review worktree at `C:/Users/Joshu/AppData/Local/Temp/codex-amanda-review-20261025-01` from that existing commit, no new commit, and copy only the scoped deliverables/source evidence. Review and inspection run against that repository. Before review, also copy the builder, CSS, full transcript, all three corpus sources, Asia note, teaching voice/copy-correction references and before-refinement snapshots into the isolated worktree. Write a source/snapshot manifest with SHA-256s. Mirror source/build/canonical bytes from the actual vault before final inspection and record matching SHA-256s. These deliverables are untracked at the historical Git baseline, so --base gives whole-file additions rather than their revision delta; the inspector must explicitly compare each before-refinement snapshot to its corresponding current file. The preserved snapshots provide the actual task delta. Logs/runner diagnostics stay outside the review checkout. The inspector reads the scoped manifest and reports its actual coverage. This avoids including other chats' ongoing changes in the approval snapshot.

## Verification

1. Source coverage/readback: all six category definitions and the overlap warning present; rule-link conclusion remains conditional; all four fact cases and AND answers withstand counterexamples; full conditions/modality retained. Privately cite sources and distinguish new examples.
2. Builder: `uv run --with markdown python -I .agents/skills/post-session-recap/references/session-manual/build_session_manual.py brainstorms/2026-10-25-amanda-post-session` -> recap.html lint ok. Output body matches source after CSS injection/newline normalization, stable marker, inline-only assets, under 500KB.
3. Focused browser proof script in the Amanda folder using the already-installed Playwright at `C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright`, Edge headless. Navigate the actual built local file. Check table rows/headings; every reveal opened/closed with pointer and keyboard; correct text and focus; no page errors; no horizontal document overflow at 1280, 838, 390 and 320 widths and enlarged text; no-JS essential definitions readable and all four native fact-case answers reachable; reduced-motion styles. Record core visible and total-with-reveals word counts; target about 1000-1300 visible words rather than padding every section. Report reading-time tradeoffs honestly. Do not start a server or attach to the user's authenticated browser. These are separate offline render checks, not signed-in student acceptance.
4. Save readable before/after screenshots including sentence table, scenarios, AND section and practice at desktop and phone widths. Host opens and actually inspects them. Reviewer receives screenshot paths if its read-only Read tool supports images; state image coverage honestly. Any failed image read is not visual approval.
5. Canonical Markdown matches current visible/revealed teaching in order, no private continuation in HTML; previous text/private records preserved. Add a dated note explicitly superseding the previous Preparation readback for the pre-refinement artifact; do not carry its ten-chip/dry-run claims onto the new build. Repeat the publisher dry-run for the new recap if claiming it passed. Check student-facing HTML text and the student-facing Markdown portion against the COPY-CORRECTIONS Never-column vocabulary and punctuation rules, distinguishing natural subject words from banned UI labels and private implementation terms. No student-facing writes occurred.
6. Independent fresh Claude `inspect --host codex --builder codex --repo <review worktree> --plan <this exact plan> --base <baseline>`. Supply host evidence; record actual model, whole result, findings, dispositions, final source hashes and inspection limits. Any new code/content changes after approval require fresh inspection within the two-round limit.
7. Open the improved original recap for Joshua using the Codex file panel / existing file browser tab. Remains a local draft. No perfection guarantee or publication claim.

## Assumptions and risks

- The user-approved model remains authoritative; visual improvements adapt it rather than replacing the note with an app or assessment.
- Reading time may increase with six explicit definitions; keep other sections concise without deleting important teaching or commitments.
- Some spoken heuristics are broader than formal logic allows. Preserve their teaching purpose but qualify misleading absolutes and document changes privately. Do not use review approval as Joshua's editorial approval.
- Publishing and homework assignment remain separately pending. This task does not repair unrelated operational-checkout edits or resolve the earlier wrong-chat bootcamp request.
