-- PT112-S3-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=3 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$To minimize crop damage, farmers should water crops only just enough to ensure that there is no substantial threat, from a lack of water, to either the growth or the yield of the crops.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The leaves of mildly drought-stressed plants are tougher in texture than the leaves of abundantly watered plants.

Insects prefer to feed on the leaves of abundantly watered plants.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument fits the Recommendation pattern. Peter is suggesting a course of action (water plants minimally) to achieve a goal (minimize crop damage).

To assess this argument, we should consider whether following the recommendation would indeed lead to the intended outcome, with a net gain when compared to the current scenario of abundant watering.

The author thinks insects' preference for softer leaves means that mildly drought-stressed plants will experience less insect damage. The argument assumes that the benefit of reduced insect damage outweighs any negative effects of mild drought stress, so a strong point in favor would be evidence that supports minimizing insect damage as a priority.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that highlights that the potential benefits of reduced insect feeding, thanks to watering crops less, outweigh the risks associated with slight drought stress.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT112-S4-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=4 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (this is evidence that)$lsat$,$lsat$The program to improve the morale of high school students has begun to take effect to reduce dropouts.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$High school students who feel they are not succeeding in school often drop out.

Last year, the city's high school dropout rate was significantly lower than the previous year's rate.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument falls into the Explain Curious Fact pattern because it identifies a change in situation (a *Curious Fact*) and provides a causal explanation.

*Curious Fact:* Why is the high school dropout rate is lower this year compared to last year?

*Author's Explanation:* The program to improve student morale has caused the reduction in dropout rates.

The argument assumes that the program is the main or only reason the dropout rate has decreased. To weaken this argument, we can look for alternative explanations for the reduced dropout rate, or we could challenge the plausibility that the morale program was indeed responsible for the change.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that suggests an alternative reason for the reduced dropout rate, one that is unconnected to the morale improvement program.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT112-S4-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=4 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (must conclude)$lsat$,$lsat$Henry was widely watched before the move to Wednesday evenings because it followed That's Life and not because people especially liked it.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The television show Henry was not widely watched until it was scheduled for Tuesday evenings immediately after That's Life, the most popular show on television.

During the year after the move, Henry was consistently one of the ten most-watched shows on television.

Since Henry's recent move to Wednesday evenings, it has been watched by far fewer people.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument follows the Explain Curious Fact pattern. The author is exploring why *Henry* was widely watched after being moved to a Tuesday slot following *That's Life*, but not before, and why its viewership declined with the move to Wednesday.

*Curious Fact*

Why was Henry widely watched originally only when following That's Life, and then less so after moving to Wednesdays?

*Author's Explanation*

The viewership of Henry was high because it followed the popular show That's Life, not because of its own merits.

To strengthen the argument, we need to enhance the author's explanation by showing that the association with That's Life was a significant factor in Henry's viewership, or rule out some alternate explanation for why Henry is struggling on Wednesday nights (maybe the show fundamentally changed for the worse, or it's competing against some other really popular show on Wed nights).$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that increases the plausibility that Henry's high viewership was due to its position immediately after That's Life, or that rules out an alternate explanation for the decline in popularity.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S2-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=2 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (to conclude that)$lsat$,$lsat$VDTs cause headaches.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Researchers conducted a survey asking office workers to estimate their VDT usage and frequency of headaches over the past year.

The survey showed frequent VDT users suffered headaches more often than other office workers.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument involves correlational reasoning: it observes a correlation between VDT usage and headache frequency and concludes a causal relationship.

CUROUS FACT: why is VDT usage correlated with headaches?
EXPLANATION: VDT usage causes headaches.

To undermine the argument, we should consider alternative explanations for the observed correlation or demonstrate that the VDT usage doesn't actually cause headaches.

A common pattern to consider is Reverse Causality, where possibly the headaches caused people to think they spent more time using VDTs, or Third Factor, where some other variable causes both headache frequency and VDT usage estimation.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that suggests an alternative explanation for the correlation, such as a factor that could cause both increased VDT usage estimation and headaches or that undermines the plausibility of the idea that using VDT could cause headaches.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S3-Q3 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=3 AND q.question_number=3 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Advertisement$lsat$,$lsat$To assess whether female physicians are more sensitive than male physicians to the needs of female patients, we'll ask male and female physicians.$lsat$),(1,$lsat$Flaw$lsat$,$lsat$The people who are best equipped to judge "how sensitive was the doctor to the patient's needs" are the patients!

Meanwhile, this TV show is saying they're going to ask the doctors themselves to self-evaluate how sensitive they were to the patient's needs.

This would be like saying, "Who is better at making Mac & Cheese the way Sammy likes it, Mom or Dad? To get the answer, we'll ask both parents this question."

Shouldn't we ask Sammy? Isn't *he* the arbiter of who make the better Mac & Cheese?$lsat$),(2,$lsat$Goal$lsat$,$lsat$Look for an answer saying that it's silly to be asking the physicians who was more sensitive to the patient's needs, when only the patient knows what their needs are and only the patient can tell us which doctor was more sensitive to their needs.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S3-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=3 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The practice of using this therapy to treat the illness cannot be adequately supported by the claim that any therapy for treating the illness is more effective than no therapy at all.

*Rephrase: Effectiveness alone is not enough justification for using this therapy.*$lsat$),(1,$lsat$Evidence$lsat$,$lsat$What must also be taken into account is that this therapy is expensive and complicated.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The conclusion appears in the first sentence and is clarified by the following sentence. This argument fits one of the common patterns, where the conclusion is found in the first sentence and then supported by additional claims or considerations. In this case, the consideration of expense and complication acts as support for the main claim—that effectiveness is not sufficient justification.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find the best available meaning match for *effectiveness alone is not enough justification for using this therapy.*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S4-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=4 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion of Lydia's Argument$lsat$,$lsat$Squirrels are attracted to sugar in the sap of sugar maple trees.$lsat$),(1,$lsat$Rebuttal by Galina$lsat$,$lsat$The sugar concentration in the sap is too low for squirrels to be attracted to it for sugar.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Because we're trying to counter someone's objection, we want to defend the idea that squirrels are trying to get sugar from this sap, while addressing the fact that there's so little sugar content that you'd have to drink tons of sap to get much sugar.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Given that you'd have to drink tons of sap to get much sugar, how can we still maintain that squirrels are interested in the sap for its sugar content.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

