---
type: reference
subject: Running Claude Code and Codex on one project the idea, and where ai-os stands
updated: 2026-10-26
aliases: []
---

# Running Claude Code and Codex on one project — the idea, and where ai-os stands

Distilled from three clips: two ingested 2026-07-18 (archived at `raw/sources/clips/youre-using-claude-code-wrong-add-codex/` and `raw/sources/clips/codex-projects-in-5-mins/`) and the Herdr clip ingested 2026-09-22 at `raw/This Repo Just Solved The 1 Claude + Codex Headache.md`. These are method and architecture sources about the OS itself, not business or LSAT knowledge. Siblings of [[obsidian-command-center]] and [[second-brain-levels]].

- **"You're Using Claude Code Wrong (Add Codex)"** — Chase AI, YouTube `VdxUKiF8CWI`, 2026-05-07. The *why + the tandem workflow*.
- **"How to Use Your Claude Code Projects in Codex in 5 Mins"** — Nate Herk, YouTube `kB9iMD0EjT8`, 2026-05-18. The *how of file structure* — one project, both agents.
- **"This Repo Just Solved The #1 Claude + Codex Headache"** — Chase AI, YouTube `neK8ydl0Vlk`, 2026-07-16. The *execution and observability layer* using Herdr. [Source summary](../wiki/sources/herdr-claude-codex-headache.md), written 2026-10-10.

## The pitch: it's "and," not "or"

Don't pick Claude Code *or* Codex. Run both on the same project and let each check the other. The Venn diagram is ~99% overlap, so learning one gets you the other for free. The argument underneath is **tool agnosticism**: you owe these companies zero loyalty, models are converging, and pitting them against each other gets better output than staying tribal. Practical upside beyond quality: if one tool is down or stuck, you switch in seconds without losing context.

## The tandem workflow (Chase)

Run Codex in its desktop app (openai.com/codex) with a terminal open inside it, then run `claude` in that terminal, so both operate in the same directory. Then bounce work between them:

- **Plan review.** Codex plans → copy the plan into Claude ("what's missing, any blind spots?") → paste Claude's critique back → Codex revises. Two expert second-opinions before any code. Works in reverse too.
- **Adversarial code review.** One builds, the other reads the same files and hunts bugs. In the demo Claude found ~20 real bugs on Codex's first pass. Telling the reviewer the *other* model wrote it may make it usefully more adversarial. There is a Codex plugin skill for Claude literally called "adversarial review."
- **Cost logic.** Uses more tokens up front, but catching bugs and weak plans early saves tokens in aggregate.
- Desktop-app niceties Chase leans on: in-app browser + sidebar dev server, click-to-annotate/screenshot front-end reviews, diff viewer, "pets" background-activity indicator. Context note: GPT-5.5 Pro ~258k window vs Claude's ~1M; new chat = the `/clear` equivalent.

## The file-structure map (Nate) — one project, both agents

Both agents read the **same shared knowledge** (docs, references, scripts, context files). Only the tool-specific wrappers differ:

| Concern | Claude Code | Codex |
|---|---|---|
| Instructions file | `CLAUDE.md` | `AGENTS.md` |
| Config folder | `.claude/` | `.codex/` |
| Skills folder | `.claude/skills/` | `.agents/skills/` |
| Skill files | markdown + YAML front matter | **identical** markdown |
| Agent files | markdown | **TOML** (same job, different format) |
| Both support | global (`~/.claude`, `~/.codex`) + project-level scope | same |

**3-layer mental model:** (1) shared knowledge any agent reads unchanged, (2) skills + agents — same content, just placed in each tool's folder, (3) tool-specific config that genuinely differs. Maintenance rule: a major change to `CLAUDE.md` gets mirrored to `AGENTS.md` (and skills/agents to their twin). Codex sub-agents don't auto-invoke — you call them explicitly.

