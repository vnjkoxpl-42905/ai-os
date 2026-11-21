# All 48 Spot the Relationship questions reviewed

Date: 2026-10-25. Scope: read-only authored content and grading source audit. No implementation or publication.

Claude Opus 5.5 examined each of Q01-Q48 and returned REVISE. Requested and observed model were both claude-opus-5-5; Claude Code 2.1.309. There was one completed independent review round. Codex checked coverage, source routing, and representative matcher behavior rather than treating the review as unquestionable authority.

## Evidence and exact version

- Repository: C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-video-release-20261025
- HEAD: e26001375e68ee67af757b20f2349aeca5e3cb91
- Content SHA256: 3C6AA28FD5BD78CCF190DF580C20FE853C219ACE1CD97CB6154A27F0BBA330B9
- Full independent response, coverage and limitations: ../handoffs/claudex/spot-all-questions-20261025/claudex-mc2nyxuo/result.json
- Audit instructions: ../brainstorms/2026-10-25-spot-all-questions-review.md
- Source inventory: ../handoffs/claudex/spot-all-questions-20261025/source-receipt.json
- Local behavior probe: ../handoffs/claudex/spot-all-questions-20261025/probe.mts

## What the review established

All 48 items have structured keys and explanations. Claude independently derived a relationship-type set for every item and found no objective type-set errors. It considered necessary/sufficient direction, exceptions, implicit comparisons, alternate indicators, explanations and progression. This is an evidence-backed source review, not a guarantee of correctness or a test of production grading.

There are nine grouped findings in the raw report, three rated medium and six low. Their claims require the following dispositions; the raw count is not a count of nine confirmed bugs.

## Findings and Codex dispositions

### F1: whole-sentence quotations can earn instant credit

Confirmed behavior, qualified as a task-design weakness rather than a simple violation of the existing rubric. The rubric expressly permits wider contiguous quotations. The source probe confirmed Q5's full sentence earns instant credit, and Q28 accepts the entire sentence repeated under both comparative and causal labels. Q34 accepts the shared span 'so masons reserve it for thresholds, but only if' under both types.

These answers contain valid indicators, so calling the identical repeated quotations 'swapped labels' is misleading. The problem is that the response provides no evidence of distinguishing which words support which type. Tighten that learning requirement deliberately if desired. Do not blindly adopt Claude's arbitrary six-word cap or reject every quotation containing another type; legitimate clause quotations can contain nested relationships. Prefer identifying a focused supporting span for each type, with clear instructions and representative cases.

### F2: unquoted Causal, caused falls through to AI

Confirmed with the real matchesCredited function: Q5 'Causal, caused' returns false while 'Causal, "caused"' returns true. The comma lookahead mistakes caused for another type label. This is an instant-grading inconsistency and unnecessary fallback, not proof that the AI marks the answer wrong. The claimed format example exists in stored instructions.rules but is not rendered by the current RelationshipIntro. The plain unquoted answer remains a reasonable supported format, since quoting style is not supposed to affect credit. Fix parsing with narrowly targeted regression cases, preserving multi-type boundaries.

### F3: lower and larger are treated inconsistently

Accepted ambiguity requiring revision. Q31 credits larger with an implicit alternative mould; Q7 and Q26 explicitly discourage lower as a comparison. The local probe confirmed the different treatment. The probe does not establish how the AI would grade the extra type.

Do not treat Claude's proposal to remove larger as an established grammatical rule. Larger and lower are both comparative forms, and the distinction between identifying position and comparing alternatives is genuinely ambiguous here. A safer authoring correction is to remove accidental comparisons from the early single-type prompts, such as describing the bolts as 'at the base' and the field by a non-comparative name, then align their keys/traps/explanations. Preserve deliberate contextual comparisons in Q31 and Q36.

### F4: the revealed answer joins alternatives with and

Accepted student-copy issue. One valid indicator per type is enough, but the reveal lists multiple valid quotations joined by and. Clearly present alternatives as alternatives. Prefer presentation from structured keys; do not casually change the authored delimiter without updating GROUP parsing and parity checks.

### F5: the current intro gives away Q30 and Q36

Rejected as a claim about the current normal Spot page. ActivityIntro.tsx routes the exact Spot title in non-section mode to RelationshipIntro.tsx, which renders its own instructions and does not read instructions.rules. Claude inspected the generic ActivityEditorialIntro and missed this routing. Item-specific statements remain in stored rules and are worth cleaning if that content will be reused; current exposure on the requested page was not established. A neutral teaching example sharing a construction is not inherently an answer leak.

### F6: causal connects fields conflict with connective-only indicators

