---
type: brainstorm
subject: Project CLAUDE.md .claude/ Standardization Brainstorm / Discovery Notes
updated: 2026-07-16
aliases: []
---

# Project CLAUDE.md + .claude/ Standardization: Brainstorm / Discovery Notes
Date: 2026-07-15 · Goal: Nail down exactly what Joshua wants for standardizing project-level CLAUDE.md files and .claude/ folders across all ~/ai-os projects, and the standing rule for future projects.

## Summary / key decisions (FINAL — design complete)

**What Joshua actually wants (surfaced by the grill):** not just "give every project a CLAUDE.md" — a full two-level Claude setup with a consolidated master DATABASE for skills/agents/commands, deliberate activation, and auto-capture.

### 1. Two parallel config levels (session reads BOTH; project layers on global)
- GLOBAL `~/.claude/`  — loads everywhere. Standard shape: CLAUDE.md + settings.json + commands/ + agents/ + skills/.
- PROJECT `<proj>/` + `<proj>/.claude/` — loads only in that project. Same shape.
- Global must be HYPER-CONSERVATIVE (only genuinely cross-cutting items). Project-specific things live in their project.

### 2. Per-project standard (ALL projects — brain root, lsatu, life-path, email-hq, briefbar, cluely, hypertrophy)
```
your-project/
├── CLAUDE.md            # plain-English rules for THIS project; also POINTS to the master DB for discovery/import
└── .claude/
    ├── settings.json    # permissions & config
    ├── commands/        # this project's slash commands
    ├── agents/          # this project's subagents
    └── skills/          # this project's skills
```

### 3. Master DATABASE in the brain (skills, agents, commands)
- Location: brain/skills/, brain/agents/, brain/commands/ (skills/ expands from "authored-only" to full master DB).
- Holds EVERY item (incl. the ~72 vendor/plugin skills). Exhaustive: union across Claude + Codex + plugins (~129 unique skills across 7 roots today). Nothing missing.
- A+B storage: authored = real files (source of truth); vendor/plugin = LIVE symlink into plugin location (A, self-updating) PLUS a frozen real copy under _snapshots/ (B, git-tracked, survives plugin removal).
- The DB is INERT storage — it NEVER auto-loads into a chat.
- INDEX with ONE clear line per item explaining what it does (auto-generated from each SKILL.md/agent `description`).
- Fix all stale pointers (22 global symlinks point at retired ~/Documents/... LSATU paths) to resolve into the DB.

### 4. Save + Load behavior
- SAVE a skill/agent/command => writes to BOTH the current project's .claude/<kind>/ AND the master DB. Every time. Project-scoped by default, NEVER auto-global.
- LOAD => only ACTIVATED items load (conservative global + current project). DB stays silent. => "don't load every skill in every chat."
- Activation = pointer (symlink) from an active location into the DB.

### 5. Assumptions ADOPTED as defaults (Joshua can still correct)
- Codex side (~/.agents/skills, lsatu/.agents/skills, ~/.codex/skills) feeds from the SAME master DB so Claude+Codex stay in sync.
- The DB is git-tracked in brain (backup/versioning).
- Enforcement: skill/agent creation defaults to writing into the DB (skill-creator points there); a lint/sync check (extend check-skills.sh) flags anything outside the DB. Standing rule also documented in global ~/.claude/CLAUDE.md.

### 6. This is a BUILD, not a quick task
- Consolidating ~129 skills across 7 roots + wiring A+B + index + auto-capture + scaffolding 7 projects = its own plan. Next step: write PLAN.md and execute skills-first, then agents, then commands.

---
### Starting point / prior state (for reference)
- Joshua's opening: "all projects should have CLAUDE.md + project .claude folder." Grill expanded it to the above.
- Current: brain root/lsatu/life-path/email-hq have CLAUDE.md+.claude (varying completeness); the 3 apps have nothing. Standing rule was only prose in global CLAUDE.md, no tooling.

## Q&A log

### Q1 — Grounding: current state + is it automatic?
- Established: NO auto-scaffolder exists. Every CLAUDE.md/.claude was placed by hand. `mkdir projects/foo` gets nothing. The "standing rule" is just prose in global ~/.claude/CLAUDE.md, not enforced tooling.
- Verified per-project table: brain root / lsatu / life-path / email-hq have the pair; apps (briefbar, cluely, hypertrophy) have NOTHING. lsatu is the fully-loaded example (hooks, launch.json, safe-push, statusline, skills).
- Confirmed Claude understands what .claude/ is: per-project config dir (settings.json = allow/deny/ask + hooks + model + plugins + statusline; also agents/, commands/, skills/, hooks/). CLAUDE.md is separate = written guidance loaded into prompt.

