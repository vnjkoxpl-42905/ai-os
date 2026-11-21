# Finish LR explanations: Brainstorm / Discovery Notes
Date: 2026-10-07 · Goal: decide what "finished" means for the LR explanations job and the fastest order to get there
Status: complete (plan confirmed 2026-10-07: Joshua said "go")
Context sources: corpus/lr-explanations/fixes/index.md, fixes/revamp-list.md, fixes/choice-note-issues.md, fixes/model-library-defects.md, fixes/side-issues.md, wiki/tasks.md

## Starting state (verified 2026-10-07, before questions)
- Coverage: 3,958 DB questions, all `is_explained`; gaps.py reported 3,957 Complete on 2026-10-03. The "772 missing" job is done.
- Types: bank and DB on the 18 canonical types (PRs #199, #200); sealed timed sittings keep frozen labels (PR #201, live).
- Open items in fixes/index.md: about 30. The big ones are quality, not coverage:
  - Revamp list: 523 weak existing explanations (192 Revamp, 100 Weak, 231 Watch) plus about 136 unread.
  - Model-library defects: 192 slot references (misread choices, wrong-claim Role, Logic Games analogies, mocking lines, political examples).
  - Choice Note problems: about 130 lines in choice-note-issues.md.
  - Side issues: bank misalignment (PT119-S2-Q19, PT101-S3-Q1), transcription damage, typos.
  - Housekeeping: PRs #138, #141, #142 open; two explanation paths (DB vs sidecar JSON); "Games-y LR" tag; 110 explained questions with no bank match.
- Assumption to confirm: "Alex for Nations" in the request is dictation for "LR explanations".

## Summary / key decisions
- The job is LR explanations (confirmed; "Alex for Nations" / "our explanations" are dictation).
- Done means (c): every correctness defect fixed, plus the 192 rated Revamp rewritten. The 331 Weak/Watch and about 136 unread stay queued.
- No review from Joshua. Claude self-checks every rewrite (independent second check against the question) and must be confident before writing.
- Housekeeping cleared without asking: PRs #138, #141, #142, the "Games-y LR" tag rename, the sidecar-vs-DB path, and worktree cleanup.
- Full autonomy to publish: guarded DB writes with snapshots and a log, and app PRs merged and deployed after tests pass.

## Q&A log
### Round 1
#### Q1 - Which job
- Asked: is "Alex for Nations" dictation for "LR explanations"?
- Recommended: yes.
- Captured: yes. Joshua: "Our explanations is what I meant to say" (dictation for LR explanations).
#### Q2 - Definition of finished
- Asked: (a) correct only, (b) correct and all weak rewritten, (c) correct plus the 192 Revamp.
- Recommended: (c).
- Captured: "go with what you recommended" -> (c).
#### Q3 - Review of rewrites
- Asked: Joshua reads all, samples 10%, or none.
- Recommended: (b), Claude writes and a second AI check runs, Joshua samples 10%.
- Captured: "I don't need any review so long as you're confident that you did it right. Just double check yourself." -> no Joshua sample. Claude self-checks every item.
#### Q4 - Housekeeping without asking
- Asked: merge #138/#141/#142, rename "Games-y LR", settle the two explanation paths, remove worktrees.
- Recommended: yes to all four; stop only on conflicts or failing tests.
- Captured: "Yes, you can clear the housekeeping without my permission. Yes, do to all four."
#### Q5 - Publishing without asking
- Asked: guarded DB writes live immediately; app changes deployed via free Lovable publish.
- Recommended: yes, with snapshots and a log.
- Captured: "You can publish the live site without asking. Yes, you have the complete autonomy to do that."

## Open flags (pending input)
