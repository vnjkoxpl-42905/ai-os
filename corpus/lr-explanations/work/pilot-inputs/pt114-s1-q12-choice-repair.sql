-- PT114-S1-Q12 D, source: bank; corroborated by Apollo Test Prep PT38-S1-Q12 and 7Sage's explanation.
-- Pre-write snapshot: raw/sources/lsatu-lr-snapshots/2026-09-28-pre-pt114-s1-q12-choice-repair.json
UPDATE lr_answer_choices
SET choice_text = 'Large governmental job retraining programs do not meet the short-term needs of different individual companies.'
WHERE id = '456c1e98-30e9-4547-89f5-cfcbe8c58343'
  AND question_id = '6a01eec7-56c4-44c5-a79f-e07b60c732c2'
  AND letter = 'D'
  AND choice_text = 'Large governmental job retraining programs do not meet the short-term needs of individual companies.'
RETURNING id, choice_text;
