---
type: reference
subject: Decisions log
updated: 2026-07-20
aliases: []
---

# Decisions log

Append-only record of locked decisions — so nothing gets re-explained or re-litigated. Newest first. Format per entry: **Date · Decision · Reasoning · Context.** ("Save decisions, not conversations — every architectural call stored here is a paragraph you never have to type again.")

---

## 2026-07-20 — The second brain is a tiered distillation layer, not a RAG index
- **Decision:** Full context is delivered by four tiers, not by embeddings or semantic search. Tier 1 is the lean always-loaded context (`CLAUDE.md`, `context/`, native memory), hand-curated. Tier 2 is synthesized and regenerable. Tier 3 is one dense prose distillate per session or artifact, roughly 7:1 compression, preserving voice and verbatim quotes. Tier 4 is immutable raw source, read only when Tier 3 is insufficient. No vector store will be built.
- **Reasoning:** The corpus is lopsided, not large: 86% of 2.1M words are student transcripts, already partitioned per student by folder. Finding them was never the problem; reading 1.8M words is. Embeddings return chunks of transcript, which is the bulky raw material that is already too costly to use. A 500-word brief solves it outright, across ten student folders rather than ten thousand. `CLAUDE.md` already carried this instinct ("there is no semantic search and none is needed at this size") and it was correct.
- **Context:** Grilled 2026-07-20, 13 questions, full record in `brainstorms/2026-07-20-second-brain-architecture.md`. Two live retrieval tests decided it: querying "comparative passages" against the batch-1 graph returned zero correct hits while plain `grep` on raw source returned five, and a representative graph note pulled in full had one edge and no content beyond a link home. Tier 3 already exists as `graph-imports/distillates/` (125 files, 269,935 words) and had never been wired into anything.

## 2026-07-20 — Tier 2 is `_playbook.md` per topic, joining planned teaching to delivered teaching
- **Decision:** The synthesis layer is aggregated on two axes: by LSAT concept and by curriculum arc (the order concepts are actually introduced, derived from what happened rather than what was planned). Not by teaching move, which is not separable from the concept it teaches. It lives at `corpus/Curriculum/<Topic>/_playbook.md`, one generated file per existing topic folder. `Notes/` is ingested source and stays untouched.
- **Reasoning:** The concept axis already exists as folder structure (118 curriculum pages across Main Conclusion, Flaw, Necessary Assumption, Conditional Logic and the rest), so this enriches the tree already in use rather than growing a parallel truth. Curriculum arc is the half that would be missed: a lesson plan is sequencing and prerequisites, not only content. Keeping synthesis in a separate file from `Notes/` preserves the line between what Joshua authored and what was inferred, which for a system meant to speak in his voice is the worst possible contamination to allow.
- **Context:** The join is the point. What he planned to teach is in `corpus/Curriculum/`; what he actually taught is in the distillates; nothing connected them. The gap between the two is also the critique signal, the computable form of "where did I miss something". De-personalizing by concept also resolves student staleness: a former student's session still teaches how Joshua teaches, and that does not expire.

## 2026-07-20 — One unified graph, built after ingest, not four batches merged
- **Decision:** The target is a single graph over the whole brain at document altitude, where every node carries real prose and is worth landing on standalone. The four existing vaults (`vault`, `vault-b2`, `vault-b3`, `claude-code-docs`, 5,406 notes) are staged batches that will not be merged into it. They stay on disk and stay visible in Obsidian, per Joshua's explicit call that he wants to see everything. Connection finding is a core organ, serving the third job of the brain (critique), alongside retrieval and synthesis.
- **Reasoning:** Merging inherits the defect. The batches are stub quality, so assembling them yields one large stub graph, which is both unbrowsable for Joshua and token hostile for the model (pay to read a pointer, pay again for the real file). Sequencing matters more: a graph cannot create knowledge the vault does not hold, and the business half is barely written down (roughly 3,800 words against 2.1M of LSAT material). Building now yields a map with teaching richly connected to itself and the cross-domain edges most wanted having no endpoints. Joshua's objection that business and teaching are intertwined is the strongest argument for ingest-first: the connective tissue is the homework, correspondence and follow-ups, none of which is ingested.
- **Context:** Corrected mid-interview by Joshua. The four vaults were never four intended products; they were batches deliberately held unmerged while he decided whether merging would flood the working vault. That caution was correct and the blocking question was the right one. Also established: `brainstorms/2026-07-19-takeout-deep-ingest-emulation.md` locked ten decisions that were never executed (no `students/former-students/`, no domain wiki pages), and three graph batches were built the following day instead. The inbox is tractable at 3,318 messages; most Takeout bulk is Drive.

