# Reading Center homepage navigation, 2026-10-18

Joshua requested the Reading Center option in his homepage rail and for Sandra, Gianna, and Celia.

## Live student grants verified

Authenticated with the existing admin account, resolved each exact email to one live class_id, previewed existing items, called the existing `assign_reading_center` RPC, and read back qualifying visible items with no unlock delay.

| Student | Email | Item | Result |
| --- | --- | --- | --- |
| Sandra Kooh | koohsandra@gmail.com | f326c9b9-29df-4e17-8042-d1a6c3f45406 | New, assigned |
| Gianna Jean | giannajean005@gmail.com | 966ebcda-bdbe-430e-a9bb-3653adfb3605 | New, assigned |
| Celia Cutler | celiacutler@gmail.com | 3ef6c6db-ec23-4da5-9960-221466605fd1 | Existing in_progress item preserved |

No notifications or emails sent. No student-session visual check claimed. The existing student launcher uses these grants.

## Teacher fix verified locally, awaiting merge

The teacher classroom shell explicitly excluded admins from the assignment-based launcher. A teacher-only Reading Center button was added to `src/components/classroom/shell/ClassroomLayout.tsx`, leaving student access rules unchanged. Branch `codex/reading-center-home-sidebar`, isolated sibling checkout `lsatu-reading-center-sidebar`.

Parent agent signed in through the local preview UI with saved credentials, verified Joshua Fisseha / Teacher, saw the new Reading Center rail button on `/classroom`, clicked it, and verified the loaded `/reading-center` dashboard. [Screenshot](2026-10-18-reading-center-teacher-sidebar.png).

17 navigation tests passed. Typecheck passed. Production build and canonical question-bank guard passed.

Joshua explicitly authorized merge and publication. PR #224 merged as `143875ad52eabadf50ae1c3f1d75d61021b8dd65`. Lovable latest_commit_sha matched this merge before free deploy_project was called. Deployment `44176743-8a60-4043-9d57-831761cbc55c` accepted, pending live verification. Previous production bundle: `index-Cf0f-2pW.js`.

Live verification passed: production bundle changed to `index-DXyQ7KsG.js`; downloaded bundle contains the new `!loading && is_admin` navigation group, button label Reading Center, and route `/reading-center`. Signed-in production `/classroom` showed Joshua Fisseha / Teacher and the new sidebar button below Library. Clicking opened `/reading-center` and loaded Your reading dashboard with the account's existing data. [Live screenshot](2026-10-18-reading-center-teacher-sidebar-live.png). Codex browser left on the live reading dashboard.
