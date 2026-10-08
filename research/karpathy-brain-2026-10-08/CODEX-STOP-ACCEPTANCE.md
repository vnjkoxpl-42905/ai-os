# Codex Stop hooks are enabled and natively verified

Verified 2026-10-08. Joshua authorized enabling the hooks and selected Codex in place of the video's Claude runtime. The original [Prompt 5](../karpathy-video-2026-10-08/verbatim/prompt-05.txt) remains unchanged.

## The native stop actually blocked and recovered

Interactive Codex thread `01a11db5-0a7d-7dc0-8fd1-56d0de500279`, scoped turn `01a11db7-b1f8-7312-b3e8-96f68230681d`, read the real activated skill and wrote a new Python probe. Its first final answer deliberately attempted to stop without execution.

- At **2026-10-08T22:52:52.555Z**, a native **HookPrompt** event, not agent prose, recorded `hookRunId=stop:6:C:\Users\Joshu\dev\ai-os\.codex\hooks.json` and exactly `Karpathy rule, run it before you say it works.`
- At **2026-10-08T22:52:59.840Z**, the subsequent Python execution produced `CODEX_NATIVE_STOP_PROBE_OK`, exit **0**.
- At **2026-10-08T22:53:08.774Z**, the native task completed. The scoped hook state retained the code edit and real execution with `pending_run=false`.
- A new unrelated turn `01a11db8-b116-72b3-8540-d2fd5a9f2417` wrote ordinary code without execution. It completed at **2026-10-08T22:53:45.702Z** with **no HookPrompt**. Its state correctly had `scope=false` and `pending_run=true`, so the unrelated edit did not trigger the guard.

[Preserved native event evidence](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/examples/codex-stop-probe/native-acceptance-events.jsonl) contains the real command outputs, blocking event and completion records. The original rollout remains in the native Codex session store. These isolated tests establish main Stop enforcement and unrelated-turn acceptance, not teaching quality or native custom-agent discovery. Karpathy child SubagentStop is configured and unit-tested but was not separately exercised live.

## Activation uses reviewed definitions

The project now has `.codex/config.toml` enabling hooks and adjacent `.codex/hooks.json` with six events: UserPromptSubmit, SubagentStart, PreToolUse, PostToolUse, Stop and SubagentStop. All six current definitions were inspected and enabled as **Trusted** through the native Codex `/hooks` interface. No trusted hashes were fabricated and no trust bypass was used.

The original bare quoted Windows executable pair failed when launched through the runtime's PowerShell shell. The handlers now explicitly invoke `powershell.exe -NoProfile -NonInteractive -Command` with PowerShell's `&` call operator for the installed Python executable and [Codex adapter](C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/codex_stop.py). A supported fresh `--no-daemon` interactive session exercised the current trusted definitions. Two earlier `codex exec` captures and an earlier interactive failure remain preserved; their absence of interception was not presented as success. Their failure alone does not certify that current noninteractive execution is protected.

## The contract matches the source

- Actual project skill invocation/read or native karpathy subagent use scopes the turn. Parent and child state are tracked separately.
- Real code changes set pending execution. A later completed runtime clears it; help, version, install and read-only commands do not. Later edits invalidate the prior run. Asynchronous starts require terminal completion.
- A failed real execution counts as ran and must be reported honestly. Execution relevance and correctness remain part of the seven-rule grade.
- Scoped pending code blocks with the video's exact message. Continuation preserves the edit. A new ordinary turn resets scope and is left alone, as natively verified.
- Explicit compound shell **write then run** is allowed; **run then write** and a final subsequent code write remain pending. Runtime output redirection to a log is allowed; code-file redirection remains conservative. Quote-aware attached redirection is recognized inside Bash/sh wrappers while PowerShell argument syntax and quoted greater-than characters are preserved. Opaque program side effects cannot be ordered from a single snapshot and require a separate run.

## Tests and limits remain explicit

**82 combined tests pass:** 36 Codex adapter tests, 26 historical Claude-project tests and 20 receipt-helper tests. Eleven new Codex regressions cover compound ordering, opaque mutations and output redirection. The native isolated test preceded the final output-redirection refinements; those additional branches have local regression evidence.

Snapshots observe project code and registered external examples. Explicit edit/patch paths also cover code outside those roots. Raw material, credentials/runtime folders, dependencies and symlink directories are excluded. Arbitrary MCP file-edit wrappers whose canonical tool name is absent from the matcher are not certified. Shell edits outside watched roots require explicit tracked edit paths. Concurrent external writers can affect snapshots; this is a workflow guard, not a security or authorship boundary. Running an unrelated program meets the video's literal run condition but cannot satisfy the relevant-behavior teaching grade.

The source's Claude interface was translated to Codex with Joshua's authorization. The exact original message and scoped behavior are retained. All 1,560 preserved source files remain unchanged. No new API credential or account permission was used. [Official Codex hooks documentation](https://learn.chatgpt.com/docs/hooks) describes definition review/trust and native events.
