-- PT110-S2-Q19 (Unexplained)
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=110 AND q.section=2 AND q.question_number=19 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=110 AND q.section=2 AND q.question_number=19 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Information$lsat$,$lsat$*causal* (capacity to neutralize, can increase/stimulate)

CC >> neutralize stomach acids
CC >> increase calcium >> impair kidneys
CC >> more gastrin >> more acid secretion

*recommendation*

Don't take more than 1/2 gram of CC.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$We know that the #1 focus of *Most Supported* questions is **cause/effect** relationships.

We had a couple causal chains here as well as that initial causal claim about neutralizing stomach acids.

In addition to the obvious overlap where all four claims are about calcium carbonate, we also have two other overlaps:

- multiple claims mention "half a gram" of CC
- multiple claims mention "stomach acids"

If we combine the idea that 1/2 a gram stimulates gastrin and acid secretion with the claim that we *shouldn't* take more than 1/2 a gram, we could probably derive some takeaway like, "Once you're above 1/2 a gram, the benefits of calcium carbonate are outweighed by the harm of stimulating gastrin / stomach acids."

If we combine the idea that CC can neutralize stomach acids with the claim that 1/2 a gram of it can stimulate stomach acid secretion, we'd get some weird idea like "depending on the dose of CC, it might lessen or increase stomach acids?"$lsat$),(2,$lsat$Goal$lsat$,$lsat$Look for the most provable claim. It will likely reward us for noticing the cause/effect relationships given.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=110 AND q.section=2 AND q.question_number=19 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This is getting at the two causal claims involving stomach acids. We heard that CC can neutralize stomach acids, but in large doses can also trigger them.

Since the paragraph is suggesting that we *don't* take CC, does that imply that it's better to avoid stimulating gastrin (and thus stomach acids) than it is to try to neutralize the existing stomach acid?

No, not necessarily. Perhaps a low dose of CC is the best (like 1/4 a gram), maybe that neutralizes what's there without stimulating the secretion of more.

