---
type: source
subject: Nick Saraev video, Rea (Reverse Engineer Anything)
created: 2026-10-12
updated: 2026-10-12
aliases: [I Tested The Viral Github Repo To Reverse Engineer Anything, Rea clip, REA]
tags: [ai-workspace, claude, mcp, reverse-engineering, tools]
sources: [../../raw/sources/clips/reverse-engineer-anything-rea-saraev/PROVENANCE.md]
---

# Rea gives an agent decompiler tools; the creator calls the hype ahead of the demos

Nick Saraev's video "I Tested The Viral Github Repo To Reverse Engineer Anything" ([YouTube](https://www.youtube.com/watch?v=dAzs_rU6080), publication date unknown) tests Rea (`morluto/rea`). Both clip generations were read in full on 2026-10-12 (about 10 minutes of video). The transcript is ASR-grade.

Evidence: [archived clips, provenance and hashes](../../raw/sources/clips/reverse-engineer-anything-rea-saraev/PROVENANCE.md). Clip 1 SHA-256 `d2fc42c57ca5fce94b38f86aea58710f237ee66631ae4bf981b1fe2bde70d2c3`; clip 2 `81a0ca9cf85539bc06f50350c8e9d3871d2f4f39e3116574a141e9d5962e76b0`. Same video, caption wording differs slightly.

## What the video claims

- **What Rea is (0:00 to 1:51).** An MCP that lets an agent decompile an existing app and then rebuild its features. The agent calls Rea, which drives Ghidra (he says 2019, released by the NSA), Hopper (about 2011) and IDA (1990s), plus Chrome DevTools. It returns pseudo-code, proof and a list of unknowns, and the agent loops until it has rebuilt the app.
- **Install (2:20).** Tell your agent to download Rea. He runs it inside Orca, a terminal manager that splits panes for Claude and Codex.
- **His test (2:51 to 5:19).** He asked Claude to rebuild macOS Preview with Rea and, in parallel, without it. The version without Rea finished first, a bit laggy; the Rea version took longer, then matched Preview closely (zoom, share, draw, rotate, save), and drawing was faster.
- **His main point (5:19 to 7:27).** Rea adds no new capability: it packages old tools behind one interface. The hype is a "memetic cultural moment," and videos that open with GitHub-star graphs usually lack a good demo.
- **Prediction (7:32 to 10:42).** Most software becomes open source and front ends and back ends commoditized. Wrapper apps get absorbed by the models. Reverse-engineering a favorite app to sell it faces "severe intellectual property restrictions." Plain Claude can get about as far in roughly two-thirds the time, and he expects Claude Code to absorb much of this.

## What was checked (2026-10-12/13, GitHub API and README)

- `morluto/rea`: MIT, created 2026-04-14, about 161,000 stars (113,000 the day before in the first check, so the count is moving fast), pushed 2026-10-13.
- Its README describes one MCP for reverse engineering binaries, JavaScript/Electron apps, .NET assemblies and websites. Setup is `npx rea-agents setup`, which registers the MCP with your agent and installs workflow instructions, with backups. It can use an existing Hopper, Ghidra or IDA install, and can optionally install Hopper with approval. Analysis runs locally. Supported agents include Claude Code and Codex.
- This matches the narrator's description. His speed and quality comparison is one informal test, not a benchmark.

## What it means here (interpretation)

- **Not installed.** You do not have a Rea or general reverse-engineering skill. The nearest is `site-teardown`, which covers web pages only. See [the ten-repos summary](10-new-github-repos-make-money.md) where Rea was rated medium-low.
- **Fit.** It could help study how another prep platform's app or site behaves. It has no open task in this vault. The narrator's own result says vanilla Claude gets most of the way for visible features.
- **Caution.** Decompiling a commercial app and shipping a copy is an IP problem, as the narrator says. Use it on software you own or have rights to inspect.
- **Setup cost.** `npx rea-agents setup` edits agent configuration and may install Hopper. Run it only as an explicit, reviewed step.

Status: **captured and checked against the README**, not installed or tested.

## Limits

Publication date unknown. Demo outcome is one run on a Mac app; this machine is Windows. Star counts are volatile.

Related: [AI workspace hub](../../references/ai-workspace/index.md), [Nate Herk repos](100-github-repos-for-claude-nate-herk.md).
