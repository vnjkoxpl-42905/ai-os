update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('5efca95f-cd59-4efe-af88-66ef06e54bf7'::uuid,'be9ced87d417272ec027ee46fa22155a','A physical therapist has two goals for patients: (1) get more enjoyment from the challenge of developing physical skills, and (2) spend more time practicing those skills.','Situation','Situation'),
('8f8ecb99-14ac-4aa4-90e1-ba3743218e45'::uuid,'a125bf078f82999f2d3ee072ed0566b1','Meeting the first goal will bring about the second. If patients enjoy the challenge more, they will practice more.

Goal 1 achieved → Goal 2 achieved','Analysis','Analysis'),
('bc7f510e-7135-4c3f-871a-7be2160b8a91'::uuid,'d35c069c648e173db9e02af53b8ea785','The analysis is a causal claim about two goals held by the same party: get the first one, and the first one helps produce the second. So every answer gets the same test. Suppose this party fully meets its first goal. Does that plausibly push the second goal forward?

Notice how low the bar is. The stem asks whether the analysis "could be appropriate," so the link does not have to be guaranteed. Four answers will have a first goal that makes the second more likely.

The exception is the situation where meeting the first goal does nothing for the second, or even makes the second pointless. Look for two goals that pull in different directions.','Evaluate / Goal','Evaluate / Goal'),
('58729b6a-0187-48a3-bd9c-7a66392d691e'::uuid,'a19e85fa00508abae0909c33e4b05700','Start with what the two commissions actually disagree about. The Wildlife Commission wants regulation now: wetland development elsewhere has endangered species, so Figoria should require replacement habitats before any harm shows up at home. The Development Commission wants to develop without that requirement, and its best factual point is that Figorian development "might not affect wildlife." Figoria has conserved, and nobody has shown that its development is hurting anything.

So the fight is over timing. Should Figoria regulate in advance, based on what happened in other nations, or wait until harm is shown in Figoria? A principle that says regulation has to wait for demonstrated harm would settle that fight in the Development Commission''s favor.

Also watch the direction of the stem. We need a principle that helps the Development Commission against the Wildlife Commission. An answer that supports protecting wildlife, however reasonable it sounds, is on the wrong side.','Evaluate','Evaluate'),
('8dd9ac81-3aee-4e13-9304-5dc8e37138d0'::uuid,'60f6a2a53b54fe299612533f88531982','Two shapes would work. The first targets the timing fight: regulation should come only after development has been shown to harm wildlife. The Development Commission''s evidence (no harm shown, development "might not affect wildlife") would then block the regulation the Wildlife Commission wants.

The second targets the fairness point: a nation that has conserved its resources has the same right to develop them as nations that already used theirs commercially.

The correct answer does not have to use every premise. It just has to start from something the Development Commission has given us and lead to allowing development or to holding off on regulation.','Goal','Goal'),
('bdc514ef-27cc-436f-9e0d-caed003d5e07'::uuid,'783d0ee997b562f042033d2d295ef869','No new taxes supporting the library system should be approved unless the library hours are changed to better suit taxpayers and their families.

"Unless" introduces the requirement. Diagrammed:
approve new library taxes → hours changed to suit taxpayers
hours not changed → no new library taxes','Conclusion','Conclusion'),
('2bed2adb-7829-444d-bdd3-405f25ef5253'::uuid,'7bbbdb3c069e7023e6d5264f753a1d0b','The evidence is about access: most taxpayers have few chances to use the libraries. The conclusion is a rule about taxes. Nothing in the argument says that whether taxpayers can use a facility has anything to do with whether a tax to support it should be approved.

Ask how we could still argue for the tax. Maybe the libraries serve the public in other ways, through online services, archives or school programs, so the tax is worth approving even if few taxpayers can walk in during open hours. Unless something ties tax approval to taxpayers'' opportunities to use the facility, the conclusion does not follow.','Evaluate','Evaluate'),
('70c15f55-a227-49cf-b90b-83ef9bd4db06'::uuid,'69fc030dcc8f1627c5c4bf6ba6460c1d','Look for a principle that puts taxpayers'' opportunity to use the facility on the required side of tax approval:

approve a new tax for a facility → most taxpayers can actually use it

Our evidence says most taxpayers cannot use the libraries much under the current hours. Run that through the principle and new library taxes are blocked until something, like the hours, changes.

Watch for the reversal. An answer that says when taxes should be approved (more convenient → approve the tax) has the same pieces on the wrong sides.','Goal','Goal'),
('b6b3118e-0616-4eed-a0a5-7de9ef8c1552'::uuid,'a475d3ea26f1a7716faffabdb0d43024','Look at how far the conclusion reaches. The essayist says all commitments should be seen as morally neutral. The evidence is that what one is committed to "might be either good or bad," that one kind of commitment (to a relationship that benefits nobody) "deserves no praise," and that commitment is "often" just involvement that has outlasted its original justification.

Every piece of evidence covers some commitments. The conclusion covers all of them, including a commitment to a relationship that benefits everyone involved. Why would one unpraiseworthy commitment make that one neutral? The argument never says. That is the gap: from some to all.

So a principle that only covers the commitments described in the evidence will fall short. It has to do the generalizing for us.','Evaluate','Evaluate'),
('a10d6499-7ba9-406b-9f99-79f916f6258b'::uuid,'6c99ad829615ccf62a3edc3702d33fec','James bought a video camera and returned it to the store two weeks later.','Evicence in Application','Evidence in Application'),
('6068a1ee-d9d2-43fe-8b62-9b35dbecb2a9'::uuid,'53580ebbdcfed71b7bf05849fdc3129e','The conclusion, "unethical," matches the principle''s outcome. So the question is whether the principle''s conditions are all met. The principle needs three things: the person bought the item, got all the use from it they ever intended to get, and then returned it.

The application gives us the first and the last. James bought the camera and returned it. The middle condition is missing. Two weeks of ownership tells us nothing about whether James was finished with the camera. Maybe it broke. Maybe it was the wrong model. Without the middle condition, the principle cannot fire.','Evaluate','Evaluate'),
('7dc481d2-4aeb-4b20-8666-167e40e4768e'::uuid,'b4f880917092b25005e0c3ede014217e','Look for an answer showing that James got all the use from the camera that James ever intended to get before returning it. The cleanest version tells us what the camera was bought for and that this purpose was finished before the return.','Goal','Goal'),
('0d09bc04-0083-4b2d-96b9-7eb8213f784e'::uuid,'da7e9532c3d671ed2c13242d18598932','Some of the rare pygmy bears should be moved from their native island to the neighboring island.','Conclusion','Conclusion'),
('c4703bac-bb67-4310-8584-fba462a4d54e'::uuid,'275c50d022d1d17f7da89039376a4d22','The facts get us a long way. The bears risk extinction, and moving them is the only viable chance of saving them. But the conclusion is a "should," and nothing in the argument says we should do whatever it takes to save a species.

How could we argue against the move even granting every premise? Maybe the bears would wipe out something on the neighboring island. Maybe the move costs more than it is worth. The argument has no answer to those objections, because it never gives a principle saying that preventing extinction is what we should do.

So we need a principle that turns the fact that this is the only way to save an endangered species into the claim that we should do it. Because the conclusion says "should," the principle''s outcome has to say "should" too. A principle that says the move is allowed, or that one requirement is met, will not get there.','Evaluate','Evaluate'),
('cba5d9bc-60e0-461e-8e97-50a242ce3fcc'::uuid,'1dc8576fc86d2339b064dc7ef17ca256','The typical correct answer here has the form If evidence, then conclusion. Look for something like:

species faces extinction + this action is its best chance → the action should be taken

The correct answer may use broader words ("a species," "whatever is most likely to prevent the extinction"), but its condition must be met by our facts, and its outcome must be a "should."','Goal','Goal'),
('269d23c5-4d07-471f-8471-577bedde0f9d'::uuid,'1bfcabc3b31e4d90632d9fca5b24c03b','We''re looking for an answer that makes this missing connection. Since the correct answer only needs to justify the argument, it doesn''t have to match our prediction word for word, but it often comes close, so this question type is good practice for sharpening your predictions.

Check two things on every answer. Is the left side something Mateo actually established (automobile use contributes to the damage)? Does the right side say the automotive industry should pay? Beware of answers that add a condition Mateo never established, put the duty on a different party, or reverse the logic. Eliminate any answer that puts the industry paying on the left side (the sufficient condition).','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;