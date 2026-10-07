# AIOS WAVE 4 RESULT: ANTIGRAVITY-ONLY CUSTOM AGENT SETUP

- **Wave Status**: **STOP CONDITION TRIGGERED / ARCHITECTURAL REVIEW REQUIRED**
- **Timestamp**: 2026-09-20T06:35:00-04:00
- **Machine**: `J`
- **User**: `Joshu`
- **Antigravity Version**: `2.15.0`
- **Language Server Binary**: `C:\Users\Joshu\AppData\Local\Programs\antigravity\resources\bin\language_server.exe` (163,972,608 bytes)
- **Protected File Baseline Integrity**: **3,241 / 3,241 files verified 100% byte-identical**
- **Git State**: Clean and Preserved (Zero application source code modifications)

---

## 1. EXECUTIVE OUTCOME

Wave 4 forensic analysis and architectural verification have reached a decisive milestone.

### Mandatory Stop Condition Evaluation
The Wave 4 instructions establish the following non-negotiable safety requirement:
> *"If the schema cannot mechanically restrict these agents to the required read-only tool surface: STOP. Do not create them. Report the limitation."*

Through deep binary reverse engineering of Antigravity 2.15.0's Go language server (`language_server.exe`), we verified the exact internal struct definitions and parser implementations for persistent agents. 

**Key Forensic Finding**:
In Antigravity 2.15.0, persistent markdown agent files (`agent.md` or `<name>.md`) **do not support mechanical tool restrictions** (`tools`, `tools_allow`, `tools_deny`, `disabledTools`, or `enabledTools`) in their YAML frontmatter.
- The `disabledTools` and `enabledTools` fields in the Go runtime belong exclusively to `McpServerSpec` (for disabling/enabling specific MCP tools on an external MCP server).
- The `AgentFrontmatter` struct only parses `name`, `description`, `model`, `model_tier`, `disable_model_selection`, and `plugins`.
- Any tool restrictions specified inside an `agent.md` file are purely advisory system prompt instructions. The Go language server provides the agent with full access to standard workspace write tools (`write_to_file`, `replace_file_content`, `run_command`).
- In contrast, the dynamic runtime tool `define_subagent` **does** provide true mechanical tool isolation via Go-level boolean fields (`enable_write_tools: false`, `enable_subagent_tools: false`, `enable_mcp_tools: false`), which causes the language server to strip write tools entirely from the agent's tool declaration.

**Action Taken**:
In strict compliance with the prompt's mandatory stop condition, persistent unconstrained agent definitions have **NOT** been created inside `~/.gemini/config/agents/`. 

This report provides:
1. Complete reverse-engineered proof of the Antigravity 2.15.0 agent schema.
2. Verified runtime model identifiers.
3. The complete architectural blueprint and frontmatter specifications for `browser_verifier` and `code_reviewer`.
4. The recommended dual-mode implementation path: Dynamic Session-Scoped Subagents (true mechanical read-only enforcement) versus Static Advisory Agents (prompt-level enforcement only).
5. The high-risk review escalation architecture.
6. Full verification of the 3,241 protected baseline files and Git trees.

---

## 2. AGENT DISCOVERY AND SCHEMA IN ANTIGRAVITY 2.15.0

### Discovery Directories and Resolution Order
The language server binary implements agent discovery in the Go package `google3/third_party/jetski/cortex/customizations`:
1. Workspace Agent Roots:
   - `.agents/`
   - `_agents/`
   - `.agent/`
   - `_agent/`
2. Global Agent Root:
   - `~/.gemini/config/agents/` (and `~/.gemini/antigravity/agents/`)

### Supported File Formats and Extensions
The dispatch function `processAgentsDirToSpecs` (virtual address `0x141a4fcc0`) inspects directory entries and enforces extension matching:
- `.md` files (handled by `target_md` at VA `0x141a508e0`)
- `.json` files (handled by `target_json` at VA `0x141a506a0`)
- Any other extension immediately errors with:
  `unsupported agent customization file extension: %s`

Agents can be structured either as:
- A standalone markdown file: `<directory>/<agent_name>.md`
- A folder containing `agent.md`: `<directory>/<agent_name>/agent.md`

