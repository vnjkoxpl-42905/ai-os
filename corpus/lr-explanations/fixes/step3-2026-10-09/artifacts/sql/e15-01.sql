update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('0784c1a8-17e4-4f09-b84d-9d2771c21dbe'::uuid,'0a5549b12e260e6a2e30f9584705c77a','Chain the first two premises: `accepted → distributor buys → recoup`. So acceptance is one way to guarantee the backers get their money back.

Now look at the fact we''re given: this film was not accepted. That negates the very first condition in the chain. What does a rule tell us when its trigger is missing? Nothing. The rule describes films the committee accepts. It is silent about films it turned down.

How could the backers still recoup? A distributor could find the film somewhere other than this festival, or the film could earn its money back some other way. Nothing in the premises rules that out.

So the author has taken `accepted → recoup` and concluded `~accepted → ~recoup`. That''s an illegal negation: denying the sufficient condition and then denying the necessary condition too.','Evaluate','Evaluate'),
('644c3ff2-f372-4a52-b5df-e2ac4855c463'::uuid,'eebbedac3583625007c8edba445011d1','Because the stimulus is built from conditionals, we can match structure without arguing about content. We want this recipe:
```
P1: A → B
P2: B → C
P3: ~A
Conc: ~C
```
Two rules that chain, a fact that negates the first condition, and a conclusion that negates the last outcome. Any answer that runs a chain correctly (forward from A, or backward from ~C) is valid, so it can''t be our match.','Goal','Goal'),
('3b09f457-6f4e-41a2-a1ad-30dcd8e3b300'::uuid,'5b78f50ee91302cc26382767b9f9509e','Devan does not meet any of these basic criteria for friendship: Devan has never bothered to be kind to the speaker, and has never offered help or companionship.','Evidence (since)','Evidence (since)'),
('d26f253b-a72f-40df-8a3f-8c40a85aad70'::uuid,'4d5ad7e884609949410a1ce8960bcbf9','How would we object to this conclusion? Given that Devan has never been kind, never offered help, and never offered companionship, how could we argue that Devan is not the speaker''s enemy?

Easily. Failing the test for "friend" doesn''t put someone in the opposite category. There''s a lot of room between friend and enemy: a stranger, an acquaintance, a neighbor who never thinks about the speaker at all. An enemy is someone working against you. Nothing in the evidence says Devan has done anything against the speaker.

So the author treats two opposites as if they were the only options. That''s a false choice: the evidence shows Devan is not at one extreme, and the conclusion puts Devan at the other.','Evaluate','Evaluate'),
('09a4986f-7a40-41a5-a887-eecf63025b43'::uuid,'b8edb21a2dfcb4227ab12ffa5677daeb','Let''s look for an argument that shows something lacks the marks of one extreme, then concludes it belongs at the opposite extreme, skipping the middle ground. For example: Jim meets none of the criteria for best employee, so Jim is the worst employee.

The direction can flip (no sign of the bad extreme, so the good extreme) and the topic will change. The quick test for each answer: is there a sensible middle option that the conclusion ignores?','Goal','Goal'),
('8504a9b1-f245-4975-8778-7556d38957de'::uuid,'265c99b04f5aa41afc01e9a27c86509f','Start with what the premises do prove. Some freelance journalists sell to magazines with lax standards. No self-respecting writer sells to those magazines. So those particular freelance journalists can''t be self-respecting writers. That gives us: some freelance journalists are not self-respecting writers.

The author flipped it: some self-respecting writers are not freelance journalists. That''s a different claim, and the evidence doesn''t support it. Picture a world where every self-respecting writer happens to be a freelance journalist, and the journalists who sell to lax magazines are the other ones. Every premise is still true, but the conclusion is false.

We don''t need to name the flaw perfectly to match it, though. When a Parallel Flaw stimulus has quantifiers and repeating ideas, write an algebraic recipe. Let A = freelance journalists, B = sells work to magazines with lax editorial standards, C = self-respecting writers.','Evaluate','Evaluate'),
('2fd14b45-5190-46f6-9dd3-a188aa5c3469'::uuid,'fdfdbe005367c1702f5368357ccea955','Let''s look for something with this formula.
```
Premise 1: Some A''s are B.
Premise 2: No C''s are B.
Conclusion: Some C''s are not A.
```
In particular, we should see two premises (a Some and a No) that share the B idea, and a Some-not conclusion about the group from the No premise. Watch for the valid version, "Some A''s are not C." It has every ingredient but fixes the flaw, so it can''t be our match.','Goal','Goal'),
('3af3fb66-9fbb-4a9f-8969-596fe0678c0d'::uuid,'6fc0f7f9fa7c90db3a8a7ad0e92e4245','Because there are quantifier and conditional words like "Every" and "no", it makes sense to think about diagramming this argument somewhat algebraically.

There are also overlapping ideas (well-behaved is in all three claims, training is in two, Labradors are in two), which also argues for an algebraic approach.

With a strong structural recipe, we might find the correct answer just by matching parts. But this conclusion is causal, so let''s be clear about why we object to it.

How could we argue with the conclusion? We know training is required for good behavior. But required doesn''t mean it''s the whole story. Couldn''t a Labrador''s genes also play a role? A trained dog with a calm temperament might behave well, while a trained dog without one might not. The author''s conclusion picks one cause and throws out the other, when the evidence only shows that training is one necessary ingredient. Both factors could be at work.','Evaluate','Evaluate'),
('07295199-3b8c-4852-a42b-7a1b932528e6'::uuid,'259c70f57f955bc6e0800ea47dffe4f4','Look for the same valid move: a rule with two necessary conditions joined by "and", a fact confirming one of them, a fact denying the other, and a conclusion that the sufficient condition fails.
```
X → A and B
A
~B
Conc: ~X
```
Watch for two near-misses: the "and" sitting on the sufficient side of the arrow (if A and B, then X), and answers where both conditions are met, since meeting necessary conditions never proves the sufficient one.','Goal','Goal'),
('1c56b3ae-ebf1-4678-8be1-fa0edbd01ed0'::uuid,'671deccbfa8dfcec815cf539360c7a91','The proportion of full-length science-fiction films that are commercially successful is higher than the proportion of short documentary films that are commercially successful.','Conclusion','Conclusion'),
('30307406-fc89-436d-8539-c1da8d142d60'::uuid,'f75cce7a120f24f3d887808fae28ce65','Let''s take notes: `# succ short doc < # succ FL sci-fi`, `# short doc > # sci-fi`, therefore `% succ FL sci-fi > % succ short doc`.

The evidence talks about numbers, and the conclusion talks about proportions. That shift often signals a flaw, but here it works. Short documentaries have fewer hits and more films. Fewer successes spread over a bigger group has to be a smaller share. Try numbers: 100 short documentaries with 5 hits is 5%; 50 science-fiction films with 10 hits is 20%.

Now notice a modifier shift. The first premise and the conclusion say "full-length science-fiction films," but the middle premise says only "science-fiction films." That''s harmless too: if short documentaries outnumber all science-fiction films, they also outnumber the full-length ones.

So the argument is valid. We need an answer with the same valid shape: fewer successes in the larger group, so a lower proportion in that group.','Evaluate','Evaluate'),
('47672b3d-99ba-4d1d-8cf3-8d7d7f683885'::uuid,'7c43688ac55fbfa1fb9b1bbde101983b','Look for an answer with these pieces in these roles:
```
P1: Group X has fewer successes than Group Y.
P2: Group X is larger than Group Y.
Conc: Group Y has a higher proportion of successes.
```
The two premises must point in opposite directions (fewer hits, more members), and the proportion claim must be the conclusion, not a premise. If two answers survive, the modifier pattern breaks the tie: the middle premise drops the modifier that the first premise and the conclusion use.','Goal','Goal'),
('f04fb107-82ee-43c2-8c06-8cd429300110'::uuid,'56b550dfb68ef1f5c6c0a25c617fa7a4','```
If you complete 24
graduate credits
and a thesis in our
department, you
are eligible to
receive a master''s
degree.                  24 GC and T → EM
Roger has
completed 24
graduate credits
in our department        24 GC
yet Roger is not
eligible to receive
a master''s degree.       ~EM
So Roger must not
have finished the
thesis yet.              ~T
```','Evidence','Evidence'),
('ce3ce8f9-c18a-478b-9482-8f771a498090'::uuid,'059a9b56f0acb8a65a5ebae76a5663f6','The argument has one conditional premise with "and" in the sufficient condition: 24 GC and T → EM. A second premise fulfills one part of the sufficient condition: 24 GC. A third premise states that the necessary condition is not true: ~EM. The conclusion states that the second sufficient condition must not have been met: Therefore, ~T.

This is valid. The contrapositive of the rule is ~EM → ~24 GC or ~T. Roger is not eligible, so at least one part is missing. The credits are done, so the thesis must be the missing part.','Evaluate','Evaluate'),
('2b6dd56f-9b93-4a93-96e2-24aa919cf549'::uuid,'18645c6a00aafbfc2b2fc23c78d68a67','Look for this recipe:
```
(A and B) → C
A
~C
Conc: ~B
```
A rule where two conditions joined by "and" together guarantee a result, one condition confirmed, the result denied, and a conclusion that the other condition failed. Expect several answers built from "and", "or", and if-then; only one puts each piece in the same role.','Goal','Goal'),
('dae977ee-437c-422b-92e2-77b07b511064'::uuid,'ed0d47ac395779a1e4d45432e3818bf8','This is a reasonable argument, built on a dispute between two sources.

The reporter says the tracks are in poor condition. The inspector says they''re in good condition. Who should we believe?

The author doesn''t claim to settle it. The conclusion is modest: we should be suspicious of the reporter''s claim. Why lean toward the inspector? The inspector recently and thoroughly checked the tracks, and has no bias in the matter. Direct examination plus no stake in the outcome gives the inspector''s testimony more weight than the reporter''s claim.

Notice the conclusion''s strength. It doesn''t say the tracks are definitely fine. It says to be suspicious of the opposing claim.','Evaluate','Evaluate'),
('c4d869c5-7a8f-4996-810b-9fe73e1797b4'::uuid,'30730fc12afca55dc96e416a236a91be','Let''s look for an argument where an unbiased source who examined the thing directly contradicts someone else''s claim, and the conclusion is that we should doubt that other claim. Check three pieces: no bias, a careful examination, and a conclusion that casts doubt on a rival claim rather than proving the opposite.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;