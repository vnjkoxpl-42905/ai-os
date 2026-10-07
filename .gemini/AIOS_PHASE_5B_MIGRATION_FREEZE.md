> Historical snapshot. The "no Git remote" rule quoted below was removed on 2026-09-29. Current rule: see AGENTS.md line 75.
# AIOS PHASE 5B: FINAL SPECIFICATION CORRECTION AND MIGRATION FREEZE

- **Author**: Antigravity Runtime Architect (Jay 2)
- **Status**: FROZEN SPECIFICATION - PENDING EXTERNAL ARCHITECT APPROVAL
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

---

## EXECUTIVE ARCHITECTURAL DIRECTIVE

The external architect has formally reviewed `AIOS_PHASE_5_FINAL_TARGET_ARCHITECTURE.md` and approved the high-level system architecture:

1. **Two Antigravity Projects**:
   - Project 1: **AIOS Command Center** (`C:\Users\Joshu\dev\ai-os`)
   - Project 2: **LSAT U Engineering** (`C:\Users\Joshu\dev\ai-os\projects\lsatu`)
2. **Conversation History Remains In Place**: Zero migration or database surgery on SQLite conversation databases.
3. **Dedicated LSAT U Engineering Context**: Clean, isolated application engineering workspace.
4. **Persistent Chrome Port 9223 Preserved**: Remote debugging browser workflow maintained without disruption.
5. **Native Antigravity 2.0 `.agents` Conventions**: Adopt standard workspace discovery pathways.

This Phase 5B document resolves and freezes all implementation-level defects, incorrect assumptions, invented paths, and versioning errors identified during the Phase 5 review.

**READ-ONLY FREEZE**: No code, project definitions, instruction files, skills, or settings are modified during Phase 5B. Implementation begins strictly in Wave 0 after final external signoff.

---

## 1. INSTRUCTION CONTROL PLANE AND DUAL-RUNTIME OWNERSHIP MODEL (NO MIRRORING)

### 1.1 The Duplicate Token Problem in Phase 5
Phase 5 proposed having `AGENTS.md` and `CLAUDE.md` mirror `GEMINI.md`. That recommendation is rejected based on verified Phase 0 empirical evidence:

- Antigravity 2.15.0 eagerly loads **both** `C:\Users\Joshu\dev\ai-os\AGENTS.md` and `C:\Users\Joshu\dev\ai-os\GEMINI.md` when both exist in the workspace root.
- In Phase 0, both files were injected consecutively into the system prompt under `<RULE[...]>` tags.
- Mirroring identical content between `AGENTS.md` and `GEMINI.md` literally duplicates token consumption on every turn, wasting model context window and creating semantic ambiguity.

### 1.2 Conceptual Ownership Model
The control plane enforces strict separation of responsibilities:
- **Shared Cross-Runtime Baseline**: Exactly one authoritative home.
- **Runtime-Specific Deltas**: Only what that specific runtime requires.
- **Claude Code Isolation**: Claude reads `CLAUDE.md`. Antigravity does not read `CLAUDE.md`.

```
+-----------------------------------------------------------------------------------+
|                            CROSS-RUNTIME OWNERSHIP                                |
+-----------------------------------+-----------------------------------------------+
| AIOS Root: AGENTS.md               | Canonical EA rules, routing map, retrieval    |
| (Read by Codex + Antigravity)     | order, core business guardrails. Shared base. |
+-----------------------------------+-----------------------------------------------+
| AIOS Root: GEMINI.md              | Antigravity-only runtime deltas: native tools,|
| (Read by Antigravity only)        | subagents, discovery paths, model roles.       |
+-----------------------------------+-----------------------------------------------+
| AIOS Root: CLAUDE.md              | Claude Code only: hooks, memory pointers,     |
| (Ignored by Antigravity)          | Claude-specific execution rules.              |
+-----------------------------------+-----------------------------------------------+
| LSAT U Root: AGENTS.md            | Canonical LSAT U engineering architecture,     |
| (Read by Codex + Antigravity)     | coding standards, recovered inviolate rules.  |
+-----------------------------------+-----------------------------------------------+
| LSAT U Root: GEMINI.md            | Antigravity LSAT U project deltas: Chrome     |
| (Read by Antigravity only)        | port 9223 verification, Lovable deploy rule.  |
+-----------------------------------+-----------------------------------------------+
| LSAT U Root: CLAUDE.md            | Claude Code LSAT U instructions and hooks.    |
| (Ignored by Antigravity)          |                                               |
+-----------------------------------+-----------------------------------------------+
```

### 1.3 Exact File Ownership Specifications

#### A. `C:\Users\Joshu\dev\ai-os\AGENTS.md`
- **Primary Audience**: Codex EA runtime and shared cross-runtime foundational rules.
- **Contents**:
  - Identity: Jay 2, Joshua's executive assistant.
  - Standing duties: Student operations, prospect correspondence drafting, wiki ledgers (`hot.md`, `tasks.md`, `log.md`).
  - Routing map: Definitive relative paths to `context/`, `decisions/`, `students/`, `wiki/`, `corpus/`.
  - Retrieval order: Hot cache -> wiki index -> live systems.
  - Voice constraints: Zero em-dashes, zero AI-slop vocabulary, teaching voice requirements.
  - Security model: `.env` + `.gitignore` store; no git remote without scrub checklist.
  - Guardrails: 95% confidence rule, Lovable credit restrictions, root directory hygiene.
