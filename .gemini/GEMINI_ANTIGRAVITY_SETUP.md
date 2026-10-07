# Complete Gemini & Antigravity Setup Blueprint
**Authoritative Architectural Specification**  
**Target Focus:** Google Gemini & Antigravity Agentic Runtime  
**Workspace:** `C:\Users\Joshu\dev\ai-os\.gemini\`  
**Global System Root:** `C:\Users\Joshu\.gemini\`  
**Operator:** Joshua Fisseha | **Assistant Persona:** Jay 2  

---

## 1. Executive Summary & Design Philosophy

The Gemini and Antigravity ecosystem on this machine is structured into two complementary layers:

1. **The Workspace Operating Layer (`C:\Users\Joshu\dev\ai-os\.gemini\`)**:  
   This lives inside your central project repository. It contains all active Gemini skills, custom agent configurations, distilled wiki knowledge, research sources, and generated project deliverables. It is version-controlled, portable, and isolated from Claude and Codex.

2. **The Machine Runtime & Engine Layer (`C:\Users\Joshu\.gemini\`)**:  
   This lives in your Windows user profile. It houses the Antigravity desktop application engine, global execution policies, registered Model Context Protocol (MCP) servers, global plugin definitions, conversation history databases, and session transcripts.

### Core Architectural Principles
- **Strict Vendor Isolation**: Gemini never writes to, modifies, or depends on `.claude/` or `.codex/`. All Gemini assets reside strictly in `.gemini/` and `skills/gemini/`.
- **Progressive Disclosure**: Skills and agents do not dump massive text into every turn. The agent reads high-level frontmatter descriptions and only loads deep references when a task requires them.
- **LLM-Wiki Knowledge Lifecycle**: Information flows from immutable raw sources (`raw/`) to distilled concept notes (`wiki/`) to concrete project deliverables (`output/`).
- **Zero-Login Visual Verification**: A dedicated Chrome browser profile (`C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`) on port `9223` provides persistent authenticated testing for both production (`https://lsatprep.study`) and localhost development (`http://localhost:8080`).

---

## 2. Deep Dive: The Workspace Layer (`C:\Users\Joshu\dev\ai-os\.gemini\`)

This directory is the dedicated operating environment for Gemini within `ai-os`.

```
C:\Users\Joshu\dev\ai-os\.gemini\
├── README.md               <-- Master workspace routing index
├── agents/                 <-- 18 specialized TOML subagent definitions
├── skills/                 <-- 218 active, installed Gemini skills
├── wiki/                   <-- Distilled concept & source notes (LLM-Wiki pattern)
│   ├── concepts/           <-- Reusable conceptual rules & logic models
│   ├── sources/            <-- Documented source notes & lesson extractions
│   ├── index.md            <-- Master knowledge catalog
│   └── log.md              <-- Chronological ingest ledger
├── raw/                    <-- Immutable intake & evidence drops
│   ├── inbox/              <-- Staging area for incoming unclipped material
│   └── sources/            <-- Immutable historical sources
└── output/                 <-- Generated reports, blueprints, and teardowns
```

---

### Folder: `agents/` (18 Specialized Subagents)
Contains TOML profiles that configure specialized autonomous subagents that Antigravity can dispatch via `invoke_subagent`. Each profile sets specific system prompts, tool permissions, and operational constraints.

