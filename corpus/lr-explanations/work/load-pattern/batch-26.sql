-- PT142-S1-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=142 AND q.section=1 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (hypothesis)$lsat$,$lsat$When squirrels puff up their tails, the tail heats up, which the snakes can detect through infrared sensing, which causes them to back off.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Snakes can be repelled by the way adult squirrels puff up their tails and wag them.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$As soon as we see the word "hypothesis" in our question stem, we know this will conform to the Explain Curious Fact framework.

CURIOUS FACT: why does the puffed squirrel tail repel the rattlesnake?
EXPLANATION: the snake senses the heat from the tail and doesn't like it$lsat$),(3,$lsat$Goal$lsat$,$lsat$We can strengthen by ruling out an **alternate explanation** or by boosting the **plausibility of the author's explanation**. The latter is much more likely on Strengthen questions. In particular, they love to boost plausibility with "no cause, no effect" answers. Here that would sound something like, "when the tail isn't hot / when they can't sense the heat, the snakes aren't repelled".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT146-S1-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=146 AND q.section=1 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It's flawed to think that because moral *codes* differ, that the morality that gives birth to these codes is fabricated by one's culture, not rooted in one's human DNA.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Some moral attitudes are shared across all cultures.

It's kind of analogous to food. There are universal tastes shared by all humans (like sweet and salty), but cultures differ when it comes to their *cuisines*.$lsat$),(2,$lsat$The Blank$lsat$,$lsat$We usually see some Conclusion or Support indicator language right before the blank or at the beginning of the sentence. In this case, the rhetorical language is the wind-up for an **Analogy**.

"And **just as** X can do Y, ... so too can W do Z."

So we know our job is to complete this analogy. The author's main agenda is saying that even though moral codes differ, morality might still be grounded in some universal nature.

She's using this analogy with food, so let's think about how the parts line up.

**FOOD MORALITY**
each culture has each culture has
the universal tastes certain shared
of sweet & salty moral attitudes

these universal tastes
provide the basis for ? ? ?
many different cuisines$lsat$),(3,$lsat$Goal$lsat$,$lsat$If we think about the author's overall conclusion that "even though moral codes differ, morality might still be grounded in some universal nature", then this analogy should be working its way back to talking about moral **codes**.

Moral codes are like cuisines (each culture's is different).
Moral attitudes are like tastes (shared across all cultures).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT146-S3-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=146 AND q.section=3 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Assuming what Grimes and the president said is true, the contract was violated.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$(Assuming the truth of their statements)
The contract states that a big change can't be made unless the president or a member of the legal department is told.

Neither the president nor Yeung was told about the big changes.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Okay, so we have a clearly defined goal -- *the contract was violated*.
To reach that verdict, we just have to establish that neither the president nor anyone on the legal team was told about the change in advance.

We already know that president wasn't told in advance.

So we just need to establish that no one on the legal team was told. We know that Yeung was not told, but who cares? We don't know if Yeung is on the legal team, and even if he is, we'd still need to ask the rest of the legal team if any of them were told about the big change.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We just need an answer to establish that no one on the legal team was told, either.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT147-S4-Q19 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=147 AND q.section=4 AND q.question_number=19 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (probably)$lsat$,$lsat$Neanderthals probably preserved meat found in many Neanderthal fireplaces.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Burnt lichen and grass have been found in N. fireplaces, and a fire of lichen/grass produces a lot of smoke but doesn't produce nearly as much heat/light as a wood fire.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$There is a missing link assumption somewhere, since "preserved meat" appears only in the Conclusion. What is "preserved meat" attached to in the Evidence?

Apparently, we're assuming that fires that produce a lot of smoke but not a lot of heat/light are good for preserving meat.

However, since we're interpreting the significance of archaeological evidence, we could also use our Curious Fact / Explanation mindset.

*Curious Fact*
What are all these burnt lichen/grass fires all about? They produce a lot of smoke, but they don't produce as much heat or light as a wood fire.

*Author's Explanation*
The lichen/grass smoky fires were created to smoke meat, for preservation.

We're supposed to react to this template by considering 2 different things:
- could there be an **Alternative Explanation** for this Curious Fact?
- how **plausible** is the Author's Explanation?

So why else might the Neanderthals have been burning smoky lichen/grass fires? Maybe they didn't have any wood, so this was the best they could get. Maybe it kept away some predators. Maybe it was for some other cooking purpose.

How plausible is the Author's Explanation? His story assumes that there was meat around, that Neanderthals were aware that if you smoked meat it would preserve for longer, that they had any need/use for preserved meat, etc.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Weaken, we want an answer to
**suggest** an Alternate Explanation for why they were making lichen/grass smoky fires,
or to
**hurt** the plausibility of the story that they were making these smoky fires in order to preserve meat.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT147-S4-Q2 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT147-S4-Q2$lsat$, 147, 4, 2, $lsat$Necessary Assumption$lsat$, $lsat$Acme’s bank loan must be immediately repaid in full if Acme’s earnings fall below $1 million per year. If Acme has to repay the entire loan immediately, it will have to declare bankruptcy. Acme had seemed safe from bankruptcy, having reported annual earnings of well over $1 million in each year it has had the bank loan. However, Acme has now admitted overstating its earnings for last year, so it will have to declare bankruptcy.$lsat$, $lsat$The argument requires the assumption that$lsat$, $lsat$A$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=147 AND s.section=4
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$Acme's earnings for last year, when accurately stated, are below $1 million$lsat$,$lsat$Correct$lsat$,true),($lsat$B$lsat$,$lsat$Acme has other debts besides the bank loan$lsat$,$lsat$Out of Scope (other debts)$lsat$,false),($lsat$C$lsat$,$lsat$last year is not the only year for which Acme overstated earnings$lsat$,$lsat$Too Strong (other overstated years)$lsat$,false),($lsat$D$lsat$,$lsat$Acme's earnings for the current year will fall below $1 million$lsat$,$lsat$Irrelevant Quality$lsat$,false),($lsat$E$lsat$,$lsat$Acme would be able to avoid bankruptcy if it did not have to repay the bank loan$lsat$,$lsat$Negation$lsat$,false)) v(l,t,g,c) WHERE q.preptest=147 AND q.section=4 AND q.question_number=2
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=147 AND q.section=4 AND q.question_number=2 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=147 AND q.section=4 AND q.question_number=2 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (so)$lsat$,$lsat$ACME will have to declare bankruptcy.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$ACME has overstated its earnings for last year.