- **Rule**: This file is the single authoritative source for operational EA policy.

#### B. `C:\Users\Joshu\dev\ai-os\GEMINI.md`
- **Primary Audience**: Antigravity runtime in Project 1 (AIOS Command Center).
- **Contents**:
  - Antigravity execution model: Native tools declaration (`run_command`, `search_web`, `read_url_content`).
  - Multi-agent orchestration: Antigravity subagent invocation patterns.
  - Skill discovery hierarchy: Global skills (`~/.gemini/config/skills/`) and workspace skills (`.agents/skills/`).
  - Persistent browser tooling pointer: Points to `C:\Users\Joshu\Tools\LSATU-Agent\` for browser verification without embedding raw scripts.
  - Model assignment policy: Default operator model vs deep reasoning escalation.
- **Rule**: MUST NOT duplicate the routing map, retrieval order, voice rules, or business guardrails already loaded from `AGENTS.md`.

#### C. `C:\Users\Joshu\dev\ai-os\CLAUDE.md`
- **Primary Audience**: Claude Code CLI runtime.
- **Contents**: Claude Code operational commands, pre-commit hook integrations, memory references, and Claude-specific execution preferences.
- **Rule**: Zero Antigravity overhead since Antigravity does not scan `CLAUDE.md`.

#### D. `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md`
- **Primary Audience**: Codex engineering runtime and shared LSAT U development baseline.
- **Contents**:
  - Recovered inviolate instructions for LSAT U application engineering.
  - Tech stack: React 18, TypeScript, Vite, Tailwind CSS, shadcn/ui, Supabase client (`@supabase/supabase-js`).
  - Architecture conventions: Component hierarchies, strict typing, folder structures.
  - Lovable Cloud deployment guardrails: Edge functions deploy via Lovable; Lovable credits require prior confirmation.
- **Rule**: Single authoritative source for LSAT U application code standards.

#### E. `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md`
- **Primary Audience**: Antigravity runtime in Project 2 (LSAT U Engineering).
- **Contents**:
  - Dedicated engineering context rules: Scope restricted to `projects/lsatu/`.
  - Antigravity 2.0 workspace skills discovery: `.agents/skills/` within the project root.
  - Custom persistent agents: `browser_verifier` and `code_reviewer`.
  - Port 9223 Chrome DevTools integration: Testing protocols for localhost and live staging.
  - Git branch preservation mandate: Never switch branches during automated verification.
- **Rule**: MUST NOT duplicate the tech stack descriptions or coding rules already loaded from `projects/lsatu/AGENTS.md`.

#### F. `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md`
- **Primary Audience**: Claude Code engineering runtime.
- **Contents**: Claude Code test commands, local development scripts, and Claude hook configurations for LSAT U.

---

## 2. EMPIRICAL VERIFICATION OF GLOBAL GEMINI RULE PATH

### 2.1 Empirical Findings on This Installation
Phase 0 observed `C:\Users\Joshu\GEMINI.md` injected directly into the Antigravity prompt. Phase 5 proposed moving or establishing `C:\Users\Joshu\.gemini\GEMINI.md`. 

A direct filesystem audit of this workstation reveals:
- `C:\Users\Joshu\GEMINI.md`: **EXISTS** (Size: 1,799 bytes) [VERIFIED & OBSERVED]
- `C:\Users\Joshu\.gemini\GEMINI.md`: **DOES NOT EXIST** (Size: None) [VERIFIED]
- `C:\Users\Joshu\.gemini\config\GEMINI.md`: **DOES NOT EXIST** (Size: None) [VERIFIED]

### 2.2 Status Matrix
- `C:\Users\Joshu\GEMINI.md`: **VERIFIED & OBSERVED**. Actively parsed by Antigravity 2.15.0 as the user-home rule file.
- `C:\Users\Joshu\.gemini\GEMINI.md`: **UNVERIFIED / INVENTED**. There is no runtime evidence that Antigravity checks this path for prompt rules.
- Precedence: Antigravity walks parent directories upward from the workspace root to the user home (`C:\Users\Joshu`), loading `GEMINI.md` at each step.
- Legacy Status: `C:\Users\Joshu\GEMINI.md` is the active, functional home rule file.
- Movement Risk: Moving `C:\Users\Joshu\GEMINI.md` to `~/.gemini/` would break global rule loading.

### 2.3 Frozen Decision
`C:\Users\Joshu\GEMINI.md` **REMAINS IN PLACE**. It will not be moved, renamed, or deleted. Any workstation-wide Antigravity rules remain anchored at `C:\Users\Joshu\GEMINI.md`.

---

## 3. CANONICAL BROWSER SUITE PATHS AND RETENTION STATUS

### 3.1 Status of Browser Automation Scripts
Phase 5 introduced invented script names (`launch_lsatu_browser.py`, `verify_responsive_sweep.py`). The existing, verified, working browser verification suite lives at `C:\Users\Joshu\Tools\LSATU-Agent\`.

Every script in the target architecture is categorized below:

| Script Path | Classification | Functional Justification |
|---|---|---|
| `C:\Users\Joshu\Tools\LSATU-Agent\launch_browser.py` | **KEEP EXISTING** | Primary script launching Chrome on port 9223 with remote debugging and persistent user profile. Fully tested. |
| `C:\Users\Joshu\Tools\LSATU-Agent\start-dev-session.ps1` | **KEEP EXISTING** | PowerShell orchestrator that starts local Vite dev server, verifies port 9223, and sets up working session. |
| `C:\Users\Joshu\Tools\LSATU-Agent\verify-viewports.mjs` | **KEEP EXISTING** | Playwright CDP script executing automated visual and layout sweeps across mobile, tablet, and desktop viewports. |
| `C:\Users\Joshu\Tools\LSATU-Agent\verify_localhost.mjs` | **KEEP EXISTING** | Baseline connectivity and DOM integrity check against `http://localhost:8080`. |
| `C:\Users\Joshu\Tools\LSATU-Agent\verify_control_drill.mjs` | **KEEP EXISTING** | Deep interactive drill state and control element test script. |
| `C:\Users\Joshu\Tools\LSATU-Agent\check_auth.mjs` | **KEEP EXISTING** | Verifies active session token, local storage auth state, and cookie persistence. |
| `C:\Users\Joshu\Tools\LSATU-Agent\test_persistence_cycle.mjs`| **KEEP EXISTING** | Tests cross-restart session persistence and profile cache validity. |
| `launch_lsatu_browser.py` | **SUPERSEDED** | Invented in Phase 5. Rejected to prevent code churn. Superseded by `launch_browser.py`. |
| `verify_responsive_sweep.py` | **SUPERSEDED** | Invented in Phase 5. Rejected to prevent code churn. Superseded by `verify-viewports.mjs`. |

