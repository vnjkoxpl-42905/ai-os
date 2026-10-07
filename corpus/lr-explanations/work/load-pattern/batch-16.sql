-- PT116-S3-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=3 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$It is likely that these cave dwellers engaged in activities similar to rodeo riders (chasing and tackling animals).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The skeletal fractures these cave dwellers had are most like the type and distribution of fractures sustained by rodeo riders.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$Most of the time on Principle-Strengthen, we just want to prephrase an "If Premise, Then Conclusion" linking idea, so we'd be looking for something like,

"If your skeletal fractures are most like those of rodeo riders, then you probably engaged in activities similar to rodeo riders".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT116-S3-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=116 AND q.section=3 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$Only people with high blood pressure or those who can't process extra sodium need to restrict their sodium intake.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$For people with normal blood pressure, extra sodium doesn't significantly raise blood pressure because it is excreted by the body.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We can apply our usual Weaken template to this.

GIVEN THAT people with normal BP excrete extra sodium before it raises their BP,

HOW CAN WE ARGUE THAT these people *should* still restrict their sodium intake?

Maybe there's some other potential negative effect of sodium consumption that doesn't relate to blood pressure.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer that introduces a reason why people with normal blood pressure might also need to be cautious about sodium intake.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT117-S2-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=2 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$The arrival of humans dramatically decreased the bird population in terms of both number and diversity on the island.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Soil studies show that for the last 3,000 years, since humans arrived, the bird population is less numerous and less diverse compared to the previous 80,000 years.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We can apply the Explain Curious Fact template to this, since we have a conclusion making a causal claim about non-causal evidence.

CURIOUS FACT: How come there was a larger and more diverse population of birds on Tinga before humans arrived?

EXPLANATION: When humans arrived, their activity reduced the number and variety of birds.

To weaken, we either introduce an alternate explanation for the decline in birds or undermine the plausibility of the human causation theory.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer choice that provides an alternate cause for the decline in the bird population, or that debunks the story that human arrival is responsible.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT117-S3-Q16 (Unexplained)
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=117 AND q.section=3 AND q.question_number=16 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=3 AND q.question_number=16 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (hence)$lsat$,$lsat$A retailer's success need not depend on excellence in both convenience and variety.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Many successful retailers excel in only one of the two areas, and are average for the other.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We can probably get away with a conversational summary of this argument since it's build on only one premise.

The argument is saying, "You don't need to be great at both, because there are many examples of things that are only great at one of them"

If we want a little more formality, the conclusion needs the form,
"X doesn't depend on being great at both Y and Z"

And the evidence needs the form,
"there are many examples of X where is Y is great and Z is average, or vice versa".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's start by looking at conclusions, because if they don't have that vibe of "X doesn't depend on Y", then they're hopeless.

Technically, the argument doesn't need to mimic the idea of "great at both".

At its essence, it's saying
"X doesn't depend on Y. After all, there are examples of X without Y."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=3 AND q.question_number=16 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$The conclusion *does* look like a good match for
"X doesn't depend at being great at Y and Z".

*Being a long distance champion doesn't require being great at speed and endurance.*

Now we just need to make sure there is a premise that says there are examples of long distance champions who either weren't great at speed or weren't great at endurance.

Indeed, it tells us that
*Some long-distance champions were only great at speed, or were only great at endurance.*

Looks pretty good. It has the same logical essence as the original:
"X doesn't require Y. After all, you can find X without Y."

We might notice a couple superficial differences and keep checking out other answers to see if there's a better match.

OTHER MATCHING LAYERS
This also began with a counterpoint that matches the original. That wasn't necessary for the logic of the actual argument, but it does make (A) even more similar.

MISMATCHING LAYERS
- the premise here is about SOME counterexamples, whereas the original premise is about MANY counterexamples. That's not logically important, since you only need one counterexample to prove that "X doesn't **need** Y", but it is different.

- the premise establishes that they are *not* great at both, like the original. But the original also said that they were average when it came to the not-great trait. This one doesn't say that. Again, not logically important, because the logic comes from the fact that they are champions, even though they are not great at both things. It doesn't actually matter if they're terrible at either thing or just average. As long as we know they're not great at both, it serves the same purpose.$lsat$),($lsat$B$lsat$,$lsat$We don't need to examine this one beyond its conclusion. It is not making a claim of the form "X does not require Y".

Its conclusion says
"Most X's are ~Y"$lsat$),($lsat$C$lsat$,$lsat$We don't need to examine this one beyond its conclusion. It is not making a claim of the form "X does not require Y".

Its conclusion says
"Anything that is X is almost certainly Y"$lsat$),($lsat$D$lsat$,$lsat$This does have a conclusion the form "X does not require both Y and Z".

*best eating apples don't need to be both Firm and Flavorful*.

That means we're checking for a premise that shows at least one example of an apple that was best for eating that was either ~Firm, ~Flavorful, or both.

We do see a premise saying
"many flavorful apples that are soft (~Firm) are suitable for eating"

Hmm, close, but "best for eating" is different than "suitable for eating".

Also, the evidence is only providing examples of Flavorful but Not Firm. It doesn't also point to examples of Firm but not Flavorful.

In the original and in (A), the premise was saying there are examples of each of the two traits appearing without the other one being present.

If we didn't catch that discrepancy, we could also notice the premise
*- Flavor is required for eating*
and think, "The original never said that either of the two traits *was* required."

We could also hate on the initial counterpoint. If it were going to match the original, it would sound more like,
*Apples that are neither really firm nor really flavorful tend to not be the best for eating.*

This one is instead talking about baking.$lsat$),($lsat$E$lsat$,$lsat$The conclusion isn't quite of the form "X does not require Y".

Its conclusion says
"Not all X's and Y's are Z's"

If we were being really charitable, we could say that this is just a paraphrase for, "being X or Y doesn't require Z".

But we don't need to be charitable since we have (A), which doesn't require any translation.

This argument does validly prove its conclusion, because it does provide counterexamples where something is X or Y without being Z.

But it's way less similar to the original than (A).
(A) focused on the idea of "you don't need to be great at both. Here are counterexamples where they're only great at one."

That's way closer to the original argument than, "Not all X's and Y's are Z. There are examples of X's and Y's that are not Z."$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=117 AND q.section=3 AND q.question_number=16;

