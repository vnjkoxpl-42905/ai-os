update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('61bc06f2-ec10-4479-b3b6-b972064e44dc'::uuid,'12a2ebe688936caa5756d79ffae445f8','The whole argument rests on a rule and a fact. Rule: anything alive has a reproductive mechanism. Fact: a single nanobe is too small to contain one. Put them together and nanobes can''t be alive, so the geologist must be looking at bits of clay.

Given that a single nanobe is too small to hold a reproductive mechanism, how could we still argue that nanobes are living things? We can''t deny the rule; it''s a premise. So look at what the author assumed about how the rule applies. The author assumes the mechanism has to fit inside one nanobe. What if nanobes don''t reproduce one at a time? If several could team up, the group could have the mechanism that no single nanobe can hold.

A second route goes after the author''s alternative: anything that makes "inanimate artifacts of the clay''s microscopic structure" a poor explanation. That one is harder to predict, so expect the first route.','Evaluate','Evaluate'),
('437e8fee-c681-4344-9b4d-70ef4ceffda4'::uuid,'f5f70be7f0a5f4213af0e37d6b90537f','Look for an answer showing that a living thing can reproduce without each individual containing the whole mechanism, for example by joining up with others. Less likely: an answer that makes the clay-artifact explanation hard to believe.','Goal','Goal'),
('79015267-f501-444a-9d22-ede9236fd38d'::uuid,'7daa0915197caa231dac55167d45a804','The argument makes two jumps, so there are two places to push.

Jump one: the computers are set too high, so they were installed "without consideration of their effect on posture." Given that all the keyboards and most monitors sit too high for children, how could someone still have considered posture? Maybe the computers are shared with adults and the height is a compromise. Possible, but a stretch.

Jump two is weaker. Given that children sit in unhealthy postures, how could they still not face "the same risk" as office workers? "Same" is a strong word. It assumes a child''s body takes the same damage from bad posture that an adult''s does, and that the exposure is comparable. Office workers sit at keyboards all day; children at school probably don''t. And a child''s body may handle strain differently. Either difference breaks "the same risk."','Evaluate','Evaluate'),
('a5c9db99-26be-4a80-9b43-2dc96995471d'::uuid,'c1377f9ccacdde5124d70a208ad9bde2','Look for an answer that makes children different from office workers in a way that matters for repetitive stress injuries: less time at the computer, or bodies that handle the strain better. A less likely route: a good reason the computers were set high even though posture was considered.','Goal','Goal'),
('e7c236e6-3f07-496d-a532-8aa9c3d48c14'::uuid,'86f7593cf255b103d42bfc917807e79b','There are two moves here, and we can push on either.

Move one, in the last sentence: the change is slight, so it "cannot have effects significant enough to be worrisome." Does that follow? Pull the wrong block from a Jenga tower and the whole thing comes down. What matters is not how much changed but what the changed part does. If a single gene controls something important, changing it could matter a lot.

Move two: "In most cases" only one gene in about 750,000 is changed, so the risk is minimal. Most cases aren''t all cases. What if the foods people worry about are the ones where many genes were changed?

Move one is the bigger target. "Cannot" is a claim about every slight change, so a single counterexample hurts it.','Evaluate','Evaluate'),
('cc5cddc8-5124-4d99-8a32-b5a6c0ffe14b'::uuid,'66dd093d05574854eae000a864f32022','Look for an answer showing that changing a single gene can have a significant, worrying effect. Less likely: an answer showing that engineered foods often involve more than a slight change, or direct evidence that their health risks are serious.','Goal','Goal'),
('40d87d6b-7241-4bb1-8d14-2d14f7092136'::uuid,'fb5e453274a6b09a48ff4203232aea35','All animals can, in principle, be bred for domesticity.','Conclusion (Therefore)','Conclusion (Therefore)'),
('84b6f8bd-424a-4d23-99d6-bc8b77efe3ed'::uuid,'1c79f5655170391fd920cb4bf1419b9d','Domesticated animals have come into existence by breeding only the tamest individuals of a wild species. If you breed only the individuals that show tameness when young, then after a number of generations you end up with a domesticated version of the animal, as with wolves becoming dogs.','Evidence','Evidence'),
('803a5983-bcc7-4f36-ba62-eed7a5e23a79'::uuid,'57eb20d1728fb47100eec27e342e49f8','The conclusion is huge: "all animals" can be bred for domesticity. The evidence is one method and one example, wolves. The method needs a starting point: individuals that show tameness when young.

So how could we argue that not all animals can be bred for domesticity? Find a species where the method can''t start. Say we try it with hyenas, and no hyena pup in any litter ever shows tameness. There''s nothing to select, so there''s no way to keep breeding tame with tame.

Notice "in principle." The conclusion isn''t saying domestication is easy or fast. A slow, difficult breeding program still counts. To weaken, we need the method to be impossible for some species, not just harder.','Evaluate','Evaluate'),
('c964c786-b430-4290-ad9a-d07a9f8d0e65'::uuid,'32dd079ac99884681ce22ebe2953841e','Look for an answer saying some species have no members that ever display tameness, or anything else that makes the breeding method impossible, not merely slower, for at least one kind of animal.','Goal','Goal'),
('7f3a56f3-de2d-4d61-8740-d0f470414abe'::uuid,'ca293683115113b7339c1a1fbc520e96','Dr. Faris is in violation of the ethics code. Put another way: Dr. Faris deceived a patient about their medical treatment.','Conclusion (So / clearly)','Conclusion (So / clearly)'),
('920cf5e0-3247-44bf-b993-b02c8f4426dc'::uuid,'b28810b8268ae3d06a97b64f5bfd64e6','The ethics code says hospital staff must not deceive patients about their medical treatment. Dr. Faris gave medication A to a patient and said it would help the patient sleep, even though medication A has no known sleep-inducing properties. (The patient''s sleep did improve after taking it.)','Evidence','Evidence'),
('4d56fe9e-9cb8-4746-b18d-2cff9326adcd'::uuid,'d667895531b689d390ad0bf239741081','The conclusion says Dr. Faris is "clearly" in violation. That depends on one thing: was the patient deceived? The only evidence of deception is that medication A has "no known sleep-inducing properties."

Given that, how could we argue Dr. Faris was honest in saying the medication would help the patient sleep? Look at the gap. A drug with no sleep-inducing properties can still help someone sleep by another route. Maybe it treats something that keeps the patient awake, like pain. The author even concedes that the patient''s sleep did improve. If medication A helped through some indirect route, the statement was true, and a true statement isn''t deception.','Evaluate','Evaluate'),
('251f4e25-b347-43df-b27f-1243c8ddf3c5'::uuid,'a2529645d6f2c79e6908db4b7a5db1c6','Look for an answer that gives medication A a real, indirect way to improve sleep, so that telling the patient it would help them sleep was true. That knocks out the deception, and the violation goes with it.','Goal','Goal'),
('bbd59f2d-ab07-471d-b1e1-8f06fa8f458c'::uuid,'09baef51220ebf05c4289eb98b1db538','This is a recommendation, so ask what could go wrong with the plan. Given that relatively minor interactions can still hurt patients, as with aspirin and fruit juice, how could we argue the government should not require notice of "all known drug-related interactions"?

The author shows one upside. Look for downsides. Would it cost too much? Is it even possible? Could it backfire? Picture a drug insert listing forty interactions, most as mild as the fruit juice one. Would a patient still notice the one that could put them in the hospital? A plan meant to protect patients could end up hiding the warnings that matter most.','Evaluate','Evaluate'),
('7a8595dc-6018-42ae-9961-837af202ebe0'::uuid,'e169f729a88ebd338a341a4f54897865','Look for a downside of requiring notice of every known interaction: it costs too much, it can''t be done, or it backfires, for example by burying serious warnings under minor ones.','Goal','Goal'),
('4d8ef774-19ff-4fe9-afb3-4c535d74dde0'::uuid,'a821c24aef93f968e4f1797f4c25ebfc','The author''s case: audits are the primary way to detect violations, no corporate audit has been completed in a year, so the agency hasn''t followed through on its crackdown.

Given that not a single corporate audit was completed in the past year, how could we still argue the agency is following through? Look at the word "completed." The author assumes a real crackdown would produce finished audits within a year. What if audits take longer than that? Then the agency could have started hundreds of audits the day after the announcement, and the count of completed audits would still be zero.

Another route: the agency may be cracking down by other means. Audits are the "primary" tool, not the only one.','Evaluate','Evaluate'),
('a8fd67cf-7a75-47e3-a2c7-8020ae1e31b0'::uuid,'fcd46a2c11c24ea488af0a0e907f3967','Look for an answer that gives an innocent reason for zero completed audits, most likely that audits take more than a year to finish. Or an answer showing the agency is cracking down some other way.','Goal','Goal'),
('984f4d35-bbcf-4d00-8c76-9d5529625548'::uuid,'d7a66102b80be68bc03bb8a87424125c','The argument slides between two ideas.

Idea one: obstructive behavior hinders the jury''s effort to reach a correct verdict.
Idea two: obstructive behavior makes it reasonable to doubt that a correct verdict was reached.

A strong headwind might hinder my effort to reach the top of Mt. Whitney. But if I''m standing at the summit, the headwind gives you no reason to doubt I got there.

Same here. Obstructive behavior can make the jury''s job harder without making a wrong verdict likely. Given that these behaviors hinder the jury, how could we argue the verdict still deserves trust? Show that juries usually get past the obstruction anyway. And notice "Whenever": the conclusion covers every trial with such behavior, so anything showing the behavior rarely changes outcomes hurts it.','Evaluate','Evaluate'),
('8906ed5a-58ef-4f49-8ea9-5c075f08af65'::uuid,'9d7bf87d6b56e5b9513e49e600ee89bf','Look for an answer saying these behaviors rarely change what the jury decides, so even when lawyers use them, the verdict is probably still correct.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;