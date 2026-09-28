---
type: source-adjudication
subject: LR answer-choice wording
updated: 2026-09-28
---

# Choice wording adjudication, 2026-09-28

The bank JSON is what students answer. The database `lr_answer_choices` is the source-text guard and explanation-writing reference. Compare full choices, not just keys or prefixes.

## Confirmed repairs

| Slot | Choices | Source that settled the wording | Repair |
|---|---|---|---|
| PT101-S2-Q25 | C, D, E | Logged-in LSAT Lab question 7711 agrees with database | Bank branch `codex/lr-choice-text-fixes-2026-09-28` |
| PT101-S3-Q20 | C, D, E | Logged-in LSAT Lab question 7731 agrees with database | Same bank branch; normalized an extra database space in E |
| PT139-S1-Q11 | B, C, D | Logged-in LSAT Lab question 2333 agrees with database | Same bank branch; bank had concatenated and shifted options |
| PT111-S4-Q10 | E | Logged-in LSAT Lab question 5528 agrees with database | Same bank branch; `without` corrected to `with` |
| PT103-S3-Q18 | E | Logged-in LSAT Lab question 4500 agrees with database | Same bank branch; restored `not` |
| PT155-S1-Q21 | B | Logged-in LSAT Lab question 10183 and official `pt 155.pdf`, PDF page 11 | Same bank branch; `is` corrected to `will be` |
| PT108-S2-Q7 | C, E | Official `pt 108.pdf`, PDF page 13, agrees with bank; LSAT Lab and database differ | Database C and E updated with exact old-text guards after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt108-s2-q7-choice-repair.json` |
| PT102-S2-Q18 | C | Logged-in LSAT Lab question 7602 agrees with database | Bank branch; corrected a different flaw choice, then updated the draft note |
| PT103-S2-Q17 | E | Logged-in LSAT Lab question 4474 agrees with database | Bank branch; E had duplicated A |
| PT141-S4-Q13 | A | Logged-in LSAT Lab question 290 agrees with database | Bank branch; restored `2003` after a truncated `prior to` |
| PT144-S3-Q21 | E | Logged-in LSAT Lab question 2443 agrees with database | Bank branch; restored the comparison ending |
| PT150-S3-Q21 | E | Logged-in LSAT Lab question 4104 agrees with database | Bank branch; restored the truncated question ending |
| PT124-S3-Q17 | D | Logged-in LSAT Lab question 2988 agrees with bank | Empty database choice text filled after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt124-s3-q17-choice-repair.json` |
| PT105-S4-Q14 | D | Logged-in LSAT Lab question 7446 agrees with database | Follow-up bank branch; changed `would` to `could` in correct choice |
| PT148-S3-Q7 | A | Logged-in LSAT Lab question 135 agrees with database | Follow-up bank branch; removed extra `food` |
| PT152-S2-Q1 | B, C | Logged-in LSAT Lab question 3830 agrees with database | Follow-up bank branch; removed extra `student` before `housing` |

The PT108 database repair used `corpus/lr-explanations/work/pilot-inputs/pt108-s2-q7-choice-repair.sql`. A post-write read confirmed both exact values. The PT124 D update was guarded on the exact empty value and returned the complete text. The bank repairs changed 17 choices in 11 JSON files in [PR #181](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/181), merged 2026-09-28. No answer keys changed.

## Still needs source verification

| Slot | Choice | Issue |
|---|---|---|
| PT114-S1-Q12 | D | Bank differs from LSAT Lab/database. No official PDF found locally. |
| PT135-S1-Q1 | B | Bank differs from LSAT Lab/database; the latter says `oils in included`. No official PDF found locally. |
| PT106-S1-Q2 | B | Bank differs from LSAT Lab/database; the latter repeats `funding for`. No official PDF found locally. |
| PT105-S4-Q12 | E | Database adds `the` before `technology`; pilot bank text was preserved. |
| PT109-S4-Q14 | B | Bank includes `not plowed at all`; LSAT Lab and database omit `not`. The latter wording is logically suspect; official PDF needed. |
| PT133-S1-Q6 | D | Bank includes `other than digital circuits`; LSAT Lab and database omit it. Official PDF needed. |
| PT101-S3-Q23 | E | Bank adds `than wood, such as marble`; LSAT Lab and database end with `more expensive`. Official PDF needed. |

The active-worktree scan found 173 choice pairs different after basic case and apostrophe normalization across 3,781 aligned bank/database questions. Thirty-one pairs had string similarity below 0.9; many are spacing, spelling, or punctuation. The remaining material candidates need source checks before changing either side. The earlier estimate of about 30 was not an exact count.

PT104-S1-Q4 A has `smaller` in the bank and `small` in LSAT Lab/database. PT134-S1-Q12 E has grammatical `to do only` in the bank and `only do` in LSAT Lab/database. Neither changes the answer logic, and neither was edited without an official source.
