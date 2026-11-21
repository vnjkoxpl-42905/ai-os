insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('87919b24-e7fb-42a1-b12d-7f8ce5f8d72e'::uuid,1,'Evaluate','No conditional or causal chain here. The useful part is the pivot and its reason. The linguist is not attacking the hypothesis as false. The complaint is about verifiability: it is not clear the hypothesis could be tested at all.

What follows from a hypothesis that may not be testable? We cannot confirm it, and we cannot refute it. So we are in no position to say whether it is true. Notice what does not follow: that it is false, or that it should be ignored. The linguist says nothing about either.'),
('87919b24-e7fb-42a1-b12d-7f8ce5f8d72e'::uuid,2,'Goal','Look for a modest answer saying we cannot currently tell whether the Sapir-Whorf hypothesis is true. Expect wrong answers to call it false, or to jump to rules about which hypotheses deserve attention, or to say "only" physical science can be verified.'),
('979d1f49-6d4d-4f2a-a294-59fd314c0fbd'::uuid,1,'Evaluate','This is a concede-then-pivot paragraph, and the hard part is sorting what the commentator accepts from what the commentator rejects.

Winslow makes a claim about editors: they publish antienvironmental articles because those articles seem daring, seeming to challenge prevailing positions. The commentator says "It is true" and repeats that point almost word for word. So the commentator accepts Winslow''s account of what editors prefer.

Then comes "But." The pivot does not deny the editors'' preference. It denies that the articles actually are daring. Environmentalism is not the orthodox position, so attacking it is not a real challenge to orthodoxy, and the critics are not real dissidents. In short: the articles only seem daring, and that appearance is what editors are buying.

On a hard Most Supported question, the conceded part is often where the right answer hides, because the pivot pulls attention away from it.'),
('979d1f49-6d4d-4f2a-a294-59fd314c0fbd'::uuid,2,'Goal','Look for an answer saying Winslow is right about the editors: they prefer articles that seem to challenge prevailing positions. Expect traps that treat the "But" as a rejection of Winslow''s whole explanation, that say environmentalism is the orthodox view, or that deny the critics'' success at looking like renegades.'),
('81205ffa-816c-4c4f-8466-43873dfa8ead'::uuid,1,'Evaluate','On a logical completion, the blank is the conclusion, so we ask what the premises are building toward.

Look for the overlap. Premise one connects engine noise to communication: the noise sits in the whales'' communication range. Premise two connects engine noise to hearing damage. Put them together: boat noise can damage the very hearing the whales use to communicate.

The "Though" clause matters too. The whales do not act differently around engines, which might make us think the noise is harmless. The author is warning against that: no visible reaction does not mean no harm.'),
('81205ffa-816c-4c4f-8466-43873dfa8ead'::uuid,2,'Goal','Look for a conclusion like "boat engine noise may harm the whales'' ability to communicate, even though they show no reaction." Keep it soft, since the premises only say the damage "can" happen, and keep it tied to communication.'),
('db0144e4-130f-4db7-bd8d-55643f882b80'::uuid,1,'Evaluate','Three conditionals, and they share terms: large-scale farming appears in the first and second rules, irrigation in the second and third. Shared terms are a signal to chain.

Early urban society → large-scale farming → irrigation

Now look at the irrigation fact. Far from rivers or lakes, early irrigation was not feasible. Run the chain backward with contrapositives: no irrigation means no large-scale farming, and no large-scale farming means no early urban society.

Keep the time limit in view. Irrigation became feasible far from water "in more recent times," so the conclusion only holds for early times.'),
('db0144e4-130f-4db7-bd8d-55643f882b80'::uuid,2,'Goal','Look for an answer saying that, in early times, urban societies could not be maintained far from rivers or lakes. Watch for answers that drop "early," drop "urban," or claim anything about where people actually lived.'),
('3271c974-3514-4332-a22a-1f337613f0ba'::uuid,1,'Evaluate','Two rules talk about the same thing: whether compost may be used for drainage and fertility.

Good compost → appropriate for drainage and fertility
Strong ammonia smell → not appropriate for drainage and fertility

Take the contrapositive of the first rule: not appropriate → not good compost. Now chain:

Strong ammonia smell → not appropriate → not good compost

So any compost with a strong ammonia smell is not good compost, no matter what else is true of it.

The best-compost sentence is a distraction. It gives requirements for the best compost, so it can only tell us when something is not the best. It can never prove a compost is good or best.'),
('3271c974-3514-4332-a22a-1f337613f0ba'::uuid,2,'Goal','Look for an answer saying that compost with a strong ammonia smell is not good compost. Expect wrong answers that use the 40 to 60 percent or dark brown features to prove a compost is good, or that invent a link between organic percentage and decomposition.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;