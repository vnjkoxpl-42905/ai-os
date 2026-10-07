-- PT120-S1-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=1 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$The second criticism cannot be accurate.
*rephrase:* Depression-era filmmakers did **not** self-indulgently create films reflecting their own dreams and desires.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$These filmmakers made their movies with an eye to profit and provided what their audiences most wanted in a film.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We're trying to prove that certain people "**didn't** self-indulgently create films reflecting their own dreams and desires", but the argument has provided any proving mechanism for such wording. So the correct answer will need to give us a rule that is like:

*if xyz → then didn't self-indulgently create*
*films to reflect own thinking*

We're trying to prove this wording in relation to Depression-era filmmakers. The argument provided two facts about them, so the correct answer could use either / both of the facts to get us to that magical conclusion wording.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for,

*made movies with → did not self-indulgently*
*an eye to profit make films reflecting*
*own dreams / desires*

or

*provided audiences did not self-indulgently*
*with what they → make films reflecting*
*most wanted own dreams / desires*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S3-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=3 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*pivot / math-y* (although, >, <)

MANUFACTURING
Fiber-optic > copper
$

OVERALL COST OF NETWORK
Fiber-optic < copper
$

*causal* (this is because)

Fiber optic is cheaper than copper, to run your network on, **because** cooper requires frequent amplification, whereas fiber optic can go for a while without needing amplification.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$We can tell from the mathematical comparison in the first sentence that other aspects of running a fiber-optic network outweigh the extra cost you pay to manufacture the fiber-optic cable, since a fiber-optic network is cheaper overall than a copper network. Then the second sentence tells us, "Let me tell you why a fiber-optic network comes out to be cheaper, despite the higher upfront cost to make the cable."

When we see *Causal Connector Language* like "X is true. **This is because** Y is true", there is a very strong likelihood that the correct answer wants to test us on whether we understand this causal connection.

The order of these statements is "Effect. This is because Cause". So we want to restate this relationship in our more intuitive ordering of Cause leads to Effect.

The fact that copper requires frequent amplification **leads to** copper being a more expensive cable to run a network off of, despite the fact that copper is cheaper to manufacture than is fiber optic cable.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for a safely worded answer that potentially reinforces this idea that "needing to frequently amplify the signal makes a copper network cost more than a fiber-optic one, despite the fact that copper cable is cheaper to produce."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S4-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=4 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$If a kid has a learning deficit, the hippocampus is messed up.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Learning is the process of acquiring new info in long-term memory.

New information is held in short-term memory for a few secs, and then either moved into long-term or forgotten.

If there's a short-term memory defect, the hippocampus is messed up.$lsat$),(2,$lsat$Evaluation$lsat$,$lsat$The evidence seems to prove that a messed up hippocampus *could* lead to a learning deficit, since we know that short-term memory is crucial to learning (by transferring info into long term memory, which is what we mean by 'learning') and we know that when the short-term memory is messed up, it's because of the hippocampus.

But just because the hippocampus *could* be involved in a causal story leading up to a learning deficit, it's not clear why the author thinks he can say that all learning deficits trace back to problems with the hippocampus.$lsat$),(3,$lsat$Goal$lsat$,$lsat$This has the fuzzy vibe of **Necessary vs. Sufficient**, since the author has provided us info to give us a causal chain moving one way:
bad hippo → bad short-term → no long term → can't learn

But he's trying to go the other way:
can't learn → bad hippo

We need to point out this flaw or point out what it ignores: there could be other possible causes of learning deficits besides a bad hippocampus leading to messed up short term memory.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S4-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=4 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore concluded)$lsat$,$lsat$The Checker Spot Butterfly is moving north due to changing climate conditions, specifically the northward shift of warm zones.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Checker Spot Butterflies have become more prevalent in northern regions and less so in southern regions.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We have a causal conclusion ("responsible") and an curious comparison in the evidence ("more prevalent").

CURIOUS FACT: how come this butterfly is more prevalent in the north and less in the south?

