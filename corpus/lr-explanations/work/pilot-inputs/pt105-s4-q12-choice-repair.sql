-- PT105-S4-Q12 E, source: bank and an independent full-choice transcription on GMAT Club.
-- Pre-write snapshot: raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt105-s4-q12-choice-repair.json
UPDATE lr_answer_choices
SET choice_text = 'The less willing people are to do without technology the more likely they are to complain about the effects of technology.'
WHERE id = '7d942a9e-fcd2-48d5-b3d7-5e88ad846ea2'
  AND question_id = 'b8a0a4b5-2d88-4af0-9fc9-9d8d9f0dc1e2'
  AND letter = 'E'
  AND choice_text = 'The less willing people are to do without technology the more likely they are to complain about the effects of the technology.'
RETURNING id, choice_text;
