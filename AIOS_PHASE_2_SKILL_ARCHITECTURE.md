# AIOS Phase 2: Skill Architecture and Discovery Design Report

**Document Role:** Skill Ecosystem Forensic Analysis & Architecture Design  
**Execution Constraints:** ANALYSIS AND DESIGN ONLY (Zero file modifications, zero skill moves, zero config edits)  
**Target Audience:** External Systems Architect / Senior AI Engineer  
**Timestamp:** 2026-09-20T02:25:00-04:00  
**Host Machine:** `J` (Windows 11 Home, Build 26100)  
**Workspace Root:** `C:\Users\Joshu\dev\ai-os`  

---

## 1. CURRENT SKILL POPULATION

A machine-wide census of all skills containing a valid `SKILL.md` file across all registered locations:

### 1.1 Skill Distribution by Physical Root
- **`.gemini/skills` (`C:\Users\Joshu\dev\ai-os\.gemini\skills`):** **274 skills**
  - Active Canonical (top-level): 213
  - Vendor Snapshots (`_snapshots/`): 37
  - Archival Inactive (`_inactive/`): 13
  - Subproject Forks (`_project-forks/lsatu/`): 9
  - Example Templates: 2 (`example-command`, `example-skill`)
- **`plugin_skills` (`C:\Users\Joshu\.gemini\config\plugins`):** **46 skills**
- **`global_config_skills` (`C:\Users\Joshu\.gemini\config\skills`):** **33 skills**
- **`.agents/skills` (`C:\Users\Joshu\dev\ai-os\.agents\skills`):** **11 skills**
- **`builtin_skills` (`C:\Users\Joshu\.gemini\antigravity\builtin\skills`):** **5 skills**
- **Total Installed Skill Directories:** **369 skill directories**
- **Total Unique Skill Identifiers:** **322 unique IDs**
- **Broken / Malformed Skills:** **0** (All 369 directories contain valid `SKILL.md` files).

### 1.2 Population Breakdown by Structural Category

| Category | Total Count | Definition / Role |
|---|---|---|
| **ACTIVE CANONICAL** | 308 | Production skills intended for regular task invocation |
| **SNAPSHOT** | 37 | Frozen vendor/upstream copies kept in `_snapshots/` for parity/reference |
| **ARCHIVAL** | 13 | Deprecated skills moved to `_inactive/` (YouTube/transcript suite) |
| **PROJECT FORK** | 9 | Subproject-specific customizations stored in `_project-forks/lsatu/` |
| **EXAMPLE** | 2 | Scaffolding templates (`example-command`, `example-skill`) |
| **BROKEN / MALFORMED** | 0 | Directories missing SKILL.md or containing parse errors |

---

## 2. CURRENT ANTIGRAVITY-NATIVE PATHS

Based on official Antigravity 2.0 system documentation (verified in `C:\Users\Joshu\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md`):

### 2.1 Official Specification Classification

| Path / Config | Classification | Official Documentation Role & Precedence |
|---|---|---|
| `<workspace>/.agents/skills` | **CURRENT NATIVE** | Standard project-level customization path. Traversed automatically from CWD up to repository root. Shared VCS path. Priority: 1. |
| `~/.gemini/config/skills` | **CURRENT NATIVE** | Standard machine-local global skill path. Applies to all workspaces on host. Priority: 3. |
| `<workspace>/.gemini/skills` | **MANUAL BRIDGE / LEGACY** | Not an auto-discovered native path in Antigravity 2.0. Discovered only because it is explicitly declared in `skills.json`. |
| `~/.gemini/config/skills.json` | **MANUAL BRIDGE** | Global declared configuration file. Used to mount non-standard directories into the skill loader. Priority: 5. |
| `~/.gemini/config/plugins/` | **PLUGIN MANAGED** | Bundled extensions containing skills, rules, and MCP configurations. Auto-mounted by plugin manager. |
| Built-in Antigravity Skills | **CURRENT NATIVE** | Core application skills (`agy-customizations`, `generative_ui`). Mounted directly by application config. Priority: 4. |