If its earnings fall below $1 million per year, then its loan must be immediately repaid.

And if its loan must be immediately repaid, then it will have to declare bankruptcy.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument is trying to prove that ACME will have to declare bankruptcy, and it provided two conditional premises that end with that idea:

earnings fall loan must have to
below $1 mill → be immed → declare
this year repaid bankrupty

All the author has to do is tell us that ACME's earnings fell below $1 million last year.

Did she ever say that?

No. She only said that they admitted to overstating their earnings from last year.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for the missing Trigger Fact:
*their earnings fell below $1 million*

It's also possible they would present it as a Missing Link:
*if overstated last year's earnings, then earnings were below $1 million*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=147 AND q.section=4 AND q.question_number=2 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This is the fact that triggers bankruptcy, so the author needs to assume it's true in order to assume they'll have to declare bankruptcy.

If we negated this and said, "Their earnings last year were at least $1 million", then there'd be no reason to think they need to declare bankruptcy.$lsat$),($lsat$B$lsat$,$lsat$This argument is only about this bank loan, and this bank loan is enough to potentially trigger bankruptcy, so the author doesn't need to assume there are other debts.$lsat$),($lsat$C$lsat$,$lsat$The author doesn't need them to have overstated other years.

If they only overstated last year *and last year was less than $1 million*, then that would suffice to prove the conclusion about bankruptcy.$lsat$),($lsat$D$lsat$,$lsat$This is tricky, because this answer would be a sufficient assumption. If their earnings were below $1 million this year, then that would trigger immediate loan repayment, which would trigger bankrupcty.

But the author doesn't *need* their earnings to be below $1 million this year.

If this year's earning were $1.5 million, but last year's earnings were below $1 million, last year's low earnings would still be enough to trigger immediate loan repayment and thus bankruptcy.

So even though this would strengthen/prove, if true, it's not needed for the argument.$lsat$),($lsat$E$lsat$,$lsat$This is just an illegal negation of a premise.

The author said:
*if they have to repay loan immediately, then bankrupt*

This is saying:
*if they don't have to repay loan , then bankrupt*$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=147 AND q.section=4 AND q.question_number=2;

