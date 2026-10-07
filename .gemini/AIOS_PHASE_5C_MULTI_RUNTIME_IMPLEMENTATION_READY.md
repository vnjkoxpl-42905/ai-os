# AIOS PHASE 5C: FINAL MULTI-RUNTIME MIGRATION SPECIFICATION

- **Author**: Antigravity Runtime Architect (Jay 2)
- **Status**: FROZEN SPECIFICATION - MULTI-RUNTIME ISOLATION CONTRACT
- **Context Roots**:
  - AIOS Command Center: `C:\Users\Joshu\dev\ai-os`
  - LSAT U Engineering: `C:\Users\Joshu\dev\ai-os\projects\lsatu`
- **Reference Inputs**:
  - `ANTIGRAVITY_RUNTIME_AUDIT_INPUT.md`
  - `GEMINI_ANTIGRAVITY_COMPLETE_BREAKDOWN.md`
  - `AIOS_PHASE_0_CURRENT_STATE_PACK.md`
  - `AIOS_PHASE_1_CONTROL_PLANE.md`
  - `AIOS_PHASE_2_SKILL_ARCHITECTURE.md`
  - `AIOS_PHASE_3_AGENT_TOOL_ARCHITECTURE.md`
  - `AIOS_PHASE_3B_MODEL_AGENT_VERIFICATION.md`
  - `AIOS_PHASE_4_PROJECT_CONTEXT_ARCHITECTURE.md`
  - `AIOS_PHASE_5_FINAL_TARGET_ARCHITECTURE.md`
  - `AIOS_PHASE_5B_MIGRATION_FREEZE.md`

---

## EXECUTIVE SUMMARY AND RUNTIME PRIORITY CHARTER

This workstation operates a tri-runtime environment serving Joshua's executive operations and software engineering.

### Runtime Priority Hierarchy
1. **Codex (Priority 1)**: Primary coding runtime and executive assistant operator.
2. **Claude Code (Co-Primary / Priority 2)**: Deep implementation, architectural reasoning, and primary coding partner.
3. **Antigravity / Gemini (Secondary / Priority 3)**: Secondary runtime for browser automation, visual verification, background research, and auxiliary multi-model workflows.

### Governing Architectural Mandate
Antigravity must **ADAPT TO** the existing Codex and Claude environments. Under no circumstances will Codex or Claude be redesigned, normalized, restructured, or constrained to accommodate Antigravity.

Antigravity operates in its own dedicated, isolated adapter layer. It treats all Codex and Claude configuration trees as **PROTECTED READ-ONLY** infrastructure.

**READ-ONLY DESIGN ONLY**: Zero files, configurations, projects, branches, or skills are modified during Phase 5C. Implementation begins strictly upon explicit user authorization of Wave 0.

---

## 1. FINAL RUNTIME OWNERSHIP MATRIX

The ownership boundaries across the three runtimes are strictly delineated:

