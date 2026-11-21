---
name: claude-build
description: Codex-to-Claude build workflow. Delegate a concrete work order to Claude Code, then have Codex independently inspect and verify the changes.
---

# Claude builds, Codex coordinates and inspects

Invoke this Codex-side skill as `claude-build`. In this Codex installation, the builder is explicitly Claude. The Claude installation retains Codex as builder.

Read the sibling `../claudex-loop/references/build.md` and `../claudex-loop/references/runtime.md`. Resolve the runner from the installed sibling skill. Preserve SPEC_FILE as the actual `--plan` path, LOG_FILE, PROOF_CMD, MAX_FIX_ROUNDS, and explicit model/effort choices. Never substitute PLAN.md for a supplied spec.

On Windows, a recognized npm wrapper can now point to a native Claude binary instead of cli.js. If the runner rejects the wrapper, read that installed wrapper to resolve its actual executable, verify its version, and supply the absolute native path through --cli. Do not guess a path, rewrite global PATH, weaken permissions, or switch models. Verify requested model/effort in command.json; distinguish those flags from the returned observed_models identity.

Codex coordinates and delegates authorized implementation through `build --host codex --builder claude`. Use current valid plan approval when following the loop. An explicitly requested standalone work order may use `--unreviewed-spec`, recording that status. Settle material missing requirements before building. Review-only requests do not authorize implementation.

Record the pre-build baseline, preserve unrelated edits, and pause host edits to delegated files. Validate the completed builder result and inspect every changed file, including staged and untracked work. Run the agreed proof commands independently in Codex. Obtain a fresh Codex inspection using `inspect --host codex --builder claude`, supplying the same spec and the pre-build baseline. Do not ask Claude to certify its own work as independent inspection.

Check setup separately from implementation. An untrusted-workspace warning can mean project allow rules are ignored, even when Claude launches and Read/Write work. Version success does not prove shell or proof-command access. After a required setup command is denied, stop that setup path and report the exact blocker; do not spend the build window manually reconstructing a large snapshot file by file. The host may perform the authorized, path-checked, hash-verified setup portion and record it, as the build reference permits. Do not change global trust, bypass permissions, or claim the build completed from partial files. A timed-out result cannot be resumed as a successful runner result; preserve its artifacts and distinguish any salvaged files from an integrated, verified build.

Keep fix rounds bounded and inspect again after accepted fixes. If Codex takes over coding, its new edits require fresh Claude inspection. If both providers contribute, record authorship and have each inspect the other's work. Report failed calls, unresolved findings, actual coverage, and unreviewed edits honestly. Preserve existing commit, push, and publication authorization.

## Windows result and inspection diagnostics

Launch the Python runner with `python -X utf8` on Windows so Unicode reports do not fail while printing to a legacy console. If printing fails after result.json was saved, inspect its status, provider exit code, returned session and output; distinguish report-printing failure from builder failure. Never fabricate or rewrite a completed result.

Codex CLI configurations that expose shell only through code mode may return `code-mode host is disabled` under the required inspection restrictions. Preserve BLOCKED and the actual coverage. Do not enable integrations or weaken reviewer flags to obtain approval. A separately scoped, read-only independent review may supply additional evidence, but must be disclosed as a workflow deviation and never relabeled as successful CLI inspection.
