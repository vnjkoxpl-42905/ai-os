---
type: reference
subject: Open actions from ingested AI sources, worked by second-brain-task
created: 2026-10-14
updated: 2026-10-26
aliases: [AI action queue, AI queue, second brain task list]
tags: [ai-workspace, second-brain-task]
---

# AI action queue: what your AI sources say to build, try or change

Every skill, repository, automation, setting, workflow change, product update or prompt worth acting on from an ingested AI source lands here as one item with clear steps and a link to its source summary. `second-brain-ingest` adds items; `second-brain-task` shows them, takes Joshua's approval, builds them and clears them. A finished or declined item is removed from this page and recorded on its source summary under `## Queue record`. The item format and rules live in the `second-brain-task` skill. LSAT U ideas have their own [LSAT U idea queue](../../wiki/lsatu-idea-queue.md).

Next ID: AQ-049

## Approved

### AQ-045 · Define a post-session recap agent with a written role, limited tools and a fresh reviewer
- Type: skill
- From: [Austin Marchese and Nate Herk on managing agents](../../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md) at 0:42 to 2:15, 8:50 to 12:21 and 13:26; Joshua asked for this in chat on 2026-10-31
- Value: recaps come out as three checked drafts with a review report, and the agent cannot post or assign, so Joshua only judges the teaching.
- Already here: the `post-session-recap` skill holds the whole process and [recap calibration](../../.claude/skills/post-session-recap/references/recap-calibration.md) holds Joshua's corrections. `recap-status.py` reports who is due, and the ingest-clips Recap drawer (0.4.0) runs `rPrompt` for a note, homework or both. No recap agent definition exists (`.claude/agents/` holds only `karpathy`). Posting uses `lsat-u-platform-actions` after explicit approval.
- Steps:
  1. Joshua answers the open questions in [the role draft](../../brainstorms/2026-10-31-post-session-recap-agent-role.md) (where it runs, scope, autonomy, success measure).
  2. Finalize the role as a job description: goal, what good and bad look like, inputs, outputs, the tools it may use (read students and transcripts, write only `students/<slug>/recaps/` and the brainstorm build folder), and what it never touches (Gmail send, platform publish or assign, Supabase writes).
  3. Create the agent for both runtimes following `agents/README.md`, with the tool list as the enforcement, not the prompt. The skill stays the procedure; the agent calls it.
  4. Add a separate reviewer pass in a fresh session that checks the finished notes against the transcript, the emphasis map and the calibration table, and reports "checked N of N".
  5. Turn 5 to 10 of Joshua's past approve or reject calls on recaps into a pass or fail sample the reviewer is graded against.
  6. Wire the Recap drawer's Run button to the agent only after the check below passes.
  7. Check: one dry run on a real past session (a recap Joshua already approved) produces the three notes and a review report, posts nothing, and the tool list shows no send, publish or assign capability.
- Effort: medium · Status: approved (2026-10-31)
- Progress 2026-10-31: [Role draft](../../brainstorms/2026-10-31-post-session-recap-agent-role.md) written. Joshua asked to perfect the skill, make an agent for it and run it from the mod, which I took as accepting the draft's defaults. Built: `recap-agent` (writer) and `recap-reviewer` (read-only) in `.claude/agents/` with catalog and Codex copies; `system/scripts/recap_agent_guard.py` as a Bash guard; skill section "Run as the recap agent" in all six copies; Recap drawer 0.5.0 prompt calls both agents (uncommitted). Tested headless: gws gmail and lsatu-admin unassign refused, an allowed command ran, the reviewer has only Read, Glob, Grep. Not done: steps 5 (pass or fail sample) and 7 (dry run on a real past session) and the Desktop restart check of 0.5.0.

