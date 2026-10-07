-- PT133-S1-Q6 D, source: bank and old PT63 official PDF text corroborated by 7Sage.
-- Pre-write snapshot: raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt133-s1-q6-choice-repair.json
UPDATE lr_answer_choices
SET choice_text = 'Semiconductors will always be preferable to vacuum tubes for use in many applications other than digital circuits.'
WHERE id = '54b28769-9e13-4af4-b8aa-b41c9da9c5d2'
  AND question_id = 'e92ecbf6-de01-443f-b4b3-056856045a46'
  AND letter = 'D'
  AND choice_text = 'Semiconductors will always be preferable to vacuum tubes for use in many applications.'
RETURNING id, choice_text;
