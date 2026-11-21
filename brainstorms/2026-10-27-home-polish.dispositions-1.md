# Plan review round 1 dispositions

Review: research/2026-10-27-home-polish/review/claudex-6ax70skm/result.json. Observed claude-sonnet-5-5, Claude Code 2.1.309. Verdict REVISE. Original full result retained at that path; this file records host arbitration.

- F1 accepted: derive assigned-tab destination via canonical tab registry/access state; no link for locked/checking access. Tests cover open/locked/checking.
- F2 accepted: scan remains lean, newest stable (created_at,id), batch fetch only selected preview IDs. Explicit empty map success plus regression coverage. No large-body page scan.
- F3 accepted actor isolation/stale fidelity, with one correction: loaded denotes an existing successful actor-owned snapshot independently of current loading. Adding !loading would hide valid cached content during refresh and contradict the product requirement. The plan now explicitly defines stale=loaded+error, unavailable=!loaded+error and masked previous-actor data, with success/refetch-error/account-switch tests.
- F4 accepted per-file reconcile and explicit motion retirement. Confirmed git diff HEAD origin/main -- src/components/classroom/home is empty in old checkout. Current shared motion hook is retained elsewhere. Home uses data-motion-skip and deliberate local feedback; shared entrance hook would violate new tasteskill v2 app-screen rule against page entrances, so recommendation to reuse it for entrance is rejected. Test-day sessionStorage animation is retired for Home.
- F5 accepted: test exact-key exclusion and total/new/in-progress model coupling on refreshed/rerendered data.

No user scope change. Implementation remains authorized; original source checkout untouched. Request review of revised plan with the same limits, model/effort defaults and session.
