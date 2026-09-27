-- PT147-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=147 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Unemployment will soon decrease.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If total govt spending significantly goes up, unemployment will decrease.

If total govt spending significantly decreases, unemployment will decrease.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We ascertain that the first claim is the conclusion by seeing that the other two claims are clearly meant to work together. Conjunctions/connections like "and / but / on the other hand" show us that two claims are interacting together to move the argument forward.

Each of the conditional premises involves TWO consequences, one of which is decreasing unemployment. I didn't bother writing out the other half of each outcome, because all we care about is proving that there will be decreasing unemployment.

At first, this argument seems pretty reasonable. It seems like an *Either Way You Slice It* style of argument: "Whether spending increases significantly or decreases significantly, we end up with decreasing unemployment. So either way you slice it, we're gonna have decreasing unemployment."

But we know that an argument on Sufficient Assumption can't *already* be airtight. There has to be some gap, so that the correct answer can make it airtight.

How would unemployment *fail to decrease*?

Well, I guess spending doesn't necessarily have to go significantly up or significantly down. It could more or less stay the same.

The author is presenting a *False Choice* (a false binary / a false dichotomy), acting like spending will either go up a bunch or down a bunch.

But she's failing to consider the middle ground, where spending basically stays the same.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We just need to rule out the possibility that govt spending will stay basically the same. We need to know that it'll definitely go up or down significantly.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT147-S4-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=147 AND q.section=4 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Marisa's Conclusion$lsat$,$lsat$Zoning regulations must be loosened$lsat$),(1,$lsat$Marisa's Evidence$lsat$,$lsat$In some places, the restrictions on development are so prohibitive that it's significantly reducing the property values of undeveloped areas.$lsat$),(2,$lsat$Tyne's Conclusion$lsat$,$lsat$Zoning regulations don't need to be loosened.$lsat$),(3,$lsat$Tyne's Evidence$lsat$,$lsat$The value of natural, undisturbed areas can only be better preserved by such regulatory protection.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$What part of Tyne's response seemed weird or off-topic? To me it was the "natural, undisturbed" areas.

It sounds like Tyne is talking about regulations that prohibit developing in a wilderness refuge, or on endangered wetlands, or something like that.

Marisa seemed to just be saying, "you know that empty plot of land southwest of the Wal-Mart? It should have a pretty high property value, but because the zoning regulations are so strict, developers can't really build what they want or how they want there, and thus the value of that land is plummeting.$lsat$),(5,$lsat$Goal$lsat$,$lsat$I would go looking for an answer that speaks to the difference between "undeveloped areas" (an empty lot that developers would like to put apartment buildings on but can't because of zoning regulations) and "natural, undisturbed areas" (precious parts of the natural ecosystem that we don't want to touch".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It's imperative that we adopt the alternate code.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The alternate code has been successfully used elsewhere for several years.

Even though the current code is entrenched and widely accepted, the current code contains tons of obscure rules, which cause us to forever debate tiny details. Meanwhile the public thinks we suck, and we can't be successful if the public lacks confidence in us.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$A lot of arguments that **assume a difference** have this form: "X is kind of bad for reason Y. Thus, we should use Z instead of X."

This type of argument **assumes** that Z is **different**, in terms of reason Y.

Similarly, in this argument, our author is definitely assuming that this alternate code does **not** contain a comparable amount of obscure technicalities that will lead to ineffective quibbling over details. But maybe the alternate code is just as riddled with parliamentary complexities.

If we want to think beyond just that one possible objection, we can frame this with our Objection Mindset:

*Given that ...* this (widely accepted) code leads to endless arguing over tiny details, eroding the public's precious trust in the effectiveness of the council,

*How could we say that ...* we don't **need** to adopt the alternate code (there's some other option).

Well first of all, we could ask, "Are there only these two codes to choose from? Why I do I have to go from this traditional one to the alternate one?"

We could ask, "Is it feasible to make the switch? Could we just fix the current code we have and get rid of the excess technicalities we hate? Could we just live with no code at all?"

