---
type: task-list
subject: Fix list, LR explanation project
updated: 2026-10-02
---

# Fix list

The one running list of everything to fix that turns up while working on LR explanations. One line per item here. Anything that needs more than a line gets its own file in this folder, linked from its item. Strike items through with a date when done.

The database is the source of truth for explanations, not the local `Explanations/*.md` files.

## Open

### Explanation content
- [x] ~~**Load the approved 20-question explanation pilot.**~~ 2026-09-28: loaded 20/20 with guarded, insert-only SQL after snapshotting the affected rows. Fresh pull verified +3 questions, +18 explanations, +76 steps, +95 choice notes, and +15 answer choices. All 20 have contiguous steps and five A-E notes; the basic gap count fell from 560 to 540. Including seven partial-note slots, 547 remain.
- [x] ~~**Load approved batch 01 (40 Flaw explanations).**~~ 2026-10-01: Joshua approved; fresh pull showed source rows unchanged (regenerated SQL byte-identical), snapshot `raw/sources/lsatu-lr-snapshots/2026-10-01-pre-batch01-load.json`, then 40/40 guarded per-slot transactions via Lovable SQL. Fresh pull verified +38 explanations, +156 steps, +200 notes; questions, choices and keys unchanged; every slot byte-identical to its prepared SQL, contiguous steps, notes A-E; PT102-S3-Q14 and PT119-S2-Q24 kept their four existing steps. All 40 targets were incomplete and are now complete, so the gap falls by 40 (547 to 507 if the 2026-09-28 baseline held; DB-only count of LR questions lacking steps plus A-E notes is now 331 of 3,782).
- [x] ~~**Batch 02 bank issues.**~~ 2026-10-01: fixed in vnjkoxpl-42905/lsatu-684d89db#184 (PT107-S3-Q7 spacing, PT120-S1-Q8 hyphen, Parallel Flaw tags for PT147-S4-Q16 and PT156-S4-Q24). PT127-S1-Q4 was already fixed on main.
- [x] ~~**`gaps.py` and `neighbors.py` use stale paths.**~~ 2026-10-01: gaps.py now uses `project_paths`, fails loudly if the bank is missing, and counts partial-note slots. neighbors.py still depends on pilot `picks.json`; batch drafts pick models from `models/*.md` by sub-pattern instead.
- [x] ~~**Load batch 02 (40 Flaw).**~~ 2026-10-01: 40/40 loaded and verified byte-for-byte; gap 507 -> 467. Generator: `system/scripts/lr-explanations/generate_batch02_sql.py`.
- [ ] **Generators read the `lsatu-wt-glossary` worktree, which lags main.** Point batch generators at the current main checkout (or a fresh worktree) before batch 03.
- [ ] **Pilot source-text differences to adjudicate:** PT116-S2-Q19 and PT117-S3-Q8 have speaker paragraphs joined in the DB stimulus; PT117 also has damaged apostrophes. The bank and pilot agree; no existing stimulus was overwritten during the add-only load. PT105-S4-Q12(E)'s extra DB "the" was corrected 2026-09-28 after a snapshot and source check.
- [ ] **PT159-S1-Q21 bank text contains damaged apostrophes.** The unloaded question and choices were inserted from the bank verbatim on 2026-09-28, preserving bank/DB agreement. Repair the bank on an app branch and PR, then align the DB source text only after the wording is verified.
- [ ] **Pilot metadata and future reingest:** 15 existing pilot `lr_questions.is_explained` flags remain false under the add-only rule, though the current frontend reads the explanation rows directly. The app's `ingest-lr-explanations.mjs` deletes and rebuilds steps/notes for staged rows. Preserve authored pilot prose before any future reingest.
- [x] ~~**LSAT Lab has a written Argument Breakdown for 247 questions LSAT U lacks.**~~ 2026-09-27: 221 loaded from the full app text (26 are video-only, skipped). Verified: all 221 have steps, 0 glued emphasis markers. +760 steps, +60 choice notes, +8 questions, +12 explanations. About 551 of the 772 remain to write. Corrected 2026-09-27 (Codex review): at least 567 slots are incomplete, counting 7 with a breakdown but only 3 or 4 notes; re-run gaps.py after a fresh pull for the true number.
- [x] ~~**Full LSAT Lab audit flags (2026-09-27).**~~ 50 flags verified: 19 real, 29 false alarms, 2 unclear. Fixed in PR vnjkoxpl-42905/lsatu-684d89db#151 (11 stems, 3 choice sets, keys PT128-S2-Q5→C, PT139-S4-Q22→E, PT149-S4-Q14→B, Joshua approved) and #150 (PT101-S2-Q8 truncated stimulus). Verdicts: scratchpad flags/verdicts.json (not kept).
- [x] ~~**PT128-S2-Q26 is a copy of PT124-S2-Q26 with the wrong key (E, real B); LSAT Lab's PT128 S2 has 25 questions.**~~ 2026-09-27: it is modern PT124-S2-Q26 (old PrepTest 41, S3, Q26), confirmed on 7Sage; 7Sage, LSAT Lab and the DB all end PT128 S2 at Q25. Zero attempts, runs or journal rows. Deleted from the bank (not `status: removed`, which means an LSAC-removed position) in PR vnjkoxpl-42905/lsatu-684d89db#153. Origin unknown: already present in the recovered 2026-09-05 snapshot, so git has no earlier history.
- [ ] **Two unclear choice spellings, no PDF:** PT102-S4-Q2 C ("ensure" vs LSAT Lab "insure"), PT104-S4-Q8 A ("Packaging" vs "Packing"). Wrong answers, low stakes.
- [ ] **Database carries LSAT Lab typos in 4 stimuli:** PT108-S2-Q18 "grass:", PT141-S2-Q5 "Lemaitre", PT143-S1-Q13 "Bums", PT143-S4-Q1 "Trinidadians". Bank is right; DB copy is not shown to students but feeds the guard fixture.
- [x] ~~**Answer-key test fails on PT118's two removed questions** because it doesn't skip `status: removed`.~~ 2026-09-27: test skips them, PR #153 (PT118-S3-Q22 confirmed removed from scoring on 7Sage).
- [ ] **~364 bank rows have hard PDF line breaks inside text** (rough count). Separate cleanup.
- [x] ~~**Five explanations belong to a different question** (students see reasoning for the wrong question). PT108-S3-Q6 (whole explanation, even the stimulus), PT137-S3-Q25, PT143-S4-Q18, PT135-S4-Q25, PT133-S3-Q4. Highest priority. Detail: [[side-issues]] section 1.~~ 2026-09-27: PT108-S3-Q6 was the bank's fault (fixed by #146); the other four had wrong speaker names, corrected in the DB. Snapshot: raw/sources/lsatu-lr-snapshots/2026-09-27-wrong-speaker-rows-pre-fix.json.
- [x] ~~**PT158-S4-Q22 breakdown steers students to D; the key is E.** Rewrite the breakdown. Detail: [[side-issues]] section 2.~~ 2026-09-27: Conclusion, Evaluate and Goal rewritten in the DB. Snapshot: raw/sources/lsatu-lr-snapshots/2026-09-27-pt147-pt158-rows-pre-fix.json.
- [ ] **Revamp weak existing explanations: 523 found** (192 Revamp, 100 Weak, 231 Watch), plus ~136 unread rows that probably rate Weak. Joshua does this later, after the 772. Detail: [[revamp-list]]; scores in `revamp-inventory.csv`.
- [ ] **Empty or partial explanations:** 2 with nothing, 16 with no choice notes, 8 with some notes missing, 2 placeholder correct-answer notes (PT147-S4-Q3 D, PT147-S4-Q4 A: written 2026-09-27, done). Detail: [[side-issues]] section 4.
- [ ] **Existing explanations with defects found while building the model library (2026-09-27): 192 slot references.** Misread choices (PT146-S3-Q1 correct note reads "unlikely to be unrepresentative"; PT128-S2-Q19 B; PT101-S2-Q25 C/D describe choices not on the page), a Role explanation of the wrong claim (PT154-S2-Q18), Logic Games analogies in student copy (PT137-S4-Q3, PT107-S4-Q2 A), mocking lines, political examples, flattened diagrams. Revamp track. Detail: [[model-library-defects]].
- [ ] **Bank/database answer-choice wording disagreements.** Twenty-one named slots repaired on 2026-09-28: fifteen bank slots (22 choice texts) in merged PRs #181, #182, and #183, plus six database slots (seven choice texts) with guarded updates and snapshots. Two further slots have documented source-version differences and no edit. PT104-S1-Q4 A and PT134-S1-Q12 E still need stronger wording sources; other differences remain to inspect. Detail: [[choice-adjudication-2026-09-28]]. PT148-S3-Q26 D was already fixed in PR #154.
- [ ] **Fix individual Choice Note problems.** Misquotes, reversed logic, typos, verdict-only notes. Detail: [[choice-note-issues]].

