# Master System Architecture & Environment Blueprint
**Host Machine:** `J` (Windows 11 Home) | **Canonical Workspace:** `C:\Users\Joshu\dev\ai-os`  
**Operator:** Joshua Fisseha (Founder of Aspiring Attorneys & Builder of LSAT U)  
**Primary Assistant Identity:** Jay 2 (Executive Assistant & Command Center Operator)

---

## 1. Machine Profile & Hardware Environment

| Property | Value / Specification |
|---|---|
| **Computer Name** | `J` |
| **Operating System** | Windows 11 Home (Version 2009, OS Build 26200.5000, 64-bit) |
| **Processor (CPU)** | 13th Gen Intel(R) Core(TM) i5-1334U (10 cores, 12 threads) |
| **Installed RAM** | 16.0 GB (16,849,256,448 bytes physical memory) |
| **Primary User Account** | `Joshu` |
| **User Home Directory** | `C:\Users\Joshu\` |
| **Node.js Runtime** | `v24.19.0` (npm `11.17.0`) |
| **Python Runtime** | `Python 3.12` |
| **Git Version** | `git version 2.47.1.windows.1` |
| **Shell Environment** | PowerShell 7 (`pwsh.exe`) and Windows PowerShell (`powershell.exe`) |
| **Google Chrome Version** | `153.0.8010.53` (`C:\Program Files\Google\Chrome\Application\chrome.exe`) |
| **Antigravity App Version** | `2.15.0.0` (`C:\Users\Joshu\AppData\Local\Programs\antigravity\Antigravity.exe`) |
| **Everyday Browser** | Microsoft Edge (completely isolated, untouched by agent automation) |

---

## 2. Core Architecture: The Tri-Runtime AI-OS

The canonical workspace root on this machine is:
```
C:\Users\Joshu\dev\ai-os
```
This repository is Joshua's central command center and second brain. It manages business operations, student dossiers, curriculum knowledge, and the application source code for **LSAT U** (`https://lsatprep.study`).

### Strict Tri-Runtime Isolation Model
Three distinct agentic AI runtimes operate inside this repository simultaneously. To prevent state collision, context overwrites, or tool conflicts, each runtime has a dedicated, quarantined subdirectory:

```
C:\Users\Joshu\dev\ai-os\
├── .gemini/        <-- Google Antigravity & Gemini Workspace (Strictly Isolated)
├── .claude/        <-- Anthropic Claude Code Workspace (Strictly Isolated)
├── .codex/         <-- OpenAI Codex Workspace (Strictly Isolated)
├── .agents/        <-- Codex active skills & agent TOML definitions
├── skills/         <-- Master skill catalog partitioned by vendor
│   ├── gemini/     <-- Canonical Gemini skills
│   ├── claude/     <-- Canonical Claude Code skills
│   └── codex/      <-- Canonical Codex skills
└── projects/       <-- Shared application codebases
    └── lsatu/      <-- LSAT U web application repository
```

#### Runtime Operating Rules
1. **Gemini / Antigravity** reads `GEMINI.md` at root. It writes exclusively to `.gemini/` and `skills/gemini/`. It never touches `.claude/` or `.codex/`.
2. **Claude Code** reads `CLAUDE.md` at root. It writes exclusively to `.claude/` and `skills/claude/`.
3. **OpenAI Codex** reads `AGENTS.md` at root. It writes exclusively to `.codex/`, `.agents/`, and `skills/codex/`.
4. **Instruction Mirroring**: `GEMINI.md`, `CLAUDE.md`, and `AGENTS.md` maintain identical core routing maps, voice constraints, and business logic so all three models operate with unified context.

---

## 3. Comprehensive Directory-by-Directory Breakdown

