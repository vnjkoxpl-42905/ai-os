# AIOS Phase 4: Project Topology, Context Isolation, Knowledge, and Memory Architecture

Date: September 20, 2026
Environment: Windows 11 (Host J)
Repository: C:\Users\Joshu\dev\ai-os
Authority: Live Antigravity 2.15.0 / Antigravity IDE 2.5.5 Runtime Evidence

---

## Executive Summary

This report establishes the architectural analysis and design for project topology, context isolation, knowledge systems, and memory boundaries across Joshua's AI-OS command center and the LSAT U engineering environment.

The current system unifies 36 distinct top-level directories and 51 historical agent conversations under a single monolithic Antigravity project (`1e181e2e-860b-48c6-9209-540e3e7a1965`). This topology causes substantial cross-domain context bleeding: full-stack React and Vite engineering sessions eagerly inherit tutoring correspondence directives, student operational protocols, and executive assistant workflows. Conversely, student drafting sessions inherit UI design rules and TypeScript compilation constraints.

The objective of this design is not theoretical maximum isolation, but practical domain optimization: minimizing eager context overhead, eliminating instruction interference, and respecting Git repository boundaries while ensuring Joshua experiences minimal project-switching friction.

---

## 1. Current AI-OS Topology

Analysis of `C:\Users\Joshu\dev\ai-os` reveals 36 top-level directories spanning multiple functional responsibilities. Below is the structural inventory of context-relevant directories:

| Directory | Primary Purpose | Owner / Runtime | Git Tracked (Outer) | Root Instruction Reference | Live Operational State | Needed for LSAT U Eng | Needed for Ops / Students | Needed for Research | Machine / OS Infra |
|---|---|---|---|---|---|---|---|---|---|
| `.agents/` | Active Antigravity workspace skills & rules | Antigravity 2.0 | Yes (28 files) | Yes | Yes (active skills) | Yes | Yes | Yes | Yes |
| `.claude/` | Claude Code runtime skills & project config | Claude Code | Yes (15 files) | Yes | Yes | No | No | No | Yes |
| `.codex/` | OpenAI Codex legacy workspace & agent TOMLs | OpenAI Codex | Yes (17 files) | Yes | Legacy / Inactive | No | No | No | Yes |
| `.gemini/` | Dedicated Gemini runtime, active skills, outputs | Antigravity / Gemini | Yes (1,217 files) | Yes | Yes | Yes | Yes | Yes | Yes |
| `.obsidian/` | Obsidian vault configuration & workspace state | Obsidian | Yes (3 files) | Yes | Yes | No | Yes | Yes | Yes |
| `Clippings/` | Web-clipped articles from Obsidian clipper | Obsidian / User | Yes (2 files) | Yes (via raw) | Intake state | No | No | Yes | No |
| `Loophole Lecture/` | Transcripts & teleprompter scripts for LSAT | LSAT U Content | Yes (9 files) | Yes (via corpus) | Static content | Conditionally | No | Yes | No |
| `agents/` | Inert catalog of legacy TOML agent configs | Multi-runtime | Yes (56 files) | Yes (catalog) | Static catalog | No | No | No | Yes |
| `aios/` | Retired reform folder (superseded by brainstorms) | Historical | Yes (3 files) | Yes (marked retired) | Archived | No | No | No | No |
| `archive/` | Deprecated and preserved historical assets | User / Assistant | Yes (61 files) | No | Static archive | No | No | No | No |
| `audits/` | Structural health and migration reports | Assistant | No (untracked) | Yes (via /audit) | Point-in-time | No | No | Yes | Yes |
| `brainstorms/` | Design, interview, and planning records | Multi-runtime | Yes (28 files) | Yes | Active thinking | Yes | Yes | Yes | No |
| `context/` | Identity, business model, 90-day priorities | Joshua / EA | Yes (3 files) | Yes | Authoritative | Conditionally | Yes | Yes | No |
| `corpus/` | Pedagogical authority and LSAT curriculum | LSAT U Pedagogy | Yes (122 files) | Yes | Primary knowledge | Conditionally | Yes | Yes | No |
| `decisions/` | Locked architectural & business decisions | System / EA | Yes (1 file) | Yes | Authoritative ledger | Yes | Yes | Yes | No |
| `email system/` | Email templates and routing scripts | EA / Operations | Yes (8 files) | Yes (via skills) | Working scripts | No | Yes | No | No |
| `graph-imports/` | Knowledge graph data and visual exports | Graphify / Vault | Yes (3,841 files) | Yes (via skills) | Generated data | No | No | Yes | No |
| `handoffs/` | Inter-session continuity records | Multi-runtime | Yes (29 files) | Yes | Operational logs | Yes | Yes | Yes | No |
| `peek/` | Temporary inspection dumps and previews | Scratch | Yes (7 files) | No | Ephemeral | No | No | No | No |
| `projects/` | Nested development repositories (`projects/lsatu`) | Engineering | No (nested git root) | Yes | Active codebase | Yes | No | No | No |
| `raw/` | Immutable intake, clips, personal data | Intake Queue | No (git-ignored) | Yes | Immutable evidence | No | No | Yes | No |
| `references/` | Technical methods, frameworks, firecrawl docs | Reference Library | Yes (11 files) | Yes | Static methods | Yes | Yes | Yes | Yes |
| `research/` | External technology & market teardowns | Research Agent | Yes (6 files) | Yes | Static reports | Conditionally | No | Yes | No |
| `scratch/` | Investigative scripts and temporary audits | Assistant | Yes (35 files) | No | Ephemeral code | No | No | No | Yes |
| `setup/` | Machine and environment bootstrap configs | OS Admin | Yes (10 files) | No | Setup scripts | No | No | No | Yes |
| `skills/` | Inert central skill catalog (all runtimes) | Multi-runtime | Yes (3,514 files) | Yes | Catalog store | Yes | Yes | Yes | Yes |
| `students/` | Profiles, transcripts, homework, correspondence | Tutoring Ops | Yes (343 files) | Yes | Operational data | Conditionally | Yes | No | No |
| `superwhisper/` | Voice dictation modes and replacement rules | OS Tooling | Yes (44 files) | Yes | Local config | No | No | No | Yes |
| `system/` | Shell scripts, browser launch, validation tools | OS Admin | Yes (58 files) | Yes | Machine infra | Yes | Yes | No | Yes |
| `wiki/` | Second brain ledgers, hot cache, logs, voice | Obsidian / EA | Yes (35 files) | Yes | Authoritative brain | Conditionally | Yes | Yes | No |

