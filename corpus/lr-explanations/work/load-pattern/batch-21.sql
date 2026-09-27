-- PT122-S2-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=2 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*Quantifiers / Conditionals* (most, no, all)

Any time we have a mix of quantified claims and conditionals, we want to prioritize conditionals.

Happy → Time for
entrepreneur Leisure

Work at → No time for
least 18hrs Leisure

These both have the concept of "time for leisure", so we should see whether they chain together. If we contrapose either one, we can chain them together.

Happy → Time for → Work less than
entrepreneur Leisure 18 hrs / day

Then we get our *Most* claim.

*Most* successful *are* Work at least
entrepreneurs 18 hrs / day

The overlapping term is whether you work at least 18 hrs. We'll have to contrapose our chain so that it's starting from "Work at least 18".

Work at → No time for → Not happy
least 18hrs Leisure entrepreneurs$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$So since we know that "Most *Successful Entrepreneurs* work at least 18 hrs a day", we know the other two ideas on this chain as well:

Most successful entrepreneurs have not time for leisure.
Most successful entrepreneurs are not happy.$lsat$),(2,$lsat$Goal$lsat$,$lsat$The correct answer to Must Be False almost always either contradicts a conditional relationship we're given or contradicts an inference we can derive.

So we might see our inferences contradicted:
- Most successful do have leisure time
- Most successful are happy

Or we'll see our conditional chain contradicted:
- Someone works at least 18, but is happy.
(for example)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S2-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=2 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$Establishing that nonhuman animals are intelligent will not establish that they have consciousness.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Humans can exhibit complex, goal-oriented behavior without conscious awareness of what they're doing.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Very confusing conclusion, so we need to think about what it's saying and what our burden of proof is, if we were trying to convince a courtroom that the conclusion is true.

"Merely establishing X will not establish Y". What's another way to say that?

"X does not prove that Y is true"
"X is not sufficient to prove Y"

This conclusion is refuting a conditional. It's saying that X --/--> Y.

To refute a conditional you prove that it's possible for the trigger to be true while the outcome isn't. To prove that "knowing X does not mean you know Y", we would need an example where X is true but Y isn't.

To prove that "knowing *intelligent* doesn't mean you know *consciousness*", we would need an example where *Intelligence* is happening but *consciousness* is not.

When we look at the evidence, has the author presented a data point showing that sometimes *Intelligence* is present but *Consciousness* is not?

He presented a data point where,
*Complex, Goal-Oriented behavior* is present but *Conscious Awareness* is not.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The author is treating "complex, goal-oriented behavior" as a proxy for "intelligence", so he must be assuming that this complex, goal-oriented behavior is intelligent behavior.

If we felt very lost on this problem, we could guess that the correct answer will talk about "intelligent", because that's a *New Term in the Conclusion*.

And because "consciousness / conscious awareness" is mentioned twice, we don't need to be looking for that idea in the answer. We need to link "intelligent" to whatever idea is linked to "conscious awareness".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S2-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=2 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (this suggests that)$lsat$,$lsat$The violence in video games leads young children to believe aggressive behavior is acceptable.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Young kids tend to behave more aggressively right after playing a violent video game.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is an Explain Curious Fact style argument, with a non-causal comparison in the evidence ("tend to behave **more** aggressively"), i.e. a Correlation / a Curious Fact.

And the conclusion introduces a causal claim: "violence in these games **leads** young children ..."

CURIOUS FACT: why are kids behaving more aggressively right after playing a violent video game?

EXPLANATION: the violence in the game teaches them that violence is acceptable, so they start acting more violently toward

Strengthening can occur by ruling out alternate explanations for the curious fact or making the author's causal story more plausible.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find four answers that strengthen, either by ruling out an AlterFind the answer choice that does not strengthen the argument, possibly identifying one that has no impact or weakens the causal claim that video game violence makes aggressive behavior seem acceptable to children.$lsat$),(4,$lsat$Conclusion$lsat$,$lsat$Choice B is the correct answer, as it neither supports nor strengthens the argument's claim. Instead, it implies that kids may already find aggression acceptable, thereby failing to connect violent video games as a new cause for this belief. The other answers strengthen the argument by reinforcing or adding plausibility to the causal explanation.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S2-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=2 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Curious Fact$lsat$,$lsat$Why does the cattle egret live around herds of cattle?$lsat$),(1,$lsat$One Explanation$lsat$,$lsat$As the cattle graze, it stirs up insects that the egret can eat.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is an interesting question stem, in that it looks like Weaken, but we're not trying to weaken anything in the stimulus. We just need an additional explanation for why for why cattle egrets follow herds.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer choice that offers a different explanation for the presence of egrets among cattle herds.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S2-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=2 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$Any fruit that was inspected is safe to eat.

*Inspected ------------------------> Safe*$lsat$),(1,$lsat$Evidence$lsat$,$lsat$*Inspected ---> ~Infected*$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The "therefore" shows us the claim we're trying to prove. On Sufficient Assumption, there are two big questions we can ask about the Conclusion:

1. Is there any New Term (that isn't ever discussed in the evidence)?

2. Can I / should I write this conclusion as a "long conditional"?

When it comes to #1, yes, there was a New Term in the conclusion that was never discussed or defined in the evidence: *safe to eat*.

So it's a guarantee that the correct answer will have to say "safe to eat" or something equivalent. After all, the correct answer combines with the evidence and allows us to derive the conclusion.

If you had all these claims,
a = b
b = c
c = d
you could never derive the claim
a = x
because we don't have any givens about "x".

When it comes to #2, we're motivated to write the conclusion as a long-conditional so that we can better see the missing piece we need.

The conclusion is one big logic path we're trying to build.
*Inspected ----------------------------------> Safe*

The evidence and the answer we pick are the building blocks for that logic path. The one premise we have is this:
*No fruit that was inspected is infected*.

The other statement, "if infected, then rotten" is irrelevant to our conclusion. Our conclusion is about **inspected** fruit, and none of the inspected fruit is infected. So that first sentence is what you might call a "Fake Premise". It looks like it could be relevant, but it has nothing to do with our conclusion.

So how do we turn our one premise (the 2nd sentence) into a conditional?

**No A's are B = All A's are ~B = A → ~B**
No inspected are infected = All inspected are not infected
*Inspected → ~Infected*

We're trying to prove this,

*Inspected ----------------------------------> Safe*

and this is what we have so far

*Inspected ----> ~Infected*

So what are we missing?
*~Infected ---------------> Safe*

If you want to do this problem more conversationally, then just work backwards from the conclusion. You're trying to prove that "anything inspected is safe".

What were we told about stuff that was inspected?
We were told that it **isn't infected**.

What were we told about stuff that **isn't infected**?
Nothing.

So we know that a possible answer could be
"if **isn't infected**, then **safe to eat**"$lsat$),(3,$lsat$Goal$lsat$,$lsat$We're looking for

"if **isn't infected**, then **safe to eat**"

but since we know that Sufficient Assumption loves to hide the correct answer via contrapositive, we should also look for
"if it's **isn't safe** to eat, then it is **infected**"$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT124-S2-Q19 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=124 AND q.section=2 AND q.question_number=19 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Renting cars from dealerships rather than national firms is generally more worthwhile for locals than tourists.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The dealership is cheaper than the national firm for everybody, but for tourists to take advantage of dealership rates, they'd have to know which dealerships offer rentals, and they'd have to pay for taxi rides back and forth from airport to dealership.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$If you were trying to object to this, you might say "Can't tourists just look up which dealerships offer rentals online or by calling them up?" or "Is the rental so much cheaper that it's more than worth it to pay for the taxi rides?"

So to strengthen the argument, we would try to rule out those objections or present new facts that agree with the Conclusion.

Because the conclusion is comparative, we're also **Assuming a Difference** when it comes to locals. We have to assume that "THEY find it easier to determine which dealerships offer rentals" and "THEY don't have to pay taxi-fare levels of costs in order to get themselves back and forth from the dealership".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for "it's hard to determine which dealerships offer rentals", "the savings on the rental is matched or exceeded by the taxi fare", "locals don't have the same challenges when it comes to determining which dealerships rent cars or when it comes to transporting themselves to/from dealership", or anything else that agrees with the Conclusion.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT124-S2-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=124 AND q.section=2 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Therefore)$lsat$,$lsat$There are some days in Hillview when the wind blows from the east and the smog reaches unsafe levels.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$On some hot days in Hillview, the wind blows from the east.
On some hot days in Hillview, the smog reaches unsafe levels.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Because both premises and the conclusion are quantified *Some* claims, we might want to think about *Trait Overlap* inferences:

Some A's are B Most A's are B
All A's are C Most A's are C
**infer: Some B are C Some B are C**

There aren't any trait overlap inferences where you combine two Some facts about the same group.

I can say "Some men are U.S. Senators" and "Some men live in Mongolia", and that doesn't allow us to infer that Some U.S. Senators live in Mongolia.

*Some* is a very weak quantifier that means "at least one".

There was at least one hot day where the wind blew from the east. There was at least one hot day where the smog reached unsafe levels.

Does there have to be a day when both things occurred?

No, maybe eastern wind happened on Monday and unsafe smog happened on Thursday.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying we can't prove an overlap between "unsafe smog" and "eastern wind", since it's entirely possible that those two things happened on different hot days.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

