-- PT124-S3-Q17 D, source: logged-in LSAT Lab question 2988 and the bank.
-- Pre-write snapshot: raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt124-s3-q17-choice-repair.json
UPDATE lr_answer_choices
SET choice_text = 'offers an analogy in support of a conclusion without indicating whether the two types of things compared share any similarities'
WHERE id = '71ef7171-d980-4e69-bddb-8b69a024bd57'
  AND question_id = 'a6e8225c-7a95-498a-bc9c-faa1e22c8878'
  AND letter = 'D'
  AND choice_text = ''
RETURNING id, choice_text;
