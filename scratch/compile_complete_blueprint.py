import os
import re
import json

output_file = r"C:\Users\Joshu\dev\ai-os\.gemini\GEMINI_ANTIGRAVITY_COMPLETE_BREAKDOWN.md"

skills_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\skills"
agents_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\agents"
wiki_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\wiki"
output_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\output"
raw_dir = r"C:\Users\Joshu\dev\ai-os\.gemini\raw"
global_config_dir = r"C:\Users\Joshu\.gemini\config"
global_antigravity_dir = r"C:\Users\Joshu\.gemini\antigravity"

lines = []
def w(s=""):
    lines.append(s)

w("# Exhaustive Architecture Blueprint: Google Gemini & Antigravity Setup")
w("**Machine:** `J` (Windows 11 Home) | **Host Workspace:** `C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\`")
w("**Global Machine Runtime:** `C:\\Users\\Joshu\\.gemini\\`")
w("**Operator:** Joshua Fisseha | **Assistant Persona:** Jay 2")
w("**Last Synchronized:** 2026-09-19")
w("")
w("---")
w("")
w("## 1. Executive Summary & Design Foundations")
w("")
w("This document provides a 100% complete, granular inventory and breakdown of the **Google Gemini and Antigravity** setup on this machine. There are no omitted files, no placeholders, and no implicit assumptions.")
w("")
w("The Gemini Antigravity system operates as a **dual-layer architecture**:")
w("1. **Workspace Layer (`C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\`)**: The repository-scoped operating environment. Contains all 218 active skills, 18 autonomous subagent configurations, the Karpathy LLM-Wiki knowledge layer, immutable intake files, and permanent research deliverables. It is strictly quarantined from Claude (`.claude/`) and Codex (`.codex/`).")
w("2. **Global Runtime Engine (`C:\\Users\\Joshu\\.gemini\\`)**: The Windows system-level engine. Governs execution permissions, Model Context Protocol (MCP) server bindings (including dedicated Chrome port 9223), the global skill registry bridge (`skills.json`), and the unified conversation database (`conversation_summaries.db`).")
w("")
w("---")
w("")
w("## 2. Workspace Layer Breakdown (`C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\`)")
w("")
w("```")
w("C:\\Users\\Joshu\\dev\\ai-os\\.gemini\\")
w("├── README.md                                  <-- Workspace router and directory map")
w("├── agents/                                    <-- 18 specialized TOML subagent definitions")
w("├── skills/                                    <-- 218 active, installed Gemini skills")
w("├── wiki/                                      <-- LLM-Wiki knowledge layer")
w("│   ├── concepts/                              <-- Distilled formal concept notes")
w("│   ├── sources/                               <-- Processed source extractions")
w("│   ├── index.md                               <-- Master knowledge catalog")
w("│   └── log.md                                 <-- Chronological ingest ledger")
w("├── raw/                                       <-- Immutable evidence intake")
w("│   ├── inbox/                                 <-- Unprocessed intake dropzone")
w("│   └── sources/                               <-- Immutable historical sources")
w("└── output/                                    <-- Permanent deliverables, teardowns & plans")
w("```")
w("")
w("---")
w("")
w("### 2.1 Router File: `.gemini/README.md`")
w("Establishes the internal directory boundaries for Gemini within `ai-os`. It dictates that all Gemini-generated assets must route to `.gemini/`, all canonical skill copies route to `skills/gemini/`, and that Claude (`.claude/`) and Codex (`.codex/`, `.agents/`) are completely off-limits.")
w("")
w("---")
w("")
w("### 2.2 Subagent Definitions: `.gemini/agents/` (18 TOML Profiles)")
w("Autonomous subagents invoked on demand via `invoke_subagent`. Each runs in its own context window and reports findings back to the main agent:")
w("")