## 2026-07-20 — The booking pass is the only record of owed sessions
- **Decision:** A booking pass is the sole record that sessions are owed to a student. **No pass means nothing is owed, by definition.** There is no reconciliation between Stripe package purchases and passes granted, and none will be built for now. A student with no pass is the normal case, not a gap: they schedule individual sessions through their Stripe-linked Cal.com link. Only a student owed sessions holds a pass. Revoked passes are dead links and are excluded everywhere; exhausted passes are live but owe nothing.
- **Reasoning:** Matches the business as it actually runs — everything is paid upfront and `context/work.md` states plainly that no package-balance model exists. Building a Stripe reconciliation layer would invent a second source of truth for entitlement and a purchase-to-student matching rule that does not exist. **The accepted cost is a real silent failure: if someone pays for a package and the pass is never granted, nothing in the brain catches it** — the student has to say so. That trade was made knowingly, on the grounds that Joshua grants the pass at purchase time and the failure has not been observed.
- **Context:** Grilled 2026-07-20. Corrects a modeling error shipped hours earlier, where the roster listed students without passes under "No booking pass — grant booking access before drafting anything," framing the normal case as a defect. Companion decisions the same day: contact truth is Gmail behaviour, never a pass's stored email (Ethan's pass carried an address with one message against it while he corresponded from another with 201); status stays authored but contradictions are surfaced (Yahunatan sat as `prospect` holding 9 owed sessions); one lifecycle path — prospect, active, lapsed — with no "not a student" category, since Yahunatan was a consultation on 07-07 and a paying student by 07-15; a taught session is what earns a `students/` folder; and arrangement is authored while the remaining count is regenerated from the backend, never typed by hand (the hand-written mirrors had drifted within a day). Vocabulary in `CONTEXT.md`.

## 2026-07-17 — Adopt Nate's Four Cs / Three Ms layer (audit + level-up + connections + operator brain)
- **Decision:** Graft the useful parts of the canonical AIS-OS starter kit (github.com/nateherkai/AIS-OS, MIT) onto the existing OS: the `/audit` skill (Four-Cs structural score /100), the `/level-up` skill (weekly 3Ms interview → ship one automation), `connections.md` (7-domain registry of live systems), and `references/3ms-framework.md` (the operator brain). Both skills adapted to this layout (credit the Level-2 wiki, students, corpus, native memory, gws connections) and saved-to-both (DB + activated, Claude + Codex).
- **Reasoning:** The OS had the bones (Context + wiki) but no recurring compounding engine. `/audit` answers "where do we stand" systematically; `/level-up` is the disciplined Phase-4 build engine (EAD, autonomy-spectrum, Bike-Method guardrails baked in). Skipped `/onboard` (past it) and `EXPANSIONS.md`/intake (already have `aios/aios-intake.md` + router guardrails).
- **Context:** Full read-through of the public AIS-OS repo 2026-07-17. Intern-Rule note: the kit warns against giving the AI passwords/bank info — Joshua deliberately overrode this (`.env` holds them), so security rests entirely on `.claude/settings.json` deny-lists.

## 2026-07-17 — Slim `system/` to load-bearing plumbing only
- **Decision:** Delete the 15 one-shot migration/rename scripts and their 7 orphaned tests from `system/scripts/`. Keep only the auto-run chain (bootstrap, scan-secrets + pre-commit hook, backup job) plus the manual validators (check-skills, gen-skill-index, cold-start, skill-smoke, run-tests).
- **Reasoning:** The scripts were brain→ai-os rename archaeology, unreferenced by any live path; `system/` should hold only how the OS keeps itself alive.
- **Context:** Verified none referenced by hooks/plists/settings/bootstrap before deleting. Follows the reform's "hand-edit, no generators" direction.

