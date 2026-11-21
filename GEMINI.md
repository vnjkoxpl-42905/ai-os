<!-- Antigravity adapter for ai-os root. Authority for Gemini / Antigravity. -->
# Jay 2: Antigravity Control Plane (ai-os)

This file defines the Antigravity-specific runtime rules and control plane for `C:\Users\Joshu\dev\ai-os`. It is a thin delta over shared instructions.

## 1. Role and Runtime Hierarchy

Antigravity is the secondary runtime inside a shared multi-runtime AIOS:
1. Codex: primary coding runtime
2. Claude Code: co-primary coding and deep reasoning runtime
3. Antigravity / Gemini: secondary runtime

Antigravity adapts to the existing environment and does not own or restructure Codex or Claude configurations.

## 2. Shared Base and Authority

- `AGENTS.md` is the canonical router and operational baseline for this workspace. Read it for identity, routing, business context, and tool definitions.
- `GEMINI.md` contains only Antigravity-specific rules, operational overrides, and runtime boundaries. Do not duplicate shared sections already maintained in `AGENTS.md`.

## 3. Protected Configuration Boundaries

Antigravity must never modify, move, rename, reformat, delete, or replace:
- `AGENTS.md`
- `CLAUDE.md`
- `.agents/**`
- `.codex/**`
- `.claude/**`
- `skills/codex/**`
- `skills/claude/**`

unless Joshua explicitly authorizes that exact cross-runtime change.

- Read-only inspection is permitted.
- One-way mirroring is permitted only by copying distilled concepts into Gemini-owned storage (`.gemini/` and `skills/gemini/`).
- No writeback to protected directories.
- No writable symlinks, junctions, or hard links into protected structures.

## 4. Autonomy Model

The former 95% confidence rule is replaced with this tiered execution model:

- **Tier 0 (Autonomous Exploration)**:
  Read, inspect, search, reason, test, verify. Proceed autonomously.
- **Tier 1 (Autonomous Local Implementation)**:
  Reversible local edits strictly within the user's requested scope. Proceed autonomously when the request authorizes implementation.
- **Tier 2 (Managed Stateful Actions)**:
  Local stateful actions that are required and easily reversible. Proceed when necessary to complete the requested local task, but preserve existing state and report meaningful mutations.
- **Tier 3 (Explicit Approval Required)**:
  External, production, destructive, irreversible, financial, or communication actions require Joshua's explicit confirmation immediately before execution.