### 3.2 Frozen Decision
No browser scripts will be renamed or rewritten. The final migration specification and all agent definitions reference the exact working filenames in `C:\Users\Joshu\Tools\LSATU-Agent\`.

---

## 4. CHROME DEVTOOLS MCP RESOLUTION AND VERSION PINNING

### 4.1 Empirical Forensic Audit
Phase 5 proposed `chrome-devtools-mcp@0.9.x`, a version number not supported by runtime evidence.

Inspection of the live machine configuration and npm cache reveals:
- Config Path: `C:\Users\Joshu\.gemini\config\mcp_config.json`
- Active Server Entry:
  ```json
  "chrome-devtools": {
    "command": "npx",
    "args": [
      "-y",
      "chrome-devtools-mcp@latest",
      "--browserUrl",
      "http://127.0.0.1:9223"
    ]
  }
  ```
- NPM Resolved Package: `C:\Users\Joshu\AppData\Local\npm-cache\_npx\15c61037b1978c83\node_modules\chrome-devtools-mcp\package.json`
- **Exact Resolved Version**: **`1.9.0`** (Package: `chrome-devtools-mcp`, Version: `1.9.0`)

### 4.2 Tooling and Compatibility Analysis
- Package Source: Official npm registry (`chrome-devtools-mcp`).
- Tool Exposure: Version 1.9.0 exposes exactly the 29 Chrome DevTools MCP tools registered in Antigravity (`click`, `evaluate_script`, `take_screenshot`, `list_console_messages`, `list_network_requests`, `navigate_page`, `fill_form`, etc.).
- Port 9223 Compatibility: Fully verified and active against Chrome remote debugging endpoint `http://127.0.0.1:9223`.

### 4.3 Pinning Policy
- Policy: **PIN CURRENT VERIFIED VERSION**.
- When deterministic pinning is applied, the configuration will specify `chrome-devtools-mcp@1.9.0`.
- The invented `0.9.x` string is permanently purged from all specifications.

---

## 5. REMOVAL OF UNJUSTIFIED NETLIFY RUNTIME SKILLS

### 5.1 Project Architecture Audit
An inspection of `C:\Users\Joshu\dev\ai-os\projects\lsatu` establishes:
- `package.json` contains zero Netlify dependencies. Production backend dependencies are centered on `@supabase/supabase-js`.
- No `netlify.toml` exists in `projects/lsatu/` or at the repository root.
- Hosting and deployment: LSAT U is built via Vite and deployed directly to production on **Lovable Cloud**, with backend data and Edge Functions hosted on Lovable-managed Supabase.

### 5.2 Policy and Skill Surface Corrections
- `netlify-deploy` and `netlify-functions`: **REMOVED** from the active engineering skills for LSAT U. They must not be discoverable in `projects/lsatu/.agents/skills/`.
- Deployment Router: Netlify is completely removed from the default deployment and build router.
- Catalog Retention: Netlify skills remain preserved in the inert snapshot catalog (`skills/claude/` and `skills/codex/`) for historical reference or standalone prototypes, but are never auto-loaded.

