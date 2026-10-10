insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('502b30bb-33b7-433b-9333-2980364a57dd'::uuid,1,'Evaluate','Line the analysis up against the coat. The coat buyer gives up warmth, which is comfort. The coat buyer does it to look sophisticated, which is appearances.

So the analysis has two ingredients, and a matching situation needs both:
1. A real sacrifice: the person picks something that feels, tastes, or works worse for them.
2. A reason about how they look to others.

A choice with only one ingredient doesn''t fit. Someone who sacrifices comfort for the planet fails the second. Someone who wants to impress but gives up nothing fails the first.'),
('502b30bb-33b7-433b-9333-2980364a57dd'::uuid,2,'Goal','Look for a person who knowingly takes the less pleasant option so that other people will be impressed.'),
('02878155-9b61-4c9e-91c7-2a55dc07b72f'::uuid,1,'Evaluate','Describe what happened in general terms, since the right principle won''t mention stairs or ladders.

How did the children learn the word? By walking up and down the stairs, so they learned it through how the object is used.

What did they do later? They called a ladder "stairs." A ladder is a different object, but it is used the same way: you climb it.

So the study shows children stretching a word from the object they learned it on to a different object with the same use. Notice what the study does not show. It doesn''t compare teaching methods, so it can''t tell us how children learn "best." And it has one group at one age, so it can''t tell us anything about age.'),
('02878155-9b61-4c9e-91c7-2a55dc07b72f'::uuid,2,'Goal','Something like: children who learn a word through how an object is used sometimes apply the word to a different object that is used in a similar way.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;