# AIOS WAVE 5 RESULT: ANTIGRAVITY MCP CLEANUP, PINNING, AND TOOL AUDIT

- **Wave Status**: **PASS**
- **Timestamp**: 2026-09-20T08:16:00-04:00
- **Execution Scope**: Wave 5 (Antigravity MCP Layer Cleanup, Pinning, and Tool Audit)
- **Primary Report Path**: [`C:\Users\Joshu\dev\ai-os\AIOS_WAVE_5_RESULT.md`](file:///C:/Users/Joshu/dev/ai-os/AIOS_WAVE_5_RESULT.md)
- **Report Mirror**: [`C:\Users\Joshu\dev\ai-os\.gemini\AIOS_WAVE_5_RESULT.md`](file:///C:/Users/Joshu/dev/ai-os/.gemini/AIOS_WAVE_5_RESULT.md)
- **Machine**: `J`
- **User**: `Joshu`
- **Antigravity Version**: `2.15.0`
- **Language Server Binary**: `C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe` (163,972,608 bytes)
- **Protected File Baseline Integrity**: **3,241 / 3,241 files verified 100% byte-identical**
- **Git State**: Clean and Preserved (Zero application source code modifications)

---

## 1. EXECUTIVE SUMMARY AND PASS/FAIL VERDICT

**VERDICT: PASS**

Wave 5 has completed all required safety audits, schema verifications, package pinning, and non-interference validations without touching Codex, Claude, application source code, Git state, or browser scripts.

Key Achievements:
1. **MCP Configuration Backup**: Global configuration `C:\Users\Joshu\.gemini\config\mcp_config.json` backed up to `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\mcp_config_pre_wave5.json` before any modification (SHA-256: `F293F979FCC4D0D2752ED2AAFABBBA9F206C24B396EDBDD9D5509C602E3A6691`).
2. **Deterministic Package Pinning**: Pinned `chrome-devtools-mcp` from floating tag `@latest` to exact release `@1.9.0` in `mcp_config.json`, preserving `--browserUrl http://127.0.0.1:9223` and arguments. The pinned binary was executed and returned version `1.9.0` with exit code 0.
3. **Comprehensive MCP Server Inventory**: Audited all 4 global MCP servers (`chrome-devtools`, `notebooks`, `visualization`, `data-agent-kit`) plus plugin-bundled eager servers (`gemini-api_gemini-api-docs`), documenting package executables, tool counts, mutability, and external cloud reach.
4. **Antigravity 2.15.0 MCP Schema Verification**: Reverse-engineered `language_server.exe` to document Go struct `McpServerSpec`, verifying support for `disabledTools`, `enabledTools`, command parameters, global configuration scoping (`~/.gemini/config/mcp_config.json`), plugin scoping (`plugins/<name>/mcp_config.json`), and the absence of workspace-level MCP overrides.
5. **Subagent MCP Security Analysis**: Evaluated dynamic subagents created with `enable_mcp_tools: true`. Confirmed that Antigravity 2.15.0 exposes all globally active MCP servers to any subagent with MCP enabled, because `define_subagent` lacks a per-server whitelist parameter. Documented prompt-level containment boundaries.
6. **Conservative Scope Preserved**: Zero plugins uninstalled, zero DataCloud components deleted, zero browser automation scripts touched.
7. **Protected File Integrity**: Re-verified all 3,241 protected baseline files across 6 manifests (0 missing, 0 mismatches). Core instruction files `AGENTS.md` and `CLAUDE.md` remain 100% byte-identical.
8. **Git State Preserved**: Zero staging, zero commits, zero pushes. Working tree state matches pre-wave baseline.

---

## 2. PRE-MIGRATION BACKUP AND CONFIGURATION HASHES

### Configuration File: `C:\Users\Joshu\.gemini\config\mcp_config.json`

| Metric | Pre-Wave 5 Value | Post-Wave 5 Value |
|---|---|---|
| **Backup Path** | `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\mcp_config_pre_wave5.json` | N/A |
| **SHA-256 Checksum** | `F293F979FCC4D0D2752ED2AAFABBBA9F206C24B396EDBDD9D5509C602E3A6691` | `51FEACA6AC4B5FD0055168FC05F954525053E239781E351BEF277C62057EAF5E` |
| **File Size** | 984 bytes | 983 bytes |
| **Total Lines** | 34 lines | 34 lines |
| **JSON Parse Validity** | Valid | Valid |
| **Configured Servers** | 4 servers | 4 servers |

### Pre-Wave 5 Configuration Content:
```json
{
  "mcpServers": {
    "notebooks": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "notebooks-antigravityide"
      ]
    },
    "visualization": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "visualization-antigravityide"
      ]
    },
    "data-agent-kit": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "dataAgentKit-antigravityide"
      ]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browserUrl",
        "http://127.0.0.1:9223"
      ]
    }
  }
}
```

### Post-Wave 5 Configuration Content:
```json
{
  "mcpServers": {
    "notebooks": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "notebooks-antigravityide"
      ]
    },
    "visualization": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "visualization-antigravityide"
      ]
    },
    "data-agent-kit": {
      "command": "node",
      "args": [
        "c:\\Users\\Joshu\\.antigravity-ide\\extensions\\googlecloudtools.datacloud-0.11.0-universal\\mcp_servers\\cli\\mcp_proxy_bundle.js",
        "dataAgentKit-antigravityide"
      ]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@1.9.0",
        "--browserUrl",
        "http://127.0.0.1:9223"
      ]
    }
  }
}
```

---

## 3. FULL MCP SERVER INVENTORY

Antigravity 2.15.0 currently registers 4 servers via `mcp_config.json` plus 1 eager server via enabled plugins:

| Server Identifier | Source / Package | Resolved Version | Tool Count | Mutability Classification | External / Cloud Reach | Redundancy Assessment |
|---|---|---|---|---|---|---|
| `chrome-devtools` | `npx -y chrome-devtools-mcp@1.9.0` | 1.9.0 | 29 | Mixed (Inspection: read-only; Interaction: DOM/tab mutating) | Local browser tab only (`127.0.0.1:9223`) | None. Critical for browser verification. |
| `notebooks` | Node proxy (`datacloud-0.11.0-universal`) | 0.11.0 | 11 | Mutating (creates/edits `.ipynb` files, executes code) | Local workspace files | Used for Jupyter notebook workflows. |
| `visualization` | Node proxy (`datacloud-0.11.0-universal`) | 0.11.0 | 1 | Mutating (creates chart artifacts) | Local workspace artifacts | Used for chart generation. |
| `data-agent-kit` | Node proxy (`datacloud-0.11.0-universal`) | 0.11.0 | 4 | Read-only (editor context, GCP connections, templates) | GCP metadata if authenticated | Connected to Google Cloud DataCloud plugin. |
| `gemini-api_gemini-api-docs` | Built-in / Plugin Eager MCP | Internal | 2 | Read-only (doc search, doc retrieval) | Upstream Google doc endpoint | Official documentation reference. |

### Detailed Server Breakdown

#### 1. `chrome-devtools` (29 tools)
- **Command**: `npx -y chrome-devtools-mcp@1.9.0 --browserUrl http://127.0.0.1:9223`
- **Tool List**: `click`, `close_page`, `drag`, `emulate`, `evaluate_script`, `fill`, `fill_form`, `get_console_message`, `get_network_request`, `handle_dialog`, `hover`, `lighthouse_audit`, `list_console_messages`, `list_network_requests`, `list_pages`, `navigate_page`, `new_page`, `performance_analyze_insight`, `performance_start_trace`, `performance_stop_trace`, `press_key`, `resize_page`, `select_page`, `take_heapsnapshot`, `take_screenshot`, `take_snapshot`, `type_text`, `upload_file`, `wait_for`.
- **Classification**:
  - Read-Only Inspection: `list_pages`, `take_screenshot`, `take_snapshot`, `list_console_messages`, `get_console_message`, `list_network_requests`, `get_network_request`, `lighthouse_audit`.
  - DOM/Tab Mutating: `click`, `fill`, `fill_form`, `evaluate_script`, `navigate_page`, `new_page`, `close_page`, `press_key`, `type_text`, `hover`, `drag`.
- **Risk Profile**: High utility for UI verification. Interaction tools mutate web application state in the connected browser profile.

#### 2. `notebooks` (11 tools)
- **Command**: Node proxy to `mcp_proxy_bundle.js notebooks-antigravityide`
- **Tool List**: `create_notebook`, `delete_cell`, `execute_cell`, `get_notebook_context`, `insert_code_cell`, `insert_markdown_cell`, `move_cell`, `read_cell_output`, `read_notebook`, `run_cell`, `update_cell`.
- **Classification**: Mutating. Modifies local `.ipynb` files and executes code in Jupyter kernels.
- **Risk Profile**: Safe for notebook data science; inappropriate for read-only reviewers.

#### 3. `visualization` (1 tool)
- **Command**: Node proxy to `mcp_proxy_bundle.js visualization-antigravityide`
- **Tool List**: `render_chart`.
- **Classification**: Mutating. Writes visual chart artifacts to disk.
- **Risk Profile**: Low risk, localized output generation.

#### 4. `data-agent-kit` (4 tools)
- **Command**: Node proxy to `mcp_proxy_bundle.js dataAgentKit-antigravityide`
- **Tool List**: `get_active_editor_context`, `get_active_gcp_connection`, `list_resource_templates`, `read_resource`.
- **Classification**: Read-only context retrieval.
- **Risk Profile**: Low risk. Reads current IDE and GCP telemetry.

#### 5. `gemini-api_gemini-api-docs` (2 tools)
- **Command**: Built-in plugin server
- **Tool List**: `gemini_search_docs`, `gemini_get_doc`.
- **Classification**: Read-only documentation retrieval.
- **Risk Profile**: Zero risk.

---

## 4. MCP CONFIGURATION SCHEMA IN ANTIGRAVITY 2.15.0

Reverse engineering of `language_server.exe` identified the Go structures governing MCP:

```go
type McpServerSpec struct {
    Command       string            `json:"command"`
    Args          []string          `json:"args"`
    Env           map[string]string `json:"env"`
    Cwd           string            `json:"cwd"`
    Disabled      bool              `json:"disabled"`
    DisabledTools []string          `json:"disabledTools"`
    EnabledTools  []string          `json:"enabledTools"`
    ServerURL     string            `json:"serverUrl"`
    Headers       map[string]string `json:"headers"`
    Timeout       int               `json:"timeout"`
}
```

### Key Findings on Runtime Behavior:
1. **Per-Server Tool Filtering**: The runtime natively supports `disabledTools` and `enabledTools` arrays inside each server definition in `mcp_config.json`. This allows globally suppressing individual tools on any MCP server.
2. **Configuration Scoping**:
   - Supported: `~/.gemini/config/mcp_config.json` (global configuration across all sessions).
   - Supported: `plugins/<plugin_name>/mcp_config.json` (active when the specific plugin is enabled).
   - **Unsupported**: Project-scoped `.gemini/mcp_config.json` or workspace-specific MCP configuration. Antigravity 2.15.0 does not search workspace trees for MCP configs.
3. **Reload Semantics**:
   - The language server monitors configuration files via file system watchers (`fsnotify`).
   - Active MCP server processes are managed during session initialization. Changes to `mcp_config.json` take effect immediately on next tool dispatch or when reloading the workspace window.

---

## 5. DYNAMIC BROWSER VERIFIER MCP SAFETY ANALYSIS

In Wave 4B, the architecture locked dynamic read-only specialists instantiated via `define_subagent`.

### Subagent MCP Tool Exposure
When defining a subagent with `enable_mcp_tools: true`:
- The Go language server provides the subagent with the `call_mcp_tool` dispatcher.
- The subagent gains the ability to call **all** active global MCP servers (`chrome-devtools`, `notebooks`, `visualization`, `data-agent-kit`).
- Antigravity 2.15.0 does **not** support a per-subagent server whitelist parameter on `define_subagent` (the schema accepts only boolean `enable_mcp_tools`).

### Potential Risk Vectors:
1. `notebooks`: A browser verifier could theoretically create or execute Jupyter cells.
2. `visualization`: A browser verifier could generate chart artifacts.
3. `data-agent-kit`: A browser verifier could query GCP telemetry.

### Mitigations in Place:
- **Mechanical Workspace Isolation**: Dynamic specialists set `enable_write_tools: false` and `enable_subagent_tools: false`, preventing file creation, replacement, or shell execution.
- **Strict Prompt-Level Scoping**: The system prompt for `browser_verifier` explicitly restricts tool calls:
  `"Only call Chrome DevTools MCP tools (call_mcp_tool with ServerName 'chrome-devtools'). Do not invoke notebooks, visualization, or data-agent-kit tools."`
- **Code Reviewer Isolation**: `code_reviewer` strictly sets `enable_mcp_tools: false`, completely removing `call_mcp_tool` and eliminating all MCP risk vectors.

---

## 6. CHROME DEVTOOLS VERIFICATION POST-PIN

### Pinning Verification
- **Target Version**: `chrome-devtools-mcp@1.9.0`
- **Execution Test**: `npx -y chrome-devtools-mcp@1.9.0 --version` returned `1.9.0` (Exit code: 0).
- **CLI Options Test**: `npx -y chrome-devtools-mcp@1.9.0 --help` executed cleanly (Exit code: 0).
- **Tool Schema Stability**: Verified that tool count and declarations match the 29 tools expected by the system prompt.

### Port 9223 Connectivity Check
- **Command**: `Test-NetConnection -ComputerName 127.0.0.1 -Port 9223`
- **Result**: `TcpTestSucceeded: False`
- **Operational Context**: Chrome is not currently running with `--remote-debugging-port=9223`. As required by Step 5, the MCP configuration and tool declarations are validated independently of whether a live browser window is currently open. When Joshua launches the automated browser profile via `launch_lsatu_browser.py`, port 9223 will accept incoming CDP connections.

---

## 7. CONSERVATIVE SCOPE ENFORCEMENT

- **No Plugin Uninstalls**: No plugins were uninstalled or disabled.
- **No DataCloud Deletions**: No files in `.antigravity-ide/extensions/googlecloudtools.datacloud*` were modified or removed.
- **No Browser Script Modifications**: Shared host automation files in `C:\Users\Joshu\Tools\LSATU-Agent\` remain untouched.
- **No Configuration Pollution**: No workspace-level MCP configs or `.agents` files were created.

---

## 8. NON-INTERFERENCE VALIDATION

Cryptographic SHA-256 verification of all 3,241 protected baseline files across the 6 manifests:

| Manifest File | Scope | Tracked Files | Verified Identical | Failures |
|---|---|---|---|---|
| `protected_aios_agents_manifest.json` | Root `.agents/**` | 27 | 27 | 0 |
| `protected_aios_claude_manifest.json` | Root `.claude/**` | 14 | 14 | 0 |
| `protected_lsatu_agents_manifest.json` | LSAT U `.agents/**` | 493 | 493 | 0 |
| `protected_lsatu_claude_manifest.json` | LSAT U `.claude/**` | 475 | 475 | 0 |
| `protected_skills_claude_manifest.json` | `skills/claude/**` | 1,178 | 1,178 | 0 |
| `protected_skills_codex_manifest.json` | `skills/codex/**` | 1,054 | 1,054 | 0 |
| **Total Protected Files** | **All Protected Runtimes** | **3,241** | **3,241** | **0** |

### Core Protected Files:
- `C:\Users\Joshu\dev\ai-os\AGENTS.md`: SHA-256 `77b16d6cda2b59e55076e6ec37481da13ba9f0e768939f7a6df560f0f0245326` (Identical)
- `C:\Users\Joshu\dev\ai-os\CLAUDE.md`: SHA-256 `9b8e32a2c648a2ef99f8b0c17a7a28d5cc79b1dce200f6a52d25cb31cb777665` (Identical)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md`: SHA-256 `12c1a22f592c68a4064b6eab603d419b87a473a85abf6573e60ae5203239c5e5` (Identical)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md`: SHA-256 `1ee7aedcfcc75faf2b67163b6edb172d05e7224e22000edb7020ab237fd8937c` (Identical)
- `C:\Users\Joshu\.gemini\config\skills.json`: Verified intact (30-skill whitelist from Wave 3B).
- `C:\Users\Joshu\dev\ai-os\GEMINI.md`: Verified intact (Wave 2 control plane).

---

## 9. GIT STATE BEFORE AND AFTER

Zero Git staging, committing, or resetting actions were performed.

### Outer Repository (`C:\Users\Joshu\dev\ai-os`):
- **Active Branch**: `main` (Unchanged)
- **HEAD Commit**: `3b86f2cf0ef5ce3276b0c3c66f35b1bc8e5529a2` (Unchanged)
- **Staged Files**: 0
- **Unstaged Modifications**: 1 (`GEMINI.md`, modified in Wave 2)
- **Untracked Files**: Untracked scratch files and wave reports only
- **Application Source Code**: 0 files touched

### Inner Repository (`C:\Users\Joshu\dev\ai-os\projects\lsatu`):
- **Active Branch**: `feat/calendar-strip-deeplink` (Unchanged)
- **HEAD Commit**: `a071951e3ecca0bf81c477fa54e67663afcfc308` (Unchanged)
- **Staged Files**: 0
- **Unstaged Files**: 35 (34 baseline unstaged modifications + 1 `GEMINI.md` from Wave 2)
- **Untracked Files**: 42 (Unchanged from baseline)
- **Total Porcelain Lines**: 77 (Matches baseline)
- **Application Source Code**: 0 files touched

---

## 10. UNRESOLVED LIMITATIONS

1. **Subagent MCP Server Whitelisting**: Antigravity 2.15.0 provides only a coarse boolean (`enable_mcp_tools`) at subagent creation. Fine-grained restriction to `chrome-devtools` relies on prompt instructions.
2. **Global MCP Scoping**: Antigravity does not support workspace-level MCP configs. All servers defined in `mcp_config.json` are globally visible across all workspaces.

---

## 11. HARD STOP ENFORCEMENT

- **Wave 6 has NOT begun.**
- Zero cross-runtime changes made.
- Zero Git lifecycle commands executed.
- Ready for external architect review.
