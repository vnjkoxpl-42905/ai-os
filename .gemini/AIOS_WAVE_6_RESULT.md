# Wave 6: Mechanical Codex / Claude Protection Guard

## 1. Executive Summary

Wave 6 establishes a mechanical protection guard that prevents Antigravity from mutating Codex-owned or Claude-owned configuration files and directories while preserving complete read-only access.

Crucially, this guard operates strictly within Antigravity:
- Windows ACLs and filesystem permissions were intentionally NOT modified. Codex and Claude run under the identical Windows user account (`J\Joshu`). Applying NTFS write denials would break Codex and Claude.
- The guard is implemented using Antigravity 2.15.0 native lifecycle hooks (`PreToolUse`), intercepting mutation attempts synchronously before tool execution.
- Codex and Claude continue to possess full, unrestricted write access to their own directories.
- Antigravity retains read access across all repositories, as well as full write access to its own configuration (`GEMINI.md`, `.gemini/**`, `~/.gemini/**`) and normal application code.

All 3,241 protected baseline files across the six baseline manifests remain 100% byte-identical.

---

## 2. Guard Architecture

### 2.1 Mechanism Selection and Rationale

| Mechanism Considered | Decision | Rationale |
| :--- | :--- | :--- |
| **Windows NTFS ACLs** | **REJECTED** | Codex, Claude, and Antigravity execute under the identical OS user account (`J\Joshu`). Applying NTFS write-deny ACLs would block Codex and Claude from modifying their own files. |
| **Protected Directory Edits** | **REJECTED** | Violates the absolute boundary rule. Protected directories (`.agents`, `.codex`, `.claude`) must remain pristine. |
| **Prompt-Only Instructions** | **INSUFFICIENT** | Does not provide mechanical guarantees against accidental tool calls or hallucinated mutations. |
| **Antigravity Native Lifecycle Hook (`PreToolUse`)** | **SELECTED** | Native Go language server implementation in Antigravity 2.15.0 (`google3/third_party/jetski/cortex/customization/hooks/jsonhook`). Intercepts tool calls before execution on `stdin`/`stdout`. Returning `{"decision": "deny", "reason": "..."}` aborts the tool call instantly. |

### 2.2 Component Locations and Cryptographic Hashes

1. **Global Hook Definition**:
   - Path: `C:\Users\Joshu\.gemini\config\hooks.json`
   - Repository Mirror: `C:\Users\Joshu\dev\ai-os\.gemini\hooks.json`
   - SHA-256: `9D979F00BFB0F0639B2AD8E73A11EBDF72D87FADA14AA93DD3408971E6B6F1AE`

2. **Guard Enforcement Script**:
   - Path: `C:\Users\Joshu\.gemini\config\scripts\guard_protected_runtime_paths.py`
   - Repository Mirror: `C:\Users\Joshu\dev\ai-os\.gemini\scripts\guard_protected_runtime_paths.py`
   - SHA-256: `06F9970875CDFF101707A92A3E2B94DB40F03198CA2B6C4194745F0E6677E958`

### 2.3 Hook Configuration (`hooks.json`)