```
+----------------------------------------------------------------------------------------------------+
|                                    RUNTIME OWNERSHIP MATRIX                                        |
+----------------------+--------------------+--------------------+-----------------------------------+
| Runtime Surface      | Primary Runtime    | Access Permissions | Responsibilities & Scope          |
+----------------------+--------------------+--------------------+-----------------------------------+
| AGENTS.md (Root)     | Codex (Priority 1) | Antigravity: READ  | Canonical EA rules, routing map,  |
|                      |                    | Codex: READ/WRITE  | voice rules, standing duties.     |
+----------------------+--------------------+--------------------+-----------------------------------+
| CLAUDE.md (Root)     | Claude (Priority 2)| Antigravity: IGNORE| Claude Code execution rules,      |
|                      |                    | Claude: READ/WRITE | hooks, and memory references.     |
+----------------------+--------------------+--------------------+-----------------------------------+
| GEMINI.md (Root)     | Antigravity (Pri 3)| Antigravity: R/W   | Antigravity-specific adapter:     |
|                      |                    | Other runtimes: N/A| tools, subagents, and paths.      |
+----------------------+--------------------+--------------------+-----------------------------------+
| .agents/ (Root)      | Codex (Priority 1) | Antigravity: READ  | Codex-active skills and execution |
|                      |                    | Codex: READ/WRITE  | infrastructure. Protected zone.   |
+----------------------+--------------------+--------------------+-----------------------------------+
| .claude/ (Root)      | Claude (Priority 2)| Antigravity: IGNORE| Claude memory, session cache,     |
|                      |                    | Claude: READ/WRITE | project configuration.            |
+----------------------+--------------------+--------------------+-----------------------------------+
| .codex/ (Root)       | Codex (Priority 1) | Antigravity: IGNORE| Codex agent configs, prompt cache,|
|                      |                    | Codex: READ/WRITE  | execution metadata.               |
+----------------------+--------------------+--------------------+-----------------------------------+
| .gemini/ (Root)      | Antigravity (Pri 3)| Antigravity: R/W   | Antigravity workspace cache,      |
|                      |                    | Other runtimes: N/A| outputs, transcripts, wiki notes. |
+----------------------+--------------------+--------------------+-----------------------------------+
| skills/claude/       | Claude (Priority 2)| Antigravity: READ  | Claude catalog snapshots (inert). |
+----------------------+--------------------+--------------------+-----------------------------------+
| skills/codex/        | Codex (Priority 1) | Antigravity: READ  | Codex catalog snapshots (inert).  |
+----------------------+--------------------+--------------------+-----------------------------------+
| skills/gemini/       | Antigravity (Pri 3)| Antigravity: R/W   | Antigravity skill catalog storage.|
+----------------------+--------------------+--------------------+-----------------------------------+
| LSAT U AGENTS.md     | Codex (Priority 1) | Antigravity: READ  | Inviolate recovered engineering   |
|                      |                    | Codex: READ/WRITE  | guidelines for LSAT U app code.   |
+----------------------+--------------------+--------------------+-----------------------------------+
| LSAT U CLAUDE.md     | Claude (Priority 2)| Antigravity: IGNORE| Inviolate Claude Code rules for   |
|                      |                    | Claude: READ/WRITE | LSAT U app development.           |
+----------------------+--------------------+--------------------+-----------------------------------+
| LSAT U GEMINI.md     | Antigravity (Pri 3)| Antigravity: R/W   | Dedicated LSAT U Antigravity      |
|                      |                    | Other runtimes: N/A| engineering context rules.        |
+----------------------+--------------------+--------------------+-----------------------------------+
| LSAT U .agents/      | Codex (Priority 1) | Antigravity: READ  | Codex engineering skills and      |
|                      |                    | Codex: READ/WRITE  | agent configuration. Protected.   |
+----------------------+--------------------+--------------------+-----------------------------------+
| ~/.gemini/           | Antigravity (Pri 3)| Antigravity: R/W   | Global Antigravity configuration, |
|                      |                    | Other runtimes: N/A| MCP configs, global skills/agents.|
+----------------------+--------------------+--------------------+-----------------------------------+
| Tools/LSATU-Agent/   | Shared Machine     | All: READ/EXECUTE  | Host browser automation suite     |
|                      | Infrastructure     | Writes: FROZEN     | on Chrome remote debugging 9223.  |
+----------------------+--------------------+--------------------+-----------------------------------+
```

---

## 2. PROTECTED PATH LIST (READ-ONLY TO ANTIGRAVITY)

Antigravity may inspect, read, and reference the following paths to understand system state or mirror skills. Antigravity is **PERMANENTLY PROHIBITED** from creating, modifying, editing, renaming, deleting, moving, synchronizing, formatting, or creating symlinks/junctions into these paths without prior explicit authorization from Joshua:

