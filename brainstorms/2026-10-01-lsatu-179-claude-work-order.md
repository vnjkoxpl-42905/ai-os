# Independent study tools implementation for ticket 179

SPEC_FILE: C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-01-lsatu-179-claude-work-order.md
BUILD_REPO: C:/Users/Joshu/dev/lsatu-study-tools-179
BASE: 4474d9f9bdc68036983873f119e044137ab359c1
LOG_FILE: C:/Users/Joshu/dev/ai-os/research/2026-10-01-lsatu-179-claude-build
PROOF_CMD: npx vitest run src/lib/questionStudyTools.test.ts
MAX_FIX_ROUNDS: 2
MODEL: claude-opus-5-5
EFFORT: low
Approval status: explicitly requested standalone work order; unreviewed-spec. Independent Codex final inspection required.

Joshua authorized a substantial independent implementation chunk, explicitly selected Claude Opus 5.5 low, and wants the original audit plan advanced. Implement the following frontend slice of GitHub ticket 179. This is not authority to close the entire ticket.

## Ownership and boundaries

You are not alone in the codebase. Work ONLY in BUILD_REPO, the clean isolated worktree. Preserve other agents' changes. Read its AGENTS.md, CLAUDE.md, directory instructions and relevant domain context first. Old Mac paths in instructions are stale here. The vault is C:/Users/Joshu/dev/ai-os; teaching copy guidance is wiki/teaching-voice.md.

Own new questionStudyTools library/hook/tests plus necessary integration in src/pages/Drill.tsx, src/hooks/useQuestionHighlights.ts, src/components/drill/official/OfficialDrillToolbar.tsx, src/components/drill/official/OfficialQuestionPane.tsx and src/features/rc/pages/RcPlayer.tsx. Narrow existing RC components can be extended as needed. Record every changed file and deviations. Host will not edit these files during your build.

Do not change timed account writers, PracticeTestRun/TimedPracticeTestRun, attempt saving, Review episode writers, question-bank content, AI/Edge Functions, schema/policies, generated types, MCP code, package manifests, instruction files, credentials or vault ledgers. No external writes, paid AI/Lovable calls, notifications, push, publication, commits, or deletion. Dependency junction is supplied; do not install/update dependencies or modify its target. No permission bypass. Normal configured Claude acceptEdits applies; report denied operations rather than weakening permissions.

## Deliver the coherent study-aids slice

1. Add a typed LR/RC bookmark independent of wrong answers, flags and Review. Bind identity to the canonical question and source family, and isolate persisted state by signed-in actor. Never persist under a shared anonymous bucket. Teacher practice aids must not overwrite a selected student's records. Avoid inventing account-sync claims if using local device persistence. Loading or toggling bookmark must never write an attempt or Review task or change diagnostic accuracy.
2. Integrate an accessible bookmark toggle on ordinary LR/RC practice canvases. Provide a useful way to see/open bookmarked questions using existing source navigation where available, or clearly limit retrieval to supported source destinations; never add a dead control. Resolve the exact question rather than confusing adaptive currentQuestion with the queue index.
3. Persist LR text highlights and answer elimination separately from chosen answers, keyed by actor and canonical question. Restore after question navigation and reload. RC already persists its highlight annotations through useRcHighlights/rcProgress: preserve that working path and extend only missing bookmark/elimination behavior without rewriting it.
4. Elimination must not select/change an answer, save a grade, hide a chosen answer invisibly, or mutate first/blind answers. Keyboard/touch controls must be labeled and usable. Clear/remove one aid and clear current-question aids must be explicit, targeted actions; do not erase unrelated saved study state.
5. Keep passage find working and accessible where it exists. Add a bounded useful equivalent if missing on a relevant ordinary study canvas without changing question content. Search/highlights/elimination cannot interfere with LSAT reading text, text selection, zoom or question navigation. Preserve existing completed-report read-only and protected timed-canvas restrictions.
6. Honest failure behavior: a failed/corrupt/unavailable local store cannot claim saved state. Retain current aids in memory with a clear device-save disclosure if needed; isolate malformed records so another account/question cannot leak. No fake counts, synthetic user progress or seeded authored explanations.

Deferred from this work order: attributed second explanations, model-generated explanations, persisted mode/auto-reveal changes and first/blind grading semantics require a separate source/writer review. Do not implement those here. Whole ticket 179 remains open until its full acceptance and release gates pass.

## Verification and handoff

Meaningful tests at src/lib/questionStudyTools.test.ts must cover account/source/question isolation, restore/navigation, invalid storage and save failure, and separation from selected answers/Review. Add integration regression tests for bookmark/elimination interactions where meaningful. Run PROOF_CMD and npm run typecheck; report exact outcomes and any denied commands. Host independently reruns proofs and build.

Changes to UI are not complete until host browser verification: LR and RC task walks, widths 390/820/1060/1280/1600, actual side pane, keyboard and 200% text zoom. Builder must not claim those based on source/tests. Leave changes uncommitted, summarize architecture and changed files, identify actual device/account persistence guarantees, test commands/results and outstanding acceptance checks. Codex will inspect every file, run proof commands, and obtain fresh inspect --host codex --builder claude against BASE before integration. Keep any fix rounds bounded by MAX_FIX_ROUNDS.