---

## 2. Domain Classification

Every directory in `ai-os` maps into one of eight distinct functional domains:

### Domain A: LSAT U Engineering
- Core Focus: Software application development, React UI components, Supabase edge functions, frontend testing, browser verification.
- Directories: `projects/lsatu/`, `.gemini/skills/lsat-u-browser-verification/`, `system/scripts/launch_lsatu_browser.py`.

### Domain B: LSAT U Curriculum and Pedagogy
- Core Focus: Conceptual drill designs, LSAT question explanations, method taxonomies, teaching rules.
- Directories: `corpus/`, `Loophole Lecture/`.

### Domain C: Student Operations
- Core Focus: Private tutoring student dossiers, lesson transcripts, booking uploads, drill assignments, progress tracking.
- Directories: `students/`.

### Domain D: Business and Executive Assistant
- Core Focus: Founder identity, financial models, offer tiers, partner channels, consultation drafts, email handling, send ledgers.
- Directories: `context/`, `email system/`, `wiki/send-ledger.md`, `wiki/tasks.md`.

### Domain E: Research and Knowledge
- Core Focus: External technology teardowns, market intelligence, web clipping, second-brain concept synthesis, knowledge graphs.
- Directories: `research/`, `raw/`, `Clippings/`, `graph-imports/`, `.gemini/wiki/`, `distillates/`.

### Domain F: Machine and AIOS Administration
- Core Focus: Multi-agent runtime configuration, skill catalog maintenance, MCP wiring, Superwhisper dictation, Windows automation scripts, git hygiene.
- Directories: `.agents/`, `.claude/`, `.codex/`, `.gemini/`, `agents/`, `skills/`, `system/`, `setup/`, `superwhisper/`, `scratch/`.

### Domain G: Shared Cross-Domain Systems
- Core Focus: Operational ledgers that bridge multiple domains.
- Directories: `decisions/` (records both engineering and business choices), `brainstorms/` (contains engineering RFCs and business interviews), `handoffs/` (bridges session state across all domains), `wiki/` (houses the central master index `wiki/index.md` and hot cache `wiki/hot.md`).

### Domain H: Archive and Historical
- Core Focus: Dormant and superseded records.
- Directories: `archive/`, `aios/`, `peek/`, `tmp/`.

### Directories Currently Mixing Multiple Domains
1. `wiki/`: Houses student operation tracking (`tasks.md`, `hot.md`), founder voice (`teaching-voice.md`), and platform technical pointers (`dashboard.md`).
2. `brainstorms/`: Contains product architecture RFCs alongside private business strategy notes.
3. `context/`: Mixes Joshua's personal working preferences with business pricing models.
4. `.gemini/`: Mixes active engineering skills with Google Workspace operations skills and broad research outputs.

---

## 3. Current Project Context Behavior

Investigation of the running Antigravity 2.15.0 runtime reveals how single-project registration currently behaves:

| Behavior Dimension | Observed Runtime Mechanism | Certainty Level |
|---|---|---|
| Automatic Directory Access | All 36 top-level directories in `C:\Users\Joshu\dev\ai-os` are mounted into the agent workspace and visible to file search tools (`find_by_name`, `list_dir`, `grep_search`). | VERIFIED |
| Root Instruction Loading | The root `GEMINI.md` (or `AGENTS.md` / `CLAUDE.md`) is loaded into every session prompt regardless of whether the session is coding React or drafting student emails. | VERIFIED |
| Skill Discovery Scope | All skills located in `<workspace-root>/.agents/skills/`, `.gemini/skills/`, and `~/.gemini/config/skills/` are scanned and presented in the prompt metadata (217 installed, 85 exposed, 98 suppressed). | VERIFIED |
| Conversation History Scope | All 51 stored conversations are indexed under `project_id = 1e181e2e-860b-48c6-9209-540e3e7a1965` in `conversation_summaries.db`. They populate the sidebar but are NOT automatically injected into turn prompts. | VERIFIED |
| File Search Scope | Tools like `find_by_name` search from `C:\Users\Joshu\dev\ai-os` downwards by default. A search for `Button.tsx` traverses unrelated student, archive, and research trees unless explicitly bounded. | VERIFIED |
| MCP Server Availability | MCP servers declared in `~/.gemini/antigravity/mcp/` or extension schemas are mounted globally for the session and exposed to all conversations in this project. | VERIFIED |
| Tool Permissions | Tool execution grants stored in `state.vscdb` are registered against workspace URI `file:///c%3A/Users/Joshu/dev/ai-os`. A command approved in one domain is pre-approved for all domains. | VERIFIED |
| Nested Git Discovery | Opening a file inside `C:\Users\Joshu\dev\ai-os\projects\lsatu` triggers local instruction discovery (reading `projects/lsatu/CLAUDE.md`), but the project root remains `ai-os`. | OBSERVED |
| Multi-Folder Capability | The `language_server.exe` binary uses a repeated `workspace_uris` protobuf field. The system instruction header explicitly indicates `[URI] -> [CorpusName]` mapping, supporting multi-root projects. | VERIFIED |

