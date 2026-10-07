-- PT148-S4-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (should = opinion)$lsat$,$lsat$This legislation, which provides tax incentives and zoning variances to encourage renovation and revitalization of selected areas, should not be commended.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Its principal beneficiaries have turned out to be well-to-do professionals; the long-term residents these programs were intended to help now face displacement due to increased rent and taxes.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$Typically, the correct answer to Strengthen + Principle is a conditional that sounds like "If Premise, then Conclusion", so we'll look for something like,

*turns out to benefit yuppies, should*
*not the people it was intended → not be*
*to benefit (long-term residents) commended*

We know that the correct answer should be about whether or not to commend / praise legislation. If an answer isn't a principle addressing whether or not legislation should be commended, we'll move away from it.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It's good to have national leaders voted out of office after a few years.
(*why should we believe that?*)$lsat$),(1,$lsat$Intermediate Conclusion$lsat$,$lsat$Because, it's usually early in a new government when reforms are undertaken.
*(why should we believe that?*)$lsat$),(2,$lsat$Evidence$lsat$,$lsat$Because, if they don't act quickly to solve a problem and then it becomes a problem, they either deny there's a problem or deny they could have done anything about it, so that they can avoid being blamed for it.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$Whenever we're doing Main Conclusion, we prime our brain before reading the paragraph: "Remember, on Main Conclusion and Role, the conclusion usually appears **earlier** than its support."

For these questions, the conclusion is usually
- the first sentence
or
- a rebuttal

When we read this first sentence, we're asking ourselves, "Is this the author's conclusion? Does it sound like her opinion?"

The normative language "it is good to X" tells us that the first sentence is an opinion. If the rest of the paragraph tries to support that claim, then we'll know that the first sentence was the main conclusion.

The second sentence telegraphs that support is being provided by saying "the **reason** is that ..."$lsat$),(4,$lsat$Goal$lsat$,$lsat$Just find an answer that replicates the meaning of the first sentence, since that was our Main Conclusion.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT149-S4-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=149 AND q.section=4 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$The lack of competition from mammals is not why New Zealand has a rich and varied native bird population.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Previously, it was believed that New Zealand had no land mammals, but recent findings indicate that at least one land mammal existed there.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is a "Weaken" question, and our task is to find a way to accept the evidence while resisting the author’s conclusion. We need to support the original theory that the richness of New Zealand's bird population is due to a lack of competition with mammals, despite the newfound evidence of a land mammal.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that allows for the reconciliation of the evidence (presence of a mammal) with the idea that the birds thrived because they faced little to no mammalian competition.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT149-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=149 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thereby)$lsat$,$lsat$The hypothesis is disproved.

*rephrase:* Our solar system was **not** formed from a cloud of gas and dust produced by a supernova.$lsat$),(1,$lsat$Intermediate Conclusion (so)$lsat$,$lsat$If our solar system **were** formed from the remnants of a supernova, then iron-60 would have been present in the early history of the solar system.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$Supernovas produce the isotope iron-60.

But researchers have found no iron-60 in meteorites that formed early in the solar system's history.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The author's argument is structured as a Rebuttal that uses *Contrapositive Logic* to defeat the conclusion, by showing that a certain implication of the conclusion does not follow. Here is that structure:

*- Some people say X.*
*- But if X were true, Y would be true.*
*- Y isn't true.*
*- Thus, X isn't true.*

In this case, the argument is like this:
*- Some people say [solar system from supernova]*
*- If [solar system from supernova] were true, then [iron-60 in early history] would be true.*
*- but [iron-60 in early history isn't true].*
*- Thus, [solar system from supernova] not true.*

The author failed to establish that 3rd claim.

We need to hear that "iron-60 was not present in the early history of the solar system" to trigger that contrapositive.

She only told us that, "iron-60 was not found in the **meteorites** that formed early in the solar system's history".$lsat$),(4,$lsat$Goal$lsat$,$lsat$So a *Linking* idea being assumed is that,

iron-60 wasn't found → iron-60 wasn't present
in early meteorites in early solar system

Or by contrapositive,

iron-60 was present → iron-60 would be present
in early solar system in early meteorites

The author is also assuming *Defender* ideas like there are **not** other places we should look for iron-60 besides meteorites / we will **not** eventually find iron-60 inside an early meteorite / the iron-60 that was once in these meteorites has **not** decayed away$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT152-S2-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=152 AND q.section=2 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It became necessary to adopt new measures of land (beyond "plow time") when land uses diversified.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The initial convention for measuring land was "plow time". But knowing how long it takes to plow a piece of land doesn't tell you how many apartment complexes could be built on that parcel.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$For years and years, LSAC avoided putting the conclusion in the final sentence on Main Conclusion questions (too obvious a place to look for it). But recently it's become more common, mostly as a way of trolling test prep advice.

There are three keywords we might lean on here: thus, however, therefore.

The first "Thus" is an implication being drawn of the "plow time" method.
*We used standard X. Thus, according to standard X, this thing would be different from that thing.*

Although "thus" is usually indicating a conclusion the author is drawing, it can also be used to designate cause/effect relationships, or in this case, rule/implication relationships.

"However" usually means that we are leaving background ideas and entering the Author's argument, but we still have to figure out whether the author's argument will go Support, then Conclusion or go Conclusion, then Support.

The "Therefore" tells us that this argument is going Support, then Conclusion.

We can always test whether we've found the right claim as the conclusion by asking, "Why should I believe that?" and making sure that there's a supporting idea provided.

*Why should we believe that* **as land uses diversified, we needed to adopt new measure of land?**

Because, the old measure (plow time) wouldn't tell someone how many acres a given plot of land was, if they wanted to build apartment complexes on it.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Just pick the answer that is closest in meaning to the final sentence, which was the Conclusion.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT152-S2-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=152 AND q.section=2 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (must be = causal speculation)$lsat$,$lsat$Measures taken to clean up the river must be working.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$This year the Lalolah River is ranked as only the 3rd most polluted river in the district.

Last year it was ranked #1.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument has a common structure. The evidence is an *Asymmetric Comparison* (it used to be ranked 1st most polluted, but now it's ranked 3rd most polluted).

And the author's conclusion states or assumes a causal explanation for that Curious Fact, that asymmetric comparison.

*Curious Fact ....* Why did the river go from being the most polluted to the 3rd most polluted?

*Author's Explanation ....* they took some measures to clean up the river, and so now the river is less polluted than before.

The two pressure points for these arguments are always the same:
1. **Alternate Explanations** for the curious fact
2. the **plausibility** of the author's explanation

On Flaw, we're primarily concerned with the #1. They want us to see that the author is overconfidently jumping to one possible causal explanation while failing to consider that there could be other explanations.

What could be an alternate explanation for why the Lalolah River went from being the most polluted to the 3rd most polluted?

Maybe that river didn't get any cleaner, but the two rivers that are now ranked higher than Lalolah got worse.

It's possible for Elon Musk to go from being the richest person in the world to the 3rd richest without him losing any money. It could be explained by people who previously had less money than him gaining enough money to surpass him.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for something like, "The author fails to consider alternate explanations for the change in pollution ranking (such as other rivers getting *more polluted* than before)."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT152-S2-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=152 AND q.section=2 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Doctors treating chronic lower back pain patients should be prepared to discuss the merits of yoga.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If activity significantly doctors should
reduces chronic lower → be prepared to talk
back pain about it

Recent study showed that practicing yoga leads to an equal reduction in chronic lower back pain as does taking stretching classes with a physical therapist.$lsat$),(2,$lsat$Evaluation$lsat$,$lsat$The conclusion is saying "Doctors should do X"
+
There's a rule that says, "Y → doc should do X"

So we know we have to establish Y. In this case, we need to establish that yoga *significantly reduces chronic lower back pain*, in order to trigger that initial conditional.

Were we told that yoga *significantly reduces chronic lower back pain*?
No, we were only told that yoga reduces chronic lower back pain as much as stretching classes with a physical therapist does.

Okay .... does stretching classes with a physical therapist *significantly reduce chronic lower back pain*?$lsat$),(3,$lsat$Goal$lsat$,$lsat$It seems like we should be on the lookout for an answer that reassures us, "yes, **stretching with a physical therapist significantly reduces chronic lower back pain**". Since we know that yoga achieves an equal reduction, then yoga, too, would significantly reduce lower back pain and the author can trigger that conditional that he seems to think he's triggered.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