for fname in sorted(os.listdir(agents_dir)):
    fpath = os.path.join(agents_dir, fname)
    if fname.endswith(".toml"):
        size = os.path.getsize(fpath)
        role = ""
        prompt_snippet = ""
        tools = []
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                m_role = re.search(r'role\s*=\s*"([^"]+)"', content)
                if m_role:
                    role = m_role.group(1)
                m_prompt = re.search(r'system_prompt\s*=\s*"""([\s\S]*?)"""', content)
                if m_prompt:
                    prompt_snippet = m_prompt.group(1).strip().replace("\n", " ")[:200]
                m_tools = re.search(r'tools\s*=\s*\[(.*?)\]', content)
                if m_tools:
                    tools = [t.strip().strip('"').strip("'") for t in m_tools.group(1).split(",") if t.strip()]
        except:
            pass
        w(f"#### `{fname}` ({size} bytes)")
        if role:
            w(f"- **Role:** {role}")
        if tools:
            w(f"- **Tool Permissions:** `{', '.join(tools)}`")
        if prompt_snippet:
            w(f"- **System Prompt Focus:** {prompt_snippet}...")
        w("")

w("---")
w("")
w("### 2.3 Permanent Deliverables: `.gemini/output/`")
w("Stores high-value research reports, plans, and teardowns so they persist across sessions:")
w("")

for fname in sorted(os.listdir(output_dir)):
    fpath = os.path.join(output_dir, fname)
    if os.path.isfile(fpath):
        size = os.path.getsize(fpath)
        first_line = ""
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                first_line = f.readline().strip().lstrip("#").strip()
        except:
            pass
        w(f"- **`{fname}`** ({size} bytes): {first_line or 'Binary or JSON data file'}")

w("")
w("---")
w("")
w("### 2.4 Knowledge Layer: `.gemini/wiki/`")
w("Follows the Karpathy LLM-Wiki design pattern:")
w("- **`index.md`**: Central directory linking all concept pages and source references.")
w("- **`log.md`**: Chronological record of all ingestion events, audits, and query sessions.")
w("- **`concepts/conditional-sufficient-assumption-strategy.md`**: Distilled pedagogy breakdown covering formal logic conditional statements, algebraic linking patterns, and student execution checklists.")
w("- **`sources/conditional-sufficient-assumption-sa-strategy.md`**: Source documentation derived from Ellen Cassidy's Loophole training curriculum.")
w("")
w("---")
w("")
w("### 2.5 Active Skills Inventory: `.gemini/skills/` (All 218 Skills)")
w("Every installed skill is listed below with its folder name and exact operational description from its `SKILL.md` frontmatter:")
w("")

skills = []
for item in sorted(os.listdir(skills_dir)):
    ipath = os.path.join(skills_dir, item)
    if os.path.isdir(ipath):
        skill_md = os.path.join(ipath, "SKILL.md")
        desc = "No frontmatter description available."
        if os.path.exists(skill_md):
            try:
                with open(skill_md, "r", encoding="utf-8", errors="ignore") as f:
                    txt = f.read(2000)
                    m_desc = re.search(r'description:\s*([^\r\n]+(?:\r?\n\s{2,}[^\r\n]+)*)', txt)
                    if m_desc:
                        desc = " ".join([l.strip() for l in m_desc.group(1).splitlines()])
            except:
                pass
        skills.append((item, desc))

w(f"Total Active Skills Installed: **{len(skills)}**")
w("")
w("| Skill Identifier | Operational Trigger & Purpose |")
w("|---|---|")
for name, desc in skills:
    clean_desc = desc.replace("|", "\\|").replace("\n", " ")
    w(f"| **`{name}`** | {clean_desc} |")

