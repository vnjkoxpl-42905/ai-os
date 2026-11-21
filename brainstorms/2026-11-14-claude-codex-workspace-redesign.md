# Make Claude and Codex one organized workspace

Date: 2026-11-14. Status: implementation in progress; see the dated evidence and open items below.

## Recommendation

Keep three permanent project homes: AI OS for operations and knowledge, LSAT U for application code, and Job Search. Give each active piece of work one shared task record, a meaningful title, and links to both native conversations. Keep native conversations in their own applications. Share the files, decisions, next step, and verification evidence that let either agent continue accurately.

Do not install another workspace manager yet. Reuse existing scripts and prove one end-to-end handoff before extending automation.

## What the audit established

- Codex lists nine registered projects: ai-os, ai-job-search, dev/lsatu, four dated LSAT U working folders, and two Claude scratch folders. The sidebar also contains an additional project reference absent from the project listing. Reconcile it before removing anything.
- The sibling ai-os-projects directory contains 99 folders, 62 with lsatu in their names. These are inventory counts, not proof that they are redundant. Git worktree inspection of the documented LSAT U root was permission-denied.
- Instructions identify `../ai-os-projects/lsatu/` as the application home; the current app project uses `C:/Users/Joshu/dev/lsatu`. This is an unresolved path conflict. Compare remotes, branches, dirty files, untracked files, worktree metadata, and commits before selecting the canonical checkout.
- Several chat titles are entire pasted handoffs. The supplied screenshot also shows unrelated student filing inside a teacher-home-design chat. Thread scope and naming are part of the problem.
- `C:/Users/Joshu/.codex/hooks.json` calls the absent `C:/Users/Joshu/.orca/agent-hooks/codex-hook.cmd` on nine events. This is a verified defect. The user identified the visible indicator as Codex Review hooks; its specific pending entries were not inspected.
- Herdr SessionStart scripts exist for both runtimes, but exit unless HERDR_ENV and HERDR_PANE_ID identify a Herdr session. They report sessions, not general cross-app synchronization.
- AI OS Codex teaching hooks reference an existing Karpathy script and interpreter. Their special Stop behavior is scoped. Preserve them pending targeted testing.
- `setup/github-sync/README.md` describes two-minute snapshots; `references/ai-workspace/action-queue.md` records disabled sync/backup tasks. Receipts found by the audit date to 2026-11-11. A live scheduled-task query failed because CIM access was unavailable. Current sync health is unknown.
- `wiki/hot.md` still begins with 2026-10-30 state. A global last-session page alone does not provide reliable current state for several concurrent projects.
- Existing tools include check-skills.sh, sync-claudex-skills.py, GitHub snapshot/export scripts, cross-provider runners, and several overlapping handoff skills. Reuse before adding.

## The experience to build

Open one small Start Here page showing three project cards. Each shows current work, last verified activity, next action, agent ownership, and links to artifacts and native chats. Show Waiting on you separately from Ready to continue. Completed work stays searchable but leaves the active view.

For each task, display a short outcome title such as “LSAT U: teacher home redesign.” Do not use pasted prompts as titles. A major topic change starts a separate task. Keep only a few active tasks pinned; group temporary work beneath its parent project rather than presenting each checkout as a permanent project.

The page is a view over existing records, not another task database. Extend the existing AI workspace references and owning project records. Reuse Obsidian/Markdown first; build a local visual dashboard only if that simple view fails the usability trial.

## What stays synchronized

| Layer | Authority and method |
|---|---|
| Code | Git repository and selected working tree; check dirty files before switching |
| Shared policy | Hand-owned AGENTS.md and CLAUDE.md; parity checks on shared sections |
| Runtime settings | Separate Claude and Codex adapters; never copy entire settings files |
| Skills | Existing catalogs and activation copies, with deliberate differences in PARITY.md |
| Current work | One task record in its owning project; central page links to it |
| Conversations | Native histories, linked by IDs; exports are recovery/search evidence |
| Backup | Verified recoverable snapshots, separate from live work and native chat sync |

Each task record needs: stable ID, goal, status, canonical repo, actual checkout, branch and HEAD, active writer, source chat IDs, artifacts, accepted decisions, last verified checks, unresolved issues, next action, timestamp, and resume instructions. Never infer completion from a chat being idle or a process exiting.

Switching agents: outgoing agent saves a bounded checkpoint and yields ownership; incoming agent reads it, verifies disk/branch state, and states the next action. A missing checkpoint or changed HEAD produces a visible discrepancy. Two agents may review concurrently, but only one writes a given checkout. Parallel implementation uses explicitly assigned separate worktrees.