### 2.2 Critical Architectural Correction on `.agents/`
- Official Antigravity 2.0 documentation explicitly establishes `<workspace>/.agents/` as the canonical project customization directory for skills (`.agents/skills/`), rules (`.agents/rules/`), and custom agents (`.agents/agents/`).
- Therefore, Antigravity ingesting `.agents/skills` is **native, expected Antigravity 2.0 behavior**, not an accidental leak from Codex.
- The actual problem in this environment is that `skills.json` explicitly lists both `.agents/skills` AND `.gemini/skills`, leading to duplicate indexing of overlapping skill suites.

---

## 3. EXACT DISCOVERY FAILURE

In the active Antigravity session, exactly **85 skills are exposed** in the prompt context, while **98 skills are suppressed** due to context token budget limits.

### 3.1 Provenance of Exposed Skills
- From `.gemini/skills/` (canonical): 56 skills
- From `.gemini/skills/_snapshots/`: 10 skills (Wasted slots!)
- From `.gemini/skills/_project-forks/`: 4 skills (`emil-design-eng`, `notebooklm`, `pickup`, `subagent-driven-development`)
- From `.gemini/skills/_inactive/`: 1 skill (`session-handoff-nate-active-copy` - Wasted slot!)
- From `.agents/skills/`: 7 skills (`domain-modeling`, `grill-with-docs`, `gws-gmail`, `gws-gmail-read`, `gws-gmail-triage`, `gws-shared`, `superwhisper`)
- From Global Config (`~/.gemini/config/skills/`): 7 skills
- From Built-in / Plugins: 5 skills

### 3.2 Root Cause of Discovery Inversion
1. **No Directory Filtering:** Antigravity traverses `.gemini/skills` recursively without ignoring underscore-prefixed directories (`_snapshots`, `_inactive`).
2. **Slot Pollution:** Snapshot, example, and archival skills consume at least **13 precious active slots** in the prompt context.
3. **High-Value Skills Suppressed:** Because the discovery loader fills its budget before reaching later alphabetical or structural entries, critical capabilities are pushed out of prompt visibility:
   - `lsat-u-architecture` (SUPPRESSED)
   - `impeccable` (SUPPRESSED)
   - `code-review` (SUPPRESSED)
   - `bootcamp-builder` (SUPPRESSED)
   - `prompt-architect-refiner` (SUPPRESSED)
   - `second-brain` utilities (Partially suppressed)
   - Meanwhile, dummy/example skills like `example-command`, `example-skill`, and archived `session-handoff-nate` occupy active slots.

---

## 4. DUPLICATE IDENTIFIER ANALYSIS

Forensic scan identified **43 duplicate skill identifiers** across visible sources. Key duplicates analyzed:

| Identifier | Discovered Paths | Status | Exposed Copy | Precedence / Routing Risk |
|---|---|---|---|---|
| `chrome-devtools` | `.gemini/skills/chrome-devtools` vs `_snapshots/chrome-devtools` | **IDENTICAL** | `_snapshots` copy exposed | Unnecessary duplicate parsing |
| `a11y-debugging` | `.gemini/skills/a11y-debugging` vs `_snapshots/a11y-debugging` | **IDENTICAL** | `_snapshots` copy exposed | Unnecessary duplicate parsing |
| `grill-with-docs` | `.gemini/skills/...` (2,003 B) vs `.agents/skills/...` (2,040 B) | **DIVERGENT** | `.agents` copy exposed | Nondeterministic prompt routing |
| `subagent-driven-development` | `.gemini/skills/...` (21.6 KB) vs `_project-forks/...` (12.1 KB) | **DIVERGENT** | `_project-forks` copy exposed | Fork overrides root with 40% less guidance |
| `pickup` | `.gemini/skills/...` (3,412 B) vs `_project-forks/...` (1,940 B) | **DIVERGENT** | `_project-forks` copy exposed | Subproject fork overrides root skill |
| `superwhisper` | `.gemini/skills/...` (4,116 B) vs `.agents/skills/...` (4,103 B) | **DIVERGENT** | `.agents` copy exposed | Divergent configuration instructions |
| `imessage-access` | `.gemini/skills/...` vs `_snapshots/...` | **DIVERGENT** | Canonical exposed | Stale snapshot remains in discovery tree |
| `imessage-configure` | `.gemini/skills/...` vs `_snapshots/...` | **DIVERGENT** | Canonical exposed | Stale snapshot remains in discovery tree |
| `troubleshooting` | `.gemini/skills/` vs `_snapshots/` vs `plugin_skills/` (3 copies!) | **DIVERGENT** | `_snapshots` copy exposed | Three competing copies in runtime! |

