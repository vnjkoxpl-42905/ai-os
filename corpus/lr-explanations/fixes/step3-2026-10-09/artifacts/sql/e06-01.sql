update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('48db2e4a-ddf3-48ca-b47e-83cf548f3ec8'::uuid,'0a0c976ee4c09b47d542216f7ac5d362','Public figures'' private correspondence and diaries are meant to be confidential when written, but they later become biographers'' principal sources. In the future, most such documents are likely to be stored as encrypted text, which can be opened by password only.','Evidence','Evidence'),
('b1263c88-23c0-4741-b8db-d358aca86a38'::uuid,'d0c541810b81496af94848989e808dff','On Main Conclusion, read with one expectation in mind: the conclusion usually arrives before its support. Most of the time it is the first sentence or the sentence right after a pivot like "however."

So test the first sentence. It is a prediction: encryption "will bring the writing of biographical history virtually to an end." Nobody can observe the future, so a prediction is an opinion, and an opinion needs support. Ask: why should we believe that? The rest of the paragraph answers. Diaries and letters are the biographers'' main sources. Those documents will likely be encrypted. So historians without passwords will lose the best material. Every later sentence is a reason for the first one.

Notice the chain has two levels. The "so" claim (historians will lose the revealing material) is itself a conclusion, supported by the encryption premise. But the argument does not stop there. Losing that material matters because it ends biographical writing. When one conclusion supports another, the one that supports nothing further is the main conclusion.','Evaluate','Evaluate'),
('8fc0988e-af43-4bb4-9943-667e173bd4fd'::uuid,'687611a9181081b7f4e8dd4a9dc04404','Find a meaning match for the first sentence: widespread encryption will bring the writing of biographical history virtually to an end. "Virtually to an end" means almost stopping, so a matching answer can say it will nearly stop, sharply decline, or cease.

Expect traps that restate the encryption premise or the "so" claim about historians losing access. Both sit on the path to the conclusion, but neither is where the argument ends up.','Goal','Goal'),
('5b615769-97c6-4cf3-890c-223b39d4fef0'::uuid,'5546e0e4718a5113c19f0ecf86f92778','Radioactive elements are unstable, so most of them decay within at most a few million years into other, nonradioactive elements. Yet there is an abundance of radioactive elements in the universe today.','Evidence','Evidence'),
('45dbc0d9-a286-424f-a410-af0ebba07c3e'::uuid,'f14c81b3b5a374fdad0d680b2f157c46','On Main Conclusion, expect the conclusion before its support. It is usually the first sentence or the sentence after a pivot.

The first sentence hedges: radioactive elements "may have been created when the universe began." Here that "may" claim is a concession, not something the author sets out to prove. Then the pivot: "However, even if this occurred, these elements are clearly still being created in the universe today." "Clearly" marks the author''s own view. Check it with the support test: why should we believe new radioactive elements are being created?

The rest of the paragraph answers that question. Most radioactive elements decay within a few million years. So if none had been made since the beginning, almost none would be left. But there are plenty left. Lined up:

No new elements created after the beginning → almost none left today
Not almost none left (there is an abundance)
So: new elements have been created

That is the contrapositive at work, and it lands exactly on the second sentence.

The final sentence starts with "So," which tempts us to call it the conclusion. It is a conclusion, but an intermediate one: it is drawn from the decay premise and then used to prove the second sentence. On Main Conclusion, the last sentence is rarely the answer, so check it before you trust it.','Evaluate','Evaluate'),
('700bf360-94ed-427f-8d38-5d5c17e0cfcf'::uuid,'f2aae07c3fb60c19801696d97dbd4b24','Look for a meaning match for the second sentence: "these elements are clearly still being created in the universe today." Swap the pronoun for what it refers to: radioactive elements are still being created today. The answer does not need "clearly" or the "even if" clause.

Expect traps built from the "So" sentence, the decay premise, and the opening concession.','Goal','Goal'),
('9f682a5c-e6e2-4a79-a868-713cb9886c6d'::uuid,'3ff85f01eaec964f7130cff3ec3aa687','On Main Conclusion, expect the conclusion to come before at least some of its support. Most of the time it is the first sentence or a rebuttal after a pivot.

This one is the rebuttal. The first sentence is a fact: people are debating what caused the recession. Nothing supports it, and nothing needs to. Then the pivot: "It is a mistake, however, to assume..." That is the columnist taking a side.

To confirm, run the support test: why should we believe that answering the cause question is not essential? The next sentence opens with "after all," a support indicator, and gives a reason. Corrective lenses treated myopia well before anyone knew the cause was genetic. So a problem can be treated without knowing its cause.

The four support indicators to listen for are for, after all, because, and since (FABS). When one of them opens a sentence, the claim right before it is usually what it supports.','Evaluate','Evaluate'),
('f8fa244a-1b9a-4460-9863-0be7715e6e60'::uuid,'13ce34ae2e47d5f3dda100706bdc578d','When we have rebuttal-style conclusions, take an extra second to state the author''s position in the words of the position being rebutted. For example, if we hear, "Some people think that ketchup is a vegetable. However, they''re wrong," then the conclusion is "Ketchup is not a vegetable."

Here the opposing position is: "We need to figure out what caused the current recession in order to improve the economy. It''s essential." The columnist says that is a mistake. It''s not essential. You could improve the economy even if you never figured out what caused the recession.

Notice what kind of claim that is. "Essential" means required, so the columnist is saying knowing the cause is not necessary for improvement. Find the answer that says knowing the cause is not required, and nothing stronger.','Goal','Goal'),
('483bda78-e7ed-4f1e-a8b7-047836ea4211'::uuid,'c4faa171371e6907cbba61c063ea4c5a','Railroads rely increasingly on automation. Since fewer railroad workers are needed, operating costs have been reduced. The chief competitor of railway shipping is shipping by truck, and no reduction in operating costs is predicted for the trucking industry.','Evidence','Evidence'),
('5fd7255e-a2d2-42b3-9ba9-1cfa1f76ea10'::uuid,'c130a8f40fbb7ec8c7a305ee6ed4b49c','On Main Conclusion, expect the conclusion before at least some of the evidence. Usually it is the first sentence or a rebuttal after a pivot.

This one breaks the usual pattern. The first sentence is a plain fact about automation, and nothing argues for it. The second sentence is a claim about costs, supported by the worker reduction ("Since fewer railroad workers are needed"). The third sentence is the first one that sounds like the author looking ahead: "This means that we can expect the volume of freight shipped by rail to grow." "We can expect" is a prediction, and "This means that" tells us it is drawn from what came before.

Run the support test. Why should we believe rail freight will grow? Because rail''s costs went down. Then the last sentence adds a second reason after the conclusion: trucking, the main competitor, is not getting cheaper. So the conclusion sits in the middle, with support on both sides.

Phrases like "this means that," "this shows that," and "this suggests that" can mark a main conclusion just as well as "therefore." Don''t assume the conclusion has to be the first or last sentence.','Evaluate','Evaluate'),
('a44ddbaa-7d85-4d10-90b1-628b7856ef8c'::uuid,'986195cd4763cf85c1e430735f845b46','Find the answer that matches the third sentence: rail freight volume is expected to grow. Watch for answers that restate the cost claim or the trucking premise. They are reasons for the prediction, not the prediction.','Goal','Goal'),
('16dc0f84-9a71-46ad-b41d-fd85cadbad55'::uuid,'5faf56195adcd505c8d93e2400ed1161','Whenever we do Main Conclusion (or Role), we remind ourselves that 90% of the time, the conclusion will be the first sentence or it will be a rebuttal.
In this argument, the first sentence is clearly factual, not the author''s opinion, so it''s not a First Sentence Conclusion.
And when the second sentence begins with an attribution, "Some scientists claim", we would anticipate a Pivot into a Rebuttal.
Sure enough, we get "However, this conclusion is far from justified". The last sentence provides factual support. We can tell the last claim is factual because it is prefaced by "it is known that".

Confirm with the support test: why should we believe the scientists'' conclusion is far from justified? Because natural cycles of ocean temperature can last 60 years or more, so a 15-year warming trend could be part of one. That is a reason to doubt the scientists'' explanation, not proof that it is false. So the climatologist''s conclusion is about the evidence: the human-pollution explanation has not been established.','Evaluate','Evaluate'),
('040f7ebc-2ab8-4f5d-a00f-e1748dd5dc72'::uuid,'40c8ae0e2245a562b159d77895f46e14','Rossi states a general principle ("It is undemocratic for people to live under a government in which their interests are not represented") and applies it to children: since children''s interests are sometimes different from their parents'', children should have the right to vote.','Rossi''s argument structure','Rossi''s Argument'),
('64ff2094-a2ad-452d-b663-2ae8fe80efbf'::uuid,'71b24f58affa375a5e462c627508f952','The stem asks only about Rossi, so Smith''s reply is background here. Read Rossi''s two sentences as conclusion plus evidence.

Conclusion: children should have the right to vote.
Evidence: it is undemocratic for people to live under a government that does not represent their interests, and children''s interests are sometimes different from their parents''.

Now characterize the evidence. The first sentence is not about children at all. It is a broad rule about all people: if your interests are not represented, your situation is undemocratic. The second sentence plugs children into that rule. Their interests can differ from their parents'', so the parents'' votes do not fully represent them, so by the rule children need a vote of their own.

That is one of the standard Method moves: state a general principle, then apply it to a specific case. Other common moves are analogy, counterexample, ruling out alternatives, and raising an overlooked consideration. None of those fits Rossi. There is no comparison case, no exception, and no rival explanation.','Evaluate','Evaluate'),
('9ed8ab00-1856-4758-ac73-2673fa84fbef'::uuid,'300b0778f7dac6a8e42871cf0b4e8a82','Look for an answer saying Rossi relies on a general principle, or applies a broad rule to a specific group. Check every answer against Rossi''s argument only. Smith''s reasoning is the source of at least one trap.','Goal','Goal'),
('da224888-545e-40ea-91c7-476774fdb2d6'::uuid,'7d53604392010fbdaab9af8dc96760dc','The ad''s structure is an analogy: pride causes Austin Stables to outperform competitors in horse racing; Barr has the same tradition of pride; therefore Barr should outperform its competitors in cars. The ad reaches its conclusion by drawing a parallel between two different industries based on a shared trait.

The sentence "Such a tradition of pride is not only found in the business of horse racing" is the bridge. It tells us the ad wants pride''s payoff in one business to carry over to another. That is how an analogy works: what is true of one case is claimed for a similar case.

On Method, run the "argues X by Y" test on every answer: X has to match the conclusion and Y has to match the evidence. Here X is that Barr will beat its competitors, and Y is a comparison to a stable whose pride made it a winner. An answer that gets either half wrong is out.','Evaluate','Evaluate'),
('a317e1e5-ab37-4e5b-bbab-d8b82a2d5887'::uuid,'a19b42b50b23ea070d39db288d13638d','Pointing out that the correlation (people tend to gesture less when they talk about abstract rather than physical concepts) is far from universal is not enough reason to reject the researchers'' claim.','Conclusion','Conclusion'),
('19f9c71a-58b8-411d-8e59-a606c1293ce5'::uuid,'2040fcc203ec7348999a5321a051346a','Some people perceive words like "comprehension" as expressing a physical action, like grasping something, rather than a state of understanding, which is abstract.','Evidence (because)','Evidence (because)'),
('cf1bccc3-eaff-40dc-85d7-d20d5fbc952f'::uuid,'1d92c7c8b2e296ca774c1443d6e0aea7','Start with what the author is responding to. Researchers say people tend to gesture less when they talk about abstract concepts. A critic could point out exceptions: people who gesture while discussing something abstract. The author says exceptions like that are not enough to throw out the claim.

Why not? Because some of the exceptions may not be exceptions at all. Take someone who gestures while talking about comprehension. That looks like a strike against the researchers, since comprehension, as a state of understanding, is abstract. But if that person thinks of comprehension as grasping something, a physical action, then the person is talking about a physical concept, and gesturing is exactly what the researchers'' claim predicts.

So the author keeps the generalization and explains away the counterevidence. The cases that seem to break the pattern are reclassified using a fact about how people perceive words. Notice that the author never says the correlation is universal and never brings in new support for it. The job is defensive: show that the apparent exceptions do not hurt the claim.','Evaluate','Evaluate'),
('d4decaa6-f9e5-49e7-9cc9-94df1d943950'::uuid,'b5f5d21b4076f1128e9c49137023cdbe','Use "argues X by Y" on every answer. X should match the conclusion: the researchers'' claim survives the objection that the correlation is far from universal. Y should match the evidence: a fact about how some people perceive certain words.

In Method terms, the author answers a counterexample by giving it an alternate explanation that fits the rule. So look for something like: "uses a fact about how people perceive words to show that apparent exceptions are consistent with the generalization."','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;