Qualified clarity improvement, not a proven contradiction. A key can explain the causal relation expressed by an entire clause even if one event verb alone is not an adequate quotation. Thus Q41's gradient-to-water connection does not by itself mean 'follows' must be accepted alone. Nevertheless Q41/Q42 should explicitly distinguish the connective's explanatory role from the descriptive verb, so the grader does not infer a new valid indicator from connects. No model behavior was observed.

### F7: wording, precision and unsupported claims

Accepted. Q14 and Q18 should say same objects or situation, not same facts, because requirement and cause are different claims. Q15's 'an added lecithin' is awkward and its 'most-missed' claim lacks evidence. Q38 should preserve the sixty-percent threshold. Q45 should preserve the prompt's modality rather than substituting can. These are targeted content edits, not a bank-wide logical failure.

### F8: formulaic explanation fragments

Accepted editorial improvement. Replace stock fragments with the actual reasoning, especially Q3, Q7, Q12, Q21, Q23 and Q24. Avoid unsupported claims about what students miss most. Explanations should teach the relation through the sentence without becoming unnecessarily long.

### F9: predictable late-question pattern

Accepted progression improvement. Q29-Q48 contain all three types in 18 of 20 items. Add deliberate variation so three types is not a reliable guess. Preserve meaningful minimal pairs in the earlier questions. A no-relationship temporal distractor is not a drop-in item: the existing answer-key validator expects one to three relationships. Prefer initially varying one- and two-type late items; treat zero-type support as a separate design and grading change.

## Local checks and limits

Codex ran eight source-level probe cases using the actual TypeScript matcher through vite-node. Results confirmed the behaviors above. No AI calls, browser interactions, production DB checks, assignment mutations or student responses were used. The current code chooses google/gemini-3.1-flash-lite for the AI fallback; this audit does not establish current availability, price optimality or live deployment of that backend.

The probe triggered Vite's known generated supabase/functions/mcp/index.ts rewrite. That exact generated change was restored to HEAD; it is not part of this task. No application source fixes were made. Full tests were not necessary for a read-only content audit and were not run.

## Recommended correction order

1. Fix Q5 parsing and settle the focused-quotation acceptance rule without overrestricting valid clauses.
2. Remove accidental comparative ambiguity from Q7/Q26; clarify that alternative indicators are optional.
3. Apply the precise explanation corrections and clean up formulaic language.
4. Vary the later question combinations while preserving the intended progression.
5. Independently inspect the resulting edits, then verify learner attempts and production content if implementation is authorized.

## Claude's question-by-question ledger