## 2026-07-17 — Memory consolidates to native automemory
- **Decision:** Use Claude Code's native automemory (`~/.claude/projects/-Users-joshuaf-ai-os/memory/` + `MEMORY.md` index) as the one memory system. Migrate the 28 memories from the custom `~/ai-os/memory/` store into it; retire the custom memory scripts and `.claude/rules/memory-os.md`. Codex reads the same files by path.
- **Reasoning:** Two parallel memory systems = duplicated truth. Native automemory is zero-maintenance and is exactly the sources' model ("CLAUDE.md is the rules, memory is learned facts").
- **Context:** Audited 2026-07-17: native store active and correctly formatted; custom store declared it "deprecated" — backwards. Reform plan Phase 2.6.

## 2026-07-17 — `system/` simplifies to a hand-edited router
- **Decision:** Retire the schema generator (`core.md` → CLAUDE.md/AGENTS.md hourly regeneration) and the churn launchd jobs (ingest 5-min, reindex 30-min, memory-distill, session-guard). Keep the secret-scan pre-commit hook and a working nightly backup. `CLAUDE.md` becomes hand-owned; on major edits, mirror to `AGENTS.md` by hand.
- **Reasoning:** The generator structurally blocks "just tell Claude to edit the file," which Joshua explicitly wants. The sources' dual-runtime sync method is one sentence by hand, not a generator. Most jobs churned on an empty inbox; the backup job was already broken (pointed at a nonexistent script).
- **Context:** Adversarial two-agent review (KEEP vs KILL) 2026-07-17 + the two Codex sources. Reform plan Phase 2.

## 2026-07-17 — Level 1 foundation built by MOVE, not duplication
- **Decision:** Create `context/` (about-me · work · priorities) and this `decisions/log.md` as the Level 1 layer. Content MOVES in; old locations become pointers. Stay at Level 2 overall — no vector search, no standing knowledge graph, no always-on sync (`graphify` remains on-demand).
- **Reasoning:** One authoritative home per fact (duplication is a token-wasting error). Levels are per-folder; upgrade only on felt pain — and the sources' author himself operates at Level 2.
- **Context:** The 5-Levels source + the 27-min EA source; reform plan Phase 1.

## 2026-07-17 — Secrets = `.env` + `.gitignore`, nothing else
- **Decision:** One `.env` at the root is the single store for API keys, passwords, and bank/account info. `.gitignore` keeps it out of Git. No `private/` tier, no macOS Keychain, no encrypted vault (the `records.sparsebundle` design is dead, not deferred). Government IDs stay outside the OS entirely. Never paste a credential into chat — add it to `.env` in the editor.
- **Reasoning:** Matches the sources' actual model (keys in `.env`, ignored by git — that's the whole thing). The Tier A/B apparatus was invented locally, protected against threats Joshua doesn't prioritize, and complicated everything.
- **Context:** Joshua's explicit call, overriding the earlier out-of-scope rule. `private/` + `system/migration/` (402MB) deleted the same day.

## 2026-07-17 — Dual runtime: Claude Code + Codex, hand-synced
- **Decision:** Both runtimes work this workspace. All knowledge (`context/`, `wiki/`, `students/`, `corpus/`, `projects/`, `decisions/`) is shared tool-agnostic markdown. Config is per-tool (`CLAUDE.md`+`.claude/` vs `AGENTS.md`+`.codex/`+`.agents/`). Sync on major router edits is by hand ("also make that change to AGENTS.md"). Never both agents editing the same file at once; hand off via session-handoff.
- **Reasoning:** Tool-agnosticism ("you owe these companies zero loyalty") + adversarial cross-checking between models. The sources sync by hand; no machinery needed.
- **Context:** The two Codex sources in SETUp; reform plan Phase 3.

## 2026-07-20 — `pickup` is explicit-only
- **Decision:** Run the `pickup` skill only when Joshua explicitly asks for it. Never trigger it automatically at the start of a session. `wrapup` remains the normal end-of-session persistence step.
- **Reasoning:** Automatic pickup adds irrelevant orientation work when the request is already specific and self-contained.
- **Context:** Joshua explicitly corrected the session-start behavior after an inbox and 7Sage review request.

## 2026-07-20 | Consultation follow-ups use scheduled send with an intervention window
- **Decision:** For a prospect who completed a consultation and has not paid, schedule the follow-up for 3:00 PM Toronto time on the next calendar day, including Saturdays, Sundays, and statutory holidays. It sends automatically unless Joshua stops or changes it before the scheduled time. This is a bounded exception to the general rule that AI-generated outbound messages remain drafts.
- **Reasoning:** Joshua wants the follow-up to happen reliably without requiring an approval click, while retaining time to review, edit, or cancel it.
- **Required guardrail:** Validate the recipient, prospect state, prices, and price-to-link mapping before scheduling and again before sending. Fail closed on placeholders, malformed links, editor links, login-token URLs, self-addressed tests, and contradictory tier mappings. This is required by failures found in Joshua's actual sent-mail archive.
- **Context:** Resolved during a `grill-with-docs` review of the imported Email HQ consultation workflow.