```json
{
  "codex-claude-guard": {
    "enabled": true,
    "PreToolUse": [
      {
        "matcher": "write_to_file|replace_file_content|run_command",
        "hooks": [
          {
            "type": "command",
            "command": "python C:\\Users\\Joshu\\.gemini\\config\\scripts\\guard_protected_runtime_paths.py",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### 2.4 Guard Logic and Normalization

The guard script (`guard_protected_runtime_paths.py`) implements deterministic protection rules:

1. **Path Normalization**:
   - Strips quotes and extended-length prefixes (`\\?\`).
   - Resolves environment variables and relative paths using command working directory or workspace root.
   - Normalizes path separators to standard backslashes via `os.path.normpath` and `os.path.abspath`.
   - Converts all paths to lower-case for Windows case-insensitive comparison.

2. **Protected Target Registry**:
   - **Root AIOS Files**: `C:\Users\Joshu\dev\ai-os\AGENTS.md`, `C:\Users\Joshu\dev\ai-os\CLAUDE.md`.
   - **Root AIOS Directories**: `C:\Users\Joshu\dev\ai-os\.agents`, `\.codex`, `\.claude`, `\skills\codex`, `\skills\claude`.
   - **LSAT U Files**: `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md`, `CLAUDE.md`.
   - **LSAT U Directories**: `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents`, `\.codex`, `\.claude`.

3. **Tool Evaluation**:
   - Direct file writing tools (`write_to_file`, `replace_file_content`):
     Inspects `TargetFile`. If target matches a protected file or falls inside a protected directory, returns `decision: deny`.
   - Shell execution tool (`run_command`):
     Scans `CommandLine` for sensitive tokens (`agents.md`, `claude.md`, `.agents`, `.codex`, `.claude`, `skills/codex`, `skills/claude`). If present, checks for mutating patterns (redirections `>`, `>>`, PowerShell file writes `Set-Content`, `Add-Content`, `Out-File`, deletions `Remove-Item`, `del`, `rmdir`, moves `Move-Item`, renames `Rename-Item`, git checkouts/restores `git checkout`, `git restore`, in-place file writes). Mutating commands return `decision: deny`. Read-only commands (`Get-Content`, `cat`, `git diff`, `git status`, `Get-FileHash`, `grep`) return `decision: allow`.

---

## 3. Test Matrix and Verification Results

All 29 test cases across 11 test categories were executed against the guard script. 100% of test cases passed.

| ID | Test Category | Target / Command | Expected | Actual | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Case 1** | Root AIOS protected file | `write_to_file` on `AGENTS.md` | deny | deny | **PASS** |
| **Case 1b** | Root AIOS protected file | `write_to_file` on `CLAUDE.md` | deny | deny | **PASS** |
| **Case 1c** | Root AIOS protected file (lower) | `replace_file_content` on `agents.md` | deny | deny | **PASS** |
| **Case 2** | Root AIOS protected dir | `write_to_file` in `.agents/skills/...` | deny | deny | **PASS** |
| **Case 2b** | Root AIOS protected dir | `write_to_file` in `.codex/config.json` | deny | deny | **PASS** |
| **Case 2c** | Root AIOS protected dir | `replace_file_content` in `.claude/settings.json` | deny | deny | **PASS** |
| **Case 2d** | Root AIOS protected dir | `write_to_file` in `skills/codex/...` | deny | deny | **PASS** |
| **Case 2e** | Root AIOS protected dir | `write_to_file` in `skills/claude/...` | deny | deny | **PASS** |
| **Case 3** | LSAT U protected file | `replace_file_content` on `projects/lsatu/AGENTS.md` | deny | deny | **PASS** |
| **Case 3b** | LSAT U protected file | `write_to_file` on `projects/lsatu/CLAUDE.md` | deny | deny | **PASS** |
| **Case 4** | LSAT U protected dir | `write_to_file` in `projects/lsatu/.agents/...` | deny | deny | **PASS** |
| **Case 4b** | LSAT U protected dir | `write_to_file` in `projects/lsatu/.codex/...` | deny | deny | **PASS** |
| **Case 4c** | LSAT U protected dir | `write_to_file` in `projects/lsatu/.claude/...` | deny | deny | **PASS** |
| **Case 5** | Shell mutation on file | `Set-Content -Path CLAUDE.md` | deny | deny | **PASS** |
| **Case 5b** | Shell mutation on file | `echo test > AGENTS.md` | deny | deny | **PASS** |
| **Case 5c** | Shell mutation on file | `git checkout -- projects/lsatu/AGENTS.md` | deny | deny | **PASS** |
| **Case 6** | Shell mutation on dir | `Remove-Item -Recurse -Force .agents` | deny | deny | **PASS** |
| **Case 6b** | Shell mutation on dir | `del /f /s /q skills\codex\*` | deny | deny | **PASS** |
| **Case 6c** | Shell mutation on dir | `git restore projects/lsatu/.claude` | deny | deny | **PASS** |
| **Case 7** | Shell read on file | `Get-Content AGENTS.md` | allow | allow | **PASS** |
| **Case 7b** | Shell read on file | `Get-FileHash CLAUDE.md` | allow | allow | **PASS** |
| **Case 7c** | Shell read on file | `git diff AGENTS.md` | allow | allow | **PASS** |
| **Case 8** | Shell read on dir | `git status` | allow | allow | **PASS** |
| **Case 8b** | Shell read on dir | `git diff .agents` | allow | allow | **PASS** |
| **Case 8c** | Shell read on dir | `grep -rn "test" skills/codex` | allow | allow | **PASS** |
| **Case 9** | Gemini-owned file write | `write_to_file` on `GEMINI.md` | allow | allow | **PASS** |
| **Case 10** | Gemini-owned dir write | `write_to_file` in `.gemini/...` | allow | allow | **PASS** |
| **Case 11** | Workspace source write | `write_to_file` in `projects/lsatu/src/...` | allow | allow | **PASS** |
| **Case 11b**| Workspace doc write | `write_to_file` on `AIOS_WAVE_6_RESULT.md` | allow | allow | **PASS** |

Test Summary: 29 executed, 29 passed (100.0%).

---

## 4. Impact on Codex and Claude

1. **Windows NTFS ACLs**:
   Inspected via `Get-Acl`. Security descriptors are untouched. `J\Joshu` retains `FullControl` and `BUILTIN\Administrators` retains `FullControl`. No write denials exist at the filesystem level.
2. **Runtime Independence**:
   Codex and Claude are completely unaffected by Antigravity's lifecycle hooks. They continue to run independently with full read and write capabilities.
3. **Protected Directory Integrity**:
   Zero files were created, modified, renamed, or deleted in:
   - `C:\Users\Joshu\dev\ai-os\.agents\`
   - `C:\Users\Joshu\dev\ai-os\.codex\`
   - `C:\Users\Joshu\dev\ai-os\.claude\`
   - `C:\Users\Joshu\dev\ai-os\skills\codex\`
   - `C:\Users\Joshu\dev\ai-os\skills\claude\`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.agents\`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.codex\`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\.claude\`

---

## 5. Baseline Manifest Verification

Re-verification of all six baseline manifests generated in Wave 0 was performed across all 3,241 protected files.

| Manifest File | Total Files | Identical | Modified | Missing | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `protected_aios_agents_manifest.json` | 27 | 27 | 0 | 0 | **VERIFIED** |
| `protected_aios_claude_manifest.json` | 14 | 14 | 0 | 0 | **VERIFIED** |
| `protected_lsatu_agents_manifest.json` | 493 | 493 | 0 | 0 | **VERIFIED** |
| `protected_lsatu_claude_manifest.json` | 475 | 475 | 0 | 0 | **VERIFIED** |
| `protected_skills_claude_manifest.json` | 1,178 | 1,178 | 0 | 0 | **VERIFIED** |
| `protected_skills_codex_manifest.json` | 1,054 | 1,054 | 0 | 0 | **VERIFIED** |
| **TOTAL** | **3,241** | **3,241** | **0** | **0** | **100.0%** |

---

## 6. Git Working Tree Integrity

`git status --short` confirms:
- In AI-OS root: Only `GEMINI.md` and `.gemini/` have expected additions/modifications. No protected files are tracked or modified.
- In LSAT U: Completely untouched by Wave 6 operations.

---

## 7. Operational Status

Wave 6 is complete and operational:
- The mechanical guard is active globally across Antigravity sessions.
- Direct mutations against Codex and Claude configuration are blocked with informative diagnostics.
- Read operations are unhindered.
- All non-negotiable boundaries and style constraints are satisfied.
