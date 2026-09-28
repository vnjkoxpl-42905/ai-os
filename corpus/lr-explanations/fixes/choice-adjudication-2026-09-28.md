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
| PT114-S1-Q12 | D | Bank wording `different individual companies` is quoted by [Apollo Test Prep](https://www.apollotestprep.com/apollo-explanations/2023/05/23/38-1-12-explanation) for old PT38-S1-Q12 and used in [7Sage's explanation](https://7sage.com/lsat_explanations/lsat-114-section-1-question-12/); LSAT Lab/database omit `different` | Database choice updated with exact old-value guard after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt114-s1-q12-choice-repair.json` |
| PT135-S1-Q1 | B | [7Sage's full choice transcription](https://7sage.com/lsat/135/page/6/) agrees with bank; LSAT Lab/database had `oils in included` | Database choice updated after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt135-s1-q1-choice-repair.json` |
| PT133-S1-Q6 | D | [Old PT63 PDF](https://img.cracklsat.net/lsat/pt/pt63.pdf) and [7Sage](https://classic.7sage.com/lsat_explanations/lsat-133-section-1-question-06/) agree with bank's `other than digital circuits` | Database choice updated after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt133-s1-q6-choice-repair.json` |
| PT105-S4-Q12 | E | [Independent full-choice transcription](https://gmatclub.com/forum/nearly-everyone-has-complained-of-a-mistaken-utility-bill-that-cannot-429353.html) agrees with bank; database added `the` | Database choice updated after snapshot `raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt105-s4-q12-choice-repair.json` |
| PT101-S3-Q23 | E | [Old PT24 PDF](https://img.cracklsat.net/lsat/pt/pt24.pdf) and LSAT Lab/database end at `more expensive`; bank added `than wood, such as marble` | Bank branch `codex/lr-choice-official-2026-09-28` |

The database repairs use SQL files in `corpus/lr-explanations/work/pilot-inputs/` and snapshots in `raw/sources/lsatu-lr-snapshots/`. Each update returned the expected row with the corrected full text. The bank repairs changed 22 choices across [PR #181](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/181), [PR #182](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/182), and [PR #183](https://github.com/vnjkoxpl-42905/lsatu-684d89db/pull/183), all merged 2026-09-28. No answer keys changed.

## Deliberate source-version differences

| Slot | Choice | Decision |
|---|---|---|
| PT109-S4-Q14 | B | [Old PT22 PDF](https://img.cracklsat.net/lsat/pt/pt22.pdf) and LSAT Lab/database say `is plowed at all`; [7Sage](https://7sage.com/lsat_explanations/lsat-109-section-4-question-14/) and [PowerScore](https://forum.powerscore.com/viewtopic.php?p=113130) say `is not plowed at all`, matching the bank. Both are wrong answers. Retain the bank's clearer later wording and the database's historical wording, with the divergence documented. |
| PT106-S1-Q2 | B | [Old PT28 PDF](https://img.cracklsat.net/lsat/pt/pt28.pdf) and LSAT Lab/database print the duplicated `funding for funding for`; [PowerScore](https://testing.powerscore.com/viewtopic.php?f=617&p=85940&t=34714) and [Apollo](https://www.apollotestprep.com/apollo-explanations/2023/05/23/28-1-2-explanation) use the cleaned bank wording. Retain readable bank copy and the database's historical transcription; no key or reasoning difference. |

## Lower-impact differences left for a source audit

| Slot | Choice | Issue |
|---|---|---|
| PT104-S1-Q4 | A | Bank has `smaller`; LSAT Lab/database have `small`. Same answer logic; no official wording verified. |
| PT134-S1-Q12 | E | Bank has grammatical `to do only`; LSAT Lab/database have `only do`. Same answer logic; no official wording verified. |

The active-worktree scan found 173 choice pairs different after basic case and apostrophe normalization across 3,781 aligned bank/database questions. Thirty-one pairs had string similarity below 0.9; many are spacing, spelling, or punctuation. The remaining material candidates need source checks before changing either side. The earlier estimate of about 30 was not an exact count.
