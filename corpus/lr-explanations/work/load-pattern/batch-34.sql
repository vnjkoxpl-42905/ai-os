-- PT156-S2-Q16 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT156-S2-Q16$lsat$, 156, 2, 16, $lsat$Most Strongly Supported$lsat$, $lsat$A recent study found that small rats were approximately
 twice as likely, and large rats only half as likely, to suffer
 from heart problems than were rats of average size.$lsat$, $lsat$Each of the following, if true, contributes to an
 explanation of the correlation given above between size
 and heart disease in rats except:$lsat$, $lsat$A$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=156 AND s.section=2
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$Small rats are more likely than large rats to suffer from fatal diseases that tend to strike earlier than do heart problems.$lsat$,$lsat$Correct$lsat$,true),($lsat$B$lsat$,$lsat$Small rats generally have smaller blood vessels than do large rats, vessels that can more easily be clogged with fatty deposits.$lsat$,$lsat$Helps Explain$lsat$,false),($lsat$C$lsat$,$lsat$The larger a rat is, the more successful it will be at defending itself, and therefore the less stressful its existence will be.$lsat$,$lsat$Helps Explain$lsat$,false),($lsat$D$lsat$,$lsat$In addition to being the leading cause of weak hearts in adult rats, malnutrition at early stages of development causes rats to be undersized.$lsat$,$lsat$Helps Explain$lsat$,false),($lsat$E$lsat$,$lsat$Although large rats are no more active than rats of average size, they tend to be much more active than small rats, resulting in greater cardiovascular conditioning.$lsat$,$lsat$Helps Explain$lsat$,false)) v(l,t,g,c) WHERE q.preptest=156 AND q.section=2 AND q.question_number=16
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=156 AND q.section=2 AND q.question_number=16 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=16 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Compared to Normal Rats, How Come ...$lsat$,$lsat$small rats are 2x as likely to have heart problems?
and
large rats are 1/2 as likely to have heart problems?$lsat$),(1,$lsat$Goal$lsat$,$lsat$Since it's Paradox EXCEPT, there will be four answers that help explain this pattern.

Overall, the bigger the rat, the less likely the heart problem.

You could picture the continuum of risk as:
SMALL NORMAL LARGE
200% 100% 50%

What is it about smaller rats that's bad for the heart?
What is it about bigger rats that's good for the heart?$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=16 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This is dealing with fatal diseases *unrelated* to heart problems (they actually strike earlier than heart problems do), so it has no power to tell us why small rats have a higher rate of heart problems.$lsat$),($lsat$B$lsat$,$lsat$The smaller the rat, the smaller the blood vessels, and thus the more likely the blood vessels will be clogged with fatty deposits.

It's common sense that clogged arteries are a common form of heart problem, and that having a "clogged vessel" in general is a bad thing.

The heart is the muscle that pumps blood, so we can connect "bad blood vessels" to "more heart problems".$lsat$),($lsat$C$lsat$,$lsat$The larger the rat, the less stressful its existence.

It's common sense that stress is hard on the heart, that people sometimes have heart attacks when they're undergoing lots of stress.

So it makes sense that less stress leads to less heart problems.$lsat$),($lsat$D$lsat$,$lsat$There is a common cause of being small and having heart problems: malnutrition.

Rats that suffer from malnutrition will be both smaller and have weaker hearts, and that can explain why the rate of heart problems amount smaller rates is higher (they have weaker hearts!)$lsat$),($lsat$E$lsat$,$lsat$Weirdly this brags at the start that it will be unhelpful in distinguishing larger rats from normal size.

But this is saying large rats have better cardiovascular conditioning than small rats, so it makes sense why large rats have a lower rate of heart problems than small rats.

This doesn't explain why large rats have fewer heart problems than average rats, but because it explained *something* it did still *contribute* to an explanation of the correlation between size and heart disease.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=156 AND q.section=2 AND q.question_number=16;

-- PT156-S2-Q23 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT156-S2-Q23$lsat$, 156, 2, 23, $lsat$Must Be True$lsat$, $lsat$When a resource’s price reflects its full cost to society,
 consumers pay directly for externalities—the unintended
 but harmful consequences to society of using a resource. Further, the price of a resource deters misuse of that
 resource only if it reflects the resource’s externalities. So, since sound management of a resource requires that
 the price of the resource deter its misuse, it also requires
 that the price reflect whatever unintended harm to the
 environment the use of that resource causes.$lsat$, $lsat$The conclusion follows logically if which one of the
 following is assumed?$lsat$, $lsat$A$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=156 AND s.section=2
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$Whatever constitutes unintended harm to the environment also constitutes unintended harm to society.$lsat$,$lsat$Correct$lsat$,true),($lsat$B$lsat$,$lsat$A resource's externalities are always taken into account in setting the price of that resource.$lsat$,$lsat$Unrelated to Goal$lsat$,false),($lsat$C$lsat$,$lsat$When setting a resource's price, it is possible to forecast completely and accurately all of the effects of using that resource.$lsat$,$lsat$Unrelated to Goal$lsat$,false),($lsat$D$lsat$,$lsat$If a resource is soundly managed, then its externalities are precisely assessed.$lsat$,$lsat$Unrelated to Goal$lsat$,false),($lsat$E$lsat$,$lsat$The price of a given resource is only one of several factors relevant to a decision about whether to use it.$lsat$,$lsat$Unrelated to Goal$lsat$,false)) v(l,t,g,c) WHERE q.preptest=156 AND q.section=2 AND q.question_number=23
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=156 AND q.section=2 AND q.question_number=23 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=23 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$Sound management of a resource requires that the price reflect whatever unintended harm to the environment the use of that resource causes.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$Sound management of a resource requires that the price deters misuse.

