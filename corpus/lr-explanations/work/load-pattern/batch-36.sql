-- PT159-S1-Q2 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT159-S1-Q2$lsat$, 159, 1, 2, $lsat$Method of Reasoning$lsat$, $lsat$Some have argued that using food crops to produce fuel represents an unprecedented attack on the food supply. It seems immoral to divert crops from the food supply while there is a need for food. But we currently divert crops from the human food supply to feed livestock. So the diversion of food to fuel is not actually a radical break with traditional practices.$lsat$, $lsat$The argument proceeds by$lsat$, $lsat$C$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=159 AND s.section=1
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$arguing that the bad consequences of a practice are outweighed by the good consequences of that practice$lsat$,$lsat$Bad Evidence Match$lsat$,false),($lsat$B$lsat$,$lsat$countering the charge that a practice has a bad consequence by trying to show that the practice does not actually have that consequence$lsat$,$lsat$Bad Evidence Match$lsat$,false),($lsat$C$lsat$,$lsat$rebutting a charge that a practice is radical by contending that the practice is analogous with an existing one$lsat$,$lsat$Correct$lsat$,true),($lsat$D$lsat$,$lsat$rejecting the charge that a practice is immoral by trying to undercut the moral foundation of the charge$lsat$,$lsat$Bad Evidence Match$lsat$,false),($lsat$E$lsat$,$lsat$supporting a moral objection to a practice by trying to show that the practice is actually different from practices that might seem similar$lsat$,$lsat$Bad Evidence / Conclusion Match$lsat$,false)) v(l,t,g,c) WHERE q.preptest=159 AND q.section=1 AND q.question_number=2
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=159 AND q.section=1 AND q.question_number=2 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=159 AND q.section=1 AND q.question_number=2 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Implied Rebuttal Conclusion (so)$lsat$,$lsat$It could be okay to use food crops to produce fuel.$lsat$),(1,$lsat$Intermediate Conclusion (so)$lsat$,$lsat$Diverting food to fuel isn't a radical break with traditional practices.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$We currently divert food crops to feed livestock.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The **big 3** most common moves on Method are Analogies, Faulty Implications, and Alternatives.

This argument seems to involve an Analogy. The author is saying that diverting food crops to produce fuel is analogous to diverting food crops to feed livestock.

It also involves the idea of a **Counterexample**. The opposing claim is that diverting food crops for fuel would be an **unprecedented** move, and the author is trying to argue, "No, there's precedent. Something we're currently doing is essentially the same."$lsat$),(4,$lsat$Goal$lsat$,$lsat$Let's pick any answer that is descriptively true. It will probably comment on the analogy or counterexample.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=159 AND q.section=1 AND q.question_number=2 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$Nothing in the evidence mentions the positive consequences of diverting food crops to produce fuel.$lsat$),($lsat$B$lsat$,$lsat$There isn't any change that a practice (diverting food crops to produce fuel) has a bad consequence. The charge is simply that it's immoral to use food that way, when there are people who need food to eat.

So naturally, the author never counters a charge that was never made.$lsat$),($lsat$C$lsat$,$lsat$This captures the counterexample and analogy components we anticipated.

The charge was that this proposal was an "unprecedented attack". That qualifies as saying that the proposal is **radical**.

And the author undermines that view by saying "it's **not a radical** break from tradition", since we analogously divert food crops to feed livestock.$lsat$),($lsat$D$lsat$,$lsat$The author's rebuttal is more about countering the idea that this is unprecedented / radical. She doesn't weigh in on whether it's immoral (it might also be immoral to divert food crops to feed livestock).

Nothing in her evidence addresses the morality of the proposal. The evidence only addresses how we currently do something similar.$lsat$),($lsat$E$lsat$,$lsat$The author never supports the idea that this is immoral, and she's trying to show that this new proposal is **similar** to other practices, not different.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=159 AND q.section=1 AND q.question_number=2;

