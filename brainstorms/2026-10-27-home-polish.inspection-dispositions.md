# Final inspection dispositions
F1 fixed: five malformed hover blocks now have proper top-level media queries. Added homeStyles.test.ts to reject nested rules/media and empty media.
F2 fixed: today base highlight is outside hover query; regression assertion reads the actual source file.
F3 fixed without deleting: useHomeEntrance.ts is now a compatibility export of interaction-only useHomeFeedback.
152 existing tests passed; two new CSS checks passed after correcting the test loader to read source directly. App build/typecheck and visual evidence are being refreshed.
Read all new/untracked production files in scope, especially teacher/*, HomeWeekStrip.tsx, useHomeFeedback.ts, freshness helpers, role dispatcher, and new tests. Do not limit review to git diff for tracked files. Explicitly report files opened and coverage limits. Check the preview harness too. No claim of real signed-in backend acceptance is made.