Deterring misuse requires that the price reflects the resource's externalities (the unintended but harmful consequences to society of using a resource).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The conclusion is trying to prove that "Sound management requires X", and the evidence has provided us with a conditional chain that says, "Sound management requires Y and Z".

Sound → price deters → reflects externalities
mgmt misuse (unintended but harmful
consequences to society)

Most *Sufficient Assumption* answers are trying to get us from **What We Know** to **What We Wanna Prove**.

We *know* from the evidence that sound management requires reflecting "the unintended but harmful consequences to society of using a resource", and we're trying to prove that sound management requires reflecting "the unintended harm to the environment".$lsat$),(3,$lsat$Goal$lsat$,$lsat$So we need to know that "in order to reflect the unintended harm to society, you'd have to reflect the unintended harm to the environment."

Since "unintended harm to the environment" is a *New Concept in the Conclusion*, it needs to be in our correct answer and we can pretty much flatly reject any answer that doesn't have it.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=23 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This is actually the only answer that uses the *New Concept in the Conclusion*, so even if we were massively confused on this question, we could guess this correct answer!

We wanted to know that, "In order to reflect the unintended harm to society, you'd need to reflect the unintended harm to the environment".

Conditionally, that could look like
*reflecting unintended → reflecting unintended*
*harm to society harm to environment*

*Meanwhile, the answer looks like*
*unintended harm → unintended harm*
*to environment to society*

So it's natural to worry that this is an Illegal Reversal of what we wanted. But modern Sufficient Assumption questions make you think more about the meaning of things, rather than just giving you perfect term matches.

Our prediction was about "reflecting"; this answer isn't.

This answer is saying that all unintended harm to the environment counts as unintended harm to society.

So if you didn't mention unintended harm to the environment, then you wouldn't be fully mentioning all unintended harm to society.

In order to fully account for (i.e. "reflect") all the unintended harm to society, you'd have to include unintended harm to the environment.

^ *that* was our prediction!$lsat$),($lsat$B$lsat$,$lsat$We need to know that "reflecting unintended harm to society" involves "reflecting unintended harm to the environment" (the New Concept in the Conclusion).

This never mentions *unintended harm to the environment*, so it can't possibly give us what we need.$lsat$),($lsat$C$lsat$,$lsat$We need to know that "reflecting unintended harm to society" involves "reflecting unintended harm to the environment" (the New Concept in the Conclusion).

This never mentions *unintended harm to the environment*, so it can't possibly give us what we need.$lsat$),($lsat$D$lsat$,$lsat$We need to know that "reflecting unintended harm to society" involves "reflecting unintended harm to the environment" (the New Concept in the Conclusion).

This never mentions *unintended harm to the environment*, so it can't possibly give us what we need.$lsat$),($lsat$E$lsat$,$lsat$We need to know that "reflecting unintended harm to society" involves "reflecting unintended harm to the environment" (the New Concept in the Conclusion).

This never mentions *unintended harm to the environment*, so it can't possibly give us what we need.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=156 AND q.section=2 AND q.question_number=23;

