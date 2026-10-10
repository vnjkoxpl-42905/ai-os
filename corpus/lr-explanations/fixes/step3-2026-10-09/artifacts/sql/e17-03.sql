insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('c98f53e7-554d-45c9-860b-0fc7af5b9a5c'::uuid,3,'Goal','Look for a principle whose condition is met by the evidence and whose outcome says something about all commitments:

some commitments deserve no praise → all commitments are morally neutral

An answer that only makes one kind of commitment neutral proves the conclusion for a subset. Eliminate it.'),
('815c307e-b295-47f2-bfc4-9bf58bf45557'::uuid,3,'Goal','Look for a principle with natural behavior on the left and "more worthwhile" on the right. It may say "authentic" instead of "naturally." A documentary whose subjects act naturally depicts them authentically, so that is the same idea in different words.

A principle can only prove what is on its right side. Any answer that never reaches "worthwhile" cannot prove this conclusion, however closely it talks about cameras.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;