# LR cloud transfer: reconstructed context
Prepared 2026-10-07. Read-only reconstruction; production state was not independently revalidated.

## What was read
Main Claude session: `C:/Users/Joshu/.claude/projects/C--Users-Joshu-dev-ai-os/ea3d04fb-872d-45e2-bfa6-a69f0373cb16.jsonl`, 3,244 records, ending `2026-10-07T21:57:17Z`. Reviewed user/assistant prose, compaction narrative, linked approved finish plan, fixes index, revamp introduction, relevant latest log, scratch briefs, and delegation assignments. Not every historical tool payload or the complete older predecessor transcript was read. The imported Codex thread `01a102c4-6ecb-7100-a938-10927cbb393a` is an older snapshot and misses the latest work. No newer matching top-level transcript was found in the checked Claude project directory.

## Definition of finished
Joshua selected correctness fixes plus 192 Revamp rewrites, with independent second checks and no Joshua sample review. The 100 Weak, 231 Watch, and approximately 136 unread stay queued. The model-library list's 192 defect references is a different, overlapping list, not another 192 rewrite questions.

Phases: housekeeping; real correctness/choice-note/bank defects; 192 Revamp rewrites grouped by type; smaller text/transcription/diagram cleanup. Some cleanup is already included in slice D. Original 772 missing-explanation coverage is complete. Historical coverage counts: 3,958 DB rows marked explained and 3,957 bank-complete slots.

## Exact recorded pause
- #201 live: sealed timed sittings keep frozen type/difficulty. Wording changes still affect hashes.
- #138/#141/#142 merged; #202 live: DB Choice Notes everywhere. All 6,175 prior sidecar notes existed in DB, plus 680 additional notes.
- #203 merged `7881dab3`: sidecars/build path retired, Games-y LR renamed Rule Puzzle, PT114-S4-Q22 type repaired, parser typecheck repair included. Publication started; live polling killed due to local memory pressure. Deployment remains unconfirmed.
- New catalogs seeded/checksum verified, not activated. PT `99a8447852f183a955e0a21e1466a9480eef37069637b47f47a6c55f29d5b926`; sections `45ef6f554a1f1c402aa9f87d61326d17f16642a953757a8fb71d33b910e9aae1`.
- First verify #203 production, then safely activate catalogs after parity checks. Finish C independent review, then reconcile/finish A/B/D. No phase-two proposals were recorded applied. Proceed to Revamp after correctness work; finish remaining in-scope cleanup.

## Reusable draft state
All 13 selected pause files were copied into `corpus/lr-explanations/work/2026-10-07-resume/` (step2 and rot3 subfolders) and byte-verified with SHA-256. Read its PROVENANCE.md and SHA256SUMS.json. Use these portable copies in cloud. Original scratch was preserved unchanged.
Scratch root: `C:/Users/Joshu/AppData/Local/Temp/claude/C--Users-Joshu-dev-ai-os/ea3d04fb-872d-45e2-bfa6-a69f0373cb16/scratchpad/`.

| Artifact in step2/ | Recorded contents | Status |
|---|---|---|
| out-A.jsonl | 163 edits, 4 skips | Partial, unverified |
| out-B.jsonl | 137 edits, 7 skips, 2 flags | Partial, unverified |
| out-C.jsonl | 176 edits, 9 skips, 1 flag | Needs independent review |
| edits-C.json | 176 edits, seven added pronoun problems corrected | Use this version for C review |
| out-D.jsonl | 352 edits, 17 skips, 15 flags | Partial, unverified |

`BRIEF.md` specifies exact proposal schema; `VERIFY.md` specifies independent-review/verdict schema. No `verdicts-C.jsonl` exists. Preserve helper material (`check.py`, work-A/B/C/D, vwork-C) and `rot3/` catalog evidence as needed. Do not mistake proposal counts for unique questions or approved changes.