### Claude Protected Configuration
- `C:\Users\Joshu\dev\ai-os\CLAUDE.md`
- `C:\Users\Joshu\dev\ai-os\.claude\` (entire tree)
- `C:\Users\Joshu\dev\ai-os\skills\claude\` (entire tree)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md`
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\.claude\` (entire tree)

### Codex Protected Configuration
- `C:\Users\Joshu\dev\ai-os\AGENTS.md`
- `C:\Users\Joshu\dev\ai-os\.codex\` (entire tree)
- `C:\Users\Joshu\dev\ai-os\.agents\` (entire tree, including `.agents/skills/`, `.agents/rules/`, `.agents/agents/`)
- `C:\Users\Joshu\dev\ai-os\skills\codex\` (entire tree)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md`
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\.codex\` (entire tree)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\` (entire tree)

### Absolute Prohibition on Repurposing `.agents/`
Even though Antigravity 2.0 natively recognizes `<workspace-root>/.agents/`, Antigravity does **NOT** own that directory on this machine. The entire `.agents/` tree is established Codex operational infrastructure. Antigravity must not write skills, rules, hooks, or agent configurations into any `.agents/` directory.

---

## 3. ANTIGRAVITY-OWNED WRITABLE ZONE

The following paths constitute the exclusive writable domain for Antigravity, subject to phased wave authorization:

### Workspace-Level Antigravity Surfaces
- `C:\Users\Joshu\dev\ai-os\GEMINI.md`
- `C:\Users\Joshu\dev\ai-os\.gemini\` (including `.gemini/skills/`, `.gemini/agents/`, `.gemini/wiki/`, `.gemini/output/`, `.gemini/raw/`)
- `C:\Users\Joshu\dev\ai-os\skills\gemini\` (Antigravity skill catalog storage)
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md`
- `C:\Users\Joshu\dev\ai-os\projects\lsatu\.gemini\` (if project-specific Antigravity storage is provisioned)

### Machine-Level Global Antigravity Surfaces
- `C:\Users\Joshu\GEMINI.md` (User home rule file; preserved in place)
- `C:\Users\Joshu\.gemini\` (Global Antigravity directory)
  - `C:\Users\Joshu\.gemini\config\skills.json` (Custom skill discovery registry)
  - `C:\Users\Joshu\.gemini\config\mcp_config.json` (MCP server configuration)
  - `C:\Users\Joshu\.gemini\config\skills\` (Workstation-global Antigravity skills)
  - `C:\Users\Joshu\.gemini\config\agents\` (Workstation-global Antigravity custom agents)
  - `C:\Users\Joshu\.gemini\config\hooks.json` (Mechanical safety enforcement hooks)
- Antigravity IDE configuration databases and project metadata in `C:\Users\Joshu\AppData\Roaming\Antigravity\`.

### Shared Machine Infrastructure (Frozen)
- `C:\Users\Joshu\Tools\LSATU-Agent\`: Host browser scripts. Maintained in place as shared host infrastructure. Read-only execution by default.

---

## 4. ONE-WAY MIRRORING RULE

To prevent cross-runtime corruption, configuration drift, and accidental regressions in Codex or Claude:

```
                  +-------------------------------+
                  |      CLAUDE / CODEX SOURCE    |
                  |  (.claude/, .agents/, AGENTS) |
                  +-------------------------------+
                                  |
                                  | READ / COPY CONCEPTS ONLY
                                  | (Never write, never sync back)
                                  v
                  +-------------------------------+
                  |     GEMINI-OWNED ADAPTER      |
                  |   (.gemini/, GEMINI.md, ~/.gemini)|
                  +-------------------------------+
```

### Governing Rules
1. **Unidirectional Flow**: Information and skills flow from Claude/Codex into Gemini storage, **NEVER** in reverse.
2. **Zero In-Place Rewrites**: Antigravity never updates, refactors, or fixes a skill or rule inside `.claude/` or `.agents/`.
3. **No Dynamic Links**: No NTFS junctions, symbolic links, or hard links between Antigravity configuration folders and Claude/Codex configuration folders.
4. **Independent Evolution**: If Antigravity optimizes a skill or prompt for Gemini, that optimization lives exclusively in `.gemini/` or `~/.gemini/`.

---

## 5. REVISED ANTIGRAVITY-ONLY SKILL ARCHITECTURE

### 5.1 Comparative Architectural Evaluation
Because `<workspace>/.agents/skills/` is protected and cannot be written by Antigravity, four potential skill distribution architectures were evaluated:

| Criterion | Option 1: `.gemini/skills/` via `skills.json` | Option 2: `skills/gemini/` via `skills.json` | Option 3: Global `~/.gemini/config/skills/` | Option 4: Hybrid Scoped Discovery (Recommended) |
|---|---|---|---|---|
| **Antigravity 2.15.0 Support** | Fully supported via `skills.json` | Fully supported via `skills.json` | Natively supported without config | **100% Native & Documented** |
| **Project Scoping** | Project-specific to AIOS | Shared catalog, difficult to scope | Global across all projects | **Strict separation: Global vs AIOS vs LSAT U** |
| **Token Context Overhead** | High if all 217 skills are loaded | High (entire catalog active) | Minimal (only 5 universal skills) | **Optimized: Minimal token load per project** |
| **Different Surface for AIOS vs LSAT U** | Requires separate configs | Monolithic | Identical everywhere | **Yes: Cleanly scoped skill sets** |
| **Duplicate ID Avoidance** | High risk if overlapping `.agents` | High risk | Zero overlap with workspace | **Guaranteed: Zero duplicate IDs** |
| **Codex/Claude Impact** | Zero (ignored by both) | Zero (ignored by both) | Zero (ignored by both) | **Zero (100% protected)** |

### 5.2 The Recommended Architecture: Hybrid Scoped Discovery
The optimal architecture uses a three-tier model that completely bypasses `.agents/skills/`:

```
+----------------------------------------------------------------------------------------------------+
|                                HYBRID SCOPED SKILL DISCOVERY                                       |
+------------------------+------------------------------------+--------------------------------------+
| Tier                   | Physical Path                      | Registered Skills & Scope            |
+------------------------+------------------------------------+--------------------------------------+
| Tier 1: Machine Global | `C:\Users\Joshu\.gemini\config\    | 5 Universal Engineering Skills:      |
| (Always discoverable)  | skills\<skill>\`                   | - `google-antigravity-sdk`           |
|                        |                                    | - `systematic-debugging`             |
|                        |                                    | - `test-driven-development`          |
|                        |                                    | - `codebase-design`                  |
|                        |                                    | - `verification-before-completion`   |
+------------------------+------------------------------------+--------------------------------------+
| Tier 2: AIOS Workspace | `C:\Users\Joshu\dev\ai-os\.gemini\ | AIOS EA & Student Operations:        |
| (Project 1 only)       | skills\<skill>\`                   | - `consultation-inquiry-drafts`      |
|                        | Registered in `skills.json`        | - `consultation-followup-drafts`     |
|                        |                                    | - `inbound-tutoring-replies`         |
|                        |                                    | - `guided-drill-assignment`          |
|                        |                                    | - `lsat-u-platform-actions`          |
|                        |                                    | - `tutorocean-profile-fill`          |
|                        |                                    | - `wrapup` / `pickup`                |
+------------------------+------------------------------------+--------------------------------------+
| Tier 3: LSAT U Project | `C:\Users\Joshu\dev\ai-os\projects\| LSAT U Frontend & Browser Skills:     |
| (Project 2 only)       | lsatu\.gemini\skills\<skill>\`     | - `emil-design-eng`                  |
|                        | Registered in `skills.json`        | - `design-taste-frontend`            |
|                        |                                    | - `lsat-u-browser-verification`      |
|                        |                                    | - `webapp-testing`                   |
|                        |                                    | (Zero Netlify skills)                |
+------------------------+------------------------------------+--------------------------------------+
```

