# Drive inspection dispositions

Inspection: `C:/Users/Joshu/.codex/verification/2026-10-27-post-session-home/drive-inspection/claudex-hjty5yul/result.json`.

F1: generated manifests now ignored. git ls-files and git log --all showed none tracked or in history, so no files/index entries were removed. Existing policy already permits private student metadata in the authorized private backup, so the original severity rationale overstated a policy breach; excluding runtime manifests is still appropriate.
F2: import validates ok:true and performs owner-admin folder_links readback, comparing exact student/slug/folder sets and root identity. Mismatch exits nonzero. Backend contract implemented separately and not deployed.
F3: import requires complete copy status, matching root and slug folder IDs and verified restore sample. Before apply it freshly checks provider account, private permissions and each managed folder's root ancestry.
F4: verify-existing validates state/root consistency up front and checks restore-sample file permissions before download. Actual provider verification passed again for553 files and restore sample; originals unchanged.

Combined Python suite18 passed. No continuous sync or live Home deployment claim. Read all tests in full for final inspection; first inspection did not.

## Final inspection and bounded fixes

Second inspection `C:/Users/Joshu/.codex/verification/2026-10-27-post-session-home/drive-inspection/claudex-9ksuqhvk/result.json` returned REVISE. Accepted R1-R6: injectable transfer tests cover lost responses, conflicts, IDs and idempotent no-create reruns; private-copy and identity gates have direct mocked tests; malformed readback fails cleanly; apply failures save a safe audit without provider bodies or credentials; credential patterns expanded; native Windows gws.exe required; linked roots and escapes rejected.

Final combined suite: 36 tests run, passed with three actual symlink-creation cases skipped because Windows privilege was unavailable. Real Windows junction and deterministic link guards passed. A fresh read-only expanded credential scan passed all 553 original files. Native gws.exe path verified. No uploads, provider writes or deletes in the fix rounds. Two inspections exhausted; final corrections have host test proof, not independent reapproval.
