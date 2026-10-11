---
name: resolving-merge-conflicts
description: "Use when you need to resolve an in-progress git merge/rebase conflict."
---

1. **See the current state** of the merge/rebase. Record `git status --short`, unmerged paths and any pre-existing staged/unstaged/untracked work. Preserve that baseline. Check git history and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. Do **not** invent new behaviour. Do not abort, reset or discard work without explicit authorization. Leave incompatible conflicts visible when the goal cannot adjudicate them.

4. Discover the project's **automated checks** and run them, typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage only resolved conflict paths after inspecting their full diff; never `git add .` or absorb unrelated baseline edits. Inspect the staged diff before continuing. Finish/commit only when the task authorizes completing this merge/rebase; otherwise leave the resolved state reviewable and report the exact remaining command. Rebase continuation remains bounded to the authorized operation.
