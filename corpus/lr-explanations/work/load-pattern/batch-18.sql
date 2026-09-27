-- PT118-S4-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=4 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*conditionals* (only = *right*, unless = "if not")

people don't feel → people are not happy
needed by others

*quantifiers* (most / almost everyone)
*causal* (because)

knowing your job don't feel needed
can be done by ⇢ other than family
1000s of people & friends$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$This one is kind of a mess to break down technically, because there's causality, conditional logic, and quantifiers. So let's get more conversational with our understanding.

Usually when we see a conditional rule in Inference, they want us to chain it to another conditional or apply it to some specific fact. Both of the first two claims are talking about *Indispensability / Feeling Needed*. Overlapping concepts point us towards possible inferences.

Since people don't feel happy if they don't feel needed, and since they only ever feel needed within their group of family / friends, it means that they don't feel happy outside their sphere of family and friends.

The 3rd claim provides a causal relationship between whether or not we feel needed and whether or not we think we're easily replaceable.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's find a safely worded answer making use of our knowledge:

Most people feel replaceable at work, so they don't feel needed, so they don't feel happy. (Within the sphere of family / friends, they may feel needed, so they may feel happy)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (rebuttal)$lsat$,$lsat$But this is wrong.

*rephrase:* The complexity of connecting components to computers is a widespread obstacle to people using computers.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Setting jumpers and switches to specific specifications can be confusing, and installing necessary software for components might disrupt the functioning of other computer systems.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We need to counter the rebuttal conclusion that connecting components is a significant obstacle. So we basically need to defend the original position, that there's no reason that connecting components should thwart most people from having a computer.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer that demonstrates why connecting components, despite potential complexities, does not markedly hinder typical users from setting up and using computers.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S4-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=4 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (should = opinion)$lsat$,$lsat$We should replace the old bridge with a cable bridge, rather than a concrete skyway.$lsat$),(1,$lsat$Intermediate Conclusion (clearly)$lsat$,$lsat$The extra cost of the cable bridge would be justified.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$It's important to maintain the beauty of our river crossing.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$This argument boils down to a choice between the cable bridge and the concrete skyway. The author identifies some competing interests at play:

*concrete skyway* - better option when it comes to cost
*cable bridge* - better option when it comes to maintaining the beauty of our river crossing.

How could we object to the decision to go with the cable bridge? Maybe it's way less safe than the concrete skyway? Could safety concerns override beauty concerns?$lsat$),(4,$lsat$Goal$lsat$,$lsat$We're probably going to get a *Defender* style correct answer, where it's ruling out some objection to the cable bridge, for example:
*- the cable bridge is* **not** *far more prone than is a concrete skyway to catastrophic collapse*

Otherwise let's just pick something that relates to how the author is weighing these tradeoffs between cost and beauty.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S4-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=4 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$People can help reduce air pollution by choosing electric mowers over gasoline ones whenever feasible.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$A typical gasoline-powered lawn mower emits about as much air-polluting material per hour of use as does an automobile.

Collectively, such mowers contribute significantly to summer air pollution.

Electric mowers emit no air pollutants.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument is presenting a Plan/Goal pattern.

*Goal:* Reduce air pollution.

*Plan:* Use electric mowers instead of gasoline-powered mowers whenever feasible.

To strengthen the Plan/Goal, we want to ensure that switching to electric mowers will indeed result in a significant reduction of air pollution. In addition, the argument primarily highlights that electric mowers emit no pollutants directly. To support the argument, we could emphasize that using electric mowers, including their indirect emissions, would still be less polluting than using gasoline mowers.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that allows us to argue more persuasively that choosing electric mowers over gasoline mowers will reduce air pollution. Additionally, consider the overall environmental impact, including the generation of electricity needed for electric mowers.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT119-S2-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=119 AND q.section=2 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$Shakespeare could have written the love poetry attributed to him.

Meanwhile, the dramas attributed to him are so insightful about the minds of powerful rules that they could only be written by someone who'd hung out with rulers.

Shakespeare didn't. Bacon did.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Since this is Must Be True, the biggest thing on our radar is conditional logic, which here shows up with the word **only** (a necessary indicator = put the following idea on the Right).

*Wrote these insightful spent lots of time*
*dramas about minds → with rulers*
*of rulers*

Do we have another Conditional to chain this to? No.

Do we have a fact that triggers this rule or triggers its contrapositive? Yes.

The contrapositive says,
*didn't spend time → couldn't have written these*
*around rulers insightful dramas*

We know that Shakespeare didn't associate with rulers, so we can output the inference that Shakespeare couldn't have written the dramas attributed to him.

They are definitely trying to bait us into concluding that Francis Bacon *did* write those dramas, but that would be reading backwards.

Francis Bacon *may* have written the dramas, since he had the required firsthand exposure to rulers, but so could any number of other people who, like Bacon, associated with rulers.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Pick anything provable, but it's most likely that they're trying to reward us for applying the fact about Shakespeare to trigger the contrapositive of the rule they provided.

So we should anticipate "Shakespeare didn't write the dramas attributed to him".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT119-S4-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=119 AND q.section=4 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Charlene's Conclusion$lsat$,$lsat$Using microorganisms to metabolize pollutants has limitations.$lsat$),(1,$lsat$Charlene's Evidence$lsat$,$lsat$Microbes are less active when a region's temps are below normal.$lsat$),(2,$lsat$Olaf's Rebuttal$lsat$,$lsat$No. The activity level of microbes is basically the same whether they live in Arctic or subtropical regions.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The problem with Olaf's rebuttal is he's acting like Charlene said "microbes don't work as well in cold climates", and thus rebutting that by saying "look --- these microbes work as well in the cold (arctic) as they do in the warm (subtropical)."

But Charlene was just saying that microbes don't work as well when the local temperature is lower than average.

So if the average temperature in the Arctic is 0 degrees Celsius, then arctic microbes won't work as well when the temperature drops to -10 degrees.

If the average temp in the subtropics is 27 degrees Celsius, then subtropical microbes won't work as well when the temperature drops to 17 degrees.$lsat$),(4,$lsat$Goal$lsat$,$lsat$Olaf's flaw was thinking in **Absolute** terms of "low temp" when Charlene was talking about a **Relative** sense of "low temp".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S1-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=1 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (so)$lsat$,$lsat$The use of a cash flow statement is critical for all businesses.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Businesses can get into trouble by over-expanding if they only account for monthly expenses, ignoring non-monthly expenses.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$"Cash flow statement" is a *New Concept in the Conclusion*, so we can ask ourselves, "What is the author assuming about this new concept?"

Since they're telling us that it's critical for businesses to account for non-monthly expenses, they must be assuming that cash flow statements solve the problem of tracking both monthly and non-monthly expenses.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer that effectively demonstrates how cash flow statements are indispensable for tracking non-monthly expenses or proves there are no viable alternatives, reinforcing their critical role.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S1-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=1 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$Many people say they're more morally upright than they are.

*Conditionals* (When = sufficient indicator)

Hypocrisy → embarrassed → motivates ppl
exposed by moral lapse to be better

Hypocrisy → Fosters belief → motivates ppl
not exposed most ppl good to be good$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$We're given binary triggers: "If hypocrisy is exposed, X happens. If it's not exposed, Y happens." When you have a set of binary triggers, you're guaranteed that one or the other will be triggered.

So if there's any common denominator to the right sides, then we can infer that "*In Either Case,* Z will happen."

Is there a common denominator to these two right sides? Yes, they both end in people being motivated to become better people / to try to be good.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for something like "when people are hypocritical, it leads to ppl being motivated to try to be better (whether or not that hypocrisy is exposed)".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

