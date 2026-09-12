---
type: handoff
subject: Plan Review Log Takeout deep-mine ingestion emulation build
updated: 2026-07-19
aliases: []
---

# Plan Review Log: Takeout deep-mine ingestion + emulation build
Act 1 (grill) complete — plan locked with Joshua. MAX_ROUNDS=5. Reviewer: gpt-5.6-luna, codex-cli 0.144.1, thread 019f7964-c233-7740-be52-3906a4f91ce6

## Round 1 — Codex
The plan has material problems and should be revised.

- **Wrong schema path:** It assumes `/Users/joshuaf/brain/system/schema/core.md`, but that vault does not exist; the live vault is `/Users/joshuaf/ai-os`, and only `system/schema/frontmatter.md` exists. **Fix:** Add a preflight that resolves the canonical vault and fails closed on path/schema mismatch.

- **Existing-file protection is internally contradictory:** Agents are told to write only new files, but also to update existing `transcripts.md`; those files are currently treated as primary and non-regenerable. **Fix:** Use new generated indexes such as `transcripts.generated.md`, or require explicit compare-and-swap edits to existing indexes.

- **Proposed generated queue violates the schema:** `wiki/queue.md` is supposed to be refreshed wholesale, but the schema only permits whole-file replacement for `.generated.` files or `INDEX.generated.md`. **Fix:** Use `wiki/queue.generated.md` with `brain-managed: true`, `schema-version`, `domain`, and `source`.

- **No hard fan-out barrier:** “Pipeline not barrier where possible” can let archive agents run before roster resolution, causing wrong folders, duplicate identities, or missing transcript assignments. **Fix:** Make roster output, validation, and approval of ambiguity flags a mandatory barrier before all person agents start.

- **No idempotency or locking protocol:** A retry or duplicate Workflow invocation can create duplicate transcript files, append duplicate entries, or race on directory creation. **Fix:** Assign every source a stable hash/message or Drive ID, claim it atomically, and make every write content-addressed and retry-safe.

- **The exclusive-path rule is insufficient:** Multiple agents can still process the same transcript, alias, shared mailbox, or person if the roster mapping changes or contains duplicate addresses. **Fix:** Validate one-to-one source ownership in a manifest before launching workers and reject overlapping claims.

- **Agent writes lack transactional recovery:** A worker can create half a folder, then fail, leaving the vault looking complete but semantically partial. **Fix:** Write to per-agent staging directories, validate manifests, then atomically promote the completed output.

- **The source-of-truth boundary is missing:** Outputs may summarize scratchpad files, but the plan does not persist source IDs, message IDs, date coverage, hashes, or extraction version in each archive. Re-running after scratchpad loss cannot reliably detect drift. **Fix:** Create a durable provenance manifest mapping every output claim/file to immutable source IDs and hashes.

- **“Full correspondence timeline” risks privacy leakage:** Personal, vendor, and mixed threads can be copied into student or roster pages despite the personal-patterns-only decision; a 154-address roster may itself expose personal contacts. **Fix:** Keep personal/vendor identities in a restricted non-student manifest and require explicit classification plus redaction before durable writes.

- **Email and transcript content is untrusted input:** Full bodies and meeting notes can contain prompt injection or instructions that agents may follow while they have vault-write access. **Fix:** Treat all source text as inert quoted data, prohibit source-derived tool instructions, and restrict worker tools to read-only analysis plus scoped writes.

- **Payment handling is underspecified:** “Payment info stays as links/references” does not prevent agents from persisting card fragments, invoice data, private URLs, or credentials found in message bodies. **Fix:** Add deterministic secret/financial-data redaction and quarantine failures before any student-folder write.

- **Ambiguous status handling contradicts itself:** The plan says ambiguous cases are flagged and not guessed, but says Kaden is filed under former students pending Joshua’s answer and prospects are filed based on whether they are “dead.” **Fix:** Add an `unresolved` status and quarantine folder; never place unresolved people into active or former records.

- **The active roster is not reconciled with the vault:** The plan says 10 existing folders plus Favour, while `students/README.md` lists only nine named current students and omits `yahunatan-zetvy`; this will produce false completeness results. **Fix:** Derive the active roster from a checked, versioned manifest and reconcile it against both directory names and README links before ingestion.

- **Transcript routing is too simplistic:** “Each transcript into exactly one person’s folder” fails for consultations with multiple participants, personal sessions, unidentified meetings, and transcripts containing several people. **Fix:** Define primary subject, co-participant links, unresolved handling, and a non-student consultation archive before counting reconciliation.