The entries below are the independent reviewer's coverage claims. They are retained verbatim, including finding references whose dispositions above qualify or reject the claim. PASS means the reviewer found no type-set error; it is not live acceptance proof.
- Q01 conditional 'only if' (vent opens -> 28 degrees, necessary). PASS.
- Q02 conditional 'if' (sufficient). PASS.
- Q03 conditional 'whenever' (sufficient). 'shift' is a change, not a comparison. PASS. F8 voice.
- Q04 conditional 'required'. 'before' is temporal. Modality ('may be removed') kept. PASS.
- Q05 causal 'caused'. PASS on content. F1 and F2 grading defects (unquoted 'Causal, caused' is not credited instantly).
- Q06 causal 'destroyed'. 'late' and 'most' are not comparisons. PASS.
- Q07 causal 'corroded'. F3: the trap rejects 'lower bolts', which is inconsistent with Q31's 'larger'.
- Q08 causal 'produced'. 'new', 'measurable' and 'drop' are not comparisons. PASS.
- Q09 comparative 'louder than'. PASS.
- Q10 comparative 'lighter than' (explicit benchmark: last year's). PASS.
- Q11 comparative 'less time than' / 'less ... than' (alternatives). PASS. F4 (the 'and' join reads as both required).
- Q12 comparative 'as strong as' (equality). PASS. F8.
- Q13 conditional 'only when' (necessary). PASS.
- Q14 causal 'raises'. PASS. F7 ('same facts').
- Q15 conditional 'requires'. PASS. F7 (grammar, unsupported claim).
- Q16 causal 'stabilizes'. PASS.
- Q17 conditional 'contingent on'. PASS.
- Q18 causal 'secured'. PASS. F7.
- Q19 conditional 'depends on'. PASS.
- Q20 causal 'sank' (figurative). PASS.
- Q21 conditional 'unless' (catalogued -> signed; the No...unless direction is right). PASS. Note: the prompt word 'condition' matches the conditional type pattern, so coach feedback that mentions 'condition report' can trip the generic-hint fallback. Minor, safe failure.
- Q22 causal 'yields'. 'prolonged' and 'deep' are not comparisons. PASS.
- Q23 comparative 'more extensive than'. PASS.
- Q24 comparative 'better than'. PASS. F8 (unclear 'capacity vs property').
- Q25 comparative 'stronger ... than' (split). PASS.
- Q26 causal 'because' (an actual cause, not argument support). F3 ('lower field' trap).
- Q27 conditional 'Only if' (viable -> 4 degrees); causal 'because'/'accelerates'. PASS. F4.
- Q28 comparative 'more evenly than'; causal 'since' (reason, not time). 'efficiently' is not a comparison. PASS on content. F1 example.
- Q29 conditional 'Only when'; comparative 'lower than' (8% benchmark); causal 'because'/'expands'. PASS. I did not judge wood-science plausibility.
- Q30 conditional 'Unless' (not thinner -> craze); comparative 'thinner than'; causal 'since'. PASS. Optional: 'different rates' could be accepted as another comparative indicator, but the type is already credited. F5 (rule 9 reuses this sentence).
- Q31 comparative 'heavier' / 'farther than' / 'larger'; causal 'which is why'. F3 ('larger' has no stated benchmark). The unstated step (a larger mould makes a heavier bell) goes unexplained. Editorial.
- Q32 conditional 'only when'; comparative 'exceeds'; causal 'dampens'. PASS.
- Q33 conditional 'Provided' (sufficient); comparative 'colder than'; causal 'because'. PASS.
- Q34 comparative 'harder ... than'; causal 'so'; conditional 'only if' (reserve -> stain-free). PASS. F1 (shared span credited under two types).
- Q35 causal 'Because'; comparative 'slower than' (earlier state); conditional 'unless' (grind -> dredged). PASS.
- Q36 conditional 'when' (sufficient: softer -> lasts longer, matching the arrow direction in DIRECTION); comparative 'longer'/'softer than'; causal 'because'/'drives'. PASS. F5 (spoiled by intro rule 7).
- Q37 conditional 'only if'; comparative 'more vigorous than'; causal 'since'/'starves'. PASS.
- Q38 conditional 'Only where' (necessary); comparative 'denser than' (60%); causal 'because'/'dries'. PASS. F7 (wording drops the threshold).
- Q39 conditional 'Only when'; comparative 'closer ... than' (three split forms); causal 'since'/'elevates'. PASS. Plausibility not judged.
- Q40 causal 'passivates'/'so'; comparative 'thicker ... than'; conditional 'provided' (sufficient, necessity correctly not claimed). PASS.
- Q41 conditional 'Unless' (concentrate -> exceeds); comparative 'exceeds'; causal 'because'. PASS on types. F6 (connects field).
- Q42 conditional 'only if'; comparative 'higher than'; causal 'since'. PASS on types. F6 (connects contradicts the 'inflate' note).
- Q43 causal 'lowers'/'which is why'; comparative 'faster ... than'. Correctly has no conditional ('at ambient temperature'). PASS.
- Q44 conditional 'Only where'; comparative 'lower than'; causal 'because'/'homogenizes'. PASS.
- Q45 conditional 'Provided' (sufficient); comparative 'finer than'; causal 'since'/'produces'. PASS on types. F7 (modality 'can').
- Q46 causal 'raises'/'so'/'offsets'; comparative 'higher than'; conditional 'unless' (not offset -> height result; no converse). PASS.
- Q47 conditional 'only when' (necessary); comparative 'above'/'higher still'; causal 'drives'. Feedback loop explained correctly. PASS.
- Q48 conditional 'Only if' (trusted -> regional curve); comparative 'more regionally appropriate than'/'more ... than'; causal 'because'/'produces'. PASS. Note: an unquoted 'more than' is credited locally as the two halves. Consistent with the rubric.

## Follow-up release published on 2026-10-25
Joshua authorized implementing confirmed findings, updating principles, independent final review and scoped publication. These fixes are live through [PR #240](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/240), merge eaf82e506bbeb3b5e86f1310f98bad3e818b926a. The initial final inspection caught a real recognition-versus-grading regression, which was fixed; a fresh Opus 5.5 session then APPROVED the final nine-file state. 231 tests, typecheck/build, four responsive component widths and three mocked publication guards passed. Only this work entered the merge. Shared design/principles.md links this audit and the committed activity brief records the reusable principles.

Production entry index-RIels5zf.js and reachable new answer-guidance markers were verified. The canonical 48-question activity was synchronized to the reviewed source and freshly read back. All four existing assignment snapshots and states were preserved; the one assigned copy retains its original saved bank. The revised preview and future assignments use the updated content. No live grader calls or signed-in production attempts were performed. Two low residual notes remain in the approving review: an existing unquoted wider-clause parsing edge case and preflight baseline semantics (mitigated for this release by not rerunning preflight and confirming original observation equals preflight). Optional curriculum reordering was not included. [Exact release receipt](../handoffs/claudex/spot-confirmed-fixes-20261025/release.json).

