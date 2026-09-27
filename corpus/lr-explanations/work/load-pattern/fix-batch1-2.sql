-- PT102-S3-Q17 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Agriculture did not begin under conditions of drought and hunger (it began when resources were plentiful)$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Agriculture required the active study of natural processes in order to make complex discoveries about how various plants reproduced and grew to maturity. Devoting yourself to the study of natural processes requires leisure, and leisure requires plentiful resources.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Around 50% of all Main Conclusion questions involve a conclusion that is a rebuttal to someone else's thinking. Knowing this tendency helps us to find the conclusion here. "**Although** anthropologists claim X ... " is our signifier that the author is probably trying to rebut their claim.

If we follow that hint, we see that she definitely is doing just that. They have claimed that agriculture began under conditions of drought and hunger, and our author lays out a case that agriculture, based on what it requires, would have to have began during a time of plentiful resources.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that sounds like "agriculture did NOT begin under conditions of drought/hunger, it began when resources were plentiful".$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S3-Q18 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Less money is being spent on effective treatments of X now than ten years ago.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Only the standard treatments for X are effective,
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

So to lock in the author's conclusion, we want to hear that the total is the same, or that it's lower than before.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=3 AND q.question_number=18 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S3-Q19 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Setup$lsat$,$lsat$(Unlike steel) when you put glass under pressure, the volume stays the same because glass is a fluid, so it flows to areas under less pressure.$lsat$),(1,$lsat$The Blank$lsat$,$lsat$If you have a horizontal sheet of glass of uniform thickness and you put a really heavy object in the middle of it, then assuming the glass can support the the weight without cracking, the sheet of glass will eventually ______ .$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We need to use the information we were provided about how glass behaves when it's put under pressure, to fill in this blank about what will happen when we put a horizontal sheet of glass under pressure by putting a heavy object in the middle of it.

We were told that when glass is put under pressure, the fluid glass will flow very slowly from areas under sustained pressure to areas under less pressure.

If we put a heavy object in the center of a sheet of glass, then the center will be under sustained pressure, while areas way from the center (like the four corners, for example) will be under less pressure.

So we know that the fluid glass will flow very slowly away from the center of the sheet of glass.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The blank is saying that **eventually** (this is accounting for the *very slow* flow of glass) ... *what* will happen?

Eventually, *the fluid underneath the heavy object will flow away from the center to areas under less pressure*.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=3 AND q.question_number=19 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S4-Q19 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Inez's Conclusion$lsat$,$lsat$If we have our antique objects inspected by professional appraisers who could remove any questionably authentic pieces, people would be more willing to buy antiques at our fair.$lsat$),(1,$lsat$Inez's Evidence$lsat$,$lsat$In these poor economic times, people want to be sure they're getting good value for their money.$lsat$),(2,$lsat$Anika's Conclusion$lsat$,$lsat$No, the inspection by appraisers wouldn't make people more willing to buy our antiques.$lsat$),(3,$lsat$Anika's Evidence$lsat$,$lsat$The customers are already themselves experts, and hiring an appraiser would force us to raise our prices to cover those costs.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$This is neither here nor there, but Inez ... in poor economic times, **why would anyone buy antiques**?! (ok, just had to say it)

Does Anika's response seem like any of our 3 most common moves on Method:
- making / breaking an **Analogy**
- showing the **Faulty Implications** of an Idea
- eliminate / suggesting an **Alternative**

Sure, it seems like the 2nd would apply. Anika is showing how Inez's recommendation would lead to the bad consequence (faulty implication) of needing to raise prices, in order to cover the costs of the appraisers.

Anika's other point is raising an Overlooked Consideration, that the customers are already antique experts so they don't really crave or benefit from an appraiser testifying to an object's authenticity.

She's point out that part of Inez's pitch wouldn't be a compelling upsell for their customer base.$lsat$),(5,$lsat$Goal$lsat$,$lsat$Look for any answer that's descriptively true. It'll probably comment on Anika rejecting Inez's plan by saying it's supposed upside isn't really something their customers would value, or by saying that it comes with a compelling downside (they'd have to raise prices).$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=4 AND q.question_number=19 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

UPDATE lr_explanation_choice_notes n SET body=v.b FROM (VALUES ($lsat$A$lsat$,$lsat$The anticipated effect of Inez's plan was people to be *more* willing to buy antiques.

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

Anika doesn't present anything resembling that.$lsat$)) v(l,b), lr_explanations e, lr_questions q WHERE n.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=4 AND q.question_number=19 AND e.style='single' AND n.letter=v.l AND n.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S4-Q6 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Curious Fact$lsat$,$lsat$Why does the male inflate its air sac and display it to the female, during the courtship ritual?$lsat$),(1,$lsat$Hypothesis$lsat$,$lsat$It's so the female can select healthy mates.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The most common way to strengthen a hypothesis is to add plausibility to the causal story the author is telling. We'd love to hear that displaying air sacs is a way for a female to select healthy mates. We'd love a "no cause, no effect" answer that suggests that "when a female isn't trying to inspect the health of mates, the males don't inflate their air sacs".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that supports the plausibility that inflated air sacs help a female to determine how healthy a male is, (or an answer that rules out an alternate explanation for why the male inflates its air sacs during the mating ritual, like "it's NOT to make himself look bigger than other males".)$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=4 AND q.question_number=6 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT103-S1-Q3 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion (Therefore)$lsat$,$lsat$A piece of candy with x amount of refined cane sugar is no higher calorie than a piece of fruit with x amount of fructose.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The number of calories in a gram of refined cane sugar is the same as in a gram of fructose.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$*Given that* a gram of refined sugar has the same caloric content as a gram of fructose,

*How could we argue that* a piece of candy with x grams of refined sugar **does** have more calories than a piece of fruit with x grams of fructose?

Well when it comes to the head to head battle of refined sugar vs. fructose, we know they're tied in calories.

But could the candy have other ingredients (fat? carbs? protein?) that also adds calories that the fruit doesn't have?$lsat$),(3,$lsat$Goal$lsat$,$lsat$This is basically a *Part vs. Whole* flaw, since the argument is thinking that since the "sugar part" of the candy/fruit would have the same calories, the candy/fruit "overall" would have the same calories.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=103 AND q.section=1 AND q.question_number=3 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

