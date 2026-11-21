# Destructive Command Guard evaluation, 2026-10-29

## Result

Not installed. The v0.15.3 native Windows release is present only as an evaluation artifact in this directory. Claude Code 2.1.309 and Codex CLI 0.162.1 were present. Real Claude and Codex hook dispatch was not tested, so direct protocol tests are not evidence of end-to-end enforcement. In particular, the upstream [Codex integration](https://github.com/Dicklesworthstone/destructive_command_guard/blob/v0.15.3/docs/codex-integration.md) documents that Windows Desktop and CLI unified_exec calls can bypass PreToolUse completely and fail open. A hook cannot be treated as a universal deletion guard.

## Evidence

The Windows x64 release ZIP was downloaded from the v0.15.3 GitHub release. Its SHA-256 `2e399907f6854e189abe6cb08c693751211527594e92b202f4d9452e758da109` matched that release's SHA256SUMS. This is a checksum comparison, not independent signature verification. The extracted binary is `release/dcg.exe`.

The synthetic `probe.py` passed JSON to the binary only; it did not execute the named commands. The binary allowed `git status --short`; denied `git reset --hard HEAD~1`; and denied `Remove-Item -Recurse -Force` in a Codex-shaped Bash payload. It output a Codex-shaped JSON denial for the latter two. This proves only direct evaluator behavior. It does not prove desktop dispatch, hook trust, coverage for every tool, or fail-closed behavior on binary failure.

## Unintended side effect and correction

The first synthetic invocation unexpectedly enabled DCG's self-heal and inserted a hook pointing to the evaluation binary into the user's Claude settings. The inserted entry was removed with `undo-probe-hook.py`, which required an exact single match and verified that every other parsed setting was identical across the correction. The hook is no longer present. The source's `src/main.rs` says self-heal is enabled by `general.self_heal_hook`, re-registers in Claude settings, and logs errors without blocking. It must be explicitly controlled in future isolated tests. The probe also created `%APPDATA%/dcg/pending_exceptions.jsonl` and `selfheal-97206f48.lock`; these diagnostic artifacts were retained. No guard binary or hook was installed in the user's runtime directories, and no PATH was altered.

Existing Claude and Codex hooks were identified. Any future installation must preserve them, use a stable binary path and deliberate configuration, and test actual runtime hook dispatch in a disposable target. Upstream docs say the hook can fail open on some paths, and no claim should be made that it governs app connectors, filesystem tools or shell paths it does not receive. User permission is still required for deletion even where the guard does not intercept it.