### 5.3 Safe Configuration of `C:\Users\Joshu\.gemini\config\skills.json`
To prevent duplicate skill discovery between Codex and Antigravity:
1. `C:/Users/Joshu/dev/ai-os/.agents/skills` is **REMOVED** from `skills.json`.
2. Antigravity discovers workspace skills exclusively through `.gemini/skills/` entries declared in `skills.json`.
3. The resulting `skills.json` will be cleanly formatted:
   ```json
   {
     "entries": [
       {
         "path": "C:/Users/Joshu/dev/ai-os/.gemini/skills",
         "include_only": [
           "consultation-.*",
           "inbound-.*",
           "guided-drill-.*",
           "lsat-u-platform-actions",
           "tutorocean-profile-fill",
           "superwhisper",
           "wrapup",
           "pickup",
           "prompt-architect-refiner"
         ]
       },
       {
         "path": "C:/Users/Joshu/dev/ai-os/projects/lsatu/.gemini/skills"
       }
     ]
   }
   ```
4. This completely avoids touching `.agents/skills/`, eliminates duplicate skill IDs, and ensures Codex and Claude remain 100% undisturbed.

---

## 6. REVISED CUSTOM AGENT STRATEGY

### 6.1 Constraint Analysis
The previous plan placed custom agents in `projects/lsatu/.agents/agents/`. Because `.agents/` is protected Codex infrastructure, Antigravity cannot write there.

### 6.2 Architectural Options for Antigravity Agents
1. **Option A: Workstation-Global Antigravity Agents** (`C:\Users\Joshu\.gemini\config\agents\<agent-name>\agent.md`)
   - Official Antigravity 2.0 documented pathway.
   - Completely outside `.agents/` and `.claude/`.
   - Accessible across all Antigravity projects (both AIOS and LSAT U).
   - Clean, persistent, declarative YAML + Markdown structure.
2. **Option B: Dynamic Subagents** (`define_subagent` / `invoke_subagent`)
   - Programmatically declared during active conversation.
   - Ephemeral; does not persist across restarts.
   - Useful for ad-hoc research tasks, but inadequate for persistent verification infrastructure.
3. **Option C: Postpone Persistent Agents**
   - Fall back to inline tool calling and prompt execution.
   - Wastes developer time re-briefing browser inspection protocols.