| Agent TOML File | Role & Purpose |
|---|---|
| `browser-navigator.toml` | Interactive DOM navigation, clicking, form submission, and visual checking via CDP. |
| `web-researcher.toml` | Deep internet research using search engines and Firecrawl without polluting the main context. |
| `feature-dev-code-architect.toml` | High-level system design, schema planning, and modular decomposition before writing code. |
| `feature-dev-code-explorer.toml` | Read-only codebase explorer for tracing call stacks, imports, and component trees. |
| `feature-dev-code-reviewer.toml` | Technical code review, style enforcement, and edge-case detection. |
| `code-simplifier-code-simplifier.toml` | Refactoring complex functions into deep, simple interfaces. |
| `pr-review-toolkit-code-reviewer.toml` | Automated pull request validation and architecture sanity checking. |
| `pr-review-toolkit-code-simplifier.toml` | PR-level code simplification and deduplication. |
| `pr-review-toolkit-comment-analyzer.toml` | Code comment quality, accuracy, and docstring auditing. |
| `pr-review-toolkit-pr-test-analyzer.toml` | Test coverage, assertion strength, and mock validation. |
| `pr-review-toolkit-silent-failure-hunter.toml` | Hunts unhandled promises, swallowed errors, and empty catch blocks. |
| `pr-review-toolkit-type-design-analyzer.toml` | TypeScript type safety, generic design, and strictness audit. |
| `agent-sdk-dev-agent-sdk-verifier-py.toml` | Verifies Python implementations using the Google Antigravity SDK. |
| `agent-sdk-dev-agent-sdk-verifier-ts.toml` | Verifies TypeScript implementations using the Google Antigravity SDK. |
| `hookify-conversation-analyzer.toml` | Analyzes conversation patterns to identify repetitive tasks suitable for automation hooks. |
| `plugin-dev-agent-creator.toml` | Authors new subagent definitions and prompts. |
| `plugin-dev-plugin-validator.toml` | Validates plugin schemas, manifests, and directory hierarchies. |
| `plugin-dev-skill-reviewer.toml` | Lints and validates `SKILL.md` frontmatter and instruction quality. |

---

### Folder: `skills/` (218 Installed Active Skills)
Every skill in this folder is an actionable procedure or cheatsheet. When Antigravity evaluates a user request, it scans the YAML frontmatter (`name` and `description`) of all skills and loads only the one relevant to the task.

#### Critical Custom Skills in This Folder:
1. **`lsat-u-browser-verification/`**:  
   - Purpose: Controls the dedicated Chrome instance on port `9223`.
   - Subfolder `scripts/`: Holds detached WMI launchers, Playwright CDP scripts, and the 5-viewport sweep runner.
   - Capabilities: DOM extraction, console monitoring, network request tracking, non-destructive clicking, and multi-device screenshotting.
2. **`auto-auth-browser/`**:  
   - Purpose: Session state management and automatic login handling for protected sites (Loophole Online, LSAT U).
   - Scripts: Automates form fill using `.env` credentials, avoiding manual login screens.
3. **`second-brain-ingest/`, `second-brain-lint/`, `second-brain-query/`**:  
   - Purpose: Implements the Karpathy LLM-Wiki knowledge pattern. Allows Gemini to ingest raw sources into markdown, audit links for contradictions, and query collected notes.
4. **`design-taste-frontend/`, `frontend-design/`, `minimalist-ui/`, `high-end-visual-design/`**:  
   - Purpose: Enforces premium visual standards for LSAT U. Overrides generic AI design defaults, mandating metric spacing, typographic balance, and warm monochrome aesthetics.
5. **`gws-gmail/`, `gws-calendar/`, `gws-drive/`, `gws-docs/`**:  
   - Purpose: Official Google Workspace CLI automation routines (using `gws`), keeping all email and calendar operations fast and scripted.

---

### Folder: `wiki/` (The Gemini Knowledge Layer)
The structured knowledge repository maintained directly by Gemini:
- **`index.md`**: Master table of contents.
- **`concepts/`**: Reusable concept writeups (for example, `concepts/conditional-sufficient-assumption-strategy.md` outlining formal logic rules, algebraic diagrams, and student execution steps).
- **`sources/`**: Formal summaries of processed research material with source links and timestamps.
- **`log.md`**: Append-only log recording every ingest event, query session, and maintenance action.

---

### Folder: `raw/` (Immutable Intake Drops)
- **`raw/inbox/`**: The dropzone where unorganized transcripts, scraped articles, or student submissions are initially placed.
- **`raw/sources/`**: Once reviewed, immutable sources are stored here permanently. Gemini reads these files to update the wiki, but never modifies the original source.

---

### Folder: `output/` (Permanent Deliverables & Teardowns)
All reports, research summaries, and blueprints generated across Gemini conversations are permanently stored here:

