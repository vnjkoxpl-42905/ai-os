insert into lr_explanation_steps (explanation_id,position,label,body) select v.e,v.p,v.l,v.b from (values
('3937fc73-7987-4439-80cc-6b64375df558'::uuid,1,'Goal','Since nothing forces any one author in or out, expect a conditional answer: K → ~L or its contrapositive, L → ~K.

Any answer that makes a flat claim about one author, or about how many authors appear, can be tested the same way: build a legal book that breaks it. If you can, it doesn''t have to be true.'),
('1df1c56c-2734-48a2-9856-6a70bf7258cb'::uuid,1,'Evaluate','Three conditionals. Is there a term they share?

Willingness to compromise shows up twice. Mediation requires it (first rule), and ideological conflicts lack it (third rule). That overlap is the hinge. Flip the first rule with its contrapositive and attach it to the third:

I → ~WC
~WC → ~M

So: I → ~WC → ~M.

What about litigation? L → SC shares no term with the other two. Being sure of your position never connects to compromise or ideology, so that rule is a dead end. Any answer that bridges it to the others is inventing a link.'),
('1df1c56c-2734-48a2-9856-6a70bf7258cb'::uuid,2,'Goal','Predict I → ~M: people in ideological conflicts should not undergo mediation.

Then watch for two traps: answers that start from a negated trigger or a necessary condition (those trigger nothing), and answers that try to connect the litigation rule to anything else.'),
('73c0e56c-6943-42cd-ac7c-f2720d27b25d'::uuid,1,'Evaluate','Look for the shared term. "Easier to limit, but not eliminate" is the result of the second sentence and the trigger of the third. That lets us chain them:

Listed → Easier to limit → Many people limit → Their health improves

Now the first sentence. It''s a fact, and it negates the start of the chain: caffeine content is not listed. A negated trigger tells us nothing, so the chain only describes what would happen if the content were listed. Any answer about what happens because it isn''t listed is going past the statements.'),
('73c0e56c-6943-42cd-ac7c-f2720d27b25d'::uuid,2,'Goal','Predict the chain from start to finish, kept hypothetical: if exact caffeine content were listed, some people''s health would improve.

Watch for answers that run the chain from "not listed," and answers that swap limiting for eliminating.'),
('fa9d395e-6f34-483b-8af6-e2d7a964a3f2'::uuid,1,'Evaluate','Three conditionals, and they overlap. More consumers is the result of the second and the trigger of the first. Higher profits is the result of the first and the trigger of the third ("not increase unless" puts lower congestion on the necessary side). Line them up:

↓CL → ↑C → ↑P → ↓TC

Read the chain like a one-way street. Anything on the left guarantees everything to its right. Nothing on the right guarantees anything to its left. Lower congestion is required for higher profits, but it doesn''t produce them.

The contrapositive runs the other way with every term negated: if congestion doesn''t fall, profits won''t rise, the number of residents won''t increase, and the cost of living won''t decrease.'),
('fa9d395e-6f34-483b-8af6-e2d7a964a3f2'::uuid,2,'Goal','Every answer is a conditional, so the test is direction. A correct answer moves left to right along the chain, or right to left with both sides negated. Expect something like ↓CL → ↑P, ↑C → ↓TC, or ↓CL → ↓TC.

Any answer that starts at ↓TC and claims something follows is backwards.'),
('fa360b2e-cdb0-4824-80b2-17740d6bbb08'::uuid,1,'Evaluate','What do the two claims share? Doubling in computing speed. Claim 1 ties each transistor doubling to a speed doubling. Claim 2 ties each speed doubling, in that window, to a cost doubling. Connect them through the shared term:

Transistors double → speed doubles → (mid-1990s into next decade) cost doubles

Now notice the limits. The cost fact covers only the mid-1990s into the next decade. Nothing tells us why costs doubled, what happened to the retail price of computers, what engineers were trying to do, or whether the pattern will continue.'),
('fa360b2e-cdb0-4824-80b2-17740d6bbb08'::uuid,2,'Goal','Predict the substitution, with its time window intact: from the mid-1990s into the next decade, each doubling in transistors came with a doubling in production cost.

Expect wrong answers to stretch past what was reported: the only way to raise speed, retail prices, engineers'' motives, or the future.'),
('92c75e79-e4b4-40b3-a28b-6e2b1286aeb1'::uuid,1,'Evaluate','The only conditional is the last sentence. Addictive substances have to be hard to quit for most users. Contrapositive: if withdrawal does not cause most users extreme difficulty, the substance is not addictive.

Now ask what the rejected test missed. A few users quitting tells us about some users. The requirement is about most users. Both can be true at once: a substance can be easy to quit for a handful and brutal for the majority. That''s exactly how the prime examples of addictive substances slip past the some-users test.

Notice also what the rule can''t do. It gives a requirement for addictiveness. It never says what is enough to make something addictive.'),
('92c75e79-e4b4-40b3-a28b-6e2b1286aeb1'::uuid,2,'Goal','Expect an answer that applies the requirement in the right direction, probably playing some against most: a substance some users quit easily can still be addictive, but only if most users have a hard time.

Be ready to reject answers that treat the requirement as sufficient, or that talk about one person instead of most users.'),
('6f0a8af5-c592-4ba7-b022-e821e909ea5d'::uuid,1,'Evaluate','Watch the modal words. Rule 1 says "are to be preserved": a requirement. Rule 2 says "may": permission, not a duty. Rule 3 also says "may." An answer that turns a "may" into a "should" goes beyond the manual.

Then watch the triggers. Rule 2 needs only one thing: archaic material from an older work that occurs frequently. Whether it interferes doesn''t matter. Rule 3 covers obvious typos in modern works, not archaic spellings. And the manual is silent about some cases, like an archaic form that occurs infrequently but does interfere. Neither rule 1 nor rule 2 triggers there, so nothing follows.'),
('6f0a8af5-c592-4ba7-b022-e821e909ea5d'::uuid,2,'Goal','Look for an answer that triggers a rule cleanly and keeps its strength. The likeliest shape: archaic spelling or punctuation from an older work that occurs frequently may be modernized. Extra details are fine as long as the whole trigger is there.')
) v(e,p,l,b) where not exists (select 1 from lr_explanation_steps x where x.explanation_id=v.e and x.position=v.p) returning id;