# Interim host proof observations

These checks ran during the initial build and are not final snapshot verification.

- Host `npm run typecheck` failed. With this repo's loose strictNullChecks setting, truthiness checks on discriminated unions do not narrow as intended. Reported property errors: backup.ts AssembleResult.reason/missing; RcRecallRunner.tsx SaveResult.reason and BackupHealth.reason; useRecapRecorder.ts BackupWrite.reason. Prefer explicit `ok === false` discrimination or equivalent type-safe handling; do not change global strictness.
- Initial reading-center test run: 31 files passed, 2 failed; 214 tests passed, 19 failed. RcRecallPage tests lacked Router context after new useLocation usage; runner tests expected the old Done reading/Start recap flow. Builder was updating tests during this run, so rerun completed snapshot before disposition.
- Claude's `npm run typecheck 2>&1 | tail -30` was denied by headless permissions. Host independently ran typecheck. No permission bypass or trust change authorized/performed.
