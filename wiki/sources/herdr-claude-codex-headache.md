---
type: source
subject: Chase AI video, Herdr for Claude Code and Codex
created: 2026-10-10
updated: 2026-10-10
aliases: [Herdr clip, This Repo Just Solved The 1 Claude + Codex Headache]
tags: [ai-workspace, claude, codex, herdr, terminal]
sources: [../../raw/sources/clips/herdr-claude-codex-headache/PROVENANCE.md]
---

# Herdr gives many coding agents one organized, persistent home

Chase AI's video "This Repo Just Solved The #1 Claude + Codex Headache" ([YouTube](https://www.youtube.com/watch?v=neK8ydl0Vlk), published 2026-07-16) presents Herdr, a free terminal multiplexer for running several coding agents at once. The full clip transcript was read on 2026-10-10 (about 10:18 of video). Herdr's repository is linked in the description as `github.com/ogulcancelik/herdr`; the captions mis-hear the name as "Herder" and "Hurder".

Evidence: [archived clip, provenance and hashes](../../raw/sources/clips/herdr-claude-codex-headache/PROVENANCE.md). Archived clip SHA-256 `44d232646d6de038bfeecc4e2496f01b60ce16b305b87b377fcfb7b8a8f47d2e`.

**This video was already ingested on 2026-09-22.** That ingest updated [Claude and Codex on one project](../../references/claude-plus-codex.md) and installed Herdr, but wrote no source summary and archived no clip. This page is the missing source summary, written from a newer caption generation. The provenance file lists all three clip copies and records an unresolved hash discrepancy for the 2026-09-22 file.

## What the video claims

All of this is the narrator's account, checked here only where noted.

- **Three benefits (0:31).** Organization (one window instead of many loose terminals), monitoring (a sidebar showing which agents are working, done or stuck), and persistence (Herdr runs as a server, so closing the window does not stop the agents; reopen and they are still running).
- **Versus tmux and Cmux (1:43 to 2:17).** The narrator says tmux does not show agent status out of the box, and that Cmux lacks persistence and is hard to use on Windows. He also says a running session can be reached from a phone or over SSH.
- **Install (2:33).** One line from `herdr.dev` or the GitHub page, then type `herdr`.
- **Structure (2:56 to 5:37).** Spaces are projects, tabs are subtasks inside a space, and panes hold the agents. Everything is mouse-clickable, not only keybinds.
- **Claude and Codex together (5:37 to 8:14).** His main use is making visible what is normally done headlessly: a skill where Claude plans, Codex critiques, and they iterate. With the Herdr skill he has Claude open a pane that shows that exchange live.
- **The Herdr skill (6:44).** It teaches an agent to create panes and spaces itself. One line installs it, and he mentions a plugin marketplace for add-ons.
- **Persistence demo (8:14).** He closes the terminal completely mid-task, relaunches with `herdr`, and both agents are still working. He says this survives as long as the computer stays on.
- **Keybinds (9:05).** Tmux-like: `Ctrl+B` for prefix mode, then a key (for example `V` to split vertically).
- **Scope claim (9:47).** Claude Code's own agent view works only inside Claude Code; Herdr covers any harness, including Codex and OpenCode.

## What was checked against reality

Checked 2026-10-10 against Herdr's own CLI help, its published agent guide (`herdr.dev/agent-guide.md`) and the GitHub releases API:

- Herdr is a terminal workspace manager with a background server, workspaces, tabs and panes, agent state in a sidebar (`working`, `blocked`, `done`, `idle`, `unknown`), and the `Ctrl+B` prefix. The narrator's description matches. The official guide says new users need no keybindings.
- Persistence matches: panes survive a closed window, and `herdr server stop` is the explicit stop.
- Naming: the guide calls the top level a "workspace". The video says "space". Same thing, different wording.
- Release state on 2026-10-10: the latest stable release is `v0.9.3`, published 2026-09-29, with a Windows build. `herdr update` installs it.
- The video's claim that Cmux lacks persistence, and the tmux comparison, were not checked.

## Limitations

- Captions, not a script. Product names, tool comparisons and the phrase "Fable" in the demo should be checked against the video before quoting.
- The video is a creator's endorsement with a sponsor link to his paid community. No benchmarks are given.
- The demo skill ("Codex review") is the narrator's own and is not identified here.

## How it fits this workspace

Status: **implemented and checked locally** for the install, not yet for a hands-on session. The working reference is [Claude and Codex on one project](../../references/claude-plus-codex.md), which holds the installed setup table, first-run commands and the shared-file guardrail. On 2026-10-10 that table was corrected after finding Herdr off the user PATH and no `codex` command resolving; Herdr is now `0.9.3`, Codex CLI `0.162.1` and Claude Code `2.1.295`. Details and open checks are on that page and in the [log](../log.md).

Related: [AI workspace hub](../../references/ai-workspace/index.md), [Claude plus Codex](../../references/claude-plus-codex.md).