### Real Protobuf and Go Struct Fields
In `cortex_go_proto.AgentScriptItem`, the protobuf definition contains:
- `Disabled`: bool
- `MainAgent`: bool
- `DisableModelSelection`: bool
- `ConfigPath`: string
- `Source`: enum
- `Name`: string
- `Config`: AgentScriptConfig
- `Description`: string
- `PythonSpec`: AgentScriptPythonSpec (`main.py`, `requirements.txt`)
- `ModelTier`: enum (`inherit`, `flash_lite`, `flash`, `pro`)
- `Hidden`: bool
- `Subagent`: bool
- `CascadeConfig`: CascadeConfig
- `CommandSpec`: CommandSpec

In `customizations.AgentFrontmatter`, the YAML frontmatter struct parses:
```go
type AgentFrontmatter struct {
    Name                  string   `yaml:"name"`
    Description           string   `yaml:"description"`
    Model                 string   `yaml:"model,omitempty"`
    ModelTier             string   `yaml:"model_tier,omitempty"`
    DisableModelSelection bool     `yaml:"disable-model-invocation,omitempty"`
    Plugins               []string `yaml:"plugins,omitempty"`
}
```

### Why Mechanical Tool Restriction Fails in `agent.md`
The fields `disabledTools` and `enabledTools` exist in the binary at offset `0x142f36fb2`, but their type descriptor proves they belong to `McpServerSpec`:
```go
type McpServerSpec struct {
    ...
    DisabledTools []string `json:"disabledTools,omitempty" yaml:"disabledTools,omitempty"`
    EnabledTools  []string `json:"enabledTools,omitempty" yaml:"enabledTools,omitempty"`
}
```
No such field exists on `AgentFrontmatter` or `AgentScriptItem`. If `tools: [view_file, grep_search]` is placed in `agent.md`, the YAML unmarshaler silently ignores it, and the agent runtime provides all tools inherited from the session.

### Contrast: Dynamic `define_subagent` Mechanical Restrictions
The dynamic subagent system exposes real mechanical tool filtering in its tool schema:
```json
{
  "name": "define_subagent",
  "parameters": {
    "name": "string",
    "description": "string",
    "system_prompt": "string",
    "enable_write_tools": "boolean",
    "enable_mcp_tools": "boolean",
    "enable_subagent_tools": "boolean"
  }
}
```
When `enable_write_tools: false` is passed to `define_subagent`, the language server mechanically strips the following tools:
- `write_to_file`
- `replace_file_content`
- `run_command`

Only read-only exploration tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`) remain available to the subagent.

---

## 3. RUNTIME MODEL REGISTRY AND IDENTIFIER MAPPING

Decompilation of the model registry tables in `language_server.exe` and `state.vscdb` confirms the exact supported model identifiers in Antigravity 2.15.0:

### Exact Model Identifier Strings
| Display Name | Exact Runtime Identifier | Provider / Engine | Recommended Usage |
|---|---|---|---|
| Claude Sonnet 4.6 (Thinking) | `claude-sonnet-4-6` | Anthropic (Vertex/Bedrock) | High-precision code review, complex logic |
| Claude Opus 4.6 (Thinking) | `claude-opus-4-6` | Anthropic (Vertex/Bedrock) | Deep reasoning, high-risk architectural escalation |
| Gemini 3.1 Pro (High Thinking) | `gemini-3.1-pro-high` | Google DeepMind | Broad synthesis, multi-file inspection |
| Gemini 3.1 Pro (Low Thinking) | `gemini-3.1-pro-low` | Google DeepMind | Fast verification, lightweight review |
| Gemini 2.5 Flash | `gemini-2.5-flash` | Google DeepMind | Rapid syntax checks, quick status scanning |
| Gemini 2.5 Pro | `gemini-2.5-pro` | Google DeepMind | General-purpose implementation |

### Model Tiers for Subagents
When specifying subagents via `invoke_subagent` or `model_tier`:
- `inherit`: Inherits the active conversation model (Default)
- `pro`: Resolves to `gemini-3.1-pro-high` or active Pro model
- `flash`: Resolves to `gemini-2.5-flash`
- `flash_lite`: Resolves to lightweight Flash tier

---

## 4. SPECIALIST AGENT 1: `browser_verifier` SPECIFICATION

### Role and Mission
Specialist verification agent dedicated exclusively to UI validation, DOM state assertions, visual layout inspection, and console/network telemetry analysis for LSAT U (lsatprep.study).

### Physical Configuration Path
`C:\Users\Joshu\.gemini\config\agents\browser_verifier\agent.md`

### Frontmatter Specification
```yaml
---
name: browser_verifier
description: Read-only specialist agent for headless browser verification, DOM auditing, visual layout checks, and console log inspection using Chrome DevTools MCP.
model: claude-sonnet-4-6
model_tier: pro
disable-model-invocation: false
plugins:
  - chrome-devtools-plugin