---

## 4. Conversation History Scope

Antigravity currently unifies all 51 conversations under Project ID `1e181e2e-860b-48c6-9209-540e3e7a1965`.

### Empirical Findings on History Injection
1. Past Conversations Do Not Enter Model Context: Each conversation maintains an isolated transcript on disk (`~/.gemini/antigravity/brain/<id>/.system_generated/logs/transcript.jsonl`). Past turns from other sessions are never injected into the prompt.
2. Summaries are UI-Only: `conversation_summaries.db` generates titles and previews exclusively for the sidebar UI and workspace management.
3. Cross-Domain Bleed in Suggestions: Because all sessions share one Project ID, cross-conversation search and sidebar history mix frontend bugfixes with student tutoring recaps.
4. Splitting Projects Does Not Reduce Prompt Tokens: Creating a separate project for LSAT U will not reduce the per-turn conversation history tokens, because old conversations are already excluded from prompt context.
5. Real Context Value of Splitting Projects:
   - Root instruction shedding: Sheds 150+ lines of EA and tutoring rules during React development.
   - Skill catalog shedding: Sheds 40+ non-engineering skills from the initial system prompt metadata.
   - Tool scoping: Prevents Google Workspace CLI tools from loading during code refactoring.
   - Search scoping: Bounds file searches directly to `projects/lsatu`.

---

## 5. Knowledge Layer Architecture

| Knowledge Layer | Contents | Authority vs Mirror | Read Frequency | Write Frequency | Intended Consumer | Overlap / Duplication | Freshness | Placement Recommendation |
|---|---|---|---|---|---|---|---|---|
| `wiki/` | Concept notes, hot cache, task ledgers, voice | Canonical Brain | Frequent (via router) | Daily / Per-Session | Jay 2 (EA) / Joshua | Overlaps with `context/` and `corpus/` | Real-time | Shared Root (AIOS) |
| `corpus/` | Pedagogical frameworks, question explanations | Primary Authority | On Demand | Weekly | Assistant / LSAT U | None (authoritative) | Durable | Shared Root (AIOS) |
| `students/` | Profiles, session transcripts, assignments | Primary Working | On Demand (per student) | Post-Session | Assistant (Jay 2) | Overlaps with Supabase homework | Live operational | Operations Domain |
| `decisions/` | Locked architectural & business choices | Primary Authority | On Demand | Per Major Decision | All Agents | Overlaps with brainstorms | Permanent | Shared Root (AIOS) |
| `context/` | Identity, business model, 90-day slate | Primary Authority | Session Start | Monthly | All Agents | Overlaps with `wiki/dashboard` | Stable | Shared Root (AIOS) |
| `references/` | Frameworks (3Ms, Firecrawl, second brain) | Authoritative Guides | On Demand | Rare | Assistant / Subagents | None | Static | Shared Root (AIOS) |
| `raw/` | Immutable sources, web clips, Takeout data | Immutable Evidence | Ingest Only | Weekly | Ingest Subagent | Overlaps with `Clippings/` | Archival | Shared Root (AIOS) |
| `brainstorms/` | RFCs, plan interviews, design thinking | Working Sandbox | During Planning | Active Feature Work | Joshua / Planner | Overlaps with `decisions/` | Transitional | Shared Root (AIOS) |
| `research/` | Technology teardowns, competitive analysis | Derived Reports | On Demand | Per Research Project | Joshua / Assistant | None | Point-in-time | Shared Root (AIOS) |
| `handoffs/` | Continuation notes between sessions | Ephemeral Operational | Session Transitions | End of Session | Next Agent Turn | Overlaps with `wiki/hot.md` | Ephemeral | Shared Root (AIOS) |
| `.gemini/wiki/` | Gemini-specific concept notes | Derived Mirror | Rare | Experimental | Gemini Runtime | Duplicates `wiki/` | Stale | Retire / Merge to `wiki/` |
| Brain Storage | Session transcripts, tool outputs, plans | Raw Execution State | Current Session Only | Continuous | Active Agent | None | Real-time | Runtime Managed (`~/.gemini/`) |
| Claude Memory | Native auto-memory (`MEMORY.md` index) | Learned Fact Store | Automatic (Claude) | Per Insight | Claude Code | None | Continuous | Machine Local |
| Summaries DB | SQLite conversation metadata & titles | UI Index | Sidebar Launch | Per Turn | Antigravity Shell | None | Real-time | Runtime Managed |

---

## 6. Source-of-Truth Map

