---
name: branch-per-session-in-lsatu
description: "Concurrent agent sessions each work on their own branch off main in projects/lsatu and open a PR; never commit straight to main."
metadata:
  type: feedback
---

In `projects/lsatu`, when more than one agent session may be running, work on a named
branch off `main` (`git checkout -b <topic>`) and open a PR. Do not commit to `main`.

**Why:** Joshua's call, 2026-09-09, after two sessions committing to `main` in the same
working tree pushed each other's work. One session's push carried the other's commit; the
other's push carried this session's plus two untested commits, which then went to
production because a Lovable deploy ships `main`. Every commit is authored "Joshua
Fisseha", so authorship cannot separate the sessions. He chose branch-per-session over
worktrees.

**How to apply:** branch before the first edit, commit with explicit paths (never `git
add -A`, the tree holds other sessions' uncommitted files), push the branch, open a PR
with `gh pr create --base main`. Check `git branch --show-current` before each commit: the
working tree is still shared, so a branch protects your commits and not the other
session's, and a peer that believes it is on `main` will commit onto your branch. If both
sessions will run for a while, a `git worktree` is the fuller fix and is worth raising.

Related: [[push-only-your-own-commits]], [[lovable-frontend-publish-is-separate]].
