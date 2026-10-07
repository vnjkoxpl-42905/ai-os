-- PT102-S2-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=2 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (should = opinion)$lsat$,$lsat$The color-changing ink should be adopted, rather than microprinting.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Even though the color-changing ink is more expensive, it would allow anyone to detect photocopied counterfeit currency easily.

Meanwhile, microprinting would be easily detected by experts but not by normal people (which is why counterfeits of microprinting often circulate widely before being detected, i.e. those counterfeit bills get used in a lots of different financial transactions before someone realizes the bill is a fake).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We're choosing between Option A (microprinting) and Option B (color-changing ink).

They each have a stated advantage and disadvantage.

Microprinting wins when it comes to being less costly, but loses when it comes to the fact that it's hard for non-experts to detect counterfeit bills when microprinting is the giveaway.

Color-changing ink loses when it comes to being more costly, but wins when it comes to the fact that it's easy for *anyone* (including non-experts) to detect a counterfeit bill.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since we're *Weighing Tradeoffs,* we would want to strengthen by adding another positive to colored-ink, another negative to microprinting, or to hear that the positive about colored-ink outweighs the negative.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT102-S2-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Special ink should be adopted, despite the expense.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$The cheaper alternative, microprinting, allows for counterfeits that circulate widely before being detected (it's easy for experts to detect that they're fakes, but it sounds like it's not so easy for non-experts, which is why it circulates widely).

Special ink would make it easy for non-experts to recognize fakes.$lsat$),(2,$lsat$Goal$lsat$,$lsat$We need some way to argue that special ink *isn't* a good idea. Maybe we could defend microprinting as a better option. Maybe there's a third option we haven't heard. Maybe we can hear something negative about special ink.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT102-S3-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Agriculture did not begin under conditions of drought and hunger (it began when resources were plentiful)$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Agriculture required the active study of natural processes in order to make complex discoveries about how various plants reproduced and grew to maturity. Devoting yourself to the study of natural processes requires leisure, and leisure requires plentiful resources.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Around 50% of all Main Conclusion questions involve a conclusion that is a rebuttal to someone else's thinking. Knowing this tendency helps us to find the conclusion here. "**Although** anthropologists claim X ... " is our signifier that the author is probably trying to rebut their claim.

If we follow that hint, we see that she definitely is doing just that. They have claimed that agriculture began under conditions of drought and hunger, and our author lays out a case that agriculture, based on what it requires, would have to have began during a time of plentiful resources.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that sounds like "agriculture did NOT begin under conditions of drought/hunger, it began when resources were plentiful".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT102-S3-Q18 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=3 AND q.question_number=18 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Less money is being spent on effective treatments of X now than ten years ago.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Only the standard treatments for X are effective,
and
a decreasing percentage of money being spent on treatments of X now than ten years ago.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Let's say we run a business and every month we spend $2000 on advertising -- $1000 is newspaper ads and $1000 is Facebook ads.

We currently spend 50% of our advertising budget on newspaper ads.

If we decide to experiment and add another $1000 into the Facebook ads category, then we'd be spending $1000 on newspaper and $2000 on Facebook.

That means we now spend 33.3% of our ad dollars on newspaper ads.

We now spend a *decreased percentage* of our ad budget on newspaper ads, but do we spend *less money* on newspaper ads?

No, we spend the same amount of money.

The author of this argument is confusing those two things.

The author is making the move from, "If you spend a lower percentage on standard (i.e. *effective*) treatments now, then you spend less money on standard (i.e. *effective*) treatments now."

But we just showed that you can spend a lower percentage on something without spending less money on it.

If we were trying to contradict the author's conclusion, we could say, "we still spend just as much money on effective treatments --- over the last ten years we poured a lot more money into ineffective treatments, so the money we spend on effective treatments is a smaller % of the overall pie, but we haven't reduced the amount of what we spend on effective treatments."$lsat$),(3,$lsat$Goal$lsat$,$lsat$The only wiggle room to this argument is if the overall amount of money spent on treating disease X has gone up (that's the only way that a lower % of a total could still end up equaling at least as big a number as before).

i.e. 50% of a $2000 ad budget was the same as
33.3% of a $3000 ad budget

So to lock in the author's conclusion, we want to hear that the total is the same, or that it's lower than before.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT102-S3-Q19 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=3 AND q.question_number=19 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Setup$lsat$,$lsat$(Unlike steel) when you put glass under pressure, the volume stays the same because glass is a fluid, so it flows to areas under less pressure.$lsat$),(1,$lsat$The Blank$lsat$,$lsat$If you have a horizontal sheet of glass of uniform thickness and you put a really heavy object in the middle of it, then assuming the glass can support the the weight without cracking, the sheet of glass will eventually ______ .$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We need to use the information we were provided about how glass behaves when it's put under pressure, to fill in this blank about what will happen when we put a horizontal sheet of glass under pressure by putting a heavy object in the middle of it.

We were told that when glass is put under pressure, the fluid glass will flow very slowly from areas under sustained pressure to areas under less pressure.

If we put a heavy object in the center of a sheet of glass, then the center will be under sustained pressure, while areas way from the center (like the four corners, for example) will be under less pressure.

So we know that the fluid glass will flow very slowly away from the center of the sheet of glass.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The blank is saying that **eventually** (this is accounting for the *very slow* flow of glass) ... *what* will happen?

Eventually, *the fluid underneath the heavy object will flow away from the center to areas under less pressure*.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT102-S4-Q19 (Unexplained)
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=102 AND q.section=4 AND q.question_number=19 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=4 AND q.question_number=19 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Inez's Conclusion$lsat$,$lsat$If we have our antique objects inspected by professional appraisers who could remove any questionably authentic pieces, people would be more willing to buy antiques at our fair.$lsat$),(1,$lsat$Inez's Evidence$lsat$,$lsat$In these poor economic times, people want to be sure they're getting good value for their money.$lsat$),(2,$lsat$Anika's Conclusion$lsat$,$lsat$No, the inspection by appraisers wouldn't make people more willing to buy our antiques.$lsat$),(3,$lsat$Anika's Evidence$lsat$,$lsat$The customers are already themselves experts, and hiring an appraiser would force us to raise our prices to cover those costs.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$This is neither here nor there, but Inez ... in poor economic times, **why would anyone buy antiques**?! (ok, just had to say it)

Does Anika's response seem like any of our 3 most common moves on Method:
- making / breaking an **Analogy**
- showing the **Faulty Implications** of an Idea
- eliminate / suggesting an **Alternative**

Sure, it seems like the 2nd would apply. Anika is showing how Inez's recommendation would lead to the bad consequence (faulty implication) of needing to raise prices, in order to cover the costs of the appraisers.

Anika's other point is raising an Overlooked Consideration, that the customers are already antique experts so they don't really crave or benefit from an appraiser testifying to an object's authenticity.

She's point out that part of Inez's pitch wouldn't be a compelling upsell for their customer base.$lsat$),(5,$lsat$Goal$lsat$,$lsat$Look for any answer that's descriptively true. It'll probably comment on Anika rejecting Inez's plan by saying it's supposed upside isn't really something their customers would value, or by saying that it comes with a compelling downside (they'd have to raise prices).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=102 AND q.section=4 AND q.question_number=19 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$The anticipated effect of Inez's plan was people to be *more* willing to buy antiques.

Was Anika saying that Inez's plan would lead to people being *less* willing to buy antiques?

Sure. She doesn't explicitly say that, but Anika is saying that Inez's plan would force them to raise prices on their antiques.

Is it common sense to think, "if you raise the price on your antiques, people will be *less* willing to buy it?"

Yes.

(There might be a voice in your head saying, "Not necessarily! Sometimes people are *more* attracted to buying something because the price is higher, like a Fendi bag, or like really expensive wine." Sure, but that's not the typical association. Businesses offer sales and discounts and coupons in order to create demand, in order to make people *more* willing to buy. They don't raise prices to do that, generally.)$lsat$),($lsat$B$lsat$,$lsat$This answer is wicked tempting because "undesirable consequence" is a great match for the Faulty Implications answer we were anticipating.

Anika *did* claim that the plan has at least one undesirable consequence (raising prices).

But she never said the plan would be effective. Effectiveness is measured by whether the Plan achieves its Goal of "making people more willing to buy antiques at the fair".

Since Anika says "I disagree with your prediction", she is saying "I don't think the plan would be effective in making people more willing to buy antiques at the fair".

So that part of the answer is contradicted by Anika's statements.$lsat$),($lsat$C$lsat$,$lsat$Anika doesn't offer any alternative plan. She just points out problems with Inez's plan.$lsat$),($lsat$D$lsat$,$lsat$Nothing Anika says ever touches on whether there would be appraisers available to judge the authenticity of these antiques.

She just says the appraisers are *unnecessary* (since the customers are already experts), not unavailable.$lsat$),($lsat$E$lsat$,$lsat$The only general claim Inez makes is that "in poor economic times, people want to be sure they're getting good value for their money".

A counterexample to that would involve a specific case of poor economic times where someone *didn't* care about getting good value for their money.

Anika doesn't present anything resembling that.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=102 AND q.section=4 AND q.question_number=19;

