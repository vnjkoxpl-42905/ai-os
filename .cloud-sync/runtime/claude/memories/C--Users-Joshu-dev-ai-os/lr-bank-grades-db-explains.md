---
name: lr-bank-grades-db-explains
description: LR questions live twice; the app shows and grades from the question bank files but shows explanations from the DB, so the two must match slot for slot.
metadata:
  type: project
---

LSAT U stores each LR question twice: the question bank (`public/data/PT*-LR.json`, stimulus, choices, key, type, features, difficulty) and the database (`lr_questions` plus the explanation tables). The app shows the question and grades the student from the bank; it shows the Question Explanation from the database, matched by PT/section/number.

**Why:** on 2026-09-27, 155 bank slots held a different question than the database (runs copied from the wrong section), and an earlier key repair had aligned keys to slots without fixing the text. Students were graded against another question's key. Fixed in PR vnjkoxpl-42905/lsatu-684d89db#146 from official PDFs.

**How to apply:** after any bank or explanation load, compare bank and DB stimulus + key per slot (0 mismatches expected). The DB lacks answer choices, so a bank rebuild needs the official PDFs (Joshua has them in Downloads). The bank `correctAnswer` test only checks keys, not text. See [[lsatu-content-lives-in-postgres]].