### AQ-014 · Write a file rulebook for Downloads and run it as a proposal Joshua approves
- Type: workflow change
- From: [Jeff Su, Stop Organizing Files Yourself](../../wiki/sources/stop-organizing-files-yourself-jeff-su.md) at 1:35 to 5:54 and 12:34
- Value: downloaded files get a findable name and a home without Joshua sorting them, and nothing moves until he says so.
- Already here: no file rulebook exists (`references/` has none). `~/Downloads` held 182 entries on 2026-10-14. `second-brain-ingest` searches Downloads for sources only. Google access is `gws` CLI only, and Gmail/Drive deletes are denied by rule.
- Steps:
  1. Read-only snapshot of `~/Downloads`: counts by type and age, and a proposed future tree. Move nothing.
  2. Draft `references/file-rulebook.md` with three parts: areas (for example business, students, finances, personal), naming patterns (documents, dated records, project folders), and when to ask. Student evidence keeps routing to `students/<name>/` per `students/README.md`.
  3. Show Joshua the snapshot and the rulebook. Record his answers to the clarifying questions in the rulebook.
  4. On his yes, run one proposal: a table of original name, new name and destination. Move only the rows he approves; never delete.
  5. Only if he asks, add a recurring trigger that produces the same proposal.
  6. Check: the approved files sit at their new paths with their SHA-256 unchanged, and the rulebook records every preference he gave.
- Effort: medium · Status: approved (2026-10-14)
- Progress: Run 2026-10-14: steps 1 and 2 done, `references/file-rulebook.md` with 10 questions. Nothing moved. Waiting on Joshua's answers.
- Progress 2026-10-26: Rulebook now has proposal-only defaults and refreshed metadata (194 files,5305489837bytes). Remaining: actual original/new-name/destination filing batch and row approval. Nothing moved or deleted.