## Ordered implementation checklist

### 1. Preserve and identify the current state

- [ ] Capture sanitized project, checkout, hook, runtime-version, and scheduled-task inventories. Back up exact settings with hashes outside tracked content.
- [ ] Reconcile both LSAT U roots and every active dated checkout. Record dirty/untracked work and branch reachability. Classify keep, active worktree, recover, or archive candidate.
- [ ] Resolve the sidebar reference missing from list_projects.

Acceptance: every active task resolves to an existing checkout; no unknown work is labelled disposable. Verification: compare filesystem, Git, app project inventory, and saved manifest. Dependencies: none. Scope: inventory script and report, plus existing registry.

### 2. Repair hooks with the smallest change

- [ ] Disable only orphan Orca registrations after preserving their original configuration. Do not reinstall Orca just to satisfy abandoned references.
- [ ] Inventory remaining hooks by purpose, owner, event, command, interpreter, state writes, and test.
- [ ] Review the exact remaining hooks through Codex's supported review UI. Retain Herdr conditionally; test specialized Karpathy behavior separately.

Acceptance: no missing targets; ordinary prompt/tool/stop flow succeeds; approved unchanged hooks do not repeatedly ask for review. Verification: fresh Codex session, Claude session, and scoped teaching session. Dependencies: 1. Scope: global hook config, inventory, targeted check script. Rollback: restore the backed-up config. Never modify internal trust databases to suppress review.

### 3. Establish stable project navigation

- [ ] Set canonical mappings for the three projects using phase 1 evidence.
- [ ] Organize Codex using supported sidebar tools. Label active chats by outcome. In Claude, use supported project/session controls; do not edit private session databases.
- [ ] Preserve temporary folders until their work is accounted for. Archive only after explicit authorization where required; delete nothing as part of this plan.

Acceptance: find the correct project and latest task within 30 seconds. Verification: reopen both apps and navigate to each project. Dependencies: 1. Scope: registry and app organization. Checkpoint: project names and paths agree before further automation.

### 4. Pilot one shared checkpoint

- [ ] Select one unfinished task and add its task record beside its existing plan.
- [ ] Extend the existing handoff routes to reference that record. Preserve explicitly requested chat-only handoffs; add a distinct persistent checkpoint operation rather than silently changing their contract.
- [ ] Link the task from Start Here and test Claude to Codex to Claude.

Acceptance: each receiving agent names the correct goal, checkout, latest decisions, verification limits, and next action without Joshua repasting the full history. Verification: two round trips including one restart and one deliberately stale checkpoint. Dependencies: 3. Scope: task record, existing workflow reference, paired runtime skill copies/catalog entries as needed. Split skill changes into their own small patch.

### 5. Add a small read-only doctor

- [ ] Extend existing validation with missing hook targets, invalid settings, shared-policy drift, undeclared skill drift, absent project paths, stale checkpoints, and last successful sync receipt.
- [ ] Report healthy, warning, failed, or unknown with evidence and a repair action. A configuration file saying enabled does not count as a successful run.
- [ ] Use generated output and compare-and-swap. Keep transcripts, environment values, credentials, and raw tool output out of reports.

Acceptance: planted missing-path and stale-receipt fixtures are detected; valid deliberate runtime differences pass. Verification: focused tests and read-only run on this laptop. Dependencies: 2 and 4. Scope: validator, tests, generated health report.

### 6. Prove backup and synchronization separately

- [ ] Obtain live scheduler status through a permitted host route; inspect job commands and last results before enabling anything.
- [ ] Test a harmless file snapshot and restore into a separate temporary directory. Hash-compare restored content.
- [ ] Keep cloud snapshots, local backups, and cross-agent task continuity clearly labelled. Do not mirror-delete from an incompletely restored machine.

Acceptance: verified current receipt and successful restore; failure is visible. Verification: one controlled round trip without touching originals. Dependencies: 1 and 5. Scope: existing sync runner/config and receipt checks. Do not blindly run existing sync/backup jobs merely to test them.

### 7. Roll out only after the pilot works

- [ ] Apply checkpoints to remaining active tasks and link existing explanations, plans, previews, and PRs.
- [ ] Run a seven-day usability trial. Target: find work in 30 seconds; resume in either agent within two minutes; zero missing-hook errors; no ambiguous writer ownership.
- [ ] Review archive candidates only after recovery evidence is complete. Keep a reversible mapping of old sidebar names and paths.

