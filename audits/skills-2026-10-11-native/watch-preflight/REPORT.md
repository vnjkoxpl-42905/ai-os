# Watch startup now checks free tools without configuring paid services

On 2026-10-11, the native Claude startup probe exposed an older SessionStart payload that suggested adding paid-provider keys to `~/.config/watch/.env`. Its companion setup script also installed tools on macOS and scaffolded that credential file by default. Both behaviors contradicted the repaired free default and the AI OS central `.env` policy.

Replaced the owned setup payload with a stdlib read-only preflight. Default execution checks FFmpeg, ffprobe, and yt-dlp on PATH. It does not inspect credentials, install tools, create configuration, change permissions, or call a provider. An explicit `--paid-provider groq|openai` checks only the selected credential's presence in the process environment or the root `.env` found from paired AGENTS.md and CLAUDE.md instructions. That flag does not authorize a paid request.

SessionStart delegates to this same preflight with `--hook`. It stays silent when the free tools are present. Missing tools produce a PATH/install-discovery message without performing an install. Existing hook definitions quote the plugin path, and missing referenced hook scripts were added to the existing Claude/Gemini payloads. No new native activation or trust configuration was created.

Changed-file inventory, original byte backups, and before/after SHA256 values are in [receipts.json](receipts.json). Frozen vendor snapshots and unrelated payloads were preserved. Six existing owned roots were repaired; project .agents/.claude watch activations were absent and were not created.

## Executed checks

- Guarded repair helper through run_gate: receipt `82b21d18ad194a3ead52adea9e8414f2`.
- Four preflight tests through run_gate, tracing the actual edited canonical setup.py: receipt `ac1c380d395946cabad03aba3a781bb8`.
- Tests demonstrate absent-tool failure and corrected PATH discovery, free-ready without credential reads, explicit provider selection with a temporary fake central credential, no filesystem changes, matching owned setup bytes, valid quoted hook definitions, and actual Bash hook execution.
- Actual Bash SessionStart command: exit 0, empty stdout.
- Actual `python skills/codex/watch/scripts/setup.py --json`: `status=ready`, `mode=native_captions`, no missing binaries, no paid provider.
- Existing watch boundary regression suite: 9 tests passed. No provider/network requests made.

## Native counterexample and final correction

The first repair omitted the existing global `C:/Users/Joshu/.claude/skills/watch` payload. A fresh native run still emitted the obsolete key-scaffolding message. That was a real coverage mistake; the earlier Bash check alone did not establish native acceptance. Corrected the exact three global Claude payload files and added this root to the repair and parity-test lists. Original bytes and hashes are in `claude-global-receipts.json`; repair gate receipt `3b989fc0ee2d442d9ad5a4c77c319953`.

A new independent no-prompt native Claude print run now emitted exactly two SessionStart hook responses, both exit 0/success with empty output, stdout, and stderr. Session ID: `19851b08-96b5-48dc-b5e8-72989cdc282f`. Process exit 1 is the expected `Input must be provided` rejection, so no model prompt was submitted. Actual output is preserved in `claude-native-after.jsonl` and `claude-native-after.stderr.txt`; verifier receipt `7424e188dc294052a64cdd249852b702`. This verifies the already-registered SessionStart path, not additional newly trusted definitions.

Also corrected the related paid-preflight/loader mismatch: whisper.py searched only cwd `.env`, while setup resolved the central paired-instruction root. Seven owned whisper payloads now use the same ancestor resolution. The nested-cwd test proves both find only the central selected-provider fixture and ignore a nested credential file. No real key is printed and no provider is called. Hashes/backups: `whisper-root-receipts.json`; repair receipt `acc43e56abce41659160e6107058625b`. Final five-test suite traced both actual setup.py and whisper.py: `9369bf760e9a4fbb94099d8b6cef0f0c`. The nine existing boundary regressions were rerun after this change and passed.

## Seven-rule evidence

Method references: [hot](../../../wiki/karpathy/hot.md), [rules](../../../wiki/karpathy/rules.md).

1. Mechanism reconstruction: pass. One PATH-only preflight is shared by CLI and startup shell hook.
2. Small baseline: pass. Stdlib setup plus a shell delegate; no dependency or new credential store.
3. Prediction/run/comparison: pass. Predicted silent free-ready and explicit missing-tool failure; actual hook and isolated tests matched.
4. Counterexample/fix: pass. Missing-tool branch fails, mocked corrected discovery reruns successfully. Selected missing provider does not fall back to another key.
5. Relevant execution: pass. Gate traced the edited setup file, and Bash executed the actual hook.
6. Explicit assumptions: pass. Tool discovery follows inherited PATH; paid key presence is not spending authorization; native acceptance remains separate.
7. Justified simplicity: pass. Removed installer/wizard state rather than creating a competing setup system.
