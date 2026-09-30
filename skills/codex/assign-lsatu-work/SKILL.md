---
name: assign-lsatu-work
description: Use whenever Joshua wants to do anything on LSAT U headlessly, with no browser. That covers assigning an Activity, a guided drill, a homework set, or a timed PT section to one or many students ("assign this to Celia", "give Lydia the Negation Station", "put PT156.S2 on Avneet due Friday", "assign RRC to Celia, Lydia and Dakota"). It covers messaging a student from his admin account ("send Dakota a message", "tell Celia to start with PT105.S2"). It covers reading how students are doing ("how is Celia doing", "what does Lydia have", "who is overdue", "who has gone quiet", "Celia's weakest question types", "Avneet's last sections"). It covers accounts and upkeep: new signups ("who signed up", "did anyone new join"), access ("give Venusa access", "turn on drills for X", "what can X see"), archiving, moving a due date, unassigning, booking passes ("how many sessions does Sandra have left"), notifications, and reading or marking messages ("who messaged me", "show my thread with Celia"). It is the one place for any operation on the LSAT U platform, and none of it uses Lovable.
---

# assign-lsatu-work (pointer)

This is a pointer. The full skill lives in ONE place:

    C:\Users\Joshu\.agents\skills\assign-lsatu-work\SKILL.md
    (identical to C:\Users\Joshu\.claude\skills\assign-lsatu-work\SKILL.md, which Claude uses)

**Read that file in full before every LSAT U operation, and follow it exactly.**
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