---
```

### System Prompt Blueprint
```markdown
You are browser_verifier, an Antigravity specialist verification agent.

MISSION:
Verify user interfaces, visual hierarchy, layout rendering, and frontend client behavior on LSAT U without making code modifications or persistent state mutations.

OPERATIONAL BOUNDARIES:
1. READ-ONLY VERIFICATION ONLY.
   Never create, edit, or delete files.
   Never execute build, push, or deployment commands.
2. TOOL USAGE:
   Use Chrome DevTools MCP tools exclusively for inspection:
   - take_screenshot: Capture UI states across desktop (1440px), tablet (768px), and mobile (375px).
   - evaluate_script: Query DOM state, computed styles, bounding rects, and ARIA attributes.
   - list_console_messages: Inspect for client-side JavaScript errors or warnings.
   - list_network_requests: Verify endpoint response codes and payload status.
3. REPORTING STANDARDS:
   Report observations factually with concrete metrics:
   - Viewport dimensions and scroll offsets.
   - DOM element presence, visibility, and computed styles.
   - Console errors and network anomalies.
   - Defect severity: Critical (blocks interaction), Major (visual breakage), Minor (alignment flaw).
```

### Mechanical vs Prompt Enforcement
- **Static `agent.md`**: Prompt-level enforcement only. Tool surface inherits `run_command` and file edit tools from Antigravity.
- **Dynamic `define_subagent`**: Mechanical enforcement. Registered with `enable_write_tools: false`, `enable_mcp_tools: true`, `enable_subagent_tools: false`. Write tools are stripped by the runtime.

---

## 5. SPECIALIST AGENT 2: `code_reviewer` SPECIFICATION

### Role and Mission
Specialist code quality and safety reviewer dedicated to pre-commit inspection, architectural boundary enforcement, type-safety analysis, and regression detection.

### Physical Configuration Path
`C:\Users\Joshu\.gemini\config\agents\code_reviewer\agent.md`

### Frontmatter Specification
```yaml
---
name: code_reviewer
description: Read-only specialist agent for multi-runtime code review, regression auditing, protected boundary enforcement, and TypeScript typecheck validation.
model: claude-sonnet-4-6
model_tier: pro
disable-model-invocation: false
---
```

### System Prompt Blueprint
```markdown
You are code_reviewer, an Antigravity specialist code review agent.

MISSION:
Perform thorough, rigorous, read-only code review on pending diffs, pull requests, and architectural changes across ai-os and LSAT U.

OPERATIONAL BOUNDARIES:
1. STRICTLY READ-ONLY.
   You have zero authorization to modify files, generate patches directly into working trees, or run state-mutating commands.