All paths below are relative to `C:\Users\Joshu\dev\ai-os\`:

### Core Operational & Governance Folders

#### `context/`
Holds ground-truth facts about Joshua and the business.
- `about-me.md`: Joshua's identity, preferences, communications, scheduling rules, and bio.
- `work.md`: Business structure, tutoring offers, pricing, channels, and marketing roadmap.
- `priorities.md`: Current active 90-day slate and strategic objectives.

#### `decisions/`
- `log.md`: Immutable record of settled architectural, pedagogical, and business decisions. Once logged, decisions are never reopened without explicit justification.

#### `wiki/`
The live operational brain (LLM-Wiki pattern).
- `hot.md`: Current-session scratchpad, hot cache, and active threads.
- `index.md`: Master index of all concept and system pages.
- `tasks.md`: Operational work ledger (open, in-progress, completed).
- `log.md`: Chronological session history and ingest ledger.
- `dashboard.md`: Product ground truth pointing to live backend tables and services.
- `teaching-voice.md`: Authoritative voice rules for any text read by students or prospects.
- `send-ledger.md`: Append-only record of every outbound email or draft.

#### `students/`
Student operations hub. Contains individual dossiers for each active or historical student:
- `README.md`: Student operations workflow protocol.
- `roster.generated.md`: Automatically generated student directory (names, emails, session counts). Never edited by hand.
- Individual folders: `students/asia/`, `students/ore/`, `students/yahunatan/`, etc., holding session notes, diagnostic scores, transcripts, and assigned drills.

#### `corpus/`
Pedagogical knowledge base.
- `index.md`: Master curriculum index.
- Structured modules on LSAT logic: Sufficient Assumption, Flaw, Principle-Conform, Reading Comprehension methods, and question breakdowns.

#### `references/`
Methodology and automation design blueprints.
- `3ms-framework.md`: Automation philosophy (Mindset, Machinery, Mastery).
- `automation-backlog.md`: Ranked roadmap of automations to build.
- `firecrawl.md` & `references/firecrawl/`: Schemas and operating standards for web research agents.

#### `raw/`
Immutable evidence intake.
- `raw/inbox/`: Temporary intake dropzone for unclipped articles and transcripts.
- `raw/sources/`: Processed source documents, never edited.
- `raw/sources/clips/<slug>/`: Archived web captures with provenance records and SHA256 hashes.

#### `brainstorms/` & `research/` & `handoffs/`
- `brainstorms/`: Strategy interview outputs and design RFCs.
- `research/`: Competitor analyses, browser benchmarks, AI model evaluations.
- `handoffs/`: Context handoff summaries used to pass state cleanly between Claude, Codex, and Gemini.

---

### Application Codebase: `projects/lsatu/`
The complete frontend and backend repository for **LSAT U** (`https://lsatprep.study`).
- **Tech Stack**: React 18, Vite 5.4, TypeScript, Tailwind CSS, Shadcn UI, Lucide Icons, Radix UI.
- **Backend Architecture**: Lovable Cloud / Supabase PostgreSQL, Row-Level Security (RLS), Supabase Edge Functions (Deno runtime).
- **Key Modules**:
  - `src/pages/classroom/`: Student classroom, drills, testing centre, performance analytics.
  - `src/pages/teacher/`: Teacher workspace, student management, custom drill assignment.
  - `src/components/`: Modular component design system.
  - `supabase/functions/`: Backend serverless functions for booking, Stripe webhooks, auth events.
- **Development Server**: Configured to run on `http://localhost:8080` via `npm run dev`.

---

### Dedicated Gemini / Antigravity Workspace: `.gemini/`
Contains the dedicated runtime assets for Google Antigravity within `ai-os`:
- `.gemini/README.md`: Directory router and runtime map.
- `.gemini/skills/`: 218 active skills installed for Gemini.
- `.gemini/agents/`: Subagent TOML configuration profiles.
- `.gemini/wiki/`: Distilled knowledge layer maintained specifically by Gemini.
- `.gemini/raw/`: Intake queue for Gemini-driven research.
- `.gemini/output/`: Permanent storage for generated reports, blueprints, and audits:
  - `ai_model_showdown.md`: Benchmarks of Gemini 3.1 Pro vs Claude Opus 4.6 vs GPT-5.6 Luna.
  - `browser_deep_dive_report.md`: Memory and speed comparisons of Edge vs Chrome vs Brave.
  - `edge_workflow_optimizations.md`: Windows 11 browser performance tuning.
  - `laptop_setup_guide.md`: Machine optimization documentation.
  - `magic_mouse_master_plan.md`: Secure Bluetooth configuration guide.
  - `conditional_logic_notes.md`: Curriculum documentation.
  - `lsat-u-browser-verification/`: The full browser automation skill and scripts.

---

## 4. The Dedicated LSAT U Browser Verification Suite

To enable zero-overhead, repeat visual verification without repetitive logins, a dedicated browser testing environment was configured.

```
[ Antigravity / Gemini ]  <-- (CDP on port 9223) -->  [ Dedicated Chrome Instance ]
        |                                                     |
  Chrome DevTools MCP                                 User Data Profile:
  or Playwright Node                                  %LOCALAPPDATA%\LSATU-Agent-Chrome
        |                                                     |
        +-----------------------------------------------------+
                                  |
            Navigates & Verifies Both Origins:
            1. Production:  https://lsatprep.study
            2. Local Dev:    http://localhost:8080
```

### Key Technical Specifications
1. **Dedicated User Data Profile**:
   ```
   C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome
   ```
   Completely isolated from your everyday Chrome profile and Edge. Stores login tokens and passwords permanently.
