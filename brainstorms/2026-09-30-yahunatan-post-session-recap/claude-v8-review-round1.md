# V8 Claude review, first pass

2026-09-30. Observed model: claude-opus-5-5. Verdict: REVISE.

V8's teaching order is a real improvement over V7. Applying a rule (03) and linking rules (04) now sit next to each other. Adding a fact is its own section (05). Advice/permission, requires-vs-received and AND/OR negation have moved after linking and its failure cases. "Only if" is taught (08) before modality and compound negation use it. POP-QUIZ-2 now comes after the prose that explains it. Contraposition, the four fact cases, the hidden chain through contraposition, existence limits and "some" scope are all still present. Assigned work is drills first, then LSAT questions, with no invented IDs or deadlines. No em dashes, no "concept lesson" label, and arrows render as bold teaching type. I found no logical errors in the worked answers.

Status of the V7 findings:
- ORD-1, ORD-2 and ORD-4: resolved.
- ORD-5: resolved by a different order. Contrapositive now comes after linking, and link failures are grouped in 06.
- ORD-3: resolved in the HTML only, not in the Markdown.
- ORD-6, ORD-7 and ORD-9: partly resolved.
- ORD-8: not resolved.

Two problems block approval. First, the HTML under review cannot have been built from the current Markdown. CHAIN-LAB's position and the Fact 1-4 heading levels differ, and in the Markdown the chain lab still tests requires-vs-received before teaching it. Second, all four final practice problems repeat earlier examples almost word for word, so there is no fresh transfer question. A few smaller fidelity and polish issues follow.

## V8-1 (high)

The HTML and the current Markdown disagree in two places. (1) Chain lab position. In the HTML, class="chain-lab" comes right after the requires-vs-received check (data-check="6") inside section-8. Under 'Carry a negative fact through a chain', the next heading is '<h3>A contrapositive c...' with no lab between them. In concept-lesson-v8.md, <!-- CHAIN-LAB --> sits at line 216 in section 07, between those two h3s. (2) Heading levels. The HTML renders '<h4>Fact 1: The person is trained</h4>' and '<h4>Fact 4: ...</h4>'. The Markdown has '### Fact 1' (line 167), and build-preview-v3.py:94-95, the only heading handler build-preview-v8.py inherits, maps '### ' to <h3> and has no h4 handling. Running build-preview-v8.py on the current Markdown would therefore produce a different page from the one being reviewed and approved. The SKILL makes the Markdown the editable source and the static fallback.

Fix: Pick one canonical version. The HTML's placement is the better one. Update concept-lesson-v8.md to match: move <!-- CHAIN-LAB --> to after the worked answer at line 256, and decide on h3 vs h4 for Fact 1-4. Then rebuild with build-preview-v8.py. Add a builder assertion on the order of the h2/h3 headings and markers so the source and the package cannot drift apart again.

## V8-2 (medium)

In the source, CHAIN-LAB (line 216) offers 'Has received special approval → Needs a signature' (build-preview-v3.py:45). Its feedback explains 'Requires approval ≠ Has received approval' (v3 JS chainCases.received). That distinction is first taught at lines 250-256 in section 08. This is ORD-3 again, which breaks the 'teach boundaries before testing them' criterion. The lab also tests forming links ('Can these rules form a chain?') but sits inside the contrapositive section (07), between the chain-contrapositive and hidden-chain subsections.

Fix: Move the CHAIN-LAB marker to directly after line 256, as the current HTML already does. The alternative is to move the 'Keep requirements separate from completed actions' subsection (lines 250-256) into section 06 and put CHAIN-LAB at the end of 06.

## V8-3 (medium)

All four 'Mix the moves' problems repeat earlier material almost word for word:
- Practice 1 (lines 317-319) matches the confidential/restricted-storage Try-it at line 205.
- Practice 2 (321-323) is the Application J example from section 05 (lines 101-105).
- Practice 3 (325-327) is the panel/training/badge Try-it at line 139.
- Practice 4 (329-331) is the reviewed-and-authorized Try-it at line 294.
The SKILL and the quality bar require a fresh transfer question and different examples where possible. None of the problems tests a hidden chain through contraposition, OR negation, 'only if' translation, should/may, or requires-vs-received.