| Domain / Artifact | Primary Authority | Secondary Mirror | Stale / Historical Source | State Type | Active Contradictions Flagged |
|---|---|---|---|---|---|
| LSAT U Codebase | `projects/lsatu/` (Git repo) | None | Stale snippets in root `scratch/` | Live Static Code | Root instructions reference `projects/lsatu` without sub-repo awareness |
| Production DB | Lovable Cloud Supabase | Local schema types | Mock fixtures in tests | Live Cloud Backend | Local documentation claims direct Supabase CLI migration path |
| Product Decisions | `decisions/log.md` | `wiki/dashboard.md` | `brainstorms/` older notes | Static Authoritative | Some UI specs in `brainstorms/` conflict with locked decisions |
| Student Records | Live Google Drive & Cal.com | `students/<name>/` | `students/roster.generated.md` | Live Operational | Local folder notes lag behind Cal.com cancellations |
| Calendar & Schedule | Google Calendar & Cal.com | `wiki/hot.md` | `wiki/tasks.md` | Live Cloud API | Tasks ledger sometimes marks canceled sessions as open |
| Correspondence | Gmail (Live API) | `wiki/send-ledger.md` | Drafts in `students/<name>/` | Live Cloud API | None (send-ledger is append-only) |
| Payments | Stripe Dashboard / API | `context/work.md` | Notes in `students/` | Live Cloud API | `work.md` estimates MRR that diverges from Stripe live events |
| Teaching Knowledge | `corpus/` | `Loophole Lecture/` | Video files on Google Drive | Durable Static | Concept numbering differs slightly from older video notes |
| Active Tasks | `wiki/tasks.md` & `wiki/hot.md` | None | Brainstorm action items | Live Operational | Completed tasks occasionally remain un-struck |
| Browser Verification | Port 9223 Persistent Chrome | Playwright snapshots | Local temporary screenshots | Live Runtime | Port conflict between default 9222 and dedicated 9223 scripts |
| Machine Config | `.env` (single root secret) | `connections.md` | `setup/` historical notes | Machine Local | None |
| Agent Skills | `.agents/skills/` | `skills/` (central catalog) | `agents/` (18 inactive TOMLs) | Static Executable | 18 legacy TOMLs present in `.gemini/agents/` are inert |
| Research Findings | `research/` & `raw/sources/` | `.gemini/output/` | Old chat outputs in `scratch/` | Static Immutable | None |

---

## 7. LSAT U Engineering Context Requirements

When developing the LSAT U application in `projects/lsatu/`, the agent requires a tightly scoped technical context:

### Always Needed
- Full access to `projects/lsatu/` (codebase, components, package scripts, tailwind configuration).
- Nested engineering instructions (`projects/lsatu/CLAUDE.md` and `projects/lsatu/AGENTS.md`).
- UI polish and component engineering guidelines (`emil-design-eng`, `high-end-visual-design`, `shadcn`).
- Browser verification control (`lsat-u-browser-verification`, Chrome DevTools MCP, Playwright CDP on port 9223).
- Lovable deployment guardrails (Edge function rules, credit spend confirmation requirements).

### Conditionally Needed (Loaded on Explicit Demand)
- Core LSAT drill definitions from `corpus/` when implementing question renderers or score calculators.
- Product design lock records from `decisions/log.md` when reviewing feature scope.
- Anonymized student drill submission schemas from `students/` when building student review dashboards.

### Should NOT Load During Normal Coding
- Private tutoring notes, student transcripts, and prospect consultation correspondence.
- Financial data, pricing offers, Stripe ledger records, and bank credentials.
- Google Workspace CLI skills (`gws-gmail`, `gws-calendar`, `gws-drive`).
- Obsidian second-brain onboarding, linting, and graph management skills.
- Windows audio dictation modes and Bluetooth mouse driver scripts.

---

## 8. Student and Business Operations Context Requirements

When executing executive assistant duties, prospect correspondence, and student tracking:

### Always Needed
- Student operational dossiers (`students/<name>/`) and roster (`students/roster.generated.md`).
- Founder voice authority (`wiki/teaching-voice.md`).
- Active operational ledgers (`wiki/tasks.md`, `wiki/hot.md`, `wiki/send-ledger.md`).
- Google Workspace tools via `gws` CLI (Gmail, Calendar, Drive).
- Consultation inquiry and follow-up templates (`consultation-inquiry-drafts`, `consultation-followup-drafts`).
- Business context (`context/about-me.md`, `context/work.md`).

### Should NOT Inherit from Engineering
- React frontend components, Tailwind styles, and Vite build scripts.
- Node modules, TypeScript configs, and edge function source code.
- Playwright browser test suites and DOM inspection scripts.
- Git worktree management and merge conflict resolution runbooks.

---

## 9. Research and Knowledge Context Requirements

When conducting research, ingesting raw materials, or linting the knowledge base:

### Always Needed
- Intake directory (`raw/inbox/`) and permanent source archive (`raw/sources/clips/`).
- Web research tools (`search_web`, `read_url_content`, Firecrawl integration).
- Knowledge base wiki (`wiki/`) and curriculum repository (`corpus/`).
- Second brain maintenance skills (`second-brain-ingest`, `second-brain-lint`, `second-brain-query`).
- Output directory for persistent reports (`research/`).

### Output Placement and Authority
- Research outputs must be saved with ISO dates to `research/YYYY-MM-DD-<slug>.md`.
- Pure research remains non-authoritative until synthesized and cross-linked into `wiki/` (for concepts) or `corpus/` (for teaching methods).
- Source evidence must retain SHA-256 provenance hashes in `raw/sources/clips/<slug>/PROVENANCE.md`.

---

## 10. Machine and AIOS Administration Context

Administrative and machine-maintenance tasks require specialized system access:

