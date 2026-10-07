---
name: codex-build
description: Codex-host inverse of the Codex Build entry point. Delegate a concrete work order to Claude Code, then have Codex independently inspect and verify the changes.
---

# Claude builds, Codex coordinates and inspects

The retained name `codex-build` is a compatibility name. In this Codex installation, the builder is explicitly Claude. The Claude installation retains Codex as builder.

Read the sibling `../claudex-loop/references/build.md` and `../claudex-loop/references/runtime.md`. Resolve the runner from the installed sibling skill. Preserve SPEC_FILE as the actual `--plan` path, LOG_FILE, PROOF_CMD, MAX_FIX_ROUNDS, and explicit model/effort choices. Never substitute PLAN.md for a supplied spec.

Codex coordinates and delegates authorized implementation through `build --host codex --builder claude`. Use current valid plan approval when following the loop. An explicitly requested standalone work order may use `--unreviewed-spec`, recording that status. Settle material missing requirements before building. Review-only requests do not authorize implementation.

Record the pre-build baseline, preserve unrelated edits, and pause host edits to delegated files. Validate the completed builder result and inspect every changed file, including staged and untracked work. Run the agreed proof commands independently in Codex. Obtain a fresh Codex inspection using `inspect --host codex --builder claude`, supplying the same spec and the pre-build baseline. Do not ask Claude to certify its own work as independent inspection.

Keep fix rounds bounded and inspect again after accepted fixes. If Codex takes over coding, its new edits require fresh Claude inspection. If both providers contribute, record authorship and have each inspect the other's work. Report failed calls, unresolved findings, actual coverage, and unreviewed edits honestly. Preserve existing commit, push, and publication authorization.