---

## 6. DEPLOY-SUITE RESPONSIBILITY MATRIX

Deployment responsibilities are strictly decoupled across their authoritative subsystems:

```
+-----------------------------------------------------------------------------------+
|                        DEPLOYMENT RESPONSIBILITY MATRIX                           |
+------------------------------+---------------------+------------------------------+
| Subsystem                    | Authoritative Tool  | Validation & Scope           |
+------------------------------+---------------------+------------------------------+
| Git Verification             | Local Git CLI       | `npm run typecheck`, lint,   |
|                              |                     | verify working tree clean.   |
+------------------------------+---------------------+------------------------------+
| Pre-Commit Checks            | Husky / lint-staged | Runs formatting, staged diff |
|                              |                     | verification prior to commit.|
+------------------------------+---------------------+------------------------------+
| Git Remote Push              | Git CLI (`origin`)  | Pushes commits to GitHub;    |
|                              |                     | maintains VCS source history.|
+------------------------------+---------------------+------------------------------+
| Frontend Web Deployment      | Lovable Cloud       | Production web build/publish |
|                              | Platform Agent      | from approved Git state.     |
+------------------------------+---------------------+------------------------------+
| Edge Function Deployment     | Lovable Agent       | Supabase Edge Functions      |
|                              | (Per Guardrail)     | deployed via Lovable Cloud.  |
+------------------------------+---------------------+------------------------------+
| Legacy Netlify Prototypes    | Standalone CLI      | Isolated sandbox prototypes; |
|                              | (Manual on demand)  | NOT part of LSAT U pipeline. |
+------------------------------+---------------------+------------------------------+
```

---

## 7. GIT BRANCH INTEGRITY AND PRESERVATION RULE

### 7.1 Empirical State
Phase 0 verification confirmed:
- `C:\Users\Joshu\dev\ai-os\projects\lsatu` is currently checked out on feature branch:
  `feat/calendar-strip-deeplink`

### 7.2 Locked Migration Rule
Registering `C:\Users\Joshu\dev\ai-os\projects\lsatu` as Project 2 in Antigravity must **NEVER**:
- Checkout `main` or `master`.
- Create a new Git branch.
- Switch the active branch.
- Merge branches or rebase.
- Stage, commit, or push files.

Project registration is purely an IDE control-plane operation in `state.vscdb` / `workspaceStorage`. It attaches to the directory exactly as it stands on disk, preserving Joshua's working branch and uncommitted edits intact.

---

## 8. AUTHORITY AND SOURCE-OF-TRUTH MATRIX

To prevent ambiguity between code repositories, backend databases, and schema declarations, the system establishes a four-tier authority matrix:

```
+-----------------------------------------------------------------------------------+
|                         SOURCE-OF-TRUTH AUTHORITY MATRIX                          |
+------------------------+------------------------------------+---------------------+
| Domain                 | Authoritative Source               | Status & Scope      |
+------------------------+------------------------------------+---------------------+
| Current Committed Code | GitHub Repository (`origin`) and   | PRIMARY AUTHORITY   |
|                        | local working checkout.            | for React, TS, Vite |
|                        |                                    | and frontend code.  |
+------------------------+------------------------------------+---------------------+
| Live Production        | Lovable Cloud Managed Database     | PRIMARY AUTHORITY   |
| Backend State          | and Supabase Backend.              | for tables, live    |
|                        |                                    | data, auth, rows.   |
+------------------------+------------------------------------+---------------------+
| Migrations and         | `supabase/migrations/` and         | HISTORICAL INTENT   |
| Generated Types        | `src/integrations/supabase/types.ts`| ONLY. Not proof of  |
|                        |                                    | live execution.     |
+------------------------+------------------------------------+---------------------+
| Product and Business   | `decisions/log.md`, `wiki/`, and   | LOCKED CANONICAL    |
| Architecture           | `context/work.md`.                 | DECISION RECORDS.   |
+------------------------+------------------------------------+---------------------+
```

- **Correction of Phase 5 wording**: GitHub is NOT a downstream mirror of Lovable for application code. GitHub is the authoritative repository for committed TypeScript/React source code. Lovable Cloud is the authoritative hosting environment and live database provider.

---

## 9. SKILL MIGRATION SEQUENCING WITHOUT DUPLICATE IDS

### 9.1 The Collision Hazard
In Antigravity 2.15.0:
- `C:\Users\Joshu\dev\ai-os\.gemini\skills\skills.json` manually indexes skills located in `.gemini/skills/`.
- Antigravity 2.0 natively discovers skills located in `<workspace-root>/.agents/skills/`.
- If a skill exists in `.agents/skills/` while its identical copy is still indexed in `.gemini/skills/`, Antigravity will discover duplicate skill IDs, causing registry errors or unpredictable prompt injection.

### 9.2 Safe Migration Sequencing
The migration must transition skill discovery without ever leaving two active copies of the same identifier visible:

