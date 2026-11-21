# Claude round1 dispositions

2026-10-25. Actual reviewer: Claude Code2.1.309, observed model claude-sonnet-5-5; no model or effort override requested. Verdict REVISE. Entire response and its source hashes retained alongside this file. Claude read nine09 screenshots plus08 Home, all three runtime source files and host proof reports. It did not run a browser or tests. The runner used bounded artifact review, not full repository-diff inspection.

All eight findings are accepted with these implementation choices:

| ID | Decision |
|---|---|
| F1 | Wrap phone calendar into4+3 readable tiles with every day visible. Earlier no-document-overflow check was insufficient for clipped scroll content. |
| F2 | Preserve typed-reference demonstration but explicitly label synthetic content as not the real PrepTest item on question pages and result rows; clarify the finder. |
| F3 | Normalize partial reference search, including PT155, PT155 S1 and Q14. |
| F4 | Derive summary counts and date range from attempt records. |
| F5 | Restore useful keyboard focus after marking a message read; announce the state and retain draft text. |
| F6 | Use a neutral, clearly labelled sample-answer comparison, not fake assessment of arbitrary typed input. Preserve some/none scope. The review's phrase 'contrapositive negation' is not adopted: negating an existential is not contraposition. |
| F7 | Trim blank typed references and show accepted-format help. |
| F8 | Separate unavailable storage from malformed stored data; reset invalid sample data without claiming saving is unavailable. |

Run affected interaction and edge checks and recapture final screenshots before a fresh second review. Maximum2 review calls total. No prior review is claimed to cover later source changes.
