-- PT105-S1-Q23 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=105 AND q.section=1 AND q.question_number=23 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (it's clear that / should)$lsat$,$lsat$Farmers who currently till deeply should strive, by using other topsoil aeration techniques, to incorporate no-till methods instead.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Farmers who till deeply are ten times more likely to lose topsoil to erosion than are farmers who use no-till methods.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we hear a Curious Comparison deployed with that familiar correlation language of, "Ppl who are X are **more/less likely** to be Y", we can guess that our author is going to assume a causal connection between the two correlated things.

*Curious Fact ...* how come farmers who till deeply are ten times more likely to lose topsoil than farmers who use no-till methods?

*Author's Explanation ...* the deep tillage is damaging the topsoil (it's deleterious -- i.e., harmful)

We have two baked-in concerns for this template:

1. are there any **Alternate Explanations** for the Curious Fact?
-- *Reverse Cause* (maybe losing topsoil to erosion comes first and causes you to need to deep till)
-- *Third Factor* (maybe there's a type of crop that both requires deep tilling and leads to more topsoil erosion)

2. how **plausible** is the Author's Explanation?
Does deep-tilling have any effect on topsoil? When people switch from deep-tilling to no-till methods, does the loss of topsoil to erosion improve?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Necessary Assumption, we'd primarily assume that the correct answer is going to **rule out** some Alternate Explanation for the curious fact:

- farmers are **not** forced to deep till once they have already lost tons of topsoil to erosion

- the type of farmers whose crops force them to deep till are **not** more likely than those who don't to be dealing with farming conditions that greatly accelerate erosion of topsoil$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT105-S4-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=105 AND q.section=4 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$We urgently need a major tax cut for our upper-income citizens.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The present level of unemployment is the highest ever due to the recession.

A major tax cut for upper-income citizens would lead to a large increase in investment, thereby creating new jobs.

Without this measure, investment will not grow.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The citizen is arguing for a specific solution to counter the effects of the recession, namely by proposing a tax cut. The premise that connects this solution to the desired effect (job creation) is that if upper-income citizens receive tax cuts, they will invest the extra money, thus creating new jobs.

For this argument to hold, the citizen is assuming that tax cuts for upper-income citizens will directly lead to increased investment. Put another way, the citizen assumes that the money saved from taxes will be used in a way that stimulates economic activity.

A potential objection could be that upper-income citizens might choose to save the extra money or spend it on non-investment ventures, which wouldn't create jobs. Therefore, for the citizen's argument to stand, there must be an assumed link between the tax cuts and increased investment.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We need to identify an assumption that explicitly links tax cuts for upper-income earners to increased investment. An answer choice that confirms the reasoning that tax cuts will result in the behavior needed to support job growth (i.e., investing) is crucial.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT105-S4-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=105 AND q.section=4 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$Ideally social science would achieve what all scientific laws hope to achieve: precision and generality.

**However** ...

Laws of social science are often imprecise,
and
Most laws in social science can only be generalized to certain social systems.$lsat$),(1,$lsat$Evaluate / Goal$lsat$,$lsat$This feels like a **Reconcile the Pivot** type of paragraph to me, inclining me to expect a safely worded synthesis of what came before the However with what came after.

So something like, "social science laws are not always able to to embody the ideal virtues of scientific laws".

Wrong answers will probably go over the top and say stuff like "social science isn't a real science".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT105-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=105 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Maude is a hypocrite for her diatribes against people who are materialistic.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$When it comes to the watch her grandmother gave her, Maude is very fond of it, worries about damaging it, and always sets it carefully in a special box before going to bed.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument is essentially calling Maude a hypocrite because she criticizes materialism, yet seems to have a deep connection with a material object: her grandmother's watch. For this argument to stand, we'd need to assume that Maude's fondness for the watch is indeed a sign of materialism. Otherwise, her careful treatment of the watch might just be a form of sentimental attachment rather than materialistic behavior.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want to find an answer that suggests Maude's behavior towards her grandmother's watch makes her materialistic, which would make the charge of hypocrisy make sense. Alternatively, the correct answer could eliminate a way to argue against the conclusion, such as asserting that a sentimental attachment isn't a form of materialism.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S1-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=1 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Introducing permanent economic incentives for water conservation could avoid water emergencies in Springhill.$lsat$),(1,$lsat$Intermediate Conclusion$lsat$,$lsat$Springhill currently discourages conservation.$lsat$),(2,$lsat$Evidence (because)$lsat$,$lsat$Each household pays a flat fee for any amount of water under a usage threshold, and a higher rate only after this threshold is surpassed.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$This argument involves a recommendation: the plan is to introduce permanent economic incentives for water conservation to achieve the goal of avoiding water emergencies. The argument highlights how the current pricing structure discourages conservation because people are incentivized to use less water only after a certain threshold.

That's not exactly *discouraging* conservation, but the author seems to be implying that you only get encouraged to conserve once you cross that threshold and the pricy per liter rates kick in (she must be assuming that most people don't cross that threshold).

To strengthen this argument, we need to emphasize the inefficiency or problems with the current pricing system and illustrate how an alternative approach would provide better motivation for conservation.$lsat$),(4,$lsat$Goal$lsat$,$lsat$Let's identify an answer that reinforces the claim that the current pricing model fails to encourage conservation and that implementing economic incentives would better prevent water emergencies.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S2-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=2 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Background$lsat$,$lsat$There's a little Curious Fact / Explanation feel to this one.

*Curious Fact:* Why is the cape on this painting red on top, but green underneath? (the red paint was added after the painting was completed, and the paint did not come from the artist's workshop.)

*Author's Explanation*: Someone tampered with Veronese's painting. Veronese wanted it to be green, but this mischief maker added red paint on top.$lsat$),(1,$lsat$Art Critic's Response$lsat$,$lsat$She impugns the plausibility of the Author's Explanation.

There's a copy of this painting from right after Veronese died. That soon after an artist's death, a copyist wouldn't dream of tinkering with major features of the work, such as the color of this cape.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The critic is supporting the idea that
*when Veronese died, the cape in the painting was already red. If it had been green, reflecting Veronese's intended color, a copyist working right after Veronese's death would have kept the cape green.*

So, if we think that the cape in the painting was read when Veronese died, does that mean that Veronese wanted it to be red? Did he mix some paint at another studio some time after the painting was initially completed, and add that red cape he'd realized he wanted?

Maybe. Could be that some vandal tampered with the painting during Veronese's lifetime, and Veronese was either uninterested in fixing it or unable to fix it.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since searching for alternate explanations is inherently speculative, we're probably going to see a correct answer that reinforces the idea that either Veronese added the pigment later in life, or the vandalism happened within his lifetime.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S2-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=2 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$John must have worked in the insurance company on Mon - Thurs last week.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If it isn't a national holiday and not a vacation week, then John works five days each week.

Last week was neither a holiday nor a vacation week.

He works four days a week at an insurance company. On Friday he works as a blacksmith.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The evidence establishes that John worked five days last week. And we know that four of those five days involved working at an insurance company. But there's no reason we need to think those four days were Mon - Thu.

First of all, just because John works as a blacksmith on Fridays, he might **also** work at an insurance company on Friday. Nothing in here says he only works one job per day.

Secondly, even if we accepted that John *only* works as a blacksmith on Friday, that still leaves Saturday, Sunday, Monday, Tuesday, Wednesday, and Thursday as the six remaining options for the four insurance days.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The argument is assuming that "if he works as a blacksmith on Friday, he doesn't work at an insurance company on Friday". And it's assuming "John doesn't work on the Sat / Sun".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