---

## 5. SEMANTIC OVERLAP CLUSTERS

Forensic grouping and relationship analysis of overlapping skill capabilities:

### Cluster A: Frontend & Design Engineering
- **Members:** `impeccable`, `frontend-design`, `design-taste-frontend`, `high-end-visual-design`, `redesign-existing-projects`, `emil-design-eng`, `minimalist-ui`.
- **Relationship:** **REDUNDANT & SPECIALIZED.**
- **Analysis:** High fragmentation. `frontend-design`, `design-taste-frontend`, and `high-end-visual-design` give overlapping advice on typography, card borders, and palette selection. `emil-design-eng` is specialized for subtle micro-interactions and transitions. `impeccable` is an elite design auditor but is currently suppressed.

### Cluster B: Debugging & Troubleshooting
- **Members:** `systematic-debugging`, `diagnosing-bugs`, `troubleshooting`, `a11y-debugging`, `debug-optimize-lcp`, `memory-leak-debugging`.
- **Relationship:** **ROUTER + SPECIALISTS.**
- **Analysis:** `systematic-debugging` and `diagnosing-bugs` compete directly for general bug investigation (redundant). `a11y-debugging`, `debug-optimize-lcp`, and `memory-leak-debugging` are highly specialized diagnostic tools that belong under an umbrella router.

### Cluster C: Testing & TDD
- **Members:** `tdd`, `test-driven-development`, `webapp-testing`, `verification-before-completion`.
- **Relationship:** **REDUNDANT + GATE.**
- **Analysis:** `tdd` (3.5 KB) and `test-driven-development` (9.8 KB) are 100% redundant implementations of the same methodology. `verification-before-completion` is a mandatory post-work gate.

### Cluster D: Code Review
- **Members:** `code-review`, `review`, `requesting-code-review`, `receiving-code-review`, `codex-review`.
- **Relationship:** **SUPERSEDED & REDUNDANT.**
- **Analysis:** `code-review` and `review` duplicate the same generic review checklist. `requesting-code-review` and `receiving-code-review` represent specialized procedural phases.

### Cluster E: Implementation & Planning
- **Members:** `implement`, `implement-spec`, `executing-plans`, `writing-plans`, `subagent-driven-development`, `brainstorming`.
- **Relationship:** **WORKFLOW PIPELINE.**
- **Analysis:** `brainstorming` (exploration) -> `writing-plans` (specification) -> `executing-plans` / `subagent-driven-development` (execution). However, `implement` and `implement-spec` duplicate parts of this pipeline.

### Cluster F: Handoff & Session Transition
- **Members:** `handoff`, `session-handoff`, `claude-handoff`, `chat-export`, `resume`, `wrapup`, `pickup`.
- **Relationship:** **SPECIALIZED & REDUNDANT.**
- **Analysis:** `session-handoff` is the primary cross-agent handoff. `wrapup` and `pickup` are LSAT U vault-specific lifecycle hooks. `session-handoff-nate` in `_inactive` is dead baggage.

### Cluster G: Skill Authoring
- **Members:** `skill-creator`, `skill-development`, `writing-skills`, `writing-great-skills`, `skill-lint`, `skill-doctor`, `skill-repair`.
- **Relationship:** **HEAVILY REDUNDANT.**
- **Analysis:** 7 skills exist solely to create, lint, and repair skills! `writing-skills` (26 KB) and `skill-creator` (33 KB) duplicate the same guidelines. `skill-repair` in global config handles manifest patching.

### Cluster H: Research
- **Members:** `research`, `research-add-items`, `research-deep`, `research-report`, `web-researcher`.
- **Relationship:** **ROUTER + LEAF.**
- **Analysis:** `research-deep` and `research-report` are subroutines of a multi-stage research agent. Exposing them as individual top-level skills wastes discovery slots.

### Cluster I: Browser Automation
- **Members:** `chrome-devtools`, `lsat-u-browser-verification`, `webapp-testing`, `edge-live-control`, `auto-auth-browser`, `troubleshooting`.
- **Relationship:** **SPECIALIZED.**
- **Analysis:** `lsat-u-browser-verification` is tailored specifically for the persistent Chrome instance on port 9223. `edge-live-control` targets Edge. `webapp-testing` provides generic Playwright helpers.

