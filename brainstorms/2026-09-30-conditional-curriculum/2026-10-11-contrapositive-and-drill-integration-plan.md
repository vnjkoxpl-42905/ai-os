# Teach the missing requirement, then build the full translation sequence

Date: 2026-10-11. Status: proposed game plan requested by Joshua. No course reorder, question import, grading implementation or publication has occurred in this turn. Prototype drill numbers below identify the existing review prototype; final student numbering should follow the approved course order.

## The decision

Teach the **meaning of the contrapositive directly after Must arrow**. Teach the **written transformation later, after students can identify both complete conditions and translate a rule**. Reuse and improve the existing two lessons instead of creating competing explanations.

This follows the original HTML skeleton: discover the missing-requirement inference, compare four fact situations, then learn formal diagrams and contrapositives. The desktop worksheets demand the whole process, so split their tasks by prerequisite rather than importing each packet unchanged.

## Sources checked

- [Original teaching HTML](../../raw/sources/conditional-reasoning-voice-standard/conditional_reasoning_transcription.html): conceptual contrapositive at lines 234–291, four sign patterns at 355–385, practice-versus-real-use distinction at 413–420.
- [Opening source map](2026-10-02-opening-lessons-source-map.md): stages 6–7, 9 and 13 distinguish discovery, formal writing and integrated practice.
- [Desktop source integration audit](2026-10-11-desktop-group-1-2-integration-audit.md), with every-item ledgers and original file hashes. Three notes teach operator → complete ideas → symbols → diagram → contrapositive → English.
- [LSAT Lab source review](../../wiki/sources/lsat-lab-conditional-logic-clip.md): sufficient-present/necessary-absent contrast and reverse-and-negate; compound work is outside the simple introductory lesson. This turn used the preserved review, not a fresh video viewing.
- Current local app: missing-requirement discovery, four-case comparison, formal contrapositive lesson, 24-question foundation drill, 24 baseline mixed-translation items, and nine-item final integrated drill.
- [Seven-drill prototype](prototype/group-1-2-drills.html): 133 source task instances, editable responses without grading. Familiar statements repeat for different operations.

## Lesson 1: The contrapositive

Placement: directly after Must arrow, reusing the existing missing-requirement lesson. Keep the law-school relationship as the connecting anchor; preserve the existing fresh prediction example as a transfer check.

Teaching sequence:

1. **Keep the original rule visible.** If you are enrolled in law school, you are a student. Show complete conditions on either side of the original arrow.
2. **Change one fact.** This person is not a student. Ask whether the person can be enrolled in law school. Require an attempt before revealing the explanation.
3. **Explain why.** Enrollment requires being a student. Someone who is not a student cannot satisfy that requirement, so they cannot be enrolled under this rule.
4. **Name the inference.** Proposed copy: “The contrapositive tells us what follows when the necessary condition is false.” Immediately read the concrete version: “If you are not a student, you cannot be enrolled in law school.” This is proposed wording, not a user-approved quotation.
5. **Show both forms.** Original: enrolled → student. Contrapositive: not student → not enrolled. Keep both visible; present each new arrow left to right. It is the same relationship expressed another way, not an additional assumption.
6. **Compare the four facts.** Enrolled establishes student; not student rules out enrolled; student alone does not establish enrollment; not enrolled alone does not settle student status. Use one clearly labeled fact at a time with a learner prediction.
7. **Fresh check.** Use a clean existing requirement example with no modality or timing ambiguity. Check the inference, not recall of the label.

Design: large complete-condition labels, clear given-fact versus conclusion distinction, meaningful transition from the original necessary condition to its negation. Do not animate a bare reversal as though it were valid. Keep a static reduced-motion version. The color identity of a concept can remain consistent, but original sufficient/necessary labels must not falsely persist in the transformed rule: not-student is sufficient in the contrapositive and not-enrolled is necessary there.

Do not start with symbols or the phrase flip and negate. Do not claim a rule disappears when a fact leaves the other side undecided. Do not teach temporal or causal conclusions from the arrow.

## Lesson 2: Write and read the contrapositive

Placement: after forward translation and the whole-meaning checks, before full worksheet contraposition. Reuse the existing formal lesson and its sign-pattern interactions.

1. Read the original diagram in ordinary English.
2. Reverse the positions of its two complete conditions.
3. Negate both complete conditions. Explain not before introducing the symbol; negating not-A gives A.
4. Read the new arrow back into English and compare its meaning with the original.
5. Work through A → B; A → not-B; not-A → B; not-A → not-B. Derive each transformation rather than displaying four unexplained formulas.
6. Distinguish a contrapositive from reversal alone and negation alone using short correction tasks.
7. Explain why these training drills ask students to write the contrapositive, while later test-taking need not involve writing it every time.

Whole-condition negation comes before compound decomposition. Not returned unopened does not automatically mean returned opened; not both is not neither. Advanced AND/OR and quantified scope items stay outside this lesson until their own prerequisites are taught.

## Where every prototype drill goes