### 6.3 Frozen Decision: Global Gemini-Owned Persistent Agents
Antigravity custom agents will be provisioned in **Gemini-owned global configuration**:
- `C:\Users\Joshu\.gemini\config\agents\browser_verifier\agent.md`
- `C:\Users\Joshu\.gemini\config\agents\code_reviewer\agent.md`

#### A. `browser_verifier` Specifications
- **Location**: `C:\Users\Joshu\.gemini\config\agents\browser_verifier\agent.md`
- **Model**: `Gemini 3.0 Flash` (high speed, cost effective for UI parsing) or `Claude Sonnet 4.6 Thinking`.
- **Allowed Tools**: `view_file`, `read_url_content`, MCP `chrome-devtools` (29 tools).
- **Restricted Command Tool**: `run_command` allowed **strictly** for executing pre-existing read-only scripts in `C:\Users\Joshu\Tools\LSATU-Agent\`:
  - `node verify-viewports.mjs`
  - `node verify_localhost.mjs`
  - `node check_auth.mjs`
  - `node test_persistence_cycle.mjs`
- **Denied Tools**: `write_to_file`, `replace_file_content`, arbitrary shell execution.

#### B. `code_reviewer` Specifications
- **Location**: `C:\Users\Joshu\.gemini\config\agents\code_reviewer\agent.md`
- **Model Policy**:
  - **Tier 1 (Default Review)**: `Claude Sonnet 4.6 Thinking` for standard React, TypeScript, and styling reviews.
  - **Tier 2 (High-Risk Escalation)**: `Claude Opus 4.6 Thinking` or `Gemini 3.1 Pro High` for RLS security, migrations, auth, payments, or destructive operations.
- **Allowed Tools**: `view_file`, `grep_search`, `find_by_name`.
- **Denied Tools**: `write_to_file`, `replace_file_content`, `run_command`.

---

## 7. MECHANICAL PATH PROTECTION DESIGN

Written guardrails in instruction files are advisory. To guarantee that Antigravity can never inadvertently modify protected Claude or Codex configurations, a mechanical enforcement mechanism is established using Antigravity's native hook lifecycle.

### 7.1 Native Hook Architecture (`PreToolUse`)
Antigravity 2.15.0 officially supports `hooks.json` in the configuration root (`C:\Users\Joshu\.gemini\config\hooks.json`).

The `PreToolUse` event intercepts tool execution before any action is executed on disk.

```
                  [Antigravity Agent Emits Tool Call]
                                  |
                                  v
                     +--------------------------+
                     | PreToolUse Lifecycle Hook |
                     | (guard_protected_paths)  |
                     +--------------------------+
                                  |
            +---------------------+---------------------+
            |                                           |
    [Target is Protected]                     [Target is Permitted]
            |                                           |
            v                                           v
    Output: {"decision": "deny"}              Output: {"decision": "allow"}
            |                                           |
            v                                           v
    [TOOL HARD BLOCKED BY RUNTIME]             [TOOL PROCEEDS NORMALLY]