## 2026-07-20 | Variant C is the standard consultation follow-up template
- **Decision:** When a completed consultation produced no special arrangement, use Variant C from `email system/Post-Consultation Follow-Up Template.md` as the canonical base. It presents the three standard tutoring offers. Bounded fields may supply one or two personalized lines, the 7Sage request when applicable, current prices, and verified action links.
- **Reasoning:** Variant C is the stored template that matches the required three-tier offer, and Joshua's sent-mail archive supports its broader warm-recap and clear-actions structure.
- **Context:** A special arrangement still overrides the standard price or link for the affected offer.

## 2026-07-20 | Consultation intake belongs in LSAT U
- **Decision:** Remove the application-form step from consultation follow-ups. Do not send Google Forms or `gformsapp.com` application links. Intake will happen inside LSAT U during onboarding.
- **Reasoning:** One platform should own onboarding data. Keeping the old form step would duplicate intake and preserve links that have already failed in real correspondence.
- **Context:** This changes Variant C's action sequence but preserves its warm recap and three-tier offer structure.

## 2026-07-20 | Confirmed payment triggers onboarding
- **Decision:** A prospect does not need to reply after purchasing. Confirmed payment triggers LSAT U onboarding automatically. Any consultation follow-up still waiting to send is cancelled if payment arrives first.
- **Reasoning:** Stripe and Stripe-linked Cal.com are the operational authorities for standard payments, so asking the prospect to report a payment the system can observe adds friction and creates duplicate state.
- **Context:** A special arrangement uses the payment authority stated for that arrangement.

## 2026-07-20 | LSAT U account creation may precede payment
- **Decision:** Consultation follow-ups include `https://lsatprep.study` near the end of the next steps. A prospect may create an account before payment, and the conditional 7Sage Analytics request appears beside that step. Confirmed payment is still required before Joshua grants student permissions or onboarding begins.
- **Reasoning:** Account creation is safe before payment because Joshua controls LSAT U permissions on his side. Separating account creation from onboarding removes the earlier false equivalence between signing up and receiving student access.
- **Context:** This corrects the earlier statement that LSAT U should appear only after payment; onboarding remains post-payment, but account creation does not.

## 2026-07-20 | Special arrangements replace the standard offer
- **Decision:** If the consultation established a verified person-specific arrangement, the follow-up presents only that arrangement. It does not show the standard three-tier menu beside it.
- **Reasoning:** Mixing bespoke and standard terms can contradict what was agreed and confuse the prospect about which offer applies.
- **Context:** The standard $45/$40/$35 three-tier offer is used only when no special arrangement exists.

## 2026-07-20 | Standard offer is the default unless Joshua explicitly overrides it
- **Decision:** Use the standard three-tier offer unless Joshua explicitly states a special arrangement. An explicit statement captured in the consultation notes or email thread counts; circumstances and historical links do not.
- **Reasoning:** Different arrangements exist, but the automation must not invent discounts or bespoke terms from indirect clues.
- **Context:** Ambiguous evidence resolves to the standard offer, not to an inferred exception.

## 2026-07-20 | Consultation follow-ups do not claim a multi-day delay
- **Decision:** Remove the breathing-room line from the standard consultation follow-up. Do not say Joshua waited a couple of days or gave the prospect time to think.
- **Reasoning:** The workflow sends at 3:00 PM Toronto time on the next calendar day, including weekends and holidays. A claimed multi-day delay would often be false, and the sent-mail archive shows that the line was not consistently part of Joshua's actual voice.
- **Context:** Resolved during the `grill-with-docs` review of the imported consultation templates and sent-mail evidence.

## 2026-07-20 | Standard consultation emails show hourly rates only
- **Decision:** Present the standard offers as $45/hour for a single session, $40/hour for the five-hour package, and $35/hour for the ten-hour package. Do not show package totals in the email.
- **Reasoning:** Joshua wants the prospect-facing comparison centered on the hourly rate. The automation must still verify the total charged by each link before it schedules or sends the message.
- **Context:** This is a presentation rule, not a change to the underlying $200 and $350 package totals.

