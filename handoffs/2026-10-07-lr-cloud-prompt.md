# LR explanations: Claude cloud handoff prompt
Prepared 2026-10-07. Draft for a separate cloud session. Supporting files and operational access must be supplied before it can finish the whole job. No cloud session has been started by this chat.

```text
Resume Joshua's LSAT U LR explanation completion job from the recorded pause below. You are running in a separate cloud workspace. Do not assume you can see Joshua's local disk, local Claude history, local credentials, or local tools. Read the supplied context and artifacts before working. Report precisely any missing dependencies; complete the work supported by your actual access without claiming unavailable steps were done.

SELECT CURRENT LOCAL SNAPSHOTS
Attach ai-os at codex/local-sync/laptop-le9a083p/ai-os and lsatu-684d89db at codex/local-sync/laptop-le9a083p/lsatu. These automatically published branches contain filtered current local work, including uncommitted files. Read .cloud-sync/workspace.json for freshness and original source commit, and .cloud-sync/conversations/index.json in AI OS for exported conversation context. Fetch the latest snapshot before starting. Never push to these sync branches; create your own work branch. setup/github-sync/README.md explains exclusions and Google Drive mirrors. Verify that these branches exist and contain the required files before proceeding.

GOAL AND SCOPE
Finish every verified correctness defect in the existing LR explanations, then rewrite the 192 entries rated Revamp, then finish remaining in-scope text/transcription/diagram cleanup. The model-library list's 192 defect references is a different, overlapping list, not another 192 rewrite questions. The 100 Weak, 231 Watch, and approximately 136 unread entries remain queued. Coverage work for the original 772 missing explanations is complete; do not restart it. The last recorded coverage was 3,958 DB questions with is_explained true and 3,957 complete explanations. These are historical counts, not a fresh production audit.

Joshua chose this scope on 2026-10-07. He wants an independent second check of every correction and rewrite against the actual question, with no personal review queue. Preserve student work. Previously authorized housekeeping includes PRs #138/#141/#142, explanation-path consolidation, the Games-y LR tag rename, and cleanup. Those PRs are already recorded as merged; do not redo them.

RECORDED RESUME POINT
1. App PR #202 made Choice Notes use the DB everywhere and was recorded live.
2. App PR #203 retired explanation sidecars, renamed Games-y LR to Rule Puzzle, and fixed PT114-S4-Q22's type. It merged as 7881dab3. A free deployment started, but the production check was interrupted by low local memory. Production publication was NOT confirmed. Check the actual deployed question and app assets before activating any new timed catalogs.
3. New timed catalogs were seeded and verified but NOT activated:
   PT: 99a8447852f183a955e0a21e1466a9480eef37069637b47f47a6c55f29d5b926
   Sections: 45ef6f554a1f1c402aa9f87d61326d17f16642a953757a8fb71d33b910e9aae1
   Recheck live configuration and bank/catalog parity first. Preserve old manifests and sealed sittings. PR #201 already addressed frozen LR classification for sealed sittings.
4. Step 2 correction proposals are local artifacts, not applied changes. Slice C has 176 proposed edits, a pronoun-corrected edits-C.json, and no completed independent verification file. Slices A/B/D contain partial proposals and must be resumed by reconciling against their assigned lists. Do not throw away or blindly apply partial output. No step-two proposals were recorded as written to the DB.
5. Finish and independently verify step 2, then proceed to the 192 Revamp rewrites, then reconcile remaining in-scope issues and verification.

REQUIRED CONTEXT AND DATA
Locate these files in the supplied package or repository; resolve paths inside your own workspace:
- brainstorms/2026-10-07-finish-lr-explanations.md: Joshua's approved scope and autonomy.
- handoffs/2026-10-07-lr-cloud-context.md, if supplied: detailed source reconstruction and slice assignments.
- corpus/lr-explanations/fixes/index.md, choice-note-issues.md, model-library-defects.md, side-issues.md, revamp-list.md, revamp-inventory.csv, and relevant adjudication records.
- corpus/lr-explanations/golden-set.md and golden-set-observations.md; models/index.md and relevant models/*.md. Read model weaknesses; do not reproduce their defects.
- wiki/teaching-voice.md, wiki/COPY-CORRECTIONS.md, references/lsat-teaching-voice-standard.md, and project-owned lsat-u-voice skill.
- Five DB snapshots: lr_questions.json, lr_answer_choices.json, lr_explanations.json, lr_explanation_steps.json, lr_explanation_choice_notes.json. Snapshot dates matter; refresh against live data where access permits.
- LSAT U app repository vnjkoxpl-42905/lsatu-684d89db, including public/data/PT*-S*-LR.json and its own instruction files. The ai-os repository is separate: vnjkoxpl-42905/ai-os. Neither clone automatically includes the other's local files.
- Preserved pause artifacts are now in corpus/lr-explanations/work/2026-10-07-resume/step2/: BRIEF.md, VERIFY.md, out-A.jsonl, out-B.jsonl, out-C.jsonl, out-D.jsonl, edits-C.json, check.py. Catalog evidence is in the sibling rot3/ folder. PROVENANCE.md and SHA256SUMS.json document all 13 byte-verified copies. Use those portable repository paths. The original Windows Temp scratch root remains unchanged and does not exist in your cloud VM.

CORRECTION METHOD
The bank is the question students actually read and are graded on. Read the stimulus, stem, five choices, key, and complete explanation. Reconcile DB/bank differences before making a semantic judgment. Check every affected style: standard, brief, another_way, single. A prior issue list or proposal can be wrong or already fixed. Record justified skips and explicit flags.
For step 2, make the smallest correct edit. Preserve surrounding sound writing. Allowed proposal fields are lr_explanation_steps.body, lr_explanation_steps.label, and lr_explanation_choice_notes.body. Never silently change the credited choice. Suspected key or question-text defects require separate adjudication.
Use the exact proposal schema and ownership lists in step2/BRIEF.md and the context note. Every row proposal includes its identity, exact full old value, full new value, reason, and question evidence. Detect duplicates and conflicting replacements before applying.
Have a separate review pass independently solve the question and assess the proposed replacement. Revise failures, recheck, and apply only passed changes. Maintain durable per-item states: proposed, reviewed, revised, applied, skipped, flagged.
For DB writes, refresh current values, keep a before snapshot, and use compare-and-swap guards on the row identity and exact old value. A mismatch is a conflict to reconcile, not permission to overwrite. Verify affected-row counts and reread results. Preserve logs and rollback evidence.

WRITING AND REWRITES
No em dashes or gendered pronouns for people in the stimulus. Use names, the author, or they. No Logic Games analogies, mocking/political asides, filler, unsupported outside facts, invented quotations, or broad false rules. Teach the reasoning through concrete steps. Preserve modality and logical direction.
For the 192 Revamp items, write the complete breakdown and all five Choice Notes appropriate to the actual type and approved structure. Model quality comes from the reasoning, not length: evaluate the argument, predict the answer's content, demonstrate the test for each choice, explain the tempting trap, and teach a transferable move. The current Joshua-selected voice standard takes precedence over older reference habits.

ACCESS AND EXECUTION
Inspection on 2026-10-07 confirmed that both required repositories appear in the cloud repository picker. The Default environment has Full network access, no setup script, no environment variables, and no network secrets. Lovable is Connected at account level and checked in the new cloud task's Connectors menu. LSATU App needs reconnection; the separate Supabase connector is not connected. Use the enabled Lovable connector, but first inspect its actual tools and perform a read-only project/query probe. Account connection alone does not prove access to this specific project's tables or deployment controls. Attach both repositories explicitly; local-only scratch and uncommitted files still need transfer.
Both repositories were accepted together at main in the unsent composer. The ai-os GitHub main inspected on 2026-10-07 was 7e3a37c49aad80bc3d36352b796612425fe9b051 from 2026-10-02. It predates the latest approved plan and paused work. Do not use that old clone as a substitute for the accompanying current transfer artifacts.
The local job used free Lovable query_database and deploy_project for project 53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76. Those integrations and authorizations do not create credentials or tools in a cloud session. Confirm actual access. Never put secrets in chat, handoff files, commits, or output artifacts. Never spend Lovable credits. Lovable Cloud Edge Functions follow the project's Lovable deployment route; do not substitute Supabase CLI deployment.
Joshua authorized guarded live DB writes and free app publishing for this job after successful checks. Operate only with available, appropriately authorized access. If live access is absent, finish independently reviewed proposals and return a ready-to-apply package, explicitly marking production verification, activation, application, or deployment as pending. Do not fabricate completion.
For app edits, obey the app repository instructions, use an isolated branch and PR, run relevant checks, and include only this job's changes. Do not overwrite unrelated local or remote work. Avoid simultaneous writers for the same question or row.

DELIVERY
Keep a durable progress ledger so the job survives compaction and cloud restarts. Reconcile every in-scope issue and all 192 Revamp entries. Report what was corrected, independently reviewed, actually applied, and verified live; list unresolved flags and exact reasons for any skipped steps. Keep the Weak/Watch/unread backlog separate. Return changed files, review evidence, before/after records, and precise continuation instructions for any remaining operational steps.
```
