-- PT108-S2-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=108 AND q.section=2 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (this leads to)$lsat$,$lsat$It seems like there have been spacecraft sighted near Earth that are extraterrestrial in origin.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$When the British government gets requests from civilian researchers for information about sightings of UFOs made by military and intelligence agencies, those requests are brushed aside.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This author seems to interpret the brushed-aside requests for information as evidence that the British government has something to hide.

Isn't it possible that we could Explain this Curious Fact with some alternate explanation?

Maybe there really is nothing interesting to share with civilians and the British government is just annoyed by the frequent requests. Maybe there is something to hide, but it isn't "we discovered aliens".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this author is interpreting the meaning behind a Curious Fact, we can strengthen the argument by finding an answer that either
- **rule out** an alternate explanation for why requests for info are brushed aside
- **boost** the plausibility of the author's explanation, which is that the British government has sighted extraterrestrial spacecraft near Earth and is just unwilling to share info with the public about it.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S1-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=1 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (hence)$lsat$,$lsat$The presence of professional athletes violates the spirit of fairness essential to the games.$lsat$),(1,$lsat$Intermediate Conclusion$lsat$,$lsat$It is unlikely that amateurs will ever offer a serious challenge to professionals in Olympic events where they compete against each other.$lsat$),(2,$lsat$Evidence (since)$lsat$,$lsat$Amateurs rarely have the financial or material resources available to professionals.

The ancient Olympics did not include professional athletes.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We don't really need to worry about Michiko's response. We just need a way to accept that amateurs rarely have the resources that professionals have, but argue that amateurs might still offer a serious challenge to professionals and thus it's still a fair competition.

Or we can argue that even though the amateurs won't offer a serious challenge to professionals competing in the same event, the presence of professionals doesn't violate the spirit of fairness.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S1-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=1 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$The current use of plastics actually does less harm to the environment nationwide than that of paper products.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The environmental damage done by given unit of plastic trash is roughly the same as the damage done by an equal unit of paper trash.

A national survey shows there is currently less plastic trash than paper trash.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Usually, like 90% of the time, the conclusion on Main Conclusion questions is **earlier** than the evidence. But in this case it's the final claim, telegraphed with the indicator word "therefore".

The word 'therefore' is definitely signaling that the final sentence is **a** conclusion, but is it just an intermediate conclusion there to fool us?

No. The other two sentences aren't eligible to be conclusions, because they're both facts and there isn't any support offered for either one.

The last sentence is supported by combining the 1st and 2nd sentences.

P1: the harm caused by 1 unit of Plastic trash = 1 unit of Paper trash
P2: nationwide, fewer units of trash are plastic than paper
C: so, nationwide more harm is caused by plastic than paper$lsat$),(3,$lsat$Goal$lsat$,$lsat$We're just looking for the answer whose meaning best matches the final claim, "The current use of plastics actually does less harm to the environment nationwide than that of paper products."

They'll probably invert it or use synonyms, or both: "Paper trash, across the nation as a whole, presently does more harm than plastic trash."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S3-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=3 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$To explore cost-effective ways to help people prone to mental disorders, we should increase funding for intervention research.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Limited research shows therapeutic intervention before the onset of mental disorders can mitigate major contributing factors.

A comprehensive research program is needed to verify and design specific health measures.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument fits the Plan / Goal pattern.

GOAL: save money helping people prone to mental disorders
PLAN: increase funding for intervention research

We want to know the plan is feasible, that people will cooperate with it, that it won't backfire in some way that undermines the goal, or that it targets the main source of our current issue/problem.

To assess whether increasing funding achieves the goal, consider the differences between the recommendation-world and the current-world. What are the potential advantages and disadvantages?

The argument relies on the premise that therapeutic intervention can mitigate the contributing factors of mental disorders. Thus, if more funding leads to more effective interventions that are relatively inexpensive compared to treatment, then the recommendation would seem beneficial.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that helps us argue that increasing funding for intervention research can lead to more cost-effective help for those prone to mental disorders.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S3-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=3 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (conclude)$lsat$,$lsat$Violent crime is now out of control, and, to be safe from personal attack, one should not leave one's home except for absolute necessities.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Unlike newspapers in the old days, today's newspapers and televised news programs are full of stories about murders and assaults in our city.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument presents a Curious Difference (an asymmetric comparison) in the evidence. Does the author then assume some causal interpretationof that evidence? Yes!

CURIOUS FACT: How come today's papers and TV news are so much more full of murder/assault stories?

EXPLANATION: Because there's so much more murder and assault these days!

The argument observes that there's an increase in media coverage of violent crime and concludes that violent crime itself is out of control and the city's safety has drastically changed.

The argument assumes that because there's more media coverage of violent crime stories today compared to the past, the actual incidence of violent crime must have increased proportionally.

To weaken this conclusion, we want to consider alternative explanations for the increase in media coverage that do not involve an actual increase in violent crime.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that suggests an alternate reason for the observed change in media content, rather than an actual increase in the amount or rate of violent crimes, or an answer that undermines the plausibility of the author's belief that violent crime has gotten much worse in recent times.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S4-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=4 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The bill to say "using car phone while driving is illegal" should be adopted.
(i.e. it should be illegal to use your car phone while driving)$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Using a car phone distracts the driver, which poses a threat to safe driving.

Meanwhile, if it were illegal to use your car phone while driving, people would be deterred from doing it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$On Sufficient Assumption, if there are any New Terms in the conclusion, they need to be in the correct answer. The big one in this conclusion is **should be adopted**.

We need to a construct a rule that sounds like

**if ..... then ....**
the stuff we described in should adopt
the evidence about this bill the bill

So what do we know about this bill?

It would make using your car phone while driving illegal. That would deter people from using their car phone while driving. Using your car phone seriously distracts the driver, which poses a threat to safe driving.

Chunking that all together, this bill would "deter people from doing something that poses a threat to safe driving".

That seems to be the most common sense understanding of the author's rationale for why we should adopt the bill.$lsat$),(3,$lsat$Goal$lsat$,$lsat$So we just need to hear something like

"Any bill that would deter people from doing something that poses a threat to safe driving ... **should be adopted**".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT109-S4-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=109 AND q.section=4 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$There's a Causal Chain type story presented:

1. buried in the soil all winter
2. churned up to surface when soil is plowed in the spring
3. gets brief exposure to sunlight
4. receptors get stimulated
5. receptors trigger germination

The final idea is a Conditional that says

if not 1 → then 3 doesn't trigger 4

Technically, it's "if there isn't prolonged darkness", then 3 doesn't trigger 4.
Being buried all winter is *one* way to get prolonged darkness, but there are presumably other ways (f.e. watching French films, I'd imagine)

For the last sentence, I would primarily remember it as a Causal Difference-Maker:
*the long exposure to darkness is what makes the receptors sensitive enough to get triggered by brief sunlight*

It's kinda like, "If you don't spend enough time in the dark, your eyes won't adjust to see faint things".$lsat$),(1,$lsat$Goal$lsat$,$lsat$The question stem is about pigweed seeds in the exact situation we just had described to us, so it seems like it's just asking us what we can best prove from the paragraph.

We'd expect them, when plowed, to receive brief sunlight, and if they do, and they've truly been exposed to prolonged darkness over the winter, then we expect them to germinate. Otherwise, we'd expect them not to germinate.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

