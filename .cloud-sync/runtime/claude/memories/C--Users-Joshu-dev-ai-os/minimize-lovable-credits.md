---
name: minimize-lovable-credits
description: Joshua wants Lovable credit use kept to a minimum (said 2026-09-24); use free paths first and batch unavoidable Lovable work into one short message
metadata:
  node_type: memory
  type: feedback
  originSessionId: 01f6c6ab-d788-4c39-a7f0-1a790cf99b21
  modified: 2026-09-25T01:13:16.715Z
---

Keep Lovable credit spend minimal. Stated 2026-09-24, after the workspace ran out mid-deploy.

**Why:** credits ran out halfway through the access-tiers rollout; he topped up and asked to conserve from now on.

**How to apply:**
- Free paths first: migrations and data fixes via `query_database` (direct SQL, no agent), frontend publish via `deploy_project`, code via git push/PR.
- The only thing that truly needs the Lovable agent is deploying Edge Functions. Batch every pending function into ONE short, backend-only message ("deploy X and Y exactly as on main, edit no code"), never a exploratory or multi-turn chat.
- Never use the Lovable agent to read code, verify, or investigate; do that locally or with `query_database`.
- Still confirm with Joshua immediately before any credit-spending message (see [[lovable-frontend-publish-is-separate]], [[lovable-edge-functions-do-not-deploy-from-push]]).
