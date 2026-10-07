# AIOS WAVE 0 RESULT: BACKUP AND BASELINE FREEZE

- **Wave Status**: **PASS** (100% Verified, Zero Failures, Zero Errors)
- **Timestamp**: 2026-09-20T03:55:00-04:00
- **Machine**: `J`
- **User**: `Joshu`
- **Antigravity Version**: `2.15.0`
- **Backup Root Location**: [`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config`](file:///C:/Users/Joshu/dev/ai-os-backup-pre-migration-config)
- **Manifest File**: [`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\WAVE0_MANIFEST.md`](file:///C:/Users/Joshu/dev/ai-os-backup-pre-migration-config/WAVE0_MANIFEST.md)
- **Baseline JSON**: [`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\WAVE0_BASELINE.json`](file:///C:/Users/Joshu/dev/ai-os-backup-pre-migration-config/WAVE0_BASELINE.json)
- **SHA-256 Checksum Manifest**: [`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\MANIFEST.sha256`](file:///C:/Users/Joshu/dev/ai-os-backup-pre-migration-config/MANIFEST.sha256)

---

## 1. EXECUTIVE OUTCOME

Wave 0 has completed with a status of **PASS**.

- **Backup Execution**: 1,736 control and snapshot files were securely backed up into `C:\Users\Joshu\dev\ai-os-backup-pre-migration-config` without copying reproducible `node_modules`, build artifacts, or cache files. Total storage footprint is under 30 MB.
- **Protected Runtime Non-Interference**: All protected Claude and Codex files (`AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/`, `.codex/`, and catalogs) were hashed and verified. Zero protected files were modified or touched.
- **Live Database Safety**: Zero SQLite databases were vacuumed, migrated, or modified. Exact metadata, sizes, and hashes were recorded while leaving active databases untouched.
- **Git State Preservation**: Both repositories remain on their exact pre-wave branches and working trees. `projects/lsatu` remains checked out on `feat/calendar-strip-deeplink`.
- **HARD STOP ENFORCED**: Wave 1 has **NOT** begun. No configuration or runtime settings have been changed.

---

## 2. BACKUP LOCATION AND FILES BACKED UP

### Backup Root Directory
`C:\Users\Joshu\dev\ai-os-backup-pre-migration-config\`

### Inventory of Backed-Up Trees
1. **Antigravity Control Files** (`antigravity_control/`):
   - `C:\Users\Joshu\GEMINI.md` -> `antigravity_control\user_home_GEMINI.md`
   - `C:\Users\Joshu\dev\ai-os\GEMINI.md` -> `antigravity_control\ai_os_GEMINI.md`
   - `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` -> `antigravity_control\lsatu_GEMINI.md`
   - `C:\Users\Joshu\.gemini\config\` -> `antigravity_control\gemini_global_config\`
   - `C:\Users\Joshu\dev\ai-os\.gemini\` -> `antigravity_control\aios_gemini_dir\`
   - `C:\Users\Joshu\Tools\LSATU-Agent\` -> `antigravity_control\LSATU-Agent\`
2. **Protected Runtime Snapshots** (`protected_snapshots/`):
   - `root_AGENTS.md` (Original SHA-256: `77b16d6cda2b59e55076e6ec37481da13ba9f0e768939f7a6df560f0f0245326`)
   - `root_CLAUDE.md` (Original SHA-256: `9b8e32a2c648a2ef99f8b0c17a7a28d5cc79b1dce200f6a52d25cb31cb777665`)
   - `lsatu_AGENTS.md` (Original SHA-256: `12c1a22f592c68a4064b6eab603d419b87a473a85abf6573e60ae5203239c5e5`)
   - `lsatu_CLAUDE.md` (Original SHA-256: `1ee7aedcfcc75faf2b67163b6edb172d05e7224e22000edb7020ab237fd8937c`)
   - `root_codex\` (Directory snapshot)
   - `lsatu_codex\` (Directory snapshot)
3. **Protected Manifests** (`manifests/`):
   - `protected_aios_agents_manifest.json` (27 files indexed)
   - `protected_aios_claude_manifest.json` (14 files indexed)
   - `protected_skills_codex_manifest.json` (1,054 files indexed)
   - `protected_skills_claude_manifest.json` (1,178 files indexed)
   - `protected_lsatu_agents_manifest.json` (493 files indexed)
   - `protected_lsatu_claude_manifest.json` (475 files indexed)

---

## 3. PROTECTED-RUNTIME HASH VERIFICATION

Every protected file was verified byte-identical before and after Wave 0 execution:

| Protected File Path | Size (Bytes) | SHA-256 Checksum | Before/After Match |
|---|---|---|---|
| `C:\Users\Joshu\dev\ai-os\AGENTS.md` | 13951 | `77b16d6cda2b59e55076e6ec37481da13ba9f0e768939f7a6df560f0f0245326` | **IDENTICAL** |
| `C:\Users\Joshu\dev\ai-os\CLAUDE.md` | 13946 | `9b8e32a2c648a2ef99f8b0c17a7a28d5cc79b1dce200f6a52d25cb31cb777665` | **IDENTICAL** |
| `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md` | 8556 | `12c1a22f592c68a4064b6eab603d419b87a473a85abf6573e60ae5203239c5e5` | **IDENTICAL** |
| `C:\Users\Joshu\dev\ai-os\projects\lsatu\CLAUDE.md` | 12992 | `1ee7aedcfcc75faf2b67163b6edb172d05e7224e22000edb7020ab237fd8937c` | **IDENTICAL** |

---

## 4. CURRENT GIT STATE FOR BOTH REPOSITORIES

Zero git operations were performed. Both repositories remain exactly as Joshua left them:

### Outer Repository (`C:\Users\Joshu\dev\ai-os`)
- **Root**: `C:\Users\Joshu\dev\ai-os`
- **Active Branch**: `main`
- **HEAD Commit SHA**: `3b86f2cf0ef5ce3276b0c3c66f35b1bc8e5529a2`
- **Remote Fetch URL**: `https://github.com/vnjkoxpl-42905/ai-os.git`
- **Working Tree**: Staged: 0, Unstaged: 0, Untracked: 125

### Inner Repository (`C:\Users\Joshu\dev\ai-os\projects\lsatu`)
- **Root**: `C:\Users\Joshu\dev\ai-os\projects\lsatu`
- **Active Branch**: `feat/calendar-strip-deeplink` (Strictly Preserved)
- **HEAD Commit SHA**: `a071951e3ecca0bf81c477fa54e67663afcfc308`
- **Remote Fetch URL**: `https://github.com/vnjkoxpl-42905/lsatu-684d89db.git`
- **Working Tree**: Staged: 0, Unstaged: 34, Untracked: 42

---

## 5. SKILL BASELINE

Current skill distribution across directories:
- **`C:\Users\Joshu\dev\ai-os\.gemini\skills\`**: 215 skills
- **`C:\Users\Joshu\dev\ai-os\.agents\skills\`**: 11 skills
- **`C:\Users\Joshu\.gemini\config\skills\`**: 33 skills
- **Builtin Skills**: 5 skills
- **Registered Skill Roots in `C:\Users\Joshu\.gemini\config\skills.json`**:
  1. `C:/Users/Joshu/dev/ai-os/.gemini/skills`
  2. `C:/Users/Joshu/dev/ai-os/.agents/skills`
- **Duplicate Identifiers**: All 11 skills in `.agents/skills/` also exist in `.gemini/skills/` (`gws-gmail-triage, gws-shared, session-recap, superwhisper, kling-cli, gws-gmail-read...`), causing duplicate discovery collisions. This will be resolved in Wave 3 by de-indexing `.agents/skills` from `skills.json`.

---

## 6. INSTRUCTION AND TOKEN BASELINE

- **Instruction Files Loaded in AIOS Root**:
  - `C:\Users\Joshu\dev\ai-os\AGENTS.md` (6,954 bytes, ~1,740 tokens)
  - `C:\Users\Joshu\dev\ai-os\GEMINI.md` (6,458 bytes, ~1,615 tokens)
  - `C:\Users\Joshu\GEMINI.md` (1,799 bytes, ~450 tokens)
- **Instruction Tokens Baseline**: ~3,805 tokens
- **Skill Descriptions Overhead in Prompt**: ~6,500 tokens (67 exposed skills + 197 excluded skills listed)
- **Total System Prompt Baseline Overhead**: ~11,500 tokens before user turn

---

## 7. BROWSER BASELINE

- **Chrome Executable**: `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Chrome Product Version**: `153.0.8010.53`
- **Persistent Profile Directory**: `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome` (Exists: `True`)
- **Port 9223 (Remote Debugging CDP)**: Currently `Closed / Not Running`
- **Port 8080 (Localhost Dev Server)**: Currently `Closed / Not Running`
- **Host Tools Directory (`C:\Users\Joshu\Tools\LSATU-Agent\`)**: 23 files verified and hashed (including `launch_browser.py`, `start-dev-session.ps1`, `verify-viewports.mjs`).

---

## 8. CHROME DEVTOOLS MCP BASELINE

- **Config File**: `C:\Users\Joshu\.gemini\config\mcp_config.json`
- **Command**: `npx`
- **Arguments**: `["-y", "chrome-devtools-mcp@latest", "--browserUrl", "http://127.0.0.1:9223"]`
- **Resolved Package**: `chrome-devtools-mcp`
- **Resolved Version**: `1.9.0`
- **Exposed Tools**: 29 tools (click, evaluate_script, take_screenshot, list_console_messages, etc.)

---

## 9. MODEL BASELINE

Authoritative model catalog verified from `state.vscdb` (`antigravityUnifiedStateSync.userStatus`):
- Total Recommended Models in UI: 14
- Verified Models Visible:
  1. Gemini 3.8 Flash (High, Medium, Low)
  2. Gemini 3.7 Flash (High, Medium, Low)
  3. Gemini 3.6 Flash (High, Medium, Low)
  4. Gemini 3.1 Pro (High, Low)
  5. Claude Sonnet 4.6 (Thinking)
  6. Claude Opus 4.6 (Thinking)
  7. GPT-OSS 120B (Medium)

---

## 10. REAL ANTIGRAVITY STATE AND DATABASE PATHS

Verified physical locations on this workstation:
- **Global `state.vscdb`**: `C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage\state.vscdb` (Size: 372736 bytes, SHA-256: `fd446ddcbcd13741ec67b14ecc25b996df9328bb7a78b86a2640718d51481e3c`)
- **Workspace Storage Root**: `C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\workspaceStorage`
- **Global Storage Root**: `C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\globalStorage`
- **Conversation Summaries Database**: `C:\Users\Joshu\.gemini\antigravity\conversation_summaries.db` (Size: 77824 bytes, SHA-256: `cabcf75db4f949c48b98002b5612ffc7324eefb9e7c2814bbdd655eef44a036f`)
- **Antigravity Brain Directory**: `C:\Users\Joshu\.gemini\antigravity\brain`
- **Global Skills Registry**: `C:\Users\Joshu\.gemini\config\skills.json`
- **MCP Configuration**: `C:\Users\Joshu\.gemini\config\mcp_config.json`
- **Agent Configuration / Preferences**: `C:\Users\Joshu\.gemini\config\config.json`
- **User Settings**: `C:\Users\Joshu\AppData\Roaming\Antigravity IDE\User\settings.json`

---

## 11. FAILURES, ANOMALIES, AND UNCERTAINTIES

- **Failures**: **ZERO**. Every file copy, directory snapshot, and hash computation completed successfully.
- **Anomalies**:
  - Chrome on port 9223 and Vite dev server on port 8080 were not running during Wave 0. This is expected since Wave 0 is a passive baseline.
  - `skills.json` currently registers both `.gemini/skills` and `.agents/skills`, creating duplicate discovery entries for 11 skills. This confirmed the forensic audit finding and will be cleanly decoupled in Wave 3.
- **Uncertainties**: **ZERO**.

---

## 12. HARD STOP CONFIRMATION

Wave 0 is **COMPLETE**.

The system is in a fully documented, measured, backed-up baseline state.
- Zero files in Claude, Codex, or Antigravity configuration have been modified.
- Wave 1 has **NOT** been started.
- Awaiting explicit authorization from Joshua and the external architect before proceeding.
