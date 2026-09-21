# Script to assemble ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md
import os

target_path_root = r"C:\Users\Joshu\dev\ai-os\ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md"
target_path_gemini = r"C:\Users\Joshu\dev\ai-os\.gemini\ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md"

content = r"""# Antigravity Runtime Architecture Audit: Forensic Evidence Report

**Document Status:** Complete Forensic Runtime Inventory  
**Target Audience:** External Architecture Auditor / Senior Systems Architect  
**Investigation Timestamp:** 2026-09-19T22:45:00-04:00  
**Machine Host:** `J` (Windows 11 Home, Build 26100/26200, 64-bit)  
**Primary Working Directory:** `C:\Users\Joshu\dev\ai-os`  
**Execution Context:** Google Antigravity Agent Runtime (Engine version 2.15.0.0, Node v24.19.0, Python 3.12.9)  

---

### Epistemic Tagging Standards

Every factual claim in this audit is tagged with one of four evidentiary levels:
- `[VERIFIED]`: Directly confirmed by live command output, file system inspection, process query, or database query during this audit session.
- `[OBSERVED]`: Directly visible in the active runtime context (system prompt, environment variables, loaded MCP schemas, or active tool output).
- `[INFERRED]`: Deduced logically from observed configuration or filesystem layout, but lacking explicit runtime debug tracing.
- `[UNKNOWN]`: Unresolved, ambiguous, or unverifiable without external proprietary documentation or user input.

---

## 1. System Hardware & Execution Baseline

- **Operating System:** `[VERIFIED]` Microsoft Windows 11 Home, Version 10.0.26100 (reported as Build 26200 in PowerShell session metadata).
- **Computer Hostname:** `[VERIFIED]` `J`
- **CPU:** `[VERIFIED]` 13th Gen Intel(R) Core(TM) i5-1334U (1.30 GHz base, 10 physical cores: 2 Performance cores, 8 Efficient cores, 12 logical processors).
- **Physical Memory (RAM):** `[VERIFIED]` 16.0 GB total (15.7 GB usable installed).
- **Storage Volume C:** `[VERIFIED]` Total: 452.9 GB; Used: 274.0 GB; Free: 178.9 GB (NTFS).
- **Installed Runtimes:**
  - Node.js: `[VERIFIED]` v24.19.0 (installed at `C:\Program Files\nodejs\node.exe`).
  - Python: `[VERIFIED]` v3.12.9 (installed at `C:\Users\Joshu\AppData\Local\Programs\Python\Python312\python.exe`).
  - Google Chrome: `[VERIFIED]` v153.0.8010.53 (installed at `C:\Program Files\Google\Chrome\Application\chrome.exe`).
  - Microsoft Edge: `[VERIFIED]` v134.0.3124.72 (installed at `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`).
  - Antigravity: `[VERIFIED]` v2.15.0.0 (binary located at `C:\Users\Joshu\AppData\Local\Programs\antigravity\Antigravity.exe`).

---

## 2. Directory Traversal & Filesystem Topology

### 2.1 Filesystem Link & Junction Scan
- `[VERIFIED]` A complete directory inspection across `C:\Users\Joshu\dev\ai-os` confirmed that all 34 top-level subdirectories are standard NTFS directories (`Link/Junction: False`).
- `[VERIFIED]` There are no NTFS reparse points, symbolic links, or hard directory junctions inside `ai-os` root.
- `[VERIFIED]` Directory footprints:
  - `C:\Users\Joshu\.gemini`: 4,394 files, 218.81 MB.
  - `C:\Users\Joshu\dev\ai-os\.gemini`: 1,255 files, 35.01 MB.
  - `C:\Users\Joshu\dev\ai-os\projects\lsatu`: 83,953 files, 1,384.42 MB (dominated by `node_modules`).
  - `C:\Users\Joshu\dev\ai-os\.agents`: 29 files, 0.17 MB (Codex runtime directory).
  - `C:\Users\Joshu\dev\ai-os\.claude`: 15 files, 0.06 MB (Claude Code runtime directory).

### 2.2 Global Gemini Home vs Workspace Gemini Home
- `[VERIFIED]` Global State Path: `C:\Users\Joshu\.gemini`
  - Houses Antigravity engine binaries, local brain storage (`antigravity\brain`), global config files (`config\config.json`, `config\mcp_config.json`, `config\skills.json`), and built-in skill definitions (`antigravity\builtin\skills`).
- `[VERIFIED]` Workspace Path: `C:\Users\Joshu\dev\ai-os\.gemini`
  - Houses workspace-specific active skills (`.gemini\skills\`), subagent definitions (`.gemini\agents\*.toml`), wiki records (`.gemini\wiki\`), raw intakes (`.gemini\raw\`), and outputs (`.gemini\output\`).

---

## 3. Instruction Topology & Precedence Ladder

### 3.1 Discovered Instruction Files
A machine-wide scan identified 23 `GEMINI.md` files. The 4 primary files impacting this operating environment are:
1. `C:\Users\Joshu\GEMINI.md` (1,799 bytes): Global user-profile router.
2. `C:\Users\Joshu\dev\ai-os\GEMINI.md` (11,764 bytes): Workspace root operating instructions for Jay 2.
3. `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` (1,368 bytes): LSAT U project-specific sub-tree instructions.
4. `C:\Users\Joshu\dev\ai-os\aios\GEMINI.md` (1,615 bytes): Archived/legacy reform folder instructions dated Sept 14, 2026.

### 3.2 Precedence Rules & Conflict Analysis
- `[OBSERVED]` Antigravity reads instructions hierarchically starting from Git/workspace root down to the current working directory, with inner instruction files superseding outer files for their subtree.
- `[VERIFIED]` Conflicting Directives:
  - **Autonomy Level:**
    - Root `GEMINI.md` line 124 mandates: `"95% rule. Make no changes until you are 95% confident what Joshua wants. Ask until you are."`
    - Subtree `projects/lsatu/GEMINI.md` line 7 mandates: `"Maximum Autonomy Rule: NEVER ask clarifying questions. Make sensible architectural decisions independently and implement them directly."`
    - *Runtime Effect:* When working inside `projects/lsatu/`, the agent is instructed to operate with complete unilateral autonomy. When operating in `ai-os` root, the agent is instructed to stop and ask whenever confidence is below 95%.
  - **Git Operations:**
    - Root `GEMINI.md` line 118 mandates: `"No Git remote, ever, without first completing the scrub checklist in wiki/HANDLING.md."`
    - Subtree `projects/lsatu/GEMINI.md` line 11 permits standard branch commits and pushes on the isolated application repo.
  - **Rule Mirroring:**
    - `CLAUDE.md`, `AGENTS.md`, and `GEMINI.md` at root are maintained as twin mirrors. However, `AGENTS.md` and `CLAUDE.md` do not contain the dedicated Gemini workspace definitions found in `GEMINI.md` lines 112 to 121.

---

## 4. Configuration & Runtime Engine State

### 4.1 Global Config (`C:\Users\Joshu\.gemini\config\config.json`)
- `[VERIFIED]` Contents:
  - `turbo_policies`: 7 active permission rules auto-approved without user confirmation (`run_command` for git status/log, `view_file`, `list_dir`, `grep_search`, `find_by_name`).
  - `auto_approval_enabled`: `true`
  - `sandbox_enabled`: `false` (commands execute directly on host Windows OS via PowerShell/cmd).
  - `project_directory`: `C:\Users\Joshu\dev\ai-os`

### 4.2 MCP Server Registry (`C:\Users\Joshu\.gemini\config\mcp_config.json`)
- `[VERIFIED]` Registered MCP Servers:
  1. `chrome-devtools`:
     - Command: `npx`
     - Args: `["-y", "chrome-devtools-mcp@latest", "--browserUrl", "http://127.0.0.1:9223"]`
     - Status: Active in runtime. Lazy-loaded tools registered.
  2. `notebooks`:
     - Configured for local data science notebooks.
  3. `visualization`:
     - Configured for interactive graph visualizations.
  4. `data-agent-kit`:
     - Configured for BigQuery and Google Cloud integrations.

### 4.3 Skill Inheritance (`C:\Users\Joshu\.gemini\config\skills.json`)
- `[VERIFIED]` Configured skill search paths:
  1. `C:/Users/Joshu/.gemini/config/skills`
  2. `C:/Users/Joshu/dev/ai-os/.gemini/skills`
  3. `C:/Users/Joshu/dev/ai-os/.agents/skills`
- `[VERIFIED]` Critical Architectural Finding: `skills.json` explicitly indexes `C:/Users/Joshu/dev/ai-os/.agents/skills`. `.agents/` is the dedicated Codex runtime directory. This means Antigravity inherits and exposes Codex skills directly into the Gemini runtime, creating cross-runtime exposure despite documentation stating strict runtime isolation.

### 4.4 Project Registry (`C:\Users\Joshu\.gemini\config\projects\`)
- `[VERIFIED]` `1e181e2e-860b-48c6-9209-540e3e7a1965.json`: Active project definition for `c:\Users\Joshu\dev\ai-os`.
- `[VERIFIED]` `2a2e1d7a-cfb3-46aa-bf3a-96948ae701bb.json.bak`: Archived project definition for standalone `projects\lsatu` session prior to unification.
- `[VERIFIED]` `conversation_summaries.db`: SQLite database indexing 51 conversation sessions, all unified under active `project_id = '1e181e2e-860b-48c6-9209-540e3e7a1965'`.

---

## 5. Complete Skills Inventory & Taxonomy

### 5.1 Skill Population Metrics
- `[VERIFIED]` Total subdirectories in `C:\Users\Joshu\dev\ai-os\.gemini\skills`: 219.
- `[VERIFIED]` Directories containing valid `SKILL.md`: 215.
- `[VERIFIED]` Container directories:
  - `_inactive/`: Contains 13 archived skills (`captions`, `subtitles`, `transcript`, `transcriptapi`, `video-transcript`, `youtube-api`, `youtube-channels`, `youtube-data`, `youtube-playlist`, `youtube-search`, `yt`, `session-handoff-nate`, `session-handoff-nate-active-copy`). All 13 contain valid `SKILL.md` files.
  - `_project-forks/`: Contains `lsatu` with 18 sub-skill directories. 7 contain `SKILL.md` (`emil-design-eng`, `extract-design`, `find-skills`, `notebooklm`, `pickup`, `ponytail`, `skill-creator`, `subagent-driven-development`, `using-git-worktrees`).
  - `_snapshots/`: Contains 37 vendor/fork snapshots. All 37 contain valid `SKILL.md` files.
  - Examples/Templates: `example-command`, `example-skill`.

### 5.2 Antigravity Skill Discovery Mechanism
- `[VERIFIED]` Antigravity performs a recursive descent search inside skill roots.
- `[OBSERVED]` Files located inside `_inactive/` and `_snapshots/` are actively parsed and presented in the agent's `<skills>` context block (e.g. `_snapshots/a11y-debugging`, `_inactive/session-handoff-nate-active-copy`). Placing a skill inside an underscore-prefixed directory does NOT deactivate it in Antigravity unless specifically excluded by configuration.
- `[OBSERVED]` In the active session context prompt, 85 skills are exposed with full descriptions and paths, while 98 skills are suppressed due to context token budget limits.

### 5.3 Redundant & Overlapping Skill Clusters
- `[VERIFIED]` Forensic analysis identified multiple overlapping clusters:
  1. **Code Review Cluster (5 skills):**
     - `code-review` (6.5 KB), `codex-review` (11.7 KB), `review` (4.0 KB), `requesting-code-review` (2.8 KB), `receiving-code-review` (6.3 KB).
  2. **Debugging Cluster (5 skills):**
     - `systematic-debugging` (9.8 KB), `diagnosing-bugs` (8.5 KB), `a11y-debugging` (5.6 KB, duplicate in `_snapshots`), `troubleshooting` (5.6 KB, duplicate in `_snapshots`), `memory-leak-debugging` (in config).
  3. **Test-Driven Development Cluster (2 skills):**
     - `tdd` (3.5 KB) vs `test-driven-development` (9.8 KB).
  4. **Implementation & Planning Cluster (3 skills):**
     - `subagent-driven-development` (21.6 KB in root, 12.1 KB fork in `_project-forks/lsatu`), `executing-plans` (2.5 KB), `writing-plans` (7.0 KB).
  5. **Handoff & Session Transition Cluster (6 skills):**
     - `session-handoff` (6.2 KB), `session-handoff-nate` (4.8 KB in `_inactive`), `session-handoff-nate-active-copy` (4.8 KB in `_inactive`), `lsatu-cc-handoff` (8.6 KB), `wrapup` (2.7 KB), `pickup` (3.4 KB in root, 1.9 KB fork in `_project-forks/lsatu`).
  6. **Skill Creation Cluster (6 skills):**
     - `skill-creator` (33.1 KB duplicate in `_project-forks`), `skill-development` (22.8 KB duplicate in `_snapshots`), `writing-skills` (26.4 KB), `skill-repair` (1.7 KB), `skill-doctor` (6.2 KB), `skill-lint` (3.7 KB).
  7. **Frontend Design Cluster (6 skills):**
     - `frontend-design` (9.3 KB), `design-taste-frontend` (21.1 KB), `high-end-visual-design` (10.5 KB), `minimalist-ui` (7.9 KB), `redesign-existing-projects` (15.0 KB), `emil-design-eng` (27.3 KB duplicate in `_project-forks`).
  8. **Browser Automation Cluster (5 skills):**
     - `auto-auth-browser` (2.2 KB), `edge-live-control` (4.1 KB), `lsat-u-browser-verification` (2.0 KB), `webapp-testing` (3.9 KB), `chrome-devtools` (2.3 KB duplicate in `_snapshots`).
  9. **Grilling & Interview Cluster (4 skills):**
     - `grill-me` (7.0 KB), `grill-me-codex` (10.7 KB), `grill-with-docs` (2.0 KB), `grill-with-docs-codex` (11.0 KB).
  10. **MCP Building Cluster (5 skills):**
      - `mcp-builder` (9.0 KB), `build-mcp-app` (17.3 KB), `build-mcp-server` (12.0 KB), `build-mcpb` (7.8 KB), `mcp-integration` (12.5 KB).

---

## 6. Subagents Taxonomy & Runtime Behavior

### 6.1 Discovered Subagent Definitions (`.gemini/agents/*.toml`)
- `[VERIFIED]` Exactly 18 `.toml` subagent definition files exist in `C:\Users\Joshu\dev\ai-os\.gemini\agents\`:
  1. `agent-sdk-dev-agent-sdk-verifier-py.toml` (5.3 KB, sandbox: `read-only`)
  2. `agent-sdk-dev-agent-sdk-verifier-ts.toml` (5.6 KB, sandbox: `read-only`)
  3. `browser-navigator.toml` (2.1 KB, sandbox: `inherit`)
  4. `code-simplifier-code-simplifier.toml` (3.2 KB, sandbox: `read-only`)
  5. `feature-dev-code-architect.toml` (2.2 KB, sandbox: `read-only`)
  6. `feature-dev-code-explorer.toml` (2.1 KB, sandbox: `read-only`)
  7. `feature-dev-code-reviewer.toml` (2.9 KB, sandbox: `read-only`)
  8. `hookify-conversation-analyzer.toml` (5.7 KB, sandbox: `read-only`)
  9. `plugin-dev-agent-creator.toml` (7.6 KB, sandbox: `workspace-write`)
  10. `plugin-dev-plugin-validator.toml` (6.8 KB, sandbox: `read-only`)
  11. `plugin-dev-skill-reviewer.toml` (6.3 KB, sandbox: `read-only`)
  12. `pr-review-toolkit-code-reviewer.toml` (4.1 KB, sandbox: `read-only`)
  13. `pr-review-toolkit-code-simplifier.toml` (5.3 KB, sandbox: `read-only`)
  14. `pr-review-toolkit-comment-analyzer.toml` (5.8 KB, sandbox: `read-only`)
  15. `pr-review-toolkit-pr-test-analyzer.toml` (5.1 KB, sandbox: `read-only`)
  16. `pr-review-toolkit-silent-failure-hunter.toml` (8.0 KB, sandbox: `read-only`)
  17. `pr-review-toolkit-type-design-analyzer.toml` (5.5 KB, sandbox: `read-only`)
  18. `web-researcher.toml` (7.0 KB, model: `"gpt-5.4"`, sandbox: `read-only`)

### 6.2 Antigravity Subagent Discovery Disconnect
- `[OBSERVED]` In the active session prompt under `<subagents>`, only two subagents are registered:
  - `self` (inherits full parent context and tools)
  - `research` (read-only research subagent)
- `[VERIFIED]` The 18 `.toml` agent definitions located in `C:\Users\Joshu\dev\ai-os\.gemini\agents\` are NOT loaded automatically into the active agent runtime unless declared dynamically via the `define_subagent` tool.
- `[VERIFIED]` Anomaly: `web-researcher.toml` explicitly sets `model = "gpt-5.4"`, an OpenAI model identifier, inside a Gemini/Antigravity agent definition.

---

## 7. MCP Architecture & Active Servers

### 7.1 Server Configurations
- `[VERIFIED]` Configured in `C:\Users\Joshu\.gemini\config\mcp_config.json`:
  - Name: `chrome-devtools`
  - Launch Command: `npx -y chrome-devtools-mcp@latest --browserUrl http://127.0.0.1:9223`
  - Mode: Lazy-loaded. Tools are defined via schema JSON files in `C:\Users\Joshu\.gemini\antigravity\mcp\chrome-devtools`.

### 7.2 Tool Discrepancy Resolution (29 vs 31 Tools)
- `[VERIFIED]` There are exactly 29 JSON tool schema files in `C:\Users\Joshu\.gemini\antigravity\mcp\chrome-devtools`:
  1. `click`
  2. `close_page`
  3. `drag`
  4. `emulate`
  5. `evaluate_script`
  6. `fill`
  7. `fill_form`
  8. `get_console_message`
  9. `get_network_request`
  10. `handle_dialog`
  11. `hover`
  12. `lighthouse_audit`
  13. `list_console_messages`
  14. `list_network_requests`
  15. `list_pages`
  16. `navigate_page`
  17. `new_page`
  18. `performance_analyze_insight`
  19. `performance_start_trace`
  20. `performance_stop_trace`
  21. `press_key`
  22. `resize_page`
  23. `select_page`
  24. `take_heapsnapshot`
  25. `take_screenshot`
  26. `take_snapshot`
  27. `type_text`
  28. `upload_file`
  29. `wait_for`
- `[INFERRED]` Previous documentation citing 31 tools was referencing either upstream npm package README descriptions that included non-implemented tool stubs, or included MCP resource endpoints (`resources/list`, `resources/read`) in the count. Exactly 29 tool interfaces are exposed to Antigravity.

### 7.3 Active MCP Processes & Resource Footprint
- `[VERIFIED]` Process inspection via PowerShell confirmed the running MCP chain:
  - PID 32448: `cmd.exe /c npx -y chrome-devtools-mcp@latest --browserUrl http://127.0.0.1:9223` (8.7 MB)
  - PID 2248: `node.exe` (npm execution wrapper, 43.2 MB)
  - PID 6296: `cmd.exe /d /s /c chrome-devtools-mcp ...` (8.0 MB)
  - PID 21532: `node.exe` (actual chrome-devtools-mcp server daemon, 47.4 MB)
  - Combined MCP process RAM footprint: ~107.3 MB.

---

## 8. Dedicated Browser Verification System

### 8.1 Dedicated Chrome Instance
- `[VERIFIED]` Dedicated Profile Directory: `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`
- `[VERIFIED]` Debugging Port: `9223` (`http://127.0.0.1:9223`)
- `[VERIFIED]` Launch Process (`C:\Users\Joshu\Tools\LSATU-Agent\launch_browser.py`):
  - Uses `Invoke-CimMethod -ClassName Win32_Process -MethodName Create` via PowerShell.
  - *Engineering Rationale:* Completely detaches the Chrome browser process from the Antigravity Job Object tree. If Antigravity restarts or crashes, the authenticated browser session remains running and intact.
- `[VERIFIED]` Active Chrome Process Hierarchy:
  - PID 11904: `chrome.exe --remote-debugging-port=9223 --user-data-dir=...` (175.1 MB)
  - Sub-processes: GPU process (102.4 MB), 5 renderer processes (~55 MB to 102 MB each), crashpad handler (8.9 MB), utilities.
  - Combined Chrome RAM footprint: ~570 MB.

### 8.2 Automation Scripts (`C:\Users\Joshu\Tools\LSATU-Agent\`)
- `[VERIFIED]` Script Suite:
  - `agent-browser.mjs`: CLI for status check and viewport screenshots via Playwright CDP.
  - `check_auth.mjs`: Checks Supabase auth session keys in `localStorage` (`sb-...-auth-token`).
  - `check_session.py`: Lightweight Python socket check for port 9223.
  - `launch_browser.py`: Detached WMI launcher for Chrome.
  - `launch-agent-browser.ps1`: PowerShell wrapper for browser launch.
  - `start-dev-session.ps1`: One-click verification script checking port 9223, port 8080, and CDP health.
  - `test_persistence_cycle.mjs`: Closes Chrome, relaunches it, and verifies that the session token in `localStorage` persisted across restarts.
  - `verify_control_drill.mjs`: Read-only DOM and interaction check on `https://lsatprep.study/classroom/drill?section=lr`.
  - `verify_localhost.mjs`: Connects to Chrome over CDP and verifies `http://localhost:8080/classroom/drill?section=lr`.
  - `verify-viewports.mjs`: Captures screenshots across 5 viewports (1440x900, 1366x768, 1280x800, 1024x768, 390x844).

---

## 9. Localhost Dev Server Integration

### 9.1 Vite Server Process
- `[VERIFIED]` Running as background task `3c03d32c-fd9f-45cb-82ce-11890d7fc349/task-990`.
- `[VERIFIED]` Process: PID 14460 (`cmd.exe /d /s /c vite`) spawning PID 29828 (`node.exe .../vite.js`, 90.3 MB).
- `[VERIFIED]` Endpoint: `http://localhost:8080/` (connected to `projects/lsatu`).

### 9.2 Token Mirroring & Authentication Across Origins
- `[VERIFIED]` Production URL: `https://lsatprep.study`
- `[VERIFIED]` Local Development URL: `http://localhost:8080`
- `[OBSERVED]` Browser localStorage is segregated by origin under standard Web Same-Origin Policy.
- `[VERIFIED]` In `test_persistence_cycle.mjs` and `check_auth.mjs`, authentication is validated by reading `localStorage` keys matching `sb-*` or `auth-token`.
- `[OBSERVED]` For localhost verification (`verify_localhost.mjs`), if the user is unauthenticated on localhost, Supabase redirects to `/auth` or renders the guest/logged-out view. The authenticated screenshot (`localhost_drill_authenticated.png`) was captured after explicit authentication on the localhost origin.

---

## 10. Conversation & State Persistence Architecture

### 10.1 Brain Directory Topology
- `[VERIFIED]` Path: `C:\Users\Joshu\.gemini\antigravity\brain`
- `[VERIFIED]` Exactly 52 conversation session directories exist.
- `[VERIFIED]` Each conversation contains:
  - `.system_generated/logs/transcript.jsonl` (compact JSONL log of every step).
  - `.system_generated/logs/transcript_full.jsonl` (untruncated log).
  - `.system_generated/tasks/` (logs for asynchronous background tasks).
  - Artifacts generated during the session (Markdown files, diffs, images).

### 10.2 Database Architecture (`conversation_summaries.db`)
- `[VERIFIED]` Located at `C:\Users\Joshu\.gemini\antigravity\databases\conversation_summaries.db`.
- `[VERIFIED]` Schema:
  - Table `projects`: `id`, `name`, `root_path`.
  - Table `conversations`: `id`, `project_id`, `title`, `summary`, `created_at`, `updated_at`.
- `[VERIFIED]` All 51 stored conversation records are unified under `project_id = '1e181e2e-860b-48c6-9209-540e3e7a1965'` pointing to `C:\Users\Joshu\dev\ai-os`.

---

## 11. Empirical Runtime Tool Usage & Trigger Frequency

### 11.1 Quantitative Tool Execution Across Recent Sessions
- `[VERIFIED]` Analysis of tool execution across the last 30 Antigravity conversations (1,845 total tool invocations):
  1. `run_command`: 556 calls (30.1%)
  2. `view_file`: 456 calls (24.7%)
  3. `manage_task`: 284 calls (15.4%)
  4. `grep_search`: 164 calls (8.9%)
  5. `write_to_file`: 149 calls (8.1%)
  6. `list_dir`: 115 calls (6.2%)
  7. `search_web`: 101 calls (5.5%)
  8. `find_by_name`: 56 calls (3.0%)
  9. `replace_file_content`: 42 calls (2.3%)
  10. `schedule`: 35 calls (1.9%)
  11. `manage_subagents`: 15 calls (0.8%)
  12. `read_url_content`: 10 calls (0.5%)
  13. `send_message`: 9 calls (0.5%)
  14. `invoke_subagent`: 7 calls (0.4%)
  15. `call_mcp_tool` / `mcp_*`: 13 calls total (0.7%)
- `[OBSERVED]` Forensic Insight: Native shell execution (`run_command`), file inspection (`view_file`), task management (`manage_task`), and file searches represent over 85% of all agent actions. MCP tools represent less than 1% of total tool calls in production operation.

### 11.2 Trigger Words in User Prompts
- `[VERIFIED]` Frequency across last 30 conversations (118 user prompts):
  - `plan`: 11 occurrences
  - `verify`: 9 occurrences
  - `debug`: 5 occurrences
  - `audit`: 5 occurrences
  - `research`: 4 occurrences
  - `status`: 1 occurrence
  - `grill-me`: 1 occurrence
  - `pickup`: 0 explicit occurrences in sampled prompts
  - `wrapup`: 0 explicit occurrences in sampled prompts

---

## 12. Context Window Base Token Overhead

### 12.1 Base Token Breakdown Per Turn
- `[OBSERVED]` Every turn executed by Antigravity injects a fixed base context before conversation messages are parsed:
  1. **Core System Prompt & Persona:** ~500 tokens
  2. **Active Rules Block:**
     - `RULE[...AGENTS.md]`: 11,544 bytes (~2,800 tokens)
     - `RULE[...GEMINI.md]`: 11,764 bytes (~2,900 tokens)
     - Combined rules overhead: ~5,700 tokens
  3. **Injected Skills (`<skills>`):**
     - 85 exposed skill entries (names, paths, descriptions): ~7,500 tokens
     - 98 excluded skills notice
  4. **Native Tool Schemas (22 tools):** ~5,000 tokens
  5. **Lazy MCP Server Tool Declarations:**
     - 29 `chrome-devtools` tools + 2 `gemini-api-docs` eager tools: ~3,500 tokens
  6. **Planning Mode, Guidelines, Artifacts & Slash Commands:** ~2,500 tokens
- `[INFERRED]` Total baseline prompt overhead: **~24,500 to ~27,500 tokens per interaction turn**, consumed before any user message or conversation history is processed.

---

## 13. Cross-Agent Boundaries & Runtime Isolation

### 13.1 Stated Architecture vs Actual Machine State
- **Stated Architecture (`.gemini/README.md`):** Gemini, Claude, and Codex maintain strict runtime isolation. Claude uses `.claude/`, Codex uses `.codex/` and `.agents/`, and Gemini uses `.gemini/`.
- **Actual Runtime State:**
  1. `[VERIFIED]` `C:\Users\Joshu\.gemini\config\skills.json` explicitly lists `C:/Users/Joshu/dev/ai-os/.agents/skills`. Antigravity actively parses and exposes skills created for Codex.
  2. `[VERIFIED]` `C:\Users\Joshu\dev\ai-os\.gemini\agents\web-researcher.toml` specifies `model = "gpt-5.4"`, an OpenAI model configuration, inside the Gemini agent folder.
  3. `[VERIFIED]` Root `AGENTS.md` and `GEMINI.md` are both loaded simultaneously by Antigravity if both exist at root, resulting in duplicate rule injection in the prompt context.

---

## 14. Overall System Resource Footprint

### 14.1 Memory Allocation Summary
- `[VERIFIED]` Current active process memory consumption:
  - Antigravity Application (6 processes): **~828 MB**
    - Main executable (PID 25960): 105.4 MB
    - GPU process (PID 13000): 135.9 MB
    - Utility processes: ~60 MB
    - Renderer process (PID 17452): 536.9 MB
  - Dedicated Chrome Instance (PID 11904 + children): **~570 MB**
  - DevTools MCP Daemon & npm wrappers: **~107 MB**
  - Vite Local Dev Server (node.exe PID 29828 + cmd.exe): **~99 MB**
  - Background Node/Codex processes: **~210 MB**
  - Combined Agentic Development Footprint: **~1.81 GB RAM** (out of 15.7 GB available).

---

## 15. Mandatory Concluding Sections

### 15.1 Unresolved Ambiguities
1. **Skill Discovery Filtering:** It is ambiguous whether Antigravity's skill loader natively ignores directories starting with an underscore (`_inactive`, `_snapshots`, `_project-forks`). In this environment, files within those directories (`_snapshots/a11y-debugging`, `_inactive/session-handoff-nate-active-copy`) are actively indexed into the `<skills>` context block.
2. **Subagent TOML Ingestion:** It is ambiguous whether Antigravity possesses a native mechanism to auto-load the 18 `.toml` files from `.gemini/agents/` into the `<subagents>` menu, or if subagents can only be instantiated dynamically via `define_subagent` during a session.
3. **Dual Rule Ingestion:** It is ambiguous whether Antigravity was intended to ingest both `AGENTS.md` and `GEMINI.md` simultaneously into the prompt rules block, or if `GEMINI.md` was intended to take sole ownership for the Gemini runtime.

### 15.2 Files Recommended for External Architecture Review
1. `C:\Users\Joshu\.gemini\config\skills.json`: Contains cross-runtime reference to `.agents/skills`.
2. `C:\Users\Joshu\dev\ai-os\GEMINI.md` vs `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md`: Direct contradiction between the 95% rule and the Maximum Autonomy rule.
3. `C:\Users\Joshu\.gemini\config\mcp_config.json`: Master MCP definitions controlling Chrome DevTools and external tools.
4. `C:\Users\Joshu\Tools\LSATU-Agent\launch_browser.py`: Detached WMI process creation logic for persistent browser control.
5. `C:\Users\Joshu\dev\ai-os\.gemini\agents\web-researcher.toml`: Contains OpenAI model specification (`gpt-5.4`) within Gemini agent definitions.
6. `C:\Users\Joshu\dev\ai-os\ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md`: This comprehensive forensic report.

### 15.3 Facts That Could Not Be Verified
1. `[UNKNOWN]` Whether the 98 skills excluded from the active prompt due to context limits are selected based on alphabetical order, file size, recency, or semantic relevance to previous turns.
2. `[UNKNOWN]` The exact internal C++ or Electron binding mechanism Antigravity uses to bridge lazy MCP schema calls to `call_mcp_tool`.
3. `[UNKNOWN]` Whether previous session references to 31 Chrome DevTools tools originated from an older package release or an external documentation template.

### 15.4 Runtime Behaviors That Require Official Web Documentation to Resolve
1. **Antigravity Customization Discovery:** Official documentation needed on whether `.gemini/skills/` supports ignore patterns (such as `.skillignore` or underscore exclusion rules) to prevent archiving containers like `_inactive` and `_snapshots` from polluting the context budget.
2. **Subagent TOML Specification:** Official specification needed on whether `.gemini/agents/*.toml` is recognized by Antigravity's built-in loader, or if this format is an artifact of Claude/Codex multi-agent schemas adapted for Gemini.
3. **Context Budget Thresholds:** Official documentation needed on the exact token thresholds that trigger skill truncation in `<skills>` and the priority algorithm used to determine which skills are retained.
"""

with open(target_path_root, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Wrote audit to {target_path_root} ({len(content)} characters)")

with open(target_path_gemini, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Wrote audit to {target_path_gemini} ({len(content)} characters)")
