-- PT115-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=115 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$With the arrival of interactive television, obesity among North American school-age children will increase.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Among North American school-age children, there is a strong positive correlation between obesity and the amount of television watched.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we see a correlation presented in the evidence,
*X is correlated with Y*
*ppl who are X are more likely to be Y*
*ppl who are X tend to be Y*
we anticipate that the author will assume that X causes Y (or vice versa).

Here, there was a correlation between obesity and TV watching. Is the author assuming that one causes the other?

Yes, we can tell from her conclusion that she thinks that TV watching causes obesity, because she thinks the arrival of more TV will lead to more obesity.

*Correlations* are the most famous of all Curious Facts (asymmetric comparisons). We know that when author's state or assume a causal explanation for a curious fact, we're primarily supposed to ask ourselves about *Alternate Explanations*.

When an author sees that X and Y are correlated and starts acting like X causes Y, we're supposed to automatically think:
1. Could it be **Reverse Cause** (Y causes X)?
2. Could it be a **3rd Factor** (Z causes X and Y)?

#1 would be saying "Hey maybe the obesity came first and it led to more TV watching because it made exercising harder".

#2 would be saying something like, "Hey maybe there's some underlying condition like working class income, that leads to cheaper junk food that makes us obese and leads to more TV watching because the parent(s) is constantly working and can't afford childcare".

However, there's also a *New Concept in the Conclusion*, this "interactive television", and the author is making a *Prediction*.

What if "interactive television" is meaningfully different from other television? Maybe kids won't like it, so they won't watch any additional TV as a result. Maybe the interactiveness will actually burn calories so it will combat obesity.$lsat$),(3,$lsat$Goal$lsat$,$lsat$A correct answer could rule out an alternate explanation for the correlation.

Or it could rule out a possible objection that interactive TV will be unlike regular TV, in terms of school-age children watching lots of it and becoming obese.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S2-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=2 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$Moral socialization has had a net effect of increasing the total amount of suffering.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Moral socialization works by making children feel ashamed of immoral behavior. In many people that shame produces deep guilt and self-loathing, which can be a severe hardship.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$If we're going to try to argue that *moral socialization has a net effect of reducing total suffering*, we're going to have to counteract the author's evidence which speaks to ways in which moral socialization causes suffering.

Maybe, when the parents are shaming their kids for immoral behavior ("Billy! It was wrong for you to hit all those other kids with the hockey stick. You hurt them!"), the shaming makes Billy suffer, but then he stops hitting the other kids at school with a hockey stick.

It would seem in a case like that like even though Billy's suffering went up, everybody else's suffering went down, and so moral socialization had the net effect of reducing suffering.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer getting at this idea that moral suffering might also reduce suffering in ways the author failed to account for. The evidence for "net effect" is incomplete if you only mention ways it increases suffering but never weigh that against ways it decreases suffering.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S2-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=2 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Therapists who deal with violent criminals can't simultaneously respect their clients' right to confidentiality *and* be sincerely concerned for the welfare of future victims.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Reporting a client's unreported crimes would violate the client's trust that what they say to their therapist is confidential.

And failing to report a client's unreported crimes would leave the client out of prison, free to commit more crimes.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The conclusion is very harshly worded. It's saying that X is impossible, so to prove this dude wrong, we'd only need to come up with one instance in which X is possible.

Can we think of a scenario in which a therapist who treats violent criminals could manage to both respect the client's right to confidentiality while also showing real concern for potential future victims, were that client to remain out of prison.

The premises are framed as an *Binary*.

The therapist either reports the violent crimes she learns about from her client or she remains silent about them (doesn't report them).

The author thinks that *In Either Case*, the therapist has failed to do one of the two things that supposedly can never co-exist. We would need to think of way where in one of those two words, the therapist could still manage to do both things.

When a therapist **does report the crimes** of their client, could they still be respecting confidentiality and also looking out for future victims? They're definitely looking out for future victims, but it's hard to say they're respecting confidentiality. If you tell the cops what you know, you have failed to keep what you know confidential.

When a therapist **does not report the crimes** of their client, could they still be respecting confidentiality and also looking out for future victims? They're definitely respecting confidentiality. Could they still be looking out for future victims? Maybe. Maybe they don't consider their client dangerous to future victims? Their violent crime was a crime of passion, not a symptom of a dangerous person?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that helps us argue that a therapist could simultaneously keep a client's crimes a secret while still showing proper concern for potential future victims, were that client to remain out of prison.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S2-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=2 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$Don't take preventive measures Soil
and → nutrients
Don't rotate crops depleted

Soil nutrients totally depleted Crops can't
and → be grown
no fertilizer added

Fertilizer → more vulnerable → must use
used to pests pesticides

All other things being equal,
more fertilizer, more vulnerable to pests, more likely treated with pesticides, worse for human health.$lsat$),(1,$lsat$Question Stem Fact$lsat$,$lsat$This question stem provides one starter fact … the veggies were grown without fertilizer.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Does anything get triggered by the fact they were grown without fertilizer?

The fact that there was no fertilizer means the crops didn't *need* pesticide. They were presumably less vulnerable to pests / less likely to have been treated with pesticides.

The fact that they were grown at all triggers one of the two contrapositives.

Crops can soil nutrients **not** totally depleted
be grown → or
fertilizer was added

And since we know that fertilizer was NOT added, we know which part of that outcome would have to be true.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since these crops were grown (and fertilizer was not added), it must be the case that the soil nutrients were not totally depleted.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S2-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=2 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Claim$lsat$,$lsat$Increasing the prison term for robbery won’t discourage people from committing robbery.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$There's no argument to grapple with. It's just one solitary claim.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Get rid of the four answers that help us argue that increasing the penalties for robbery won't do much, if anything, to discourage people from robbing.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S3-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given that ...$lsat$,$lsat$The sun, throughout Earth's history until about 2 billion years ago, was 30% dimmer$lsat$),(1,$lsat$and that ...$lsat$,$lsat$Nowadays, a sun that dim would lead to frozen oceans$lsat$),(2,$lsat$Why is it that ..$lsat$,$lsat$3.8 billion years ago, there was liquid water?$lsat$),(3,$lsat$Evaluate / Goal$lsat$,$lsat$There must be something *else* that was also different about the Earth back then that would allow a dimmer Sun to still warm the Earth enough to keep water in its liquid state.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S3-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=3 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Background$lsat$,$lsat$They lowered the personal income tax rate by 2% each of the last two years.$lsat$),(1,$lsat$Surprising Thing$lsat$,$lsat$In the first year of lowered income tax rate, the overall personal income tax collected was the same as before.
In the second year of even-lower income tax rate, the overall personal income tax collected went up a bunch.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$*GIVEN THAT* ...
the personal income tax rate got lowered 2% in each of the last two years,

*HOW CAN IT BE THAT ...*
total money collected from personal income taxes stayed same and then went up a bunch last year?

4 answers will explain how that could be. 1 will be irrelevant or make the paradox more surprising.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S3-Q25 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=3 AND q.question_number=25 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evidence (for)$lsat$,$lsat$Good things cause no harm X → ~Y

Wealth is often harmful. W is often Y.$lsat$),(1,$lsat$Conclusion$lsat$,$lsat$Wealth is not a good thing. W is ~X.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Because this argument has repeating ideas (wealth / good things / harmful), it's conducive for putting into an algebraic recipe.

But we could also just say to ourselves "A contrapositive argument structure", if we know what that means.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want two premises that feel something like this:
- All X's are Y
- This thing isn't Y

And a conclusion that then validly concludes the opposite of the original trigger:
- This thing isn't X.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

