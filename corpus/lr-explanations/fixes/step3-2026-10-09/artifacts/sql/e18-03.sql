insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('54578ff4-38db-4c40-a9a5-21b0d21c86b9'::uuid,4,'Evaluate','Two arguments are stacked here. Graham''s: a person is truly happy only when doing something, so the best life is full of activity. The philosopher''s: we shouldn''t be persuaded by Graham''s argument, because people are sometimes truly happy while sleeping, when they aren''t doing anything.

Which part of Graham''s argument does the sleep claim hit? Graham''s premise is a conditional:

truly happy → doing something

A sleeper who is truly happy while doing nothing has the left side without the right side. That''s a counterexample to the premise.

Notice what the philosopher does not claim. The philosopher never says the best life isn''t full of activity. The conclusion is only that Graham''s argument shouldn''t persuade us. Knocking out a premise is enough for that, because an argument with a false premise doesn''t establish its conclusion, even if the conclusion happens to be true.'),
('54578ff4-38db-4c40-a9a5-21b0d21c86b9'::uuid,5,'Goal','The claim in the stem is the philosopher''s premise, and its job is to show that Graham''s premise is false. Look for an answer that names both pieces: an example, aimed at Graham''s premise rather than Graham''s conclusion.'),
('c455f175-2763-4d8b-972a-a61f7a8224a2'::uuid,4,'Goal','The quoted claim is an intermediate conclusion, but the answer may not use that phrase. It might call the claim a premise that has support of its own. Look for an answer that says the claim is supported and also supports the main conclusion.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;