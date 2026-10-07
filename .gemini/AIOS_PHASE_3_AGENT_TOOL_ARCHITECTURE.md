# AIOS Phase 3: Agent, Model, Tooling, MCP, and Delegation Architecture Report

**Document Role:** Agent Ecosystem & Tooling Control-Plane Specification  
**Execution Constraints:** ANALYSIS AND DESIGN ONLY (Zero file modifications, zero agent conversions, zero config edits)  
**Target Audience:** External Systems Architect / Senior AI Engineer  
**Timestamp:** 2026-09-20T02:30:00-04:00  
**Host Machine:** `J` (Windows 11 Home, Build 26100)  
**Workspace Root:** `C:\Users\Joshu\dev\ai-os`  

---

## 1. CURRENT ACTUAL AGENT RUNTIME

Forensic inspection of the active Antigravity session runtime:

### 1.1 Registered & Active Agent Fleet

| Agent Identifier | Runtime Status | Model | Tools Accessible | Terminal / Shell | Browser Access | Write Access | Recursive Delegation | Recent Usage |
|---|---|---|---|---|---|---|---|---|
| **Primary Agent (Jay 2)** | ACTUALLY REGISTERED | Host Gemini Model | Full Suite (22 native + MCP) | Full (PowerShell / cmd) | Port 9223 via MCP/Playwright | Full (`write_to_file`, `replace_file_content`) | YES (`invoke_subagent`) | 100% of turns |
| **`self` (Subagent)** | ACTUALLY REGISTERED | `inherit` (default) | Inherits parent tools | Inherits parent shell | Inherits parent MCP | Inherits parent filesystem | YES (if depth < max) | Occasional (7 invocations) |
| **`research` (Subagent)** | ACTUALLY REGISTERED | `flash` / `inherit` | Read-only (`view_file`, `search_web`, `read_url`) | NO shell access | NO browser access | Read-Only | NO subagent spawning | Occasional (research tasks) |
| **18 TOML Subagents** | DEFINED ON DISK BUT INERT | Unloaded | Defined in TOML files | Varies per TOML | Varies per TOML | Varies per TOML | Unloaded | 0 invocations in Gemini |
| **Dynamic Subagents** | AVAILABLE DYNAMICALLY | Configurable (`flash_lite`, `flash`, `pro`, `inherit`) | Defined via `define_subagent` | Configurable | Configurable via MCP flag | Configurable via write flag | Configurable | 2 definitions recorded |