## 2026-07-20 | Consultation offer links use action-specific labels
- **Decision:** Label the single-session action `Schedule here`. Label the five-hour and ten-hour package actions `Purchase here`.
- **Reasoning:** Scheduling and purchasing are different actions. The labels should tell the prospect what each link does before they click it.
- **Context:** This applies to the standard Variant C option list.

## 2026-07-16 — carried forward from `aios/DECISIONS-POST-REVIEW.md` (pre-reform)
- **D2 — Student data:** one tracked folder per student under `students/<name>/` holding everything (transcripts, correspondence, homework, notes, profile). Git history retains student data permanently — accepted; the scrub-before-any-remote checklist (`wiki/HANDLING.md`) is the compensating control.
- **D3 — Consultation email sends:** fixed pre-approved templates may auto-send via deterministic scheduler; anything AI-generated stays a Gmail draft for approval.
- **D4 — Operational state:** live systems are authority, the brain mirrors. Cal.com + Google Calendar = sessions; LSAT U Supabase = homework/dossier/publish; Stripe = payments; Gmail = correspondence. Backend wins on disagreement. The brain is primary for transcripts, teaching notes, judgments, prep briefs, curriculum, decisions.
- **Architecture:** one vault = the `~/ai-os` root; three knowledge systems (`wiki/`, `corpus/`, `students/`); LSAT U code knowledge stays in the lsatu repo.

## 2026-09-17: General Conditionals paired answers
Joshua approved four answer options, each containing a diagram and its proposed contrapositive. Distractors must separately test translation and contraposition, including a wrong translation with a valid contrapositive of that wrong translation. Use refined slash negation and percentage-only in-session progress. Preserve existing attempts and scores. Applies throughout General Conditionals, including compound and multi-rule items.


