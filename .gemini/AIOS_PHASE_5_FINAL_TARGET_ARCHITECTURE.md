# AIOS Phase 5: Final Target Architecture and Migration Specification

Date: September 20, 2026
Environment: Windows 11 (Host J)
Repositories: C:\Users\Joshu\dev\ai-os (Outer) & C:\Users\Joshu\dev\ai-os\projects\lsatu (Inner)
Authority: Synthesized Target Architecture from Phases 0 through 4 and Phase 3B

---

## Executive Summary

This specification defines the final target architecture and execution blueprint for Joshua's AI-OS command center and the LSAT U engineering environment.

Grounded in the forensic evidence of Phases 0 through 4 and Phase 3B, this architecture resolves the core tensions identified in the current system:
1. Context Bleed: Replaces the monolithic single-project model with a clean two-project topology, separating full-stack application development from executive operations.
2. Discovery Inversion: Restructures the skill catalog so that each project discovers 20 to 30 relevant skills rather than overwhelming the runtime with 217 skills (which previously caused 98 skills to be suppressed).
3. Autonomy Conflict: Replaces the binary contradiction between the 95% rule and maximum autonomy with a four-tier, risk-graded autonomy model.
4. Model Staleness: Aligns model routing with the live September 2026 runtime catalog (Gemini 3.8/3.7/3.6 Flash, Gemini 3.1 Pro, Claude Sonnet 4.6 Thinking, Claude Opus 4.6 Thinking, and GPT-OSS 120B).
5. Source-of-Truth Drift: Establishes a strict authority contract across Git repositories, production databases, and knowledge stores.

This document is an architectural specification and migration blueprint. No files, configurations, or databases are modified during this phase.

---

## 1. Final Design Principles

The target architecture is governed by fourteen foundational principles tailored specifically to Joshua's workstation, teaching authority, and business model:

1. Progressive Disclosure Over Context Ingestion: Never load procedural knowledge, skill bodies, or full documentation into prompt context until explicitly triggered by the task.
2. Strict Two-Project Isolation: Maintain two independent Antigravity projects (`ai-os` Command Center and `lsatu` Engineering) to prevent cross-domain context pollution while respecting Git repository boundaries.
3. Single Canonical Source of Truth: Every piece of information has exactly one authoritative owner. Live cloud backends own operational state; local repositories own source code; `corpus/` owns pedagogy; `decisions/log.md` owns locked choices.
4. Risk-Graded Reversible Autonomy: Autonomy is proportional to reversibility. Pure inspection and local reversible edits proceed with maximum autonomy; external, irreversible, and billing actions require explicit approval.
5. Strict Functional Typing: Maintain rigorous separation between Agents (autonomous execution contexts with isolated state), Skills (on-demand procedural instructions), and Tools (executable API/system primitives).
6. Live Operational State Beats Local Mirrors: Real-time backend APIs (Stripe, Cal.com, Google Calendar, Supabase) supersede local scratchpads or markdown notes in all operational conflicts.
7. Evidence Precedes Assertion: Never claim a feature is complete, a bug is fixed, or a build succeeds without verified command output or browser inspection evidence.
8. Bounded Eager Context: Target eager prompt envelopes under 10,000 tokens for engineering sessions and under 13,000 tokens for operations sessions, reserving context for active reasoning.
9. Shared Portable Primitives: Store skills and tools in standard formats accessible across runtimes (Gemini, Claude, Codex) while isolating vendor-specific metadata in owning directories.
10. Independent Specialized Review: Critical code refactors, database migrations, and architectural decisions must be verified by an independent review model with fresh context.
11. Preserved Persistent Infrastructure: Treat the dedicated Chrome browser profile (port 9223) as durable host infrastructure, completely decoupled from agent lifetimes.
12. Deterministic Front-Door Skill Routing: Group sprawling toolsets under unified front-door router skills to eliminate tool discovery collisions.
13. Immutable Source Provenance: Historical sources, web clippings, and student session recordings must be preserved immutably with SHA-256 hashes.
14. Automated Structural Observability: Provide a deterministic health check mechanism (`aios-doctor`) to audit token budgets, detect dead paths, and verify port availability continuously.

---

## 2. Final Directory Architecture

The intended end-state directory structure organizes workstation assets into clearly defined functional roles:

```
C:\Users\Joshu\
├── .gemini\                                     [MACHINE-LOCAL RUNTIME]
│   ├── antigravity\                             # Local harness runtime state, brain, conversations
│   ├── config\                                  # Global Antigravity configuration
│   │   ├── agents\                              # Global custom agent definitions
│   │   ├── rules\                               # Global fallback rules
│   │   └── skills\                              # Machine-level shared utility skills (10-15 skills)
│   └── GEMINI.md                                # Global machine fallback instructions (< 60 lines)
│
├── Tools\LSATU-Agent\                           [MACHINE-LOCAL TOOLING]
│   ├── launch_lsatu_browser.py                  # Canonical browser daemon launcher (port 9223)
│   ├── verify_browser_health.ps1                # Port and CDP connectivity validator
│   └── browser_watchdog.cmd                     # Windows startup watchdog script
│
├── dev\ai-os\                                   [PROJECT 1: AIOS COMMAND CENTER]
│   ├── .git\                                    # Outer repository Git authority
│   ├── .env                                     # Single secret store (git-ignored)
│   ├── AGENTS.md                                # Codex EA instructions (mirrors GEMINI.md)
│   ├── CLAUDE.md                                # Claude Code EA instructions (mirrors GEMINI.md)
│   ├── GEMINI.md                                # Antigravity EA authority (< 120 lines)
│   │
│   ├── .agents\                                 [ACTIVE RUNTIME]
│   │   ├── skills\                              # Active Command Center skills (25-30 skills)
│   │   └── rules\                               # Scoped operational rules (GWS, voice, intake)
│   │
│   ├── .claude\                                 [ACTIVE RUNTIME - Claude Code]
│   ├── .codex\                                  [ACTIVE RUNTIME - Codex]
│   ├── .obsidian\                               [ACTIVE RUNTIME - Vault Configuration]
│   │
│   ├── context\                                 [REFERENCE - Business & Founder Profile]
│   │   ├── about-me.md                          # Identity, working preferences, contact
│   │   ├── work.md                              # Offer structure, pricing, channels
│   │   └── priorities.md                        # 90-day active business priorities
│   │
│   ├── corpus\                                  [CANONICAL CATALOG - Pedagogy Authority]
│   │   ├── index.md                             # Master curriculum router
│   │   └── modules\                             # Drill architectures and teaching methods
│   │
│   ├── decisions\                               [CANONICAL CATALOG - Locked Choices]
│   │   └── log.md                               # Immutable append-only decision ledger
│   │
│   ├── students\                                [ACTIVE RUNTIME - Tutoring Operations]
│   │   ├── README.md                            # Student operations workflow
│   │   ├── roster.generated.md                  # Machine-generated student index
│   │   └── <student-name>\                      # Individual dossiers, transcripts, assignments
│   │
│   ├── wiki\                                    [CANONICAL CATALOG - Second Brain]
│   │   ├── index.md                             # Master index
│   │   ├── hot.md                               # Current-session operational cache
│   │   ├── tasks.md                             # Active work ledger
│   │   ├── log.md                               # Dated history log
│   │   ├── dashboard.md                         # Product ground-truth pointers
│   │   ├── teaching-voice.md                    # Canonical voice rules (zero em-dashes)
│   │   └── send-ledger.md                       # Outbound communication records
│   │
│   ├── research\                                [REFERENCE - Dated Reports]
│   │   └── YYYY-MM-DD-<slug>.md                 # Synthesized research teardowns
│   │
│   ├── raw\                                     [ARCHIVE - Immutable Source Evidence]
│   │   ├── inbox\                               # Unprocessed intake queue
│   │   ├── sources\clips\                       # Permanent clips with PROVENANCE.md + SHA256
│   │   └── data-about-me\                       # Raw personal Takeout exports (git-ignored)
│   │
│   ├── handoffs\                                [ACTIVE RUNTIME - Session Transitions]
│   │   └── YYYY-MM-DD-<topic>.md                # Inter-session operational handoffs
│   │
│   ├── skills\                                  [CANONICAL CATALOG - Inert Skill Library]
│   │   ├── common\                              # Shared portable skills
│   │   ├── gws\                                 # Google Workspace skill family
│   │   └── second-brain\                        # Obsidian / knowledge skill family
│   │
│   ├── system\                                  [MACHINE-LOCAL - System Scripts]
│   │   └── scripts\                             # Local maintenance and validation utilities
│   │
│   └── projects\lsatu\                          [PROJECT 2: LSAT U ENGINEERING]
│       ├── .git\                                # Inner repository Git authority (GitHub remote)
│       ├── package.json                         # React + Vite dependencies and scripts
│       ├── AGENTS.md                            # Codex engineering instructions
│       ├── CLAUDE.md                            # Claude Code engineering instructions
│       ├── GEMINI.md                            # Antigravity engineering authority (< 120 lines)
│       │
│       ├── .agents\                             [ACTIVE RUNTIME - LSAT U Project]
│       │   ├── skills\                          # Active engineering skills (20-25 skills)
│       │   ├── rules\                           # Scoped engineering rules (Lovable, tests, UI)
│       │   └── agents\                          # Workspace persistent custom agents
│       │       ├── browser_verifier\agent.md    # Dedicated browser verification specialist
│       │       └── code_reviewer\agent.md       # Independent code review specialist
│       │
│       ├── src\                                 # Full-stack React / TypeScript application
│       ├── supabase\                            # Lovable Cloud Edge Functions and migrations
│       └── references\                          # Thin router pointers to corpus/ and decisions/
```

---

## 3. Final Instruction Control Plane

The rule hierarchy establishes clear boundaries, eliminating duplication across runtimes:

```
=================================================================================
                       INSTRUCTION CONTROL-PLANE TOPOLOGY
=================================================================================

                     [1] GLOBAL MACHINE FALLBACK
                     Location: ~/.gemini/GEMINI.md
                     Scope: All sessions on Host J
                     Content: Universal safety, secrets policy (.env), no em-dashes
                     Budget: < 60 lines (~500 tokens)
                                    |
                    +---------------+---------------+
                    |                               |
                    v                               v
       [2A] AIOS COMMAND CENTER          [2B] LSAT U ENGINEERING
       Location: ai-os/GEMINI.md         Location: projects/lsatu/GEMINI.md
       Scope: Project 1 Root             Scope: Project 2 Root
       Content: EA mission, student ops,  Content: React/Vite guidelines,
       teaching voice, GWS workflows,     browser verification (port 9223),
       knowledge retrieval order         Lovable cloud deployment rules
       Budget: < 120 lines (~1,200 tok)   Budget: < 120 lines (~1,200 tok)
                    |                               |
                    v                               v
       [3A] AIOS SCOPED RULES            [3B] LSAT U SCOPED RULES
       Location: .agents/rules/*.md      Location: projects/lsatu/.agents/rules/*.md
       Scope: On-demand path matching    Scope: On-demand path matching
       - gws_execution.md                - emil_ui_polish.md
       - student_ingest.md               - lovable_edge_functions.md
       - research_provenance.md          - test_driven_rules.md
```

### Responsibility Matrix by Instruction Level