| File Name | Description |
|---|---|
| `ai_model_showdown.md` | Benchmarks and qualitative analysis: Gemini 3.1 Pro vs Claude Opus 4.6 vs GPT-5.6 Luna. |
| `browser_deep_dive_report.md` | Performance and RAM benchmarks: Microsoft Edge vs Google Chrome vs Brave on Windows 11. |
| `edge_workflow_optimizations.md` | Windows 11 Edge tuning, sleep tab policies, and extension management. |
| `laptop_setup_guide.md` | Hardware configuration and Windows developer settings for this machine. |
| `magic_mouse_master_plan.md` | Boot Camp driver extraction and user-space gesture mapping for Apple Magic Mouse 2. |
| `magic_mouse_implementation_plan.md` | Step-by-step installation plan for Magic Mouse Bluetooth drivers. |
| `conditional_logic_notes.md` | Student lesson notes assigned to Asia, pulled directly from LSAT U production database. |
| `conditional-sufficient-assumption-teardown.md` | Detailed pedagogy breakdown for Sufficient Assumption questions. |
| `system_architecture_master.md` | Full-stack machine and AI-OS master blueprint. |
| `GEMINI_ANTIGRAVITY_SETUP.md` | This authoritative specification document. |

---

## 3. Deep Dive: The Machine Runtime Layer (`C:\Users\Joshu\.gemini\`)

This directory is the global machine-level configuration and runtime engine for Google Antigravity on Windows.

```
C:\Users\Joshu\.gemini\
├── config/                         <-- Machine-level Antigravity settings
│   ├── config.json                 <-- Core engine settings & security grants
│   ├── mcp_config.json             <-- Registered Model Context Protocol servers
│   ├── skills.json                 <-- Global skill registry (points to ai-os)
│   ├── projects/                   <-- Active project definitions
│   │   ├── 1e181e2e...json         <-- ai-os project mapping (Active)
│   │   └── 2a2e3dc0...json.bak     <-- c: duplicate project mapping (Archived)
│   ├── plugins/                    <-- Installed global plugins
│   └── skills/                     <-- 33 global machine skills
└── antigravity/                    <-- Desktop application runtime data
    ├── builtin/skills/             <-- Factory-installed skills (agy-customizations, etc.)
    ├── brain/                      <-- 52 session folders (transcripts & logs)
    ├── conversation_summaries.db   <-- SQLite database tracking all chat sessions
    ├── mcp/                        <-- Lazy tool schemas for MCP integrations
    └── scratch/                    <-- Temporary web scraping scratchpad
```

---

### Folder: `config/` (Global Configurations)

#### 1. `config.json` (Core Execution Settings)
Defines how the agent executes commands, manages permissions, and handles remote control:
- **`artifactReviewMode`**: `"ARTIFACT_REVIEW_MODE_TURBO"` (fast automated artifact processing).
- **`autoExecutionPolicy`**: `"CASCADE_COMMANDS_AUTO_EXECUTION_EAGER"` (eagerly chains non-destructive commands).
- **`browserJsExecutionPolicy`**: `"BROWSER_JS_EXECUTION_POLICY_TURBO"` (fast browser script evaluation).
- **`enableTerminalSandbox`**: `false` (grants native PowerShell and Node execution on Windows).
- **`globalPermissionGrants`**: Whitelist of pre-authorized commands, directories, and URL domains (including `lsatprep.study`, `superwhisper.com`, `firecrawl.dev`).