**Convert-any-project prompt (Nate's):**

```
I built this project using Claude Code, but I need you, Codex, to be able
to use it too. Create an AGENTS.md that uses the CLAUDE.md as inspiration,
create a .codex config, put all skills in .agents, put all agents in .codex
(as TOML). Research both the Codex and Claude Code documentation and make
sure everything important converts over.
```

**Session handoff** (Nate's own skill) is the bridge: summarize decisions / active files / next steps, paste into the other tool, keep going. When one gets stuck, hand off and the other often unsticks it in seconds.

## Herdr makes the tandem workflow visible and persistent

Herdr is the terminal and session layer around Claude Code and Codex. It does not replace either agent or the shared-file architecture. It gives the workflow an operational surface:

- **Workspaces** separate projects.
- **Tabs** separate activities within a project.
- **Panes** show Claude Code, Codex, servers, tests, and helper agents side by side.
- **Agent status** rolls up which pane is working, idle, or blocked.
- **Persistence** keeps pane processes running after the Herdr client detaches or its terminal window closes. Reopen `herdr` to reconnect. Use `herdr server stop` only when the processes should actually stop.
- **Agent control** lets an agent with the Herdr skill inspect neighboring panes, split panes, run commands, read output, and wait for another agent.

### Setup recheck, 2026-11-20

Herdr 0.9.5, the latest stable GitHub release checked on 2026-11-20, is installed at `C:/Users/Joshu/dev/tools/herdr/0.9.5`; its Windows ZIP matched the SHA-256 published by GitHub. This manual release installation is on the user PATH. The earlier `~/.herdr` installation and shared Node prefix were absent in the environment checked; the historical 2026-10-10 table below is not current evidence. The shared prefix `C:/Users/Joshu/dev/tools/node` was recreated with Claude Code 2.1.322 and Codex CLI 0.169.0 and placed on user PATH. Both shared CLI copies report signed-in status: Claude.ai Pro and Codex via ChatGPT. Herdr reports Claude integration v11 and Codex v10 current. The previous integration scripts were retained as `herdr-agent-state.before-v095.ps1` alongside their replacements. A live Windows Terminal/Herdr pane launch, detection and actual model turn have not been verified; open a fresh terminal to pick up PATH and test. The manual release installation has not been verified to support `herdr update`.

### Codex daemon startup issue, 2026-11-20

Codex in Herdr rejected `~/.codex/app-server-daemon` because its inherited ACL included the CodexSandboxUsers group. With the recorded daemon process IDs absent, the directory ACL was changed to a protected owner-only full-control ACL; the former security descriptor is saved in `~/.codex/app-server-daemon-acl-before-20261120.txt`. The next startup exposed a missing managed daemon executable. `codex app-server daemon start` failed with the same missing-executable error. `codex --no-daemon` reached the signed-in interactive prompt in a terminal test. The ordinary daemon-backed startup is not repaired; no daemon update or restart was attempted because Codex Desktop sessions were active. The workaround has not been tested in the user's Herdr pane.

### Installed setup on Joshua's Windows machine

Re-verified and updated on 2026-10-10 (the 2026-09-22 install had drifted: Herdr was off the user PATH and no `codex` command resolved):

| Component | Installed state, 2026-10-10 |
|---|---|
| Herdr | Stable `0.9.3`, installed with `herdr update`; under `C:\Users\Joshu\.herdr\packages\standalone\releases\0.9.3-x86_64-pc-windows-msvc`, which is on the user PATH. `0.9.1` is still on disk, unused. |
| Claude Code | `2.1.295` at `C:\Users\Joshu\.local\bin\claude.exe` |
| Codex CLI | `0.162.1` from npm `@openai/codex`, in `C:\Users\Joshu\dev\tools\node` (first on the user PATH); signed in with ChatGPT. A second copy in `AppData\Roaming\npm` is invisible inside Herdr and is shadowed by the first. `firecrawl-cli` `1.26.3` and `@klingai/cli-global` `0.2.1` are installed beside it for the same reason. |
| Herdr integrations | Claude `v10` and Codex `v8`, both reported current by `herdr integration status` |
| Herdr agent skill | Refreshed from the official `herdrdev/herdr` copy (SHA-256 `b16ba0d9…`) in `~/.claude/skills/herdr` and `~/.agents/skills/herdr` |

The 2026-09-22 values were Herdr `0.9.1`, Claude Code `2.1.280` and Codex CLI `0.156.1`, both CLIs in a shared Node tools directory. That directory did not exist when checked on 2026-10-10, and was recreated that day.

**Keep CLIs out of `AppData` for Herdr.** Windows Terminal is a Microsoft Store app. Anything it launches, including the Herdr server and every pane, sees `AppData\Roaming\npm` as an empty folder (verified 2026-10-10: a pane listed no files there while the disk had them). Tools installed with plain `npm install -g` are therefore invisible inside Herdr. Install them with `npm install -g --prefix C:\Users\Joshu\dev\tools\node <package>`. The desktop shortcut's launcher `C:\Users\Joshu\.herdr\launch-herdr.ps1` also rebuilds PATH from the registry on every start.

**What a pane sees, verified 2026-10-10** in a separate test session started through Windows Terminal: `codex`, `firecrawl`, `kling`, `gws`, `claude`, `herdr`, `node`, `git`, `gh`, `py`, `ffmpeg`, `yt-dlp`, `deno` and `uv` all resolve; Codex `0.162.1` and Claude Code `2.1.295` run; Codex reports ChatGPT sign-in; the vault and both skill folders are readable. An already-running Herdr server keeps the environment it started with, so run `herdr server stop` and relaunch from the desktop shortcut to pick up the new PATH.

**Windows clipboard-image paste, 2026-10-11.** Herdr's native local Windows panes do not provide its clipboard-image bridge. AutoHotkey v2 is installed with a user startup shortcut at `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Herdr image paste.lnk`; its active script is `C:\Users\Joshu\.herdr\clipboard-paste\herdr-image-paste.ahk`. Windows Terminal's Ctrl+V paste binding is unbound so the key can reach the focused CLI. The AutoHotkey shortcut checks whether the clipboard contains an image: for images it forwards Ctrl+V to the CLI for its native image attachment; for text it sends Windows Terminal's Ctrl+Shift+V text-paste shortcut. The image check is `C:\Users\Joshu\.herdr\clipboard-paste\has-image.ps1`. The previous path-insertion helper remains at `paste-image.ps1` as a fallback but is not used by the active shortcut. Clipboard detection is verified; an end-to-end attachment in the live Herdr panes remains unverified.

**Skills seen from a terminal launch, 2026-10-10.** Claude Code started in the vault loads 376 skills, 7 agents and 11 plugins. Codex reports about 200 skills in its visible list, and its own startup warning says the skills context budget was exceeded, all descriptions were dropped and 321 skills were left out of the visible list. Codex has 303 unique skills across its three roots (project `.agents/skills`, `~/.agents/skills`, `~/.codex/skills`). Told to look for `wrapup` and `herdr`, two skills missing from its visible list, Codex found both by listing the folder. Automatic triggering of hidden Codex skills was not shown.

**Skill differences for Claude, 2026-10-10.** `claude-build` and `pre-consultation-check-in` are Codex-side by declared design in `skills/PARITY.md`. `kling-cli` is declared active for both runtimes, but its project copy under `.claude/skills/kling-cli` was deleted in the working tree (uncommitted) while the `.agents` copy was being edited, so Claude does not load it. Not changed here. `system/scripts/check-skills.sh` could not run because `python` is the Microsoft Store stub on this laptop; `py` works.

Not checked: Herdr panes with Claude and Codex editing side by side in your live session.

Open a new PowerShell window so it receives the updated user PATH. Then:

```powershell
cd C:\Users\Joshu\dev\ai-os
herdr
```

Inside Herdr, use the first pane for Claude Code:

```powershell
claude
```

Split right with the mouse menu or press `Ctrl+B`, release, then press `V`. In the new pane:

```powershell
codex
```

Recommended layout:

| Pane | Purpose |
|---|---|
| Left | Claude Code as the primary operator or planner |
| Right | Codex as reviewer, critic, or independent implementer |
| Optional bottom pane | Dev server, tests, or logs |

Herdr improves visibility but does not change the shared-worktree guardrail: Claude and Codex may read the same files, but they must not edit the same file at the same time. Assign explicit file ownership or use a worktree when both are implementing.

First-run checks:

```powershell
herdr integration status
herdr agent list
```

If an agent is detected incorrectly, run `herdr agent explain <target> --json`. The Windows config file is `%APPDATA%\herdr\config.toml`; no custom config is required for the initial setup.

## Where ai-os stands (gap-check, 2026-09-22)

ai-os **already runs this exact pattern** — it was built dual-runtime from the reform (see `wiki/log.md` 2026-07-17, and [[../decisions/log.md]]). Point-by-point:

- **`CLAUDE.md` + `AGENTS.md` hand-owned twins** — present, mirrored, near-identical byte size. The only diffs are the *intentional* Claude↔Codex swaps (twin pointer, folder paths, the dual-runtime section written from each runtime's view). Voice section is in full parity. **No drift.**
- **`.claude/` and `.codex/` config folders** — both present (`.codex/hooks.json` mirrors the SessionStart bootstrap).
- **Skills as identical markdown, activated by copy** — `.claude/skills/` (22) and `.agents/skills/` (12); Codex runs the same business set minus the wiki/Obsidian/graphify/youtube extras, which is deliberate, not a gap.
- **`session-handoff` skill** — Nate's skill, already installed and active in both runtimes.
- **Agents as TOML for Codex** — catalog holds `agents/codex/web-researcher.toml`. Note: that agent is authored to activate **globally** (its module path is `~/.codex/agents/web-search-modules/`), so it is not project-activated into `~/ai-os/.codex/agents/`, and that is by design, not missing wiring.

**Conclusion:** the first two clips validated the shared-file architecture. The third exposed a real execution gap: there was no persistent, visible session layer for running both agents together. Herdr now fills that gap on this Windows machine. The remaining human step is Claude authentication on first launch.

## What's new vs already-known

- **New and implemented:** Herdr as the visible, persistent execution layer for Claude Code and Codex; direct integrations and the Herdr agent skill are installed for both.
- **Worth adopting as a habit:** the plan↔critique and adversarial-review ping-pong between the two models on genuinely hard or high-stakes work; reach for the Codex desktop app's live browser + annotation when doing front-end review.
- **Already true in ai-os:** the whole file-structure map, twin instruction files, copy-based skill activation, session-handoff bridge, tool-agnostic stance.

## Choosing Sonnet or Opus inside Claude (source claim, 2026-10-12)

Nate Herk's seven-task test argues for Sonnet 5.5 when the task has a clear spec and a check, and Opus 5.5 when the goal is vague or taste-driven; with a skill defining the output, the two came out close and the cheaper one won. Single runs, his judging, API prices. Untested on our work. [Source summary](../wiki/sources/sonnet-5-5-vs-opus-5-5-nate-herk.md).

### Our test: Sonnet 5.5 vs Opus 5.5 on two lint skills (2026-10-14, AQ-004)

Each skill ran twice on the same fixed input. Each run was a fresh subagent with `model: sonnet` or `model: opus`. Every run was read-only and reported without fixing anything. Inputs:

- **second-brain-lint:** `py system/scripts/wiki-maintenance.py --lint`, plus a semantic pass over `wiki/sources/`, `CLAUDE.md`, `AGENTS.md`, `wiki/hot.md` and the memory index. No `--evidence`.
- **skill-lint:** an audit of `second-brain-query` across every runtime copy, plus `skills/PARITY.md`.

Time is wall clock and usage is the subagent token total, both as the harness reported them.

| Skill | Model | Skill's own check | Result | Time | Usage | Verdict |
|---|---|---|---|---|---|---|
| second-brain-lint | Sonnet | Passed: script ran, steps 1-6 covered in scope | Script: 2 thin pages, 2 broken links in `wiki/log.md`. 12 findings, mostly metadata and freshness: the `hot.md:10` pickup tension, stale 2026-07-16 lines in `hot.md`, and 16 pre-convention source pages without `evidence:`. 11 entity candidates. Three findings spot-checked and correct | 145 s | 108k tokens, 8 tool calls | Same structural result. Shallower on meaning: it found no contradictions between pages |
| second-brain-lint | Opus | Passed | Script: the same 4 findings. 12 findings that are mostly real contradictions: source pages saying Rea, Orca and 21st.dev are "not installed" when they are; one page with a conflict recorded but `contradictions: []`; `CLAUDE.md:131` "never this file", which is wrong inside `CLAUDE.md`; two skills claiming to be the single LSAT U entry point. Two spot-checked and correct | 474 s | 216k tokens, 29 tool calls (rerun after the first Opus run hit the usage limit) | Better: it caught the cross-page contradictions that step 4 asks for. It cost about 2x the tokens and 3x the time |
| skill-lint | Sonnet | Passed | 5 copies found. 4 project copies identical (it gave SHA-1 without labeling it). No confirmed defects. Flagged the `wiki/synthesis/` path as a minor wording issue. Said `rg` is missing (true only on the Git Bash PATH) | 66 s | 96k tokens, 6 tool calls | Close, but missed two things Opus found |
| skill-lint | Opus | Passed | 7 copies found, including the home `.agents` and `.codex` dispatchers that Sonnet missed. Confirmed the `wiki/synthesis/` path as a defect, with a fix. Found that the Karpathy generated catalogs carry no `Also:` aliases (0 of 3,831 entries) | 121 s | 100k tokens, 8 tool calls | Better: wider discovery and one real gap Sonnet missed, for about the same tokens |

**Reading:** Sonnet matched Opus on the deterministic part of both skills: the script counts, and finding and hashing the copies. Opus was better on the judgment part, which is the reason these skills exist. It found contradictions between pages, extra dispatcher copies, and an alias gap in the catalog. On skill-lint the extra depth cost almost nothing (100k vs 96k tokens). On second-brain-lint it cost 2x the tokens. These are single runs, so treat them as evidence, not proof.

**Recommendation (Joshua decides; nothing changed):** Neither skill met step 4's "Sonnet matched Opus" bar, so do not add `model: sonnet` to either one. A cheaper option for second-brain-lint is to run the script by itself (`py system/scripts/wiki-maintenance.py --lint`) for routine structural checks. That needs no model at all. Keep the full Opus lint for after an ingest batch. No `model:` line has been added to any skill.

Side note: `wiki-maintenance.py --lint` is not purely read-only. Each run rewrites `system/generated/wiki-lint.generated.tsv`. Both benchmark runs did this. It is a generated file, so this is expected, but it is a write.


## Claudex skills installed globally (2026-09-30)

Current upstream: https://github.com/chaseai-yt/claudex-loop, installed from commit `8cf5e2c1771c5151d90c12642391d0ba8fa71b0e`. Clone: `C:/Users/Joshu/dev/ai-os-projects/claudex-loop`, outside the vault. All four current skills (`claudex-route`, `claudex-loop`, `codex-review`, `codex-build`) and both local compatibility aliases (`grill-me-codex`, `grill-with-docs-codex`) are complete copies in both catalogs and project activation directories, plus global `.agents/skills`, `.codex/skills`, and `.claude/skills`. No linking into the application directory.

Prefer `claudex-route` for one scoped handoff, and `claudex-loop` for repeated independent review and implementation. The host-aware loop sends Codex work to Claude for review and Claude work to Codex. Both grill names now delegate to this current loop; the docs variant preserves context, glossary, and architecture decisions. Local alias sources live in `system/skill-overrides/claudex`. The updater copies these instead of upstream legacy instructions. Shared references and Python runner ship with the complete current package. Existing conversations may need a new session to refresh discovery.

Both CLIs authenticated on 2026-09-30: Codex 0.156.1 and Claude Code 2.1.280. Metadata validation, 23 package tests, and both role-routing checks pass. These checks do not establish a completed live model review; the earlier stalled review remains a failed run.

Automatic updater: `system/scripts/sync-claudex-skills.py`. Codex app automation `update-claudex-skills` runs daily at 07:00 America/Toronto while the local automation host is available. It fast-forwards the clean clone and updates only seven declared skill names, preserving older copies under `~/.agents/claudex-backups` and refusing to overwrite locally edited trees. State is `~/.agents/claudex-sync-state.json`. Run without `--install` for routine updates; that flag explicitly adopts existing versions and is only for supervised initial installation. No deletions, commits, pushes, CLI upgrades or review/build launches occur during sync. Skills INDEX is regenerated after changes.


### Ask Codex to grill by Claude

`grill-by-claude` is a locally maintained entry point installed in both catalogs and all five activation roots. Say "grill by Claude" in Codex: Codex interviews and prepares the plan, calls the authenticated Claude Code CLI for independent review, evaluates findings, and revises within the shared loop limits. Review alone does not authorize implementation. Verified runner roles select Codex planner and Claude reviewer; this installation check did not perform a live model review. The updater maintains this alias alongside the other two local compatibility names.


### Every Claudex skill has the inverse Codex direction (2026-09-30)

Supersedes the shared-entry-point installation details above. All six package skills now have runtime-specific entry points. Claude installations coordinate toward Codex; Codex installations coordinate toward Claude. codex-review retains its familiar name but asks Claude to review in Codex. codex-build delegates to Claude in Codex, using build --host codex --builder claude and fresh inspect --host codex --builder claude. The Claude copy retains Codex builder and Claude inspector. The loop defaults to the host builder with other-provider inspection, and route defaults to the other provider for cross-provider handoffs while honoring explicit user choices.

The updater renders separate entry points and hashes for each runtime, preserving complete upstream supporting files. Codex review/build adaptations are locally maintained in system/skill-overrides/claudex/codex; future upstream support updates do not overwrite these intentional directions. Seven roots contain matching copies for their runtime. Verified metadata, both inverse role maps, idempotent repeat sync, and preservation of edited targets. These checks did not launch a live provider review/build.


### Codex entry points renamed (2026-09-30)

Supersedes retained-name descriptions above. Codex now exposes claude-review, claude-build, grill-me-claude, and grill-with-docs-claude. Claude retains the corresponding Codex names. claudex-loop and claudex-route remain unchanged in both runtimes. The sync maps source names to installed names, updates frontmatter, and moves previously managed old Codex copies into inactive backups after verifying their replacements. Edited old copies are preserved as conflicts. The grill-by-claude shortcut remains available.

### Stateful UI work orders require transition evidence (2026-10-01)

After the LSAT U study-tools review, Joshua requested durable prevention guidance for Claude. Future delegated stateful UI work orders must specify state ownership and lifetime, then require actor-switch isolation, multiple edits during failed persistence, selected-answer/cross-out consistency, reducer-committed persistence under rapid interactions, and touch/keyboard accessibility checks where applicable. Include these acceptance checks in the actual work order; do not rely on remembered guidance alone. Inspect the final mixed snapshot after fixes and distinguish tested behavior from blocked browser checks.

The detailed failure cases and corrective instructions are indexed in Claude's native ai-os memory as `lsatu-study-tool-transition-checks.md`. Reviewers must trace existing behavior before calling it missing: the initial LR-find omission claim was false. Memory is guidance; regression tests and independent inspection provide enforcement. Keep Claude and Codex file ownership separate and preserve all existing student records.

## Captured harness changes need version and workflow checks (2026-10-26)

[Chase AI's Claude mods clip](../wiki/sources/claude-mods-chase-ai.md) describes plugin-based, persistent event and UI customizations, distinct from manually invoking a skill. Its examples include next-step choices, cache/compaction display, project and demo helpers, and before/replace/after/wrapped deletion actions. The reusable idea is to identify repeated requests from recent sessions before choosing a customization; this overlaps the existing correction-analysis queue AQ-012. The transcript does not establish an official API, desktop/terminal parity, installed availability or subscription-cache economics. AQ-040 holds the evaluation, with no plugin installed by ingestion.

[A refreshed Codex CLI walkthrough](../wiki/sources/meet-new-codex-cli.md) presents a full-screen interface, voice, searchable task views and cross-task follow-ups, worktree forks, phone remote control, usage analytics and Mermaid/LaTeX rendering. These are captured claims with unspecified release/version/account requirements. Native within-Codex task management may overlap some monitoring, while Herdr covers mixed-provider terminals; neither source establishes complete replacement or persistence equivalence. AQ-041 holds a current-capability comparison. The historical local setup tables above were not reverified or upgraded in this ingest.

## ClaudeX Loop clip, and running `codex-build` from the Claude desktop app on Windows (2026-11-14)

[Chase AI's ClaudeX Loop walkthrough](../wiki/sources/claudex-loop-chase-ai.md) demonstrates the same plan-review and build-inspection method installed on 2026-09-30, from one promoter's demo. Complementary: no change to the local skill.

### Running codex-build on this Windows machine (tested 2026-11-14)

This replaces the earlier 2026-11-14 note here, whose "private view" explanation was wrong. What was found:

- The Codex CLI I could run from the Claude app's Bash tool was installed only in that tool's own view of `AppData\Roaming\npm`. Joshua's real PowerShell had no `codex` command. The Codex desktop app does not ship a plain CLI.
- Even with a fresh CLI in the real shell, the sandbox failed with `CryptUnprotectData failed: 2148073483`. The cause was the saved sandbox login file, `~/.codex/.sandbox-secrets/sandbox_users.json` (written 2026-11-11), which Windows could no longer decrypt.
- Moving that file aside and rerunning from the real shell made Codex recreate it. Doing the same from a hidden shell fails with error 1223, because the Windows approval prompt cannot appear. The old file is kept as `sandbox_users.json.bak-2026-11-14`.
- `codex sandbox -- cmd /c ...` from the checkout then failed with `CreateProcessWithLogonW failed: 267`. That standalone command is not a reliable test; the real build ran fine.

Result: a real throwaway build through the runner (`--builder codex`, `workspace-write` sandbox) from the real shell created the requested file, exact bytes, in 222 seconds. Claude verified the file and removed it. Codex's own proof command failed because `python` is not on the sandbox's PATH and `Get-FileHash` is missing. The upstream project reports the same limit ([claudex-loop VALIDATION](https://github.com/chaseai-yt/claudex-loop)), so **the host must run the proof and inspect every changed file itself**.

The working path, in order:

1. Install the CLI in the real shell, once: `npm install -g @openai/codex` (done 2026-11-14, version 0.169.0, logged in with ChatGPT).
2. Make an isolated, clean checkout that holds every input the work order names. This vault's last commit is 2026-10-01, so most current files are uncommitted; copy them into a worktree and commit a baseline there. The first one is `C:/Users/Joshu/dev/ai-os-codex-ore` (branch `codex/ore-notes-2026-11-14`, baseline `157cfef5`).
3. Keep the work order outside the checkout.
4. Start the build from the real PowerShell with `system/scripts/run-codex-build.ps1`, which checks the CLI, the login and a clean checkout, then calls the runner with `--cli` set to the real Codex path.
5. Claude then runs the proof, runs `inspect`, and reads every changed and untracked file before anything reaches Joshua.

The Bash tool cannot launch it: `codex` there is the private copy and its sandbox cannot show the Windows approval prompt.


## Persistent task checkpoints (2026-11-14)

For a shared task record and explicit writer transfer, follow [Switch between Claude Code and Codex](ai-workspace/switching-agents.md). This is separate from the existing chat-only `session-handoff` contract. Native conversations remain in their own applications.

**Fixed later the same day: Python inside the Codex sandbox.** Codex's official Windows page ([windows-sandbox](https://learn.chatgpt.com/docs/windows/windows-sandbox)) recommends the `mxc` sandbox mode (no admin setup, no extra accounts or firewall rules; needs Windows 24H2 build 26100.9278 or 25H2 build 26200.9278 or later; this machine is 10.0.26300). `[features] prefer_mxc = true` was added to `~/.codex/config.toml` (backup `config.toml.before-mxc-20261114.bak`). Tested: `codex -c windows.sandbox=mxc sandbox ... -- python -V` printed Python 3.12.10, while `py -V` fails there ("No installed Python found"), so **use `python`, never `py`, in anything Codex runs**. A throwaway build through the runner then created the file and ran its proof with `python` inside Codex (201 seconds). Still blocked inside Codex: PowerShell profile loading and `Get-FileHash`; network access (an earlier run could not download a runtime). Whether Codex may use the network is a separate setting, `[sandbox_workspace_write] network_access`, not changed here. Do not leave an orphaned `codex exec` running: stopping the Terminal tab does not stop it; kill the process tree.