Fix: Replace at least two or three problems with fresh scenarios that mix moves. Examples: two rules that only link after contraposition, plus a negative fact; an 'only if' sentence with an OR requirement; and a requires-vs-received chain that does not link. Keep one problem whose correct answer is 'the other side stays open'.

## V8-4 (medium)

Line 18 adds an HTML-only 'intro-definitions' glossary: Fact, 'Something established as true about a case or group. “Mira is trained.”', and Rule, '“Every trained person has a badge.”'. Section 01 (line 33-35) and section 02 (line 47-49) then define the same terms again with the same Mira and badge examples. lesson-quality-bar.md line 10 says to 'avoid a compact glossary followed by the same examples again'. The glossary is also missing from the Markdown fallback. It does not define 'starting condition' or 'shared condition', which the opening uses (lines 13 and 25).

Fix: Remove the injected glossary. If an early definition is needed, put one sentence in the Markdown opening that names 'starting condition' and 'required result', and keep the full definitions with their examples in 01 and 02.

## V8-5 (low)

Line 214 says 'use the chain's contrapositive: Does not need signature → Does not require approval → Was not late' without restating which chain. Line 125 has just told the reader 'Rules from earlier examples do not carry over', and three other examples (badge, confidential, panel) come in between. The section also gives no worked fact for the backward carry.

Fix: Restate both rules from section 04. Then add one worked line, for example: 'Application K does not need a signature, so K does not require approval and was not late.'

## V8-6 (low)

Line 137 (section 06) says 'keep the rules separate or see whether a valid contrapositive produces a match'. The contrapositive is not defined until section 07 (line 157), and the hidden match is taught at lines 218-240.

Fix: Drop the contrapositive clause from line 137, or replace it with a forward pointer such as 'Section 07 shows one way a restated rule can reveal a match.'

## V8-7 (low)

ORD-8 is unresolved. Line 22 rewrites the FACT-LAB title as '<h2>What does this fact let you conclude?</h2>'. Grep confirms that h2 sits inside section-7, so in the heading outline the lab looks like a peer of the numbered sections.

Fix: Emit the lab title as <h3>, or as a non-heading label with an aria-label on the section.

## V8-8 (low)

ORD-7 is partly unresolved. Line 311 brings in a new move after the summary table in 09: applying a rule to a 'some' group fact ('Some applications were submitted late ... therefore some applications require special approval'). Section 03 only shows rules applied to individuals.

Fix: In section 03, add one sentence noting that a group fact ('some X') can meet a starting condition while keeping its scope. Alternatively, move the line 311 paragraph above the table.

## V8-9 (low)

Line 240 repeats what lines 226-232 have just shown: rewriting Trained → Has a badge as No badge → Not trained creates the connection. The quality bar says 'Remove repetition once the example has done the teaching.'

Fix: Delete line 240, or cut it down to its one new point: if the match is already visible, link directly.

## V8-10 (low)

The MODALITY figure (v3 VISUALS: 'Should be inspected ≠ Has been inspected') is at line 268. That is after the 'may enter' permission paragraph (266) and separate from the 'should' paragraph it illustrates (264).

Fix: Move <!-- MODALITY --> to directly after line 264.

## V8-11 (low)

The V7 builder refused to write a package of 500 KB or more (build-preview-v7.py:69-70). The V8 builder removed that guard. It also dropped the V7 rejected-copy entries 'Keep only what must follow.' and 'First, understand each statement.' The SKILL requires a single-document package under 500 KB.

Fix: Restore the size assertion and the full V7 list of rejected copy in build-preview-v8.py.

## Limits

- This was a static source review only. I did not view the page live, so visual hierarchy, spacing, contrast, mobile layout and interaction behaviour were not checked.
- The HTML is minified onto one line. I read it only through targeted grep excerpts, not in full.
- I did not run the builder, any tests or a dry-run publish. Package size was not measured.
- I did not read the Must Be True Core transcript/teleprompter or the student's session transcript. No teaching claim needed source clarification, and I took the assigned-work wording at face value against the plan.
- The order of Glob's modification-time sort suggests the HTML is older than the Markdown, but I did not confirm it. V8-1 rests only on rendering differences that the current builder cannot produce.
- The canonical student recap file was not checked for a V8 block. Git status shows it unmodified, and the V8 builder reads concept-lesson-v8.md directly.