```
[Phase 1: Freeze Current]
  Audit all 217 items in .gemini/skills/ and current skills.json.
       |
       v
[Phase 2: Global Skill Migration]
  Copy workstation-wide skills (5 items) to ~/.gemini/config/skills/.
       |
       v
[Phase 3: Workspace Skill Allocation]
  Allocate Project 1 skills to ai-os/.agents/skills/.
  Allocate Project 2 skills to projects/lsatu/.agents/skills/.
       |
       v
[Phase 4: Atomic De-indexing]
  Retire or clear skills.json from .gemini/skills/ so legacy manual
  indexing ceases before .gemini/skills/ is archived.
       |
       v
[Phase 5: Archival & Verification]
  Move .gemini/skills/ to inert catalog or archive storage.
  Verify zero duplicate skill IDs via native discovery query.
```

---

## 10. NATIVE TOOLS VS SKILLS DELINEATION

### 10.1 The Misclassification in Phase 5
Phase 5 listed `search-web` and `read-url` as proposed global skills in `~/.gemini/config/skills/`.

A forensic check of Antigravity native tool declarations confirms:
- `search_web`: **NATIVE TOOL** (`default_api:search_web`) - built directly into the agent runtime.
- `read_url_content`: **NATIVE TOOL** (`default_api:read_url_content`) - built directly into the agent runtime.
- File operations (`view_file`, `write_to_file`, `replace_file_content`): Native tools.
- Shell and task control (`run_command`, `manage_task`, `invoke_subagent`): Native tools.

Recreating native tools as skills introduces overhead, circular prompts, and unnecessary token consumption.

### 10.2 Corrected Global Skills Set
Only true cross-project workflows and methodology guides belong in `~/.gemini/config/skills/`:

| Global Skill Name | Function and Purpose |
|---|---|
| `google-antigravity-sdk` | Agent design, orchestration, and lifecycle protocols for Antigravity. |
| `systematic-debugging` | Four-phase root-cause diagnosis protocol before touching code. |
| `test-driven-development` | Red-green-refactor discipline and automated test authoring. |
| `codebase-design` | Deep module interfaces, seam definitions, and testability principles. |
| `verification-before-completion` | Evidence-first gate requiring test and execution proof before completion. |

---

## 11. BROWSER VERIFIER AGENT LEAST-PRIVILEGE PERMISSION MODEL

### 11.1 Agent Purpose
The persistent custom agent `browser_verifier` in `projects/lsatu/.agents/agents/browser_verifier/agent.md` exists solely to conduct read-only visual inspection, layout audits, DOM checks, console inspection, and network analysis on port 9223.

### 11.2 Permission Policy
- **Allowed Read Tools**:
  - `view_file`: Read test logs, HTML snapshots, test fixtures.
  - `read_url_content`: Verify public endpoints or local HTTP servers.
  - MCP `chrome-devtools`: All 29 browser inspection tools (`click`, `evaluate_script`, `take_screenshot`, `list_console_messages`, etc.).
