-- Approved pilot, one slot per transaction.
BEGIN;
-- PT120-S4-Q9
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_questions q WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND q.stimulus=$pilot$Writer: I collaborated with another writer on my last book, instead of writing alone as I usually do. Because the book sold so well as a result of this joint effort, I should collaborate with a writer on my next book so that book will sell well too.$pilot$ AND q.prompt=$pilot$Which one of the following principles, if valid, most helps to justify the reasoning above?$pilot$ AND q.correct_choice=$pilot$C$pilot$) THEN RAISE EXCEPTION 'Question changed: PT120-S4-Q9'; END IF; END $guard$;
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND c.letter=$pilot$A$pilot$ AND c.choice_text=$pilot$If a person’s book sells well because of a collaboration, that person’s next book will sell well, if he or she collaborates with the same writer.$pilot$) THEN RAISE EXCEPTION 'Choice changed: PT120-S4-Q9 A'; END IF; END $guard$;
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND c.letter=$pilot$B$pilot$ AND c.choice_text=$pilot$A book sells well only if its author collaborated on the book with another writer.$pilot$) THEN RAISE EXCEPTION 'Choice changed: PT120-S4-Q9 B'; END IF; END $guard$;
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND c.letter=$pilot$C$pilot$ AND c.choice_text=$pilot$If a person’s book sells well because of a collaboration, future collaborations on the part of that person will produce other books that sell well.$pilot$) THEN RAISE EXCEPTION 'Choice changed: PT120-S4-Q9 C'; END IF; END $guard$;
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND c.letter=$pilot$D$pilot$ AND c.choice_text=$pilot$Writers who do not collaborate on books have a smaller chance of writing a book that will sell well.$pilot$) THEN RAISE EXCEPTION 'Choice changed: PT120-S4-Q9 D'; END IF; END $guard$;
DO $guard$ BEGIN IF NOT EXISTS (SELECT 1 FROM lr_answer_choices c JOIN lr_questions q ON q.id=c.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND c.letter=$pilot$E$pilot$ AND c.choice_text=$pilot$Writers who collaborate on books, if they are good writers, usually produce books that sell well.$pilot$) THEN RAISE EXCEPTION 'Choice changed: PT120-S4-Q9 E'; END IF; END $guard$;
DO $guard$ BEGIN IF (SELECT COUNT(*) FROM lr_explanation_steps s JOIN lr_explanations e ON e.id=s.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND e.style IN ('single','standard')) <> 0 OR (SELECT COUNT(*) FROM lr_explanation_choice_notes n JOIN lr_explanations e ON e.id=n.explanation_id JOIN lr_questions q ON q.id=e.question_id WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND e.style IN ('single','standard')) <> 0 THEN RAISE EXCEPTION 'Explanation changed: PT120-S4-Q9'; END IF; END $guard$;
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND NOT EXISTS (SELECT 1 FROM lr_explanations e WHERE e.question_id=q.id AND e.style IN ('single','standard')) ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body) SELECT e.id, v.position, v.label, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES (0, $pilot$Conclusion (should = opinion)$pilot$, $pilot$I should collaborate with a writer on my next book, so it will sell well too.$pilot$), (1, $pilot$Evidence (because)$pilot$, $pilot$My last book was a collaboration, and it sold well *because of* that collaboration.$pilot$), (2, $pilot$Evaluate$pilot$, $pilot$On Principle-Strengthen, we prephrase a rule that sounds like "If premise, then conclusion." So in this case:
```
my book sold well    →   collaborating again will
because of a             make my next book sell
collaboration            well (so I should)
```
Notice the conclusion says collaborate with *a* writer, not the same writer. Our principle has to cover any collaboration.$pilot$), (3, $pilot$Goal$pilot$, $pilot$Look for a rule whose trigger matches our evidence (a book sold well because of a collaboration) and whose outcome delivers our conclusion (future collaborations will produce books that sell well).$pilot$)) v(position,label,body) WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND e.style='single' AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body) SELECT e.id, v.letter, v.body FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id CROSS JOIN (VALUES ($pilot$A$pilot$, $pilot$This rule would look like this:
```
book sold well because    →   next book sells well
of a collaboration            IF same co-writer
```
The trigger applies. And to be fair, (A) helps a little: working with the same co-writer again is one way to "collaborate with a writer." But (A) only backs that one version. The writer's conclusion is broader. It says collaborating with a writer, any writer, will make the next book sell well. (A) says nothing about a new partner, so it justifies a narrower plan than the one the writer states. (C) covers the whole conclusion, so (C) helps more.$pilot$), ($pilot$B$pilot$, $pilot$This is the most popular wrong answer. Diagrammed:
```
book sells well    →   author collaborated
```
So yes, if the writer wants the next book to sell well, he'd better collaborate. But the conclusion also promises that collaborating means the book "*will* sell well." (B) never promises that. It only says you can't sell well *without* collaboration. Collaboration could be required and still not be enough.

(B) also ignores the writer's evidence completely. His reasoning is "collaboration *caused* my last book's success." (B) would make that evidence pointless.$pilot$), ($pilot$C$pilot$, $pilot$```
book sold well because    →   future collaborations
of a collaboration            produce books that sell well
```
Does the trigger apply? Yes: his last book sold well because of the collaboration. Does the outcome deliver the conclusion? Yes: if he collaborates on the next book, it will sell well. Both halves match, word for word.$pilot$), ($pilot$D$pilot$, $pilot$A "smaller chance" of selling well without collaboration doesn't mean collaboration will make the next book sell well. It only compares odds. The writer's conclusion is confident: the next book *will* sell well.$pilot$), ($pilot$E$pilot$, $pilot$```
writer collaborates + is    →   usually produces
a good writer                    books that sell well
```
Does the trigger apply? We don't know whether our writer is a good writer. And "usually" is weaker than the writer's conclusion. Two strikes.$pilot$)) v(letter,body) WHERE q.qid=$pilot$PT120-S4-Q9$pilot$ AND e.style='single' AND NOT EXISTS (SELECT 1 FROM lr_explanation_choice_note