### Cluster J: MCP Creation
- **Members:** `mcp-builder`, `build-mcp-server`, `build-mcp-app`, `build-mcpb`, `mcp-integration`.
- **Relationship:** **HEAVILY REDUNDANT.**
- **Analysis:** 5 separate skills for building MCP servers, 4 of which are duplicated in `_snapshots/`.

### Cluster K: LSAT U Bootcamp
- **Members:** `bootcamp-builder`, `lsat-u-topic-builder`, `bootcamp-parity-audit`.
- **Relationship:** **COMPLEMENTARY.**
- **Analysis:** Domain-specific curriculum tools for LSAT U. All 3 are currently suppressed by discovery limit.

---

## 6. LARGE SUITES THAT SHOULD BE ROUTED

Large capability families currently exposed as individual leaf skills, severely bloating the discovery budget:

| Suite / Family | Leaf Skill Count | Approx Discovery Tokens | Usage Frequency | Recommended Routing Model |
|---|---|---|---|---|
| **Google Workspace (`gws-*`)** | 30 leaf skills | ~1,850 tok | Occasionally used | **Single Router (`gws-workspace`)**: Dispatches to Gmail, Drive, Calendar, Docs on demand |
| **Netlify Suite** | 12 leaf skills | ~950 tok | NEVER used (app is on Lovable Cloud) | **Archive / Project-specific**: Remove from root discovery |
| **Google Cloud / BigQuery** | 16 leaf skills | ~1,400 tok | NEVER used in standard app dev | **Global On-Demand Plugin**: Load only when explicit GCP task invoked |
| **YouTube & Transcripts** | 13 leaf skills | ~800 tok | Rarely used | **Single Router (`media-transcribe`)**: Dispatches to yt-dlp/whisper |
| **Document Formats (pdf, docx, etc.)** | 4 leaf skills | ~250 tok | Occasionally used | **Single Document Router (`doc-tools`)** |
| **Obsidian Suite** | 4 leaf skills | ~320 tok | Frequently used | **Single Vault Router (`obsidian`)** |

---

## 7. WORKSPACE VS GLOBAL VS PROJECT SCOPE

Conceptual scope allocation for all 322 unique installed skills:

| Conceptual Scope | Skill Count | Scope Criteria / Examples |
|---|---|---|
| **AI-OS WORKSPACE** | ~65 skills | EA operations, student ops, wiki/second-brain, executive drafting, general research |
| **LSAT U PROJECT** | ~28 skills | Browser verification port 9223, bootcamp builders, homework tools, design engine |
| **GLOBAL MACHINE** | ~20 skills | Core agent SDK, CLI utilities, general coding gates (`verification-before-completion`) |
| **EXPLICIT / MANUAL ONLY** | ~45 skills | Heavy suites (GCP Airflow, BigQuery, Netlify, Kling CLI) invoked only on demand |
| **ARCHIVE / SUPERSEDED** | ~85 skills | Snapshots (37), inactive YouTube skills (13), duplicate TDD/review skills (~35) |
| **UNKNOWN / PENDING REVIEW** | ~79 skills | Miscellaneous niche skills pending external architect evaluation |

---

## 8. SHARED VS VENDOR-SPECIFIC

Skill portability classification:
- **PORTABLE (Shared across Gemini, Claude, Codex):** **~75% of active skills.** Skills describing methodology, testing protocols, prompt design, and domain concepts (e.g. `systematic-debugging`, `frontend-design`, `writing-plans`, `domain-modeling`) are 100% portable Markdown instructions.
- **ANTIGRAVITY-SPECIFIC:** Skills referencing native Antigravity tools (`run_command`, `manage_task`, `call_mcp_tool`, `schedule`), such as `lsat-u-browser-verification`, `agy-customizations`, and `google-antigravity-sdk`.
- **CLAUDE-SPECIFIC:** Skills referencing Claude Code CLI slash-commands or hooks (`git-guardrails-claude-code`, `claude-handoff`).
- **CODEX-SPECIFIC:** Skills configured with OpenAI schema bindings or `codex-review`.
- **PROJECT-SPECIFIC:** Skills tightly coupled to `projects/lsatu` database schemas and routing.

---

## 9. MANDATORY TRIGGER COLLISIONS