2. **Dedicated Debugging Port**:
   - Port: **`9223`** (verified free; avoids collision with any personal Chrome instances on 9222).
   - Binding: `127.0.0.1:9223`.
   - Required Security Flag: `--remote-allow-origins=*` (prevents modern Chrome from rejecting CDP WebSocket handshakes).
3. **Windows Shortcuts Configured**:
   - Desktop: `C:\Users\Joshu\OneDrive\Desktop\LSAT U Agent Browser.lnk`
   - Start Menu: `C:\Users\Joshu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\LSAT U Agent Browser.lnk`
   - Command Line:
     ```powershell
     "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9223 --remote-debugging-address=127.0.0.1 --remote-allow-origins=* --user-data-dir="C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome" --no-first-run --no-default-browser-check https://lsatprep.study
     ```
4. **Machine Automation Suite**:
   Stored in `C:\Users\Joshu\Tools\LSATU-Agent\` and mirrored in `.gemini/skills/lsat-u-browser-verification/scripts/`:
   - `launch-agent-browser.ps1` & `launch_browser.py`: Detached WMI background process launchers.
   - `agent-browser.mjs`: Fast Playwright CDP status checker and screenshot utility.
   - `verify-viewports.mjs`: Complete multi-device viewport sweep runner.
   - `start-dev-session.ps1`: One-click dev stack launcher.
5. **Standard 5-Viewport Presets Verified**:
   - `desktop-1440` (1440 x 900)
   - `laptop-1366` (1366 x 768)
   - `laptop-1280` (1280 x 800)
   - `tablet-1024` (1024 x 768)
   - `mobile-390` (390 x 844)

---

## 5. Antigravity System & Machine Configuration Layer

Antigravity uses global configurations in your user profile to govern sessions and MCP servers:

### Global Configuration Directory: `C:\Users\Joshu\.gemini\`
- **`config/mcp_config.json`**:
  Registers active MCP servers, including the dedicated Chrome connection:
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
- **`config/skills.json`**:
  Global skill registry ensuring that any Antigravity window inherits your workspace skills:
  ```json
  {
    "entries": [
      { "path": "C:/Users/Joshu/dev/ai-os/.gemini/skills" },
      { "path": "C:/Users/Joshu/dev/ai-os/.agents/skills" }
    ]
  }
  ```
- **`config/projects/`**:
  Defines registered projects. The sole active project is `ai-os` (`file:///c%3A/Users/Joshu/dev/ai-os`). Duplicate drive-level project definitions have been archived.
- **`antigravity/conversation_summaries.db`**:
  Internal SQLite database holding all 51 conversation sessions, all unified under `ai-os`.

### Global Machine Routers
- **`C:\Users\Joshu\GEMINI.md`**: Directs any unattached Gemini session straight to `C:\Users\Joshu\dev\ai-os`.
- **`C:\Users\Joshu\AGENTS.md`**: Directs any unattached Codex session straight to `C:\Users\Joshu\dev\ai-os`.

---

## 6. Security, Credentials & Live Connections

### Single Secret Store Model
- All API keys, database credentials, bank references, and platform tokens live in a single, git-ignored file:
  ```
  C:\Users\Joshu\dev\ai-os\.env
  ```
  There is no third-party vault or cloud secret manager. The repository is never pushed to a remote without a full scrub check (`wiki/HANDLING.md`).

### Connected External Systems (`connections.md`)
1. **Google Workspace (Gmail, Calendar, Drive, Docs)**: Accessed strictly via the official `gws` CLI tool (`skills/codex/gws-shared/`). Never through Google connector MCPs.
2. **Cal.com**: Live calendar and booking event authority.
3. **LSAT U Supabase Backend**: PostgreSQL database, auth events, student homework tracking.
4. **Stripe**: Payment and subscription processing.
5. **Firecrawl API**: High-fidelity web scraping and structured search.

---

## 7. Operational Voice & Persona Rules

When generating any student-facing or outward communication:
1. **Zero Em-Dashes**: Strictly forbidden. Joshua never types em-dashes; a stray em-dash destroys trust and reads as artificial.
2. **No AI-Slop Vocabulary**: Prohibited words include *delve*, *tapestry*, *testament*, *demystify*, *boasts*, *in the realm of*, *beacon*, and similar tropes.
3. **Decisive Stance**: Always lead with a recommendation and clear rationale, never a passive list of options.
4. **Pedagogical Authority**: Joshua is the product and voice authority for LSAT preparation. The AI assists, drafts, and verifies, but never impersonates him or auto-sends unapproved outbound messages.
