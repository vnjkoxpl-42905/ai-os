# Protocol: Seamless Push to Main

This document defines the canonical procedure for pushing changes to `origin/main` in `lsatu` (or any sub-project) when Joshua commands "push to main."

---

## 1. Core Principles & Constraints

1. **Push only this session's work:** Never push commits or uncommitted files created by another session, another branch, or automated tools.
2. **Explicit staging only:** Never use `git add -A` or `git add .`. The repository often has active concurrent edits or experimental scripts. Stage only the exact files modified for the requested task.
3. **Avoid branch lockouts:** Local worktrees may have `main` checked out (e.g. `fatal: cannot force update the branch 'main' used by worktree...`). Push directly to the remote tracking branch via `git push origin HEAD:main` instead of attempting local branch switches.
4. **Targeted validation:** Run `npx tsc --noEmit` and targeted vitest suites for modified code. Do not run full production builds unless packaging or bundler configs were touched, because bundlers can mutate generated files (such as `supabase/functions/mcp/index.ts`).
5. **No em-dashes:** Never use em-dashes in commit messages, documentation, or responses.

---

## 2. The 5-Step Execution Path

When Joshua says "push to main", execute these steps in sequence:

### Step 1: Targeted Verification
Verify syntax, types, and regressions for the touched scope:
```powershell
# In the active repository or worktree:
npx tsc --noEmit
npx vitest run <target_test_file>.test.tsx
```
Ensure zero type errors and clean test runs before proceeding.

### Step 2: Explicit Staging
Stage only the exact files authorized and modified during the session:
```powershell
git add path/to/file1.tsx path/to/file2.css
```
Verify staged contents:
```powershell
git diff --cached --stat
```
Confirm no unexpected or generated files are included in the staged index.

### Step 3: Atomic Commit
Create a concise, imperative commit message explaining the change:
```powershell
git commit -m "Descriptive action summary without em-dashes"
```

### Step 4: Verification of Outgoing Commits & Direct Push
Ensure only this session's commit(s) will be sent upstream:
```powershell
git log --oneline origin/main..HEAD
```
If the commit list matches exactly what was authored this session:
```powershell
git push origin HEAD:main
```
This pushes the current commit directly to `origin/main` without conflicting with local worktrees that may have `main` checked out.

### Step 5: Post-Push Sync
Synchronize the local remote tracking reference:
```powershell
git fetch origin main
git status
```
Confirm the working tree is clean and aligned with `origin/main`.

---

## 3. Handling Special Scenarios

### Scenario A: Working inside a dirty root repository (`projects/lsatu`)
If the session occurred in `projects/lsatu` while other files were dirty:
1. Stage only the session's files: `git add <file1> <file2>`.
2. Commit on the local feature branch.
3. Check `git log origin/main..HEAD`.
4. If the branch has prior unrelated commits, cherry-pick or apply the patch to a clean worktree branched from `origin/main`, then push.
5. If the commit is directly on top of `origin/main`, push directly with `git push origin HEAD:main`.

### Scenario B: Generated file mutations during test or build
If running a script or build mutates an unintended file (such as `mcp/index.ts`):
```powershell
git checkout -- <unintended_file>
```
Discard the artifact mutation before staging and committing.