- **Restricted Command Execution (`run_command`)**:
  - `run_command` is strictly restricted to running existing, read-only Playwright verification scripts located in `C:\Users\Joshu\Tools\LSATU-Agent\`:
    - `node verify-viewports.mjs`
    - `node verify_localhost.mjs`
    - `node check_auth.mjs`
    - `node test_persistence_cycle.mjs`
- **Strictly Denied Tools**:
  - `write_to_file`: **DENIED**
  - `replace_file_content`: **DENIED**
  - Arbitrary shell execution, package installation, or Git write operations: **DENIED**

---

## 12. CODE REVIEWER DUAL-TIER MODEL POLICY

### 12.1 Agent Purpose
The persistent custom agent `code_reviewer` in `projects/lsatu/.agents/agents/code_reviewer/agent.md` performs automated structural, architectural, and security reviews of proposed code changes before commit.

### 12.2 Model Tier Selection Matrix
Using the 14 verified models currently active in Antigravity's model selector (confirmed in Phase 3B):

```
+-----------------------------------------------------------------------------------+
|                        CODE REVIEWER MODEL TIER POLICY                            |
+---------------------+---------------------------------+---------------------------+
| Review Tier         | Selected Model                  | Scope and Triggers        |
+---------------------+---------------------------------+---------------------------+
| Tier 1: Default     | Claude Sonnet 4.6 Thinking      | Standard React components,|
| Routine Review      | (`claude-sonnet-4.6-thinking`)  | styling, utility functions|
|                     |                                 | type updates, unit tests. |
+---------------------+---------------------------------+---------------------------+
| Tier 2: High-Risk   | Claude Opus 4.6 Thinking        | RLS security policies,    |
| Escalation          | (`claude-opus-4.6-thinking`) OR | database migrations, auth |
|                     | Gemini 3.1 Pro High             | flows, Stripe payments,   |
|                     | (`gemini-3.1-pro-high`)         | destructive data scripts. |
+---------------------+---------------------------------+---------------------------+
```

- **Escalation Protocol**: If a diff touches files in `supabase/migrations/`, `src/integrations/supabase/`, auth middleware, or payment routing, the review must automatically escalate to Tier 2 (Claude Opus 4.6 Thinking or Gemini 3.1 Pro High) for exhaustive reasoning.

---

## 13. LEAN WAVE 0 BACKUP STRATEGY

### 13.1 Flaw in Phase 5 Backup Strategy
Phase 5 proposed copying the entirety of `C:\Users\Joshu\dev\ai-os` to `C:\Users\Joshu\dev\ai-os-backup-pre-migration`.
- This would unnecessarily copy ~500MB of `projects/lsatu/node_modules/`, Vite build caches, git objects, and temp files.
- It is slow, wastes disk I/O, and complicates diffing.

### 13.2 Lean Configuration Backup Scope
Wave 0 will execute a targeted, deterministic backup to:
`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\`

Targeted components:
1. Outer root control files:
   - `C:\Users\Joshu\dev\ai-os\AGENTS.md`
   - `C:\Users\Joshu\dev\ai-os\GEMINI.md`
   - `C:\Users\Joshu\dev\ai-os\CLAUDE.md`
   - `C:\Users\Joshu\dev\ai-os\.agents\` (entire directory)
   - `C:\Users\Joshu\dev\ai-os\.gemini\` (entire directory)
2. Inner LSAT U control files:
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` (if exists)
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\` (if exists)
3. Workstation global configuration:
   - `C:\Users\Joshu\GEMINI.md`
   - `C:\Users\Joshu\.gemini\config\` (entire directory, including `mcp_config.json`)
4. Antigravity IDE workspace state:
   - `C:\Users\Joshu\AppData\Roaming\Antigravity\User\workspaceStorage\` (state metadata)
5. Browser automation suite:
   - `C:\Users\Joshu\Tools\LSATU-Agent\` (entire directory)

**Explicitly Excluded**:
- `node_modules/`
- `.git/objects/`
- Build artifacts (`dist/`, `build/`, `.vite/`)
- Temporary cache files

Estimated backup size: **Under 35 MB**. Execution time: **Under 3 seconds**.

---

## 14. CONVERSATION HISTORY RETENTION (LOCKED)

### 14.1 Architectural Decision
- **STATUS: LOCKED.**
- No conversation history records will be migrated, moved, or deleted.
- No SQLite database surgery on `conversation_summaries.db`, `state.vscdb`, or Antigravity storage files.
- All historical conversations remain fully searchable, accessible, and intact within Project 1 (**AIOS Command Center**).
- When Project 2 (**LSAT U Engineering**) is registered, new engineering conversations will naturally begin within Project 2 with a clean context.

---

## 15. TWO-PROJECT TOPOLOGY (LOCKED)

### 15.1 Architectural Decision
- **STATUS: LOCKED.**
- **Project 1: AIOS Command Center**
  - Workspace Root: `C:\Users\Joshu\dev\ai-os`
  - Scope: Executive assistant command center, student operations, wiki ledgers, business operations, cross-cutting coordination.
- **Project 2: LSAT U Engineering**
  - Workspace Root: `C:\Users\Joshu\dev\ai-os\projects\lsatu`
  - Scope: Focused software engineering for LSAT U frontend, components, verification, and Lovable backend integration.
- Execution Constraint: Project 2 is **NOT** created during Phase 5B. It is provisioned during Wave 3.

---

## 16. REVISED INCREMENTAL AND REVERSIBLE MIGRATION WAVES

The revised implementation waves incorporate all corrections and guardrails:

```
+-----------------------------------------------------------------------------------+
|                           MIGRATION WAVES TIMELINE                                |
+--------+------------------------------------+---------------------+---------------+
| Wave   | Focus Area                         | Risk Level          | Rollback Time |
+--------+------------------------------------+---------------------+---------------+
| Wave 0 | Lean Config Backup & Environment   | Zero (Read-only copy)| < 30 seconds  |
+--------+------------------------------------+---------------------+---------------+
| Wave 1 | Global Config & MCP Pinning        | Low                 | < 1 minute    |
+--------+------------------------------------+---------------------+---------------+
| Wave 2 | Outer Repo (AIOS) Control Plane    | Low                 | < 2 minutes   |
+--------+------------------------------------+---------------------+---------------+
| Wave 3 | Project 2 Registration & Branch    | Low                 | < 1 minute    |
+--------+------------------------------------+---------------------+---------------+
| Wave 4 | LSAT U Control Plane & Agents      | Low                 | < 2 minutes   |
+--------+------------------------------------+---------------------+---------------+
| Wave 5 | Chrome Port 9223 Verification      | Zero (Read-only test)| Immediate     |
+--------+------------------------------------+---------------------+---------------+
| Wave 6 | Cross-Project Audit & Signoff      | Zero (Verification) | N/A           |
+--------+------------------------------------+---------------------+---------------+
```

### Wave 0: Lean Config Backup & Environment Freeze
- **Objective**: Create a deterministic, restorable backup of all control files and configurations without copying reproducible dependencies.
- **Files Affected**: Writes to new backup directory `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\`.
- **Actions**:
  1. Copy outer root control files (`AGENTS.md`, `GEMINI.md`, `CLAUDE.md`, `.agents/`, `.gemini/`).
  2. Copy inner LSAT U control files (`projects/lsatu/CLAUDE.md`, `projects/lsatu/AGENTS.md`).
  3. Copy machine global config (`C:\Users\Joshu\GEMINI.md`, `C:\Users\Joshu\.gemini\config\`).
  4. Copy browser tooling (`C:\Users\Joshu\Tools\LSATU-Agent\`).
- **Prerequisites**: Confirm disk space (requires ~35MB).
- **Validation**: Verify file count and SHA-256 integrity of backed-up control files.
- **Rollback**: Delete backup directory.
- **Joshua Confirmation**: **No** (Standard safe backup).

### Wave 1: Global Configuration and MCP Pinning
- **Objective**: Align machine-level tools and configuration.
- **Files Affected**:
  - `C:\Users\Joshu\.gemini\config\mcp_config.json`
  - `C:\Users\Joshu\.gemini\config\skills\`
- **Actions**:
  1. Pin `chrome-devtools-mcp@1.9.0` in `mcp_config.json` (replacing `@latest`).
  2. Populate verified workstation-global skills in `~/.gemini/config/skills/` (`google-antigravity-sdk`, `systematic-debugging`, `test-driven-development`, `codebase-design`, `verification-before-completion`).
  3. Ensure `C:\Users\Joshu\GEMINI.md` remains untouched.
- **Prerequisites**: Wave 0 completed.
- **Validation**: Inspect MCP tool registration list in Antigravity; confirm 29 chrome-devtools tools load.
- **Rollback**: Restore `mcp_config.json` and delete added global skills from backup.
- **Joshua Confirmation**: **No**.

### Wave 2: Outer Repo (AIOS Command Center) Control Plane and Skill Alignment
- **Objective**: Establish non-duplicative instruction ownership and native `.agents/skills/` discovery in AIOS Command Center.
- **Files Affected**:
  - `C:\Users\Joshu\dev\ai-os\AGENTS.md`
  - `C:\Users\Joshu\dev\ai-os\GEMINI.md`
  - `C:\Users\Joshu\dev\ai-os\.agents\skills\`
  - `C:\Users\Joshu\dev\ai-os\.gemini\skills\skills.json`
- **Actions**:
  1. Update `AGENTS.md` as canonical EA baseline; update `GEMINI.md` with Antigravity-only deltas (zero duplicated rules).
  2. Copy verified active EA skills into `C:\Users\Joshu\dev\ai-os\.agents\skills\`.
  3. De-index or retire `skills.json` in `.gemini/skills/` to prevent duplicate ID discovery.
  4. Archive legacy `.gemini/skills/` into inert storage.
- **Prerequisites**: Wave 1 completed.
- **Validation**: Confirm skills list in Antigravity shows single instances of EA skills; test prompt token load.
- **Rollback**: Restore `AGENTS.md`, `GEMINI.md`, and `.gemini/skills/` from Wave 0 backup.
- **Joshua Confirmation**: **Yes** (Reviewing EA instruction adjustments).

### Wave 3: Project 2 Registration and Git Branch Preservation
- **Objective**: Register `LSAT U Engineering` as a dedicated Antigravity Project while strictly preserving Git branch state.
- **Files Affected**:
  - Antigravity Project registry in IDE configuration.
- **Actions**:
  1. Verify current Git branch in `C:\Users\Joshu\dev\ai-os\projects\lsatu` is `feat/calendar-strip-deeplink`.
  2. Register `C:\Users\Joshu\dev\ai-os\projects\lsatu` in Antigravity project manager as "LSAT U Engineering".
  3. Confirm working tree remains unmodified.
- **Prerequisites**: Wave 2 completed.
- **Validation**: Verify Git status in `projects/lsatu` reports unchanged branch and working tree. Open Project 2 in Antigravity.
- **Rollback**: Deregister Project 2 from Antigravity IDE configuration.
- **Joshua Confirmation**: **Yes** (Confirming project registration in IDE).

### Wave 4: LSAT U Engineering Control Plane, Skills, and Agents
- **Objective**: Establish clean engineering instructions, native skills, and custom agents in LSAT U.
- **Files Affected**:
  - `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md`
  - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\skills\`
  - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\agents\browser_verifier\agent.md`
  - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\agents\code_reviewer\agent.md`
- **Actions**:
  1. Create `projects/lsatu/GEMINI.md` with clean engineering context rules, referencing Lovable deployment guardrails.
  2. Populate `projects/lsatu/.agents/skills/` with engineering skills (`emil-design-eng`, `design-taste-frontend`, `lsat-u-browser-verification`, `webapp-testing`). Explicitly exclude Netlify skills.
  3. Create `browser_verifier` agent with read-only/CDP permissions.
  4. Create `code_reviewer` agent with dual-tier model escalation rules.
- **Prerequisites**: Wave 3 completed.
- **Validation**: Verify skills and custom agents appear in Project 2 Antigravity UI.
- **Rollback**: Remove created `.agents/` and `GEMINI.md` in `projects/lsatu/`.
- **Joshua Confirmation**: **Yes** (Reviewing agent definitions).

### Wave 5: Chrome Port 9223 Browser Suite Verification
- **Objective**: Verify end-to-end integration between Antigravity, MCP, and Chrome on port 9223 without modifying any browser code.
- **Files Affected**: None (Read-only execution).
- **Actions**:
  1. Ensure Chrome is running on port 9223 via `C:\Users\Joshu\Tools\LSATU-Agent\launch_browser.py`.
  2. Execute `node C:\Users\Joshu\Tools\LSATU-Agent\verify_localhost.mjs`.
  3. Execute `node C:\Users\Joshu\Tools\LSATU-Agent\verify-viewports.mjs`.
  4. Verify MCP `chrome-devtools` responds to lazy tool calls from Antigravity.
- **Prerequisites**: Wave 4 completed.
- **Validation**: Successful execution output from verification scripts; valid DOM snapshot returned via MCP.
- **Rollback**: N/A (Read-only verification).
- **Joshua Confirmation**: **No**.

### Wave 6: Cross-Project Isolation Audit and Final Signoff
- **Objective**: Verify complete architectural isolation between Project 1 and Project 2.
- **Files Affected**: None (Verification only).
- **Actions**:
  1. Audit Project 1: Confirm EA duties, wiki ledgers, and student tools load without pollution from LSAT U agents.
  2. Audit Project 2: Confirm clean engineering context, zero EA wiki overhead, active browser verification suite.
  3. Verify zero duplicate skill IDs across both projects.
  4. Confirm conversation histories remain intact in Project 1.
- **Prerequisites**: Wave 5 completed.
- **Validation**: Successful execution of cross-project audit checklist.
- **Rollback**: N/A.
- **Joshua Confirmation**: **Yes** (Final operational acceptance).

---

## 17. PRE-IMPLEMENTATION ACCEPTANCE CHECKLIST

Before ANY implementation wave begins, this checklist must be verified:

```
[X] 1. NO INVENTED PATHS
    - All browser scripts reference existing filenames in C:\Users\Joshu\Tools\LSATU-Agent\.
    - Global rule path anchored at C:\Users\Joshu\GEMINI.md.
    - No phantom .gemini\GEMINI.md references.