### Aggressive Trigger Phrases in Active Skills
Multiple installed skills contain absolute imperative triggers (`MUST`, `ALWAYS`, `BEFORE ANY`, `BEFORE IMPLEMENTATION`, `EVERY RESPONSE`):
- `using-superpowers`: *'requiring skill invocation before ANY response including clarifying questions'*
- `brainstorming`: *'You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior.'*
- `systematic-debugging`: *'Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes'*
- `test-driven-development`: *'Use when implementing any feature or bugfix, before writing implementation code'*
- `verification-before-completion`: *'Use when about to claim work is complete, fixed, or passing, before committing or creating PRs'*

### Stacking Collision Walkthrough
Consider a routine user request: *'Fix the alignment of the drill options in `ClassroomDrill.tsx`'*:
1. `using-superpowers` intercepts the request before any reply can be formulated.
2. `systematic-debugging` activates because an alignment issue is reported as a bug.
3. `brainstorming` activates because modifying UI behavior is classified as component work.
4. `test-driven-development` activates because bug fixing mandates writing tests first.
5. `verification-before-completion` activates before the result can be acknowledged.
- **Result:** **5 mandatory skills collide on a 1-line CSS adjustment**, causing prompt thrashing, contradictory instructions, and extreme token wastage.

---

## 10. REAL USAGE VS INSTALLED CAPABILITY

Cross-referencing installed skills against empirical execution logs across 30 recent Antigravity sessions (1,845 tool calls):

### Usage Classification Table

| Category | Skills Included | Observed Activity in Transcripts |
|---|---|---|
| **FREQUENTLY USED** | Browser verification, implementation plans, file inspection, web search | Constantly invoked via native tools and prompt keywords (`verify`, `plan`) |
| **OCCASIONALLY USED** | Debugging, research, student correspondence, audit | Invoked intermittently on dedicated workflows |
| **RARELY USED** | Second brain linting, prompt architect, math olympiad | Infrequent single-session use |
| **NEVER OBSERVED** | Netlify suite (12 skills), Google Cloud Airflow/Spark (16 skills), Discord/iMessage (4 skills) | **Zero invocations** across entire session history |

### Key Inefficiencies Identified
1. **High-Value Suppressed:** `lsat-u-architecture`, `code-review`, `bootcamp-builder` are actively needed in app development but pushed out of context.
2. **Deadweight Exposed:** Netlify, example templates, and snapshot duplicates occupy slots despite having zero relevance to current projects.

---

## 11. LSAT U IDEAL SKILL SURFACE

Proposed discoverable skill surface for an Antigravity session operating inside `projects\lsatu`:

### Immediate Discoverable Set (Capped at 10 Core Skills)
1. **`lsat-u-browser-verification`** (Port 9223 persistent Chrome, CDP screenshots, DOM inspection)
2. **`lsat-u-architecture`** (Supabase Edge Functions, database schema, app seam definitions)
3. **`systematic-debugging`** (Consolidated single debugging runbook)
4. **`frontend-design`** (Polished UI/UX design standards, shadcn components)
5. **`verification-before-completion`** (Visual evidence hard gate before git commit)
6. **`executing-plans`** (Structured implementation execution)
7. **`test-driven-development`** (Unit & integration test-first workflow)
8. **`code-review`** (Pre-commit code quality checklist)
9. **`bootcamp-builder`** (Curriculum drill generator)
10. **`pull-submissions`** (Student homework sync)

### On-Demand / Routed Capabilities
- Deep design polish (`emil-design-eng`, `high-end-visual-design`) routed on demand.
- Curriculum parity audit (`bootcamp-parity-audit`) routed on demand.
- Supabase SQL migrations routed via architecture skill.

---

## 12. AI-OS ROOT IDEAL SKILL SURFACE

Proposed discoverable skill surface for general EA command-center sessions at `dev\ai-os`:

### Immediate Discoverable Set (Capped at 8 Core Skills)
1. **`gws-workspace` (Router)** (Unified Google Workspace access: Gmail, Calendar, Drive, Docs)
2. **`consultation-inquiry-drafts`** (Personalized prospect inquiry response drafting)
3. **`consultation-followup-drafts`** (Post-consultation follow-up drafting)
4. **`second-brain`** (LLM-Wiki ingest, query, and ledger maintenance)
5. **`research`** (Source-backed investigations with Firecrawl/web integration)
6. **`prompt-architect-refiner`** (Iterative prompt engineering for external models)
7. **`tutorocean-profile-fill`** (Tutor platform profile maintenance)
8. **`session-handoff`** (Clean session state migration across agents)