### 1.2 Architectural Insight
- The active Antigravity prompt exposes **only 2 subagents** (`self` and `research`).
- The 18 `.toml` files located in `C:\Users\Joshu\dev\ai-os\.gemini\agents\` are **completely inert** in Antigravity runtime unless dynamically instantiated during a conversation via `define_subagent`.

---

## 2. THE 18 EXISTING TOML AGENTS

Census and architectural disposition of the 18 `.toml` agent configurations in `C:\Users\Joshu\dev\ai-os\.gemini\agents\`:

| Filename | Intended Role | Configured Model | Sandbox Mode | Antigravity Ingestion | Historical Usage | Proposed Disposition |
|---|---|---|---|---|---|---|
| `agent-sdk-dev-agent-sdk-verifier-py.toml` | Verify Python Agent SDK code | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** (Procedure, not stateful agent) |
| `agent-sdk-dev-agent-sdk-verifier-ts.toml` | Verify TypeScript Agent SDK code | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `browser-navigator.toml` | Autonomous browser testing | `inherit` | `inherit` | INERT | None | **KEEP AS FUTURE PERSISTENT AGENT** |
| `code-simplifier-code-simplifier.toml` | Refactor & simplify code | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** (Code style rule) |
| `feature-dev-code-architect.toml` | Architectural feature design | `inherit` | `read-only` | INERT | None | **BETTER AS DYNAMIC SUBAGENT** |
| `feature-dev-code-explorer.toml` | Trace execution flows | `inherit` | `read-only` | INERT | None | **BETTER AS DYNAMIC SUBAGENT** |
| `feature-dev-code-reviewer.toml` | Review code for bugs | `inherit` | `read-only` | INERT | None | **KEEP AS FUTURE PERSISTENT AGENT** |
| `hookify-conversation-analyzer.toml` | Analyze conversation transcripts | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `plugin-dev-agent-creator.toml` | Scaffold new agents | `inherit` | `workspace-write` | INERT | None | **BETTER AS SKILL** |
| `plugin-dev-plugin-validator.toml` | Validate plugin manifests | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `plugin-dev-skill-reviewer.toml` | Review skill markdown | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `pr-review-toolkit-code-reviewer.toml` | PR review for standards | `inherit` | `read-only` | INERT | None | **REDUNDANT** (Duplicates `code-reviewer`) |
| `pr-review-toolkit-code-simplifier.toml` | PR code simplification | `inherit` | `read-only` | INERT | None | **REDUNDANT** (Duplicates `code-simplifier`) |
| `pr-review-toolkit-comment-analyzer.toml`| Review code comments | `inherit` | `read-only` | INERT | None | **OBSOLETE / NICHE** |
| `pr-review-toolkit-pr-test-analyzer.toml` | Review PR test coverage | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `pr-review-toolkit-silent-failure-hunter.toml` | Detect swallowed errors | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `pr-review-toolkit-type-design-analyzer.toml` | Review TypeScript types | `inherit` | `read-only` | INERT | None | **BETTER AS SKILL** |
| `web-researcher.toml` | Deep web research | `gpt-5.4` | `read-only` | INERT | None | **KEEP AS FUTURE PERSISTENT AGENT** (Update model) |

---

## 3. CURRENT ANTIGRAVITY 2.0 CUSTOM AGENT FORMAT

Official Antigravity 2.0 specification for persistent custom agents (verified via `agy-customizations` and `google-antigravity-sdk`):

### 3.1 Directory Topology & Naming Standard
- **Workspace Custom Agents:** `[OFFICIALLY DOCUMENTED]` `<workspace-root>/.agents/agents/<agent-name>/agent.md`
- **Global Custom Agents:** `[OFFICIALLY DOCUMENTED]` `~/.gemini/config/agents/<agent-name>/agent.md`
- **File Format:** Markdown file (`agent.md`) with structured YAML frontmatter. TOML format is a legacy OpenAI Codex format and is NOT the native Antigravity 2.0 agent format.

### 3.2 Required YAML Frontmatter Structure
```yaml
---
name: browser_verifier
description: >-
  Specialized visual verification agent connecting over Chrome DevTools Protocol
  on port 9223 to inspect DOM layout and capture screenshots.
model: inherit # Supported: inherit, gemini-3.7-flash, gemini-2.5-pro
agent_behavior: autonomous # Supported: autonomous (default), interactive
capabilities:
  sandbox_mode: read_only # Supported: read_only, workspace_write, unrestricted
  enabled_tools:
    - view_file
    - search_directory
    - call_mcp_tool
  mcp_servers:
    - chrome-devtools
  enable_subagents: false
