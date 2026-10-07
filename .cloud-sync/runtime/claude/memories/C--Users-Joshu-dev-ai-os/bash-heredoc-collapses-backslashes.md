---
name: bash-heredoc-collapses-backslashes
description: "The Bash tool on this Windows box turns `\\\\` into `\\` inside a quoted heredoc, so inline Python patches containing escaped backslashes silently fail to match; write patch scripts to the scratchpad with the Write tool instead."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2a009d25-131b-44bd-a737-2cfd05ead74f
  modified: 2026-09-12T10:40:26.442Z
---

Inline `python - <<'EOF'` patches that contain `\\n` (to match a literal
backslash-n in a source file) fail with "substring not found" because the tool
layer collapses `\\` to `\` before Python sees it, even with a quoted heredoc.

**Why:** Cost two failed attempts on 2026-09-12 while patching
`system/scripts/transcript-inventory.py`.

**How to apply:** For any inline script that needs a literal backslash, write
the script to the scratchpad with the Write tool and run it by path. Plain
strings without backslashes are fine inline.