| Instruction Level | Concrete File | Maximum Budget | Primary Responsibility | Explicit Prohibitions |
|---|---|---|---|---|
| Global Fallback | `~/.gemini/GEMINI.md` | 60 lines | Machine paths, single secret model (`.env`), banned words, universal safety rules. | No student details, no React coding rules, no specific project commands. |
| Project 1 Root | `ai-os/GEMINI.md` | 120 lines | Identity as Jay 2 (Joshua's EA), student operations routing, teaching voice pointer, knowledge retrieval order. | No frontend UI rules, no Vite build commands, no Supabase component schemas. |
| Project 2 Root | `projects/lsatu/GEMINI.md` | 120 lines | Frontend architecture, port 9223 browser verification loop, Lovable deployment safeguards, Git commit rules. | No student correspondence, no consultation drafts, no financial details, no GWS tools. |
| Scoped Rule | `.agents/rules/*.md` | 50 lines / rule | Activated on matching file paths (progressive disclosure). | Never loaded unconditionally into prompt context. |
| Reference Doc | `references/*.md` | Unlimited | Detailed runbooks and framework definitions (e.g., 3Ms framework, Firecrawl API). | Pure passive reference; loaded only via explicit tool call. |

---

## 4. Autonomy Model

The binary conflict between the "95% rule" and "maximum autonomy" is replaced with a four-tier risk-graded autonomy model:

```
+-------------------------------------------------------------------------------+
| TIER 0: READ AND INSPECT (Autonomous Execution)                               |
| Actions: Reading files, searching code, listing directories, inspecting DOM,  |
| web research, reading logs, running read-only Git commands (status, diff).    |
| Rule: Execute immediately without prompting. Never ask permission to inspect. |
+-------------------------------------------------------------------------------+
                                    |
+-------------------------------------------------------------------------------+
| TIER 1: REVERSIBLE LOCAL CHANGES (Autonomous Execution with Diff)             |
| Actions: Editing React components, updating CSS styles, creating local tests, |
| updating local documentation, writing scratch scripts.                        |
| Rule: Execute autonomously. Present diff and verification evidence upon completion.|
+-------------------------------------------------------------------------------+
                                    |
+-------------------------------------------------------------------------------+
| TIER 2: LOCAL STATEFUL CHANGES (Autonomous Execution with Verification)       |
| Actions: Running npm build, installing dependencies, committing to local Git, |
| creating new branches, running database migrations in local dev containers.   |
| Rule: Execute autonomously if requirement confidence > 90%. Log verification  |
| evidence immediately. Halt and ask if unexpected errors occur.                |
+-------------------------------------------------------------------------------+
                                    |
+-------------------------------------------------------------------------------+
| TIER 3: EXTERNAL / PRODUCTION / IRREVERSIBLE (Mandatory Human Approval)       |
| Actions: Git push to remote, Lovable Cloud edge function deploy, actions that |
| spend Lovable credits, sending outbound emails, modifying machine registry or |
| credentials, deleting project directories.                                    |
| Rule: MANDATORY STOP. Present plan, blast radius, and request explicit approval|
| immediately before execution. Never infer approval from broad user requests.  |
+-------------------------------------------------------------------------------+
```

---

## 5. Final Skill Architecture

The active skill footprint is restructured to eliminate the 98 suppressed skills and align discovery with project context:

```
=================================================================================
                          FINAL SKILL TOPOLOGY
=================================================================================

GLOBAL UTILITIES (~12 Skills)
Location: ~/.gemini/config/skills/
- agy-customizations, google-antigravity-sdk, aios-doctor, systematic-debugging,
  verification-before-completion, watch, search-web, read-url

                |                                       |
                v                                       v
AIOS COMMAND CENTER (~25 Skills)        LSAT U ENGINEERING (~22 Skills)
Location: ai-os/.agents/skills/          Location: projects/lsatu/.agents/skills/
- gws-suite (front-door)                 - frontend-polish (front-door)
- consultation-drafts                    - lsat-u-browser-verification
- student-operations                     - emil-design-eng
- second-brain-suite (front-door)        - shadcn-ui
- research-hub (front-door)              - test-driven-development
- superwhisper                           - lovable-deploy-guardrails
- prompt-architect-refiner               - netlify-deploy
- tutor-ocean-profile                    - code-review-assistant

                |                                       |
                +-------------------+-------------------+
                                    |
                                    v
                     INERT CANONICAL CATALOG (~300 Skills)
                     Location: ai-os/skills/
                     - Storage only; never loaded into agent runtime
                     - Organized by vendor/domain (common, gws, second-brain)
                     - Mirrored into active .agents/skills/ on demand
```

### Resolution of Legacy and Intermediate Directories
1. `.gemini/skills/`: Converted to a clean read-only mirror of `.agents/skills/` during migration, then retired once native Antigravity 2.0 discovery is verified.
2. `_snapshots/`, `_inactive/`, `_project-forks/`: Moved into `skills/archive/` inside the inert catalog, removing them from active discovery.
3. Suppressed Skills Resolution: Restricting active workspace skills to 20-30 per project ensures 100% of declared skills remain below the model context ceiling, completely eliminating skill suppression.

---

## 6. Router Skills (Front-Door Pattern)

To compress tool definitions and avoid discovery collisions, seven high-impact router skills are specified:

| Router Skill | Owning Project | Bundled Leaf Capabilities | Activation Trigger | Context Savings |
|---|---|---|---|---|
| `gws-suite` | AIOS Command Center | `gws-gmail`, `gws-calendar`, `gws-drive`, `gws-sheets`, `gws-docs` | Intent to read/send email, manage calendar events, or upload files | Compresses 14 discrete GWS skills into 1 entry (~4,500 tokens saved) |
| `research-hub` | AIOS Command Center | `firecrawl`, `web-search`, `read-url-content`, `source-archiver` | Deep research requests, web crawling, market teardowns | Compresses 6 research tools into 1 entry (~1,800 tokens saved) |
| `second-brain-suite` | AIOS Command Center | `second-brain-ingest`, `second-brain-lint`, `second-brain-query`, `obsidian-bases`, `json-canvas` | Second-brain queries, vault health audits, note ingestion | Compresses 7 Obsidian skills into 1 entry (~2,200 tokens saved) |
| `frontend-polish` | LSAT U Engineering | `emil-design-eng`, `high-end-visual-design`, `shadcn`, `minimalist-ui`, `brand-guidelines` | UI design, component creation, styling polish, animation work | Compresses 8 design skills into 1 entry (~2,800 tokens saved) |
| `debugging-suite` | LSAT U Engineering | `diagnosing-bugs`, `systematic-debugging`, `memory-leak-debugging`, `a11y-debugging` | Error diagnostics, stack trace investigation, regression debugging | Compresses 5 debug skills into 1 entry (~1,500 tokens saved) |
| `media-transcription` | AIOS Command Center | `watch`, `subtitles`, `captions`, `video-transcript`, `loophole-lecture-transcribe` | Video intake, audio transcription, lecture adaptation | Compresses 5 media skills into 1 entry (~1,600 tokens saved) |
| `deploy-suite` | LSAT U Engineering | `netlify-deploy`, `netlify-functions`, `lovable-migrate`, `setup-pre-commit` | Deployment prep, edge function packaging, pre-commit validation | Compresses 4 deploy skills into 1 entry (~1,200 tokens saved) |

---

## 7. Final Agent Architecture

The custom agent fleet is partitioned cleanly between persistent specialists, dynamic execution agents, and procedural skills:

```yaml
# ===============================================================================
# AGENT 1: BROWSER VERIFIER (Persistent Custom Agent)
# Location: projects/lsatu/.agents/agents/browser_verifier/agent.md
# ===============================================================================
name: browser_verifier
description: Dedicated visual verification, DOM inspection, and console regression testing specialist for LSAT U on port 9223.
model: gemini-3.8-flash-high
reasoning_level: high
agent_behavior: autonomous
capabilities:
  sandbox_mode: false
  workspace_containment: strictly_contained
  enable_subagents: false
  enabled_tools:
    - view_file
    - run_command
    - read_url_content
  mcp_servers:
    - chrome-devtools
skills:
  - lsat-u-browser-verification
```

```yaml
# ===============================================================================
# AGENT 2: CODE REVIEWER (Persistent Custom Agent)
# Location: projects/lsatu/.agents/agents/code_reviewer/agent.md
# ===============================================================================
name: code_reviewer
description: Independent adversarial code reviewer for React components, TypeScript types, Supabase edge functions, and security policies.
model: claude-sonnet-4-6
reasoning_level: high
agent_behavior: autonomous
capabilities:
  sandbox_mode: true
  workspace_containment: strictly_contained
  enable_subagents: false
  enabled_tools:
    - view_file
    - list_dir
    - grep_search
    - find_by_name
  disabled_tools:
    - write_to_file
    - replace_file_content
    - run_command
skills:
  - receiving-code-review
```

### Allocation of Other Candidate Roles
- `web_researcher`: Implemented as a **Dynamic Subagent** spawned via `invoke_subagent` using the built-in `research` template with `Model: "flash"`.
- `database_reviewer`: Handled as a **Skill** (`database-review`) executed within the primary session rather than a standing daemon.
- `curriculum_builder`: Handled as a **Skill** (`lsat-u-topic-builder`) in the Command Center project.
- `knowledge_librarian`: Handled as a **Skill** (`second-brain-suite`) in the Command Center project.

---

## 8. Model Routing Policy

Using the verified September 2026 runtime model catalog, tasks route to optimal providers and reasoning levels:

| Task Class | Default Model | Escalation Model | Review Model | Rationale |
|---|---|---|---|---|
| Routine Coding | Gemini 3.8 Flash (High) | Claude Sonnet 4.6 (Thinking) | Code Reviewer Agent | Rapid turnaround, low latency, high native code comprehension. |
| Major Feature Build | Claude Sonnet 4.6 (Thinking) | Claude Opus 4.6 (Thinking) | Code Reviewer Agent | Superior architectural coherence across multi-file edits. |
| Frontend UI / Polish | Claude Sonnet 4.6 (Thinking) | Gemini 3.8 Flash (High) | Browser Verifier Agent | Exceptional nuance with Tailwind, micro-interactions, and visual layouts. |
| Complex Debugging | Gemini 3.8 Flash (High) | Claude Sonnet 4.6 (Thinking) | Independent fresh context | Fast ingestion of massive logs and stack traces. |
| Database / RLS / Migrations | Gemini 3.1 Pro (High) | Claude Opus 4.6 (Thinking) | Code Reviewer Agent | Deep verification of relational constraints and security boundary rules. |
| System Architecture / RFCs | Claude Opus 4.6 (Thinking) | Gemini 3.1 Pro (High) | Joshua (Grill-Me) | Maximum conceptual depth and trade-off evaluation. |
| Browser Visual Verification | Gemini 3.8 Flash (High) | Gemini 3.8 Flash (High) | N/A | High-resolution multimodal vision analysis of screenshots and viewport sweeps. |
| Web Research & Scraping | Gemini 3.8 Flash (Medium) | Gemini 3.8 Flash (High) | Primary Agent | Massive context capacity, cost-effective parallel page ingestion. |
| Bulk Mechanical Refactors | Gemini 3.8 Flash (Low) | Gemini 3.8 Flash (Medium) | Code Reviewer Agent | Highly economical execution for mechanical transformations. |
| Pedagogy & Curriculum | Claude Sonnet 4.6 (Thinking) | Claude Opus 4.6 (Thinking) | Joshua | Nuanced alignment with Joshua's teaching voice and LSAT logic. |
| AIOS Administration | Gemini 3.8 Flash (High) | Gemini 3.1 Pro (High) | Joshua | Fast script generation and system diagnostic execution. |

---

## 9. Final Tool and MCP Architecture

Ownership and mounting policies for system tools and MCP servers:

| Tool / Subsystem | Recommended Scope | Mounting Policy | Rationale |
|---|---|---|---|
| Native File Tools (`view_file`, `write_to_file`, etc.) | Global | Always Active | Core agent primitives required across all operations. |
| Terminal (`run_command`) | Global | Tier-Graded Autonomy | Required everywhere, governed by strict autonomy guardrails. |
| Web Search (`search_web`, `read_url_content`) | Global | Always Active | Essential for live documentation and research lookup. |
| Chrome DevTools MCP | LSAT U Project Only | Active in `lsatu` | Provides browser automation tools exclusively where web apps are built. |
| Google Workspace CLI (`gws`) | AIOS Project Only | Scoped to `ai-os` | Connects to Gmail, Calendar, and Drive; forbidden in engineering sessions. |
| Playwright CDP | Machine Local | Shared Library | Python/Node scripts connect to port 9223 on demand. |
| Notebooks MCP | AIOS Project Only | On Demand | Mounted only during data analysis or Python exploration. |
| Visualization MCP | Global | On Demand | Mounted when generating diagrams or architectural charts. |
| Data Agent Kit MCP | AIOS Project Only | On Demand | Mounted during BigQuery or cloud analytics operations. |
| Firecrawl API | AIOS Project Only | On Demand via Skill | Triggered for deep web extraction and markdown conversion. |
| GitHub CLI (`gh`) | Global | Tier 3 Approval for Pushes | Active for PR reviews, issue checks, and local git queries. |
| Lovable Agent | LSAT U Project Only | Tier 3 Approval for Deploys | Cloud agent routes deployment of edge functions. |

---

## 10. Final Browser Architecture

The persistent Chrome verification environment is canonicalized as machine-level host infrastructure:

```
=================================================================================
                      CANONICAL BROWSER INFRASTRUCTURE
=================================================================================

+-------------------------------------------------------------------------------+
| HOST MACHINE SERVICE (Windows 11)                                             |
| Profile Path: C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome                 |
| Dedicated Port: 9223 (Avoids default 9222 collision)                         |
| Canonical Launcher: C:\Users\Joshu\Tools\LSATU-Agent\launch_lsatu_browser.py   |
| Launch Mechanism: WMI Process Create (Detached background process)            |
+-------------------------------------------------------------------------------+
                                    |
                    Authenticated CDP Session (Port 9223)
                                    |
                    +---------------+---------------+
                    |                               |
                    v                               v
    [CHROME DEVTOOLS MCP SERVER]            [PLAYWRIGHT CDP SCRIPTS]
    Owner: LSAT U Engineering Project       Owner: Tooling / Automated Sweeps
    Capabilities:                           Capabilities:
    - DOM snapshot & element click          - Multi-viewport responsive sweeps
    - Console error streaming               - Authenticated state verification
    - Network request auditing              - Headless automated regression runs
    - Visual viewport capture               - Performance timeline recording
```

### Operational Ownership Matrix
- Lifecycle and Process Management: Owned by `launch_lsatu_browser.py` using WMI detached launch.
- Authentication State: Preserved in `LSATU-Agent-Chrome` user data directory (Loophole and LSAT prep sessions).
- Interactive Verification: Owned by the `browser_verifier` agent via Chrome DevTools MCP.
- Automated Responsive Sweeps: Owned by `system/scripts/verify_responsive_sweep.py` (Desktop 1440px, Tablet 768px, Mobile 375px).

---

## 11. LSAT U Development Loop

The gold-standard workflow for an LSAT U engineering task:

```
[1. Request Ingestion]
   Inspect issue, trace dependencies in src/, identify target components.
   (Model: Primary - Autonomous)
          |
          v
[2. Plan & Architecture Verification]
   Create implementation plan; reference corpus/ or decisions/ if pedagogy or UX is touched.
   (Model: Primary - Autonomous; halted for review only on breaking changes)
          |
          v
[3. Test-Driven Implementation]
   Write failing unit/integration tests; implement React components; apply Emil polish.
   (Model: Primary - Autonomous)
          |
          v
[4. Build & Local Server Verification]
   Run typecheck (tsc); run tests (vitest); verify Vite dev server on port 8080.
   (Model: Primary - Autonomous)
          |
          v
[5. Visual Browser Verification]
   Invoke browser_verifier agent; connect to Chrome on port 9223; inspect DOM; capture screenshot.
   (Model: browser_verifier [Gemini 3.8 Flash High] - Autonomous)
          |
          v
[6. Visual Correction Loop]
   If visual defects or console errors exist, apply corrective CSS/React changes and re-verify.
   (Model: Primary + browser_verifier - Max 3 autonomous iterations)
          |
          v
[7. Independent Code Review]
   Invoke code_reviewer agent with fresh context; check security, types, and logic.
   (Model: code_reviewer [Claude Sonnet 4.6 Thinking] - Autonomous)
          |
          v
[8. Local Commit & Walkthrough]
   Create git commit with clean summary; update walkthrough.md with verification screenshot.
   (Model: Primary - Autonomous Tier 2)
          |
          v
[9. Remote Push & Cloud Deploy]
   MANDATORY STOP. Present commit diff, test results, and deploy route.
   (Requires Joshua explicit approval - Tier 3)
```

---

## 12. AIOS Operations Loop

The standardized workflow for daily executive assistant and student operations:

```
[1. Morning Ingestion & Sweep]
   Run gws-suite to check unread tutoring inquiries and Calendar schedule.
   (Model: Jay 2 Primary [Gemini 3.8 Flash High] - Autonomous Tier 0)
          |
          v
[2. Inquiry Draft Generation]
   Invoke consultation-inquiry-drafts; match prospect tone; apply teaching-voice rules.
   (Model: Jay 2 Primary - Draft saved to send-ledger.md; NEVER auto-sent)
          |
          v
[3. Session Recap Processing]
   Ingest Gemini Meet transcript from Google Drive; update students/<name>/dossier.
   (Model: Jay 2 Primary - Autonomous Tier 1)
          |
          v
[4. Drill Assignment Preparation]
   Query corpus/ via router; format homework brief; prepare platform upload payload.
   (Model: Jay 2 Primary - Autonomous Tier 1)
          |
          v
[5. Wiki Ledger Update]
   Update wiki/tasks.md; refresh wiki/hot.md; append session entry to wiki/log.md.
   (Model: Jay 2 Primary - Autonomous Tier 1)
          |
          v
[6. Outbound Dispatch Review]
   MANDATORY STOP. Present drafted consultation and student emails for Joshua approval.
   (Action: Sent only after human approval - Tier 3)
```

---

## 13. Knowledge Architecture

Information storage across this workstation is structured into six discrete lifecycle layers:

```
=================================================================================
                           KNOWLEDGE LAYERS
=================================================================================

[1. MEMORY] 
Definition: Learned user habits, communication preferences, and tool idioms.
Storage: Claude automemory (~/.claude/projects/.../memory/) + MEMORY.md index.
Authority: Cumulative learned user profile.

[2. KNOWLEDGE]
Definition: Durable, authoritative domain facts, pedagogy, and locked decisions.
Storage: corpus/ (pedagogy), decisions/log.md (architecture), wiki/ (concepts).
Authority: Canonical project truths; immutable without conscious adjudication.

[3. LIVE STATE]
Definition: Operational backend truth; external APIs and active system services.
Storage: Google Calendar, Gmail, Supabase DB, Stripe, running Vite, port 9223 Chrome.
Authority: Absolute operational authority; always supersedes local markdown mirrors.

[4. SESSION STATE]
Definition: Ephemeral thoughts, tool arguments, scratch scripts, active artifacts.
Storage: ~/.gemini/antigravity/brain/<conv-id>/, output.txt.
Authority: Scoped strictly to current conversation turn.

[5. HANDOFF]
Definition: Explicit continuation checkpoints transferring state between chats.
Storage: handoffs/YYYY-MM-DD-<topic>.md, wiki/hot.md (hot cache).
Authority: Operational bridge; expires once absorbed into permanent ledgers.

[6. RAW EVIDENCE]
Definition: Immutable source captures, Takeout exports, recordings, web clips.
Storage: raw/sources/clips/<slug>/, raw/inbox/, Clippings/.
Authority: Permanent evidence base with SHA-256 provenance hashes.
```

---

## 14. Source-of-Truth Contract

The authoritative resolution of all cross-system data ownership:

| Domain / Asset | Primary Authority | Secondary Mirror | Deprecated / Stale Source | Conflict Resolution Policy |
|---|---|---|---|---|
| LSAT U Codebase | `projects/lsatu/` (Inner Git repo) | None | Outer repo scratch files | Inner repo Git status is absolute truth. |
| Production DB | Lovable Cloud Supabase Backend | Local TypeScript types | Mock test fixtures | Live database schema and RLS rules supersede local code. |
| Product Decisions | `decisions/log.md` | `wiki/dashboard.md` | Old notes in `brainstorms/` | `decisions/log.md` wins. Brainstorms are speculative until logged. |
| Student Records | Google Drive & Cal.com Live API | `students/<name>/` | `students/roster.generated.md` | Live API events win. Local markdown is updated to match. |
| Schedule & Sessions | Google Calendar Live API | `wiki/hot.md` | `wiki/tasks.md` | Calendar API wins. Local task entries are struck if canceled upstream. |
| Correspondence | Gmail Live API | `wiki/send-ledger.md` | Drafts in `students/` | Gmail sent folder is absolute truth. `send-ledger` is append-only mirror. |
| Financial Data | Stripe Dashboard / API | `context/work.md` | Notes in `students/` | Stripe live transaction records supersede static estimates. |
| Pedagogy Knowledge | `corpus/` | `Loophole Lecture/` | Video recordings | `corpus/` is primary pedagogy authority; nothing upstream holds it. |
| Active Tasks | `wiki/tasks.md` | `wiki/hot.md` | Brainstorm checklists | `wiki/tasks.md` is central ledger. Struck items are considered complete. |
| Browser State | Port 9223 Chrome CDP | Playwright snapshots | Local screenshot images | Live CDP session inspection is absolute visual truth. |
| Machine Secrets | Root `.env` file | None | None | `.env` is single secret authority. Never tracked in Git. |
| Agent Skills | `.agents/skills/` (Active) | `skills/` (Inert Catalog) | Inactive TOML files | Active `.agents/skills/` governs runtime. Catalog is inert reference. |
| Active Models | Live UI state (`state.vscdb`) | `PHASE_3B` Report | Hardcoded SDK lists | Live `fetchAvailableModels` response in `state.vscdb` wins. |

---

## 15. Versioning and Reproducibility

Classification of workstation assets by versioning strategy:

| Asset Category | Concrete Paths | Versioning Policy | Rationale |
|---|---|---|---|
| Committed to Git (Outer) | `ai-os` Root, `wiki/`, `corpus/`, `context/`, `decisions/`, `references/`, `system/` | Tracked in `ai-os` Git | Authoritative knowledge, decisions, and system scripts must be versioned. |
| Committed to Git (Inner) | `projects/lsatu/src/`, `package.json`, `supabase/` | Tracked in LSAT U Git | Application codebase tracked independently with GitHub remote. |
| Pinned Dependencies | `package.json` packages, `chrome-devtools-mcp` | Pinned SemVer in configs | Prevents breaking changes from floating `@latest` tags in CI and dev. |
| Backed Up but Git-Ignored | `.env`, `raw/data-about-me/`, `raw/sources/` | Local Encrypted / Offline Backup | Contains API credentials and PII; strictly forbidden in Git. |
| Ephemeral / Generated | `node_modules/`, `dist/`, `scratch/`, `~/.gemini/antigravity/brain/` | Git-Ignored; Never Backed Up | Recreatable on demand via package managers or runtime generation. |
| Pinned MCP Server | `chrome-devtools-mcp` | Pinned in `mcp_config.json` | Replace `npx -y chrome-devtools-mcp@latest` with pinned version `@0.9.x`. |

---

## 16. Health Check and Observability Layer (`aios-doctor`)

Specification for an automated health check utility (`system/scripts/aios_doctor.py`):

### Diagnostic Capabilities
1. Context Budget Audit: Measures prompt instruction lines and token weight across both projects.
2. Skill Discovery Health: Reports exposed vs suppressed skill counts; flags any duplicate identifiers.
3. Path Integrity Check: Scans instructions and skills for broken relative links or stale absolute paths.
4. MCP Connectivity Check: Pings configured MCP servers; verifies STDIO/SSE handshake latency.
5. Browser Environment Check: Verifies Chrome is listening on port 9223; tests CDP `/json/version` response.
6. Local Server Check: Verifies Vite dev server status on localhost port 8080.
7. Model Catalog Parity: Compares local model configuration against `state.vscdb` active models.
8. Git Boundary Audit: Verifies zero cross-repository staging or unignored sensitive files.

---

## 17. Backup and Disaster Recovery

Deterministic recovery procedures for system failure scenarios:

### Scenario 1: Windows Workstation Reinstall
1. Prerequisites: Offline backup of `.env` and `raw/`.
2. Clone Repositories: Clone `ai-os` to `C:\Users\Joshu\dev\ai-os`; clone `lsatu` to `C:\Users\Joshu\dev\ai-os\projects\lsatu`.
3. Restore Secrets: Restore `.env` into repository root; verify with `git check-ignore .env`.
4. Install Tooling: Run `system/setup/bootstrap_windows.ps1` (Node.js, Python 3.12, gws CLI, Playwright).
5. Initialize Browser: Run `system/scripts/launch_lsatu_browser.py` to create fresh profile on port 9223.

### Scenario 2: Antigravity IDE Corruption (`~/.gemini` Failure)
1. Close Antigravity IDE processes.
2. Backup conversation database: Copy `~/.gemini/antigravity/conversation_summaries.db` to safe location.
3. Re-initialize configuration: Run `system/scripts/reinit_antigravity_config.py`.
4. Restore global skills from canonical library: Copy from `skills/common/` into `~/.gemini/config/skills/`.
5. Re-open workspace: Antigravity will regenerate `state.vscdb` cleanly.

---

## 18. Final Target Metrics

Quantitative benchmarks defining successful target architecture implementation:

| Metric Dimension | Current Baseline | Target Acceptance Range | Verification Method |
|---|---|---|---|
| LSAT U Engineering Eager Context | ~18,000 tokens | 6,500 - 9,500 tokens | Run token counter on system prompt |
| AIOS Command Center Eager Context | ~22,000 tokens | 8,000 - 13,000 tokens | Run token counter on system prompt |
| Exposed Skills per Project | 85 exposed (global) | 20 - 30 skills per project | `aios-doctor` skill scan |
| Suppressed Skills Count | 98 suppressed skills | < 10 suppressed skills | Prompt metadata inspection |
| Duplicate Skill Identifiers | 43 duplicate names | Exactly 0 duplicates | `aios-doctor` catalog audit |
| Persistent Custom Agents | 0 active (18 dead TOMLs) | Exactly 2 active (`lsatu`) | Agent directory inspection |
| Maximum Concurrent Subagents | Unconstrained swarms | 1 Primary + Max 2 Subagents | Hardware throttle rule validation |
| Browser Port Reliability | Collisions on 9222/9223 | 100% on port 9223 | Socket probe on startup |
| Project Switching Overhead | 0 (monolith) | 2 - 4 clean switches / day | User workflow logging |
| Wrong-Repository Commits | Frequent boundary risks | Exactly 0 incidents | Git commit hook validation |
| Stale Hardcoded Paths | 12 detected in scripts | Exactly 0 stale paths | Regex path audit |
| First-Token Latency | Baseline latency | 25% - 40% reduction | Time to first streaming token |

---

## 19. Migration Waves

The migration plan is structured into ten sequential, reversible waves:

```
=================================================================================
                            MIGRATION WAVE SEQUENCE
=================================================================================

[WAVE 0: Baseline Snapshot & Safety Backup]
Goal: Full backup of repos, configs, databases, and browser profiles before touching any file.
Requires User Approval: Yes (Tier 3)
Rollback: Restore complete backup archive.
       |
       v
[WAVE 1: Antigravity Project Registration]
Goal: Register C:\Users\Joshu\dev\ai-os\projects\lsatu as a dedicated Antigravity Project.
Requires User Approval: No (Safe additive configuration)
Rollback: Remove project registration from Antigravity IDE.
       |
       v
[WAVE 2: Instruction Control-Plane Partitioning]
Goal: Write dedicated, lightweight GEMINI.md in projects/lsatu/ and trim root GEMINI.md.
Requires User Approval: Yes (Instruction authority change)
Rollback: Restore original GEMINI.md from Wave 0 snapshot.
       |
       v
[WAVE 3: Skill Topology Restructuring]
Goal: Populate project-specific .agents/skills/ and archive duplicates in central library.
Requires User Approval: No (Additive local file copies)
Rollback: Revert .agents/skills/ directories.
       |
       v
[WAVE 4: Native Custom Agent Deployment]
Goal: Deploy browser_verifier and code_reviewer agent.md definitions in projects/lsatu/.
Requires User Approval: No (Additive agent definitions)
Rollback: Delete agent.md folders.
       |
       v
[WAVE 5: Tool and MCP Scoping]
Goal: Scope chrome-devtools MCP strictly to lsatu; unmount GWS from engineering.
Requires User Approval: No (Configuration edit)
Rollback: Restore original mcp_config.json.
       |
       v
[WAVE 6: Browser Infrastructure Canonicalization]
Goal: Move and pin browser launcher to Tools/LSATU-Agent/; standardize on port 9223.
Requires User Approval: No (Safe script alignment)
Rollback: Revert launcher script paths.
       |
       v
[WAVE 7: Knowledge & Router Pointers]
Goal: Place thin router documents in projects/lsatu/ pointing to corpus/ and decisions/.
Requires User Approval: No (Additive markdown files)
Rollback: Delete router markdown files.
       |
       v
[WAVE 8: Observability & Health Check Deployment]
Goal: Deploy aios_doctor.py to audit token budgets, broken links, and port health.
Requires User Approval: No (Read-only diagnostic utility)
Rollback: Delete script.
       |
       v
[WAVE 9: Final Acceptance Benchmark]
Goal: Run full verification suite; test visual correction loop on LSAT U drill page.
Requires User Approval: Yes (Final handover sign-off)
Rollback: Review findings and adjust configs if needed.
```

---

## 20. Exact Migration Operations Ledger

Detailed specification of proposed file and configuration changes:

| Operation Type | Source Path | Target Destination | Architectural Rationale | Dependencies | Rollback Plan |
|---|---|---|---|---|---|
| BACKUP | `C:\Users\Joshu\dev\ai-os` | `C:\Users\Joshu\dev\ai-os-backup-pre-migration` | Wave 0 safety snapshot of complete repository state | None | N/A (Safety copy) |
| REGISTER | `C:\Users\Joshu\dev\ai-os\projects\lsatu` | Antigravity IDE Project Registry | Establishes dedicated clean engineering project | Wave 0 | Unregister project |
| REWRITE | `C:\Users\Joshu\dev\ai-os\GEMINI.md` | In-place update | Trims root instructions to EA, student ops, and knowledge routing (< 120 lines) | Wave 1 | Restore from Wave 0 |
| CREATE | `projects/lsatu/GEMINI.md` | `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` | Establishes dedicated engineering instructions for LSAT U (< 120 lines) | Wave 1 | Delete file |
| COPY | Selected frontend skills from `skills/` | `projects/lsatu/.agents/skills/` | Equips engineering project with UI polish, TDD, and debugging skills | Wave 1 | Delete target skills |
| COPY | Selected EA/GWS skills from `skills/` | `ai-os/.agents/skills/` | Equips Command Center with GWS, student drafting, and second-brain skills | Wave 1 | Delete target skills |
| ARCHIVE | 18 legacy `.toml` files in `.gemini/agents/` | `skills/archive/legacy-codex-agents/` | Removes inert Codex agent files from active Gemini view | Wave 0 | Restore to original path |
| CREATE | Dedicated agent definition | `projects/lsatu/.agents/agents/browser_verifier/agent.md` | Native persistent agent for visual verification on port 9223 | Wave 2 | Delete agent directory |
| CREATE | Dedicated agent definition | `projects/lsatu/.agents/agents/code_reviewer/agent.md` | Native persistent agent for adversarial code reviews | Wave 2 | Delete agent directory |
| PIN | `npx -y chrome-devtools-mcp@latest` | Pinned `@0.9.x` in `mcp_config.json` | Prevents upstream breaking changes during browser automation | Wave 5 | Float version |
| MOVE | Browser launch scripts from `system/scripts/` | `C:\Users\Joshu\Tools\LSATU-Agent\` | Establishes persistent machine-level browser daemon tooling | Wave 0 | Move back to system/ |
| CREATE | Thin router markdown | `projects/lsatu/references/knowledge-router.md` | Provides on-demand pointers to `corpus/` and `decisions/` without context load | Wave 1 | Delete file |
| CREATE | Diagnostic utility | `ai-os/system/scripts/aios_doctor.py` | Standalone health check script to verify metrics and path integrity | Wave 8 | Delete script |

---

## 21. Questions That Still Require Joshua

Only three decisions require Joshua's input before Wave 0 execution:

1. **Two-Project Topology Confirmation**: Do you approve establishing `projects/lsatu` as a dedicated, separately opened Antigravity project, understanding you will switch between `ai-os` (operations) and `lsatu` (coding) 2 to 4 times a day?
2. **Conversation History Retention**: Are you satisfied leaving past conversation threads inside the `ai-os` project history, starting fresh dedicated conversations in `lsatu` for future engineering work?
3. **Approval to Proceed with Wave 0**: Do you authorize creating the baseline safety backup (`ai-os-backup-pre-migration`) and beginning the non-destructive Phase 5 migration waves?

---

## 22. Final Architecture Diagram

```
===================================================================================================
                         AI-OS WORKSTATION TARGET ARCHITECTURE
===================================================================================================

                                 +-------------------------+
                                 |  WINDOWS 11 HOST (J)    |
                                 +-------------------------+
                                              |
               +------------------------------+------------------------------+
               |                                                             |
               v                                                             v
+-----------------------------+                               +-----------------------------+
|    GLOBAL RUNTIME LAYER     |                               |   HOST BROWSER INFRA        |
|  ~/.gemini/GEMINI.md        |                               |  Port: 9223                 |
|  ~/.gemini/config/skills/   |                               |  Profile: LSATU-Agent-Chrome|
|  Secrets Store: Root .env   |                               |  Launcher: Tools/LSATU-Agent|
+-----------------------------+                               +-----------------------------+
               |                                                             |
       +-------+-----------------------+                                     |
       |                               |                                     |
       v                               v                                     v
+-----------------------------+ +-----------------------------+ +---------------------------+
| PROJECT 1: AIOS CMD CENTER  | | PROJECT 2: LSAT U ENG       | | LIVE EXTERNAL SERVICES    |
| Root: dev/ai-os             | | Root: dev/ai-os/projects/   | | - Lovable Cloud Supabase  |
| Git: Outer Repository       | |       lsatu                 | | - Stripe Payments API     |
| Authority: Jay 2 (EA)       | | Git: Inner Repository       | | - Google Calendar API     |
|                             | | Authority: Lead Engineer    | | - Gmail API               |
| Core Domains:               | |                             | | - Cal.com Webhooks        |
| - Student Operations        | | Core Domains:               | +---------------------------+
| - Business & Finances       | | - React / Vite Frontend     |
| - Gmail & Calendar Workflows| | - Tailwind UI Polish        |
| - Research & Ingestion      | | - Edge Functions & Schemas  |
| - Second-Brain Wiki Vault   | | - TDD & Testing Suites      |
|                             | | - Visual Verification Loop  |
| Key Skills:                 | |                             |
| - gws-suite (router)        | | Key Skills:                 |
| - consultation-drafts       | | - frontend-polish (router)  |
| - second-brain-suite        | | - lsat-u-browser-verify     |
| - research-hub              | | - test-driven-development   |
| - superwhisper              | | - shadcn-ui                 |
|                             | |                             |
| Custom Agents:              | | Custom Agents:              |
| - Dynamic Research Agent    | | - browser_verifier (9.8 Fl) |
|                             | | - code_reviewer (Sonnet 4.6)|
+-----------------------------+ +-----------------------------+
               |                               ^
               |   On-Demand Knowledge Pointers|
               +-------------------------------+
               | (corpus/ pedagogy, decisions/ log)
               v
+-------------------------------------------------------------+
|               SHARED DURABLE KNOWLEDGE VAULT                |
|  corpus/ (Pedagogy)        decisions/ (Locked Choices)      |
|  wiki/ (Concepts & Ledgers)context/ (Identity & Priorities) |
+-------------------------------------------------------------+
```

---

## 23. Hard Stop Notice

This completes Phase 5. The final target architecture and migration ledger are fully articulated. No files, configurations, projects, or databases have been modified. Execution awaits Joshua's explicit authorization of Wave 0.