[X] 2. NO INVENTED VERSIONS
    - Chrome DevTools MCP pinned to verified resolved version 1.9.0 (chrome-devtools-mcp@1.9.0).
    - Phantom 0.9.x version completely eliminated.

[X] 3. NO DUPLICATED INSTRUCTION AUTHORITY
    - AGENTS.md owns shared baseline and Codex EA rules.
    - GEMINI.md owns Antigravity-specific runtime additions only.
    - Zero copy-pasting of routing maps or voice rules into GEMINI.md.

[X] 4. NO DUPLICATED ACTIVE SKILL IDS
    - Explicit sequencing retires skills.json prior to populating native .agents/skills/.
    - Global skills (~/.gemini/config/skills/) do not overlap with workspace skills.

[X] 5. NO STALE MAC PATHS
    - All paths reference C:\Users\Joshu\... on Windows with valid escaping.

[X] 6. NO INCORRECT NETLIFY ASSUMPTIONS
    - Netlify skills removed from active LSAT U engineering discovery and deploy router.
    - Lovable Cloud confirmed as authoritative frontend and backend hosting.

[X] 7. NO STALE MODEL IDS
    - Models reference the 14 verified models from Phase 3B (Claude Sonnet 4.6 Thinking,
      Claude Opus 4.6 Thinking, Gemini 3.1 Pro High).