### Data and question bank
- [x] ~~**Tag the 128 rebuilt questions.**~~ Done 2026-09-27: all 155 repaired slots tagged from LSAT Lab (the 27 moved ones also carried the wrong labels), PR vnjkoxpl-42905/lsatu-684d89db#147 merged. Tool: system/scripts/lsatlab-pull/.
- [x] ~~**304 bank questions had labels that differ from LSAT Lab's current tags.**~~ Joshua chose LSAT Lab's; applied 2026-09-27, PR vnjkoxpl-42905/lsatu-684d89db#148.
- [x] ~~**The question bank holds the wrong question in 155 slots** (verified 2026-09-27, replaces the "18 wrong keys" item). Whole blocks were copied from another section: PT113-S3 holds PT112-S3; PT117-S2 holds PT116-S2; PT119-S2/S3 hold PT113-S2/S3; PT129-S3 holds PT128-S3; PT148-S4 holds PT142-S4; PT149-S3 holds PT148-S3; smaller runs in PT101, PT116, PT117-S3, PT129-S2, PT130-S3, PT131-S2/S3, PT154-S4, PT155-S4. The app shows and grades from the bank, and shows explanations from the database, so in these slots the student answers one question and reads the explanation for another. The database text is right (web-checked PT113-S3-Q21 on 7Sage, LSAT Lab and LSAT Hacks). 28 correct questions already sit elsewhere in the bank and can be moved; 127 need their answer choices sourced.~~ Fixed 2026-09-27 in PR vnjkoxpl-42905/lsatu-684d89db#146 (27 moved, 128 rebuilt from the official PDFs, 5 nonexistent rows removed). Verified merged at 2026-09-27 06:51 UTC with `gh pr view` on 2026-09-28.
- [ ] **Bank misalignment:** PT119-S2-Q19 is matched to a different question, and PT101-S3-Q1's bank text differs from the DB. Detail: [[side-issues]] section 3.
- [ ] **Transcription damage, LSAT Lab leftovers, and small typos in explanations.** Detail: [[side-issues]] sections 5, 6 and 8.
- [ ] **Rename the "Games-y LR" feature tag.** There are no Logic Games on the LSAT.
- [x] **Question bank `questionType` is unreliable.** 110 raw variants, casing duplicates, some wrong (PT151-S2-Q13 is a Paradox, bank says Most Strongly Supported; PT143-S1-Q6 is a Paradox, bank says Strengthen). Needs a canonical ~25-type set. **Fixed 2026-10-03** (type sweep, see below).
- [ ] **110 explained questions have no match in the question bank** (`public/data/PT*-LR.json`), so they have no features or difficulty.
- [ ] **Reasoning-type names don't match the glossary.** Data: "Conditional Reasoning". Glossary: "Conditional Logic".
- [ ] **PT123 to PT138 are thin.** 362 words on average, 51% Complete. Check whether some "Complete" ones are too thin to count.
- [ ] **Diagrams lose their layout in the database.** PT107-S3-Q5 (chain flattened to inline text), PT146-S1-Q21 (transcription damage). Count how many render badly in the app.

