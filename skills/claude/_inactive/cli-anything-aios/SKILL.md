---
name: cli-anything-aios
description: Use when building, refining, testing, validating, or listing CLI-Anything harnesses for GUI applications or source repositories. Read the complete bundled methodology and mode-specific command files before acting.
---

# CLI-Anything for Claude Code

Use the installed `cli-anything` Claude Code plugin commands for harness work:

- `/cli-anything <path-or-repo>` builds a harness.
- `/cli-anything:refine <path> [focus]` expands an existing harness.
- `/cli-anything:test <path-or-repo>` runs its tests.
- `/cli-anything:validate <path-or-repo>` checks it against the methodology.
- `/cli-anything:list [options]` discovers generated harnesses.

Before work, read `HARNESS.md` and the matching specification under `commands/`. Read applicable files under `guides/` when the command specification calls for them. The official user-level plugin provides the slash commands after Claude Code reloads. If the plugin commands are unavailable, use the bundled methodology directly and report that the plugin was not discovered.
