-- PT111-S1-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (This strongly suggests)$lsat$,$lsat$Humans hold onto acquired beliefs even in the absence of any credible evidence to support them.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In a study, people read statements that caused them to form new beliefs. Later when they were told that the original statements were false, the subjects maintained those new beliefs.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author's conclusion is extremely broad, speaking for all of humankind, based only on a sample of people in a study (who may not be representative). So it's possible that a Weaken answer would attack this *Sampling* move, where the author reasons, "If it was true for *these* people, it must be true for people in general."

But we can also attack the notion that the conclusion was even true for the people in the study. Were they examples of "humans who continued to hold onto acquired beliefs even in the absence of any credible evidence to support those beliefs"?

If we want to fight that categorization, we either have to find a way to argue that the people in the study:
1. DIDN'T hold onto acquired beliefs, or
2. DID have credible evidence to support those beliefs (or both)

We can't argue that first line of objection, because the evidence explicitly says that most of them persisted in their newly acquired beliefs.

Okay, so is it possible that they *did* have credible evidence to support those beliefs? They probably didn't have credible evidence for those beliefs *prior* to the study, since we know it was reading the statements in the study that caused the people to form these new beliefs.

But in between the time they're reading these statements and forming beliefs and the time, "Later," when they're told the statements were false, could they have gotten credible evidence to support the belief?

Sure, I guess so. You could read a statement like, "Barack Obama plans to invest in a passenger spaceship to Mars" and then form the new belief, "Within the next 50 years, people will be able to take a passenger spaceship to Mars".

Later, we tell you that Obama statement we provided you with was false, but when you got home that day, you Googled "passenger spaceship to Mars" and found out that Elon Musk was actually planning to do this. Your newly acquired belief has some credible evidence, in addition to the statement we provided.

Thus, when we rescind the truth of those statements, it doesn't cause you to jettison that new belief you formed about "within 50 years, passenger travel to Mars". You are **not** an example of someone who is holding onto an acquired belief even though you have no credible evidence to support it.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer impugning the Sampling move, by saying that what happened in this study is not a generalizable "human" trait.

Or look for an answer exploiting the wiggle room with "Later, ...". Someone might have found credible evidence to support their new belief in the intervening period. Just because the original reason for the belief turns out to be false, that doesn't mean the belief is false (that's the *Unproven vs. Proven False* distinction).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Novelists cannot become great as long as they remain in academia.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Schools hone observation and analysis (useful to novelists). But an intuitive grasp of everyday emotions can only be obtained through immersion in everyday life, which being an academic precludes.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument moves from "academics can't get the intuitive grasp of everyday emotions" to "academics can't become great novelists." That step only works if the intuitive grasp of everyday emotions is something *required* for greatness. If it were merely nice to have, the argument would not establish that academics are barred from greatness.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The right answer should fill the gap by establishing that an intuitive grasp of everyday emotions is necessary for greatness. Negation test: if it's not necessary, the argument falls apart.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$There is reason to be skeptical about the conclusion drawn in the magazine's survey.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The survey question was biased: "Which do you think about more: politics or the joy of earning money?"

The readers of the magazine are a self-selecting sample.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The statistician is making a case that the results of the magazine's survey are not reliable because the survey question is biased, and the sample is self-selecting, making it unrepresentative. The argument is about questioning the validity and accuracy of the magazine’s conclusion that North Americans care more about finances than politics.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's get rid of four answers that strengthen the argument. We might see evidence that supports the idea that the survey results are not credible due to these issues. This could include evidence about the bias or unreliability of such surveys or additional data suggesting the survey's conclusion is incorrect.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The Antarctic ice sheet must temporarily have melted about three million years ago — i.e., Antarctica has not been continuously ice-covered for the last 14 million years.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Three-million-year-old ocean-floor-sediment fossils were found beneath the central Antarctic ice sheet. Either severe climatic warming or volcanic activity could have melted the ice and submerged the continent (which is what would have allowed those fossils to settle into ocean-floor sediments at that location).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Identify the main conclusion vs. supporting claims. The "either-or" sentence about volcanic activity or climatic warming is offered as *support* for the melting-ice claim ("after all, ..."). The melting-ice claim is the main conclusion the author is arguing for; the previous-belief framing (14M years of ice) sets up the contrast.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find the answer that captures the claim "the ice melted three million years ago" — i.e., the ice sheet has not been continuously present.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$About 3 million years ago, the Antarctic ice sheet must have temporarily melted.$lsat$),(1,$lsat$Evidence (after all)$lsat$,$lsat$We recently discovered 3 million year old fossils under the ice sheet covering central America (previously we had only found this type of fossils at the bottom of the ocean).

