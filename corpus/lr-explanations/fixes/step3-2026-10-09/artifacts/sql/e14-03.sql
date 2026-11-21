insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('024b58e6-5d5c-4e51-b8ff-f32dc5ce5e85'::uuid,2,'Goal','Eliminate four answers that take one of the two routes: more gas burned in Jimmy''s household, or a higher price per unit. The correct answer will do neither. A good place to look: an answer about the water heater itself, since the stimulus already tells us the heater is efficient, which points toward less gas, not more.'),
('c55f58b1-63cc-446d-9615-85cc6834668a'::uuid,3,'Goal','Look for an argument with the same recipe:
People who do X have more Y than people who do not.
So if you want Y, you should do X.

The evidence must be a bare comparison between groups, not a stated cause. If an answer''s evidence already says X produces Y (it enables Y, lowers Y, helps with Y), then recommending X is reasonable and the flaw is gone.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;