- **The plan conflates primary and generated records:** Full transcript exports are primary, but `email-history.md` and `mined-decisions.md` are model-generated interpretations with no `generated` or review status. **Fix:** Mark derived files as generated/draft, preserve raw transcript sources, and require promotion into primary teaching notes only after review.

- **Decision promotion lacks an approval gate:** A model may mistake repeated behavior or one email for a locked policy, then promote it into append-only `decisions/log.md`. **Fix:** Separate `observed pattern`, `inferred policy`, and `Joshua-confirmed decision`, and require explicit confirmation for the last category.

- **Trend claims lack statistical guardrails:** Conversion, retention, revenue, and response-lag analysis cannot be reliably calculated from a partial mbox and calendar alone; denominators, cancellations, payment truth, aliases, and cutoff censoring are undefined. **Fix:** Define each metric’s authoritative source, denominator, coverage window, exclusions, and uncertainty before analysis.

- **Calendar counts can be wrong:** The plan does not specify treatment of cancellations, reschedules, duplicate calendar events, time zones, no-shows, or multi-attendee events. **Fix:** Normalize event IDs and statuses, define session-count semantics, and reconcile against Cal.com/Google Calendar where claims affect operations.

- **Verification is too weak for 40 agents:** Three spot checks cannot establish identity accuracy, privacy hygiene, or transcript fidelity across 154 addresses and 52 files. **Fix:** Validate every output manifest mechanically, sample by risk class, and require zero unresolved ownership or schema errors before synthesis.

- **Observability is missing:** There is no run ID, worker status, retry/error ledger, input/output count, token/cost accounting, or quarantine report. A “counts reconcile” check cannot distinguish silent omissions from successful processing. **Fix:** Emit a durable run manifest with per-agent inputs, outputs, errors, retries, hashes, and final coverage metrics.

- **The Workflow assumption is unverified:** The plan names a Workflow tool, concurrency of 10, and a 1,000-agent cap without specifying the executable interface, permissions, timeout, token budget, or failure semantics. **Fix:** Add a small dry run that proves the actual fan-out API, scoped write permissions, cancellation behavior, and rate limits before processing real data.

- **Scope accounting is inconsistent:** The plan describes a 5MB corpus, while the takeout directory is approximately 12GB and contains ZIPs, Drive exports, DOCX files, and personal data; the cost and preprocessing assumptions are therefore not credible. **Fix:** Build a file-level inventory and process only explicit immutable source sets with measured byte/token budgets.

- **The planned lint will miss much of the new structure:** Existing `second-brain-lint` focuses on wiki source/entity/concept paths and does not validate `decisions/`, `students/former-students/`, provenance, or student-record invariants. **Fix:** Add a dedicated ingestion validator covering all proposed paths, frontmatter, links, ownership, and source coverage.

- **Shared-page writes still have a race with human edits:** “Inline by the orchestrator” does not protect `wiki/index.md`, `wiki/log.md`, or `decisions/log.md` from simultaneous Claude/Codex/Obsidian edits. **Fix:** Require file hashes and compare-and-swap updates, aborting on changed files.

- **The auto-send deliverable lacks operational safety details:** Ratification “per template” does not define exact triggers, recipient eligibility, variable validation, expiry, versioning, audit logs, or a global kill switch. **Fix:** Produce templates with explicit predicates, version IDs, test cases, approval records, and fail-closed send controls.

VERDICT: REVISE
### Claude's response (Round 1)
Accepted (incorporated): generated-file naming for all agent writes (email-history.generated.md, transcripts.generated.md, queue.generated.md) per vault automation rule; hard barrier after roster resolution with 1:1 ownership manifest validation; `unresolved` quarantine status (Kaden Forges quarantined, not filed); roster reconciliation vs students/README.md + folders; provenance frontmatter (source, coverage window, run date) on every generated file; durable run report with per-agent coverage/errors; prompt-injection hygiene (source text inert; miners read-only; writers path-scoped); financial-fragment redaction + quarantine; decision three-tier ladder with promotion to decisions/log.md only on Joshua's confirmation; trend metrics carry source/denominator/coverage/cutoff caveats; calendar counts approximate, live systems authoritative; multi-participant transcript primary-subject rule; CAS/git-status check on shared-page writes; auto-send template spec hardened (predicates, versioning, audit, kill switch); lint gap covered by added ownership/frontmatter pass.
Rejected (with reasons): staging directories + atomic promotion — overkill for a git-tracked markdown vault; git diff + deterministic filenames + run report give equivalent recovery for a one-shot run. Workflow-API dry run — Workflow is a first-class harness tool with documented concurrency/journal/resume semantics; a dry run burns tokens to prove known behavior. "Wrong schema path /Users/joshuaf/brain" — the plan never referenced that path; canonical root now stated explicitly as /Users/joshuaf/ai-os. Content-addressed atomic claim system — single orchestrated run; ownership manifest + deterministic names suffice.

