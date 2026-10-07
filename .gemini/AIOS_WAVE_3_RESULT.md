# AIOS WAVE 3 RESULT: ANTIGRAVITY SKILL DISCOVERY ISOLATION AND CLEANUP

- **Wave Status**: **BLOCKED** (Mandatory Stop Condition Triggered: Clean Project-Specific Discovery Requires Touching Protected `.agents/**`)
- **Timestamp**: 2026-09-20T05:05:00-04:00
- **Execution Scope**: Wave 3 (Antigravity Skill Discovery Isolation and Cleanup)
- **Primary Report Path**: [`C:\Users\Joshu\dev\ai-os\AIOS_WAVE_3_RESULT.md`](file:///C:/Users/Joshu/dev/ai-os/AIOS_WAVE_3_RESULT.md)
- **Report Mirror**: [`C:\Users\Joshu\dev\ai-os\.gemini\AIOS_WAVE_3_RESULT.md`](file:///C:/Users/Joshu/dev/ai-os/.gemini/AIOS_WAVE_3_RESULT.md)

---

## 1. EXECUTIVE SUMMARY AND STOP CONDITION TRIGGER

Wave 3 has stopped cleanly at the mandatory **STOP CONDITION** with a status of **BLOCKED**.

### The Stop Condition:
> "If clean project-specific Antigravity skill discovery CANNOT be implemented without writing into `.agents/**`: STOP. Do not alter skill discovery. Create the Wave 3 report explaining the limitation and safest alternative. Codex isolation is more important than Antigravity skill convenience."

### The Technical Reality:
Reverse-engineering of the installed Antigravity 2.15.0 language server (`language_server.exe`) and inspection of official customization documentation (`agy-customizations`) proves:
1. **Hardcoded Workspace Discovery Root**: Antigravity's workspace-level customization walker discovers project-specific customizations **only** by searching for `.agents/` (or `.agent/`, `_agents/`, `_agent/`) walking up from the current directory.
2. **Project-Local `skills.json` Location**: The only project-local location Antigravity checks for a declarative `skills.json` is `<workspace_root>/.agents/skills.json`. It does **not** recognize `.gemini/skills.json` as a project customization root.
3. **No Project Scoping in Global Config**: Global `~/.gemini/config/skills.json` supports path filtering (`include_only` and `exclude`), but does **not** support project-scoping conditionals or workspace targeting. Any entry in `~/.gemini/config/skills.json` applies globally to all projects on the machine.
4. **Project Config Limitation**: Antigravity Project definitions in `~/.gemini/config/projects/<id>.json` contain only repository resources, folder URIs, and execution settings. They have no schema fields for skill declarations.

Because configuring true project-specific skill surfaces in Antigravity is technically impossible without creating or writing into `<workspace_root>/.agents/skills.json`, and because `.agents/**` is strictly protected Codex-first infrastructure that Antigravity must never modify:
**The STOP CONDITION was triggered. Skill discovery was not altered, and zero configuration or source files were modified.**

---

## 2. EXACT ANTIGRAVITY SKILL CONFIG SCHEMA VERIFIED

Inspection of the binary strings, Go symbols (`customizations.ProcessSkillsConfigFileToSpecs`), and embedded docs (`agy-customizations/docs/json_configs.md`) confirmed the exact supported schema of `skills.json`:

```json
{
  "inherits": [
    {
      "path": "/path/to/shared/skills.json",
      "include_only": ["linter-skill"],
      "exclude": ["deprecated-skill"]
    }
  ],
  "entries": [
    {
      "path": "path/to/skills/directory",
      "include_only": ["pattern-.*"],
      "exclude": ["experimental-.*"]
    }
  ]
}
```

### Schema Properties:
- **`entries`** (array of objects): List of directories to scan for skills.
- **`inherits`** (array of objects): Other `skills.json` files to inherit and merge.
- **`path`** (string, required): Absolute path (`/...`), home-relative path (`~/...`), or workspace-relative path (relative to git root).
- **`include_only`** (array of regex strings, optional): Whitelist of regex patterns. If present, only skill subdirectories matching at least one pattern are loaded.
- **`exclude`** (array of regex strings, optional): Blacklist of regex patterns. Matching skill subdirectories are skipped.
- **Unsupported / Non-Existent Fields**: There are no fields for `project`, `workspace_id`, `scope`, `profiles`, or environment conditions.

---

## 3. PROJECT-LOCAL SKILLS.JSON MECHANISM AND LIMITATION

| Question | Runtime Evidence | Architectural Finding |
|---|---|---|
| **Does Antigravity 2.15.0 support project-local `skills.json`?** | YES | Supported natively by the language server. |
| **Exact allowed location for project-local `skills.json`?** | `<workspace_root>/.agents/skills.json` | Hardcoded to `.agents/` (and `.agent/`, `_agents/`, `_agent/`). |
| **Does Antigravity check `.gemini/skills.json`?** | **NO** | Binary search confirms `.gemini` is only checked in user home `~/.gemini/config/`. |
| **Can project-local `skills.json` be set up without writing to `.agents/**`?** | **NO** | Placing `skills.json` anywhere outside `.agents/` results in Antigravity ignoring it. |
| **Can `.agents/skills.json` reference Gemini-owned paths?** | YES (`{"entries": [{"path": ".gemini/active-skills"}]}`) | But the JSON file itself must reside in `.agents/`, violating Codex isolation. |
| **How does workspace configuration merge with global?** | Merges with priority: Workspace `.agents/` > Workspace `skills.json` > Global `~/.gemini/config/` > Builtins > Global `skills.json`. |
| **Reload mechanism?** | File system watcher (`fsnotify`) triggers automatic reload on config save. |

---

## 4. INVENTORY OF CURRENT SKILL SOURCES

A complete scan across all physical skill locations on the workstation yielded **459 total skills** (324 unique IDs, 118 duplicate IDs):

| Discovery Source | Path | Physical Skill Count | Governance / Ownership |
|---|---|---|---|
| **Built-in Skills** | `C:\Users\Joshu\.gemini\antigravity\builtin\skills\` | 5 | Antigravity internal binaries (`agy-customizations`, `generative_ui`, etc.) |
| **Plugin Skills** | `C:\Users\Joshu\.gemini\config\plugins\` | 46 | 5 installed plugins |
| **Gemini Global** | `C:\Users\Joshu\.gemini\config\skills\` | 33 | Official Google DataCloud bundle (`.datacloud_skills_manifest`) + utility |
| **Gemini Workspace Library** | `C:\Users\Joshu\dev\ai-os\.gemini\skills\` | 274 | Preserved legacy library (includes forks, snapshots, inactive) |
| **AIOS Codex Workspace** | `C:\Users\Joshu\dev\ai-os\.agents\skills\` | 11 | Protected Codex active skills |
| **LSAT U Codex Workspace** | `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\skills\` | 90 | Protected Codex LSAT U skills |
| **Total Scanned** | | **459** | |

---

## 5. COMPLETE DUPLICATE-ID ANALYSIS

The scan identified 118 duplicate skill IDs. The two most critical collision clusters are:

### Cluster 1: The 11 Immediate Collisions Between `.agents/skills` and `.gemini/skills`
Because `C:\Users\Joshu\.gemini\config\skills.json` explicitly registered both `C:/Users/Joshu/dev/ai-os/.gemini/skills` and `C:/Users/Joshu/dev/ai-os/.agents/skills`, all 11 Codex skills were dual-discovered:
1. `domain-modeling`
2. `grill-with-docs`
3. `grilling`
4. `gws-gmail`
5. `gws-gmail-read`
6. `gws-gmail-triage`
7. `gws-shared`
8. `kling-cli`
9. `pre-consultation-check-in`
10. `session-recap`
11. `superwhisper`

### Cluster 2: Plugin vs Global DataCloud Duplication (Hyphen vs Underscore)
All 32 BigQuery and GCP data skills in `~/.gemini/config/skills/` (e.g. `bigquery-sql`, `bigquery-graph`) duplicate the 32 skills in `data-agent-kit-plugin` (e.g. `bigquery_sql`, `bigquery_graph`). Both versions are injected into the prompt simultaneously, consuming double the token budget.

### Cluster 3: Plugin Snapshots in Workspace Library
Skills like `a11y-debugging`, `chrome-devtools`, and `troubleshooting` are provided by `chrome-devtools-plugin` and also duplicated in `C:\Users\Joshu\dev\ai-os\.gemini\skills\_snapshots\`.

---

## 6. CLASSIFICATION OF THE 33 GLOBAL SKILLS

Investigation of `C:\Users\Joshu\.gemini\config\skills\` revealed that 32 of the 33 skills are tracked by a formal bundle manifest:
`C:\Users\Joshu\.gemini\config\skills\.datacloud_skills_manifest`
(Bundle checksum: `c13b95c3f059c90a82ae459696806e06d975ed342da645791b05fadd30bb2c3a`).

- **32 Skills**: Official Google DataCloud skill bundle (`bigquery-*`, `gcp-*`, `dataform-*`, `dbt-*`). None are user-authored or relevant to LSAT U or business tutoring operations.
- **1 Skill**: `skill-repair` (Antigravity installation repair utility).
- **Provenance**: Known vendor bundle. None are personal or custom.

---

## 7. PLUGIN-OWNED SKILL ANALYSIS

The 5 installed plugins in `C:\Users\Joshu\.gemini\config\plugins\` provide 46 skills:
1. **`chrome-devtools-plugin`** (5 skills): `a11y-debugging`, `chrome-devtools`, `debug-optimize-lcp`, `memory-leak-debugging`, `troubleshooting`.
2. **`data-agent-kit-plugin`** (34 skills): Google Cloud and BigQuery developer tools.
3. **`gemini-api`** (4 skills): `gemini-api-dev`, `gemini-interactions-api`, `gemini-live-api-dev`, `gemini-omni-flash-api`.
4. **`google-antigravity-sdk`** (1 skill): `google-antigravity-sdk`.
5. **`modern-web-guidance-plugin`** (2 skills): `chrome-extensions`, `modern-web-guidance`.

Per the Plugin Duplication Rule (Step 4), these skills are owned by their plugins and must never be manually copied into workspace directories.

---

## 8. RECOMMENDED ACTIVE SKILL SURFACES (EVIDENCE-BASED DESIGN)

When the external architect decides how to resolve the Stop Condition, the active surfaces should be restricted to:

### Surface A: Universal Antigravity (Cross-Project)
- `chrome-devtools` (from plugin)
- `systematic-debugging`
- `diagnosing-bugs`
- `verification-before-completion`
- `executing-plans`
- `writing-plans`

### Surface B: AIOS Command Center (Operations)
- `gws-gmail`
- `gws-calendar`
- `gws-drive`
- `gws-docs`
- `consultation-inquiry-drafts`
- `consultation-followup-drafts`
- `inbound-tutoring-replies`
- `level-up`
- `audit`
- `superwhisper`
- `prompt-architect-refiner`

### Surface C: LSAT U Engineering (Platform Code)
- `lsat-u-browser-verification`
- `emil-design-eng`
- `design-taste-frontend`
- `frontend-design`
- `subagent-driven-development`
- `tdd`
- `pull-submissions`
- `loophole-lecture-transcribe`

*(Netlify production skills excluded per architecture directions).*

---

## 9. EXACT FILES CHANGED OR MOVED

- **Files Created**: **0**.
- **Files Modified**: **0**.
- **Files Deleted**: **0**.
- **Files Moved**: **0**.

In compliance with the Stop Condition, zero mutations were performed.

---

## 10. BEFORE AND AFTER METRICS (MEASURED)

| Metric | Pre-Wave Baseline | Post-Wave State | Delta |
|---|---|---|---|
| Exposed Skills in Prompt | 67 | 67 | 0 (Preserved) |
| Excluded / Suppressed Skills | 197 | 197 | 0 (Preserved) |
| Active Prompt Description Tokens | ~6,500 | ~6,500 | 0 (Preserved) |
| Duplicate IDs Across Directories | 118 | 118 | 0 (Preserved) |
| Explicit Registrations in `skills.json` | 2 (`.gemini/skills`, `.agents/skills`) | 2 (`.gemini/skills`, `.agents/skills`) | 0 (Preserved) |

---

## 11. PROTECTED RUNTIME INTEGRITY VERIFICATION

Re-execution of cryptographic SHA-256 checks across all 6 Wave 0 baseline manifests confirms:

| Manifest Name | Scope | Total Files | Verification Status |
|---|---|---|---|
| `protected_aios_agents_manifest.json` | Root `.agents/**` | 27 | **27 / 27 (100% IDENTICAL)** |
| `protected_aios_claude_manifest.json` | Root `.claude/**` | 14 | **14 / 14 (100% IDENTICAL)** |
| `protected_lsatu_agents_manifest.json` | LSAT U `.agents/**` | 493 | **493 / 493 (100% IDENTICAL)** |
| `protected_lsatu_claude_manifest.json` | LSAT U `.claude/**` | 475 | **475 / 475 (100% IDENTICAL)** |
| `protected_skills_claude_manifest.json` | `skills/claude/**` | 1,178 | **1,178 / 1,178 (100% IDENTICAL)** |
| `protected_skills_codex_manifest.json` | `skills/codex/**` | 1,054 | **1,054 / 1,054 (100% IDENTICAL)** |
| **Total Protected Files** | **All Protected Runtimes** | **3,241** | **3,241 / 3,241 (0 MISMATCHES)** |

Core instruction files (`AGENTS.md` and `CLAUDE.md` in both roots) are 100% byte-identical.

---

## 12. GIT STATE

- **`C:\Users\Joshu\dev\ai-os`**: Active branch `main`, clean working tree (only Wave 2's `GEMINI.md` unstaged modification + untracked reports/scratch).
- **`C:\Users\Joshu\dev\ai-os\projects\lsatu`**: Active branch `feat/calendar-strip-deeplink`, preserved working tree (35 unstaged, 42 untracked).
- Zero Git operations performed.

---

## 13. ARCHITECTURAL ALTERNATIVES FOR EXTERNAL APPROVAL

Because Antigravity does not support `.gemini/skills.json` at the project level, the external architect has two viable paths:

### Path 1: Curated Global Whitelist (Recommended - Zero Cross-Runtime Touch)
- **Mechanism**: Use `~/.gemini/config/skills.json` with an explicit `include_only` regex array containing only the ~25 essential skills from `C:/Users/Joshu/dev/ai-os/.gemini/skills/`.
- **Action**: Remove `C:/Users/Joshu/dev/ai-os/.agents/skills` from `skills.json`.
- **Advantage**:
  - Requires **zero writes to `.agents/**` in either repository**.
  - Eliminates all 11 duplicate collisions.
  - Drops prompt token overhead from ~6,500 to ~1,200 tokens across all sessions.
  - Leaves the 274-skill physical library intact.
- **Tradeoff**: Both Project 1 and Project 2 share the same curated ~25-skill whitelist rather than strictly isolated project-specific surfaces.

### Path 2: Authorized Project Pointers in `.agents/skills.json`
- **Mechanism**: The architect explicitly authorizes Antigravity to create a single read-only pointer file in `C:\Users\Joshu\dev\ai-os\.agents\skills.json` and `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\skills.json`.
- **Action**: These pointer files point to `.gemini/active-skills/aios` and `.gemini/active-skills/lsatu` respectively.
- **Advantage**: Achieves 100% project isolation between AIOS and LSAT U.
- **Tradeoff**: Violates the absolute ban against creating files inside `.agents/**`.

---

## 14. FINAL VERDICT AND HARD STOP

- **Final Status**: **BLOCKED** (Safely halted at Stop Condition).
- **Hard Stop Enforced**: Wave 4 has **not** begun.
- **Workstation Integrity**: 100% stable, verified, and protected.
- Awaiting external architect evaluation and direction between Path 1 and Path 2.