### Scope of Administration
- Antigravity configuration files (`~/.gemini/antigravity/`).
- Central skill catalog synchronization (`skills/`, `.agents/skills/`).
- MCP server configurations (`mcp_config.json`).
- Dedicated browser environment scripts (`system/scripts/launch_lsatu_browser.py`).
- Windows scripts and hardware adjustments (`Install-MagicMouse.ps1`, Superwhisper configs).
- Secret store audits (`.env` validation).

### Isolation Rationale
Administration tasks require broad shell execution permissions (`run_command`), access to machine-level AppData directories, and direct editing of agent runtime configs. Mixing these administrative permissions into routine feature coding creates severe prompt pollution and elevates the risk of accidental configuration drift.

---

## 11. Antigravity Project Options

### Option A: Monolithic Single Project (Current State)
- Structure: One project rooted at `C:\Users\Joshu\dev\ai-os`.
- Context Cleanliness: Low. 36 directories and hundreds of mixed-domain files compete for context.
- Instruction Simplicity: Low. Root instructions must juggle EA, tutoring, and engineering rules simultaneously.
- Skill Scoping: Low. 217 skills are globally visible, causing 98 skills to be suppressed by context budget limits.
- Switching Friction: Zero. Joshua never changes projects.
- Maintenance Burden: High. Unrelated domains drift into shared instruction files.

### Option B: Two Projects (Command Center + LSAT U Engineering) - RECOMMENDED
- Structure:
  1. Project 1 (`ai-os`): `C:\Users\Joshu\dev\ai-os` (Command Center, Operations, Knowledge, Research, Administration).
  2. Project 2 (`lsatu`): `C:\Users\Joshu\dev\ai-os\projects\lsatu` (LSAT U Application Engineering).
- Context Cleanliness: High. React engineering is completely decoupled from student records and business emails.
- Instruction Simplicity: High. Project 2 loads `projects/lsatu/GEMINI.md` directly, shedding all EA rules.
- Skill Scoping: High. Engineering sessions expose only frontend, browser, and testing skills. Operations sessions expose only EA and GWS skills.
- Switching Friction: Minimal. Joshua switches only when transitioning between administrative/student tasks and application coding.
- Git Alignment: Perfect. Project 1 tracks the outer repository; Project 2 tracks the independent LSAT U repository.

### Option C: Three Projects (Engineering + Operations + Administration/Research)
- Structure:
  1. Project 1: `projects/lsatu` (LSAT U Engineering).
  2. Project 2: `students/` + `context/` + `wiki/` (Operations & Tutoring).
  3. Project 3: `ai-os` Root (AIOS System Administration, Research, Skill Maintenance).
- Context Cleanliness: Very High.
- Switching Friction: Moderate to High. Joshua must switch projects to review system health or run research before writing student notes.
- Operational Overhead: High. Knowledge base updates become fragmented across two non-engineering projects.

### Option D: Four or More Projects (Fine-Grained Domain Separation)
- Structure: Separate projects for Engineering, Students, Business, Research, and Administration.
- Analysis: Over-engineered. Creates severe context fragmentation, high switching friction, and constant cross-project jumping. Rejected.

---

## 12. Multi-Folder Project Capability

Inspection of `language_server.exe` confirms that Antigravity 2.0 supports multi-root workspaces via repeated `workspace_uris` protobuf entries.

### How a Multi-Folder Project Operates
In a multi-folder project configuration, an Antigravity project can mount multiple discrete paths:
```json
{
  "folders": [
    { "path": "C:\\Users\\Joshu\\dev\\ai-os\\projects\\lsatu" },
    { "path": "C:\\Users\\Joshu\\dev\\ai-os\\wiki" },
    { "path": "C:\\Users\\Joshu\\dev\\ai-os\\corpus" },
    { "path": "C:\\Users\\Joshu\\dev\\ai-os\\decisions" }
  ]
}
```

### Architectural Implications
1. Instruction Precedence: Each mounted folder evaluates its own local `GEMINI.md` / `AGENTS.md`. Files edited within `projects/lsatu` obey LSAT U rules; files referenced in `wiki` obey wiki rules.
2. File Search: Searches scan across all mounted folder roots but completely bypass unmounted sibling directories (`students/`, `raw/`, `archive/`).
3. Git Integrity: Antigravity respects independent Git roots per folder. Git operations inside `projects/lsatu` execute against the LSAT U repository, while Git operations in `wiki` execute against the outer repository.
4. Overlap Support: Folders can be mounted across multiple projects without file locking conflicts.

---

## 13. Shared Knowledge Without Shared Context

To allow the LSAT U Engineering project to query authoritative knowledge without eagerly loading it into memory, six access mechanisms were evaluated:

| Access Mechanism | Freshness | Context Cost | Drift Risk | Operational Reliability | Maintenance Burden | Suitability |
|---|---|---|---|---|---|---|
| A. Shared Filesystem Mount | Real-time | Moderate (scanned on demand) | Zero (single canonical file) | Very High | Zero | Ideal for multi-folder setups |
| B. Explicit Router Documents | Real-time | Minimal (< 300 tokens) | Low | High | Low | Essential for index navigation |
| C. Skill-Mediated Retrieval | Real-time | Zero eager tokens; on-demand only | Zero | High | Low | Ideal for deep pedagogical queries |
| D. Obsidian CLI / Search | Real-time | High (external tool call) | Low | Moderate (CLI dependency) | Moderate | Overkill for basic lookups |
| E. Cross-Project Markdown Links | Real-time | Negligible | Low | High | Minimal | Best for lightweight references |
| F. Generated Static Summaries | Periodic | Low | High (summaries drift) | Moderate | High (requires sync automation) | Not recommended |