## Round 2 — Codex
The revision addresses most prior findings, but several material issues remain.

Addressed successfully:

- Hard roster barrier and one-to-one ownership manifest.
- Unresolved identity quarantine.
- Prompt-injection handling and scoped writer access.
- Generated filenames and provenance metadata.
- Privacy exclusions and financial redaction.
- Decision-promotion approval.
- Metric denominators, source windows, and cutoff caveats.
- Durable run report and expanded verification.
- Generated queue naming.
- Explicit auto-send predicates, versions, audit lines, and kill switch.

Rejected findings:

- **`/Users/joshuaf/brain` path:** Rejection is sound. The live instructions and vault are `/Users/joshuaf/ai-os`, and the old path is absent.
- **Workflow dry run:** Conditionally sound. If Workflow is genuinely an established harness with documented concurrency, journaling, and resume semantics, a dry run is unnecessary. The plan should still name the invocation and permission contract, but this is not independently material.
- **Staging/atomic promotion:** The rejection is reasonable for a one-shot, local, git-tracked markdown run with deterministic outputs, but the stated recovery rationale is incomplete: new files are untracked, `git diff` does not recover them, and direct writes can leave partial files. Full staging is not required, but each file should be fully rendered and redaction-validated before creation, with atomic temp-file replacement for retries.

Remaining material problems:

- **Primary transcript conflict:** `students/README.md` explicitly treats `transcript-downloads/` as primary and says never regenerate or overwrite it, while the plan permits “retry-safe overwrites.” **Fix:** Make transcript exports append-only and reject any existing filename/content mismatch; never overwrite primary files.

- **Generated transcript index is disconnected:** Existing student profiles link `transcripts.md`, but the plan forbids touching it and creates `transcripts.generated.md`, so the new index may be undiscoverable. **Fix:** Add a permitted fenced generated section/link to the existing index, or define a clear generated index link convention.

- **Former-student structure conflicts with the validator:** `check-student-records.sh` will treat `students/former-students/` as a student folder and fail on it, while the plan creates nested former folders. **Fix:** Update the validator contract to exclude the container and validate each nested former-student folder.

- **Former folders are underspecified:** The plan says “profile + generated files,” but the existing student contract requires primary files such as `open-loops.md`, `teaching-notes.md`, `assignment-log.md`, and `transcripts.md`. **Fix:** Define the former-student minimum schema and distinguish agent-created generated records from required primary placeholders.

- **Favour has no destination:** Favour is declared active, but no existing folder or creation rule says whether she receives `students/favour/`, a prospect pipeline entry, or a cross-reference. **Fix:** Resolve Favour’s canonical slug and destination in the roster manifest before Stage 1.

- **CAS is not actually compare-and-swap:** Checking `git status` before and after does not prevent a time-of-check/time-of-use edit and does not reliably cover untracked files. **Fix:** Hash each shared file immediately before writing and abort if the hash changes.

- **Personal privacy is still too narrow:** Excluding personal contacts from the roster does not prevent personal names or sensitive third-party details appearing inside business-thread summaries, playbooks, quarantine reports, or the durable run report. **Fix:** Apply PII minimization to all generated text and keep personal-source diagnostics out of vault reports.

- **Source coverage is still incomplete:** Verification reconciles addresses and transcripts but not all 3,318 messages, 998 authored messages, attachments, aliases, CC/BCC participants, or unmatched messages. **Fix:** Add message-, thread-, attachment-, and unmatched-source counts to the ownership manifest and final report.

- **Single-agent identity resolution remains a weak point:** A single resolver can confidently make the same wrong mapping across the whole run; “ambiguous” only catches uncertainty it notices. **Fix:** Use deterministic exact matches plus an independent second-pass identity check for high-impact mappings.

