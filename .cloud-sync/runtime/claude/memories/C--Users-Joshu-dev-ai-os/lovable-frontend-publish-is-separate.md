---
name: lovable-frontend-publish-is-separate
description: A push builds a Lovable preview but never reaches lsatprep.study; publish with deploy_project, wait for the sync, and prove it from the bundle.
metadata:
  type: project
---

Pushing to `main` makes Lovable build the commit — its project record shows a
preview screenshot tagged with the commit sha within minutes — but the published
site at lsatprep.study keeps serving the previous bundle until something calls
`deploy_project` (Lovable MCP, `project_id 53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`,
name `lsatu`). Confirmed 2026-09-08: a fix sat built-but-unpublished for 20
minutes with no error anywhere.

**The sync lags the push.** `deploy_project` publishes whatever Lovable has
ingested, not what is on origin. On 2026-09-09 a deploy fired seconds after a
successful push and shipped the *previous* commit; `get_project` showed
`latest_commit_sha` catching up about three minutes later, and a second deploy
was needed. There is no error and no warning — the deploy reports `pending` and
succeeds, just on the wrong commit.

**Why:** build, sync and publish are three separate steps, and none of them
reports that the others have not happened. A green push reads as shipped.

**How to apply:** before calling `deploy_project`, call `get_project` and check
`latest_commit_sha` equals your HEAD; if it does not, wait and re-check. After
deploying, prove it from the bundle: pick a string **the commit alone**
introduces — not a class name an earlier deploy already shipped, which is how a
stale bundle passed a check on 2026-09-09 — then fetch `https://lsatprep.study/`,
read the `index-*` asset hash out of it, and grep the asset for the marker.
Allow several minutes; the hash changing is the signal a publish landed at all.
Note `deploy_project` ships every unpublished commit on main, not just yours.

Same trap, different half: [[lovable-edge-functions-do-not-deploy-from-push]].
Related: [[push-only-your-own-commits]].

**Standing permission (Joshua, 2026-09-26):** publishing the frontend with the
free `deploy_project` is pre-authorized, so he does not need to press Publish
himself. It applies only to that free path. Anything that spends or might spend
Lovable credits still needs his confirmation right before it runs
([[minimize-lovable-credits]]). If he opens Lovable after one of these publishes,
it will show nothing to publish, and that is expected.
