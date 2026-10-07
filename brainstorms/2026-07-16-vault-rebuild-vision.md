---
type: brainstorm
subject: Vault rebuild vision Brainstorm / Discovery Notes
updated: 2026-07-16
aliases: []
---

# Vault rebuild vision: Brainstorm / Discovery Notes
Date: 2026-07-16 · Goal: Lock the shared vision for the ground-up Obsidian vault rebuild on Nate Herk's architecture (AIOS-MASTER-PLAN Part 6) before executing anything — vault count/locations, fate of existing wiki content, LSAT teaching-corpus spin-off, hot/tasks/dashboard carryover, LSAT U code-knowledge placement.

Context going in: Joshua will clear existing Obsidian vault content and rebuild ground-up with the Karpathy LLM-wiki prompt (he supplies the prompt; NOTHING executes until he sends it AND this grilling locks the decisions). Onboarding intake (aios/aios-intake.md) stays the seed context. Plan of record: aios/AIOS-MASTER-PLAN.md.

## Summary / key decisions
(running synthesis, updated as we go)

4. **Q5 RESOLVED — LSAT U knowledge placement (confirmed "yes"):** Code knowledge stays IN the lsatu repo's own CLAUDE.md (other-worlds pattern; already good). Product/business knowledge (offers, pricing, launch status, bootcamps, decisions) lives in the new brain wiki, rebuilt organically via ingests + grills. Consequence: lsatu repo's CLAUDE.md/README wiki-paths (repointed earlier today at wiki/domains/lsat-u/...) DIE in the wipe → repointing lsatu references + rewiring /pickup//wrapup to the new ledger = explicit Phase-0/1 task.

3. **Q4 RESOLVED — operational files (confirmed "yes"):** `tasks.md` content CARRIES FORWARD into the new wiki's task ledger (real open work: Activity Centre, Intro to LR, VoiceCoach live-verify). `hot.md` rebuilt fresh (stale by definition). `log.md` starts fresh (new append-only history), old one archived. `dashboard.md` archived (regenerable from the app). The concepts (hot cache, ledger, log) all live on — Nate-native.

2. **Q3 RESOLVED — wipe policy:** ONLY `teaching-voice.md` carries over as a verbatim seed page in the new wiki (the one asset Joshua cares about). ALL other existing wiki content → `archive/wiki-pre-rebuild-2026-07-16/` (moved, never deleted; re-ingestable via raw/ later if ever needed). Joshua doesn't use/know the product-design docs, quality bar, or source map — the source map is regenerable from the lsatu codebase anytime. Karpathy prompt (stored at aios/karpathy-llm-wiki-prompt.md) builds the new wiki clean.

1. **ARCHITECTURE CONFIRMED (Q2, 2026-07-16):** One Obsidian vault = `~/ai-os` root. Three linked knowledge systems inside: `wiki/` (the brain — Joshua, business, decisions, hot.md), `corpus/` (LSAT teaching knowledge, Karpathy-built, future LSAT U feedstock), `students/` (per-student folders: transcripts, sessions, homework, schedules, profile.md wikilinked into corpus + LSAT U material). Root = the OS; no sub-nesting. Matches Nate's actual pattern (his "separate vault" is a folder inside Herk 2; he runs everything at Level 2).

## Q&A log

### Q1 — Vault count & location
- Asked: Two vaults (brain at ~/ai-os/wiki rebuilt in place + separate LSAT teaching corpus vault) vs one vs other split?
- Captured: Joshua says two-vault suggestion "is fine, BUT determine whether it is truly optimal." Wants investigation of how vault connections actually work and whether separate vs one centralized is best FOR HIS SETUP. Also: "should it be at the root, maybe a folder if I need to change that — optimize, keep that in mind" (root-vs-folder placement is open). Keep onboarding info central to the design.
- **Full vision dump (his words, condensed — this is the requirements spec):**
  - Ingest tutoring-session transcripts; keep FULL transcript per student in the student's OWN FOLDER, alongside their practice sessions, data, notes, developing profile.
  - Match each student with correct drills/materials already inside LSAT U; when needed use outside info from his existing corpus (corpus eventually integrates INTO LSAT U).
  - Assign appropriate work per student; manage student correspondence; track progress; know what's been covered; evaluate progression; incorporate interaction history, email correspondence, other useful info.
  - Assign homework, create study schedules + notes, prepare future sessions from the student's work/needs. Prep should become "nearly mindless" — system reviews everything, prepares lesson/lecture, organizes session; Joshua only shows up and teaches.
  - Post-session: generate notes, assign targeted drills/bootcamps/lessons per student needs.
  - Beyond tutoring: respond to messages from Gmail, 7Sage, Reddit, Facebook, any inbox/channel. All-encompassing: pre/post-consultation workflows, general business ops, personal-life tasks.
  - He's not sure how it all fits — wants me to think deeply, fully understand Nate's operating model (folders, files, information flow, skills↔folders interaction, practice), understand existing setup, design the best possible system.
