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

The database repair used `corpus/lr-explanations/work/pilot-inputs/pt108-s2-q7-choice-repair.sql`. A post-write read confirmed both exact values. The bank branch changes exactly 12 choices across six JSON files; no keys changed.

## Still needs source verification

| Slot | Choice | Issue |
|---|---|---|
| PT114-S1-Q12 | D | Bank differs from LSAT Lab/database. No official PDF found locally. |
| PT135-S1-Q1 | B | Bank differs from LSAT Lab/database; the latter says `oils in included`. No official PDF found locally. |
| PT106-S1-Q2 | B | Bank differs from LSAT Lab/database; the latter repeats `funding for`. No official PDF found locally. |
| PT105-S4-Q12 | E | Database adds `the` before `technology`; pilot bank text was preserved. |

These are the named discrepancies examined so far, not a complete inventory of the previously estimated 30. The broader diff inventory is being reduced by question identity and material wording changes.
