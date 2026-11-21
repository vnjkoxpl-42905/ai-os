# RC Training delegated build

- User authorized implementation through claude-build, requested Sonnet 5.5 medium, and authorized a local isolated snapshot commit.
- SPEC_FILE: `C:/Users/Joshu/dev/ai-os/brainstorms/2026-10-16-rc-training-build-spec.md`
- LOG_FILE: this file.
- PROOF_CMD: `npm run test -- src/features/reading-center`. Additional required independent proofs: `npm run typecheck`, `npm run build`.
- MAX_FIX_ROUNDS: 3.
- Original checkout: `C:/Users/Joshu/dev/ai-os-projects/lsatu-reading-center-rc-recall`, original HEAD `e2f24cdadad70f218e2b2002ce1a7ee6b59d3d18`.
- Isolated build checkout: `C:/Users/Joshu/dev/ai-os-projects/lsatu-rc-sonnet-build`.
- Pre-build baseline: `efc748b0` (local snapshot commit). 36 copied files individually SHA-256 verified in baseline-files.json. Excluded unrelated `supabase/functions/mcp/index.ts`. Original checkout preserved.
- Host setup authored no application changes. Reused installed node_modules through an isolated-checkout junction; no dependency installation or global permission changes.
- Claude CLI 2.1.296 at `C:/Users/Joshu/.local/bin/claude.exe`.
- Model smoke check returned READY, observed identity `claude-sonnet-5-5`, requested effort medium. Smoke test is not build verification.
- Build artifact directory: `claudex-1gn9x_09`. command.json confirms `--model claude-sonnet-5-5 --effort medium`, normal acceptEdits permissions, no bypass.
- Work order launched with `--unreviewed-spec`: user authorized standalone build; independent plan approval is not claimed. Final independent inspection remains mandatory.
- Setup warning: Claude reports untrusted workspace and ignored project allow entries. No trust configuration changed. Required denied commands must be reported; host may run authorized proofs independently.
- Backend deployment and video rendering remain outside scope. Real signed-in persistence acceptance remains blocked by the previously confirmed missing table until separately authorized deployment.

## Build outcome and independent repair, 2026-10-17

- Initial Claude build `claudex-1gn9x_09` timed out after 1810 seconds. It is FAILED, not resumed or relabelled successful. Substantial saved files were salvaged. Some shell proofs were denied under the untrusted workspace; host ran proofs without changing trust or permissions.
- Required Codex CLI inspection `claudex-a_2shiz3` failed before launch with "Codex MCP discovery failed; review was not launched." Independent scoped Codex subagents inspected persistence, runner/instruction/history, and navigation, then repaired accepted findings. This is a disclosed workflow deviation, not successful Codex CLI inspection.
- Authorship is mixed: initial implementation by Claude Sonnet 5.5 medium, subsequent repairs by Codex. No simultaneous provider edits. Fresh Claude inspections review Codex repairs.
- First fresh Claude inspection `claudex-8q8wjrjj`: REVISE. Round 2 fixed empty recording-start orphan retry, access-error navigation, history deduplication/stale checkpoints, table/storage probes, recovery overlap, completion clock restart, and inaccurate instructional/save copy. Neutral historical labels avoid inventing a procedure version missing from the schema. The spec was updated accordingly (SHA256 bed3e1c5f41c02dfa11063297cadc1b27b52153dfd93a815f1cb2915618fc203).
- Independent host final3 proofs: 363 tests across 41 Reading Center test files passed; typecheck and production build exited 0. These are local/mocked proofs, not real backend acceptance.
- Second Claude inspection `claudex-208suehb`: REVISE. The Vite/build tooling regenerated an unrelated MCP function pointing at a machine-local path. This was detected by host integration preflight and reviewer. Its generated contents are preserved in this artifact directory; the isolated MCP file must be restored after tooling stops and excluded from integration. Original MCP SHA256 remains 95dfb1a138c1c0fe7c73c7978184550456180dc84c67738c9f358511cf7a641f.
- Round 3 addresses non-resumable history attention and expired-session probe classification. Pending timestamp concern is being assessed against the explicit active-time contract.

## Browser evidence

- Tested existing authenticated local preview at 127.0.0.1:8080 with actual connected backend. Backend remains unavailable; launch stays disabled, with an honest message and retry check.
- Manually exercised all seven instructional demo stages, including text hidden during recall, omission/correction, both-paragraph confirmation and optional final recall. No recording or section-completion claim.
- Verified RC-to-LR and LR-to-RC from scrolled views: destination scroll starts at top and heading receives focus. Mobile drawer also yields focus to heading. Back restores RC scroll (~725.6px); Forward restores LR at top. Direct instructions hash/reload expands and focuses the instructions heading.
- Tags retains main navigation. Reading Progress exposes RC Training and updates the activity query parameter.
- Responsive DOM checks at 320, 768, 900, 1024 and 1440px: no page horizontal overflow. Desktop and narrow-screen screenshots saved here. Narrow screenshot used a 400x1000 capture clip for Windows 125% display scaling; layout emulation was 320x800. Desktop layout restored afterward.
- Deliberately unverified: actual microphone recording, cloud uploads/playback, server writes/RLS isolation, full live completion/history, and cross-device resume (not implemented). The missing persistence objects block those acceptance paths.