- Flags: none yet — analysis owed by Claude (vault-connection mechanics → determination).

### Q2 (analysis) — Deep-read of the 5-levels section + vault mechanics (Claude research, 2026-07-16)
- Asked (by Joshua): re-read the course's "5 levels of second brain" deeply, catch anything missed, use agents for other parts.
- Captured — NET-NEW FACTS from the full read:
  1. **His "separate vaults" physically live INSIDE Herk 2.** The YouTube transcript wiki = `Herk 2/other worlds/YouTube OS/transcript wiki/`. "Vaults" are just Obsidian windows opened at subfolders. He *hardly ever opens Obsidian* — the visual graph is optional sugar; what matters is that the agent can traverse. → Directly validates the Q2 one-root/multi-system determination; `corpus/` inside `~/ai-os` IS his pattern.
  2. **He runs his ENTIRE Herk 2 at Level 2** (router + LLM-wiki + memory + references). Not L3/L4/L5. "I haven't felt a pain big enough to switch."
  3. **Levels are per-FOLDER, not per-system.** "Doesn't mean the whole folder needs one style" — one corpus could go vector-DB while context/decisions/projects stay markdown. Choose per data-type + usage.
  4. **L3 (semantic search) tradeoffs:** chunking loses whole-document context (his sales-table example: retrieval found week 6 as 'highest sales', missed weeks 14/19). Good for needle-in-haystack ("1000 rules, what's rule 17"); bad when full-context reads matter (meeting summaries → better as one markdown file read whole). Practical rule: describe the data + usage to the agent and ask which fits.
  5. **L4 (knowledge graph)** = an added folder/layer on top of the wiki (entities + typed relationships: works-at, endorsed-by). Wiki links are "see-also" backlinks, NOT typed/semantic relations. Graph can be MORE token-efficient than wiki for relationship-chasing (wiki must read full pages; graph reads edges). He demoed LightRAG + graphify over his whole brain but does NOT run it daily.
  6. **`@agents.md` injection:** referencing `@agents.md` inside CLAUDE.md injects the file — the twin-file trick without duplication.
  7. **Extraction > retrieval:** "before you blame AI, ask if the system actually has the nuance in your brain" — grill-me (checkpoint loop to a knowledge doc, exactly what we're doing now) is the extraction engine; it's the difference between 95% and 80% systems.
  8. Level movement is pain-driven in BOTH directions; team-sync is an adoption problem not a tech problem (moot — solo).
- Flags: two background agents sweeping transcript ranges 100k–264k (skills/subagents/connections/session practice) and 328k–440k (cadence/hooks/deployment/trust) → fold results in when they land.

### Sweep result 1 — course chars 328k–440k (cadence/hooks/deploy/trust/teams/tokens)
Key facts for OUR build (full brief retained by Claude; offsets available):
- **Routines:** 3 triggers (natural-language schedule / API call / GitHub events). Cloud routines: stateless clone of a GitHub repo, no local file access, env-var keys (NOT .env — his automation failed twice until prompt said "key is an env var, don't look for .env"), min 1-hour interval, Max plan = 15 runs/day, network access none/trusted/full. Local scheduled tasks can run every minute but need the machine on. Routine prompt = one-shot, never asks questions; best pattern = reference a skill + order of operations; consider a dedicated small repo per routine to keep context lean. Always "Run now" test repeatedly; add "if this fails, message me" tail.
- **Deterministic tier:** if the process is linear, deploy a Python script (Modal / trigger.dev), zero AI where possible ("if this was AI it would have fixed my typo" — template-fill beats AI); Modal Secrets for keys; feed failed run IDs back to Claude to fix permanently.
- **Trust:** scoped keys capped in $ (his: ~$1/day research key); when a tool has no scoped keys, HARDCODE the destination in the script so the agent can't choose it, and demand "prove it to me"; never commit .env; per-automation risk ritual ("what is our risk?" → mitigations).
- **Delegation economics:** subagent fan-outs ≈ 7–10× a single session; Haiku for subagents/bulk, Opus <20%; CLAUDE.md rule "3+ files → Haiku subagent, return summaries only." Agent teams = experimental, token-heavy, for debate/consensus ("war rooms", STORM-style); dynamic workflows = phased subagent waves for verification.
- **Token discipline:** disconnect unused MCP servers (~18k tokens/msg each; prefer CLIs); plan mode + 95%-confidence rule; compact at ~60% (never ride to auto-95%); session-handoff skill (summary → /clear → paste) replaces /compact; subscription cache TTL 1hr — model switches reset cache; token dashboard localhost.
- **Hooks & n8n: effectively absent from the course** — hooks only appear as settings.local.json env-var config. Our launchd/hook infrastructure is already beyond his course material.
- Maintenance frame: CLAUDE.md = constitution (<200 lines, decisions not conversations) + bounded applied-learning block needing periodic pruning; AIOS never finished — weekly additions.

### Sweep result 2 — course chars 100k–266k (skills/agents/connections/session practice)
Key facts for OUR build (full brief retained; offsets available):
- **Skills:** frontmatter description = the trigger; misfire → ask "why didn't you invoke it," rework description. Two build paths: proactive spec, or RETROACTIVE ("we just did this manually — turn those steps into a skill" — often better). New skills start read-only/approval-gated; autonomy only after 10–30 battle-tested runs. Skills can route to playbooks, run scripts, and CALL SUB-AGENTS; skills can be 5 sentences. Re-test all skills on every model release. His inbox-triage build: verify connection first → scoping questions → SKILL.md + references/ + scripts/ → corrections written back into the skill mid-run.
- **Sub-agents:** `.claude/agents/*.md` — name, description ("use proactively" allowed), pinned model, color (cosmetic), tools/disallowed-tools (read-only reviewers!), memory scope (project usually, NONE for amnesiac critics), max_turns guard. Delegate when output would dump a pile you'll never read; skip when steps are sequential/dependent or the worker needs to ask you questions. "Smart boss, cheap workers" (Opus orchestrator, Haiku workers). Skill/agent collision: Claude defaults to skills — have the skill invoke the agent or name it explicitly. Anti-sycophancy: adversarial "roast" personas in parallel. Scan third-party skills/agents for prompt injection.
- **Connections doctrine:** wiring recipe = Google "<tool> API documentation" → paste to Claude → key in .env → done; ~one tool/week. **API > CLI > MCP** ("the future is agents using CLIs"; one MCP ≈ 18k tokens/msg). AVOIDS desktop-app OAuth connectors — they lock you to the harness; .env+keys = tool-agnostic. GWS CLI = one interface to all Google Workspace (their Gmail/Calendar/Drive = OUR consultation + transcript pipeline). Visual-validation loops: give a skill screenshot access so it audits its own output.
- **Session practice:** session-handoff skill (shift-change doc → /clear → paste) at ~250k tokens or on any new distinct build; rejects autocompact; /clear between unrelated tasks = #1 habit; edit-and-regenerate over follow-up corrections; plan mode + 95%-confidence rule; batch requests; blank session floor 30–40k → prune MCPs, progressive disclosure.
- **Memory taxonomy confirmed:** CLAUDE.md = rules/router · memory = learned facts (one-fact-per-file + index — ours already matches) · wiki = knowledge, never autoloaded.
- **Build selection:** theory of constraints ("if you 5×'d students tomorrow, what breaks first?"); every build gets a north-star metric BEFORE building; "you can't automate what you can't map."
- Reusable pattern flagged: brand_assets/ + screenshot self-validation for generated artifacts (→ our worksheets/study schedules).

### Q3 — Fate of existing wiki content (IN PROGRESS)
- Asked: carry 5 canonical pages (teaching-voice, intro-to-lr-product/design, bootcamp-quality-bar, lsatu-source-map) as verbatim seeds + archive rest for selective re-ingestion — or hard reset (everything through raw/)?
- Captured so far: Joshua unsure how to answer; instead delivered the **canonical Karpathy LLM-wiki build prompt** (preamble: "You are now my LLM wiki agent… create the CLAUDE.md schema file with full rules, set up index.md and log.md, define folder conventions, show me the first ingest example. From now on, every interaction follows the schema."). Saved verbatim → `aios/karpathy-llm-wiki-prompt.md`. Prompt is IN THE PLAN, not executed. Note the prompt's own doctrine confirms: raw immutable / LLM owns wiki / schema co-evolves / one-at-a-time supervised ingest preference / index+log formats (`## [date] ingest | Title`) / lint ops / qmd as future search / answers filed back into wiki.
- Flags: Q3 decision still open → simplified recommendation put to Joshua (default: seeds + archive).

## Open flags (pending input)
- Root vs folder placement of the OS/vault → RESOLVED by 5-levels finding #1: root = OS = single Obsidian vault; knowledge systems are folders inside. Awaiting Joshua's confirm on Q2.
- BOTH agent sweeps complete and integrated. Course transcript now covered end-to-end (0–100k = beginner material, deliberately skipped).
