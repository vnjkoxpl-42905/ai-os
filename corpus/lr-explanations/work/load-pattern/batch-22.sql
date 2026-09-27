-- PT124-S2-Q21 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=124 AND q.section=2 AND q.question_number=21 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given that ...$lsat$,$lsat$Workers in this industry know that "strikes during poor working conditions are usually followed by much better working conditions five years later".

And given that working conditions are poor.$lsat$),(1,$lsat$Why is it that ...$lsat$,$lsat$They refuse to strike?$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We'd think that these workers would want to strike, thinking that the usual "result" of striking is improved working conditions five years later.

But maybe that improvement is a coincidence. It's a fact that working conditions are improved, not that the *strike* played a causal role in improving them.

And it's only *usually* the case that strikes are followed by improvement. Maybe these workers think that their current situation is more likely to play out like the minority of times in which a strike doesn't lead to better conditions.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for a reason they don't want to strike:
- a bad thing about strikes
- they don't think strikes will cause improvement
- something special is occurring that makes them think THEY wouldn't have good luck with a strike
- or something else$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT124-S2-Q26 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=124 AND q.section=2 AND q.question_number=26 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Increasing the speed limit 10-20% in order to better match the actual average driving speed of people would greatly decrease highway safety.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Even though the people currently speeding would probably obey the new law, the people currently obeying the slower speed limit would increase their speed to the new, faster speed limit.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This author is making a **Prediction**, comparing what would be the case in this hypothetical Plan-World with what is the case in Current-World.

Predictions are always inherently comparisons, and with comparisons we think about other ways in which two things might be similar or different.

**Current-World Plan World**
*Speed*
*limit* 55mph 70mph

*Rule* drive drive
*breakers* 70mph 70mph

*Rule* drive drive
*followers* 55mph 70mph

**Author's** more highway less highway
**prediction** safety safety

The only difference between the two worlds is that the law-abiding drivers speed up. So if we're fighting this argument, we're thinking,

*Given That*
*...* the law-abiding drivers will speed up,
*How Can We Argue That*
... the highways **won't** be less safe?$lsat$),(3,$lsat$Goal$lsat$,$lsat$The author is assuming that because we've increased the average speed of highway drivers, we've made things more risky (which is a reasonable assumption). We need to counter that effect by saying that *something else* matters to this prediction, or that something else will be different in Plan-World that will help highway safety.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT126-S3-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=126 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evidence$lsat$,$lsat$Many Prospective buyers of ALAI
homes for sale are likely to
**assume that large**
**appliances in the home**
**would be included** with its
purchase.$lsat$),(1,$lsat$Conclusion$lsat$,$lsat$Sellers who will be keeping MO
the appliances are **morally**
**obliged** either to remove
them before showing the
home or to indicated in
some other way that the
appliances are not
included$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument assumes that ALAI → MO
if some people would
**assume the appliances**
**would be included** with the
sale of the home, then the
seller is **morally obliged** to
remove them before showing
the home or indicate in some
other way that the appliances
are not included.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT126-S4-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=126 AND q.section=4 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Consumer price increases have not averaged less than 3% over the past year.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Gas is up 10%. Auto insurance, 12%. Papers, 15%. Propane, 13%. Bread, 50%.$lsat$),(2,$lsat$Evaluation$lsat$,$lsat$Well the author has definitely convinced us that *some commodities* have gone up by more than 3% over the past year, but the claim he's fighting is about whether consumer prices *on average* have gone up 3% or more.

We could potentially call this flaw a **Sampling** flaw, because the author's sample of goods might be highly unrepresentative in terms of average price increases.

We could also maybe call it **Part vs. Whole**, since the author is thinking "since these individual commodities have gone up by more than 3%, it must be that commodities overall have gone up by more than 3%".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something saying, "Those are just a few items you may have cherry-picked to prove your point, author. But we're talking about averages, so maybe those dramatic upticks are offset by a lot of products that barely went up, stayed, the same, or even got cheaper."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT126-S4-Q23 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=126 AND q.section=4 AND q.question_number=23 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Superheated plasma with failed electrical resistance is never a factor in causing ball lightning.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If superheated plasma with failed electrical resistance were a factor in causing ball lightning, then that lightning would emit intense light and would rise in the air.

But the instances of ball lightning I've seen were of low intensity and floated horizontally before vanishing.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This stimulus is written to make our brains turn into applesauce. We need to chunk down "superheated plasma in which electrical resistance fails" into one idea, X.

We need to also recognize the rebuttal structure of the argument. Authors often refute a certain claim by saying, "If it were true, it would imply this 2nd thing. Since the 2nd thing isn't true, the original claim must not be true".

When authors say something like, "If this *were* true ...", we call it **Implications of Logic**. The right side of a conditional is the *implication* of the left side. Authors go on to tell us that the implication is untrue / absurd / unacceptable, in order to rule out the original trigger idea, via **Contrapositive Logic**,

The argument looks like this:

*Some scientists claim X is a factor in causing Y.*
*If X were a factor is causing Y, then A and B would follow.*
*But when I saw Y, there was ~A and ~B.*
*Thus, X is never a factor in causing Y.*

The contrapositive logic checks out. The real gap between the evidence and the conclusion is that the evidence is about "the instances of ball lightning that I observed", whereas the conclusion is about "never a factor, in any instance".

We are logically sure that that X was not a factor in the ball lightning that the author observed (because neither of the symptoms of such an occurrence, intense light and rising in the air, were present.

But we can't be logically sure that X is **never** a factor in causing ball lightning, because we don't know whether the instances of ball lightning the author observed are representative of all cases of ball lightning.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We need to get from "If X (hot plasma etc.) wasn't a factor in causing the ball lightning that the professor has observed, then X is **never** a factor in causing it."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT127-S1-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=127 AND q.section=1 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$For some consumers, front-loaders are superior (to top-loaders).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Front-loaders have the controls and access in front, which is more convenient for wheelchair users, who also find it inconvenient to remove laundry from top-loaders.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The conclusion has a very modest goal: it's only trying to prove that for **at least some** consumers, front-loaders are superior.

The author is building the case that for some wheelchair users, front-loaders are superior.

Why? Front-loaders have the controls and access in front.
*The author assumes a difference, that top-loaders do not have control and access in front.*

Also, wheelchair users find it highly inconvenient to remove laundry from top-loaders.
*The author assumes a difference, that wheelchair users do not find it highly inconvenient to remove laundry from front-loaders.*

Beyond those assumed differences, can we think of any objections to this argument?

*Given that ...* wheelchair users would have controls and access in front and might find it less inconvenient to remove laundry,

*How could we still argue that ...* top-loaders are superior, even for these wheelchair users?

We'd have to go into *Net Gain / Loss* mode and argue that even though front-loaders have these stated advantages over top-loaders, top-loaders have other advantages over front-loaders that make them at least as good an option for wheelchair users.

We are helped by the opening opposing idea, which tells us that top-loading washers are superior overall. Maybe they get clothes cleaner while using less water and are much more affordable. That could be enough for a wheelchair user to still make a top-loader a superior option.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer staying one of the assumed differences (top-loaders don't have controls/access in front ... it's *not* highly inconvenient for wheelchair users to remove clothes from a front-loader).

Or look for an answer ruling out the idea that *other* aspects of washing machines (how well they clean / how much they cost / how much water they use) do not make top-loaders the better overall choice, even for wheelchair users.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

