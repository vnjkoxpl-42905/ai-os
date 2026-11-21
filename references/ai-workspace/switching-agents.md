# Switch between Claude Code and Codex

A checkpoint is a shared task record, not a copy of a native conversation. Start at [Start Here](Start-Here.md), open the task, and read its linked plan. A chat-only session handoff remains chat-only; this persistent checkpoint is a separate operation.

## Before leaving the outgoing agent

1. Stop writing in the checkout. Record the goal, status, repository and actual checkout, branch and full HEAD, active writer, native chat IDs, artifacts, accepted decisions, checks and their limits, unresolved issues, next action and timestamp with timezone. Do not include secrets or full transcripts.
2. Verify the branch and HEAD and note relevant staged, unstaged and untracked work without modifying it. If a check fails, say unknown. Preserve other people's edits. Save the checkpoint beside the task plan and link it from Start Here.
3. Set the checkpoint field `- **Active writer:** Yielded` only when the outgoing writer has stopped. Save using a compare-and-swap check: re-read and compare the file to the version you started from before replacing it; if it changed, stop and reconcile. These records do not enforce locks.

## Start the incoming agent

Open the same project and tell the incoming agent to read the checkpoint and plan. Ask it to verify the checkout exists, compare its current branch and HEAD, inspect relevant dirty and untracked work, and name the goal, accepted decisions, latest checks, limitations and next action before editing. A changed HEAD, changed checkpoint, missing checkout or unyielded writer is a visible discrepancy, not permission to overwrite. Investigate it and update the record before taking ownership. Two reviewers may read concurrently. Only one writer uses a checkout; parallel implementation needs separately assigned worktrees.

For the pilot record format, run `python -B system/scripts/check-workspace-checkpoint.py` from AI OS. It checks the recorded checkout, branch, full HEAD and explicit yielded status, and fails visibly on a mismatch. An optional checkpoint path accepts another record in the same format. This is not a lock and it does not inspect dirty files or prove the other writer stopped.

From the actual checkout, these commands provide evidence:

```powershell
git branch --show-current
git rev-parse HEAD
git -c core.fsmonitor=false status --short
```

If Git cannot inspect the checkout, report the error and stop before writing there. Native chats stay in their own applications; IDs are pointers, not synchronized conversations. Never use a chat's idle state as proof of completion.

## Pilot and verification

The pilot is [workspace redesign](../../brainstorms/2026-11-14-workspace-redesign-checkpoint.md). The [plan](../../brainstorms/2026-11-14-claude-codex-workspace-redesign.md) records whether real cross-agent handoffs, restarts and stale-checkpoint tests succeeded. A document alone does not prove a handoff.
