-- PT152-S2-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=152 AND q.section=2 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The lottery did not meet the fairness requirement.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The fairness requirement is that all entrants have an equal chance of winning.

90% of the winners selected by this lottery submitted their entry forms within the first 2 days of the 30 day registration.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Let's say there were 100 winners to this contest. If every day was equally likely to have contest winners, then there would be 3.3 winners per day for the 30 days the registration period was open.

Our author is picturing this math in her head, and saying if 90% of winners came from the first 2 days, it seems like every day wasn't equally likely to have a contest winner.

Of course the actual fairness rule is that "all **entrants** (not days) had an equal chance of winning". So why is it that the author thinks some entrants had a bigger / smaller chance?

She's assuming that there were a comparable number of entrants on each of the 30 days. If that were the case, then the people who submitted sometime between day 3 and day 30 would be like, "hey, how come only 10% of us won, but 90% of the people from day 1 and day 2 won?"

But if most people got their entries in right when the registration period opened, then we would expect a bigger percentage of winners to have come from that time period.

Pretend we have 1000 entrants over a 10 day period, 100 entries per day.
100, 100, 100, 100, 100, 100, 100, 100, 100, 100

If 90 of the 100 winners came from the first two days, that would seem fishy and unfair.

But suppose most of the entries came in the beginning of the 10 day period.
500, 400, 20, 15, 15, 10, 10, 10, 10, 10

Now, wouldn't we expect most of the contest winners to be people who submitted during the first two days? After all, 90% of the entries came in the first two days, so we'd expect 90% of the randomly drawn winners to come from the first two days.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this argument is vulnerable to one big mathematical objection (what if 90% of the entries were submitted in the first two days?), we should probably expect an answer that rules out that idea.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT154-S2-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=154 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evidence$lsat$,$lsat$As consumers’ desire for farmed salmon increases, the market for threatened wild salmon drops, which in turn leads to more wild fish being allowed to live and multiply freely.$lsat$),(1,$lsat$Intermediate Conclusion$lsat$,$lsat$Wild salmon numbers will increase.$lsat$),(2,$lsat$Main Conclusion$lsat$,$lsat$The best reason to prefer farmed salmon is ecological.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The evidence is generally about the popularity of farmed salmon leading to an increase in wild salmon numbers. Base on this, the conclusion claims that a preference for farmed salmon provides some ecological benefit.

What if the process of farming salmon somehow causes ecological harm? What if consumers' increased desire for farmed salmon is drastically increasing this harm? If any of this is true, it weakens the argument.

However, there's another potential flaw in the argument. There's potentially a gap between the evidence and the intermediate conclusion. If we have a reason to believe that "more wild fish being allowed to live and multiply freely" might not actually increase wild fish numbers, that weakens the argument.$lsat$),(4,$lsat$Goal$lsat$,$lsat$Keep an eye open for a correct answer that would weaken the argument in one of these two ways.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT156-S2-Q15 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT156-S2-Q15$lsat$, 156, 2, 15, $lsat$Flaw$lsat$, $lsat$People would not follow a leader if they felt that there
 was nothing they could gain by following that leader.
 Therefore, even those leaders who are incompetent or
 evil bring some good to their followers.$lsat$, $lsat$Which one of the following is most similar in its flawed
 reasoning to the flawed reasoning in the argument
 above?$lsat$, $lsat$A$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=156 AND s.section=2
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$Because people expound upon only theories they believe are true, any theory that is expounded upon by someone contains at least a grain of truth.$lsat$,$lsat$Correct$lsat$,true),($lsat$B$lsat$,$lsat$Because there is some good to be found in even the worst circumstances, the world's most vicious people must have brought about at least some good.$lsat$,$lsat$Bad Evidence Match / Topic Trap$lsat$,false),($lsat$C$lsat$,$lsat$To be a worthy leader, one must bring some good to people. Therefore, those who bring about some good make worthy leaders.$lsat$,$lsat$Bad Evidence Match$lsat$,false),($lsat$D$lsat$,$lsat$Because people can never completely separate what is true from what they wish to be true, no theory is ever completely true.$lsat$,$lsat$Bad Conclusion Match$lsat$,false),($lsat$E$lsat$,$lsat$Even leaders of scientific revolutions are influenced by the false theories of their predecessors.  Therefore, the influence of earlier false theories never completely disappears.$lsat$,$lsat$Bad Conclusion Match$lsat$,false)) v(l,t,g,c) WHERE q.preptest=156 AND q.section=2 AND q.question_number=15
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=156 AND q.section=2 AND q.question_number=15 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=15 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$Even incompetent or evil leaders bring some good to their followers.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If people felt there was nothing to gain from following a leader, they wouldn't follow them.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$By contrapositive, the premise is saying
"If you followed a leader, you felt there was something to gain from following them".

So we know that people who followed an evil or incompetent leader **felt** there was something to gain by following them.

But the conclusion is claiming that there **was** something gained by following them.

So this is a variation of the famous **Intent vs. Result** flaw (or **Belief vs. Fact**) People intended to gain something by following a leader, but whether that resulted in gain is another question.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The essence of that flaw is, "Just because they **felt** that X would be true doesn't mean that X was actually true". So we can look for arguments vulnerable to a similar objection.

If the answer were going to mirror the structure more, then we'd have an argument like,

*Prem: if ppl didn't believe X, then wouldn't do Y.*
*Conc: So when it comes to people who did Y, we know X is true.*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=2 AND q.question_number=15 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This works. We get a conditional saying,
"If you expound on a theory, you **believe** the theory is true."

And then a conclusion acting like the Belief is Reality.
"thus, the theories they expounded on are partially true".

The premise here doesn't need to be contraposed (a closer match would be "People wouldn't expound on a theory if they didn't believe it was true), but that doesn't matter. Contraposing is just equivalently rephrasing something, so it doesn't impact the logic.

The conclusion is similarly weak to the original one:
"bring **some** good" / "contains **at least a grain** of truth"

And the essence is the same:
"Just cuz they thought they'd gain something from following the leader doesn't mean that they DID gain something"

vs.

"Just cuz they thought the theory was true doesn't mean the theory IS true."$lsat$),($lsat$B$lsat$,$lsat$Since the premise here has nothing to do with someone's Belief / Intent, there's no way we'll be able to match it up with our flaw.

This is trying to get us with Topic/Word bait in the conclusion, because it's also talking about "at least some good".$lsat$),($lsat$C$lsat$,$lsat$Since the premise here has nothing to do with someone's Belief / Intent, there's no way we'll be able to match it up with our flaw.$lsat$),($lsat$D$lsat$,$lsat$To some extent, the premise is discussing what people believe, but the argument isn't treating that belief as fact. To the contrary, it's saying there is a gap between what *is* and what they believe.$lsat$),($lsat$E$lsat$,$lsat$To some extent, the premise is discussing what people believe (they believe the false theories of their predecessors), but the argument isn't treating that belief as fact. To the contrary, it's saying that those are **false** theories.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=156 AND q.section=2 AND q.question_number=15;