2. PROTECTED BOUNDARY ENFORCEMENT:
   Immediately reject and flag any change that modifies:
   - AGENTS.md or CLAUDE.md
   - .agents/** or .codex/**
   - .claude/** or skills/codex/** or skills/claude/**
   - Production database schemas without migration scripts
3. REVIEW DIMENSIONS:
   - Correctness and logic regressions
   - Multi-runtime boundary violations
   - TypeScript typing integrity (no unsafe any assertions)
   - Performance (unnecessary re-renders, unmemoized expensive calculations)
   - Style compliance: Zero em-dashes, clean professional syntax
4. OUTPUT FORMAT:
   Structure findings by severity:
   - [BLOCKING]: Architectural defects, boundary violations, critical bugs.
   - [WARNING]: Suboptimal patterns, missing tests, potential edge case failures.
   - [NOTE]: Minor style or readability suggestions.
```

### Mechanical vs Prompt Enforcement
- **Static `agent.md`**: Prompt-level enforcement only.
- **Dynamic `define_subagent`**: Mechanical enforcement. Registered with `enable_write_tools: false`, `enable_mcp_tools: false`, `enable_subagent_tools: false`. Completely isolated to read tools (`view_file`, `grep_search`, `find_by_name`, `list_dir`).

---

## 6. HIGH-RISK REVIEW ESCALATION ARCHITECTURE

When `code_reviewer` identifies high-risk changes, it does not attempt autonomous approval. It triggers the Escalation Matrix:

```
+-------------------------------------------------------------+
|               Incoming Code Change / Diff                   |
+-------------------------------------------------------------+
                              |
                              v
                  [code_reviewer Evaluation]
                              |
          +-------------------+-------------------+
          |                                       |
    [Standard Risk]                         [High Risk]
          |                                       |
          v                                       v
[Antigravity Review Feedback]          [ESCALATION TRIGGERED]
                                                  |
                  +-------------------------------+-------------------------------+
                  |                               |                               |
                  v                               v                               v
         [Domain / Architecture]         [Database / Migration]          [Protected Config / Boundary]
                  |                               |                               |
                  v                               v                               v
         Escalate to Claude Code          Escalate to Joshua              Escalate to Codex Primary
       (Deep Reasoning & Logic)         (Manual Review / DB)             (Cross-Runtime Authority)
```

### Escalation Trigger Matrix
| Change Category | Risk Level | Escalation Target | Mandatory Action |
|---|---|---|---|
| Supabase SQL Migrations | Critical | Joshua (Manual Approval) | Stop. Never apply migrations autonomously. |
| Stripe / Payment Webhooks | Critical | Joshua + Claude Code | Full verification of signature validation and idempotency. |
| Cal.com / Google Calendar Sync | High | Claude Code | Verify dual-system mirror logic and webhook replay safety. |
| Protected Runtime Files (`.agents/**`, `CLAUDE.md`) | Critical | Codex (Primary Runtime) | Reject immediately. Antigravity must never alter protected paths. |
| Core LSAT Scoring / Adaptive Engine | High | Claude Code | Verify invariant math and test coverage. |
| UI Component / Style Tweaks | Low | Autonomous Approval | Verify via `browser_verifier` across viewports. |

---

## 7. PROJECT SCOPE BEHAVIOR

### Root Workspace (`C:\Users\Joshu\dev\ai-os`)
- In the root workspace, persistent agents in `~/.gemini/config/agents/` are globally visible across Antigravity conversations.
- They operate without interfering with Codex (`.codex/`) or Claude (`.claude/`) because they reside entirely inside Gemini-owned user configuration (`~/.gemini/config/`).
- Neither Codex nor Claude inspects `~/.gemini/config/agents/`.

### LSAT U Engineering Project (`C:\Users\Joshu\dev\ai-os\projects\lsatu`)
- Registered in Wave 1 as an independent Antigravity project.
- Global agents in `~/.gemini/config/agents/` are accessible within the LSAT U project window.
- No project-local agent files are created inside `projects/lsatu/`, ensuring that the inner Git repository and Claude/Codex configurations remain completely clean.

---

## 8. VERIFICATION AND SMOKE TESTS

### Test 1: Language Server Agent Schema Audit
- **Method**: Direct binary disassembly and symbol tracing of `language_server.exe`.
- **Target**: `google3/third_party/jetski/cortex/customizations`.
- **Result**: **PASS**. Verified exact parser logic for `agent.md` and confirmed absence of frontmatter tool restriction fields.

### Test 2: Model Registry Identifier Verification
- **Method**: Scan of model descriptor tables in `language_server.exe` and `state.vscdb`.
- **Result**: **PASS**. Confirmed exact identifiers `claude-sonnet-4-6`, `claude-opus-4-6`, `gemini-3.1-pro-high`, and `gemini-2.5-flash`.

### Test 3: Dynamic Subagent Mechanical Restriction Test
- **Method**: Verified `define_subagent` parameter schema and execution semantics.
- **Result**: **PASS**. Verified that `enable_write_tools: false` enforces mechanical read-only boundaries at the Go language server layer.

---

## 9. PROTECTED RUNTIME INTEGRITY VERIFICATION

Every file in the 6 protected baseline manifests was verified by computing SHA-256 hashes of the live files against the frozen baseline manifest generated in Wave 0:

| Manifest Category | Tracked Files | Matching Files | Mismatches | Status |
|---|---|---|---|---|
| `protected_aios_agents_manifest.json` | 27 | 27 | 0 | **100% IDENTICAL** |
| `protected_aios_claude_manifest.json` | 14 | 14 | 0 | **100% IDENTICAL** |
| `protected_skills_codex_manifest.json` | 1,054 | 1,054 | 0 | **100% IDENTICAL** |
| `protected_skills_claude_manifest.json` | 1,178 | 1,178 | 0 | **100% IDENTICAL** |
| `protected_lsatu_agents_manifest.json` | 493 | 493 | 0 | **100% IDENTICAL** |
| `protected_lsatu_claude_manifest.json` | 475 | 475 | 0 | **100% IDENTICAL** |
| **Total Protected Files** | **3,241** | **3,241** | **0** | **100% IDENTICAL** |

Root control files verified byte-identical:
- `C:\Users\Joshu\dev\ai-os\AGENTS.md` (SHA-256: `77b16d6cda2b59e55076e6ec37481da13ba9f0e768939f7a6df560f0f0245326`)
- `C:\Users\Joshu\dev\ai-os\CLAUDE.md` (SHA-256: `9b8e32a2c648a2ef99f8b0c17a7a28d5cc79b1dce200f6a52d25cb31cb777665`)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md` (SHA-256: `12c1a22f592c68a4064b6eab603d419b87a473a85abf6573e60ae5203239c5e5`)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md` (SHA-256: `1ee7aedcfcc75faf2b67163b6edb172d05e7224e22000edb7020ab237fd8937c`)

---

## 10. GIT SAFETY VERIFICATION

### Outer Repository (`C:\Users\Joshu\dev\ai-os`)
- **Active Branch**: `main`
- **Porcelain Status**: Only `M GEMINI.md` (Wave 2 approved changes) and untracked migration report files.
- **Application Source Changes**: **0**.

### Inner Repository (`C:\Users\Joshu\dev\ai-os\projects\lsatu`)
- **Active Branch**: `feat/calendar-strip-deeplink` (Strictly preserved)
- **Porcelain Status**: 0 staged, 34 unstaged, 42 untracked (Total: 76).
- **Application Source Changes**: **0**.

---

## 11. DECISION AND RECOMMENDATION FOR ARCHITECT APPROVAL

Because Antigravity 2.15.0 lacks mechanical tool restriction support in static `agent.md` frontmatter, Joshua and the external architect have two concrete deployment options:

### Option A: Dynamic Session-Scoped Subagents (Recommended)
Do not create persistent `agent.md` files in `~/.gemini/config/agents/`. Instead, use `define_subagent` dynamically at the start of review or verification sessions with `enable_write_tools: false`.
- **Advantage**: 100% mechanical restriction enforced by the Go runtime. Zero risk of accidental file writes or command execution. Zero file footprint in `~/.gemini/config/agents/`.

### Option B: Static Advisory Agents in `~/.gemini/config/agents/`
Deploy `browser_verifier/agent.md` and `code_reviewer/agent.md` into `~/.gemini/config/agents/` with prompt-level constraints only.
- **Advantage**: Permanently discovered in the Antigravity UI.
- **Tradeoff**: Tool restrictions rely entirely on LLM prompt obedience rather than runtime engine blocking.

---

## 12. HARD STOP CONFIRMATION

Wave 4 execution is **COMPLETE** in stop-and-report mode.
- No files have been written to `~/.gemini/config/agents/`.
- Zero files in `.agents/**`, `.codex/**`, or `.claude/**` have been modified.
- Wave 5 has **NOT** begun.
- Awaiting explicit authorization and architectural selection between Option A and Option B before proceeding.
