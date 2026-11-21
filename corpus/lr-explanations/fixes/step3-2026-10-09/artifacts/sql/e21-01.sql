update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('e8c85123-28f1-4b94-801f-fcc6fe3a8a11'::uuid,'ae2c3d494dcd88b3dea773bb0fa9ccf6','We know the first claim is the conclusion because the other two claims are clearly built to work together. Connectors like and, but, and on the other hand show two claims interacting to move the argument forward.

Each conditional premise has TWO outcomes, and one of them is decreasing unemployment. I didn''t bother writing out the other half of each outcome, because all we care about is proving that unemployment will decrease.

At first, this argument seems pretty reasonable. It looks like an *Either Way You Slice It* argument: whether spending increases significantly or decreases significantly, we end up with lower unemployment, so either way unemployment goes down.

But an argument on Sufficient Assumption can''t *already* be airtight. There has to be a gap, so that the correct answer can close it.

So let''s argue with the economist. How could unemployment *fail to decrease*?

Spending doesn''t have to go significantly up or significantly down. It could stay about the same. Then neither rule is triggered, and the premises tell us nothing about unemployment.

The economist is presenting a *False Choice* (a false dichotomy), treating a big increase and a big decrease as the only two options while ignoring the middle ground where spending barely moves.','Evaluate','Evaluate'),
('0cf755b5-c56e-473b-8db9-5095d3dd3436'::uuid,'dfc69dc9be2714a1ba355f1f51d1c098','We need to rule out the middle ground. Predict an answer saying that next year government spending will either significantly increase or significantly decrease.

With that fact in hand, one of the two rules has to fire, and both rules end at lower unemployment. Whenever an argument covers two cases that lead to the same result, the sufficient assumption is often the one that guarantees one of those cases actually happens.','Goal','Goal'),
('85a2d1a6-42aa-4496-adf4-0d1642958629'::uuid,'20cf85bc6f33097591b75bec53cd2596','Most children under six are egocentric and selfish in their attitudes toward animals.

Ordinarily, children only begin to understand that animals are independent creatures with their own feelings and needs somewhere between the ages of six and nine. So most children under six do not yet understand this.','Evidence','Evidence'),
('472a536c-d84c-49b2-aad8-6e30ad1e0350'::uuid,'0c63806a78ba133caef1c74de26105f6','Look at the conclusion''s key word: "should." The evidence only describes what young children are like. The conclusion tells us what ought to happen. That "should not have pets" idea is a new concept in the conclusion, and on Sufficient Assumption the correct answer almost always has to supply it.

Let''s argue with the psychologist. Given that most children under six don''t yet understand that animals have their own feelings and needs, how could we argue that they should still have pets? Easy: maybe a child doesn''t need to understand that to have a pet. A parent could do the caring, and the child could learn along the way. The argument never rules that out.

We can sketch it with arrows, as long as we remember the premise says "Ordinarily," so it is a "most" claim, not an "all" claim:

under 6 → not understand (most of them)
not understand → should not have pet (missing)

If every child who doesn''t understand should not have a pet, then the "most" in the premise carries straight through: most children under six should not have pets.','Evaluate','Evaluate'),
('e501b187-6096-4885-ace4-2b883984f8ee'::uuid,'901d240f1334acff05fd8bce72538390','We''re looking for a rule that says children who don''t understand that animals are independent creatures with their own feelings and needs should not have pets:

not understand → should not have pet

The contrapositive is just as good: should have pet → understand. That version may be worded with only, so read the sentence carefully: after only if, the idea goes on the right side of the arrow, but in a sentence shaped like The only X are Y, the X goes on the left (X → Y). A rule linking "egocentric and selfish" to "should not have pets" would also work, because that premise is about the same group of children.','Goal','Goal'),
('e22a1235-1b8a-493d-9730-2389bc4d1396'::uuid,'fed3899d12c1745fb6ecbdf9c71c1fea','In an experiment with 200 randomly selected people, the half who were allowed to gesture spoke more quickly and repeated themselves less than the half who were not.

So gesturing went along with quicker speech and less repetition.','Evidence','Evidence'),
('6c0dcf04-1ad2-456e-9c21-182306f1a7f2'::uuid,'508cb5067b3af4947f76c884451736ce','Gesturing helps speakers quickly find the phrases they want.

Notice the new idea here: finding phrases. The experiment measured speed and repetition. Nobody measured how quickly anyone found a phrase.','Conclusion','Conclusion'),
('d2de34f4-7f8e-4820-b578-a74b19bebb08'::uuid,'b2235e2b3dc08148fbcdcf0025fd28b6','Let''s argue with the author. Given that the gesturers spoke faster and repeated themselves less, how could gesturing still not help them find phrases?

Maybe gesturing just speeds people up. Waving your hands could make you more animated without making the right words come any faster. Or maybe gesturers repeated themselves less because a gesture did some of the describing for them, so they didn''t need to say it twice. Either way, the speech changed for a reason that has nothing to do with phrase-finding.

The author is assuming that quicker, less repetitive speech is a sign of finding phrases faster. On Sufficient Assumption, we don''t need to argue about whether that is true. We just need the rule that makes it true:

gesturing → quicker speech, less repetition (evidence)
quicker speech, less repetition → helps find phrases (missing)','Goal','Evaluate'),
('9728151b-3a9a-45fe-873a-4f54d2e8c7a9'::uuid,'3d4d570b5dfe4c59da9d83d22549c9cc','Because television is in nearly every home, few children today spend their free time reading stories.','Evidence','Evidence'),
('fa2f2545-0ba5-431b-931f-a8d91caad3b1'::uuid,'17584c9fc1a3b718a630802d90fcd6bf','The evidence is about reading stories now. The conclusion is about a lifelong interest in literature. Those are different ideas.

Let''s argue with the author. Given that few children read stories in their free time today, how could plenty of them still end up with a lifelong interest in literature? Easy: they could discover it later, in a high school English class or as adults. Nothing in the argument says the only road to loving literature runs through childhood story time.

To shut that down, we need reading stories to be required for a lifelong interest:

~ spend free time reading → ~ lifelong interest in lit

Why does that prove "few"? If interest requires reading, then everyone who develops the interest is inside the reading group. The reading group is small (few children), so the interested group can be no bigger. A rule in the other direction, reading → interest, would not cap the number at all.','Evaluate','Evaluate'),
('0492dc85-3192-4e83-9065-5aca24fe75d8'::uuid,'58846005e622c065be71b1dd727f4ae6','We''ll keep our eyes open for the rule above or its contrapositive:

lifelong interest in lit → spend free time reading

Words like only or requires attached to reading stories are the giveaway. We can also eliminate any answer that doesn''t include the idea of developing a lifelong interest in literature, because the answer has to bring that new idea in.','Goal','Goal'),
('278cae2d-f407-4a3e-bdb0-c3fd23a744a5'::uuid,'374bd576a1158fccf8be521762d83ee3','On Sufficient Assumption, once we''ve found the conclusion, we ask whether it contains a New Concept. If it does, the correct answer almost always brings that concept in.

This conclusion is trying to prove that most indie films "do not have absolute integrity." Did the filmmaker ever say what it takes to have absolute integrity, or what destroys it? No. So the correct answer must be a rule that lets us prove that a film does not have absolute integrity.

What do we know about most indie films? Their artistic decisions are affected by the need to make profits.

Let''s argue with the filmmaker. Given that profit affects the artistic decisions behind most indie films, how could those films still have absolute integrity? Maybe a little profit pressure doesn''t touch a film''s integrity at all. The argument never says it does.

Notice the first sentence is just the view the filmmaker is pushing back on (people think indie films have more integrity because they are less conventional). It isn''t support, so the answer doesn''t need to deal with conventionality.

The "most" also carries through cleanly. If profit-affected decisions always mean no absolute integrity, then most indie films (the profit-affected ones) lack it.','Evaluate','Evaluate'),
('c1b89a6b-a22e-4291-b0ec-fb8a90405b87'::uuid,'28ac8855bcc377cfaabeaec0d2e48295','A classic missing link correct answer would say that if the artistic decisions made in creating a film are affected by the need to make profits, then the film doesn''t have absolute integrity as a work of art. They might surprise us with how the trigger is worded, but we''re only interested in answers that provide a rule that puts not-absolute-integrity on the right side of the arrow, with profit-affected decisions on the left. Expect an illegal negation or a reversal of this rule as a trap. The correct answer might also come in contrapositive form: if a film does have absolute integrity, then its artistic decisions aren''t affected by profit.','Goal','Goal'),
('aa629d31-a0a0-420d-a245-fe69cf370cd6'::uuid,'a4e3f8ee187caf32ef83b8673bedfd16','Thriving populations of turtles require conditions that are beneficial to turtles. Wallakim Pond has acidic water.

(Sosachi Pond''s water is not acidic, but the conclusion is only about Wallakim, so Sosachi is just a contrast.)','Evidence','Evidence'),
('69d8de67-a247-45fd-ad3a-e04bf08d846b'::uuid,'8822615026bf84f175dc4b2734971225','We know Wallakim''s water is acidic. We know that without beneficial conditions there''s no thriving turtle population. But nothing connects acidity to beneficial conditions. For all the argument says, turtles might love acidic water.

So it looks like we just need to hear that acidic water is not a condition that is beneficial to turtles. If we don''t hear that missing link intuitively, we can derive it by turning the Conclusion into an elongated logic path, checking which parts of that path the Evidence provides, and solving for the missing part as our Sufficient Assumption.
```
CONCLUSION
Wallakim -------------------------------> ~Thriving
Pond                                       Pop of T''s
EVIDENCE
Wallakim --> acidic     Cond''s --> ~Thriving
Pond         water      not ben    Pop of T''s
MISSING LINK
acidic --> Cond''s
water      not ben
```','Evaluate','Evaluate'),
('4d2c72d0-003e-4884-8ca7-9c482e665c7b'::uuid,'c57b42907b2d30857256328d4870450b','We want an answer that conveys this rule: if there''s acidic water, then the conditions are not beneficial to turtles. Its contrapositive works too: if conditions are beneficial, then the water is not acidic. Since only if introduces the right side of an arrow, the contrapositive version could easily show up as an only if statement about beneficial conditions. We''ll also take any other answer that we could combine with our evidence to derive that Wallakim Pond doesn''t have a thriving population of turtles.','Goal','Goal'),
('6b9ab90e-9128-4a0d-a8e6-696490172bcf'::uuid,'9f777d2f1afb7f096806487800f350c4','Some government employees who work in the Hanson Building are computer programmers.
```
some HB are CP   or   HB <--s--> CP
```','Conclusion (Thus)','Conclusion (Thus)'),
('c1a4ac94-a384-475f-9253-d31144c6ab21'::uuid,'be2e23082e48ce9933f9a3c5b967b953','Most members of Bargaining Unit 17 (B17) are computer programmers.
```
most B17 are CP   or   B17 --m--> CP
```','Evidence','Evidence'),
('39805444-6433-4dea-822c-9ca39c5ee1c0'::uuid,'1eb7ab09311a97c69a6ecf3b76b881d2','The blank comes right after "since," a support indicator, so whatever fills it is support for the conclusion announced by "Thus."

We need to prove that at least one government employee in the Hanson Building is a computer programmer. All we know is that most members of B17 are computer programmers. B17 is a unit of the government employees'' union, so its members are government employees.

Let''s argue with the author. Given that most B17 members are programmers, how could the Hanson Building have no programmers at all? Easy: none of those programmers work there. Nothing yet puts anyone from B17 in the building.

Computer programmers is the ingredient the premise and conclusion share, so the answer has to tie together the two dangling ingredients:

membership in Bargaining Unit 17
working in the Hanson Building','Evaluate','Evaluate'),
('f38237d6-a747-4bb6-8a15-72901fcc9ff8'::uuid,'182bcbda253fb91d83c87f52483cae8a','Since we''re trying to prove that some people in the Hanson Building are programmers, and we know that most people in B17 are programmers, we want an answer that puts B17 into the Hanson Building.

There''s a precise version of this. When the premise is a "most" and the conclusion is a "some," think about the most + most inference:
```
Most A are B
+ Most A are C
=================
Some B are C
```
Why does it work? Picture B17 with 100 members. If at least 51 are programmers and at least 51 work in the Hanson Building, those two groups can''t fit into 100 people without overlapping. At least 2 members have to be in both.

So we''re predicting the other "most" about the same group:
```
Most B17 are programmers      prem
+ Most B17 are Hanson          answer
=================
Some Hanson are programmers    conc
```
Watch for a "most" that runs the wrong direction (most Hanson workers are B17). The two "most" statements have to be about the same group.','Goal','Goal'),
('28cdc2ba-d384-4753-8f11-f5896a11438e'::uuid,'6e1ccf967e7f1e7cefce819f7d7ff20c','The Survey Group, a neutral polling company, has tracked tea sales at numerous stores for the last 20 years and has found no change in the amount of tea sold.','Evidence','Evidence'),
('e2b40f22-3be4-4848-b01c-e1ad9068d728'::uuid,'b2de032551e8335258731dc412c759e1','We''re trying to argue that tea **is** more popular than before.
Barr will ask how there could be no change in the amount of tea sold at these numerous stores over the past 20 years. We could either make an excuse for that survey data (they measured the wrong thing, or the wrong places), or bring up other data that makes it sound like tea IS more popular.
Notice the jump: the evidence is about some stores; the conclusion is about tea''s popularity in general. Whenever an argument rests on a survey, ask whether the sample represents the group in the conclusion.
Maybe the stores that are selling the most tea weren''t even open 20 years ago, so they''re not part of this comparison. Or maybe the surveyed stores are all in places where tea never caught on.','Evaluate','Evaluate')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;