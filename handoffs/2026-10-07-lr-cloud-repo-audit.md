# LR cloud repository audit

Checked 2026-10-07 using GitHub API recursive main trees and actual Git blob identities, compared to local files through Git clean filters (`git hash-object --path`) so Windows line endings do not create false differences. Read-only remote inspection; no task execution or production access tested.

ai-os remote main: `7e3a37c49aad80bc3d36352b796612425fe9b051`, recorded commit date 2026-10-02. Of 46 selected required/context/support files: 20 match, 18 are absent remotely, 8 differ locally. This is a selected dependency inventory, not every repository file.

Cloud clone alone cannot resume the exact local state. Missing approved finish plan and handoffs, newer voice files, newer DB mirrors, and local scratch proposals must be transferred or refreshed. Scratch outputs under Temp are outside either repository and were not part of these Git trees.

## Required files and supporting records

| Path | GitHub main compared to local |
|---|---|
| `brainstorms/2026-10-07-finish-lr-explanations.md` | missing remote |
| `handoffs/2026-10-07-lr-cloud-context.md` | missing remote |
| `handoffs/2026-10-07-lr-cloud-prompt.md` | missing remote |
| `wiki/teaching-voice.md` | different local |
| `wiki/COPY-CORRECTIONS.md` | different local |
| `references/lsat-teaching-voice-standard.md` | missing remote |
| `corpus/lr-explanations/golden-set.md` | identical |
| `corpus/lr-explanations/golden-set-observations.md` | identical |
| `corpus/lr-explanations/fixes/choice-adjudication-2026-09-28.md` | identical |
| `corpus/lr-explanations/fixes/choice-note-issues.md` | identical |
| `corpus/lr-explanations/fixes/index.md` | different local |
| `corpus/lr-explanations/fixes/label-sweep-2026-10-02.txt` | missing remote |
| `corpus/lr-explanations/fixes/lsatlab-audit-2026-09-27.json` | identical |
| `corpus/lr-explanations/fixes/lsatlab-audit-2026-09-27.md` | identical |
| `corpus/lr-explanations/fixes/model-library-defects.md` | identical |
| `corpus/lr-explanations/fixes/revamp-inventory.csv` | identical |
| `corpus/lr-explanations/fixes/revamp-list.md` | identical |
| `corpus/lr-explanations/fixes/side-issues.md` | identical |
| `corpus/lr-explanations/fixes/type-sweep-2026-10-02-bank-changes.json` | missing remote |
| `corpus/lr-explanations/fixes/type-sweep-2026-10-02-db-changes.json` | missing remote |
| `corpus/lr-explanations/fixes/type-sweep-2026-10-02-verdicts.json` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/applybank.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/byteparity.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/catdiff.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/catsql.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/classify.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/difftests.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/stemtype.py` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/sweep.ts` | missing remote |
| `corpus/lr-explanations/fixes/timed-catalog-rotation/verdict.py` | missing remote |
| `corpus/lr-explanations/models/Flaw.md` | identical |
| `corpus/lr-explanations/models/index.md` | identical |
| `corpus/lr-explanations/models/MBT-MBF.md` | identical |
| `corpus/lr-explanations/models/MC-Role-Agree.md` | identical |
| `corpus/lr-explanations/models/NA.md` | identical |
| `corpus/lr-explanations/models/Paradox-Method.md` | identical |
| `corpus/lr-explanations/models/Parallel.md` | identical |
| `corpus/lr-explanations/models/Principle.md` | identical |
| `corpus/lr-explanations/models/Strengthen-SA.md` | identical |
| `corpus/lr-explanations/models/Weaken-Evaluate.md` | identical |
| `.claude/skills/lsat-u-voice/SKILL.md` | missing remote |
| `system/scripts/lsatlab-pull/data/db/lr_questions.json` | different local |
| `system/scripts/lsatlab-pull/data/db/lr_answer_choices.json` | different local |
| `system/scripts/lsatlab-pull/data/db/lr_explanations.json` | different local |
| `system/scripts/lsatlab-pull/data/db/lr_explanation_steps.json` | different local |
| `system/scripts/lsatlab-pull/data/db/lr_explanation_choice_notes.json` | different local |

## App repository

GitHub `vnjkoxpl-42905/lsatu-684d89db` main is `6483f7ee77aa68a2a290dab96e1ae13d9c91c73f`, commit date 2026-10-07T21:57:27Z. PR #203 is closed and merged at 2026-10-07T21:54:46Z, merge commit `7881dab3c880e1ca9986eb1abfacc2bf9a6f9510`. GitHub compare reports main ahead by two commits, behind by zero relative to that merge. This confirms source availability, not deployed production.

Remote tree contains 156 `public/data/PT*-S*-LR.json` files. `public/data/PT114-S4-LR.json` blob is `83fffcc4bd18cc951ede33de7b4267e18a6490b1`. Root `AGENTS.md` and `CLAUDE.md` exist, blobs `ade7b18a7693743023bd6e56549be49ac8a9292c` and `9c5ebdc36b06e19155ffc935958801a96ec12da6`. Root `CONTEXT.md` is absent; this does not establish whether a differently located context file exists.

Repository picker availability and selecting both repositories do not prove a running cloud session has read either checkout. The browser inspected an unsent task composer, so a runtime probe remains needed. Enabled Lovable connector does not by itself prove project/table/write/deploy tool access.
