---
name: assign-lsatu-work
description: Operate LSAT U headlessly. Assign guided drills and daily schedules through a mapped catalog and verified batch MCP; assign activities or timed sections, read student progress, manage access and Classroom work, and handle platform messages.
---

## Current AI OS execution contract

Classify the request first: inspection and recommendations do not assign work. Only an explicit assignment request uses the current assignment executor. Resolve the supported transport, verify exact student and assignment, then read back the live result.

# Assign LSAT U work

For guided-drill selection or schedules, follow [the guided-drill workflow](references/guided-drill-workflow.md). Use the mapped catalog, one live preview and one batch MCP assignment. This local branch contains its authorization and verification rules; do not load the global reference for a routine guided schedule.

This is a pointer. The full skill lives in ONE place:

    C:\Users\Joshu\.agents\skills\assign-lsatu-work\SKILL.md
    (identical to C:\Users\Joshu\.claude\skills\assign-lsatu-work\SKILL.md, which Claude uses)

For other LSAT U operations, read that file in full and follow it exactly.
Do not copy its contents here; this file must stay a pointer so the two runtimes never drift.

The short version, in case the file cannot be read:

- Every LSAT U operation runs headless through ONE command, from the vault root, with bash:
  `bash system/scripts/lsatu <command> ...`
  Examples: `bash system/scripts/lsatu status "Celia"`,
  `bash system/scripts/lsatu assign --student "Celia" --section PT156.S2 --due 2026-09-30`.
- No browser, no Chrome, no Lovable for routine content or assignments. Use
  `lsat-u-platform-actions` for a complete interactive Classroom lesson: its
  local MCP posts the HTML directly and verifies the saved copy headlessly.
  This skill handles other assignments and student operations.
- Reads never need permission. One named student assign / message: run it, then report.
  Confirm first: 3+ students, revoke/archive/unarchive/unassign/all-off, unsend.
- Never pass a multi-line argument. On Windows a newline drops `--dry-run` and sends for real
  (this happened on 2026-09-23). The wrapper refuses it; do not work around it.

Guided-drill catalog and MCP details live in the [guided workflow reference](references/guided-drill-workflow.md), including the authored-content exception and immediate fallback when new MCP tools have not appeared in a chat yet.
