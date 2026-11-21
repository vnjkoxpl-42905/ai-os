---
name: claude-review
description: Codex-to-Claude review workflow. Claude Code independently reviews an existing plan while Codex coordinates a bounded revision loop.
---

# Claude reviews, Codex revises

Invoke this Codex-side skill as `claude-review`. This Codex copy selects Claude as the independent reviewer. The Claude installation retains Codex as reviewer.

Load `../claudex-loop/SKILL.md` and use `mode=review`, `host=codex`. Preserve PLAN_FILE, LOG_FILE, MAX_ROUNDS or rounds, and explicit model/effort choices. Do not restart an interview when the supplied plan is adequate. This invocation authorizes review, not implementation.

Read the sibling runtime reference and resolve its runner from the installed sibling skill. Use `review --host codex` with the actual resolved plan path. Codex evaluates Claude's findings and records dispositions before any further review rounds. Follow the shared loop's resume, approval, hash validation, failure, and round-limit rules. A failed, empty, malformed, or blocked result is not approval.

Any separately authorized implementation follows the shared build and inspection phases. Plan review does not replace independent inspection of the final changes.