Acceptance: successful daily resume without hunting through scratch folders or repasting long histories. Dependencies: 4 through 6. Scope: existing task records and navigation views in small batches.

## Downloads and installation policy

No additional download is justified by this audit. Existing Git, PowerShell, Python, native apps, and scripts can support the first version. If a verified missing runtime blocks a specific step, install that dependency from its official source, record its version, and verify it. Do not add another plugin bundle, hook suite, scheduler, or workspace manager before proving the core workflow.

## Evidence and limits

Local sources: references/claude-plus-codex.md; references/ai-workspace/action-queue.md; setup/github-sync/README.md; wiki/hot.md; user and project hook files. Live evidence: Codex list_projects and recent thread metadata on 2026-11-14. Recent history is a sample, not an exhaustive conversation audit. No repositories were consolidated or configurations changed. No package was downloaded. Scheduler health and protected Git paths remain unverified.

Official references checked: [Codex hooks](https://learn.chatgpt.com/docs/hooks), [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees), [Claude hooks](https://code.claude.com/docs/en/hooks), [Claude workflows](https://code.claude.com/docs/en/common-workflows). Codex documents review for changed hooks; both products document worktree workflows. These capabilities do not establish native conversation synchronization between vendors.


## Implementation progress, 2026-11-14

- **In progress:** Full plan read; current Codex project and sidebar inventories taken. Nine listed projects and one additional sidebar project reference remain to be reconciled. No native histories were changed.
- **In progress:** Separate read-only checkout and backup investigations; targeted hook repair is preserving its original configuration before any change.
- **Unverified:** End-to-end handoff, fresh-session hook approvals, health report, scheduler, restore and seven-day trial.

- **Completed:** Preserved seven existing global/project runtime settings exactly under ignored `setup/github-sync/state/workspace-redesign-20261114/`; `settings-manifest.json` records source paths, sizes and SHA-256 hashes. Configuration contents were not copied into tracked notes.
- **Finding:** The `C:/Users/Joshu/dev/lsatu` checkout contains uncommitted and untracked work. It is retained. Path reconciliation is still running.

- **Completed, phase 2 repair:** Removed only nine registrations pointing to the absent global Orca executable; global Herdr registration remains. Original global hook SHA-256 `78d8875e46d3a77ad7522f8b1c104cb50cacaba08577cd017cd8784ee718e657`; repaired SHA-256 `b94479987a385329db7e14bacd3c08d1a21fbb34ea5b131916d5dbef2379c2c9`. Original is in the ignored settings backup and a separate visualization backup. No trust database was changed. Remaining-hook inventory and live approval tests pending.
- **Completed, phase 6 inspection:** Live Task Scheduler enumeration found neither documented GitHub sync nor replacement laptop-backup task registered. Latest combined runner receipt is a deferred attempt at 2026-10-30 10:33:36 UTC, not a success. Controlled restore test pending.

- **Completed, phase 1/3 (partial):** The two LSAT U roots are separate clones of the same remote. `C:/Users/Joshu/dev/lsatu` was on main at `258d41b5` and is the navigation home; `C:/Users/Joshu/dev/ai-os-projects/lsatu` was on `codex/rc-quality` at `7958d032` and remains a worktree/recovery hub. Both have unfinished changes. The paired root instruction files and `references/ai-workspace/project-registry.md` now reflect this. Nested automation worktrees and a sidebar project ID absent from list_projects remain unverified. The documented sync does not claim to cover `dev/lsatu`.
- **Completed, navigation (partial):** Created `references/ai-workspace/Start-Here.md` and grouped four dated LSAT U folders and two Claude scratch folders into a reversible Codex sidebar section. Original sidebar mapping is in the ignored settings backup. No histories or checkouts removed. Claude navigation and 30-second reopening test remain unverified.
- **Completed, checkpoint setup:** Created the shared task record beside this plan and `references/ai-workspace/switching-agents.md`; retained the chat-only session-handoff contract. **Failed pilot:** the real read-only Claude CLI invocation exited with an error; a separate minimal diagnostic returned `Failed to authenticate: OAuth session expired and could not be refreshed`. No Claude intake or round trip is claimed. A Claude desktop window inspection also failed because the window was not usable. Resume after Claude Code is signed in, then perform the two round trips, restart and stale-checkpoint test.
- **Completed, isolated restore:** Real `setup/backup/new-machine-backup.py` and `new-machine-restore.py` ran against a synthetic home and separate restore directory. Source, manifest and restored file SHA-256 `1d293d6be451938f6a2ba1b1d0ff762a057779f4b39e4521193f731d081753ca`. Artifacts: `C:/Users/Joshu/.codex/visualizations/2026/11/15/01a1dcca-a2aa-7a70-b2e2-968b34f0ae6e/backup-restore-proof-sumnqke1/`. Production source coverage, cloud restore and current scheduled backup are not established.
- **Completed, doctor initial test:** Nine focused tests passed; the live report identified existing skill drift, old GitHub receipt and deferred combined run. Follow-up fixes to timestamp handling and path labels are in progress.
- **Not started:** Seven-day usability trial and remaining-task rollout depend on a successful pilot, current sync evidence and safe ownership review. Archive candidates have not been removed.

- **Completed, sidebar reference reconciliation:** Native Codex chat metadata associates unlisted project ID `3b28914b-43f5-40a0-a8d0-c017d018ffa5` with `C:/Users/Joshu/dev/ai-os-projects/lsatu-design-11-claude`. The directory exists, but Git reports an invalid gitfile. Classified as unknown/recover and preserved.
- **Inventory evidence:** `tmp/workspace-checkout-inventory-2026-11-14.json` covers 62 immediate LSAT U paths: 57 dirty, three unknown, and two without normal status. Nested automation worktrees were excluded. No clean/disposable conclusion follows from the remaining entries. `tmp/workspace-lsatu-worktrees-2026-11-14.txt` records worktree metadata.

- **Blocked, scheduler restoration:** Inspection of the existing sync installer found enabled logon and two-minute triggers; its runner can replace Drive `latest.zip` and initialize private repositories. The replacement-backup installer schedules a runner whose offload code unlinks local payloads and SQLite snapshots, and its configured `C:/Users/Joshu/Tools/recovery-toolchain-20261006/gws/gws.exe` path is missing. These are not safe to run under this request’s no-deletion rule or against incompletely reconciled sources. Neither installer nor production job was run. A non-deleting, scoped configuration and independently verified destination/coverage are needed before enabling schedules.
- **Verified, doctor:** 13 focused tests passed, including missing-hook target, stale receipt, deliberate runtime-only skill and report compare-and-swap fixtures. Live report generated at `system/generated/workspace-health.md`; its nonzero exit reflects existing skill-validator failures. The report checks explicit global and AI OS hooks only and does not certify approvals or other projects.

- **Verification limitation:** Full AI OS `git status --short` failed with `skill-audit/.git` not recognized as a Git repository; no clean-state claim is made. `git diff --check` on touched tracked paths found pre-existing extra blank lines at the end of `wiki/hot.md`, preserved byte-for-byte; the other checked tracked paths passed.
- **Safety incident:** Initial Codex thread metadata output included a Firecrawl credential from an old summary. Its value was not copied into these records. Treat that credential as exposed and rotate it.

- **Failed, cloud metadata check:** Installed `gws` reports version 0.22.5. A read-only Drive metadata request encountered Windows keyring access denial; the CLI then attempted to remove `credentials.enc` and `token_cache.json` as undecryptable. Sandbox permissions denied both removals and the check was stopped. Authenticated Drive access and cloud generations remain unverified. Do not retry this authentication path unsandboxed without first preventing that deletion behavior.
- **Checkpoint verifier:** `system/scripts/check-workspace-checkpoint.py` checks the pilot record’s checkout, branch, full HEAD and explicitly yielded ownership. Six tests passed, including a retained real Git fixture with deliberately stale HEAD. This does not prove clean status, real writer inactivity or a live Claude handoff.

- **Final focused verification:** 20 doctor and checkpoint tests passed. The stale-HEAD test used a real retained Git fixture. An independent review found and the doctor corrected an unresolved relative-hook target false-healthy case. Report writing uses a cooperative lock and comparison immediately before replacement; a noncooperating writer could still race, so unconditional atomic compare-and-swap is not proven.
- **Credential-cache preservation:** After the denied `gws` removal attempts, both credential-cache files were independently confirmed present. No authenticated Drive generation or current cloud coverage was obtained. `gws.cmd` version 0.22.5 resolves under `C:/Users/Joshu/tools/npm/`, while the stored backup configuration references a missing older path.
- **Still open:** Sign in to Claude Code, complete real Claude-to-Codex-to-Claude transfers including a restart and stale-checkpoint test, review hooks through the supported UI, reconcile incomplete source coverage and use a non-deleting backup route, verify a current sync receipt and restore, then roll out active tasks and run the seven-day trial. Do not label this implementation complete on the basis of the synthetic tests.
