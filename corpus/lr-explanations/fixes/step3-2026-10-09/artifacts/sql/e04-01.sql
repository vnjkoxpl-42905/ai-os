update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('cd1342fe-bb3b-469c-a6a4-750b15d91103'::uuid,'833907d7a11daa688e3a71cf1a2e3b38','This isn''t a crazy argument. The author is assuming that what happened in the recent past will probably happen again in the near future.

Given that September beat July in each of the last two years, how could we argue that July might still get more rain this year? Easily. Two years is a tiny record. Two seasons can line up that way by chance, the way a fair coin can land heads twice in a row. And maybe something about this year is different from the last two.

Notice that the author was careful: the conclusion says "probably," not "definitely." That softer wording helps, but it doesn''t save the argument. Even "probably" needs more than two data points behind it. The flaw is the size of the record, not the strength of the claim.','Evaluate','Evaluate'),
('f84a9bed-d622-4d14-9f81-6f71996ab903'::uuid,'59b658d134acad3a5d7513e71f1a073a','Look for an answer saying the prediction rests on too few past cases: two years is not enough to say what this year will do. An answer could also say the author overlooks that this year may differ in some important way from the previous two. Expect abstract wording, so be ready to translate "future event" and "instances of related past events" back into this year''s rain and the last two years.','Goal','Goal'),
('ab7e94a7-ddbd-4d45-9caf-4cb90af52647'::uuid,'f52e0550ab91b0ffcffe95dcaa682d50','There are exceptions to the general rule that people should practice what they preach. Rephrase: sometimes it''s fine for people not to act the way they tell others to act.','Conclusion','Conclusion'),
('d9b0a365-ab76-41ff-b451-3a338496b16a'::uuid,'38823ceea03e15ca139d751d4f48b4cc','Logicians don''t need to be logical in their discussions of logic, any more than physicians need healthy lifestyles in order to treat people.','Evidence (for instance)','Evidence (for instance)'),
('fc848127-25d4-473d-8483-fd17e81006ed'::uuid,'89eb980c119dabe5b2090f845b588692','The author''s example of an exception is an analogy. Physicians preach health, and nobody thinks a physician has to live a healthy life to treat patients well. So, says the author, logicians don''t have to be logical in their discussions of logic either.

Any time an argument rests on an analogy, ask: are these two cases alike in the way that matters? The physician case works. A physician''s lifestyle happens outside the job. A physician who never exercises can still diagnose and prescribe correctly.

The logician case is different. Being logical while discussing logic isn''t something a logician does after work. It is the work. A logician who argues illogically about logic is doing the job badly. How would anyone come away understanding logic if the lesson itself were illogical?

So, given the physician example, how could we argue the logician example still fails? Point out that the physician''s failure is personal, while the logician''s failure is professional.','Evaluate','Evaluate'),
('1a1ff027-bd4f-45ee-a3cb-3be320682ecd'::uuid,'11f10060dd9db32537ab5739863deb07','Look for an answer that breaks the analogy: being illogical in discussions of logic is a failure at the logician''s actual job, while an unhealthy lifestyle doesn''t stop a physician from treating people well. The stem says "fails to take into account," so the right answer will be a fact that, had the author considered it, would weaken the comparison.','Goal','Goal'),
('542f69a1-1945-43b7-8afc-9f50da21f625'::uuid,'6ff67bc1b8d98623183ee0476522d562','The professor said A''s would go only to papers whose conclusions were supported by reliable statistical evidence. My conclusions were supported by reliable statistical evidence, and the professor admits it, but my paper got a B.','Evidence','Evidence'),
('db12ab11-af52-46c2-a683-ab4d5b3b4340'::uuid,'d1d25a22e4ad401f5a96be602dbbd34c','When a Flaw stimulus contains conditional logic, suspect the most common famous flaw: Necessary vs. Sufficient. The author takes a rule and runs it backward or negates it.

"Only" introduces a necessary condition. So the professor''s rule is:

gets an A → conclusions supported by reliable statistical evidence

That rule says reliable evidence is required for an A. It doesn''t say reliable evidence earns an A. The student reasons: my paper had reliable evidence, so it should have gotten an A. That is the reversal. It treats a requirement as a guarantee.

An everyday version: "Only people with a ticket get into the concert." Having a ticket doesn''t promise entry. You could still be turned away for showing up after the doors close. The professor may have other requirements too, like clear writing or a sound argument, and the paper may have missed one of them. A B is perfectly consistent with the stated rule.','Evaluate','Evaluate'),
('2aa2772e-075c-454e-93da-387d3cc3a000'::uuid,'3d151976f4c79fb256daeb8ead9934a7','Look for an answer calling out the formal Necessary vs. Sufficient error: the student treats something required for an A as if it were enough for an A. An answer could also say the student fails to consider that there may be other requirements for an A besides well-supported conclusions.','Goal','Goal'),
('6da4f1d9-4f19-4c6f-bd37-76f449cb2203'::uuid,'5e1295299b7e2142cda1461c773f261c','Lindsey is rebutting an opposing position. Some people say the company was unfair. Lindsey guesses at their reason ("Perhaps"): the company''s promise that the staff would all get bonuses if profits increased over last year''s. Then Lindsey knocks that reason down. The promise was:

profits increase over last year''s → staff all get bonuses

Profits were much smaller than last year''s, so the promise never kicked in, and it didn''t require bonuses. Fair enough. But Lindsey concludes much more: the company acted fairly.

Given that the promise didn''t require bonuses, how could we argue the company still acted unfairly? Easily. Maybe the staff worked unpaid overtime all year. Maybe executives paid themselves large bonuses while the staff got nothing. The critics may have had reasons Lindsey never mentions.

This is the famous Unproven vs. Proven False flaw. Defeating one argument for a claim doesn''t prove the claim false. Example: "Some people say this restaurant is bad, perhaps because the parking is terrible. But the lot was just doubled in size. Clearly the restaurant is good." The food could still be awful.','Evaluate','Evaluate'),
('a6b9a3bb-235d-48b4-bc1a-ec837003f877'::uuid,'b536e4c1b8c0f443490307b4f4afdd81','Look for an answer saying Lindsey concludes a claim is false just because one possible reason for it fails. An answer might also point out that Lindsey only guesses at the critics'' reason ("Perhaps") rather than answering the reasons they actually gave.','Goal','Goal'),
('7ce366d3-9e04-4358-830c-cd3f66090c56'::uuid,'1e584ad4291dd745a84680eccb5c1d76','The recycling process for those products uses as much energy as producing them from raw materials, and almost all energy production damages the environment.','Evidence (and)','Evidence (and)'),
('f66b65fd-91c6-4001-820b-e9afc2bddf2d'::uuid,'9be55aeea7d4dc2f225f40008798e94b','Given that recycling these products uses as much energy as producing them from raw materials, how can we argue that making them from recycled materials is still better for the environment?

One route would be to say the energy used for recycling is cleaner. The second premise mostly blocks that: almost all energy production damages the environment.

So look past energy. Energy is only one way that making a product can harm the environment. What about mining, logging, or drilling for the raw materials in the first place? What about the waste that goes to a landfill when nothing is recycled? Recycling could win on those counts even if energy is a tie.

The columnist treats one part of the environmental cost as if it were the whole cost. Two options that tie on one factor only tie overall if nothing else differs.','Evaluate','Evaluate'),
('79ee2b71-105c-45d1-891a-006a162f1f84'::uuid,'f0274fb9d01aa6339ac4ec03781fc002','Look for an answer saying the columnist fails to consider environmental effects other than energy use. The best version would say recycling might help the environment in some way unrelated to energy. That would show the energy tie doesn''t settle the overall comparison.','Goal','Goal'),
('d90cc213-c178-450e-8472-21d25661714a'::uuid,'16f57f1dadfbafe56de2604f8f75a7ac','Six months ago the city raised the fines for parking violations, to help pay for a parking garage that had just opened. Since then, parking violations on city streets have dropped by 50 percent.','Evidence','Evidence'),
('a080ae89-c3a2-4236-8112-a1b0217ea8b3'::uuid,'dc3b8efad2eb1f477418c5c502a790f4','A common pattern in Logical Reasoning: "Policy X went into effect. Then Y happened. So X caused Y." The official assumes the higher fines caused the 50 percent drop. The conclusion depends on that causal story: "if we want there to be even fewer parking violations, the fines should be raised again" only makes sense if fines are what reduced violations.

This is an Explain Curious Fact argument. Curious fact: violations dropped by half. The official''s explanation: the higher fines. Alternate explanation: read the first sentence again. A new parking garage opened at the same time. Drivers who used to park illegally on the street may now have somewhere legal to park. That would cut violations whether or not the fines changed.

The official mentions the garage only as the reason the fines were raised, then forgets about it. That''s the detail the test wants us to catch. When a stimulus mentions a second change at the same time, ask whether that change could explain the result.','Evaluate','Evaluate'),
('6a3f4f2e-bc5b-472f-b3f3-a54cd6a1c8e4'::uuid,'aa3ffdd3201c19a4c1788c0afd7e1217','Look for an answer saying the official fails to rule out another cause for the drop. The best one names the obvious rival: the new garage gave drivers more legal places to park.

There''s also a smaller worry. Even if the fines did cause the drop, raising them again may not add much. At some point the fine is already high enough: whether it''s $500 or $600, I''m equally determined not to get that ticket. But the official only predicts "even fewer" violations, so this worry is weaker than the garage, which threatens the causal claim the whole recommendation rests on.','Goal','Goal'),
('838e1b73-7cfb-43f3-8a17-2fbf861c77b5'::uuid,'26da7a9b77023eda008d0c87d9018c9a','Let''s survey the customers at a sushi restaurant about whether they like fish. Or ask the people at a dog park whether dogs make good pets. We know what answer we''ll get.

The president did the same thing. The survey went only to members present at a Tuesday meeting. Of course those people have no trouble attending on Tuesdays: they''re there. The members most likely to have a Tuesday conflict are the ones who missed the meeting, and they never got a survey.

That matters because the attendance problem is about the people who don''t come. The president drew a conclusion about why members miss meetings from the members who didn''t miss this one. How many absent members stay home because Tuesday doesn''t work for them? The survey can''t tell us.','Evaluate','Evaluate'),
('4a174753-dd5b-4207-a61e-681de2f49d5a'::uuid,'f72701dd92bd6b91eff9f0913feb5a06','Look for an answer describing a Sampling flaw: the president generalized from a sample that isn''t representative of the group the conclusion is about. The answer might say it abstractly (an unrepresentative sample) or concretely (the survey left out members who couldn''t attend on Tuesday).','Goal','Goal'),
('e4ba3f07-62ae-44d9-99f4-08896cab079b'::uuid,'8025116dfd8ab9dabd4288c943f75d6f','If the proposed measures are adopted, we''ll spend about a billion dollars less on ozone-related health costs.','Conclusion','Conclusion'),
('04d03232-ed43-4784-a704-d1c3dc7f2ce6'::uuid,'c5f2d914855f432f59613c67fc0ee7be','If the proposed measures are adopted, ozone levels in the city''s air will be one fifth lower than they are now.
Ozone is currently responsible for over $5 billion in health costs.','Evidence','Evidence'),
('700f2f4d-2273-44df-b221-4909c2471829'::uuid,'24fe13bc2051139990694452735d3fb7','The author takes one fifth of the $5 billion in ozone health costs and assumes that cutting ozone by one fifth cuts those costs by one fifth.

But who said the relationship is one to one? Given that ozone will drop by a fifth, how could we argue the costs won''t drop by a billion?

Maybe health costs depend on a threshold. Suppose ozone makes people sick only above a certain level, and even 80 percent of today''s ozone is well above it. Then cutting ozone by a fifth might barely change health costs. Or it could run the other way: the last fifth of the ozone could be the most harmful part, and the savings could be bigger than a billion.

Either way, the argument needs costs to rise and fall in step with ozone levels, and it never shows that.','Evaluate','Evaluate'),
('06c62d20-4965-4cea-a503-b5cada434090'::uuid,'96b2c1b9250386a3ab970051f6dab7e8','Look for an answer saying "just because ozone is reduced by one fifth doesn''t mean ozone-related health costs will be reduced by one fifth." In flaw language: the author presumes, without evidence, that health costs are proportional to ozone levels.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;