### Recommended Knowledge Strategy
Combine **B (Explicit Router Documents)** with **C (Skill-Mediated Retrieval)**:
- LSAT U engineering sessions maintain a thin reference file (`references/knowledge-router.md`) pointing to `../../corpus/` and `../../decisions/`.
- Knowledge is read strictly on demand via `view_file` or a dedicated read skill, ensuring zero permanent token burden during code edits.

---

## 14. Memory vs Knowledge vs Session State

To prevent architectural confusion, information storage across this machine is partitioned into six discrete lifecycle categories:

| Category | Definition | Concrete Storage Location in AI-OS | Mutation Frequency |
|---|---|---|---|
| 1. MEMORY | Long-lived learned user habits, communication preferences, and tool idioms. | Claude automemory (`~/.claude/projects/.../memory/`) indexed via `MEMORY.md`. | Event-driven (when user states a preference). |
| 2. KNOWLEDGE | Durable, authoritative domain facts, pedagogy, and locked decisions. | `corpus/` (teaching), `decisions/log.md` (architecture), `wiki/` (concepts). | Deliberate synthesis (weekly / per decision). |
| 3. LIVE STATE | Operational backend truth; external APIs and active system services. | Google Calendar, Gmail, Supabase DB, Stripe, running Vite process, port 9223 Chrome. | Real-time / Continuous. |
| 4. SESSION STATE | Ephemeral thoughts, tool arguments, scratch scripts, and active artifacts. | `~/.gemini/antigravity/brain/<conv-id>/`, `scratch/`, `output.txt`. | Turn-by-turn. |
| 5. HANDOFF | Explicit continuation checkpoints designed to transfer context between chats. | `handoffs/YYYY-MM-DD-<topic>.md`, `wiki/hot.md` (hot cache). | Session start / wrapup. |
| 6. RAW EVIDENCE | Immutable source documents, Takeout exports, video recordings, web clips. | `raw/sources/`, `raw/inbox/`, `Clippings/`. | Append-only. |

### Storage Locations Currently Mixing Categories
- `wiki/hot.md`: Mixes Live State notes with Session Handoff text.
- `wiki/tasks.md`: Mixes Durable Knowledge with Live State tracking.
- `.gemini/antigravity/brain/`: Contains both ephemeral scratch scripts and durable implementation plans.

---

## 15. Current Duplication and Drift Audit

Forensic inspection identified eight concrete areas where facts are duplicated across the repository:

| Functional Area | Canonical Candidate | Existing Duplicates | Drift Already Detected | Operational Consequence |
|---|---|---|---|---|
| LSAT U Product Rules | `projects/lsatu/CLAUDE.md` | `AGENTS.md`, `GEMINI.md`, `wiki/dashboard.md` | Root rules reference older feature names and outdated Supabase schemas | Agents operating from root use stale component contracts |
| Lovable Backend Rules | `projects/lsatu/CLAUDE.md` | `AGENTS.md`, `GEMINI.md`, `projects/lsatu/AGENTS.md` | Conflicting advice regarding Supabase CLI vs Lovable Cloud agent | Risk of unauthorized credit spend or failed migrations |
| Teaching Voice | `wiki/teaching-voice.md` | `context/about-me.md`, inline skill system prompts | Skill prompts contain slightly different banned word lists | Outbound drafts show minor stylistic inconsistencies |
| Browser Verification | `system/scripts/launch_lsatu_browser.py` | `output/browser_deep_dive_report.md`, skill docs | Some docs reference default port 9222 while script binds 9223 | Browser connection failures in automated test scripts |
| Active Task Ledger | `wiki/tasks.md` | `wiki/hot.md`, `context/priorities.md` | Tasks struck in `tasks.md` remain listed as active in `priorities.md` | Next agent turn re-evaluates finished work |
| Model Identifiers | Live UI catalog (`state.vscdb`) | `AIOS_PHASE_3` Section 6, legacy TOMLs | Phase 3 cited Gemini 2.0/2.5; live environment uses 3.8/3.7/3.6/3.1 | Agent configs risk invoking deprecated or non-existent models |
| Agent Definitions | `.agents/skills/` & native format | `agents/*.toml` (18 files), `.gemini/agents/*.toml` | TOMLs contain Codex schemas and invalid model strings (`gpt-5.4`) | Files appear active to users but are ignored by Antigravity |
| Git Workflow Rules | `projects/lsatu/CLAUDE.md` | Root `AGENTS.md`, `wiki/HANDLING.md` | Root instructions prohibit git remotes; LSAT U requires git pushes | Agent blocks legitimate LSAT U commits or attempts outer repo pushes |

---

## 16. Context Budget by Domain

Target eager context budgets for each isolated domain (excluding user turn history):

```
Target Eager Context Allocation (in Tokens)

LSAT U Engineering:        [6,500 - 9,500]
  - Instructions:          2,000 - 3,000
  - Scoped Skills:         1,500 - 2,500
  - Native Tools & MCP:    2,500 - 3,500
  - Project Metadata:        500 - 500

Student / Operations:      [8,000 - 13,000]
  - Instructions:          3,000 - 4,500
  - Scoped Skills:         2,000 - 3,500
  - Native Tools & GWS:    2,500 - 4,000
  - Roster / Tasks Cache:    500 - 1,000

Research / Knowledge:      [5,000 - 8,000]
  - Instructions:          1,500 - 2,500
  - Scoped Skills:         1,500 - 2,500
  - Native Tools & Web:    1,500 - 2,500
  - Knowledge Index:         500 - 500

Machine Administration:    [4,000 - 7,000]
  - Instructions:          1,500 - 2,500
  - Scoped Skills:         1,000 - 2,000
  - Native Tools & Shell:  1,500 - 2,500
  - Config Schema:             0 - 0
```