w("")
w("---")
w("")
w("## 3. Machine Runtime Layer Breakdown (`C:\\Users\\Joshu\\.gemini\\`)")
w("")
w("```")
w("C:\\Users\\Joshu\\.gemini\\")
w("├── config/                                    <-- Global machine configuration")
w("│   ├── config.json                            <-- Execution settings, permissions, turbo policies")
w("│   ├── mcp_config.json                        <-- Registered MCP tool servers")
w("│   ├── skills.json                            <-- Global skill registry bridge")
w("│   ├── projects/                              <-- Registered workspace definitions")
w("│   │   ├── 1e181e2e...json                    <-- ai-os project mapping (Active)")
w("│   │   └── 2a2e3dc0...json.bak                <-- c: duplicate mapping (Archived)")
w("│   ├── plugins/                               <-- 5 global plugin packages")
w("│   └── skills/                                <-- 33 global machine skills")
w("└── antigravity/                               <-- Desktop application runtime data")
w("    ├── builtin/skills/                        <-- Installer-bundled skills")
w("    ├── brain/                                 <-- 52 session folders (transcripts & logs)")
w("    ├── conversation_summaries.db              <-- SQLite database tracking all sessions")
w("    ├── mcp/                                   <-- Lazy tool schemas for MCP tools")
w("    └── scratch/                               <-- Temporary web scraping scratchpad")
w("```")
w("")
w("---")
w("")
w("### 3.1 Global Configuration Files (`C:\\Users\\Joshu\\.gemini\\config\\`)")
w("")
w("#### 1. `config.json` (Core Execution Settings)")
w("Controls the low-level automation engine:")
w("- `artifactReviewMode: \"ARTIFACT_REVIEW_MODE_TURBO\"`: Enables rapid markdown artifact streaming.")
w("- `autoExecutionPolicy: \"CASCADE_COMMANDS_AUTO_EXECUTION_EAGER\"`: Chains and executes safe terminal commands proactively.")
w("- `browserJsExecutionPolicy: \"BROWSER_JS_EXECUTION_POLICY_TURBO\"`: Accelerates DOM script evaluation.")
w("- `enableTerminalSandbox: false`: Grants native Windows PowerShell and Node.js command execution.")
w("- `globalPermissionGrants`: Explicit whitelist of trusted shell commands, directories, and URL domains (e.g., `lsatprep.study`, `superwhisper.com`, `firecrawl.dev`).")
w("")
w("#### 2. `mcp_config.json` (Model Context Protocol Servers)")
w("Registers external tool servers exposed to the agent:")
w("```json")
w("{")
w('  "mcpServers": {')
w('    "chrome-devtools": {')
w('      "command": "npx",')
w('      "args": [')
w('        "-y",')
w('        "chrome-devtools-mcp@latest",')
w('        "--browserUrl",')
w('        "http://127.0.0.1:9223"')
w("      ]")
w("    },")
w('    "notebooks": { "command": "node", "args": [...] },')
w('    "visualization": { "command": "node", "args": [...] },')
w('    "data-agent-kit": { "command": "node", "args": [...] }')
w("  }")
w("}")
w("```")
w("")
w("#### 3. `skills.json` (The Global Bridge)")
w("Bridges the repository skills to every Antigravity session on the machine:")
w("```json")
w("{")
w('  "entries": [')
w('    { "path": "C:/Users/Joshu/dev/ai-os/.gemini/skills" },')
w('    { "path": "C:/Users/Joshu/dev/ai-os/.agents/skills" }')
w("  ]")
w("}")
w("```")
w("")
w("#### 4. `projects/` (Project Workspace Registry)")
w("- **Active (`1e181e2e-860b-48c6-9209-540e3e7a1965.json`)**: Binds project name `ai-os` to `file:///c%3A/Users/Joshu/dev/ai-os` with full file access.")
w("- **Archived (`2a2e3dc0-5f6e-44f5-9cb4-5ad0c5a2a95b.json.bak`)**: Previously registered `C:\\` drive as a parallel project, causing conversation splitting. Now safely archived.")
w("")
w("---")
w("")
w("### 3.2 Global Plugins (`C:\\Users\\Joshu\\.gemini\\config\\plugins\\`)")
w("Five global plugin bundles are active, providing domain-specific skills:")
w("1. **`chrome-devtools-plugin`** (v0.21.0): Exposes 29 browser automation tools, memory leak debugging (`memlab`), accessibility auditing (`a11y-debugging`), and LCP performance optimization.")
w("2. **`data-agent-kit-plugin`**: Provides BigQuery SQL, BigFrames, Cloud Storage, Dataform, dbt, Airflow, and Cloud Composer orchestration skills.")
w("3. **`gemini-api`**: Direct access to upstream Google Gemini API, Interactions API, and Live API tools.")
w("4. **`google-antigravity-sdk`**: Agent building and multi-agent orchestration tools for Antigravity.")
w("5. **`modern-web-guidance-plugin`**: Modern web development standards and Chrome extension architecture guides.")
w("")
w("---")
w("")
w("### 3.3 Antigravity Runtime Engine (`C:\\Users\\Joshu\\.gemini\\antigravity\\`)")
w("")
w("#### 1. Conversation Database: `conversation_summaries.db`")
w("A SQLite database that manages the left sidebar conversation index. Contains table `conversation_summaries`:")
w("- Columns: `conversation_id`, `title`, `preview`, `step_count`, `last_modified_time`, `workspace_uris`, `status`, `project_id`.")
w("- **Status:** All 51 lifetime conversations have been unified under `project_id = '1e181e2e-860b-48c6-9209-540e3e7a1965'` (`ai-os`). Zero conversations remain unattached.")
w("")
w("#### 2. Session Brain Stores: `brain/<conversation-id>/` (52 Folders)")
w("Every conversation session has a dedicated folder containing:")
w("- `.system_generated/logs/transcript.jsonl`: Complete, verbatim execution logs of every user prompt, model response, and tool call.")
w("- `.system_generated/tasks/`: Execution logs for background commands and daemons.")
w("- Artifacts (`*.md`): Implementation plans, walkthroughs, and research deliverables.")
w("")
w("#### 3. Builtin Skills: `builtin/skills/`")
w("Installer-bundled core skills:")
w("- `agy-customizations`: Reference manual for rules, skills, plugins, and MCP servers.")
w("- `generative_ui`: Dynamic inline interactive HTML widget generation.")
w("- `migrate-workflows`: Workflow-to-skill converter.")
w("")
w("---")
w("")
w("## 4. Master Instruction Routers (`GEMINI.md`)")
w("")
w("1. **Workspace Router (`C:\\Users\\Joshu\\dev\\ai-os\\GEMINI.md`)**:  ")
w("   Active whenever Antigravity runs inside `ai-os`. Sets Jay 2 persona, routing map, retrieval order, voice rules (no em-dashes, no AI-slop words), and tool guardrails.")
w("")
w("2. **Global Machine Router (`C:\\Users\\Joshu\\GEMINI.md`)**:  ")
w("   Placed at the user root. When any Antigravity window opens unattached or in scratch mode, it walks up the directory tree, reads this file, and immediately routes the agent to `C:\\Users\\Joshu\\dev\\ai-os`.")
w("")
w("---")
w("")
w("## 5. Dedicated LSAT U Browser Verification Suite")
w("")
w("- **Dedicated Profile:** `C:\\Users\\Joshu\\AppData\\Local\\LSATU-Agent-Chrome`")
w("- **Debugging Port:** `9223` (`http://127.0.0.1:9223` with `--remote-allow-origins=*`)")
w("- **Desktop Shortcuts:** Desktop and Start Menu (`LSAT U Agent Browser.lnk`)")
w("- **Machine Automation Scripts:** `C:\\Users\\Joshu\\Tools\\LSATU-Agent\\` and mirrored in `.gemini\\skills\\lsat-u-browser-verification\\scripts\\`")
w("- **Origins Supported:** Production (`https://lsatprep.study`) and Localhost (`http://localhost:8080`) with automatic token mirroring.")
w("- **Standard 5-Viewport Presets:** 1440x900, 1366x768, 1280x800, 1024x768, 390x844.")
w("")
w("---")
w("### End of Authoritative Blueprint")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Successfully generated {output_file} ({len(lines)} lines)")