| Prototype set | Items | Core-path placement | Adaptation |
|---|---:|---|---|
| D1 Intro identification | 15 | After students have learned both indicator groups and condition roles | Select indicator(s), then full sufficient and necessary conditions. Preserve scope/modality. Intro training is the first source-backed drill. |
| D2 Indicator identification | 13 | Follow D1 as focused word-family practice, or use targeted subsets following each group's instruction | Label the selected expression, not the entire sentence. Correct the-only conflict. Avoid falsely forcing one group when more than one indicator is present. |
| D4 Indicator roles | 10 | After complete-condition teaching, before independent rewriting | Reuse familiar statements to place both conditions beside an arrow. Explicitly identify this as a new operation on familiar examples. |
| D3 Intro diagrams | 15 | After role placement; forward-only first, revisit after formal contraposition | Provide distinct original-only and original-plus-contrapositive task variants. Remove premature optional contrapositive controls from the early version. |
| D5 If/then rephrasing | 25 | Keep the whole meaning / mixed forward translation | Write a faithful if/then version and diagram it. Later revisit selected items with contraposition. Split into short sessions, keeping all available in the bank. |
| D6 Full indicator translation | 20 | After formal contrapositive lesson and readiness check | Original diagram, contrapositive, and English readbacks. Separate simple from negative/temporal/compound items. |
| D7 Independent translation | 35 | Final mixed practice and assignable review | Fresh mixed tasks after prerequisites. Hold flawed/unclear sources and compound-scope items until corrected/taught. Do not force a single 35-item sitting. |

Thus the likely working order is D1 → D2 → D4 → D3 original-only → D5 forward-only → formal contraposition → D3/D5 revisit → D6 → D7. This is a learning sequence, not a requirement to complete every available item before advancing. Final numbering must reflect the actual chosen path rather than the order in which source files were prototyped.

## How these fit the material already built

- Keep the definition and Must arrow lessons. Move and clarify missing-requirement discovery, rather than making a third contrapositive destination.
- Keep brief checks next to the idea they assess. Audit the existing 24-question Drill 1 against new D1/D2: retain distinct conceptual questions as lesson checks or supplementary practice; remove duplicate mandatory work only after item-level comparison. Do not silently delete that bank.
- Use the new source items to deepen complete-condition and forward-translation practice. The existing mixed engine already supports attempts, diagramming, equivalence checks and error-specific follow-up, so reuse those mechanics where they fit.
- Keep the nine-item final integrated drill as a short readiness check. D6/D7 supply sustained practice after it.
- Keep flashcards separate for recall. They do not substitute for writing or constructing an equivalent rule.
- Keep all source sets accessible from a drill library, even when the recommended path assigns a shorter subset.

## Implementation plan

### Pass 1: Clean and structure the source bank

Preserve the PDFs/DOCX unchanged. Give every exercise a stable source ID and every operation a task-variant ID. Record file/hash/page/item, original statement, reviewed derivative, source issues, complete conditions, indicator spans, forward relation, optional contrapositive, accepted paraphrases, explanations and prerequisite tags. Resolve or hold each flagged answer. The 133 prototype count is source coverage, not a promise of 133 approved graded items.

Block unreviewed keys from grading. In particular correct indicator-as-condition, the-only direction/classification, ability-versus-action, duty-versus-compliance, omitted deadlines and unscoped negation. Keep a teacher-visible correction record.

### Pass 2: Fix the teaching sequence

Move conceptual contrapositive after Must arrow and improve its explanation/visuals. Keep formal contraposition after accurate forward translation. Ensure full mixed-group drills follow actual teaching of both groups, not merely visibility of a list. Update lesson menu, next/back links and drill prerequisites together.

### Pass 3: Ship Intro Training first for review

Build the source-backed introductory drill with one clear operation at a time. Support selecting full phrases or writing them, specific feedback, keyboard/touch access, revisiting mistakes and meaningful progress. Distinguish answered, correct and needs-review states. Do not count typing a draft as mastery.

### Pass 4: Add forward-translation sets

Integrate D2/D4, then D3/D5 forward variants. Compare a student's meaning rather than exact string equality. Use constrained selections/diagram assembly where automatic grading is reliable. Open prose can receive a model explanation and an explicit self-check or teacher-review state; do not present it as automatically validated if no reliable grading exists.

### Pass 5: Add full contraposition practice

After teaching and readiness checks, expose the full task variants and integrate D6/D7. Add negative-condition items before compound/quantified challenges. Preserve full negation and all modality/time restrictions in feedback.

### Pass 6: Verify real student use

Check each answer against the source adjudication; independently review explanations. Walk the rendered UI, including wrong answers, retries, completion, responsive layouts and reduced motion. For recorded/assignable work, use the app's existing attempt and persistence contracts, then verify reload, resume, completion and assignment behavior. The standalone prototype's browser-local writing fields are not production assessment or cross-device persistence.

## Review boundary

This plan proposes the sequence and implementation. It does not certify all items as ready, alter the current course, or publish work. First concrete implementation should be the conceptual contrapositive lesson plus cleaned Intro Training, reviewed together before bulk importing the later sets.
