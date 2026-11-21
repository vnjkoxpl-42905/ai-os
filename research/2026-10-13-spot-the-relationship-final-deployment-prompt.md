# Spot the Relationship deployment prompt

Approved by Joshua on 2026-10-14 in this chat. The prepared changes were merged with current main into 9e8dd6df7385863f54eb82a05eb26557c06e5fe3 before submission; the actual sent text and accepted message ID will be recorded separately below.

Sent once in standard build mode, Max off. Accepted message umsg_01m4ygdssfe5psdrxfn49bjv7p, main thread. Completion and verification pending.

Completed on 2026-10-14 for 5.5 credits. Managed migration applied, grading enabled for the Spot activity only, activity-coach deployed with submitted fingerprint 248556b893cd0bc144b6b36496371b97b869c57e25ab94acde511c2e6af352b2. Lovable removed only the explicit transaction wrappers from migration 0030 for its managed migration runner, commit be3f0a78, resulting main e2b1236e. Lovable made zero real provider calls because its preview authentication was blocked. The parent subsequently used the existing authenticated admin login and ran the six authorized preview grading checks: all passed. Exact verdict/feedback evidence is 2026-10-14-spot-the-relationship-live-grades.json. No third prompt was sent.

## Exact submitted text

```text
The reviewed repair is already on main at 9e8dd6df7385863f54eb82a05eb26557c06e5fe3. Deploy it rather than rebuilding it: apply drizzle/migrations/0030_activity_ai_grader_revision.sql through the managed database migration route, deploy activity-coach through Lovable Cloud, and retain its included frontend revision-conflict recovery. Read docs/implementation-plans/2026-10-13-relationship-backend-draft.md for the passed checks. Keep google/gemini-3.1-flash-lite in both grader and proxy, the 220-token output cap, free exact-key matching and cache reuse.

After verifying the activity slug, atomically restrict activity_ai_configuration_v1.allowed_activity_ids to Spot the Relationship activity 12251bd3-d260-4108-bc35-bcf478e483e6 and set enabled=true. Preserve budgets, counters, unrelated settings, completed assignments and student responses. Do not assign work or send notifications; I handle Gianna's assignment separately.

Verify the managed migration, exact deployed function fingerprint, enabled flag and allowlist. Run the prepared mock/SQL regression tests. Use at most six real provider grading calls in an isolated admin preview: (1) item 1 type-only conditional -> partial with a nonrevealing hint; (2) item 5 comparative, caused -> partial for mislabeled indicator; (3) item 25 comparative, stronger -> partial for missing than; (4) item 1 conditional, only if is not the indicator -> must not be correct; (5) item 48 a valid prose paraphrase pairing conditional/only if, comparison/more ... than, causal/because or produces -> correct; (6) item 1 second attempt after test 1, using a non-exact but valid explanatory answer -> final explanation. Confirm exact-key and cache paths avoid provider calls, first hints do not leak missing answers, and revision recovery keeps a durable saved request. Report actual verdicts/feedback, provider-call count, deployment fingerprint, config and any blocker. Use existing approved admin access; do not create accounts, change roles or obtain credentials in chat. No extra paid prompts or model upgrades. Leave frontend production publishing to me after verification.
```

Use after fresh approval for one paid Lovable prompt and up to six paid live grading checks. Before sending, make commits 7d24ff42a5c08c0d18ae7a2fd6e35b832dd30fb5 and 4b56a99d available to Lovable through the repository, safely reconcile the migration number against current main, and preserve concurrent work. Local branch: codex/relationship-backend-draft in C:\Users\Joshu\dev\ai-os-projects\lsatu-str-backend. Review note: docs/implementation-plans/2026-10-13-relationship-backend-draft.md.

```text
Integrate the two prepared relationship-backend-draft commits, preserving current main and completed student snapshots. Apply the additive grader-revision/allowlist migration and deploy activity-coach through Lovable Cloud, together with the included durable frontend revision-conflict recovery. Keep google/gemini-3.1-flash-lite, the 220-token output cap, free exact-key matching and cached results.

Enable activity_ai_configuration_v1 only after restricting allowed_activity_ids to Spot the Relationship activity 12251bd3-d260-4108-bc35-bcf478e483e6, freshly verified by its slug. Preserve existing budgets and unrelated settings. Do not rewrite completed assignments, send notifications, switch models, reset spending, or issue a second agent prompt.

Run the prepared tests and managed deployment/config readback. Use at most six real AI grading requests in an isolated admin preview to check type-only partial, mislabeled indicator, missing half of a split comparison, contradictory prose, item 48 with a valid paraphrase, and second-attempt explanation. Verify first hints do not reveal answers, exact-key answers and cache replays make no provider call, and reload/revision recovery retains its saved identity. Report each verdict, feedback, real provider-call count, deployment fingerprint, enabled scope and any blocker. Leave frontend publishing to me after these checks.
```