### App and loading
- [ ] **The app has two explanation paths.** `useLrExplanation` reads the database; `questionLoader.mergeExplanationSidecars` also fetches `public/data/explanations/PT<n>-explanations.json`, built from the local markdown for PT139 to PT159. Find out which one students see, and retire the sidecars if the database has replaced them. Until then, the PT140 sidecar JSON still carries the thin text.
- [x] ~~**Where the LSAT U writer mark (Explanation Source) lives.**~~ 2026-09-27: Joshua dropped it; not needed.
- [ ] **`targeted-questions/` layout is unreadable by the parser.** PT134-S1-Q16 and PT158-S4-Q24, in LSAT U's voice. Convert and load, or drop.

### Student-visible question text (found in batch 04, 2026-10-01)
- [x] ~~**Speaker turns run together in the database stimulus.**~~ 2026-10-01: line break added in 99 questions (PT111 to PT126), guarded update, verified against snapshot `raw/sources/lsatu-lr-snapshots/2026-10-01-pre-stimulus-fix-lr_questions.json`. Students never saw this: the app reads question text from the bank, not `lr_questions.stimulus`.
- [x] ~~**PT113-S3-Q2 database stimulus says "silverfleaf".**~~ 2026-10-01: fixed to "silverleaf".
- [x] ~~**PT110-S3-Q3 wording differs.**~~ Fixed: "epidemic". Database "endemic", bank "epidemic". Check the printed PT and make both match it.
- [x] ~~**Word-level mismatches between bank and database.**~~ 2026-10-01: settled from screenshots of the printed tests. DB fixed: PT110-S3-Q3, PT111-S1-Q26, PT111-S3-Q10. Bank fixed in PR #185: PT111-S3-Q10 line break, PT112-S4-Q13/Q14 em dashes, PT120-S1-Q25 hyphen. (The earlier "duplicated passage" note was wrong; it was dash and hyphen loss.)
- [ ] **Bank-only issues.** PT114-S4-Q22 typed "Necessary Assumption EXCEPT" in the bank but is plain NA (the database type is correct). PT106-S1-Q12 bank stimulus starts with "The following passage is used for Section 1, questions 12 through 13."
- [x] ~~**Generator defaulted unloaded questions to type Flaw and could not add steps alone.**~~ 2026-10-01: `generate_batch_sql.py` now uses the draft's type and handles steps-only slots.

