# Review log: Reading Center RC Recall

## 2026-10-16 — initial plan

- Host/planner: Codex. Independent plan reviewer: Claude CLI. Builder: Claude via `claude-build` workflow if available. Independent final inspector: Codex only if Claude builds; no commit, push, upload or deploy authorized.
- Scope: implement RC Recall and Cumulative Recall in Reading Center, use the static RC bank, matched demos, per-student append-only attempts/recordings, full source instructions, prepare a no-subscription explainer video.
- Authorization: Joshua answered “yes go” after the requirements grill. No paid service, external subscription, credit-metered generation, remote upload, or publication is authorized.
- Plan: `C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-16-reading-center-rc-recall-plan.md`.
- Source checkout was clean at `c0a8c48cba5cfb2913371e6881c4b73385c9983d` on `feat/reading-center`, 49 commits behind `origin/main`. Work will proceed on local `feat/rc-recall` at the current `origin/main` snapshot; original checkout is retained.
- Confirmed local media state: 7 Decaf examples + 3 Cappuccino examples; source MP4s ~680 MB with M4A sidecars. HyperFrames usage: 63% weekly allowance remaining, spend unknown. HeyGen signed out; offline Kokoro dependencies missing. No paid video call made.
- Review rounds: maximum 5. Build-fix rounds: maximum 2. Final inspection rounds: maximum 2. Review/build diagnostics remain outside the app checkout.

## 2026-10-16 — review round 2 disposition

- Claude returned `REVISE`, confirming F1-F10 from round 1 were addressed and identifying five new consistency defects.
- Updated plan to allow spoken or silent optional RC Recall full-passage recaps while keeping paragraph recalls and confirmations silent; record only spoken recaps and persist the choice.
- Replaced LR-specific “colour” with source-accurate “read, translate and quip”; specified cross-A/B cumulative recap and persisted confirmation scope.
- Kept source mode names inside original lesson footage but mapped them in chapter cards/captions; exclude the unsupported Cappuccino 35 variant and verify edit-boundary caption alignment.
- Clarified local-only source-video derivatives and no authorization for public distribution, upload, or deployment.
- Plan reviewer resume artifact: `C:/Users/Joshu/AppData/Local/Temp/claudex-5bc57_p8/result.json`.

## 2026-10-16 — review round 3 disposition

- Claude returned `REVISE`; it found contradictory recording guidance, missing persistence for RC Recall confirmation scope, and a public-asset merge risk.
- Recording now starts only during each spoken recap, creates one unique object per spoken recap, and saves per-recap `not_recorded` / `pending` / `saved` / `failed` status. Voice is chosen per recap; spoken end-of-passage RC Recall is recorded; silent-only attempts remain valid.
- RC Recall confirmation scope is chosen before the run and saved, with source default all text read so far; an alternate current-sub-passage-only option is retained. Cumulative recall scope is A+B together on Passage B.
- All lesson derivatives are outside Git and public assets regardless of size; media is hidden without a configured local media base.
- Review resume artifact: `C:/Users/Joshu/AppData/Local/Temp/claudex-zv792o8j/result.json`.
