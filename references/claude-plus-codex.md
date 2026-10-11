---
type: reference
subject: Running Claude Code and Codex on one project the idea, and where ai-os stands
updated: 2026-10-10
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

### Installed setup on Joshua's Windows machine

Re-verified and updated on 2026-10-10 (the 2026-09-22 install had drifted: Herdr was off the user PATH and no `codex` command resolved):

| Component | Installed state, 2026-10-10 |
|---|---|
| Herdr | Stable `0.9.3`, installed with `herdr update`; under `C:\Users\Joshu\.herdr\packages\standalone\releases\0.9.3-x86_64-pc-windows-msvc`, which is on the user PATH. `0.9.1` is still on disk, unused. |
| Claude Code | `2.1.295` at `C:\Users\Joshu\.local\bin\claude.exe` |
| Codex CLI | `0.162.1` from npm `@openai/codex`, in `C:\Users\Joshu\AppData\Roaming\npm`; signed in with ChatGPT |
| Herdr integrations | Claude `v10` and Codex `v8`, both reported current by `herdr integration status` |
| Herdr agent skill | Refreshed from the official `herdrdev/herdr` copy (SHA-256 `b16ba0d9…`) in `~/.claude/skills/herdr` and `~/.agents/skills/herdr` |

The 2026-09-22 values were Herdr `0.9.1`, Claude Code `2.1.280` and Codex CLI `0.156.1`, both CLIs in a shared Node tools directory that no longer exists on this machine. Not checked: an interactive Herdr launch with both agents in panes, and whether panes launched from a Microsoft Store PowerShell can see `AppData\Roaming\npm`.

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