By decoupling domains, LSAT U engineering sessions shed approximately 6,000 to 10,000 tokens of irrelevant operational overhead on every single prompt turn.

---

## 17. Project-Scoped Skills

Under the recommended two-project topology, skills are partitioned into their natural domains:

### Project 1: AIOS Operations & Command Center (`ai-os`)
- Active Skill Allocation:
  - Google Workspace integration: `gws-gmail`, `gws-calendar`, `gws-drive`, `gws-sheets`, `gws-docs`.
  - Student drafting: `consultation-inquiry-drafts`, `consultation-followup-drafts`, `inbound-tutoring-replies`.
  - Knowledge and second brain: `second-brain-ingest`, `second-brain-lint`, `second-brain-query`, `graphify`.
  - Research & media: `watch`, `subtitles`, `captions`, `research`, `firecrawl`.
  - Machine administration: `superwhisper`, `agy-customizations`, `google-antigravity-sdk`.
- Benefits: Completely hides React engineering, Vite testing, and Tailwind polish skills.

### Project 2: LSAT U Engineering (`projects/lsatu`)
- Active Skill Allocation:
  - Frontend engineering & UI polish: `emil-design-eng`, `high-end-visual-design`, `shadcn`, `design-taste-frontend`, `frontend-design`.
  - Browser verification & inspection: `lsat-u-browser-verification`, `chrome-devtools`, `webapp-testing`.
  - Development methodology: `test-driven-development`, `systematic-debugging`, `diagnosing-bugs`, `codebase-design`.
  - Netlify & cloud deployment: `netlify-deploy`, `netlify-functions`, `lovable-migrate`.
- Benefits: Eliminates 100% of email, calendar, and private student operational skills from the coding environment.

---

## 18. Project-Scoped MCP Servers

Analysis of the four active MCP plugins:

| MCP Server | Recommended Scope | Rationale | Token / Overhead Impact |
|---|---|---|---|
| `chrome-devtools` | Project-Scoped (`lsatu`) | Exclusively required for web application UI inspection, console log auditing, and visual DOM verification. | Saves ~3,000 tokens of tool schemas in non-engineering sessions. |
| `notebooks` | On-Demand (Global) | Specialized data science and Python notebook execution. | Zero background cost if unmounted until activated. |
| `visualization` | On-Demand (Global) | Diagramming and chart generation. | Mounted only during data analysis tasks. |
| `data-agent-kit` | Project-Scoped (Operations/Data) | BigQuery, Dataform, and cloud analytics. Never needed during frontend UI coding. | Sheds 15+ complex SQL/BQ tools from frontend sessions. |

---

## 19. Browser Across Project Boundaries

The persistent Chrome instance running on port 9223 (`LSATU-Agent-Chrome`) is critical infrastructure:

1. Machine-Level Infrastructure: The browser process is managed as a machine daemon, completely decoupled from any specific Antigravity project.
2. Port Isolation: Running on port 9223 ensures complete separation from standard developer browser instances running on default port 9222.
3. Access Control:
   - In Project 2 (`lsatu`), the browser verification skill and Chrome DevTools MCP tools are mounted eagerly.
   - In Project 1 (`ai-os`), browser tools are unmounted. If an operations session requires web interaction, it utilizes high-level text fetch tools (`read_url_content`, Firecrawl) or launches an isolated headless browser.
4. Single Profile Integrity: A single persistent Chrome profile avoids memory duplication (saving ~600 MB of RAM) and maintains authenticated session cookies for Loophole and LSAT prep platforms.

---

## 20. Project Switching Friction Analysis

Joshua requires a streamlined workflow without administrative friction. The human cost of switching projects was evaluated across the topologies:

| Topology | Switching Frequency | Typical Trigger for Project Switch | Context Preservation Method | Friction Level |
|---|---|---|---|---|
| Option A (1 Project) | Never | None | All tasks handled in one massive conversation sidebar | Zero switching; high prompt pollution |
| Option B (2 Projects) | 2 to 4 times per day | Shifting between morning EA/email routine and focused coding blocks | Each project retains its own distinct conversation history and recent file tabs | Low; highly manageable natural boundary |
| Option C (3 Projects) | 6 to 10 times per day | Transitioning from tutoring ops to research to code refactoring | Fragmented histories across three sidebars | Moderate to High; disruptive |
| Option D (4+ Projects)| Continuous | Every task change | Constant workspace reloading and window juggling | Unacceptable |

### Cross-Domain Workflow Strategy
Option B matches Joshua's actual daily workflow: morning operations, tutoring review, and communication happen in `ai-os`; focused development happens in `lsatu`.

---

## 21. Recommended Project Topology

### Final Architectural Recommendation: Option B (Two Projects)