- **The run report may expose quarantined personal data:** “Source to output coverage” and error details can put personal identities into `references/ingest-run...md`, contradicting the personal-contact exclusion. **Fix:** Redact or aggregate personal-source entries in the durable report and retain detailed personal diagnostics only in ephemeral scratch space.

- **The final approval count is inconsistent:** Stage 3 has skill, template, decision, and unresolved-person approvals, but the final report says “three approvals.” **Fix:** Rename this to four approval gates or explicitly combine the quarantine decision with roster review.

- **Lint coverage remains incomplete:** The plan adds custom checks for students and decisions but does not explicitly cover `wiki/playbooks/`, `wiki/operator-profile.md`, `wiki/roster.md`, `wiki/queue.generated.md`, or the new references pages. **Fix:** Make the custom validator enumerate every new path and verify links, frontmatter, generated markers, and index membership.

VERDICT: REVISE
### Claude's response (Round 2)
Verified Codex's factual claims against the vault (check-student-records.sh exists; students/README.md D4 marks transcript-downloads/ and transcripts.md primary) — accepted accordingly: transcript writes append-only with collision quarantine + atomic temp-rename; discoverability via fenced generated section in transcripts.md through real CAS (hash-check + temp + rename, replacing the weak git-status check); former-student minimum schema defined (no placeholder primaries) + check-student-records.sh updated to treat former-students/ as container; Favour resolved to students/favour/ full active folder at Stage 0; second independent identity-check agent for all vault-writing mappings; full message-count reconciliation (3,318 accounted: business/personal/vendor/unmatched); PII minimization across ALL generated text incl. run report (personal sources as aggregate counts only); "four approval gates" corrected; custom validator enumerates every new path.
Rejected: none this round — all Round-2 findings were factually grounded.

## Round 3 — Codex
Most Round-2 findings are addressed, but the plan still has material schema and execution gaps.

Addressed:

- Transcript collision handling, append-only primary transcript storage, and redaction-before-write.
- Favour’s slug and folder destination.
- Independent identity verification.
- Message-level coverage accounting, including unmatched messages and attachments.
- Real hash checks, temp-file writes, and atomic renames.
- Personal data aggregation in the durable run report.
- Four approval gates.
- Expanded custom validation across all new paths.

Remaining material problems:

- **Favour will fail the current student validator:** The plan creates `students/favour/`, but does not say it will create the active folder’s required primary files (`favour.md`, `transcripts.md`, `assignment-log.md`, `teaching-notes.md`, `open-loops.md`). **Fix:** Define Favour’s complete initial folder schema or explicitly exempt new active folders until Joshua reviews them.

- **Former-student profile handling conflicts with write rules:** The plan creates `<name>.md` marked “draft,” but the write rule permits only `.generated.md` files and transcript conversions. A draft profile is neither clearly generated nor safely replaceable on rerun. **Fix:** Create `profile-draft.generated.md`, or specify that the profile is a one-time generated file with a non-overwrite policy.

- **“Same structure as active” is contradicted by the former schema:** The key decision says former students use the same structure, but the minimum schema omits required active files and creates only generated records. **Fix:** Make the exception explicit in the key decision and validator, or implement the full active structure.

- **The transcript verification count contradicts quarantine:** It requires all 52 transcripts to be filed into exactly one person’s folder, while unresolved people such as Kaden must never be filed into active or former records. No durable quarantine location for the transcript itself is specified. **Fix:** Define a `students/quarantine/` or equivalent source-preserving location and include quarantined transcripts in the reconciliation count.

- **New shared pages do not follow the generated-file contract:** `wiki/playbooks/`, `wiki/operator-profile.md`, `wiki/roster.md`, the five `decisions/` pages, and the reference reports are automation-produced but are not `.generated.md` files or described as fenced-section updates. This will make reruns schema-invalid or overwrite primary content. **Fix:** Mark these as generated files, or define append-only/fenced generated sections and promotion rules.

- **The CAS algorithm still has a narrow race:** Rechecking the hash and then renaming is not a true compare-and-swap if a human edits between the second hash check and rename. **Fix:** Use a lock around the target or an OS-level exclusive replacement primitive; otherwise describe this as best-effort CAS.

- **The plan still overstates Git recovery:** New generated files are untracked, so `git diff` will not recover them after a partial run. The per-file atomic writes make the rejected staging approach defensible, but this justification is factually incomplete. **Fix:** Rely on the run manifest plus explicit untracked-file inventory, or state that recovery means cleanup by manifest rather than `git diff`.