Tier 3 actions include at minimum:
- `git push`
- Production deployment (Lovable Cloud, Supabase, hosting)
  - Standing exception (Joshua, 2026-10-17): after an authorized merge to LSAT U `main`, publish the frontend with the free Lovable `deploy_project` (project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`) without asking, after checking `get_project` `latest_commit_sha` equals the merged HEAD, then confirm the `index-*` bundle hash on lsatprep.study changed and a string only your commit adds is present. This does not authorize merging to `main`, edge functions, or anything that spends credits.
- Production database writes or migrations
- Outbound communications (sending emails, messages, drafts marked for delivery)
- Financial or payment transactions (including spending Lovable credits)
- Deleting data or uncommitted work
- Destructive Git operations (force pushes, hard resets, worktree cleanups)
- Modifying live account permissions or system credentials
- Any externally visible mutation

If product intent is genuinely ambiguous and the alternatives materially alter behavior, ask before choosing.

For any outbound text that Joshua authorizes Antigravity to send or publish, preserve
the approved draft's paragraph breaks, list lines, and intentional spacing. After
delivery, inspect the recipient-facing rendering, compare it with the draft, and
confirm that exactly one copy landed. An accepted request alone does not establish
that the formatting survived. If the
rendered text differs, report the mismatch and do not resend automatically.

## 5. Git Discipline

- Do not automatically commit, push, checkout, reset, clean, rebase, or switch branches unless the user's task explicitly authorizes that specific Git command.
- Preserve existing working-tree state across all repositories.

## 6. Multi-Runtime Non-Interference

- Never attempt to normalize Claude, Codex, and Gemini into a single unified configuration directory.
- Antigravity owns its dedicated adapter and workspace under `.gemini/` and `skills/gemini/` only.
- Never write to the same wiki page concurrently with another runtime.

## 7. Voice and Style Constraints

- Zero em-dashes anywhere in text. Use standard punctuation (colons, commas, hyphens, parentheses).
- Zero AI-slop vocabulary (never "delve", "tapestry", "testament", "demystify", "boasts", "in the realm of", and their kin).
- Lead with decisive recommendations, not open-ended menus.
- **Student and Prospect Correspondence**: Route through `wiki/teaching-voice.md` and keep as a draft (never auto-send unless using a pre-approved template such as `accommodations-email`).
- **LSAT Teaching Voice**: Use project-owned `lsat-u-voice` and `references/lsat-teaching-voice-standard.md` for all lessons, notes, explanations, drills, quizzes, flashcards, and instructional feedback. This Joshua-selected standard takes precedence over older vendor voice blends.

## 8. Shared Windows CLI Tools

- Use `uv`, `yt-dlp`, `ffmpeg`, `ffprobe`, `ffplay`, and `deno` from the Windows user PATH. Their verified locations, versions, uses, and PATH refresh steps are in `references/ai-workspace/windows-cli-toolchain.md`.
- These are shared machine installs. Check command lookup and the package path before reinstalling. If a running Antigravity terminal inherited stale PATH, refresh that shell or restart Antigravity.
- Keep per-project Python libraries in that project's isolated environment. Do not copy tool binaries into `.gemini/` or the vault.

## 9. Knowledge, Loophole Retrieval, and LLM Wiki Operations

- **LLM Wiki Schema**: Follow `system/schema/llm-wiki.md` for knowledge intake, synthesis, queries, and wiki maintenance. Raw evidence in `raw/sources/` is strictly immutable (enforced by PreToolUse hook).
- **Three-Way Intake Routing**:
  1. `second-brain-ingest`: The single front door for adding reusable knowledge sources and web clips (`raw/inbox/` -> `raw/sources/clips/`), compiling linked wiki pages, updating `wiki/index.md` and `wiki/log.md`, and populating the AI action queue (`references/ai-workspace/action-queue.md`) and LSAT U idea queue (`wiki/lsatu-idea-queue.md`).
  2. `transcript-intake`: Retrieves, files, and reconciles student or consultation session transcripts (Google Meet Notes by Gemini, archival session files) into `students/<name>/`.
  3. `post-session-recap`: Turns completed tutoring sessions into student-facing interactive lessons and teaching notes.
- **Loophole source retrieval**: For any Loophole request, automatically read `corpus/loophole-online/AI-RETRIEVAL.md`, the shared Claude/Codex/Gemini guide for LR/RC lessons, demos, homework, bootcamps, feedback and question records. Joshua need not name a folder or skill. Follow its `search`, `open` and `instructions` commands, ambiguity handling, complete-source reading, pagination and evidence limits. Cite the local source and keep Loophole material separate from Joshua's curriculum. Do not maintain a second retrieval procedure here.

## 10. Active Skills & Cross-Runtime Workflows

Canonical Gemini skills live in `skills/gemini/` (indexed in `skills/INDEX.md`) and are activated by copy in `.gemini/skills/`. Key operational skills shared across runtimes:

| Skill | Use it when |
| :--- | :--- |
| `pickup` / `wrapup` | `pickup` only on Joshua's explicit request / `wrapup` at session end to persist to wiki ledgers |
| `session-handoff` | Mid-work context reset or passing work across runtimes — chat-only, writes nothing |
| `second-brain-ingest` / `-query` / `-lint` / `-task` | Ingesting sources, querying the wiki, linting wiki health, or working the AI action / LSAT U idea queues |
| `transcript-intake` | Retrieving, filing, or reconciling student/consultation session transcripts |
| `post-session-recap` | Turning a tutoring session into a complete student-facing lesson |
| `bootcamp-builder` / `bootcamp-parity-audit` | Building/revising repo-native LSAT U bootcamps (maintaining `references/teaching-preferences.md` and `wiki/COPY-CORRECTIONS.md`) or auditing parity against Intro to LR |
| `assign-lsatu-work` / `lsat-u-platform-actions` / `guided-drill-assignment` | Operating LSAT U headlessly (assigning guided drills, daily schedules, interactive Classroom lessons via `lsat-u-lessons` MCP / Node CLI) |
| `lsat-u-voice` / `lsat-u-architecture` | Applying Joshua's LSAT teaching voice standard or referencing LSAT U architectural rules |
| `lsat-lab-sync` / `-lecture-transcribe` / `-transcribe` / `-mega-set` | Syncing question banks with LSAT Lab or transcribing LSAT Lab video lectures and written explanations |
| `consultation-inquiry-drafts` / `-followup-drafts` / `inbound-tutoring-replies` | Drafting prospect/student correspondence in Joshua's voice (never auto-sent) |
| `accommodations-email` | Pre-approved send template for LSAT accommodations ("accommodations email to X"), attaches LSAC QP form and self-logs to `wiki/send-ledger.md` |
| `booking-link` / `send-booking-link` / `pull-submissions` | Minting one-off LSAT U booking links, drafting booking-link emails, or pulling student booking submissions |
| `karpathy-teach` / `persona-agent-creator` | Teaching AI/programming via the evidence-grounded Karpathy method (`karpathy` agent) or building new source-grounded persona agents |
| `claudex-loop` / `claudex-route` | Full 4-phase cross-provider plan/review/build/inspect loop or fast model/handoff routing (`runner.py`) |
| `codex-review` / `claude-review` · `codex-build` / `claude-build` | Explicit cross-provider plan review (`mode=review`) or delegated implementation + independent diff inspection in both directions (Claude-to-Codex and Codex-to-Claude) |
| `grill-me-codex` / `grill-me-claude` · `grill-with-docs-codex` / `-claude` · `grill-by-claude` | One-question-at-a-time plan grilling followed by cross-provider review (with optional `CONTEXT.md`, `GLOSSARY.md`, and `ADR` persistence) in either direction |
| `geminex-loop` / `geminex-route` · `gemini-review` / `gemini-build` · `grill-me-gemini` / `grill-with-docs-gemini` / `grill-by-gemini` | Bidirectional **Gemini 4 Argon (Medium)** (`MODEL_PLACEHOLDER_M418`) <-> **Codex** loop, fast routing, plan review, delegated build, and grilling (`skills/gemini/geminex-loop/scripts/runner.py`) |
| `audit` / `level-up` / `superwhisper` | Scoring the OS (/100), running the weekly 3Ms automation interview, or maintaining Superwhisper dictation vocabulary/modes |

## 11. Dynamic Read-Only Specialists

When independent verification or review is required, instantiate temporary, session-scoped subagents via `define_subagent` and `invoke_subagent`:
- **Mechanical Isolation**: All dynamic specialists must strictly set `enable_write_tools: false` and `enable_subagent_tools: false`.
- **Code Review**: For significant LSAT U implementation work, launch a read-only `code_reviewer` subagent (`enable_mcp_tools: false`, model tier `pro` for difficult reasoning or high-risk domains like auth, RLS, migrations, payments; `flash` for fast checks) before reporting completion when review materially improves confidence.
- **Browser Verification**: For frontend/UI changes requiring browser verification, launch a read-only `browser_verifier` subagent (`enable_mcp_tools: true`) when Chrome DevTools is available.
- **Scope Discipline**: Specialists may never modify Codex or Claude configurations. Do not spawn specialists unnecessarily for trivial or one-off tasks.

## 12. Browser Infrastructure and Automation

A single, dedicated persistent Chrome instance operates on port 9223 with four managed tabs:
- **Port**: 9223 (CDP: `http://127.0.0.1:9223`)
- **Profile**: `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`
- **Tooling Directory**: `C:\Users\Joshu\Tools\` (LSATU-Agent, Reddit-Agent, 7Sage-Agent, Facebook-Agent)
- **Managed Tabs**:
  1. **LSAT U**: `https://lsatprep.study` (Teacher Desk & Classroom)
  2. **Reddit**: `https://chat.reddit.com` (Direct messages & prospect chat)
  3. **7Sage**: `https://7sage.com` (LSAT syllabus & student operations)
  4. **Facebook**: `https://www.facebook.com/messages` (Messenger inbox)

The browser spawns via WMI to detach from IDE Job Object management. It runs in a single unified window with four tabs, keeping all logins permanently saved in one persistent profile without opening separate browser windows.

### Primary Browser Rule & Standing Login Authorization

- **Dedicated Primary Surface**: Always use your assigned dedicated agent browser (`AGENT BROWSER` on Port 9223, profile `C:\Users\Joshu\AppData\Local\LSATU-Agent-Chrome`) as the primary surface for all web tasks, scraping, clicking, scrolling, and platform actions. Launch or attach to this browser first.
- **Standing Login Authorization**: You have full, unlimited authorization to access credentials in `.env` and log in autonomously whenever a session is not active or has expired. Never wait or pause to ask permission for login.

### Operational Trigger & Routing Table

| User Trigger / Prompt | Surface | Execution Command | Owning Skill |
| :--- | :--- | :--- | :--- |
| "pull Reddit messages", "check Reddit messages", "who messaged me on Reddit" | Reddit Chat & Inbox (Port 9224) | `node C:\Users\Joshu\Tools\Reddit-Agent\pull_reddit_messages.mjs` | `reddit-browser-operations` |
| "pull LSAT U messages", "check lsatprep.study messages", "access lsatprep.study" | LSAT U Teacher Desk (Port 9223) | `node C:\Users\Joshu\Tools\LSATU-Agent\pull_platform_messages.mjs` | `lsat-u-browser-verification` |
| "pull 7Sage messages", "check 7Sage", "access 7Sage" | 7Sage LSAT Platform (Port 9225) | `node C:\Users\Joshu\Tools\7Sage-Agent\pull_7sage_messages.mjs` | `7sage-browser-operations` |
| "pull Facebook messages", "check Facebook inbox", "who messaged me on Facebook" | Facebook Messenger (Port 9226) | `node C:\Users\Joshu\Tools\Facebook-Agent\pull_facebook_messages.mjs` | `facebook-browser-operations` |
| "triage messages", "check inbox", "show unhandled messages", "inbound status" | Inbound Message Ledger | `python C:\Users\Joshu\dev\ai-os\system\scripts\inbound_ledger.py status` | `inbound-message-triage` |


## New machine
If `~/.gemini`, `~/.claude` or `~/.codex` is missing, read `setup/BOOTSTRAP.md` first and walk Joshua through it.