```
=================================================================================
                      RECOMMENDED TWO-PROJECT TOPOLOGY
=================================================================================

+-------------------------------------------------------------------------------+
| PROJECT 1: AIOS COMMAND CENTER                                                |
| Path: C:\Users\Joshu\dev\ai-os                                                 |
| Git Authority: Outer Repository (c:\Users\Joshu\dev\ai-os\.git)               |
| Instruction Authority: C:\Users\Joshu\dev\ai-os\GEMINI.md                     |
+-------------------------------------------------------------------------------+
| Purpose: Founder EA, student operations, business, research, knowledge vault   |
| Default Skills: GWS CLI, student drafting, second-brain, research, superwhisper|
| Default MCP: None (on-demand visualization only)                              |
| Browser Access: Headless / read_url_content / Firecrawl                       |
+-------------------------------------------------------------------------------+
                                    |
            Cross-Project Knowledge Sharing (Read-Only Pointers)
                                    |
                                    v
+-------------------------------------------------------------------------------+
| PROJECT 2: LSAT U ENGINEERING                                                 |
| Path: C:\Users\Joshu\dev\ai-os\projects\lsatu                                 |
| Git Authority: Inner Repository (projects\lsatu\.git -> github.com/.../lsatu) |
| Instruction Authority: projects\lsatu\GEMINI.md                               |
+-------------------------------------------------------------------------------+
| Purpose: Full-stack application engineering, UI polish, backend edge functions|
| Default Skills: emil-design-eng, lsat-u-browser-verification, tdd, shadcn     |
| Default MCP: chrome-devtools (port 9223)                                      |
| Browser Access: Persistent LSATU-Agent-Chrome on port 9223                    |
+-------------------------------------------------------------------------------+
```

### Truly Global Shared Assets
- Secrets Store: Root `.env` file (git-ignored, verified by `.gitignore`).
- Hardware & Machine Automation: Superwhisper profiles, Bluetooth mouse scripts, audio daemons.
- Central Skill Library: `skills/` (inert source catalog).
- Chrome Daemon: Port 9223 background service.

---

## 22. Migration Risks and Safeguards

| Migration Risk | Potential Severity | Consequence | Concrete Safeguard |
|---|---|---|---|
| Conversation History Isolation | Low | Stored conversations remain under Project 1 ID and do not appear in Project 2 sidebar | Existing conversations remain accessible by opening Project 1; new engineering conversations start cleanly in Project 2. |
| Instruction Inheritance Breakage | Moderate | Project 2 stops inheriting root `GEMINI.md` guardrails | Port critical global guardrails (95% rule, Lovable credit confirmation, no em-dashes) into `projects/lsatu/GEMINI.md`. |
| Skill Disappearance | Low | An engineering skill accidentally remains in Project 1 | Ensure active skills are mirrored into `projects/lsatu/.agents/skills/`. |
| Git Boundary Confusion | High | Agent runs outer git commands on LSAT U code | Separate project roots guarantee `git` commands execute against the correct `.git` repository. |
| Broken Absolute Paths | Moderate | Hardcoded paths to `c:\Users\Joshu\dev\ai-os\...` break | Standardize on repository-root relative paths across all instructions. |
| Browser Port Collision | Moderate | DevTools attempts to bind port 9222 instead of 9223 | Hardcode port 9223 in Project 2's MCP configuration and launch scripts. |
| Accidental File Duplication | Low | Modifying a mirrored file instead of canonical source | Mark all knowledge references in Project 2 as read-only symlinks or markdown pointers. |
| User Opening Wrong Context | Low | User asks an engineering question in Project 1 | Provide a lightweight router instruction in Project 1 that directs engineering tasks to Project 2. |

---

## 23. Target Success Metrics

The success of the proposed project topology will be evaluated against ten quantifiable benchmarks:

1. Eager Prompt Context in Engineering: Reduced from ~18,000 tokens to under 9,500 tokens per turn.
2. Irrelevant Visible Skills: Zero operations/email skills visible in engineering sessions; zero React skills visible in operations.
3. Suppressed Skill Count: Decreased from 98 suppressed skills to under 15 per project context.
4. Project Switching Frequency: Maintained between 2 and 4 natural switches per working day.
5. Wrong-Repository Commits: Exactly 0 incidents of LSAT U files committed to the outer repo or vice versa.
6. Stale Path Incidents: Exactly 0 failures caused by hardcoded absolute paths.
7. Browser Verification Availability: 100% immediate connection to port 9223 in engineering sessions without port conflicts.
8. Cross-Domain Instruction Conflicts: Zero occurrences of tutoring voice rules interfering with React code generation.
9. Source-of-Truth Discrepancies: Elimination of all 8 identified duplication points.
10. System Responsiveness: Measurable decrease in first-token latency due to lighter system instruction envelopes.

---

## 24. Questions for External Architect and User

Four foundational decisions require adjudication before Phase 5 implementation:

1. **Project Registration Topology Approval**: Does the external architect endorse **Option B (Two Projects: `ai-os` Command Center + `lsatu` Engineering)** as the optimal balance between context cleanliness and human switching overhead?
2. **Multi-Folder vs Pure Nested Isolation**: Should Project 2 (`lsatu`) be a single folder rooted at `projects/lsatu`, or should it be registered as a multi-folder workspace mounting `corpus` and `decisions` directly into the sidebar?
3. **Instruction Synchronization Protocol**: Should `projects/lsatu/GEMINI.md` be maintained as an independent, fully self-contained instruction file, or should an automated synchronization script verify parity for shared guardrails (e.g., 95% rule, Lovable credit safeguards)?
4. **Conversation Archive Strategy**: Upon creating the dedicated `lsatu` project, should previous LSAT U conversations remain in Project 1 history, or should relevant engineering conversations be migrated into the new project ID in `conversation_summaries.db`?

---

## Hard Stop Notice

Phase 4 analysis and design is complete. No projects were created or deleted, no folders were relocated, no configuration settings were changed, and no git operations were performed. All recommendations await formal approval before Phase 5 migration design.
