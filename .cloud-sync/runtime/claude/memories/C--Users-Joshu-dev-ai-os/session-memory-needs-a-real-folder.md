---
name: session-memory-needs-a-real-folder
description: Joshua's sessions must open dev/ai-os, not "No folder" — otherwise memory lands in a throwaway scratch dir and is lost.
metadata:
  type: feedback
---

Open `C:\Users\Joshu\dev\ai-os` as the session folder. Do not work from a "No folder" scratch workspace.

**Why:** Memory is stored per project directory. Every "No folder" session gets a fresh date-stamped scratch path, so memory starts empty and is deleted with the session. On 2026-09-07 three prior sessions were found with completely empty memory folders for exactly this reason — nothing had ever been able to accumulate.

**How to apply:** If a session starts with no folder and the work concerns LSAT U, the vault, or anything ongoing, move to `dev/ai-os` with `change_directory` before doing real work. Related: [[ai-os-vault-location]]
