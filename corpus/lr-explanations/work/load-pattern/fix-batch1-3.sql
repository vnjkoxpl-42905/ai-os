-- PT103-S2-Q5 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The Hyperion School of Journalism offers a valuable program to its students.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$65% of its graduates went on to internships or jobs in print or broadcast journalism.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The dean is defending the utility of the Hyperion School's program by pointing to the success of its graduates in securing positions in the field of journalism.

GIVEN THAT 65% of grads went on to internships or jobs in journalism,
HOW CAN WE ARGUE this school's program is not valuable to students?

Maybe we could say the program itself may not be the reason for the graduates' success. We could challenge the idea that the program added significant value by introducing an alternate explanation for the placement success.

Maybe we could point to an alternate way they could have gotten internships or jobs that would have been cheaper / more efficient.

Maybe the school places you in an internship/job, but they've prepared you so poorly that you quickly get fired from that position and blacklisted in the industry.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that allows us to argue that the school is not offering a lot of value to the students, or that offers an alternate explanation for why a majority of grads do end up getting internships/jobs in journalism.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=103 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT103-S3-Q13 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Evidence$lsat$,$lsat$Using rational argument → doesn't persuade
in advertisements ppl to buy$lsat$),(1,$lsat$Conclusion$lsat$,$lsat$Using nonrational appeals → will persuade
to emotion in ads ppl to buy$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Consider this analogous argument:
*People who drive Toyota's do not live on Mars.*
*So, ppl who don't drive Toyota's do live on Mars.*

We're not allowed to just "flip a lightswitch" on claims. It's an illegal Negation (aka Necessary vs. Sufficient).

Our author's argument was basically this:
*Rational arguments don't persuade ppl.*
*Thus, nonrational arguments will persuade ppl.*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an argument that is like,
*Prem -* Things of type X don't do thing Y.
*Conc* - Things not of type X will do thing Y.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=103 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT103-S3-Q14 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Curious Phenomenon$lsat$,$lsat$Recently installed traps are far less effective than in eliminating pests than were traps installed several years ago.$lsat$),(1,$lsat$Hypothesis$lsat$,$lsat$The reason traps in certain households decreased in effectiveness is that successive generations of insects developed a resistance to the pesticide in the traps.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is presenting a Curious Comparison (the more recently installed traps eliminate **far fewer** pests than the old ones did) and trying to explain it (the newer pests have developed resistance to the poison inside), we would think about this as we always do when an author is Explaining a Curious Fact:

- could there be some Alternate Explanation for the curious fact?
*maybe the newer traps are less effective because the trap manufacturer changed the glucose/poison formula. maybe the newer traps are less effective because the insects have just learned to avoid them by seeing their friends and relatives enter but never exit.*

*-* how plausible is the Author's Explanation for the curious fact?
*if we were to insert some insects into these households who* **haven't** *been living with these traps for successive generations (and thus who* **wouldn't** *have been able to develop resistance), do they get killed at the higher rate like when we first installed the traps?*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Weaken, we want an answer to either
- **suggest** an Alternate Explanation for why these traps don't seem to be as effective any more, or
- **undermine** the plausibility of the Author's Explanation that successive generations of pests have developed resistance to the pesticide$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=103 AND q.section=3 AND q.question_number=14 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT103-S3-Q6 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$First L's Conclusion$lsat$,$lsat$Govt-sponsored medical research should have to include studies of women.$lsat$),(1,$lsat$Second L's Objection$lsat$,$lsat$(No they shouldn't). Considerations of male/female balance are inappropriate in medical research, and they have no place in science.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since we're trying to logically counter the 2nd person, we want to defend the 1st person's idea while responding to the 2nd person's.

It sounds like the second person is saying that science is sex-blind, but is it? Didn't science figure out that males have Y-chromosomes and females don't? Aren't there scientific differences between the sexes that make it scientifically relevant whether we're testing males vs. females?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that allows us to argue that having some research done on women IS appropriate. It does have a place in science. Doing research only on men is worse.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=103 AND q.section=3 AND q.question_number=6 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT104-S1-Q8 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The poison set out to eliminate the gray squirrels eliminate them and would pose no threat to the owl population.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$The poison would be placed in containers accessible only to squirrels and other rodents.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument involves a Plan/Goal structure:

*Goal:* Eliminate the gray squirrels / don't harm the owls

*Plan:* Set out poison in specific containers for squirrels and other rodents.

To evaluate the argument, consider whether the Plan (poisoning squirrels) could fail to achieve the Goal (eliminating squirrels without harming owls). Although the officials believe their method won't impact owls due to the poison's placement, we should consider if this Plan could somehow still threaten the owl population indirectly.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want to find an answer that suggests a way in which setting out the poison could still pose a threat to the owl population, despite officials' claims to the contrary, or a way that it would fail to eliminate the squirrels.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=104 AND q.section=1 AND q.question_number=8 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

