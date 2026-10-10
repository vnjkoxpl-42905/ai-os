update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('4e39deec-4023-4995-829c-82c8a07c2ae5'::uuid,'3d2728f9b97efb5424bb1f2a59b310fb','The conclusion is weakly worded. It only claims the new test can prompt dangerous operations that are not medically necessary.

Do we know the test leads to dangerous operations? Close enough. It finds polyps so early that it is generally unclear whether they are malignant, and in most cases doctors have such polyps surgically removed anyway. The researcher tells us that removal is a dangerous process.

Do we know those operations are not medically necessary? Not quite. The evidence only says some of the polyps "turn out not to be malignant." The author treats that as if it means the surgery was "not medically necessary." That is the leap. Maybe a polyp that is not malignant still needs to come out for some other medical reason.','Evaluate','Evaluate'),
('d8805a25-d6a2-4027-991a-44fffca76e7a'::uuid,'134fd5e62a88f7c5d2beb81b610f8396','Look for an answer expressing the author''s linking move: at least some of the time, removing a polyp that turned out not to be malignant was not medically necessary.

Or look for an answer ruling out the objection we just built, something like this: nonmalignant polyps don''t always need to come out for some other medical reason.

Either way, negate it. If the negation lets us say every one of these operations was medically necessary after all, we''ve found the assumption.','Goal','Goal'),
('8dde1203-b987-4e5e-8c6b-3b85336686bc'::uuid,'ffae75714e791f064fbf961f7481c073','The conclusion has a conspicuous new term: the Sumerian civilization in Mesopotamia. The evidence only tells us about Egyptian tablets dated to between 3300 and 3200 B.C.

For those tablets to challenge the belief that the Sumerians were first, historians must not already credit the Sumerians with literature from before the tablets. If historians believed the Sumerians were writing literature in 3500 B.C., an Egyptian tablet from 3300 B.C. would come in second, and there would be nothing to challenge.

Try an everyday version. Jerry can bench press 200 lbs. Hence, this accomplishment challenges the widely held belief among students that Maggie is the strongest student in school. What are we assuming about Maggie? That the students don''t already think Maggie lifts more than 200 lbs. If they believed Maggie benched 250, Jerry''s lift would change nothing.','Evaluate','Evaluate'),
('bc066e4f-d952-412f-8416-94a29eb59057'::uuid,'a68683aed69450e294e84c9502bc4f02','Look for an answer saying historians don''t date the Sumerians'' first literature before the Egyptian tablets, in other words, not earlier than about 3300 B.C. Negate it, and the tablets arrive too late to challenge anything.','Goal','Goal'),
('d768c294-1f6a-4632-bd81-f82cb8c3e736'::uuid,'736216bd0ab089122a11c0fc5b0394c1','We''re told there''s something worse / life-shortening about living in captivity.

So if the odds of reaching max life expectancy are the same for captive vs. wild, then we need to hear one of these:
- something good / life-elongating about captivity
- something bad / life-shortening about the wild
- these fatal diseases that become a risk in captivity are not actually shortening the lives of very many leatherbacks','Evaluate','Evaluate'),
('97b26917-cf91-49c0-b5de-1a4234051d82'::uuid,'266d5a8653b3de2a0e87fbee6f0b0fbe','Honey adds bacteria, and bacteria cause the infections that slow healing. So honey should have slowed healing. Instead, honey wounds beat two other groups, and the answer has to explain both wins.

Honey vs. cleaning alone: honey must do something good enough to make up for its own bacteria. Maybe it stops bacteria from growing, or its bacteria are harmless.

Honey vs. antibiotic ointment: the ointment kills bacteria, so even if honey controls bacteria too, why does it do better? Something must be holding the ointment back, or honey must help healing in some other way.

Look for an answer that covers both comparisons. An answer that explains only one of them leaves half the result a mystery.','Evaluate / Goal','Evaluate / Goal'),
('fd7cc7f3-0c52-4d37-aaf8-7873a2088d60'::uuid,'90e4ff78e5ab4b14edbe75c009c74d60','The historians'' rule says significant intellectual advances generally occur where the political system is stable. "Generally" leaves room for exceptions, so Athens doesn''t refute the rule. What we need is an explanation for why Athens turned out to be an exception.

The cleanest way to reconcile a rule with a counterexample: find the reason the rule usually holds, then show that reason didn''t apply in this case. Why would stability usually matter for intellectual work? Maybe unrest cuts off money, safety, or time to think. If something in Athens kept thinkers supplied with whatever unrest normally takes away, Plato and Aristotle become an explained exception.

Look for an answer that names something instability usually destroys and shows Athens had it anyway.','Evaluate / Goal','Evaluate / Goal'),
('110085b7-403b-4786-bc1e-5c7e106e110a'::uuid,'39282fc5c693703e0081e4310f0c5c93','The stimulus closes the obvious escape route. The stripes contrast with the green or brown vegetation, and lions can see stripes clearly. So the stripes don''t hide zebras. They seem to announce to every lion that lunch is right here.

So how does a zebra survive with them? Seeing a zebra isn''t the same as catching one. The stripes could protect zebras in some way other than hiding, for example during the chase. Or zebras could have some other protection that makes up for being easy to spot.','Evaluate','Evaluate'),
('9756593d-f136-4fa9-8aec-908d9706c158'::uuid,'fe291a93a58bb05742ffa2cedadd9ae9','Look for an answer showing that the stripes help zebras survive in some way other than making them hard to see, such as making them harder to catch once a lion attacks. A weaker but possible version would give zebras some other defense that offsets being visible.','Goal','Goal'),
('d6a66e7b-c8bf-42d7-aef8-bced3c92abbd'::uuid,'b28795bb62cf6a9c21dabe2e4d3ab997','We need a way to explain how rain, or something that accompanies rain, is adding pollution to Crystal Bay. Maybe when it rains heavily, people in this town light more fires in their fireplace, and the smoke from the fireplace drifts over the Bay and drops particulates on the water, adding to its pollution levels. Who knows. Let''s just find some way to connect heavy rainfall to pollution in the Bay.','Evaluate / Goal','Evaluate / Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;