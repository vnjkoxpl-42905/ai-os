-- PT102-S4-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=4 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Curious Fact$lsat$,$lsat$Why does the male inflate its air sac and display it to the female, during the courtship ritual?$lsat$),(1,$lsat$Hypothesis$lsat$,$lsat$It's so the female can select healthy mates.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The most common way to strengthen a hypothesis is to add plausibility to the causal story the author is telling. We'd love to hear that displaying air sacs is a way for a female to select healthy mates. We'd love a "no cause, no effect" answer that suggests that "when a female isn't trying to inspect the health of mates, the males don't inflate their air sacs".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that supports the plausibility that inflated air sacs help a female to determine how healthy a male is, (or an answer that rules out an alternate explanation for why the male inflates its air sacs during the mating ritual, like "it's NOT to make himself look bigger than other males".)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT103-S1-Q3 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=103 AND q.section=1 AND q.question_number=3 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Therefore)$lsat$,$lsat$A piece of candy with x amount of refined cane sugar is no higher calorie than a piece of fruit with x amount of fructose.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The number of calories in a gram of refined cane sugar is the same as in a gram of fructose.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$*Given that* a gram of refined sugar has the same caloric content as a gram of fructose,

*How could we argue that* a piece of candy with x grams of refined sugar **does** have more calories than a piece of fruit with x grams of fructose?

Well when it comes to the head to head battle of refined sugar vs. fructose, we know they're tied in calories.

But could the candy have other ingredients (fat? carbs? protein?) that also adds calories that the fruit doesn't have?$lsat$),(3,$lsat$Goal$lsat$,$lsat$This is basically a *Part vs. Whole* flaw, since the argument is thinking that since the "sugar part" of the candy/fruit would have the same calories, the candy/fruit "overall" would have the same calories.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT103-S2-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=103 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The Hyperion School of Journalism offers a valuable program to its students.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$65% of its graduates went on to internships or jobs in print or broadcast journalism.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The dean is defending the utility of the Hyperion School's program by pointing to the success of its graduates in securing positions in the field of journalism.

GIVEN THAT 65% of grads went on to internships or jobs in journalism,
HOW CAN WE ARGUE this school's program is not valuable to students?

Maybe we could say the program itself may not be the reason for the graduates' success. We could challenge the idea that the program added significant value by introducing an alternate explanation for the placement success.

Maybe we could point to an alternate way they could have gotten internships or jobs that would have been cheaper / more efficient.

Maybe the school places you in an internship/job, but they've prepared you so poorly that you quickly get fired from that position and blacklisted in the industry.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that allows us to argue that the school is not offering a lot of value to the students, or that offers an alternate explanation for why a majority of grads do end up getting internships/jobs in journalism.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT103-S3-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=103 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evidence$lsat$,$lsat$Using rational argument → doesn't persuade
in advertisements ppl to buy$lsat$),(1,$lsat$Conclusion$lsat$,$lsat$Using nonrational appeals → will persuade
to emotion in ads ppl to buy$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Consider this analogous argument:
*People who drive Toyota's do not live on Mars.*
*So, ppl who don't drive Toyota's do live on Mars.*

We're not allowed to just "flip a lightswitch" on claims. It's an illegal Negation (aka Necessary vs. Sufficient).

Our author's argument was basically this:
*Rational arguments don't persuade ppl.*
*Thus, nonrational arguments will persuade ppl.*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an argument that is like,
*Prem -* Things of type X don't do thing Y.
*Conc* - Things not of type X will do thing Y.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT103-S3-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=103 AND q.section=3 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Curious Phenomenon$lsat$,$lsat$Recently installed traps are far less effective than in eliminating pests than were traps installed several years ago.$lsat$),(1,$lsat$Hypothesis$lsat$,$lsat$The reason traps in certain households decreased in effectiveness is that successive generations of insects developed a resistance to the pesticide in the traps.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is presenting a Curious Comparison (the more recently installed traps eliminate **far fewer** pests than the old ones did) and trying to explain it (the newer pests have developed resistance to the poison inside), we would think about this as we always do when an author is Explaining a Curious Fact:

- could there be some Alternate Explanation for the curious fact?
*maybe the newer traps are less effective because the trap manufacturer changed the glucose/poison formula. maybe the newer traps are less effective because the insects have just learned to avoid them by seeing their friends and relatives enter but never exit.*

*-* how plausible is the Author's Explanation for the curious fact?
*if we were to insert some insects into these households who* **haven't** *been living with these traps for successive generations (and thus who* **wouldn't** *have been able to develop resistance), do they get killed at the higher rate like when we first installed the traps?*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Weaken, we want an answer to either
- **suggest** an Alternate Explanation for why these traps don't seem to be as effective any more, or
- **undermine** the plausibility of the Author's Explanation that successive generations of pests have developed resistance to the pesticide$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT103-S3-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=103 AND q.section=3 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$First L's Conclusion$lsat$,$lsat$Govt-sponsored medical research should have to include studies of women.$lsat$),(1,$lsat$Second L's Objection$lsat$,$lsat$(No they shouldn't). Considerations of male/female balance are inappropriate in medical research, and they have no place in science.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since we're trying to logically counter the 2nd person, we want to defend the 1st person's idea while responding to the 2nd person's.

It sounds like the second person is saying that science is sex-blind, but is it? Didn't science figure out that males have Y-chromosomes and females don't? Aren't there scientific differences between the sexes that make it scientifically relevant whether we're testing males vs. females?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that allows us to argue that having some research done on women IS appropriate. It does have a place in science. Doing research only on men is worse.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S1-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=1 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The poison set out to eliminate the gray squirrels eliminate them and would pose no threat to the owl population.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$The poison would be placed in containers accessible only to squirrels and other rodents.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument involves a Plan/Goal structure:

*Goal:* Eliminate the gray squirrels / don't harm the owls

*Plan:* Set out poison in specific containers for squirrels and other rodents.

To evaluate the argument, consider whether the Plan (poisoning squirrels) could fail to achieve the Goal (eliminating squirrels without harming owls). Although the officials believe their method won't impact owls due to the poison's placement, we should consider if this Plan could somehow still threaten the owl population indirectly.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want to find an answer that suggests a way in which setting out the poison could still pose a threat to the owl population, despite officials' claims to the contrary, or a way that it would fail to eliminate the squirrels.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S1-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=1 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Sales Figures$lsat$,$lsat$Last year, total number of meals sold at this company's restaurants was higher than it was 2 years ago.

Looking at individual restaurants, the number of meals sold decreased a bunch, at any location that was open 2 years ago and last year.

(For every location where we can compare 2 years ago to 1 year ago, the number of meals sold was bigger 2 years ago).$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$This question stem is only asking about "sales figures", so by not including the other sentences, where the two people are speculating about whether customers find the meals desirable, we are able to focus just on the two actual math facts.

Every single franchise of this restaurant that existed 2 years ago sold *fewer* meals this past year.

But overall, the restaurant chain sold *more* meals this past year than 2 years ago.

That must mean that there are **more locations** than before. If each location is selling **fewer** meals than the prior year, then we'll need **more** locations than before to get to a higher total number of meals.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Look for something like, "this company had more restaurants operating last year than two years ago".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

