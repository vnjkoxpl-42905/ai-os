-- PT135-S1-Q1 B, source: bank and 7Sage's full choice B transcription.
-- Pre-write snapshot: raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt135-s1-q1-choice-repair.json
UPDATE lr_answer_choices
SET choice_text = 'Studies suggest that the kinds of oils in the fat included in the Mediterranean diet may protect the heart against potentially fatal disruptions of heart rhythms and other causes of heart attacks.'
WHERE id = 'e2f0c888-5c07-4af9-b6aa-af1a5ec263d2'
  AND question_id = '170cbca5-2938-4554-82b2-9e19a78ef0c4'
  AND letter = 'B'
  AND choice_text = 'Studies suggest that the kinds of oils in included in the Mediterranean diet may protect the heart against potentially fatal disruptions of heart rhythms and other causes of heart attacks.'
RETURNING id, choice_text;