### Q2 — What Joshua wants IN the .claude folder (scope of contents)
- Joshua: wants **agents, memory, workflows, and plans** handled in the .claude folders too — not just settings.json.
- Wants this "in all" — ESPECIALLY lsatu, email-hq, life-path.
- INTERPRETATION (to confirm): each project's .claude/ should be a fuller workspace — agents/ (subagents), some notion of project memory, workflows, and plans — not just a permissions file.
- Flag: need to pin down what "memory," "workflows," and "plans" concretely mean to him as files/folders (Claude Code has no standard .claude/memory or .claude/plans convention — these may be Joshua's own desired structure). RESOLVE NEXT.
- Joshua confused about the term "brain root" — answered separately (it = the ~/ai-os top-level vault itself, which is also its own project/git repo).

### Q3 — Target structure (Joshua showed two reference screenshots)
- Joshua wants each project's `.claude/` folder to contain a FULL set of subfolders, matching a reference file tree he showed:
  - `agent-memory/`, `agents/`, `plans/`, `rules/`, `skills/`, `workflows/`, `worktrees/`
  - files: `settings.json`, `settings.local.json`, (`launch.json`)
- Confirmed: agents = his subagents; skills = his skills; settings = settings.json. He asked "they should have subfolders like these?" — YES, this is the desired target shape.
- CLAUDE.md sits NEXT TO .claude/ (not inside), plain-English rules.
- HONESTY CHECK — which folders Claude Code actually uses vs. purely organizational:
  - REAL / auto-used: `settings.json`, `settings.local.json`, `agents/`, `skills/`, `commands/` (not shown), `workflows/` (Workflow tool resolves named workflows here), `launch.json` (preview dev-servers).
  - CUSTOM / organizational only (not auto-loaded unless referenced): `rules/` (only live because CLAUDE.md points to it), `plans/` (plan mode saves to ~/.claude/plans globally), `agent-memory/` (no built-in convention), `worktrees/` (git worktrees location).
- KEY TENSION to resolve: full scaffold everywhere (some folders start empty) vs. only-functional-folders + populate as needed. RESOLVE NEXT.

### Q4 — Full structure vs functional-only; per-project customization
- Joshua: the subfolders are PER-PROJECT. Claude will CUSTOMIZE the contents for each specific project AND/OR organize what's already there into the structure.
- DECISION: full standard structure is the template, but each project's contents are tailored to that project + existing scattered content gets organized into it. (Effectively option A — full structure everywhere — with per-project population, not identical empty clones.)
- SCOPE (implied, confirm): this now applies to ALL projects incl. the 3 apps (briefbar, cluely, hypertrophy), reversing the earlier "only life-path + email-hq" — the whole point is uniform standard across every project.

### Q5 — REVISED structure: bare-bones, NOT all 7 (supersedes Q4)
- Joshua REVERSED the 7-folder idea. Wants BARE-BONES per project, matching the screenshot "What's inside a project's .claude folder":
  - `CLAUDE.md` (sits NEXT TO .claude/)
  - `.claude/settings.json`
  - `.claude/agents/`  (project's own subagents)
  - `.claude/skills/`  (project's own skills)
- That's the whole standard. Drop agent-memory/, plans/, rules/, workflows/, worktrees/ from the per-project template.
- Each project customizes its OWN agents/ and skills/ contents.
- Screenshot footer insight: "Put the same folders in ~/.claude/ and they work in every project" — global-level agents/skills apply everywhere; project-level are project-specific overrides/additions.

## RESOLVED STANDARD (per project)
```
your-project/
├── CLAUDE.md            # plain-English rules, next to .claude/
└── .claude/
    ├── settings.json    # permissions & preferences
    ├── agents/          # this project's subagents
    └── skills/          # this project's skills
```

### Q6 — TWO PARALLEL LEVELS: global vs project (Joshua's core mental model)
- Joshua showed "Global vs Project: where your rules live." THE KEY POINT: there are TWO parallel levels with the SAME folder shape, and a session reads BOTH (project layers on top of global).
- GLOBAL = `~/.claude/` — loads in EVERY project:
  - CLAUDE.md (rules for all work), settings.json (perms & config), commands/ (slash commands), agents/ (subagents), skills/
- PROJECT = `./` + `./.claude/` — loads only in THIS project:
  - CLAUDE.md (rules for this project), settings.json (project config), commands/, agents/, skills/
- "Same folders, two levels. Project layers on top of global." Session reads BOTH.
- This ADDS `commands/` to the per-level standard (Q5 bare-bones screenshot omitted it; this fuller screenshot includes it). Standard item set per level = CLAUDE.md + settings.json + commands/ + agents/ + skills/.

- GROUNDING — what global ~/.claude/ actually has now:
  - CLAUDE.md ✅, settings.json ✅, settings.local.json ✅, skills/ ✅ (83 entries)
  - commands/ — MISSING, agents/ — MISSING
  - So even the GLOBAL level is not yet in the standard shape (no agents/, no commands/).

## RESOLVED STANDARD (per level — applies to BOTH ~/.claude/ and each project's .claude/)
```
<level>/
├── CLAUDE.md            # rules (all-work at global / this-project at project)
└── .claude/  (at global this IS ~/.claude/)
    ├── settings.json    # permissions & config
    ├── commands/        # slash commands
    ├── agents/          # subagents
    └── skills/          # skills
```
Session reads BOTH; project layers on top of global.

### Q7 — Global-vs-project split rule + a SKILLS DATABASE in the brain
- CONFIRMED RULE: a skill/agent goes GLOBAL only if genuinely cross-cutting (want it in ANY project). Otherwise it belongs to the specific project it serves.
  - Global must be HYPER-CONSERVATIVE. Only truly universal skills (graphify, chat-export, defuddle, skill-creator, etc.).
  - Project-specific skills (LSAT/consultation/tutoring) follow DOWN to their project (lsatu, email-hq) and load only if/when that project needs them.
- NEW REQUIREMENT: keep ALL skills in one folder = a "database of skills in my brain." A master library/catalog of every skill Joshua has, living in the brain.
  - This separates AUTHORING/STORAGE (the brain skills database — holds everything) from ACTIVATION (global ~/.claude/skills = hyper-conservative subset; project .claude/skills = per-project subset).
  - Aligns with brain core.md: "skills/ = Authored-once workflow skills; prepared here; runtime activation is a separate transaction."
- So 3 tiers emerging:
  1. BRAIN SKILLS DATABASE (master, all skills) — likely brain/skills/
  2. GLOBAL ACTIVE (~/.claude/skills/) — hyper-conservative universal subset
  3. PROJECT ACTIVE (project/.claude/skills/) — project-specific subset, only if needed

### Q7b — GROUND TRUTH inventory of current skill locations (messy!)
- brain/skills/ = 11 authored skills — ALL project-specific (LSAT/consultation/tutoring/obsidian). Ironically NONE are universal, yet all 11 are currently symlinked into GLOBAL.
- ~/.claude/skills/ = 83 entries. 45 are symlinks. Targets:
  - 21 -> /Users/joshuaf/Documents/Claude/02_PROJECTS/LSATU/.agents/skills  (STALE PATH — old pre-brain LSATU location!)
  - 11 -> /Users/joshuaf/ai-os/skills  (the authored 11)
  -  6 -> /Users/joshuaf/.agents/skills
  -  6 -> ../../.agents/skills
  -  1 -> /Users/joshuaf/Documents/Obsidian Vault/Claude/02_PROJECTS/LSATU/.claude/skills  (STALE — old vault path)
- ~/.agents/skills/ = 59 entries (a SEPARATE Codex-facing skills location).
- Of the 83 global: 72 are NOT Joshua-authored (vendor/plugin/reference/third-party skills).
- RED FLAGS:
  - Global is polluted: 72 non-authored + 11 project-specific = basically everything is global right now (opposite of "hyper-conservative").
  - 22 global symlinks point to STALE pre-migration LSATU paths (~/Documents/Claude/... and ~/Documents/Obsidian Vault/...) that the brain migration was supposed to retire — likely BROKEN or pointing at frozen sources.
  - Skills are scattered across 4+ roots: brain/skills, ~/.claude/skills, ~/.agents/skills, old ~/Documents LSATU paths.
- So "build the standard" is really a CONSOLIDATION + CLEANUP job, not just mkdir.

### Q8 — DATABASE = ALL skills; activation = point-to; per-project CLAUDE.md advertises the DB
- DATABASE holds EVERY skill, every single one, INCLUDING the 72 vendor/plugin ones. One folder = complete catalog of all skills Joshua has.
- The DATABASE does NOT auto-load into every project. It's a library, not an active set.
- Any skill that is POINTED TO (symlinked/activated) — if any pointers target OLD/stale locations, FIX them to point to the right location (the database).
- Joshua wants to be able to IMPORT any skill from the database into a project when useful.
- Each project's CLAUDE.md should POINT TO the database so, while working in a project, he/Claude can browse it and find/add skills that may be good for THAT project.

## RESOLVED ARCHITECTURE (skills)
- ONE master skills DATABASE (all skills, real content, single source of truth). Does not auto-load.
- ACTIVE locations are thin pointers (symlinks) INTO the database:
  - GLOBAL ~/.claude/skills/ — hyper-conservative; only skills wanted in EVERY project.
  - PROJECT <proj>/.claude/skills/ — only skills that project needs; imported on demand.
- Each project's CLAUDE.md references the database path for discovery ("browse here to find/import skills for this project").
- Fix all stale symlinks (the 22 pointing at ~/Documents/... old LSATU paths) to resolve into the database.
- Same pattern applies to AGENTS and COMMANDS presumably (confirm).

### Q9 — Vendor/plugin skills in the DB: Joshua wants A + B COMBINED
- A = every skill present as a LIVE symlink into its real (plugin) location -> current, self-updating, nothing breaks.
- B = frozen real COPY kept -> self-contained, survives plugin removal, but goes stale.
- DECISION: combine both. Interpretation (to confirm): the browsable catalog uses live pointers (A) for plugin skills, AND a parallel frozen snapshot (B) preserves a real copy so nothing is ever lost.
- Proposed concrete shape:
  ```
  brain/skills/                 <- DATABASE (browse here)
  ├── <authored>/               <- real files (source of truth; these ARE Joshua's)
  ├── <plugin-skill> -> symlink to ~/.claude/plugins/.../skill   (A: live/current)
  └── _snapshots/               <- frozen real copies of vendor/plugin skills (B: durable backup, may go stale; git-tracked)
      └── <plugin-skill>/
  ```
- TRADEOFFS to accept: ~2x storage for vendor skills; snapshots need periodic re-sync to stay fresh; snapshots likely git-tracked for durability.

### Q10 — DB confirmed at brain/skills/; add exhaustive discovery, a 1-line index, and auto-capture
- CONFIRMED: master database = brain/skills/ (expand meaning from authored-only to full master DB). A+B shape accepted.
- NEW REQ 1 — EXHAUSTIVE DISCOVERY: search everywhere for skills; find any that are missing so ALL end up in the DB. (Claude to do the search.)
- NEW REQ 2 — 1-LINE INDEX: a simple catalog giving ONE clear line per skill explaining what it does, covering ALL of them. (Likely auto-generated from each SKILL.md's description frontmatter -> INDEX.md.)
- NEW REQ 3 — AUTO-CAPTURE: every time Joshua saves/creates a skill, it must ALSO land in the database automatically. This is the standing enforcement mechanism (hook/convention/skill-creator integration).

## RESOLVED (skills DB)
- Location: brain/skills/ = master database (all skills). Shape: authored=real files, plugin=live symlink + _snapshots/ frozen copy (A+B).
- Deliverables: (1) consolidate ALL skills in; (2) INDEX.md with 1-line-per-skill; (3) auto-capture so new skills always join the DB.

### Q10b — DISCOVERY RESULTS (Claude ran the search)
- ~129 UNIQUE skill names scattered across 7 roots:
  - brain/skills (21 SKILL.md — incl. nested/reference bundles), ~/.claude/skills (38), ~/.agents/skills (48, Codex), ~/.claude/plugins (57, plugin-bundled), ~/.codex/skills (14), lsatu/.claude/skills (48), lsatu/.agents/skills (81).
- Codex-only skills exist that are NOT in ~/.claude/skills (e.g. frontend-design, gws-gmail-read/triage, test-driven-development, session-handoff, high-end-visual-design, minimalist-ui, redesign-existing-projects, design-taste-frontend). So a true master DB must UNION Claude + Codex + plugins to miss nothing.
- Implication: consolidation is sizable (dedup ~129 across 7 roots, classify authored vs plugin vs project, wire A+B, generate index). This is a build, not a quick task — likely its own project/plan after the grill.

### Q11 — SAVE-FLOW and LOAD behavior (confirmed)
- SAVE: whenever Joshua saves a skill, it goes to BOTH (a) the current PROJECT's .claude/skills/ (activated for that project) AND (b) the master DATABASE (brain/skills/). Every time. Two destinations.
- New skills default to PROJECT-scoped + DB-archived — NOT auto-global. Global stays hyper-conservative.
- LOAD: must NOT load every skill in every chat. Only activated skills load (conservative global + current project). The DATABASE never auto-loads.
- This reaffirms the whole design: DB = storage (silent), activation = deliberate + scoped.

## RESOLVED (save + load)
- Save a skill => write to <current-project>/.claude/skills/ AND brain/skills/ (DB). Never global by default.
- Only active (global-conservative + current-project) skills load per session. DB is inert storage.

### Q12 — AGENTS get the same master-database treatment
- Joshua: "this should apply to agents." -> AGENTS get the identical pattern: master DB (brain/agents/), save-to-both (project + DB), conservative global, per-project activation, 1-line index.
- So the master-DB pattern covers SKILLS + AGENTS. (COMMANDS not explicitly confirmed — likely same, treat as sibling; confirm.)
- Build order: skills first (biggest mess), agents next (same blueprint).

## RESOLVED (agents)
- brain/agents/ = master agent database, same A+B + save-to-both + conservative-global + per-project activation as skills.

### Q13 — COMMANDS confirmed
- Joshua: "yes commands as well." -> master-DB pattern covers SKILLS + AGENTS + COMMANDS. Design complete.

### Q14 — Joshua reaffirmed the everyday workflow (matches design)
- Create skill while working -> saves into the PROJECT's skills (active now).
- Search while in a project -> pull from the master DATABASE, LOAD (activate) as needed.
- Global = conservative always-on set.
- Confirms: DB = search/storage; project = activate/work; load = pointer from project into DB entry.
- ONE confirm outstanding: create = save to BOTH project + DB (recommended, so any project can later search it) vs project-only. Leaning BOTH.

### Q15 — FINAL: both-always confirmed; execution delegated
- CONFIRMED: create a skill => save to BOTH the current project AND the master DB. Always.
- CONFIRMED: THIS session (Claude) only AUTHORS the plan. Another model/agent will EXECUTE the phases. PLAN.md must be fully self-contained for a cold handoff.

## Open flags (pending input) — minor, executing model to confirm WITH Joshua
- (design is complete; below are execution-time confirmations only)
- INDEX format: flat list vs grouped (authored/vendor/project)? (default: grouped, auto-generated from description) -> Joshua at plan time
- Assumptions in Summary §5 (Codex feeds from DB / DB git-tracked / creation defaults into DB) offered as defaults — Joshua to confirm or correct at plan time.
- Exact _snapshots/ refresh cadence for vendor skills (manual vs a job) -> plan time.
- Scope: confirm ALL 7 projects get the CLAUDE.md + .claude(settings/agents/skills/commands) standard -> Joshua
- ~/.agents/skills (Codex) + lsatu .agents/skills — does Codex side feed from same DB / stay mirrored? -> Joshua
- This is a BUILD -> after grill, produce a plan (its own project) before executing. -> Joshua
- PLUGIN-SKILL TENSION: many of the 72 are provided by installed PLUGINS (netlify-skills, commit-commands, pdf-viewer, desktop-commander, design, anthropic-skills) and physically live under ~/.claude/plugins/, managed/updated by the plugin system. Physically moving them into one folder could break plugin updates. Options: (a) copy them in as a frozen catalog snapshot, (b) symlink the DB entry -> plugin location (DB points to them, not vice versa), (c) only consolidate free-standing skills + LIST plugin ones. -> Joshua (real decision)
- Reconcile ~/.agents/skills (Codex, 59) vs ~/.claude/skills (Claude): does the DB feed BOTH? keep Codex mirror? -> Joshua
- Does DATABASE get git-tracked in brain (so it's backed up/versioned)? -> Joshua
- Activation mechanism: how does a skill get from DATABASE -> global/project active? copy? symlink? (brain had a Phase-8 "runtime activation" transaction — reuse it?) -> Joshua
- Confirm scope = ALL 7 projects incl. apps? -> Joshua
- Bring GLOBAL ~/.claude/ into standard shape (add agents/, commands/)? -> Joshua
- Enforcement: auto-scaffolder tooling vs prose -> Joshua
- Same database concept for AGENTS and COMMANDS too, or just skills? -> Joshua