It's plausible that Antartica could have been submerged under water, since severe climate change or volcanic activity could have melted the ice sheet.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is looking at a puzzling piece of archaeological evidence and speculating what it means / what it tells us, we can use our Curious Fact / Explanation mindset.

*Curious Fact ...* why are we finding these 3 million year old fossils under the ice sheet covering Antartica? (Previously we had only found these fossils in ocean floor sediments)

*Author's Explanation* ... At the time of these fossils, the ice sheet must have been melted, which would raise the water level high enough that Antarctica would be underwater, and so the ocean creature these fossils are from would have been swimming "over" Antarctica, it would have died and sunk to the "ocean floor", which would have been the top of Antarctica, and then later as the water refroze and the continent again rose above sea level, those fossils would be trapped under the ice sheet.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$Notice how many blanks we had to fill in for the author just to understand her Causal Story! (I'm not even 100% sure I'm interpreting her causal story correctly)

When **Flaw** intersects with Curious Fact / Explanation arguments, the most common type of correct answer just calls out the fact that the author is overconfidently assuming one possible causal interpretation of the evidence, when others exist.

When we simply say "the flaw is that the author *infers a cause from a mere correlation*" we're saying, "Sure, *maybe* this correlation indicates causality, but we can't be as sure as the author is thinking."

Our author's conclusion is way too strong --- the ice sheet **must** have temporarily melted?

There aren't any other explanations? If we assumed that Antarctica did not melt and was still above sea level, can we think of any other possible way that the fossils could have ended up where we found them?

Sure, maybe a bird snatched this fish out of the ocean and was flying over Antarctica and dropped it. Maybe a hurricane or an underwater volcano lifted this fish into the air and flung it over Antarctica. Maybe within the ice sheet there used to be underwater tunnels that this fish could have gone through. Maybe this fish was really an amphibian that was able to scoot across the ice.$lsat$),(4,$lsat$Goal$lsat$,$lsat$When we're doing Flaw and read one of these Curious Fact / Explanation arguments, then we're receptive to three different types of answers:
1. Complain that the author is overly confident in arriving at one *possible* explanation, where others may exist.

2. Suggest that the author may have failed to consider some alternative explanation.

3. Point out something implausible about the author's explanation.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q3 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=3 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$This theory may be wrong.
*rephrase:* The reason that women suffer more than men from Alzheimer's might not be because women live longer.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$A recent study shows that prescribing estrogen to post-menopausal women can prevent them from developing Alzheimer's. Meanwhile, men have a big supply of testosterone, which the body converts into estrogen.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we do Main Conclusion (and Role) we read the paragraph differently, knowing that 90% of the time the conclusion is the very **first sentence**, or it's some **rebuttal** signified with a pivot word (like "but, yet, however"). In either case, 90% of the time the conclusion is **earlier** than the support, on these two question types.

As we read this first sentence, we ask ourselves whether it's eligible to be a conclusion -- does it sound like an opinion coming from the author? No, it sounds like fact.

But the second sentence contains an attribution (literally). It says "[some people] **attribute** this to women's longer life span". When we see any attribution in the early going of a Main Conclusion paragraph, then we anticipate that our author will probably be rebutting this position.

Sure enough, the second half of the 2nd sentence has one of those signature **pivot** words that we're listening for on Main Conclusion (**but**, yet, however).

So now we think, "Ah! This looks like the conclusion. The author is rebutting the idea that living longer is why women suffer more from Alzheimer's."

Does the author going to go on and try to convince us of that? Yes, because she builds up a case for an Alternate Explanation. This theory that "longer life span" is why women are more afflicted may be wrong, because the real reason that women are more afflicted could be that estrogen is the secret weapon against Alzheimer's and women have less estrogen than men in their old age.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The conclusion was "this theory may be wrong", but since this claim includes a *pronoun* (**this** theory), we need to make sure we insert the specific language that pronoun is referring to:

*It may be wrong to think that longer life span is why women suffer more from Alzheimer's (lack of estrogen may be the real reason that women suffer more from Alzheimer's)*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

