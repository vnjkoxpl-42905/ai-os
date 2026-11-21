# Cloudflare security-audit skill, quick profile (2026-10-14)

Scoped to `supabase/` plus the `src` client. Run status `incomplete` (usage limits: reconnaissance, verifier and final critic replaced by the parent agent). Source ref `2805e3bf`, dirty working tree. Source and local checks only; no sandbox, so nothing executed. 0 confirmed, 6 needs-validation (fingerprints in `findings.json`), 0 rejected. Ledger: 4 units with candidates, 3 covered, 0 deferred.

Findings 1 to 6 and the smaller findings are listed with checks in `../report-a-manual-review.md`. Skill source: cloudflare/security-audit-skill commit `c1c8a8c1`; its validators fail on Windows Node (no O_NOFOLLOW) and were run through a wrapper.