Furthermore, the recommendation to avoid CC could be based largely on the fact that it can impair kidney function, rather than on its capacity to stimulate gastrin.$lsat$),($lsat$B$lsat$,$lsat$The passage doesn't talk about at what dosage calcium carbonate starts to trigger impaired kidney function. So we wouldn't really be able to relate kidney damage to the 1/2 gram dosage.

We also know nothing about the average risk of impaired kidney function. It might be that 99% of people don't take any calcium carbonate, so the average risk of impaired kidney function is quite low. Thus, avoiding 1/2 a gram of CC might just make you have *normal* risk of impaired kidneys, not **better than average** odds.

A better version of this answer would sound like, "All other things being equal, a person who avoids taking more than 1/2 a gram of CC is less likely to suffer impaired kidney function than if they were to take more than 1/2 a gram of CC".$lsat$),($lsat$C$lsat$,$lsat$This sounds pretty reasonable, because we might be thinking there's a sweet spot (like 1/4 gram of CC) where you get to neutralize stomach acids but you avoid stimulating acid secretion.

But we don't know at what dosage the neutralizing effects kick in. They might not really kick in until 3/4 gram or more. We just know that CC has the **capacity** to neutralize stomach acids, but we don't know what dose is required for it to start having that effect.

We also don't know how to compare the acid-neutralizing effects to the acid-stimulating effects. It's not clear whether any dose of CC creates a net reduction or net increase in stomach acids.$lsat$),($lsat$D$lsat$,$lsat$This is our most provable claim. Technically, we don't know whether 1/2 a gram of CC neutralizes your stomach acids.

We know that CC has the capacity to neutralize stomach acids, but we don't know if you need to hit a certain dose to experience that effect.

So this answer isn't bulletproof, but correct answers on Most Supported don't need to be. It's our most provable.

We know that CC has the capacity to neutralize stomach acids and that 1/2 a gram of it can stimulate the secretion of stomach acids, so we have a lot of support for this. And the claim is worded very weakly.$lsat$),($lsat$E$lsat$,$lsat$We were told that increased calcium in the blood can lead to impaired kidney function, not this causally-reversed relationship.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=110 AND q.section=2 AND q.question_number=19;

-- PT110-S2-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=110 AND q.section=2 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$There is no need to look for a further explanation (beyond using different methods) to explain why the university study and the governmental study had two different estimations of the how the average workweek has changed.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The university study thinks the average workweek has gotten longer. The governmental study think it's gotten shorter. The two studies used different methods of investigation.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$How could we accept the evidence but argue that **there is** still some need to look further for an explanation of the difference?

There's a curious fact:
*how come the college study says up and the govt. study says down?*

There's a potential explanation:
*the college study and the govt study used different methods.*

The assumption is that different methods could lead to different measurements. Maybe we both measured the temperature of a lake, and I measured near the top and you measured near the bottom and that's why we got different measurements.

But maybe the reason we got different measurements is that we used the same method (measure near the top) but your instrument works fine and my thermometer was busted.

The author is overly confident in assuming that the difference between the college study's results and the govt study's results is that they employed different methods. Maybe something else was the reason.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer complaining that the author is saying, "As soon as we have one possible explanation, we need look no further. We've cracked the case!" Meanwhile, the author is failing to rule out other possible explanations and failing to convince us that different methods led to the different results$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT110-S3-Q24 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=110 AND q.section=3 AND q.question_number=24 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (concluded)$lsat$,$lsat$The native ringtail opossum population is endangered not by a scarcity of food, as had been previously thought, but by non-native predator species against which the opossum had not developed natural defenses.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$A number of ringtail opossums that were orphaned and subsequently raised in captivity were monitored after being returned to the wild.

Seventy-five percent of those opossums were killed by foxes, a species not native to Australia.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This conclusion has two claims, one of them causal and the other anti-causal. We can reverse engineer from the conclusion what causal mystery they are trying to solve.

*Curious Fact*: Why is the ringtail opossum population endangered?

*Author's Explanation*: It's due to non-native predator species, such as foxes, rather than a scarcity of food.

To strengthen this argument, we can either rule out an alternate explanation (such as food scarcity) or increase the plausibility that non-native predators are indeed a significant threat.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that either undermines the food scarcity theory or strengthens the idea that non-native predators, like foxes, are a significant threat to the ringtail opossum.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (implied)$lsat$,$lsat$An opera's stage directions are sometimes reflected in its music.$lsat$),(1,$lsat$Intermediate Conclusion (Hence)$lsat$,$lsat$A change of scenery, which is a basic stage direction, can be reflected in the music, so other operatic stage directions can also be reflected.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$In some of Mozart's funny operas, there are squeaky violin noises that Mozart clearly meant to echo the sounds that are made while scenery is changing (set pieces are often on rolling wooden frames, so they might squeak ... big backdrops are lowered or raised from the rafters via rope and pully).$lsat$),(3,$lsat$Evaluate / Goal$lsat$,$lsat$They're asking us about the Mozart premise, and asking what claim it was offered in support of. We could say that it was directly supporting the intermediate conclusion that "a change of scenery can be reflected in the music", or that it was ultimately supporting the author's rebuttal to the position in the first sentence; our author is saying "an opera's stage directions **are** sometimes reflected in its music".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Background$lsat$,$lsat$Marathons take at least 2 hours to run.$lsat$),(1,$lsat$Surprising Claim$lsat$,$lsat$It's better to train for a marathon by doing 90 min runs each day than by doing runs of 2+ hours.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$*Given that ...* the race they're training for is 2+ hours

*Why is it that* ... optimal training is only 1.5 hrs?

Maybe you burn yourself out if you practice the full-length thing too much (hint-hint: LSAT students, don't take test after test as your form of practice)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S1-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*causal* (can give rise to)

Gene >> new varieties of farm animals
splicing whose genetic makeup not
totally understood

*causal* (can introduce)

Gene >> new genes for whichever
splicing trait is desired

Gene >> new genes relate to making
splicing toxins or carcinogens

It might be hard to discover these new genes related to making toxins or carcinogens.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$We get a few causal reactions that can come from gene splicing. It sounds like we need to proceed very carefully with gene splicing. The appeal of it is that we can introduce new genes for whichever trait is desired (for example: a cow with a bigger than average milk supply).

But we're also introducing genes that govern production of toxins or carcinogens, and we can't easily detect when we've done so.

So we might successfully make a cow that has a super milk supply, but accidentally also cause the cow to have new toxins or carcinogens in its system.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for a safely worded answer that reinforces the uncertain outcomes of gene splicing.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