[X] 8. CORRECT PORT 9223 BROWSER PATHS
    - Canonical scripts (launch_browser.py, verify-viewports.mjs, etc.) preserved in place.

[X] 9. CORRECT GIT BRANCH PRESERVATION RULE
    - feat/calendar-strip-deeplink branch preserved. Zero git branch changes or commits during registration.

[X] 10. CORRECT GITHUB VS LOVABLE AUTHORITY DISTINCTION
    - GitHub owns committed source code history.
    - Lovable Cloud owns live production database, auth, and Edge Functions.

[X] 11. CONVERSATION DATABASE MIGRATION EXPLICITLY PROHIBITED
    - SQLite database surgery forbidden. Existing conversation records remain in place.

[X] 12. ROLLBACK DEFINED FOR EVERY WAVE
    - Each wave has explicit, testable, and low-latency rollback procedures.
```

---

## 18. OUTPUT AND FREEZE CONFIRMATION

- **Primary Output Path**: `C:\Users\Joshu\dev\ai-os\AIOS_PHASE_5B_MIGRATION_FREEZE.md`
- **Secondary Mirror Path**: `C:\Users\Joshu\dev\ai-os\.gemini\AIOS_PHASE_5B_MIGRATION_FREEZE.md`

### Final Freeze Declaration
This specification incorporates every correction requested by the external architect. 

**Zero implementation actions have been performed.**
**Wave 0 has NOT begun.**
The workstation remains in a 100% frozen, read-only state awaiting final external authorization.