#### 2. `mcp_config.json` (Registered Tool Providers)
Defines the external MCP servers available to Antigravity:
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browserUrl",
        "http://127.0.0.1:9223"
      ]
    },
    "notebooks": { "command": "node", "args": [...] },
    "visualization": { "command": "node", "args": [...] },
    "data-agent-kit": { "command": "node", "args": [...] }
  }
}
```
*Key Functionality:* Connects Antigravity directly to the dedicated Chrome instance on port `9223`, exposing 29 browser tools (`take_screenshot`, `click`, `take_snapshot`, `navigate_page`, `list_console_messages`, `list_network_requests`).

#### 3. `skills.json` (The Global Bridge)
Explicitly links your repository skills to the global Antigravity engine:
```json
{
  "entries": [
    { "path": "C:/Users/Joshu/dev/ai-os/.gemini/skills" },
    { "path": "C:/Users/Joshu/dev/ai-os/.agents/skills" }
  ]
}
```
*Key Functionality:* Ensures that regardless of which window you open in Antigravity, all 218 workspace skills are automatically loaded.

#### 4. `projects/` (Project Registry)
- `1e181e2e-860b-48c6-9209-540e3e7a1965.json`: Maps the project name **`ai-os`** to `file:///c%3A/Users/Joshu/dev/ai-os`.
- `2a2e3dc0-5f6e-44f5-9cb4-5ad0c5a2a95b.json.bak`: The old duplicate entry that registered the entire `C:\` drive as a project. It has been archived so conversations never split into `c:` again.

---

### Folder: `antigravity/` (Application Engine & History)

#### 1. `conversation_summaries.db` (The Session Database)
An internal SQLite database that Antigravity reads to render the left sidebar:
- Schema: Contains table `conversation_summaries` (`conversation_id`, `title`, `preview`, `project_id`, `workspace_uris`, `step_count`, `last_modified_time`).
- State: **All 51 lifetime conversations** are now unified under `project_id = '1e181e2e-860b-48c6-9209-540e3e7a1965'` (`ai-os`). Zero conversations remain unattached.

#### 2. `brain/<conversation-id>/` (The Session Stores)
Contains 52 conversation subfolders. Each subfolder corresponds to a chat session:
- `.system_generated\logs\transcript.jsonl`: Verbatim log of every user prompt, model response, and tool call.
- `.system_generated\tasks\`: Execution logs for background commands and dev servers.
- Session artifacts and temporary scratch scripts.

#### 3. `builtin/skills/` (Factory Skills)
Default skills packaged with the Antigravity installer:
- `agy-customizations`: The official guide and schema reference for Antigravity rules, skills, plugins, and MCP servers.
- `generative_ui`: Instructions for rendering rich inline interactive HTML widgets.
- `migrate-workflows`: Utility for converting legacy workflow files into modern skills.

---

## 4. Master Instruction Routers

Two critical instruction files govern how Gemini behaves across the entire machine:

### 1. Workspace Router: `C:\Users\Joshu\dev\ai-os\GEMINI.md`
Active whenever Antigravity operates inside `ai-os`. Defines:
- Assistant identity (Jay 2, Joshua's executive assistant).
- Complete routing map to context, decisions, wiki, students, and code.
- Strict voice rules (zero em-dashes, no AI-slop words, decisive recommendations).
- Safe tool and secret model (`.env` is the sole truth; zero hardcoded credentials).

### 2. Global Machine Router: `C:\Users\Joshu\GEMINI.md`
Placed directly in `C:\Users\Joshu\`. Whenever an unattached Antigravity window opens or falls back to scratch mode, Antigravity traverses parent directories and reads this file. It immediately instructs the agent that:
- The canonical workspace root is `C:\Users\Joshu\dev\ai-os`.
- The assistant is Jay 2.
- The LSAT U codebase lives in `projects/lsatu`.
- The dedicated agent browser is on port `9223`.

---

## 5. Verification Checklist

To confirm that this setup is healthy at any time:

1. **Workspace Health**:
   - Open `C:\Users\Joshu\dev\ai-os\.gemini\` in your file explorer. All 18 subagents, 218 skills, and 10 deliverables are present and accounted for.
2. **Database Health**:
   - Run in PowerShell:
     ```powershell
     python -c "import sqlite3; conn=sqlite3.connect(r'C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db'); print('Outside project:', conn.cursor().execute('SELECT count(*) FROM conversation_summaries WHERE project_id=\"outside-of-project\"').fetchone()[0]); print('Under ai-os:', conn.cursor().execute('SELECT count(*) FROM conversation_summaries WHERE project_id=\"1e181e2e-860b-48c6-9209-540e3e7a1965\"').fetchone()[0])"
     ```
     Expected result: `Outside project: 0`, `Under ai-os: 51`.
3. **Browser Automation Health**:
   - Run in PowerShell:
     ```powershell
     node C:\Users\Joshu\Tools\LSATU-Agent\agent-browser.mjs status
     ```
     Expected result: `hasLocalStorageAuth: true` on `https://lsatprep.study`.