Assignments:
- A: model-library-defects.md sections Flaw, MBT-MBF, MC-Role-Agree, NA.
- B: Paradox-Method, Parallel, Principle, Strengthen-SA, Weaken-Evaluate.
- C: choice-note-issues.md first three sections: misquotes/different question, wrong logic, missing/garbled.
- D: verdict-only section plus side-issues.md sections 1, 4, 5, 6, 8. Sections 2, 3, 7 still need reconciliation outside that assignment.

C review priorities: PT151-S2-Q18 B; PT158-S3-Q2 A; PT133-S2-Q19 A; PT124-S3-Q3 step label; diagrams PT132-S2-Q3, PT138-S2-Q1, PT130-S1-Q13 C, PT137-S3-Q12 B, PT158-S3-Q17 B/C.

## Transfer dependencies
The accompanying prompt enumerates the approved plan, defect/revamp records, model/voice references, five DB JSON snapshots, current bank, and scratch outputs. Preserve their actual files in a cloud-readable package. A local path in a prompt does not transfer its contents. Some essential files are untracked or modified locally; GitHub clone is insufficient without reconciling these.

DB snapshot directory: `system/scripts/lsatlab-pull/data/db/`. Five tables: lr_questions, lr_answer_choices, lr_explanations, lr_explanation_steps, lr_explanation_choice_notes. Original mirror dates are 2026-10-02/03 and do not establish present production values. Parse per-question records with helper scripts. Bank controls what students see and grading; DB controls explanation text. Resolve mismatch before reasoning. Fix all affected styles, not just the preferred style.

Historical operational tools were Lovable free query_database/deploy_project for project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`; these are not automatically present in cloud. Vault repo: `vnjkoxpl-42905/ai-os`. App repo: `vnjkoxpl-42905/lsatu-684d89db`. Local `.env`, authenticated browser, native memory, and Temp do not transfer via a repository clone.

Read-only snapshot helper: `system/scripts/lsatlab-pull/db_pull.py`, with project_paths.py and local authentication configuration. Do not place credentials in package or handoff. Cloud with snapshots can author/review; final production changes require actual authorized live access or local application of reviewed outputs.

## Risks to reconcile
- Latest transcript/log supersedes stale unchecked housekeeping entries in fixes/index.md.
- Revamp inventory is an older survey; reassess against current explanation, since coverage batches repaired some missing-note defects.
- Deduplicate competing row edits across slices and distinguish historical proposals from independently passed ones.
- Preserve exact old full values, before snapshots, guarded writes, conflict reporting, and applied-row verification.
- Cloud workspace configuration was subsequently inspected in the Codex in-app browser, as recorded below. No cloud execution, transfer, DB writes, catalog activation, deployment, or new explanation authoring occurred in this context-reconstruction task.

## Cloud access inspection on 2026-10-07
- Signed into Claude Code on the web in the Codex browser, account displayed as Joshua Pro.
- Repository picker lists both vnjkoxpl-42905/ai-os and vnjkoxpl-42905/lsatu-684d89db. They can be selected; no fresh clone/file-access probe was run.
- Default cloud environment: Full network access; empty setup script; empty environment-variable field; network secrets reads No secrets yet. No settings were saved or changed.
- Account connector list: Lovable Connected; GitHub Integration Connected. LSATU App reads Reconnect. Supabase reads Connect, so a separate Supabase connector is not currently connected.
- New cloud task Add > Connectors menu: Lovable checked (Value 1), alongside Figma, Higgsifield, PDF Viewer. Lovable is enabled for new cloud tasks, beyond merely connected at account level.
- Actual Lovable tool list, project access, query_database permissions, and free deployment operations remain unprobed. No task/message was sent to Claude and no live SQL was executed.
- Recommendation: attach both repositories, transfer current local-only LR artifacts, and require a read-only Lovable project/query probe before any production change. Missing environment secrets do not mean Lovable access is missing: the enabled connector uses its own account connection.
- Further inspection: both repositories were accepted together on main in an unsent cloud task composer. GitHub ai-os main is `7e3a37c49aad80bc3d36352b796612425fe9b051`, committed `2026-10-02T03:48:33Z`. It predates the approved 2026-10-07 plan and paused work. Selecting the repositories therefore does not supply all current local context.