## 2026-09-23: Accommodations email is a pre-approved send template
The "Request for Accommodations" email (Joshua's 2026-09-19 Celia wording, plus a line saying to register for a test date first and the note that removing the experimental section is written under "Other") is pre-approved. When Joshua asks for the `accommodations-email` skill for a named student, that counts as the go-ahead: it sends right away with the LSAC Qualified Professional Form attached and logs to wiki/send-ledger.md. The wording stays fixed. Only the name and the accommodations list change per student.

## [2026-09-23] decision | LSAT U operations run through system/scripts/lsatu only
All platform ops (assign, message, read messages, student data) go through the lsatu script; no Lovable, no credits. Hosted MCP connector left as-is, unused.

## 2026-09-27: Stripe payments inform, the teacher grants
Joshua chose all three entitlement rules for the Stripe ledger. (1) A payment recognized as a session package never grants booking passes on its own. It appears on the teacher Home with a one-click "Grant N passes" confirmation, so the 2026-07-20 rule stands: passes are the record of sessions owed. (2) A payer who cannot be matched to a student confidently goes into a review queue on the teacher Home with a link-to-student picker. Nothing is granted until Joshua links it. (3) Only booking Checkout and session/package products turn on platform access automatically. All other charges are logged and nothing more. This narrows the current webhook, which tries to grant access for any paid Checkout.

## 2026-09-27: LSAT U navigation consolidation

Joshua accepted three directions before the LSAT Lab and 7Sage UI audit. Student **My Work** combines Assigned work and Notes & recaps as internal tabs for To do, Completed, and Notes & recaps. **Review** groups Wrong answers and Flagged; **Progress** groups Analytics and History. The teacher gets a shorter, separate workspace rail with a View student experience shortcut. Teacher Bootcamps and Activities remain separate tabs inside Library. Preserve the different records and direct links while merging destinations. The running comparison and data prerequisites are in `research/2026-09-27-lsat-platform-ui-audit.md`. No video production is planned for this phase.

## 2026-09-28: Practice Exams stays complete inside Practice

Joshua accepted one **Practice** destination in the shorter student rail, with **Drills** and **Practice Exams** as distinct areas inside it. Practice Exams keeps the previously approved landing page with full PrepTest and timed-section start actions, **Unfinished exams and sections**, **All Exams** with PrepTest detail pages, and **Attempts** with in-progress and completed exam and section sittings. Saved sets stay with Drills. Timed work retains an explicit start step. This placement does not change the 2026-09-26 decisions about account-backed exam progress, pause behavior, second-device takeover, access changes, or the unresolved attribution of older browser-only runs. The revised sample design is `brainstorms/2026-09-28-lsatu-student-experience-design.md`; no application implementation was authorized by this placement decision.

## 2026-09-28: Impeccable reviews the completed LSAT U redesign before release

Joshua wants an Impeccable pass at the end of the student and teacher experience work to find improvements. Run its critique and technical audit on the functional application, resolve material findings through polish or targeted passes, and verify the affected screens again before the core rollout. Use LSAT U's product, design, and Classroom surface rules as context. Keep data correctness and task walks as separate release checks. This decision adds a quality gate to the adoption game plan; it does not authorize application implementation or a Lovable credit spend.

## 2026-09-28: Locked tabs remain visible in the student redesign

Joshua chose to show all tabs, including unavailable ones. An unavailable tab shows a lock and cannot open its page; a direct link remains subject to the same permission gate. This resolves [grouped student page access](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/156). Joshua also confirmed that Mark reviewed clears the review task while preserving the separate flag and answer history. He initially chose a read-only View student experience, but later corrected that choice: teacher/admin access must remain fully interactive. The [teacher scope ticket](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/162) records the revised rule.

## 2026-09-28: Student route and saved rail migration

The [canonical path decision](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/157) keeps seven stable student destinations with URL-backed local tabs. Old links forward to the equivalent place and preserve the selected question, filter, and return destination. Saved rail choices move once to a versioned seven-item preference without overwriting the old record. Full-screen question, test, and Activity runners keep their existing routes. The exact cross-source Review detail path remains for the Review ticket. A code/design mismatch in Admissions access is tracked separately in [Admissions access](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/164).

## 2026-09-28: My Work keeps each assignment and requires a real finish

Joshua chose a complete assignment history, including repeated guided drills. Practice work moves to Completed only when its source saves a finish or submission; merely opening it is not In progress. The student's own notes join Joshua's notes and session recaps in Notes & recaps, with author and type labels. The full [My Work record and status contract](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/158) also keeps unfinished overdue work in To do and requires student/teacher parity from the same scoped ledger.

## 2026-09-28: Review keeps source, reason, and history

Joshua directed the Wayfinder work to move ahead with the recommended Review rules. Missed, flagged, skipped after a session, and explicitly Joshua-selected items can create To review tasks. A missed answer needs a short written explanation before Mark reviewed. Mark reviewed closes that task but retains its independent flag and answer history; a new miss creates a new task. A typed source reference prevents LR, RC, Activity, and bootcamp items from being collapsed into an LR qid. The full [Review lifecycle decision](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/159) preserves first and blind answers and requires truthful coverage labels while source adapters are added.

## 2026-09-28: Pause timed exams when account saving fails

Joshua confirmed that a new timed exam should keep a temporary device backup, pause the exam and clock, and show the problem if account saving fails. Progress resumes when saving works. This clarifies the [Practice Exams discovery](../brainstorms/2026-09-26-practice-exams-discovery.md). Older browser-only progress without a student ID still cannot be attached safely to an account; Joshua made no decision about its optional display or recovery after asking for a simpler explanation.

## 2026-09-28: Admissions is admin-only while unfinished

Joshua directed an immediate lock on the unfinished Admissions page. Students should see its navigation item as locked and be denied the direct route. Joshua and admins retain access. This reverses the earlier recommendation to leave the current signed-in access unchanged. The [Admissions access ticket](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/164) tracks implementation and live verification.

## 2026-09-28: Do not wait for a current-student prototype test

Joshua chose not to make a current-student walkthrough of the clickable prototype a prerequisite to the build spec. The [Wayfinder test ticket](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/163) was closed as outside the map's required path. Internal task walks and app verification remain in the plan.

## 2026-09-28: Progress uses first graded answers and discloses its evidence

Joshua accepted the recommended [Progress calculation contract](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/161). Diagnostic accuracy uses the first saved, graded answer to each distinct LR or RC question for the student. Repeat attempts remain in History and practice volume; Inspect visits, blind-review answers, and ungraded work do not enter diagnostic accuracy. LR and RC are labeled separately. Every percentage names its included sources and modes and shows the correct count and eligible-question denominator; missing coverage is disclosed instead of appearing as zero. The approved 7/14/21/30/All timeframe governs statistics and History. Assignment attribution requires an explicit stored link, and Joshua's view uses the same calculation under authorized student scope. The existing student Analytics, legacy Analytics, History, and teacher Insights count retries differently, so this is a rebuild rule, not a claim about current live behavior.

## 2026-09-28: Teacher view retains full admin access, with teacher answers separate

Joshua corrected the earlier read-only preview proposal. When he opens a selected student's experience, he and other admins retain full teacher/admin access to act on that student's work. The screen must identify Teacher mode and the selected student, and teacher/admin changes must be attributed to the acting account. Joshua specifically chose that answers he gives to questions while viewing a student must stay separate from the student's score and History. They must not create student attempts or alter student completion, accuracy, or Review. The [teacher scope decision](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/162) is the implementation contract; no student-auth impersonation is needed.

## 2026-09-28: Wayfinder handoff and legacy exam boundary

The [Wayfinder map](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/155) is complete. The [implementation spec](https://github.com/vnjkoxpl-42905/lsatu-684d89db/issues/165) and fifteen blocker-aware build tickets cover student flows first, the existing teacher desk, viable question tools and weekly settings, and final Impeccable review. For ownerless older browser-only exam runs, Joshua did not choose a display or recovery design after repeated clarification attempts. The first release will preserve those local copies untouched, keep them out of account Attempts, and defer optional recovery. This is a safe scope boundary, not an attributed preference about a future recovery design. The latest `main` contains account-backed full PrepTest sync; timed LR/RC failed-save pause and live backend verification remain implementation work.

## 2026-09-29 Git remote enabled
- Decision: the "no Git remote, ever" rule is removed. origin on GitHub is the setup. Reason: lets Claude Code cloud sessions and other machines work on the repo. Never-track list still holds (.env, projects/lsatu/, logs, locks, gitlinks). wiki/HANDLING.md scrub checklist is now advisory.

## 2026-09-30: Apply the LLM Wiki pattern to the existing second brain

Joshua directed implementation of the supplied LLM Wiki idea file in the current vault and use of its schema for future knowledge work. Preserve raw evidence, compile and maintain linked knowledge, retrieve through indexes, save durable findings, and record changes in append-only logs. Keep one public `ingest` workflow; retain `second-brain-ingest` as a compatibility alias. Query and lint remain distinct; setup applies only to a new vault. Preserve student/corpus homes and live-system authority. The detailed contract is [the operating schema](../system/schema/llm-wiki.md), grounded in [the supplied source](../wiki/sources/llm-wiki-pattern.md).

## 2026-09-30: Keep application repositories outside the Obsidian vault

Joshua authorized moving the entire application tree to sibling C:/Users/Joshu/dev/ai-os-projects after the vault stalled loading. The ai-os directory remains the knowledge vault and raw/inbox remains web-clip intake. Do not link heavy application/dependency trees back into the vault. Preserve application repos and working copies as separate operational roots.


## 2026-09-30: Shared lecture library for live teaching

Joshua specified a standalone teaching library, separate from student records. Route through corpus/lectures by Logical Reasoning or Reading Comprehension, topic, Core or Advanced, then the individual lecture. Core is the easier level. Topic names may represent question types, question families, or reasoning skills; use tags and cross-links for overlapping concepts while keeping one canonical package. Every folder level has an MD index. Each lecture and level index identifies exact PrepTest section/question numbers in original presentation order. Prepare a pre-lecture teaching brief before the teleprompter so Joshua can retrieve a lecture by topic, level, or covered concept and use it during live video calls. The Must Be True lecture dated2026-08-27, video33013, is LR/Core.

## 2026-09-30: Deploy the LSAT U audit backend while preserving current work

Joshua explicitly authorized the Lovable Cloud backend/database deployment and continued implementation of the audit plan. Preserve current assignments, answers, results, and history; use additive installation and verify original row values before and after deployment. Free Lovable database and publication controls are authorized. Any action that may spend Lovable credits still requires immediate, specific confirmation. No account data cleanup or deletion is authorized by this deployment approval.


## 2026-09-30: Recap references guide quality, not topic scope

Joshua clarified that the Some, Most, and All note is a teaching/design quality benchmark, not permission to add quantity content to conditional reasoning. Future recap runs must use the accumulated [recap calibration](../skills/codex/post-session-recap/references/recap-calibration.md), stay within the selected concept and authorized enrichment, and record new feedback for skill refinement. Applied in both runtime skills and current V10.
