# Hook inventory and repair, 2026-11-14

This inventory covers explicit global and AI OS settings inspected on this machine. Plugin-provided or other project hooks were not exhaustively audited.

| Owner and event | Purpose and command | Interpreter and target | State writes | Evidence |
|---|---|---|---|---|
| Codex global, SessionStart | Herdr session report: `C:/Users/Joshu/.codex/herdr-agent-state.ps1` session | Windows PowerShell; script present | Calls Herdr's pane reporting command only inside a Herdr session with valid payload | Exits 0 with Herdr variables absent; native startup remains unverified |
| Claude global, SessionStart (startup, resume, clear, compact, fork) | Herdr session report: `C:/Users/Joshu/.claude/hooks/herdr-agent-state.ps1` session | Windows PowerShell; script present | Calls Herdr's pane reporting command only inside a Herdr session with valid payload | Exits 0 with Herdr variables absent; native startup remains unverified |
| AI OS Codex, UserPromptSubmit, PreToolUse, PostToolUse, Stop, and karpathy-matched SubagentStart/SubagentStop | Scoped execution gate: `C:/Users/Joshu/dev/ai-os-projects/karpathy-method-tools/codex_stop.py` | PowerShell invokes Python 3.12; both targets present | Per-session event state and lock under `karpathy-method-tools/runtime/codex-hooks` | Three direct unit cases passed: scoped edit blocks, ordinary task unaffected, and execution permits Stop. A real scoped native session is unverified. |

AI OS Claude settings files inspected have no explicit hook entries. No claim is made about inherited plugin hooks.

## Orca repair and rollback

Nine global Codex registrations referenced the missing `C:/Users/Joshu/.orca/agent-hooks/codex-hook.cmd`. They were removed from `C:/Users/Joshu/.codex/hooks.json`; the Herdr registration remains. The original exact bytes were backed up and hash verified before editing:

- Backup: `C:/Users/Joshu/.codex/visualizations/2026/11/15/01a1dcca-a2aa-7a70-b2e2-968b34f0ae6e/workspace-redesign-settings-backups/codex-hooks-20261115T012736948399Z.json`
- Original SHA-256: `78d8875e46d3a77ad7522f8b1c104cb50cacaba08577cd017cd8784ee718e657`
- Repaired SHA-256: `b94479987a385329db7e14bacd3c08d1a21fbb34ea5b131916d5dbef2379c2c9`
- Repair script: `system/scripts/repair-orphan-orca-hooks.py`. It refuses to run if the target exists, the expected nine entries are absent, or configuration changes during preparation.

Rollback: after checking for later changes and preserving the current file, copy the verified backup over the global hook configuration. Restoring it also restores the nine broken registrations. No trust state was edited. Review remaining hooks in the supported Codex UI; native fresh Codex and Claude sessions and repeat-approval behavior are still unverified.
