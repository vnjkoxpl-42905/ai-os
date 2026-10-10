insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('13d2121f-3a1b-4502-8593-2af9ab5f95d4'::uuid,3,'Goal','Look for a rule whose trigger matches what the experiment showed about gesturing (it goes with quicker speech and less repetition) and whose outcome is the conclusion''s new idea (helps speakers quickly find the phrases they want).

Expect a reversal trap: a rule that runs from helping find phrases to quicker speech. That direction starts from the thing we are trying to prove, so it can''t prove it.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;