### Found in batch 05 (2026-10-01)
- [x] ~~**PT119-S3-Q20 has two overlapping step sets.**~~ 2026-10-02: not duplicates; three styles (standard, brief, another_way). Five notes added to the standard explanation in batch 06, nothing deleted. Its standard explanation carries ten steps (two Conclusion/Evidence/Evaluate/Goal runs plus "The Argument"), and its notes sit under other styles. Decide which set to keep before adding anything.
- [x] ~~**PT149-S4-Q16 stimulus is missing its blank.**~~ 2026-10-01: "Hence, _______." added in DB and bank (PR #187). The bank (what students see) ends at "...increase their savings rates." with no "Therefore, ___" line. Needs the printed wording from a screenshot.
- [x] **Bank type labels that disagree with the stem.** PT149-S4-Q16 (bank: Necessary Assumption; stem is a fill-in completion) and PT105-S1-Q12 (bank: Method; it is Parallel, and the database already says Parallel). **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.
- [x] ~~**PT107-S3-Q11 "obscures the stars Many".**~~ 2026-10-01: period added in database and bank (PR #186).

### Found in batch 06 (2026-10-02)
- [x] ~~**Batch 06 loaded.**~~ 40/40 verified byte-identical 2026-10-02. Gap 307.
- [x] **PT111-S3-Q7 DB stimulus runs speakers together** ("percent.Proponent of offshore oil drilling:"). The speaker regex skipped multi-word names. Low priority: students read the bank. **Fixed 2026-10-03** (type sweep, see below). The bank copy had the same defect; fixed in PR #200.

### Found in batch 07 (2026-10-02)
- [x] ~~**Batch 07 loaded.**~~ 40/40 verified byte-identical. Gap 267. Agree/Disagree has no gaps left.
- [x] ~~**Bank text: PT117-S2-Q6, PT111-S4-Q26 speakers run together; PT156-S2-Q7 stem missing "Ms."**~~ Fixed in PR #188.
- [x] **Bank type labels wrong:** PT156-S2-Q7 (bank: Agree/Disagree, is Method) and PT156-S2-Q21 (bank: Agree/Disagree, is Flaw). The database has the right types. **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.
- [x] ~~**Unloaded questions lose speaker line breaks in the database stimulus.**~~ 2026-10-02: generator fixed; the six batch-07 rows updated. `norm_text` joins single newlines, so batch-loaded dialogues read "...guidance. Miriam:". Students read the bank, so low priority; fix `generate_batch_sql.py` to keep a break before a speaker label.

### Found in batch 08 (2026-10-02)
- [x] ~~**Batch 08 loaded.**~~ 40/40 verified. Gap 227. Most Supported has no gaps left.
- [x] ~~**Hyphenated words split at line wraps show a stray space to students** ("long- term").~~ PR #189 joined 18 plus "one- fourth".
- [x] **Bank type labels wrong on PT156 and PT159 unloaded questions.** Bank says "Most Strongly Supported" for PT142-S1-Q9, PT143-S4-Q12, PT156-S2-Q3 (Paradox), PT156-S2-Q17 (Must Be True), PT156-S4-Q19 (SA), PT156-S4-Q21 (Principle), PT159-S1-Q8 (Strengthen). The database has the right types. Many PT140+ bank type labels look unreliable; worth a full audit. **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.

### Found in batch 09 (2026-10-02)
- [x] ~~**Batch 09 loaded.**~~ 40/40 verified. Gap 187. Principle-Conform, "Principle Conform", plain "Principle" and Principle-PSA have no gaps left.
- [x] ~~**PT119-S2-Q15 choice E showed "jalape�o".**~~ PR #190 restored the ñ. A full scan of the LR bank found no other replacement characters.
- [x] **Bank type labels wrong on eight unloaded Principle questions.** Filed as Principle-Conform or Principle, but they ask for a justifying principle: PT132-S4-Q20, PT143-S3-Q3, PT144-S2-Q6, PT145-S4-Q1, PT156-S2-Q12, PT156-S4-Q26, PT159-S1-Q14, PT159-S3-Q1. Loaded as Principle-Strengthen; the database has the right type. Add to the PT140+ label audit. **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.
- [x] **DB stimulus defects on two loaded questions (students read the bank, so low priority):** PT118-S3-Q8 runs the speakers together ("inhabit them.Figorian Development Commission:"), and PT109-S3-Q6 says "asthetic" where the bank says "aesthetic". **Fixed 2026-10-03** (type sweep, see below).

### Found in batch 10 (2026-10-02)
- [x] ~~**Batch 10 loaded.**~~ 42/42 verified. Gap 145. Every Principle label and every Main Conclusion label now has no gaps.
- [x] ~~**Three bank text defects.**~~ PR vnjkoxpl-42905/lsatu-684d89db#192: PT146-S3-Q6 "seize one's of these", PT124-S2-Q18 and PT138-S3-Q11 had hyphens or nothing where the dashes belong. Fixed before loading, so the two new DB rows carry the corrected text.
- [x] **Bank type labels wrong on six more unloaded questions.** Loaded with the type the stem asks for: PT141-S2-Q4 ("PSA") and PT147-S4-Q13 ("Principle Justify") as Principle-Conform, PT146-S3-Q6 ("Principle Justify") as Principle-Strengthen, PT141-S4-Q4 ("Method of reasoning or descriptive (Principle)") as Method, PT147-S4-Q17 ("Identify The Conclusion") as Main Conclusion, PT156-S4-Q6 ("Main Conclusion", a role stem) as Role. Add to the PT140+ label audit. **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.
- [x] **DB stimulus defect, PT110-S2-Q20:** "society-largely" has a hyphen where the dash belongs, and the bank has "society— largely" with a stray space. Low priority. **Fixed 2026-10-03** (type sweep, see below). Both copies now read "society—largely".
- [x] ~~**Tooling: `generate_batch_sql.py` reads the live DB pull.**~~ Fixed 2026-10-02: the first run copies the five tables into `work/batch-NN-inputs/db-frozen/` and later runs read that copy. Delete the folder to refreeze.

### Found in batch 11 (2026-10-02)
- [x] ~~**Batch 11 loaded.**~~ 45/45 verified. Gap 100. Every Must Be True label and the Weaken label now have no gaps.
- [x] ~~**Bank soft hyphen, PT105-S4-Q9.**~~ Deployed 2026-10-02 with `726ca50` after Joshua cleared it (deployment `09a8bdf4`); confirmed live. "long ­established" carried a stray soft hyphen. PR vnjkoxpl-42905/lsatu-684d89db#193 merged as `1071efe`, **not deployed**: main also carries `726ca50` (Stripe session auto-credit, another session's work), so a deploy would ship non-LR work. Deploy once Joshua clears `726ca50`. The DB row for this question was already loaded and reads "long established" (no hyphen); low priority.
- [x] ~~**Possible soft hyphen in PT106-S1 bank file.**~~ 2026-10-02: false alarm. No U+00AD in the file; the byte grep matched the second byte of "í" (C3 AD) in "Rodríguez".
- [x] **Bank type labels wrong on six more unloaded questions.** Loaded with the type the stem asks for: PT144-S4-Q1, PT145-S4-Q24 ("Must be true"), PT156-S2-Q18, PT156-S2-Q25, PT156-S4-Q22 ("Must Be True") as Sufficient Assumption; PT156-S4-Q23 ("Must Be True") as Flaw. Add to the PT140+ label audit. **Fixed 2026-10-02** in vnjkoxpl-42905/lsatu-684d89db#194 / #198, deployed.
- [x] ~~**Type label wrong, PT119-S3-Q5.**~~ 2026-10-02: filed wrongly as a DB label. The DB already said Main Conclusion; the bank said Weaken. Fixed in the bank, vnjkoxpl-42905/lsatu-684d89db#195.
- [ ] **`gaps.json` state names read backwards.** "Steps-only" means the slot has steps and needs notes; "Notes-only" means it has notes and needs steps. The generator's names are the opposite. Rename in `gaps.py`.

### Found in batch 12 (2026-10-02)
- [x] ~~**Batch 12 loaded.**~~ 44/44 verified. Gap 56. Every Parallel and Parallel Flaw label (all spellings) now has no gaps. No bank text defects found, so no deploy needed.
- [x] ~~**Merged remote branches deleted**~~ on Joshua's OK: `fix/lr-bank-batch02-text`, `-batch10-text`, `-batch11-text`, `fix/lr-bank-jalapeno` (PRs #184, #192, #193, #190, all merged).
- [x] ~~**Type label wrong, PT105-S1-Q13.**~~ 2026-10-02: filed wrongly as a DB label. The DB already said Method; the bank said Parallel. Fixed in the bank, vnjkoxpl-42905/lsatu-684d89db#195.
- [x] ~~**Bank type label wrong, PT137-S2-Q5.**~~ 2026-10-02: fixed in vnjkoxpl-42905/lsatu-684d89db#194. Filed as "Parallel Reasoning"; it's a fill-in-the-blank. Loaded as Most Strongly Supported. Add to the PT140+ label audit.

### Found in batch 13 (2026-10-02)
- [x] ~~**Batch 13 loaded.**~~ 56/56 verified. Gap 0: every LR question in the bank now has steps and A-E notes (Complete 3957).
- [x] ~~**21 bank type labels wrong on batch 13 questions**~~ (Miscellaneous, Unknown, Flaw or descriptive weakening, role and completion variants). Fixed in vnjkoxpl-42905/lsatu-684d89db#196 to match the DB rows.
- [x] **Label sweep: 516 bank-vs-DB type disagreements.** A family-level comparison of every bank `questionType` with the DB `question_type`. A stem check puts about 331 on the bank side, 113 on the DB side and 72 unclear. Both sources need a canonical taxonomy before a bulk fix; bank labels drive drill filters and bootcamp pools. Evidence: [label-sweep-2026-10-02.txt](label-sweep-2026-10-02.txt). **Fixed 2026-10-03** (type sweep, see below).
- [x] **DB type label, PT122-S1-Q8.** Stored as Strengthen; the stem asks for an explanation (Paradox). Explained as Paradox. Part of the sweep above. **Fixed 2026-10-03** (type sweep, see below).
- [x] **DB stimulus soft hyphen, PT133-S2-Q25.** "cross­ examined" carries U+00AD plus a space. Same defect class as PT105-S4-Q9. **Fixed 2026-10-03** (type sweep, see below). All 32 DB rows with U+00AD now carry the bank's rendering.
- [x] **`is_explained` is false on 327 explained DB questions.** Nothing in `src/` reads it (only `types.ts`), so students see no effect. Set it in a later guarded UPDATE or drop it. **Fixed 2026-10-03** (type sweep, see below). 346 rows set; all 3958 now true.
- [x] **Two bank records have no `questionType`.** One in `PT118-S1-LR.json` (has a `status` key) and one in `PT118-S3-LR.json`. 2026-10-03: no fix needed; both are `status: removed` (PT118-S1-Q5, PT118-S3-Q22) and never reach students.
- [ ] **Bootcamp test failing on main.** `practiceDrillPools.test.ts`: the first-sentence pool lists PT131-S3-Q9 (difficulty 1) after PT128-S2-Q13 (difficulty 4). Unrelated to labels; spun off as its own task.
- [x] ~~**Verifier missed multi-line stimuli.**~~ The batch verify script parsed the SQL line by line, so dialogue stimuli with a speaker break read as a mismatch (PT144-S4-Q2). Fixed in the scratch verifier; copy `verify13.py` forward, not `verify12.py`.

### Type sweep and timed catalogs (2026-10-03)
- [x] **Taxonomy decided:** the app's 18 `CANONICAL_QTYPES` are the standard. EXCEPT is the `EXCEPT` feature tag, not part of the type name. Where `TYPE_SYNONYMS` has an opinion, it rules: "best illustrates / conforms to" and "principle violated" are Principle-Conform; "justifies the application of the principle" is Principle-Strengthen; misinterpretation is Flaw. Per-question record: [type-sweep-2026-10-02-verdicts.json](type-sweep-2026-10-02-verdicts.json).
- [x] **Bank:** 435 `questionType` values corrected, 88 stem-inferred labels made explicit, 12 EXCEPT tags added. PR vnjkoxpl-42905/lsatu-684d89db#199, deployed and confirmed live on 2026-10-03; all 156 live files match main. Record: [type-sweep-2026-10-02-bank-changes.json](type-sweep-2026-10-02-bank-changes.json).
- [x] **DB:** 1081 `question_type` values set to canonical names plus " EXCEPT" (196 changed the type, 885 spelling only), applied with guarded batches. Record: [type-sweep-2026-10-02-db-changes.json](type-sweep-2026-10-02-db-changes.json).
- [x] **Live regression found and fixed: timed PrepTests and timed sections.** The frozen catalogs pin each question's type and content hash. #194–#198 and the earlier text fixes left 28 timed LR sections failing "LR classification differs from the frozen manifest" in production. #199 rotated the catalogs to PT `a8d93989` and sections `17067cd1`, seeded insert-only, checked with `md5` per row, and activated after the deploy. Scripts: [timed-catalog-rotation/](timed-catalog-rotation/).
- [x] **Bank stimulus typography:** 10 jammed speaker turns ("kind.Anna:") and 13 em dashes with a stray space. PR #200 rotates the catalogs again (PT `dae8f144`, sections `e3942b59`).
- [x] **Last noncanonical DB type:** PT118-S3-Q22 (bank-removed) read "Must be True"; set to "Must Be True" with a guarded UPDATE on 2026-10-03. All 3958 `question_type` values are now canonical.
- [x] **DB stimulus cleanup:** 32 soft hyphens, 8 named defects, and 13 more speaker or dash defects. All guarded UPDATEs.
- [ ] **Joshua's own timed QA sittings are pinned to old catalogs.** Runs 246a92e0 (PT104) and 757f339d (PT106) are in progress, and the QA runs are on `cacaf2b0`. They may not reopen where their questions changed. No student sittings exist.
- [x] **Relabels no longer break sealed sittings.** Joshua chose option (a) on 2026-10-07. PR #201 (`65c9c958`), deployed and confirmed live 2026-10-07: sealed PT and section sittings keep their frozen qtype and level. Text fixes still change content hashes, so they still need catalog rotation and still break older sittings.
- [ ] ~~**Design question for Joshua:**~~ any future bank type or text fix breaks every sealed sitting that contains that question. That is harmless now, but once students have timed history it will not be. Options: (a) let verification accept the frozen classification and treat content hashes as the integrity check, or (b) freeze bank edits after go-live.
- [ ] **2047 mid-sentence hard wraps in bank stimuli.** `normalizeProseHardWraps` joins them at render, so students see clean text. Cosmetic only.

### Repo housekeeping
- [x] ~~**Codex's redundant repair branch and worktree.**~~ 2026-09-27: deleted on Joshua's OK. Its uncommitted changes kept at raw/sources/lsatu-lr-snapshots/2026-09-27-codex-repair-worktree-uncommitted.patch.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#138** (PT154 parser fix), then remove the `projects/lsatu-wt-parser` worktree.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#141** (glossary), then remove the `projects/lsatu-wt-glossary` worktree.
- [ ] **Merge PR vnjkoxpl-42905/lsatu-684d89db#142** (removes the thin local `PT140-explanations.md`).
- [ ] **Repo `CLAUDE.md` says commit straight to `main`; memory says branch + PR per session.** One should change.

## Done
