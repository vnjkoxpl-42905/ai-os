---
name: push-only-your-own-commits
description: "Never push commits this session did not make; leave another session's or Lovable's unpushed work alone."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 810e4352-f17a-4f97-96c4-7e4935eb07bb
  modified: 2026-09-09T09:43:59.339Z
---

Push only the commits this chat made itself. If `git log origin/main..HEAD` contains
commits authored by another Claude session, another chat, or a Lovable sync, do not push
them. Stick to your own work, say what you are leaving behind, and stop, unless Joshua
asks you to push the rest.

**Why:** several sessions and Lovable write to `main` in the same repo at the same time.
Pushing a commit whose author has not chosen to publish it takes that decision away from
them, and on this project a push is the first half of a deploy, so it can carry
half-finished work toward production. Set on 2026-09-09 after this session ran
`.claude/safe-push.sh` and the push went out as `e1b2507..5fd1074`, carrying another
session's `70056d3` along with its own commit.

**How to apply:** before `bash .claude/safe-push.sh`, run `git log --oneline
origin/main..HEAD` and confirm every listed commit is one you wrote this session. If any
is not, do not push. This compounds with the existing rule never to `git add -A` in this
repo: a broad add sweeps up other people's in-flight edits, and a broad push then
publishes them. That already happened in reverse here, when a concurrent session's
`git add` swept this session's uncommitted motion work into its own commit.

Related: [[lovable-frontend-publish-is-separate]], [[lsatu-content-lives-in-postgres]].
