update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('f727e59c-bb83-41c7-a5f5-9b3b9f35113d'::uuid,'3707d89de9d0c0e14cb0eb0621b04ddc','Three statements, and two of them are conditionals ("must" and "no insect brain").

Instinctual behavior → no reasoning, far fewer nerve cells than flexible behavior
Capable of flexible behavior → large number of neurons
Insect brain → NOT a large enough number of neurons

One more fact hides in a parenthesis: noninstinctual behavior is "also called flexible." So there are only two kinds of behavior here. Behavior that isn''t flexible is instinctual.','Facts','Statements'),
('e3ecd26c-6ee4-45e6-b372-59815aabb17f'::uuid,'5f714ef466d67de47c932a3889d7bfdc','On Must Be True, conditionals and shared terms come first. Do any of these rules share a term?

Yes. The second and third both talk about a large number of neurons. The second says flexible behavior requires it. The third says insect brains don''t have it. Take the contrapositive of the second (NOT large number of neurons → NOT capable of flexible behavior) and attach it to the third:

Insect brain → NOT large number of neurons → NOT capable of flexible behavior

And since anything that isn''t flexible is instinctual, insect behavior is instinctual.

Notice what this chain can''t do. A large number of neurons is a requirement for flexible behavior, not a guarantee. So we know what lacking the neurons rules out. Having them proves nothing.','Evaluate','Evaluate'),
('62386109-6b6c-4f51-8d1b-13c3913491b4'::uuid,'546b92308a57140ae8082c4e204df2cb','Predict the end of the chain: insects can''t behave flexibly, so insect behavior is instinctual.

Expect traps that read the neuron requirement backwards, treating a large brain as enough for flexible behavior, or treating a small brain as the only route to pure instinct.','Goal','Goal'),
('7285cc2f-730b-43ea-9b38-8bee4d9fa61f'::uuid,'7f3b9dd555146ac91a9170922358b9d6','Three rules about which authors make the book.

1. At least one of Lind, Knight, and Jones is in. ("Lind, Knight, or Jones")
2. Not all three are in.
3. K → J

Rule 3 is the one with a consequence. Pick Knight and Jones comes along. Now we have two of the three, and rule 2 says the third can''t join. So:

K → J → ~L

Lind is blocked whenever Knight is in. Take the contrapositive:

L → ~K

Notice what we can''t say. Knight doesn''t have to be in. Lind doesn''t have to be in. A book with Jones alone breaks no rule, and neither does a book with Lind alone. Rules like these limit combinations. They don''t force any single author into the book.','Evaluate','Evaluate'),
('3255122f-8444-46fe-ae1e-0511d98cc1fd'::uuid,'2af9df59099d977ac16280798b153c0e','Only people who are **willing to compromise** should undergo **mediation** to resolve their conflicts.

M → WC

Actual **litigation** should be pursued only when one is **sure** that one''s position is **correct**.

L → SC

People whose **conflicts are based on ideology** are **unwilling to compromise**.

I → ~WC','Explanation','Statements'),
('01749785-9dae-492e-b4b5-e0d8f392ec68'::uuid,'cc1b1ded35b29a385f13da306c26a4cc','Although some nutritional facts about soft drinks are listed on their labels, exact caffeine content is not.
That''s a fact about today: caffeine content isn''t listed.

Listing exact caffeine content would make it easier to limit, but not eliminate, one''s caffeine intake.
Listed → Easier to limit

If it became easier for people to limit, but not eliminate, their caffeine intake, many people would do so, which would improve their health.
Easier to limit → Many people limit → Their health improves','Given','Given'),
('f5f44b74-357b-411f-83c9-46f59f9143e8'::uuid,'a020e58193951bcadf27d63cf29e5b65','Claim 1: For several decades, the number of transistors on new microchips has doubled about every 18 months, "and hence" so has computing speed. Each doubling in transistors brought a doubling in speed.

Claim 2: From the mid-1990s into the next decade, each doubling in computing speed was accompanied by a doubling in the cost of producing the microchip.','Given','Given'),
('af38ad5c-9a00-4b48-851c-5ffe93d4f3ed'::uuid,'4495273e3f9ceafa4661a7b7b48a37e9','The expert rejects a proposed test: "any substance that at least some habitual users can cease to use is nonaddictive." Used as the only criterion, that test would label some prime examples of addictive substances nonaddictive.

Then the expert gives a requirement that any adequate set of criteria must include. "Only if" introduces the necessary side:

Addictive → withdrawal causes most users extreme psychological and physiological difficulty','Given','Given'),
('4ac2e9e0-7b43-43d4-9eb3-577a3d26c8e0'::uuid,'529f73683461d4234e4bad282028ef98','Three rules from the style manual.

1. Older works: archaic spelling or punctuation that occurs infrequently and does not interfere with comprehension → preserve it.
2. Older works: archaic spelling or punctuation that occurs frequently → the editor may modernize it, with an explanatory note in the text, or, if similar modernizing was done in more than one quotation, a general statement in the preface.
3. Modern works: obvious typographical error → may be corrected without explanation.','Given','Given')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;