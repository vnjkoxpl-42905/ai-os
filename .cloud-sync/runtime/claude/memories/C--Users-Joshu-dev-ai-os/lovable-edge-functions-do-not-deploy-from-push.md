---
name: lovable-edge-functions-do-not-deploy-from-push
description: "Lovable deploys edge functions from a push eventually, not promptly; prove a deploy with the grader's build marker before trusting a fix"
metadata: 
  node_type: memory
  type: project
  originSessionId: f9e1648e-8435-402f-acdc-5221fda60fbf
  modified: 2026-09-08T04:39:19.380Z
---

On 2026-09-08 a grader fix pushed at 02:53 UTC was not running at 03:25 (Cloud tab: "last updated 6 hours ago"; publishing via deploy_project did not change it). Lovable then deployed it on its own at 04:03 UTC as an ai_update "Deployed latest grade-rrc-section", about an hour later and right after another push. So a push does deploy edge functions, but with no visible receipt and no reliable timing; the vault's "auto-deploy on push" line is true only eventually.

**Why:** For an hour the fix looked shipped and was not, while a student waited on a grade. Guessing cost more than checking.

**How to apply:** After any edge function change, prove the deploy from outside: `grade-rrc-section` returns `build` in its 202 body and an `X-Grader-Build` header (bump `BUILD` on every change). Poll for the marker rather than assuming; if it has not changed after ~20 minutes, ask Joshua to nudge Lovable. Related: [[lsatu-content-lives-in-postgres]].

**Fast path (2026-09-08):** a deploy-only message to Lovable's agent via the Lovable MCP `send_message` (project `53b9a6f2-aba7-4ae4-8dd1-fa5b8aab4d76`) works: "Redeploy grade-rrc-section from the repo as it stands, do not edit code, do not publish." It ran `deploy_edge_functions` only, 0.4 credits, and the new build answered within a minute. There is no Supabase access token on the Windows box, so this is the only deploy route.