---
```

### 3.3 Runtime Semantics
- **Rules Inheritance:** `[OFFICIALLY DOCUMENTED]` Custom agents automatically inherit hierarchical `AGENTS.md` and `.agents/rules/*.md` rules unless explicitly overridden.
- **Context Inheritance:** `[OBSERVED LOCALLY]` Persistent custom agents run in an isolated conversation context, receiving the task prompt and inheriting project rules, but NOT inheriting parent chat conversation turn logs.
- **MCP Access:** `[OFFICIALLY DOCUMENTED]` Configured explicitly via `mcp_servers` allowlist in frontmatter.

---

## 4. DYNAMIC SUBAGENT BEHAVIOR

Operational analysis of `invoke_subagent` and `define_subagent` in Antigravity:

### 4.1 Context & State Inheritance
- **Chat History:** Subagents do NOT inherit the full parent turn transcript. They receive a clean conversation context initialized with the prompt provided in `invoke_subagent`.
- **Instruction Rules:** Subagents automatically inherit root `AGENTS.md` and `GEMINI.md` rules because the Antigravity engine re-loads workspace rules for every spawned agent.
- **Skills & Tools:** Subagents inherit native tools and MCP tools according to their configuration (`enable_write_tools`, `enable_mcp_tools`, `enable_subagent_tools`).
- **Filesystem State:** Subagents operate by default in `Workspace: 'inherit'`, sharing the exact same local filesystem working directory. If a child modifies a file, the parent sees it immediately on disk.

### 4.2 Workspace Isolation Modes
- `Workspace: 'inherit'` (Default): Shares the parent's directory directly.
- `Workspace: 'branch'`: Creates an isolated Git branch workspace for speculative code changes.
- `Workspace: 'share'`: Shares underlying Git object storage like a git worktree.

### 4.3 Lifecycle & Failure Propagation
- **Asynchronous Reactive Wakeup:** The primary agent does not poll. When a child finishes, Antigravity fires a high-priority system notification containing the child's final response.
- **Error Containment:** If a subagent throws an unhandled tool exception or times out, the error is caught and returned to the parent as a structured failure message, preventing parent crash.

---

## 5. AGENT USAGE HISTORY

Empirical transcript analysis across the latest 30 substantive Antigravity sessions (52 total brain sessions):
- **`invoke_subagent` Invocations:** **7 recorded invocations**
- **`define_subagent` Invocations:** **2 recorded invocations**
- **`manage_subagents` Invocations:** **15 recorded invocations** (status queries and lifecycle management)

### Delegation Outcomes & Assessment
1. **High-Value Delegations:**
   - Delegating broad codebase search and multi-file research to `research` subagent kept the primary agent's context clean and prevented token exhaustion.
2. **Low-Value / Overhead Delegations:**
   - Delegating single-file inspections or trivial syntax checks added ~10 to 15 seconds of process startup latency without analytical benefit.
3. **Missed Delegation Opportunities:**
   - Running the 5-viewport screenshot sweep on port 9223 sequentially in the primary turn blocked user interaction; this should have run inside a background browser verifier subagent.

---

## 6. MODEL INVENTORY

### 6.1 Available Model Tiers in Installed Antigravity

| Model Tier Identifier | Underlying Engine | Reasoning Level | Primary Availability | Subagent Availability | Best Use Case |
|---|---|---|---|---|---|
| `inherit` | Host Active Model | Dynamic | YES (Default) | YES (Default) | Seamless context inheritance |
| `flash_lite` | Gemini 2.0 Flash Lite | Low / Fast | Selectable | YES | High-throughput file searches, linting |
| `flash` | Gemini 2.0 Flash / 3.7 Flash | Balanced | Selectable | YES | Rapid research, DOM parsing, script execution |
| `pro` | Gemini 2.5 Pro / 3.0 Pro | High / Deep Thinking | Selectable | YES | Architectural design, refactoring, code review |

### 6.2 Incompatible / Stale Model Identifiers Identified
- **Anomaly:** `C:\Users\Joshu\dev\ai-os\.gemini\agents\web-researcher.toml` contains `model = "gpt-5.4"`.
- **Impact:** `gpt-5.4` is an OpenAI model identifier. In Antigravity's Gemini-native runtime, this identifier cannot be resolved natively and causes an initialization error if loaded.

---

## 7. ROLE-BASED MODEL ROUTING

Mapping operational task types to optimal model profiles:

| Task Class | Recommended Model Profile | Profile Characteristics |
|---|---|---|
| **Small Code Edit** (e.g. CSS, button padding) | `flash` | Fast latency, zero reasoning overhead |
| **Normal LSAT U Feature** (e.g. new drill tab) | `flash` / `inherit` | Balanced coding reasoning |
| **Frontend Visual Polish** | `flash` | Strong image multimodal capabilities for screenshot analysis |
| **Hard Bug / Race Condition** | `pro` | Deep reasoning, execution tracing across multiple files |
| **Database / RLS / Migration** | `pro` | Critical invariant reasoning, high penalty for errors |
| **Architecture / Large Refactor** | `pro` | Broad context synthesis and dependency graph evaluation |
| **Pre-commit Code Review** | `pro` (Independent fresh context) | Objective verification without confirmation bias |
| **Visual / Browser Verification** | `flash` | Fast CDP script dispatch and visual layout diffing |
| **Web Research / Sourcing** | `flash` | High throughput, fast web page summarization |
| **Repetitive File Analysis** | `flash_lite` | Minimal token consumption across bulk files |
| **Bootcamp Curriculum Construction**| `pro` | Deep pedagogical logic, LSAT stimulus-question alignment |
| **Machine Administration** | `flash` | Safe command verification and filesystem housekeeping |

---

## 8. PERMANENT AGENT VS SKILL VS DYNAMIC SUBAGENT

### 8.1 The Decision Rubric
- **Primary Agent (Jay 2):** Retains orchestrator role, user conversation, context synthesis, and executive decisions.
- **Persistent Custom Agent:** Justified ONLY when a role requires: (1) isolated long-running state, (2) strict tool allowlists (e.g. read-only sandboxes), (3) dedicated MCP bindings, or (4) independent model routing (e.g. Pro reviewer).
- **Dynamic Subagent:** Use for ephemeral parallel tasks (e.g. broad research sweeps, temporary worktree tasks).
- **Skill:** Use for repeatable procedural runbooks, multi-step instructions, and checklist workflows.
- **MCP / Tool:** Use for low-level protocol bridges (CDP port 9223, BigQuery, databases).
- **Reference Document:** Static facts, knowledge hubs, and curriculum rubrics.

### 8.2 Architectural Reclassification of Existing Candidates

| Candidate Role | Current Location | Proposed Architectural Type | Rationale |
|---|---|---|---|
| `browser-navigator` | TOML Agent | **PERSISTENT CUSTOM AGENT** | Requires dedicated port 9223 MCP binding and browser tools |
| `code-reviewer` | TOML Agent / Skills | **PERSISTENT CUSTOM AGENT** | Requires isolated fresh context and Pro deep thinking |
| `code-architect` | TOML Agent | **SKILL / DYNAMIC SUBAGENT** | Procedure executed during planning mode; not a continuous daemon |
| `code-explorer` | TOML Agent | **SKILL** | Procedural guide for tracing code; primary agent can execute |
| `code-simplifier` | TOML Agent | **SKILL** | Code polish checklist; does not need subagent isolation |
| `silent-failure-hunter` | TOML Agent | **SKILL** | Verification checklist; integrated into code-review |
| `type-design-analyzer` | TOML Agent | **SKILL** | TypeScript best-practices checklist |
| `web-researcher` | TOML Agent | **PERSISTENT CUSTOM AGENT** | Specialized read-only search agent with Firecrawl/web tools |
| `plugin-validator` | TOML Agent | **SKILL** | Diagnostic procedure |
| `skill-reviewer` | TOML Agent | **SKILL** | Diagnostic procedure |

---

## 9. PARALLELISM ON THIS LAPTOP

Hardware baseline: Windows 11 Home, 13th Gen Intel Core i5-1334U (2P+8E cores, 12 threads), 16.0 GB RAM.

### 9.1 Resource Consumption Profile
- Operating System & Background Apps: ~5.5 GB RAM
- Antigravity Host Application (6 processes): ~828 MB RAM
- Persistent Chrome Agent Browser (PID 11904 + children): ~570 MB RAM
- Vite Dev Server (Node.exe): ~99 MB RAM
- Chrome DevTools MCP Daemon: ~107 MB RAM
- Current Baseline Working Set: **~7.1 GB RAM** (~8.6 GB free headroom).

### 9.2 Practical Concurrency Policy
- **Recommended Operating Limit:** **Primary Agent + Maximum 1 to 2 Concurrent Child Subagents.**
- **Concurrency Ceilings:**
  - **1 Primary Only:** Standard development, editing, local commands.
  - **1 Primary + 1 Child:** Background research or port 9223 visual verification running while user chats.
  - **1 Primary + 2 Children:** Maximum safe laptop load (e.g. parallel frontend verifier + web researcher).
  - **Swarms (3+ Subagents):** **STRICTLY DISCOURAGED.** Spawning 3+ subagents creates CPU thermal throttling on the i5-1334U, rapid memory exhaustion, filesystem write locks on Windows NTFS, and severe user review overload.

---

## 10. CURRENT TOOL INVENTORY

Catalog of 22 native tools and 29 MCP tools available to Antigravity:

### Tool Groupings & Costs
1. **Filesystem (Native):** `view_file`, `write_to_file`, `replace_file_content`, `list_dir`, `find_by_name`, `grep_search`. Eager schema cost: ~2,200 tokens. Usage: High (>50% of all actions).
2. **Terminal (Native):** `run_command` (PowerShell/cmd direct host execution). Eager cost: ~450 tokens. Usage: Highest (30.1% of all actions).
3. **Search & Web (Native):** `search_web`, `read_url_content`. Eager cost: ~600 tokens. Usage: Moderate.
4. **Task Management (Native):** `manage_task`, `schedule`. Eager cost: ~900 tokens. Usage: High (17.3% of actions).
5. **Subagents (Native):** `invoke_subagent`, `define_subagent`, `manage_subagents`, `send_message`. Eager cost: ~1,100 tokens. Usage: Low (<2%).
6. **Interaction & UI (Native):** `ask_question`, `generate_image`. Eager cost: ~750 tokens.
7. **MCP Tools (Lazy-loaded):** 29 `chrome-devtools` tools + 2 `gemini-api-docs` eager tools. Schema cost: ~3,500 tokens. Usage: <1% of runtime invocations.

---

## 11. MCP INVENTORY AND OWNERSHIP

Forensic evaluation of all 4 registered MCP servers in `~/.gemini/config/mcp_config.json`:

| MCP Server | Actual Need | Current Usage | Startup Mode | RAM Footprint | Scope Recommendation |
|---|---|---|---|---|---|
| **`chrome-devtools`** | **ESSENTIAL** | Active for port 9223 visual checks | Lazy (On-demand) | ~107 MB | **LSAT U Project Scoped** |
| **`notebooks`** | LOW | Zero recorded usage | Lazy | Idle | **On-Demand / Data Science Only** |
| **`visualization`** | LOW | Zero recorded usage | Lazy | Idle | **On-Demand / Interactive Graphs** |
| **`data-agent-kit`** | VERY LOW | Zero recorded usage | Lazy | Idle | **Global GCP Plugin Only** |

---

## 12. CHROME DEVTOOLS OWNERSHIP

Component ownership matrix across browser automation capabilities:

| Browser Capability | Primary Owner | Secondary / Supporting Layer | Rationale |
|---|---|---|---|
| **Navigation & Lifecycle** | Persistent Chrome Port 9223 | WMI Detached Launcher (`launch_browser.py`) | Decoupled from Antigravity Job Object |
| **DOM Layout Inspection** | Playwright CDP Scripts (`verify_control_drill.mjs`) | Chrome DevTools MCP (`take_snapshot`) | Fast programmatic extraction |
| **Viewport Screenshots** | Playwright CDP Script (`verify-viewports.mjs`) | Chrome DevTools MCP (`take_screenshot`) | Standard 5-viewport sweep |
| **Console Error Tracking** | Playwright CDP listeners | Chrome DevTools MCP (`list_console_messages`) | Real-time array collection |
| **Network Request Logging** | Playwright CDP listeners | Chrome DevTools MCP (`list_network_requests`) | Tracks Supabase API latency |
| **Performance Tracing** | Chrome DevTools MCP (`performance_start_trace`) | Lighthouse Audit | Deep browser profiling |
| **Accessibility (A11y)** | Chrome DevTools MCP (`lighthouse_audit`) | `a11y-debugging` skill | Automated web.dev audit |
| **Authenticated Session** | `LSATU-Agent-Chrome` Profile Directory | `check_auth.mjs` | Persistent Supabase auth in localStorage |
| **Localhost Dev Testing** | `verify_localhost.mjs` | Vite Dev Server (Port 8080) | Local development verification |

---

## 13. FRONTEND VERIFICATION LOOP

### Current Reality vs Ideal Target Sequence
- **Current Reality:** Agent makes code changes, occasionally checks diff, and relies on manual test commands or stops without viewing running app.
- **Target Ideal Sequence:**
  ```text
  1. Inspect Code & Relevant Types
     ↓
  2. Formulate Plan
     ↓
  3. Implement Code Edit
     ↓
  4. Verify TypeScript (`npm run typecheck`) [Sequential]
     ↓
  5. Verify Local Dev Server Running (Port 8080) [Sequential]
     ↓
  6. Connect to Persistent Chrome (Port 9223) [Delegated to Verifier]
     ↓
  7. Extract DOM, Headings, and Console Errors [Sequential]
     ↓
  8. Capture Viewport Sweep (Desktop, Tablet, Mobile) [Sequential]
     ↓
  9. Evaluation: Did DOM match intent? Any console errors?
     ├── If Errors -> Automatic Correction Loop (Repeat 3-8)
     └── If Clean -> Step 10
     ↓
  10. Independent Pre-commit Review (Pro model review diff)
     ↓
  11. Stage and Commit Locally
     ↓
  12. Gate: User Confirmation before Git Remote Push
  ```

---

## 14. TOOL / AGENT COLLISION ANALYSIS

Resolving functional collisions across competing system layers:

1. **Browser Skill vs Browser Agent vs MCP:**
   - *Resolution:* **One Unified Architecture.** Chrome DevTools MCP provides low-level primitive tools; `lsat-u-browser-verification` provides the skill runbook; an optional `browser_verifier` subagent executes heavy sweeps in the background.
2. **Playwright vs DevTools MCP:**
   - *Resolution:* Complementary. Playwright scripts handle automated batch viewport sweeps (`verify-viewports.mjs`); MCP handles interactive step-by-step DOM clicks and inspections.
3. **Debugging Skill vs Debugging Agent:**
   - *Resolution:* Make `systematic-debugging` the authoritative skill. Do not create a separate persistent debugging agent.
4. **Review Skill vs Review Agent:**
   - *Resolution:* Keep `code-review` as the checklist skill; use an independent Pro-model subagent when performing pre-commit review.
5. **Native Web Search vs Research Agent:**
   - *Resolution:* Single-fact lookups use native `search_web`. Deep multi-source investigations delegate to `research` subagent.

---

## 15. PERSISTENT AGENT CANDIDATES

Candidate fleet architectures evaluated for Antigravity 2.0:

### Option 1: Minimal Fleet (2 Persistent Agents - Recommended)
1. **`browser_verifier`:**
   - Role: Connects to port 9223, runs DOM/screenshot sweeps, verifies responsive layouts.
   - Permissions: Read-only filesystem, MCP `chrome-devtools`, no shell execution.
   - Model: `flash` (Fast, multimodal screenshot inspection).
2. **`code_reviewer`:**
   - Role: Independent pre-commit code quality, security, and type design auditor.
   - Permissions: Read-only filesystem, no shell, no browser.
   - Model: `pro` (Deep reasoning, fresh context).

### Option 2: Balanced Fleet (4 Persistent Agents)
- Adds `web_researcher` (deep web search with Firecrawl) and `curriculum_builder` (LSAT question generation).

### Option 3: Maximal Justified Fleet (6 Persistent Agents)
- Adds `database_architect` (Supabase schema/migration verifier) and `second_brain_librarian` (wiki maintainer).

---

## 16. INDEPENDENT REVIEW PATTERN

Evaluation of review strategies for critical code changes:
- **Same-Model Self-Review:** High confirmation bias; model tends to validate its own code. Ineffective for subtle logic bugs.
- **Fresh-Context Same-Model Review:** Moderate effectiveness; eliminates prompt priming and chat inertia.
- **Pro-Model Independent Reviewer (Recommended):** High effectiveness. Spawning an independent `code_reviewer` with `model='pro'` provides rigorous, detached analysis of Git diffs before committing.
- **Review Gating Policy:**
  - Routine UI polish: Skip review.
  - Complex features: Fresh-context Pro review.
  - Database migrations & RLS changes: Mandatory Pro review.

---

## 17. GLOBAL VS PROJECT TOOLING

Classification of tooling and MCP servers into appropriate operational scopes:

| Component | Recommended Scope | Rationale |
|---|---|---|
| **`run_command`, `view_file`, `write_to_file`** | **GLOBAL MACHINE** | Fundamental core agent capabilities |
| **Chrome DevTools MCP (Port 9223)** | **LSAT U PROJECT** | Dedicated to LSAT U web application verification |
| **Google Workspace CLI (`gws`)** | **AI-OS WORKSPACE** | Dedicated to Joshua's EA business and student operations |
| **Data Agent Kit / BigQuery** | **ON-DEMAND PLUGIN** | Specialized data analytics; not needed in daily dev |
| **Notebooks MCP** | **ON-DEMAND** | Only used during experimental Python notebooks |
| **Visualization MCP** | **ON-DEMAND** | Only used for interactive graph visualizers |

---

## 18. TARGET ARCHITECTURE OPTIONS

Three orchestration architectures evaluated for external review:

### OPTION A: Primary-Agent Heavy (Minimal Agents)
- **Layout:** Jay 2 executes virtually all tasks directly using skills. Only `research` subagent used dynamically.
- **Pros:** Lowest latency, simplest execution trace, zero subagent coordination cost.
- **Cons:** Primary context accumulates token fatigue; self-review confirmation bias remains.

### OPTION B: Balanced Specialist Pair (Recommended)
- **Layout:** Jay 2 orchestrates; exactly 2 persistent custom agents (`browser_verifier` and `code_reviewer`) handle specialized offloaded validation.
- **Pros:** Clean separation of concerns; fresh-context review gates; non-blocking visual sweeps.
- **Cons:** Slight coordination latency (~15s) when invoking reviewer.

### OPTION C: Multi-Agent Heavy
- **Layout:** Fleet of 6+ specialized agents (Architect, Coder, Reviewer, Verifier, Researcher, Librarian).
- **Pros:** Highly granular responsibilities.
- **Cons:** Excessive process overhead on i5 laptop; severe orchestration latency; high token cost.

---

## 19. TARGET METRICS

Proposed operational target ranges for the agentic control plane:

| Dimension | Current Baseline | Proposed Target Range | Improvement |
|---|---|---|---|
| **Persistent Custom Agents** | 0 loaded (18 inert TOMLs) | **2 agents** (`browser_verifier`, `code_reviewer`) | Clean, native Antigravity 2.0 definitions |
| **Average Subagents Per Coding Task** | 0.05 subagents | **0.2 to 0.5 subagents** | Routine use of verifier / reviewer |
| **Max Concurrent Subagents** | Unbounded | **1 to 2 concurrent** | Prevents laptop CPU/thermal throttling |
| **Active MCP Daemons** | 1 daemon (~107 MB) | **1 daemon** (Project-scoped) | Kept lean |
| **MCP Schema Discovery Overhead** | ~3,500 tokens | **~1,200 tokens** (Lazy filtered) | 65% reduction in schema token bloat |
| **Pre-commit Review Gating** | 0% automated | **100% of non-trivial PRs** | Elimination of unforced code bugs |

---

## 20. QUESTIONS FOR EXTERNAL ARCHITECT / USER

Decisions that materially change the agent architecture and require human direction:
1. **Adoption of Option B Fleet:** Does the architect endorse creating exactly **2 native Antigravity 2.0 persistent agents** (`browser_verifier` on Port 9223 and `code_reviewer` with Pro model), while retiring the remaining 16 TOML agents into skills?
2. **Model Tier Policy:** Should `model = 'pro'` be reserved exclusively for architectural planning and pre-commit review, keeping all general code generation on `model = 'flash'` to maximize speed?
3. **Browser Verifier Execution Mode:** Should the browser verification sweep run automatically after every UI component edit, or only when explicitly requested by Joshua or before git commit?
4. **Deprecation of Unused MCP Servers:** Should `notebooks`, `visualization`, and `data-agent-kit` be removed from global `mcp_config.json` and kept as dormant on-demand definitions?