Since the author's conclusion goes out on a limb of, "It's *imperative* that we switch to the alternate code", we will be creating some weakening doubt with any storyline that makes it seem like we could keep the existing one or that we could choose a path other than adopting the alternate one.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something saying "the alternate code is just as bad when it comes to procedural details we'd fight over" or just as bad when it comes to "losing public confidence", or an answer suggesting an alternate viable path that shows we don't *need* to adopt the alternate code.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given that ...$lsat$,$lsat$Business frequently use customer surveys in an attempt to improve sales and increase profits.$lsat$),(1,$lsat$How can it be that ...$lsat$,$lsat$In this study, most of the businesses using the surveys had declining profits whereas most of the businesses that didn't use surveys did not have declining profits.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The paradox is that most of the businesses using this tool that's supposed to help a business improve profits have declining profits.

It's not some widespread economic downturn, because businesses not using this tool do not have declining profits.

Technically, if we're attuned to Relative vs. Absolute language, there isn't really a paradox here. The customer survey is supposed to **improve profits**. Are the businesses who are using the survey seeing **improved profits**?

Maybe! We don't know. We know they have declining profits, but maybe that was already the case before they started using the customer surveys.

If their profits were previously declining by 20% month over month, but once they started using the survey the profits are only declining by 5% month over month, then the survey is **improving** profits from what they would otherwise be without the survey.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Most correct answers on Paradox questions *Explain a Difference, Using a Difference.*

The difference we're trying to explain is declining profits vs. non-declining profits among two groups.

We already know one difference (using customer surveys vs. not using customer surveys), but it's unlikely that *that* difference explains declining vs. non-declining profits (because that difference is supposed to improve profits).

There's probably some **other** difference between the businesses using the surveys and those who aren't that explains why the former has declining profits whereas the latter does not.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Humans are generally unable to choose more wisely now than they could centuries ago.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Humans' emotional tendencies are essentially unchanged, from how we were in the early days of our species.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The "accordingly" tips us off that the last claim is the Conclusion. The "although" tells us that the first half of that claim is concession that isn't part of the core argument.

So the author is basically just making this move:

*if emotional tendencies then we're unable to*
*haven't changed, choose more wisely*

Another way to say that?

*Choosing more wisely would necessitate a change in emotional tendencies.*

A weaker way to touch on that?

*Emotional tendencies are relevant to how wisely we can make choices*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer providing this missing link between "emotional tendencies" and "ability to choose more wisely", or look for an answer ruling out an objection that would allow someone to argue that humans **are** generally able to choose more wisely these days.

f.e. "being able to access more information about the world has not increased humans' ability to choose more wisely"$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Ornithologists' Conclusion$lsat$,$lsat$Deforestation, (despite some recent reforestation), is continuing to worsen matters for many species of songbirds.$lsat$),(1,$lsat$Ornithologists' Evidence (since)$lsat$,$lsat$It's not reduction of forest size that endangers songbirds (so adding back some forest doesn't necessarily help). It's the fragmentation of the forest that imperils songbirds, **because** that introduces open spaces and corridors in forests, which reduces the distance from songbird nests to unforested areas, which reduces the songbirds' protection from predators.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we read Main Conclusion or Role paragraphs, we look out for Conclusions appearing **earlier** than the supporting ideas. On those two question types, Conclusions frequently come after pivot words such as "but, **yet**, however".

The evidence has at least one intermediate conclusion, because we see a "thus" in the final claim.

We're being asked about the claim that *there has recently been reforestation*.

We want to classify that as either Main Conclusion, Support, Opposing, or Neutral.

It's prefaced by the word **despite**, which automatically seems to cast it in the role of **Opposing**.

Whenever authors use terms like **while / despite / although / granted**, they are conceding a potential objection ... they are making acknowledging something their opponents would say.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for something like "it acknowledges a reason why you might *think* that the deforestation problem is getting better, even though it will proceed to argue that the problem is still getting worse".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