- **The current `students/README.md` remains stale:** It still omits `yahunatan-zetvy` and Favour, despite the plan treating the README as a roster reconciliation source. **Fix:** Update the README as an explicit Stage 2 output or stop using it as authoritative input.

- **Attachment handling remains underspecified:** The plan counts attachments as “noted-but-not-ingested,” despite the goal of ingesting the business corpus. Important PDFs, Docs, or payment artifacts may therefore be silently excluded. **Fix:** Define attachment classification, extraction rules, and an explicit reviewed-exclusion list.

- **Source ownership is still slightly ambiguous:** The manifest accounts for every message by category, but the stated 1:1 ownership validation is not explicitly applied to each message, thread, and attachment. **Fix:** Require every source object to have exactly one owner or an explicit non-person bucket, with no aggregate-only validation.

The prior rejections remain reasonable: the old brain path is definitively not the live vault, Workflow dry-run is unnecessary if its stated journal/resume semantics are established, and full directory staging is avoidable given per-file atomic writes. The plan should, however, correct the weaker Git-recovery claim.

VERDICT: REVISE
### Claude's response (Round 3)
Accepted: Favour gets the complete active schema (seeded primaries marked draft) so the validator passes; former profile becomes profile.generated.md (one-time, non-overwrite) and key decision 7 now states the explicit lighter former schema + validator update; quarantined transcripts reconcile as filed+quarantined=52 with sources untouched in data about me /transcripts/ (no new quarantine folder needed — source preservation IS the quarantine); CAS renamed best-effort and wrapped in system/scripts/with-lock.sh; recovery claim corrected to run-manifest + untracked-file inventory (not git diff); students/README.md refreshed as a Stage 2 output and reconciled-not-trusted as input; attachments inventoried per-object with a reviewed exclusion list (contents deferred to a follow-up pass); ownership validation stated per source object, not aggregate.
Rejected with reason: making wiki/playbooks, operator-profile, roster, and decisions pages `.generated.md` — these are LLM-wiki PRIMARY pages under the vault's own design ("the LLM writes/maintains wiki/"), authored in a supervised session and maintained by future ingests via read-merge-CAS; the generated-file contract applies to unattended refresh surfaces (queue.generated.md, fenced sections), not session-authored knowledge pages. Marking them generated would wrongly license wholesale regeneration and contradict the vault's wiki-ops pattern.

## Round 4 — Codex
The wiki-primary rationale is sound. The vault explicitly says the LLM writes and maintains `wiki/` during supervised ingest sessions, while the generated-file contract governs unattended refreshes. Since Stage 2 is explicitly supervised and single-threaded, treating playbooks, operator profile, roster, and decision pages as primary wiki knowledge is correct.

Round-3 findings are otherwise addressed. I found one new material problem:

- **The planned lock wrapper currently has a missing dependency:** `system/scripts/with-lock.sh` invokes `system/scripts/watchdog.sh`, but `watchdog.sh` does not exist in `system/scripts/`; Stage 2 would fail before writing anything. **Fix:** Restore or define `watchdog.sh`, or change the plan to invoke a verified locking path and run its self-test before ingestion.

The revised handling of `references/automation-backlog.md` is acceptable only if the addendum is written as a supervised human-reviewed edit; it is not covered by the wiki-primary rationale for unattended automation.

VERDICT: REVISE
### Claude's response (Round 4)
Codex accepted the wiki-primary rationale. Its single new finding verified TRUE and accepted: with-lock.sh is broken (missing watchdog.sh dependency, plus FreeBSD-only /usr/bin/lockf on macOS). Plan no longer uses it — best-effort CAS by the single supervised orchestrator instead; with-lock.sh brokenness recorded as a waste-audit finding. Backlog addendum explicitly a supervised human-reviewed edit.

## Round 5 — Codex
The two changes are sound:

- Rejecting `with-lock.sh` is correct. The script is unusable here because `watchdog.sh` is missing and `/usr/bin/lockf` is platform-incompatible. The plan’s supervised, single-threaded orchestrator with best-effort CAS is an adequate scoped alternative.
- Marking the `references/automation-backlog.md` change as supervised and human-reviewed resolves the prior non-wiki write concern.

The wiki-primary rationale also remains consistent with the actual vault rules: supervised LLM sessions maintain `wiki/` pages as primary knowledge, while unattended refreshes use generated files or fenced sections.

I found no new material problems in this final revision.

VERDICT: APPROVED
### Resolution: APPROVED after 5 rounds. Claude arbiter; log complete.
