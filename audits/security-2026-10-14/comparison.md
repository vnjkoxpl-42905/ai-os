# Security tool comparison (2026-10-14)

| | Manual review (stand-in for Claude Security) | Cloudflare skill (quick) |
|---|---|---|
| Real findings | 2, 3, 5, 7 | 1, 2, 3, 4, 5, 6 |
| Missed | 1, 4, 6 | 7 (judged a design choice) |
| False positives | none | none |
| Effort | 1 reviewer, ~45 min | 2 hunters x ~17 min plus parent recon/verify; prescribed run needs 8+ agents |
| Output | prose | schema-valid ledger and findings with read-only checks |
| Fit here | fine | rough: assumes a sandbox, validators break on Windows, agent-hungry |

Findings 2, 3 and 5 were found independently by both.

Recommendation (Joshua decides): keep the Cloudflare skill in the quick profile with a Windows validator wrapper. Do not adopt Claude Security until it has run once as the main agent (`claude --agent claude-security:claude-security` from the LSAT U checkout). Fix first: revoke anon/public EXECUTE on `set_booking_availability_overrides`.
