-- PT156-S4-Q13 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT156-S4-Q13$lsat$, 156, 4, 13, $lsat$Most Strongly Supported$lsat$, $lsat$If the natural history museum stays within this year’s
 budget, it will be unable to stay within next year’s
 budget, for renovating next year will make the museum’s
 expenditures exceed next year’s very tight budget. After
 all, the museum will have to renovate next year if it
 does not do so this year, because work from previous
 renovations is deteriorating rapidly.$lsat$, $lsat$The argument’s conclusion can be properly inferred if
 which one of the following is assumed?$lsat$, $lsat$D$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=156 AND s.section=4
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$The museum will stay within this year's budget.$lsat$,$lsat$No Impact$lsat$,false),($lsat$B$lsat$,$lsat$This year's budget is less than next year's budget.$lsat$,$lsat$Unrelated to Goal$lsat$,false),($lsat$C$lsat$,$lsat$The museum will not renovate next year.$lsat$,$lsat$Unrelated to Goal / Opposite$lsat$,false),($lsat$D$lsat$,$lsat$The museum will exceed this year's budget if it renovates this year.$lsat$,$lsat$Correct$lsat$,true),($lsat$E$lsat$,$lsat$The museum will stay within this year's budget if it does not renovate this year.$lsat$,$lsat$Reversal$lsat$,false)) v(l,t,g,c) WHERE q.preptest=156 AND q.section=4 AND q.question_number=13
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=156 AND q.section=4 AND q.question_number=13 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=4 AND q.question_number=13 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$If museum stays within this year's budget, it won't be able to stay within next year's budget.$lsat$),(1,$lsat$Premise (for)$lsat$,$lsat$Renovating next yr will make expenditures exceed next year's very tight budget.$lsat$),(2,$lsat$Intermediate Conclusion (after all)$lsat$,$lsat$If they don't renovate this year, they'll have to renovate next year.$lsat$),(3,$lsat$Premise (because)$lsat$,$lsat$Work from previous renovations is deteriorating rapidly.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$We can tell the first claim is the conclusion, because every claim after that is introduced by some Support indicator (for, after all, because --- awww, it's almost the whole FABS gang; Since must feel so left out).

So we're trying to prove/create this logic path:
*stay w/in won't stay*
*this yr's ---------------------------------> w/in next yr's*
*budget budget*

The first thing to ask ourselves is whether the premises already provided some sort of rule that would prove "don't stay within next year's budget".

They did!
*renov won't stay*
*next yr -----> w/in next yr's*
*budget*

So now we know we're trying to prove that they will renovate next year. Did the premises provide us with a way to prove that they'll renovate next yr?

They did!
*don't renov*
*renov ----> next yr*
*this yr*

So now we know we're trying to prove that they **won't** renovate this yr. Did they give us a way to prove that they won't renovate this yr?

Nope. The final claim, that previous renovations are deteriorating rapidly, is useless to us because it doesn't connect to this chain. They're asking us to prove that the museum won't be able to stay within next year's budget, and they've given us a mechanism to do so:

*don't renov don't stay*
*renov ----> next yr -----> w/in next yr's*
*this yr budget*

The correct answer is definitely making use of this conditional chain, and that 'deteriorating rapidly' premise doesn't interact with this chain at all, so we can ignore that.$lsat$),(5,$lsat$Goal$lsat$,$lsat$This is the logic path we want to create:

*stay w/in won't stay*
*this yr's ------------------------------------> w/in next yr's*
*budget budget*

This is what we have so far, from the evidence:

*don't renov don't stay*
*renov ----> next yr -----> w/in next yr's*
*this yr budget*

So the missing piece we need to add in order to build the logic path of the conclusion is:

*stay w/in don't*
*this yr's ---> renov*
*budget this yr*

We can also get ready for an answer saying the contrapositive version:

*do won't stay*
*renov ---> within this*
*this yr yr's budget*

The idea of "staying within this year's budget" is a *New Concept in the Conclusion*, so it needs to be in our correct answer. We can quickly ditch any answer that doesn't have it.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=156 AND q.section=4 AND q.question_number=13 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$This just speaks the *New Concept in the Conclusion*, but it doesn't connect it to anything.

The fact that the museum will say within this year's budget doesn't tell us anything. It doesn't activate any of the conditionals.

These are the ideas from the evidence

*- if don't renov this yr, have to renovate next yr*
- if renov next yr, won't stay within budget
- previous renovations are deteriorating rapidly

Saying "we're going to stay within this year's budget" doesn't interact with any of those claims. It goes nowhere.

A correct answer on SA will always interact with at least one premise in order to allow us to derive some inference.$lsat$),($lsat$B$lsat$,$lsat$This doesn't mention the *New Concept in the Conc* of "staying within this year's budget", so it's useless to us.

None of the premises mentioned that concept, so if the answer we pick ALSO doesn't mention that concept, then it would be impossible to derive a conclusion that involves that concept.$lsat$),($lsat$C$lsat$,$lsat$This doesn't mention the *New Concept in the Conc* of "staying within this year's budget", so it's useless to us.

Also this fundamentally weakens.

The way we're going to prove that we're unable to stay within next yr's budget is to say that we're going to renovate next year, and this is preventing us from saying that.$lsat$),($lsat$D$lsat$,$lsat$This is our prediction, but naturally it's **in contrapositive form**.

This says
"If renovate this year, then exceeds this year's budget"
and thus by contrapositive
"If stays within budget, then won't renovate this year".

That's what we wanted. This is the conclusion's logic path:
*stay w/in won't stay*
*this yr's ------------------------------------> w/in next yr's*
*budget budget*

This is what we have so far, from the evidence:
*don't renov don't stay*
*renov ----> next yr -----> w/in next yr's*
*this yr budget*

This answer adds this, which snaps onto the chain from the evidence, in order to prove the conclusion.

*stay w/in don't*
*this yr's ---> renov*
*budget this yr*

Conversationally, this says "staying within this yr's budget would require not renovating this year". We know that not renovating this year means we'll renovate next year. And we know that renovating next year means that we'll exceed next year's budget.

So we've proven that "staying within this yr's budget" leads to "exceeding next year's budget".$lsat$),($lsat$E$lsat$,$lsat$We wanted
"if stay within this year's budget, won't renovate this year".

This provides an illegal reversal of that:
"If not renovate this year, then stay within this year's budget"

This is what we were trying to create:

*stay w/in won't stay*
*this yr's ------------------------------------> w/in next yr's*
*budget budget*

This is what we have so far, from the evidence:
*don't renov don't stay*
*renov ----> next yr -----> w/in next yr's*
*this yr budget*

This answer adds this,

*don't renov don't stay*
*renov ----> next yr -----> w/in next yr's*
*this yr and budget*
*stay within*
*this yr's budget*

It doesn't allow us to create the desired logic path.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=156 AND q.section=4 AND q.question_number=13;

-- PT159-S1-Q10 (Unloaded)
INSERT INTO lr_questions (section_id, qid, preptest, section, question_number, question_type, stimulus, prompt, correct_choice, is_explained, source_note)
SELECT s.id, $lsat$PT159-S1-Q10$lsat$, 159, 1, 10, $lsat$Most Strongly Supported$lsat$, $lsat$A recent study found that most individuals believe that they sleep less than most other people. However, it is obviously not possible that most people sleep less than most other people. Therefore, _______.$lsat$, $lsat$Which one of the following most logically completes the argument?$lsat$, $lsat$E$lsat$, true, $lsat$Loaded 2026-09-27 from the LSAT Lab app (question API) by lsat-lab-sync.$lsat$ FROM lr_sections s WHERE s.preptest=159 AND s.section=1
ON CONFLICT DO NOTHING;
INSERT INTO lr_answer_choices (question_id, letter, choice_text, tag, is_correct)
SELECT q.id, v.l, v.t, v.g, v.c FROM lr_questions q, (VALUES ($lsat$A$lsat$,$lsat$some people believe things that could not possibly be true even in principle$lsat$,$lsat$Too Strong (even in principle)$lsat$,false),($lsat$B$lsat$,$lsat$most people are not aware of how much they sleep$lsat$,$lsat$Too Strong (most)$lsat$,false),($lsat$C$lsat$,$lsat$most people underestimate how much they sleep in comparison to others$lsat$,$lsat$Too Strong (most)$lsat$,false),($lsat$D$lsat$,$lsat$most people think that they do not sleep as much as they should$lsat$,$lsat$Out of Scope (should)$lsat$,false),($lsat$E$lsat$,$lsat$some people incorrectly believe that they sleep less than most other people$lsat$,$lsat$Correct$lsat$,true)) v(l,t,g,c) WHERE q.preptest=159 AND q.section=1 AND q.question_number=10
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=159 AND q.section=1 AND q.question_number=10 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=159 AND q.section=1 AND q.question_number=10 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Facts$lsat$,$lsat$*pivot tension* (however)

Most ppl think they sleep less than most other people.
but
it's impossible for most ppl to sleep less than most people.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$When we're doing MBT or Most Supported (like this one) and we see two claims put in tension with each other via a Pivot word, the correct answer almost always addresses that tension.

If we hear, "Most ppl think they are X, but it's impossible for X to be true of most ppl", it seems to force us to believe that some of them must be wrong.

It's impossible for them to all be correct, so some of the people who *think* they sleep less than most people don't actually sleep less than most people.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for the most provable answer. It will probably address the Pivot tension by conveying that "some of the ppl who think they sleep less than most are incorrect".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=159 AND q.section=1 AND q.question_number=10 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$We know that some people think
"I sleep less than most other people"
and are wrong about that belief.

But can we say that "I sleep less than most other people" can't possibly be true, even in principle?

No. That could definitely be a true claim for some people, so it could in principle be true.

Saying it isn't *actually* true is different from saying it couldn't even in principle be true.

If I were to believe that "most people sleep less than most other people", then I would be guilty of believing something that cannot even in principle be true. It's a self-contradictory claim.$lsat$),($lsat$B$lsat$,$lsat$We know that some of these people who think they sleep less than most others are wrong, but we can't prove that **most** of them are wrong.

Also, for them to be wrong, it doesn't have to be because they're unaware of how much *they* sleep. They might be unaware of how much most other people sleep.$lsat$),($lsat$C$lsat$,$lsat$We know that some of these people who think they sleep less than most others are wrong, but we can't prove that **most** of them are wrong.

This otherwise fits the gist of the paragraph. If you're thinking, "Compared to most other people, I get way less sleep" and you're *wrong*, then you are underestimating how much sleep you get in relation to others.

In case numbers would help, pretend there are 100 people, and most of them (51 of them) get at least 7 hrs of sleep per night.

49 of them get 6 hrs or less of sleep per night. Let's say that all 49 of those people (correctly) believe "I get less sleep than most".

If we grab two people from the 7+ hr group and say that they **also** believe "I get less sleep than most", then we'd have 51 people believing they get less sleep than most.

So **most** of our population believes they get less sleep than most.

But only 2 of them are actually wrong. Only 2 of them are underestimating how much sleep they get in comparison to others, not **most** of them, as this answer choice says.$lsat$),($lsat$D$lsat$,$lsat$We'd be very skeptical of this answer from the strength of MOST, but then we can definitely get rid of it when we see it's talking about how much sleep they *should* get.

That concept is not discussed at all in the stimulus.$lsat$),($lsat$E$lsat$,$lsat$If we know that most people believe that they are X, but it's impossible for X to be true of most people, then that means that at least some of them have an incorrect belief.

So at least some people incorrectly believe they sleep less than most other people.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=159 AND q.section=1 AND q.question_number=10;