```

### 7.2 Configuration: `C:\Users\Joshu\.gemini\config\hooks.json`
```json
{
  "protected-runtime-guard": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "write_to_file|replace_file_content|run_command",
        "hooks": [
          {
            "type": "command",
            "command": "python C:/Users/Joshu/.gemini/config/scripts/guard_protected_paths.py",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

### 7.3 Enforcement Script: `C:\Users\Joshu\.gemini\config\scripts\guard_protected_paths.py`
The guard script enforces the following deterministic logic:
1. **Reads Tool Call Payload from `stdin`** (`toolCall.name`, `toolCall.args`).
2. **File Mutation Checks (`write_to_file`, `replace_file_content`)**:
   - Checks `TargetFile` argument.
   - Normalizes path separators to forward slashes.
   - Matches against protected patterns:
     - `*/AGENTS.md`
     - `*/CLAUDE.md`
     - `*/.agents/*`
     - `*/.claude/*`
     - `*/.codex/*`
     - `*/skills/claude/*`
     - `*/skills/codex/*`
   - If match found, outputs:
     ```json
     {
       "decision": "deny",
       "reason": "BLOCKED BY RUNTIME GUARD: Mutation of protected Claude/Codex configuration is strictly forbidden. Target path is protected read-only."
     }
     ```
3. **Terminal Command Checks (`run_command`)**:
   - Inspects `CommandLine` argument for destructive or mutating operations directed at protected paths (e.g., `rm`, `del`, `mv`, `git checkout`, redirection `>` into `.agents/`, `.claude/`, `AGENTS.md`, or `CLAUDE.md`).
   - If mutating pattern detected on protected path, outputs `decision: "deny"`.
4. **All Other Tools and Paths**:
   - Outputs:
     ```json
     {
       "decision": "allow"
     }
     ```

### 7.4 Non-Interference Guarantee
This hook executes strictly within the Antigravity runtime process. It has zero impact on Codex or Claude Code CLI operations.

---

## 8. CORRECTED REVISED MIGRATION WAVES

The revised implementation sequence enforces runtime isolation and phased validation:

```
+----------------------------------------------------------------------------------------------------+
|                                    REVISED MIGRATION WAVES                                         |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave   | Focus Area                         | Risk Level          | Impact on Claude / Codex      |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 0 | Backup & Baseline Freeze           | Zero (Read-only copy)| ZERO (Pure backup)            |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 1 | Project 2 Registration & Branch    | Low (IDE config)    | ZERO (Pure IDE metadata)      |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 2 | Gemini Instruction Cleanup         | Low (Gemini files)  | ZERO (AGENTS/CLAUDE untouched)|
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 3 | Antigravity-Only Skill Discovery   | Low (skills.json)   | ZERO (.agents/ untouched)     |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 4 | Global Custom Agents Setup         | Low (~/.gemini/)    | ZERO (.agents/ untouched)     |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 5 | MCP Tooling & Version Pinning      | Low (mcp_config)    | ZERO (Chrome port 9223 only)  |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 6 | Mechanical Path Protection Guard   | Low (hooks.json)    | ZERO (Antigravity-only guard) |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 7 | Browser Integration Verification   | Zero (Read-only test)| ZERO (Existing scripts run)   |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 8 | AIOS Doctor & Observability Check  | Zero (Read-only audit| ZERO (Health diagnostic)      |
+--------+------------------------------------+---------------------+-------------------------------+
| Wave 9 | Before/After Benchmark Signoff     | Zero (Performance)  | ZERO (Signoff and baseline)   |
+--------+------------------------------------+---------------------+-------------------------------+
```

### Detailed Wave Specifications

#### WAVE 0: Lean Backup and Baseline Freeze
- **Objective**: Create a deterministic, lightweight snapshot of all Antigravity and control-plane configurations before any changes occur.
- **Scope**: Targeted backup to `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\`.
- **Files Included**:
  - `ai-os/GEMINI.md`, `ai-os/.gemini/`
  - `projects/lsatu/GEMINI.md` (if exists)
  - `C:\Users\Joshu\GEMINI.md`
  - `C:\Users\Joshu\.gemini\config\` (including `skills.json`, `mcp_config.json`)
  - `C:\Users\Joshu\Tools\LSATU-Agent\`
- **Files Excluded**: `node_modules/`, `.git/objects/`, build outputs, cache files. Total size under 35 MB.
- **Joshua Approval Required**: **Yes** (Formal confirmation to begin baseline).

#### WAVE 1: Antigravity Project 2 Registration Only
- **Objective**: Register `C:\Users\Joshu\dev\ai-os\projects\lsatu` as Project 2 ("LSAT U Engineering") in Antigravity.
- **Actions**: Register project via IDE project manager or `state.vscdb`.
- **Safety Rule**: **STRICT PRESERVATION OF GIT BRANCH**. The active branch `feat/calendar-strip-deeplink` and any uncommitted changes remain untouched.
- **Joshua Approval Required**: **Yes**.

#### WAVE 2: Gemini/Antigravity Instruction Cleanup Only
- **Objective**: Establish clean, non-duplicative instructions in Gemini-owned files.
- **Actions**:
  - Update `C:\Users\Joshu\dev\ai-os\GEMINI.md` with Antigravity-specific execution rules (native tools, subagent invocation, multi-model tiers).
  - Create `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` with focused LSAT U engineering context, Lovable Cloud deployment guardrails, and port 9223 verification instructions.
- **Safety Rule**: `AGENTS.md` and `CLAUDE.md` in both roots are **STRICTLY UNTOUCHED**.
- **Joshua Approval Required**: **Yes**.

#### WAVE 3: Antigravity-Only Skill Discovery Cleanup
- **Objective**: Eliminate duplicate skill ID collisions and scope skills cleanly without touching `.agents/`.
- **Actions**:
  - Copy universal skills to `~/.gemini/config/skills/` (`google-antigravity-sdk`, `systematic-debugging`, `test-driven-development`, `codebase-design`, `verification-before-completion`).
  - Update `C:\Users\Joshu\.gemini\config\skills.json` to include `.gemini/skills/` and remove `.agents/skills/`.
  - Remove Netlify skills from LSAT U skill discovery.
- **Safety Rule**: `.agents/skills/` is untouched.
- **Joshua Approval Required**: **Yes**.

#### WAVE 4: Antigravity-Only Custom Agent Setup
- **Objective**: Provision persistent custom agents in global Gemini-owned storage.
- **Actions**:
  - Create `C:\Users\Joshu\.gemini\config\agents\browser_verifier\agent.md`.
  - Create `C:\Users\Joshu\.gemini\config\agents\code_reviewer\agent.md`.
- **Safety Rule**: No files created under `.agents/agents/`.
- **Joshua Approval Required**: **Yes**.

#### WAVE 5: Antigravity MCP Tooling and Version Pinning
- **Objective**: Lock verified MCP configurations against port 9223.
- **Actions**: Update `C:\Users\Joshu\.gemini\config\mcp_config.json` to pin `chrome-devtools-mcp@1.9.0` (replacing `@latest`).
- **Safety Rule**: Shared browser scripts in `C:\Users\Joshu\Tools\LSATU-Agent\` remain untouched.
- **Joshua Approval Required**: **Yes**.

#### WAVE 6: Mechanical Claude/Codex Write-Protection Guard
- **Objective**: Implement automated pre-execution blocking of any Antigravity write attempts to Claude/Codex paths.
- **Actions**:
  - Write `C:\Users\Joshu\.gemini\config\scripts\guard_protected_paths.py`.
  - Configure `PreToolUse` hook in `C:\Users\Joshu\.gemini\config\hooks.json`.
- **Validation**: Attempt dry-run write to protected mock path; verify immediate hard denial.
- **Joshua Approval Required**: **Yes**.

#### WAVE 7: Browser Integration Validation
- **Objective**: Execute read-only smoke tests using existing scripts on port 9223.
- **Actions**:
  - Launch Chrome on port 9223 via `launch_browser.py`.
  - Execute `verify_localhost.mjs` and `verify-viewports.mjs`.
  - Verify MCP `chrome-devtools` responds to tool calls in Project 2.
- **Safety Rule**: Zero script renames or modifications.
- **Joshua Approval Required**: **Yes**.

#### WAVE 8: AIOS Doctor and Observability Check
- **Objective**: Run comprehensive diagnostics across all three runtimes.
- **Actions**:
  - Run verification script checking for zero duplicate skill IDs.
  - Verify Codex and Claude CLI tools run unaffected.
  - Verify Antigravity starts cleanly in both Project 1 and Project 2.
- **Joshua Approval Required**: **Yes**.

#### WAVE 9: Final Before/After Benchmark and Acceptance Signoff
- **Objective**: Measure prompt token load, discovery latency, and operational health.
- **Actions**: Document final performance metrics; submit completion report to Joshua.
- **Joshua Approval Required**: **Yes**.

---

## 9. EXACT WAVE 0 BACKUP AND BASELINE PLAN

Before any wave is initiated, Wave 0 will execute this exact backup command:

### Backup Target
`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\`

### Manifest of Items Backed Up
1. `C:\Users\Joshu\dev\ai-os\GEMINI.md`
2. `C:\Users\Joshu\dev\ai-os\.gemini\` (recursive)
3. `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` (if exists)
4. `C:\Users\Joshu\GEMINI.md`
5. `C:\Users\Joshu\.gemini\config\` (recursive, including `skills.json` and `mcp_config.json`)
6. `C:\Users\Joshu\Tools\LSATU-Agent\` (recursive)
7. `C:\Users\Joshu\AppData\Roaming\Antigravity\User\workspaceStorage\` (project metadata)

### Baseline Verification Metric
- Record SHA-256 hash of all backed-up files into `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\MANIFEST.sha256`.
- Execution time: < 3 seconds. Total storage footprint: < 35 MB.

---

## 10. ROLLBACK REQUIREMENTS

Every wave is strictly atomic, isolated, and reversible:

| Wave | Failure Condition | Rollback Action | Rollback Time |
|---|---|---|---|
| **Wave 0** | Backup script error or disk issue | Delete `ai-os-backup-pre-migration-config` | < 10 seconds |
| **Wave 1** | IDE corruption or project load failure | Deregister Project 2 from IDE configuration | < 30 seconds |
| **Wave 2** | Prompt syntax error or instructions rejected | Restore `GEMINI.md` from Wave 0 backup | < 15 seconds |
| **Wave 3** | Skill registry error or missing skills | Restore `skills.json` and global skills folder | < 30 seconds |
| **Wave 4** | Custom agent syntax or loading error | Remove `~/.gemini/config/agents/` | < 15 seconds |
| **Wave 5** | MCP connection failure on port 9223 | Revert `mcp_config.json` to `@latest` config | < 15 seconds |
| **Wave 6** | Guard falsely denies legitimate writes | Disable hook (`"enabled": false` in `hooks.json`) | < 10 seconds |
| **Wave 7** | Script execution failure or browser crash | Restart browser process via `launch_browser.py` | < 30 seconds |
| **Wave 8** | Diagnostic detects registry conflict | Trace conflict to specific wave and revert that wave | < 1 minute |
| **Wave 9** | Benchmark fails acceptance criteria | Restore entire configuration from Wave 0 backup | < 2 minutes |

---

## 11. IMPLEMENTATION ACCEPTANCE CHECKLIST

Before Wave 0 execution is authorized, verify that the frozen specification satisfies every requirement:

```
[X] 1. RUNTIME PRIORITY RESPECTED
    - Codex confirmed as Priority 1 runtime.
    - Claude Code confirmed as Co-Primary / Priority 2 runtime.
    - Antigravity confirmed as Secondary / Priority 3 runtime.
    - Antigravity adapts to existing environment; zero redesign of Codex/Claude.

[X] 2. PROTECTED BOUNDARIES ENFORCED
    - AGENTS.md and CLAUDE.md in all directories are marked read-only to Antigravity.
    - .claude/, .codex/, and .agents/ are 100% protected read-only.
    - Absolute prohibition on repurposing or writing into .agents/.

[X] 3. ANTIGRAVITY-OWNED WRITABLE ZONE PRESERVED
    - Antigravity writes restricted to .gemini/, GEMINI.md, and ~/.gemini/.
    - Host browser suite in Tools/LSATU-Agent/ preserved as shared host tooling.

[X] 4. ONE-WAY MIRRORING ONLY
    - Claude/Codex source -> READ/COPY -> Gemini-owned copy.
    - Zero writeback or sync into Claude/Codex configuration.
    - Zero writable symlinks, junctions, or hard links between runtimes.

[X] 5. ANTIGRAVITY-ONLY SKILL ARCHITECTURE
    - .agents/skills/ is NOT written to by Antigravity.
    - .agents/skills/ removed from skills.json to prevent duplicate skill ID collisions.
    - Skills cleanly scoped: Global (~/.gemini/config/skills/), AIOS (.gemini/skills/), LSAT U.

[X] 6. GLOBAL GEMINI-OWNED PERSISTENT AGENTS
    - Persistent agents live in ~/.gemini/config/agents/ (browser_verifier, code_reviewer).
    - Zero agent files written to .agents/agents/.

[X] 7. MECHANICAL PATH PROTECTION DESIGNED
    - Native PreToolUse lifecycle hook designed in ~/.gemini/config/hooks.json.
    - guard_protected_paths.py intercepts and hard-denies mutation of protected paths.

[X] 8. PRESERVE ALL VALIDATED PHASE 5B DECISIONS
    - Zero em-dashes and zero AI-slop vocabulary.
    - Chrome DevTools MCP pinned to verified version 1.9.0.
    - Browser script canonical filenames preserved (launch_browser.py, etc.).
    - LSAT U Git branch feat/calendar-strip-deeplink strictly preserved.
    - GitHub authoritative for committed code; Lovable authoritative for live backend.
    - Netlify skills purged from active LSAT U engineering discovery.
    - SQLite conversation databases remain untouched (zero migration).

[X] 9. PHASED IMPLEMENTATION WITH EXPLICIT APPROVAL
    - Every wave requires explicit authorization from Joshua.
    - One wave executed at a time with validation and rollback gates.
```

---

## 12. OUTPUT AND HARD STOP CONFIRMATION

- **Primary Output Path**: `C:\Users\Joshu\dev\ai-os\AIOS_PHASE_5C_MULTI_RUNTIME_IMPLEMENTATION_READY.md`
- **Secondary Mirror Path**: `C:\Users\Joshu\dev\ai-os\.gemini\AIOS_PHASE_5C_MULTI_RUNTIME_IMPLEMENTATION_READY.md`

### Hard Stop Declaration
This document represents the final, complete, multi-runtime migration design.

**ZERO IMPLEMENTATION HAS OCCURRED.**
- No files have been modified.
- No skills have been moved.
- No projects have been registered.
- No hooks or guards have been installed.
- Wave 0 has **NOT** begun.

The system remains in a 100% frozen, read-only state awaiting explicit authorization from Joshua to begin Wave 0.