### AQ-013 · Cut no-op lines from the five most-used vault skills
- Type: skill
- From: [Matt Pocock's skill process](../../wiki/sources/matt-pocock-system-claude-skills-austin-marchese.md) at 12:15 to 13:43
- Value: shorter skills cost fewer tokens on every run and leave the lines that actually change behavior easier to see.
- Already here: the user-invoked-only half of his advice is done (69 vendor skills `user-invocable-only` and 183 `name-only` in `.claude/settings.json`, 2026-10-12). No no-op audit of active skills is recorded. `second-brain-ingest` is 11,555 bytes and `post-session-recap` 17,509 bytes in `.claude/skills/` on 2026-10-14.
- Steps:
  1. Pick five heavily used skills, for example `second-brain-ingest`, `post-session-recap`, `transcript-intake`, `assign-lsatu-work` and `lsat-u-voice`.
  2. For each, have a sub-agent list sentences that would not change Claude's behavior ("be thorough", restated defaults, duplicated rules). Guardrails about sending, deleting, credentials, Lovable credits and student work are never candidates.
  3. Show Joshua the proposed deletions per skill, whole sentences only.
  4. Apply the approved cuts to every copy (`skills/claude/`, `skills/codex/`, `.claude/skills/`, `.agents/skills/`), sync loaded home copies with `python audits/skills-2026-10-12-karpathy/sync_loaded_copies.py <name>`.
  5. Check: `sh system/scripts/check-skills.sh` passes, byte counts before and after are recorded in `wiki/log.md`, and the next real run of each skill completes without being sent back.
- Effort: medium · Status: approved (2026-10-14)
- Progress: Run 2026-10-14: `research/skill-noop-cuts-2026-10-14.md`, about 4.4 KB of candidate cuts. Waiting on Joshua's approvals and the assign-lsatu-work authorization ruling.
- Progress 2026-10-26: One clearly redundant 50-byte sentence removed; guardrails retained. Remaining: complete five-skill audit and real-run behavior checks.

### AQ-012 · Find what Joshua keeps sending back and turn each into a one-line skill fix
- Type: workflow change
- From: [Matt Pocock's skill process](../../wiki/sources/matt-pocock-system-claude-skills-austin-marchese.md) at 0:42 to 2:37 and 11:45; [managing agents](../../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md) at 13:26
- Value: skills get fixed where they actually fail Joshua, instead of where they seem weak.
- Already here: `level-up` reads 30 days of sessions for requests repeated three or more times, not for corrections. `skill-doctor` grades sessions against rubrics. `wiki/COPY-CORRECTIONS.md` logs student-copy corrections by hand. Nothing scans for send-backs across skills.
- Steps:
  1. Have a sub-agent read only Joshua's turns from the last 30 days of Claude Code (`~/.claude/projects/C--Users-Joshu-dev-ai-os/`) and Codex (`~/.codex/sessions/`) and list corrections: redo requests, "no", "I said", reverted output.
  2. Group them by the skill that was running (or "no skill"), with counts and one example each.
  3. For each group seen twice or more, draft a one-sentence fix to that skill, or a new skill only when no existing one can compose the behavior.
  4. Show Joshua the list; apply only the fixes he approves, in both runtimes, and log copy-related ones in `wiki/COPY-CORRECTIONS.md`.
  5. Check: a report saved to `research/send-backs-YYYY-MM-DD.md` lists every correction with its session, and `sh system/scripts/check-skills.sh` passes after the edits.
- Effort: medium · Status: approved (2026-10-14)
- Progress: Run 2026-10-14: `research/send-backs-2026-10-14.md`, 36 send-backs grouped with proposed one-line fixes. Waiting on Joshua's approvals.
- Progress 2026-10-26: Three source-grounded teaching/interview corrections implemented and installed copies synced. Remaining: refreshed 30-day correction scan and remaining groups; no blanket adoption of every old suggestion.

### AQ-009 · Reconcile the consultation follow-up send rule and add a link check before drafting
- Type: workflow change
- From: [July follow-up workflow memory](../../wiki/sources/consultation-followup-workflow-memory-2026-07-07.md), sections "Sending Rule" and "Required Links"
- Value: one answer to "does the consultation follow-up send itself?" instead of three, and no draft ever carries a wrong price or a dead payment link.
- Already here: `decisions/log.md` (2026-07-20) still locks a scheduled 3:00 PM Toronto auto-send with a fail-closed price-to-link check. `wiki/CONSULTATION-FOLLOW-UP-TEMPLATE.md` (2026-09-11) and `skills/claude/consultation-followup-drafts/SKILL.md` say draft only, Joshua sends, and no later decision entry supersedes the 2026-07-20 one. The skill has no explicit step that checks each price against its Stripe or Cal.com link before drafting.
- Steps:
  1. Ask Joshua which rule stands for consultation follow-ups: draft only, or scheduled auto-send.
  2. Append a dated superseding entry to `decisions/log.md` recording his answer (leave the 2026-07-20 entry in place).
  3. Add one step to `consultation-followup-drafts` in `skills/claude/` and `skills/codex/` (and sync the loaded copies): before drafting, confirm each price in the draft matches its link in the template, and stop on a placeholder or malformed link.
  4. Check: `decisions/log.md`, the template's Rules section and both skill copies state the same send rule, and a dry run of the skill reports the link check passing.
- Effort: small · Status: approved (2026-10-14)
- Progress: Run 2026-10-14: step 3 built (`scripts/check_links.py`, dry run PASS). Steps 1 and 2 wait on Joshua's send-rule answer. $60 link id length is unusual; confirm in Stripe.
- Progress 2026-10-26: Draft-only rule reconciled and local standard/higher checker positive/negative tests pass; Cal.com GET returned HTTP200. Remaining: verify the unusual $60 Stripe link identity and amount with Stripe authority. No sends/payments.

### AQ-001 · Run a pre-release security pass on LSAT U and pick one audit tool
- Type: skill
- From: [Ten repos clip](../../wiki/sources/10-new-github-repos-make-money.md), section "Which ones are of value"; [Nate Herk's 100+ repos](../../wiki/sources/100-github-repos-for-claude-nate-herk.md), section "What is of value here", item 3
- Value: LSAT U holds student accounts and payments, and no security pass has ever been run on it; this finds real holes before students do and settles which of two tools to keep.
- Already here: Anthropic's Claude Security plugin is installed (`claude-security@claude-plugins-official` 0.12.0 in `~/.claude/plugins/installed_plugins.json`, installed 2026-10-12) but there is no record of a scan on LSAT U. The Cloudflare security-audit skill is not in `.claude/skills/`, `skills/claude/` or `skills/codex/`. The built-in `security-review` skill covers only part of the job.
- Steps:
  1. Run Claude Security in scan mode against `../ai-os-projects/lsatu` (the `claude-security` skill). Scan only; do not generate patches.
  2. Fetch `cloudflare/security-audit-skill` with `gh` into a new, empty scratch folder. Read its `SKILL.md` and every script before running anything. If AQ-002 is done, run `skillspector scan --no-llm` on it first.
  3. Run the Cloudflare skill against the same LSAT U tree by following its `SKILL.md` from the scratch copy, without activating it.
  4. Save both reports and a short comparison (findings in common, real findings only one tool caught, false positives, time taken) to `audits/security-YYYY-MM-DD/`.
  5. Show Joshua the comparison and his recommendation. On his choice, log it in `decisions/log.md`. If the Cloudflare skill wins, catalog it in `skills/claude/` and `skills/codex/`, activate it in `.claude/skills/` and `.agents/skills/`, and regenerate `skills/INDEX.md` with `system/scripts/gen-skill-index.py`.
  6. Each real finding becomes separate LSAT U work on a session branch off `main`. No push, merge or Lovable Edge Function deploy without Joshua's confirmation for that action.
  7. Check: `audits/security-YYYY-MM-DD/` holds both reports and the comparison, and `decisions/log.md` names the tool kept.
- Effort: medium · Status: approved (2026-10-14)
- Progress: Run 2026-10-14: 7 findings from source reading, none confirmed live; reports in `audits/security-2026-10-14/`. Claude Security did not run (must be the main agent). Waiting on Joshua: read-only SQL checks, tool choice (recommended: Cloudflare skill, quick profile).
- Progress 2026-10-26: Actual LSAT U security scan, tool comparison and finding adjudication remain unperformed; tool presence is not a scan.

## New

### AQ-048 · Decide whether claudex-loop should offer to extend at the round limit
- Type: workflow change
- From: [Chase AI on ClaudeX Loop](../../wiki/sources/claudex-loop-chase-ai.md) at 7:32 to 8:13
- Value: a plan that is one or two rounds from agreement is finished instead of abandoned or taken over by hand.
- Already here: the local [`claudex-loop`](../../.claude/skills/claudex-loop/SKILL.md) has five plan rounds, two build-fix rounds, an assumptions ledger and fresh inspection. At the limit it stops and reports unresolved findings; it does not offer an extension.
- Steps:
  1. Read the skill's round-limit paragraph and the runner's `--resume` rules.
  2. Show Joshua the difference: stop only, versus stop, accept the deadlock, or extend by two rounds with his approval.
  3. If he wants it, change the local skill and `skills/PARITY.md` together, keeping "exhausting rounds is not approval".
  4. Check: a mock plan that does not converge reports the three choices and records which one Joshua picked.
- Effort: small · Status: new (2026-11-14)

### AQ-047 · Add an owner and a last-reviewed date to every recurring automation
- Type: workflow change
- From: [Austin Marchese and Nate Herk on managing agents](../../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md) at 13:51 to 15:00
- Value: a skill or schedule that quietly stops working gets noticed on a date, not by a student.
- Already here: the [operating inventory](operating-inventory.md) names each layer's owning folder or skill but no review date. Windows scheduled tasks were changed on 2026-10-30 (laptop backup and GitHub sync disabled). The send ledger and wiki log are the traces.
- Steps:
  1. List every recurring automation: scheduled tasks, auto-send skills (accommodations email, pre-consult check-in), draft sweeps and the Matt Pocock skills sync.
  2. Add owner, trigger, what it can touch, and last-reviewed date as columns in the inventory.
  3. Show Joshua the filled table and mark dates only from an actual check.
  4. Check: every row has a date from a real run or read, and one stale row is flagged as an example.
- Effort: small · Status: new (2026-10-31)

### AQ-046 · Move the send and delete rules from wording into tool permissions
- Type: setting
- From: [Austin Marchese and Nate Herk on managing agents](../../wiki/sources/manage-ai-agents-five-steps-austin-marchese.md) at 2:37 to 4:10
- Value: an agent that misreads "draft only" cannot send mail to a student, because the tool refuses.
- Already here: draft-first, send-on-"send" and no-delete are written in `CLAUDE.md`. `~/.claude/settings.json` runs `bypassPermissions` with git and system deny rules and five ask rules; none covers `gws gmail` send or delete or Drive delete. Hooks exist in `.claude/settings.json` and were not read. The memory note says Gmail and Drive deletes are denied; unconfirmed here. The accommodations `send.py` is allow-listed on purpose.
- Steps:
  1. Read the hooks and the `gws` grant to find what already blocks send and delete.
  2. List what an unattended agent could do today with `gws gmail` and Drive, by trying harmless commands against a test draft.
  3. Propose ask or deny rules for `gws gmail` send, Gmail and Drive delete, keeping the two pre-approved senders working. Show Joshua before editing settings.
  4. Check: after approved changes, a test send and a test delete are refused or prompt, and the accommodations email still runs.
- Effort: small · Status: new (2026-10-31)

### AQ-043 · Evaluate Destructive Command Guard for both runtimes
- Type: repo
- From: [plugin guide](../../wiki/sources/guide-claude-plugins-2026.md), [23 mistakes](../../wiki/sources/guide-claude-mistakes-2026.md)
- Value: assess whether an additional command guard can enforce the existing no-deletion rule.
- Already here: the guide supplies a link, not an installed guard; the upstream installer can alter machine-wide hooks and PATH.
- Steps:
  1. Inspect a pinned release, installer, current runtime versions and existing hooks; map which execution surfaces are and are not protected.
  2. Test a scoped configuration with harmless representative commands and preservation of existing hooks.
  3. Check: record enforcement, bypasses and rollback before enabling it for real work.
- Effort: medium · Status: new (2026-10-29)
- Progress 2026-10-29: [Evaluation](../../research/2026-10-29-guard/REPORT.md) verified release checksum and synthetic allow/deny results. Actual runtime dispatch remains untested; Windows Codex unified_exec is documented to bypass the hook. Guard not installed. Probe-induced Claude hook removed with other settings preserved; diagnostic files retained.

### AQ-042 · Claim eligible subscription API credits and try an API-backed tool
- Type: product update to verify
- From: [OpenAI API credits clip](../../wiki/sources/openai-chatgpt-subscription-api-credits.md) at 0:05 to 2:16
- Value: put included API credits toward a useful app or agent.
- Already here: OpenAI Developers plugin is available in Codex; account eligibility, linked organization, balance and recharge settings are unverified.
- Steps:
  1. Check subscription eligibility, billing cycle and the intended API organization in OpenAI billing.
  2. If eligible, link the intended owned organization and verify the grant and expiry.
  3. Choose a small useful API-backed project and use the existing OpenAI Developers plugin; keep keys in approved secret storage and monitor API usage.
  4. Check: billing shows the correct grant and organization, and a project request is reflected in usage without an unexpected paid recharge.
- Effort: small · Status: new (2026-10-29)


### AQ-041 · Evaluate the refreshed Codex CLI against the current workspace
- Type: product update to verify
- From: [Meet the New Codex CLI](../../wiki/sources/meet-new-codex-cli.md), 0:39 to 2:44.
- Value: tests whether native terminal task coordination and access improvements remove actual workflow friction.
- Already here: Codex desktop capabilities, a historical CLI setup and Herdr mixed-provider monitoring are documented. The capture does not identify CLI version, release channel, author or account requirements, and this ingest did not change local setup.
- Steps:
  1. Verify current official release/channel/account requirements and installed CLI identity without upgrading.
  2. Check availability and practical use of full-screen output/footer, voice start/mute, task search/filter/grouping, cross-task follow-ups, context-preserving worktree forks, remote access, usage analytics and Mermaid/LaTeX rendering. Label untested behavior.
  3. Compare native task views with existing desktop and Herdr workflows, preserving cross-provider and shared-file ownership distinctions. Remote enablement or upgrades require separate authorized scope.
  4. Check: one dated capability matrix names actual version, checked behavior, unsupported/unknown features, and a keep/change recommendation backed by a scoped test rather than promotional narration.
- Effort: medium · Status: new (2026-10-26)
- Progress 2026-10-26: Installed version, official latest release and command help checked. Remaining: bounded interactive voice/task/worktree/rendering acceptance if useful; no upgrade/remote enablement.

### AQ-038 · Audit skill routing collisions and briefing overlap
- Type: workflow change
- From: [anthropic-small-business-13-skills-austin-marchese](../../wiki/sources/anthropic-small-business-13-skills-austin-marchese.md), captured transcript; see source coverage limits.
- Value: Makes each request reach one clear owner and reduces competing reports.
- Already here: The catalogs and root routers already define workflow owners; this capture does not establish a local routing defect.
- Steps:
  1. Compare utility and orchestrator boundaries on actual local skill descriptions, including inbox routing, content strategy/posts and marketing review.
  2. Compare Monday, Friday and quarterly briefing purposes with existing morning/level-up routines, using real outputs before proposing consolidation.
  3. Propose only evidence-backed trigger or handoff changes; preserve current authorization boundaries.
  4. Check: representative requests select one owner, specialist handoffs are explicit and each retained briefing has a distinct decision.
- Effort: medium · Status: new (2026-10-26)
- Progress 2026-10-26: Concrete wording/teaching fixes landed and utility/orchestrator overlap is documented. Remaining: representative request-routing and actual briefing-output collision audit.

### AQ-034 · Benchmark deterministic section retrieval against current wiki routing
- Type: workflow change
- From: [RoboNuggets brain.js description](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) at 6:53 to 10:49
- Value: tests correctness, retrieval speed and token savings before adding another search layer.
- Already here: alias/index routing, pointer links, miss logging and Smart Connections history exist; the source's code and reproducible results are absent.
- Steps:
  1. Build a small representative question set with known supporting files/sections, ambiguous aliases and genuine misses; keep model/runtime and initial context comparable.
  2. Record current index/alias retrieval correctness, elapsed time, message tokens and files read.
  3. In a scratch implementation evaluate deterministic keyword normalization, index scoring, bounded section reads and pointer following; include stale index and unresolved pointer behavior.
  4. Compare maintenance cost and repeated measurements; keep the existing route unless the measured result justifies a change.
  5. Check: saved questions, traces, correctness grades, repeated timings/token measurements and a keep/skip recommendation support the conclusion without borrowing the source's claimed 40% saving.
- Effort: medium · Status: new (2026-10-26)
- Progress 2026-10-26: Compiled-page helper implemented and integrated into existing query skill copies;10 regression tests and8/8 local top-three/miss cases pass. Remaining: fair end-to-end agent comparison with actual model-token cost; local character/timing results are not that comparison.

### AQ-029 · Evaluate a bounded reference-driven design critique recipe
- Type: workflow change
- From: [claude-design-fifteen-hacks-jack](../../wiki/sources/claude-design-fifteen-hacks-jack.md), [astra-website-design-loop-jack](../../wiki/sources/astra-website-design-loop-jack.md), [rea-feature-investigation-chase-ai](../../wiki/sources/rea-feature-investigation-chase-ai.md), [rea-output-first-workflow-nate-herk](../../wiki/sources/rea-output-first-workflow-nate-herk.md); captured method sections, see each source summary and batch action matrix.
- Value: Turns reference comparison into concrete findings with limited review rounds.
- Already here: Existing critique, browser and build/review skills cover general review; exact promoted Design Loop/five-agent prompts are not fully captured.
- Steps:
  1. Resolve original guides/prompts if accessible and inspect their method and licence; label any locally authored recipe.
  2. Choose one feature and keep seen/inferred/unknown evidence, actual reference screenshots and a finite review scope.
  3. Check: a reusable investigation and critique yields specific observable findings, preserves unknowns and avoids inflated consensus scores.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Bounded critique recipe implemented with observable findings and finite revisions. Remaining: use it on a selected rendered feature and preserve before/after evidence.

### AQ-028 · Extend the section and flow reference map
- Type: workflow change
- From: [claude-design-fifteen-hacks-jack](../../wiki/sources/claude-design-fifteen-hacks-jack.md); captured method sections, see each source summary and batch action matrix.
- Value: Finds references for a particular UI problem rather than generic landing pages.
- Already here: Existing resource map includes component and inspiration sources.
- Steps:
  1. Evaluate the captured Navbar, Footer, CTA, 404, Unsection, Bento, 60fps and motion-primitives galleries, plus Mobbin/Refero flow references.
  2. Add only useful entries to the existing map with exact purpose, access and licence notes; inspect actual examples when selected.
  3. Check: a specific UI question reaches an exact reference and useful observation rather than only a homepage.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Region/flow lookup map and evidence/licence fields implemented. Remaining: inspect chosen gallery examples and their actual access/licence constraints.

### AQ-023 · Compare funnel decisions and competitor copy
- Type: workflow change
- From: [17-claude-design-use-cases-austin-marchese](../../wiki/sources/17-claude-design-use-cases-austin-marchese.md), [25-claude-design-tricks-robonuggets](../../wiki/sources/25-claude-design-tricks-robonuggets.md); captured method sections, see each source summary and batch action matrix.
- Value: Connects visual variants to actual visitor decisions.
- Already here: Website planning and Joshua teaching voice already exist.
- Steps:
  1. Map the real visitor journey and each stage decision.
  2. Study up to five relevant comparators and compare purposeful CTA/copy variants in Joshua voice.
  3. Check: every proposed change has an explicit user decision and linked reference evidence.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Finite visitor-decision/reference worksheet implemented. Remaining: selected acquisition task, actual comparator evidence and scoped funnel/copy pilot.

### AQ-022 · Evaluate a branded authentication-email template
- Type: workflow change
- From: [17-claude-design-use-cases-austin-marchese](../../wiki/sources/17-claude-design-use-cases-austin-marchese.md); captured method sections, see each source summary and batch action matrix.
- Value: Checks whether visual email templates fit the actual backend and clients.
- Already here: Existing application owns authentication; ingestion did not change its email settings.
- Steps:
  1. Inspect the target backend variables and email-client constraints.
  2. Draft HTML and plain-text fallback on scratch files and preview mobile/desktop.
  3. Check: exact variable mapping and compatibility evidence are recorded; no live template or email is changed.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Remaining: authentication backend variable mapping and actual email-client previews before any template change.

### AQ-021 · Pilot one reusable branded output template
- Type: workflow change
- From: [17-claude-design-use-cases-austin-marchese](../../wiki/sources/17-claude-design-use-cases-austin-marchese.md), [claude-design-fifteen-hacks-jack](../../wiki/sources/claude-design-fifteen-hacks-jack.md); captured method sections, see each source summary and batch action matrix.
- Value: Avoids recreating visual documents for repeated work.
- Already here: Existing voice, Design canvas and document tools cover authoring; no format was selected for this pilot.
- Steps:
  1. Choose one useful document: a proposal, flyer, lead magnet, poster, client variant or other reusable template.
  2. Use owned content and editable review; retain remaining example formats as options rather than commitments.
  3. Check: the approved template can be reused without changing voice or brand; no outbound action occurs.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Reusable teacher content tables exist. Remaining: selected branded document/template and its reusable rendered example.

### AQ-018 · Extract a selected LSAT U brand reference
- Type: workflow change
- From: [17-claude-design-use-cases-austin-marchese](../../wiki/sources/17-claude-design-use-cases-austin-marchese.md), [25-claude-design-tricks-robonuggets](../../wiki/sources/25-claude-design-tricks-robonuggets.md), [claude-design-fifteen-hacks-jack](../../wiki/sources/claude-design-fifteen-hacks-jack.md); captured method sections, see each source summary and batch action matrix.
- Value: A chosen direction can be reused consistently across runtimes.
- Already here: Generic design skills and prototype tokens exist; secondary dashboard regions are not finally approved.
- Steps:
  1. Choose an approved direction and read its current tokens, type, spacing, states and motion.
  2. Extract one code-readable brand reference and link it from the design hub; retain exploratory alternatives.
  3. Check: another runtime finds and applies the selected system from the hub alone.
- Effort: medium · Status: new (2026-10-24)
- Progress 2026-10-26: Capture fields and selected-family route exist. Remaining: an actually approved permanent brand direction and extraction of its tokens, states and motion.