---

## 13. LARGE CAPABILITY LIBRARY DESIGN

Evaluation of 3 architectural options for managing the 300+ capability library without context bloat:

### Option A: Curated Active Core + Dormant Catalog
- **Mechanism:** Only ~20 active skills reside in discoverable directories. The remaining ~300 skills live in an indexed inert catalog (`skills/catalog/`). Users or agents activate skills on demand by copying/symlinking into active roots.
- **Token Cost:** Ultra-low (~1,500 tokens).
- **Reliability:** High; completely eliminates discovery budget truncation.
- **Drawback:** Requires manual activation step before niche skills can be used.

### Option B: Hierarchical Front-Door Routers (Recommended)
- **Mechanism:** Large suites (Google Workspace, Netlify, GCP, Document Tools, Design) are represented by a single high-level router skill that presents high-level options. When a domain is selected, the router dynamically reads the specific leaf SKILL.md.
- **Token Cost:** Low-Medium (~2,500 tokens).
- **Reliability:** Very High; model sees broad categories without drowning in 30 individual Gmail leaf descriptions.
- **Drawback:** Requires authoring ~5 router skills.

### Option C: Project-Scoped Skill Manifests
- **Mechanism:** Scopes skills strictly to Antigravity Project definitions. An LSAT U project sees only LSAT U skills; an EA root project sees only EA skills.
- **Token Cost:** Low (~1,800 tokens per project context).
- **Reliability:** High; zero cross-contamination.
- **Drawback:** Cross-project work requires switching active Antigravity project contexts.

---

## 14. TARGET METRICS

Proposed measurable acceptance metrics for the target architecture:

| Metric | Current Live State | Proposed Target Range | Improvement Target |
|---|---|---|---|
| **Immediately Exposed Skills (Root)** | 85 (budget capped) | **10 to 15 skills** | 80% reduction in discovery bloat |
| **Immediately Exposed Skills (LSAT U)** | 85 (budget capped) | **8 to 12 skills** | Scoped exclusively to app engineering |
| **Suppressed Skills Count** | 98 suppressed | **0 suppressed** | 100% of declared active skills visible |
| **Discovery Token Overhead** | ~7,500 tokens | **~1,200 to ~1,800 tokens** | Liberates ~5,500 tokens per turn |
| **Duplicate Skill Identifiers** | 43 duplicates | **0 duplicates** | Completely eliminates routing ambiguity |
| **Snapshot / Archive Skills in Context** | 13 wasted slots | **0 wasted slots** | Non-canonical skills quarantined |

---

## 15. MIGRATION DEPENDENCIES

Items that MUST be confirmed prior to executing skill migration:
1. **Confirmation of `.agents/skills` as Canonical Workspace Path:** Verify that Antigravity 2.0 fully supports checking `.agents/skills` into Git as the primary portable skill home.
2. **`skills.json` Deprecation Plan:** Determine whether `~/.gemini/config/skills.json` can be safely cleared of hardcoded workspace paths once native paths are utilized.
3. **Quarantine Strategy for `_snapshots/` and `_inactive/`:** Because Antigravity recursively parses subdirectories, snapshots and archived skills must be moved completely OUT of any registered skill root into a dormant catalog directory (e.g. `raw/skill-catalog/` or `archive/skills/`).
4. **LSAT U Dedicated Project Boundary:** Confirm whether LSAT U will be registered as an independent Antigravity project or continue operating under unified `ai-os`.

---

## 16. QUESTIONS FOR EXTERNAL ARCHITECT / USER

Key strategic decisions requiring architect/user input:
1. **Catalog Model Preference:** Do you prefer **Option B (Front-Door Routers)** for large suites like Google Workspace and GCP, or **Option A (Inert Catalog + Manual Activation)**?
2. **Consolidation of Redundant Clusters:** Do you authorize merging the 7 skill-authoring skills into a single `skill-engineering` skill, and merging the 5 code review skills into a single `code-review` workflow?
3. **Disposal of Stale Suites:** Can the 12 Netlify skills and 13 archived YouTube skills be moved to a dormant archive folder outside the active discovery path?
4. **Mandatory Trigger De-escalation:** Do you approve softening aggressive triggers (`MUST use this before any work`) to context-aware activation to eliminate the 5-skill trigger collision?