EXPLANATION: the northern areas have warmed from climate change, and that warmth brought the butterfly there.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Get rid of the four answers that strengthen. Strengthening answers will either rule out alternate explanations for why the butterfly is found more in the north / less in the south, or they will corroborate the hypothesis that it's because of the climate shift.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S4-Q24 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=4 AND q.question_number=24 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The collapse of Egypt's Old Kingdom was caused by an environmental catastrophe rather than internal social upheaval.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Ocean sediments reveal a period of global cooling at the time, a condition generally associated with extended droughts. The author acknowledges that while there were serious social problems in Egypt at the time, they resulted from a severe dry spell.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since we have a causal conclusion, we can use our Explain Curious Fact template.

CURIOUS FACT: what caused the collapse of Egypt's Old Kingdom?

EXPLANATION: an environmental catastrophe (specifically a long drought) caused the collapse.$lsat$),(3,$lsat$Goal$lsat$,$lsat$To strengthen the argument, we want to rule out an Alternate Explanation for the collapse (such as social issues) or boost the plausibility of the author's explanation that it was related to environmental reasons such as drought.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT120-S4-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=120 AND q.section=4 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (evident therefore)$lsat$,$lsat$More theaters should switch to repertory theater.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Repertory theater generates large revenues if the selected plays reflect audience demand. Additionally, actors, stagehands, and theater managers all like repertory theater for various reasons.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since this is a Recommendation, the author is assuming that for the theaters that aren't already repertory, the upsides of becoming repertory would outweigh the downsides.

Maybe actors / stagehands / theater managers like it better, but it's way less profitable than other forms of theater. Maybe the audiences don't like it as much. The evidence offered an Untriggered Conditional: **if** you choose the right shows, then they usually generate lots of revenue. But do repertory theaters usually choose the right shows?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that helps argue in favor of repertory theater or undermines one of the objections we considered.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT121-S1-Q19 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=121 AND q.section=1 AND q.question_number=19 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$University administrators tends to be biased against appointing professors to scientific administrative positions, if those professors have failed to pursue research.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In a survey, it was found that bio professors who haven't pursued research are disproportionately underrepresented among all scientific administrative positions in universities.

They're 1/20 of all science professors, but they fill
less than 1/20 of sci admin positions.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Disproportionate representation is one of those asymmetric **Comparisons** we refer to as a Curious Fact. The author's conclusion offers an Explanation.

*Curious Fact* ... why are bio professors who don't pursue research underrepresented in scientific admin positions?

*Author's Explanation ...* it's cuz they haven't pursued research. The people at the university who decide on whom to appoint to this scientific admin positions are biased against professors who haven't pursued research.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Weaken, we're expecting a correct answer to

1. Suggest an **Alternate Explanation** for why these research-less bio professors are under-appointed to scientific admin positions
or
2. Undermine the **plausibility** of the Author's Explanation, making it seem like university higher-ups are **not** biased against professors who haven't pursued research.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT121-S4-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=121 AND q.section=4 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The results of that poll are dubious$lsat$),(1,$lsat$Intermediate Conclusion (because)$lsat$,$lsat$The poll was not based on a representative sample.$lsat$),(2,$lsat$Intermediate Conclusion$lsat$,$lsat$It's quite likely that Perkin's supporters were overrepresented.$lsat$),(3,$lsat$Evidence (given that / and)$lsat$,$lsat$The poll was conducted at high-priced shopping malls. Perkins advocates for the upper-middle class.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$The #1 pattern on Main Conclusion is that the conclusion is some Pivot/Rebuttal claim. The #2 pattern is that the conclusion is in the first sentence. This argument essentially combines those patterns, by putting a rebuttal claim "the results are dubious" in the first sentence.

When we hear an opinion from the author in the first sentence, we want to guess that it's the conclusion and listen for whether the author seems to be supporting/defending that claim.

*Given that X, it is probable that Y* is a structure that indicates that X is a premise that supports the conclusion Y. So they are tempting us to pick the last claim of the paragraph, and making it even more tempting because it is *a*, conclusion, just not the main one.$lsat$),(5,$lsat$Goal$lsat$,$lsat$Find the best available meaning match for "The results of the poll are dubious".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

