# Codex Stop hook is prepared; native trust review remains

Verified 2026-10-08. Joshua selected Codex in place of the video's Claude runtime.

The project has `.codex/hooks.json` with `UserPromptSubmit`, `SubagentStart`, `PreToolUse`, `PostToolUse`, `Stop`, and `SubagentStop` handlers. All call the standard-library [Codex adapter](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/codex_stop.py). Existing user hooks and global configuration were not changed.

## What the adapter enforces

- An explicit `$karpathy-teach` or `/karpathy-teach` prompt, an actual project skill-file read, or a native `karpathy` subagent marks the turn as scoped. Subagent startup marks both the child and the launching parent's turn.
- A real code-file change sets a pending execution. Snapshots observe project code and the external examples; explicit file edits and patch paths also observe code outside those roots. Files under raw, credentials/runtime directories, dependencies, and symlink directories are excluded from recursive scans.
- A later completed real runtime command clears the pending execution. Help/version/install/read-only commands do not. An asynchronous command does not count until its terminal result arrives. A later code change invalidates the earlier run.
- A failed real command counts as executed, with its exit/output evidence retained. It does not establish that the code works. Relevance, correctness and failure disclosure remain part of the seven-rule answer grade.
- A scoped pending edit blocks Stop using exactly `Karpathy rule, run it before you say it works.` The continuation preserves unresolved edits. A new ordinary human turn resets scope. Unrelated sessions continue normally.

The adapter uses documented Codex hook payload fields and event state. It does not parse Claude transcripts or depend on an unstable Codex rollout format. State is stored outside the vault in `C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/runtime/codex-hooks/`. Per-session OS locks and atomic replacements protect concurrent hook invocations.

## Local verification

[25 tests](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/test_codex_stop.py) passed. They cover scope, ordinary sessions, actual/relative skill reads, native child and parent scope, unchanged failed patches, code writes, actual outside-root snapshots, later edits, failed executions, informational commands, structured and text asynchronous starts/completion, retry continuation and new-turn reset.

These are event simulations and local adapter tests. They do not certify a live Codex Stop interception. The final combined run passed all 71 tests: 25 Codex adapter, 26 Claude-project and 20 receipt-helper tests. The historical native Claude probe is separate evidence.

## Why native acceptance is pending

The installed Codex CLI advertises hook support, and the existing user config enables `features.hooks = true`. The project is trusted. However, the user configuration currently trusts only the pre-existing user SessionStart hook. None of these six new project definitions has a trusted hash.

[Official Codex hooks documentation](https://learn.chatgpt.com/docs/hooks) requires review and trust of each exact new or changed non-managed hook definition. Project trust alone does not grant hook trust. No global trust hash was written and no hook-trust bypass was used. A session already running before this configuration was created is not claimed to be protected by it.

To activate the completed configuration, open the Codex CLI at `C:/Users/Joshu/dev/ai-os`, enter `/hooks`, inspect the six entries from `.codex/hooks.json`, and trust them. Then run a fresh native probe: invoke the teaching skill or native karpathy agent, create a tiny code file and attempt to stop before running it. Acceptance requires an actual blocking hook event, then a real execution and a permitted stop. No such native Codex probe is recorded yet.

## Practical scope limits

## Fresh native discovery probe, 2026-10-08

The normal signed-in `codex exec` probe at `2026-10-08T22:42:03Z` exited successfully but did **not** establish hook acceptance. It read the actual activated skill, created `examples/codex-stop-probe/native_probe.py`, and stopped without running the file. No hook state directory was created. This is evidence that this CLI invocation did not invoke the configured project handlers, rather than evidence that the guard passed. Trust/discovery must be resolved before claiming protection.

The untouched native capture, invocation and stderr are stored under [the external probe folder](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-stop-probe). No trust bypass, fabricated trusted hash or alternate API credentials were used. The test was deliberately isolated from teaching acceptance.

The source review also identified a compound-command ordering defect: a single shell call that wrote code and then ran it was incorrectly left pending. The adapter now recognizes provable explicit shell-write-before-runtime ordering; run-before-write and a final subsequent edit remain blocked. Thirty adapter tests pass, including five ordering regressions. Opaque editor/program side effects remain conservatively pending because a single before/after snapshot cannot prove their internal order.

Official tool coverage maps shell commands and unified `exec_command` to the canonical hook name `Bash`; a later `write_stdin` can supply that original command's terminal PostToolUse event. `apply_patch` remains canonical `apply_patch`, with Write/Edit matcher aliases. Nested tools called through code mode receive their own hook decisions. This configuration therefore matches those documented canonical shell/edit events, not the outer `functions.exec` wrapper. Actual installed-runtime payload normalization still requires the trusted native probe. Arbitrary MCP or other file-edit wrappers whose canonical name is not in this matcher are not claimed as covered; use the configured shell/edit paths.

Shell writes outside the project and registered examples cannot be observed unless the shell is editing an explicitly tracked path. Use explicit Write/Edit/apply_patch for those paths. Simultaneous edits by other processes under a scanned root can be attributed to the enclosing tool interval; this is a workflow guard, not a security or authorship boundary. A real execution of an unrelated program satisfies the video's literal “nothing was run afterward” condition but cannot pass the relevant-behavior rule by itself.

The captured raw sources were not changed. This adapter does not send messages, install packages, alter account permissions, approve hook trust, or spend API credits.
