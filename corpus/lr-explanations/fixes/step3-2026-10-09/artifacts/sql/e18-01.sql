update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('b2723059-9d7e-4017-a4a1-29ec80e7550d'::uuid,'2f5efd746d29408eb925cad8dd954af5','The builders won''t finish the Glen Veil complex unless a road connecting it to Sierra is built. So the road is required for the complex.

If the complex is completed, it will strengthen Sierra''s economy, and a stronger economy would benefit every Sierra resident.','Evidence','Evidence'),
('3310ea29-a41b-4cd6-b66c-e5c17902eed8'::uuid,'29989d5a0b25a5447c081a3578261e6c','Line up what the premises give us against what the conclusion asks for.

The premises are all about benefit. The complex is waiting on the road, the finished complex strengthens the economy, and the stronger economy helps every resident.

The conclusion is about duty: residents should vote for a tax. Nothing in the premises says that benefiting from something means you ought to vote to fund it. That''s the new idea the conclusion brings in, and it''s the gap.

There''s also a cost the developer never weighs. A tax costs every resident something too. The developer simply treats the benefit as enough to settle the vote. A principle that justifies this reasoning has to make that move for us.','Evaluate','Evaluate'),
('96a7eb1b-8852-45ed-8fc6-c64b3d76f940'::uuid,'fea6c5627a60adea7d8a16f88a4dc7a9','On a justify-the-reasoning principle, the answer usually has the shape If Evidence, then Conclusion, written in general terms. Here the evidence boils down to benefit, and the conclusion is a vote for a tax. So predict:

would benefit from a construction project → should vote for a tax that funds it

The right side has to say residents should vote in favor. A principle that only tells us when not to vote for a tax, or who should pay one, can''t deliver that conclusion.','Goal','Goal'),
('5de67afa-c920-4f55-a9ab-7675f95e9ea6'::uuid,'23fa8aa6b1557b7cfd80dedab9dafeff','We should not be persuaded by Graham''s argument.','Main Conclusion','Main Conclusion'),
('5b95a90f-0d10-4886-b6cb-159da16407ac'::uuid,'6f19c58fdef23cd4411360a2cd595c3c','The best life is a life that is full of activity.','Opposing Point','Opposing Point (Graham''s conclusion)'),
('b65862a4-6b68-4ac1-b554-6d99edac9a87'::uuid,'c4825554f2c5f357549ac56770a2133a','A person is truly happy only when doing something.','Opposing Point','Opposing Point (Graham''s premise)'),
('21922f05-e8be-427e-85b2-ce475ef19f95'::uuid,'e459c4e7e23956427d75b2614798b0c6','The evolutionary advantage of sexual reproduction is that it increases the range of genetic variation in a species, which is an advantage for the species as a whole. However, an increased range of genetic variation in a species is not advantageous for any individual member of the species.','Evidence','Evidence'),
('74fef0de-d608-4bbf-932a-97adf76734dc'::uuid,'4a1559850785178c16855781124bd911','"It follows that" marks the last sentence as the conclusion: the sole reason sexual reproduction became the rule is that natural selection favored some entire species over others.

Why should we believe it? The biologist gives two facts that work together. First, the advantage of sexual reproduction is wider genetic variation, which helps the species as a whole. Second, that variation helps no individual member. If the advantage shows up only at the species level, selection among individuals can''t explain why sexual reproduction spread. That leaves selection among whole species, which is the conclusion.

Slow down on the "However". It contrasts species with individuals, but it doesn''t turn against the biologist. Both sentences are on the conclusion''s side. The second one actually does the heavier lifting, since it is what rules out an individual-level explanation.','Evaluate','Evaluate'),
('e781f424-c2e2-4c0a-bee0-c4bc68159971'::uuid,'a5cd1a89dc9078525dea319f5b7a0711','The stem asks about the second premise, the claim that the variation helps no individual. Predict: a premise that supports the conclusion. Expect an answer as plain as a claim offered in support of the conclusion.','Goal','Goal'),
('b00f913d-5cb5-4b09-9b98-b9a7d29ba588'::uuid,'38a005370e81160cca1baffd36eb3545','Emotion only seems nonrational because language lacks the ability to convey adequate conceptions of emotion.','Intermediate Conclusion','Intermediate Conclusion'),
('4b34d9dd-e6f5-4bd6-93cb-1ce9ec475561'::uuid,'09b1e356a652e7c3734f29045abbcc1c','The words we use to refer to emotions name only very general kinds of inner experience, such as excitement, calm and joy.

Illustration of that: there is no language for describing just how one joy differs from another.','Evidence','Evidence'),
('3dca010a-1ca5-4cfa-a0e7-ff601025c577'::uuid,'af55122d05b81512bdd3158649ccd1df','Role and Main Conclusion arguments often put the conclusion right after a pivot that pushes back on someone''s view. Here the philosopher opens with how philosophers usually treat emotions, as nonrational, then pivots with "But": emotion is not nonrational. That''s the main conclusion.

Everything after it is support, in layers. Why believe emotion isn''t nonrational? Because it only seems that way, since language can''t convey adequate conceptions of emotion. Why believe language falls short? Because emotion words name only very general kinds of experience.

Then the last sentence opens with "Thus, for example". Two signals that seem to fight. "Thus" usually marks something that follows; "for example" marks an illustration. Both fit. If emotion words are only general, they can''t separate one joy from another, so the last sentence follows from the general claim. And it is offered as one concrete case of that general claim. It isn''t where the argument is headed. It is a picture of the evidence.','Evaluate','Evaluate'),
('a9eb97e3-cf7b-4a59-a97b-4b8d2fa34fff'::uuid,'6f2fa550bf2a33c2d8cc86f2131a1fdd','The target claim is a specific case of the general claim about emotion words, and that general claim supports the main conclusion through the middle step about language. Predict an answer that calls it an example or illustration of a supporting claim, with only an indirect link to the main conclusion.','Goal','Goal'),
('fdd643c6-3726-49f1-8a6a-62029db0a774'::uuid,'1ebeae12df740e4efd3b53b08d7a376a','Start with the indicator. "Thus" opens the last sentence, so that''s a conclusion: groups that switched to agriculture were likely motivated by benefits of settled life.

Now test the first sentence the way we test any candidate: why should we believe the transition was traumatic? The second sentence answers. More disease and injury, and a diet lacking vital nutrients. So the first sentence has support of its own.

Does it support anything? Yes. Why think the groups were drawn by benefits like wealth? Because the switch was traumatic, and the argument''s thought is that groups wouldn''t accept that kind of hardship without something to gain. So the traumatic claim is supported by the second sentence and supports the last one. That makes it an intermediate conclusion.

The first sentence looks like a classic first-sentence conclusion. It is a conclusion, just not the main one. "Thus" settles which one is main.','Evaluate','Evaluate'),
('76ef4fb8-1fec-4f04-8aee-3f4e268e01bf'::uuid,'6b43e421ab74166d8d232f87a7cc8c3b','A successful legal system prohibits only those few behaviors that citizens find absolutely intolerable.','Conclusion (Therefore)','Conclusion (Therefore)'),
('b4bbfe52-39ce-4c25-af44-b5f393dff913'::uuid,'b7e19e2c46033d0cb36c3701a7858588','On Role and Main Conclusion, it pays to check the first sentence and any pivot before trusting the end. Here neither holds up. The first sentence, about the purpose of a law, gets no support from anything else. The "But" sentence, about the odds of being caught dropping as prohibitions multiply, isn''t supported either. A claim with no support can''t be a conclusion.

That leaves the "Therefore" sentence, and this time it really is the main conclusion: a successful legal system prohibits only the few behaviors citizens find absolutely intolerable. Why believe that? Laws work by threatening punishment. The threat works only if people think they''re likely to be punished. And the more kinds of acts are prohibited, the less likely punishment becomes. Keep the list short, and the threat stays believable.

The first sentence is the starting point of that chain. Nothing supports it, and it supports the conclusion.','Evaluate','Evaluate'),
('6919ad1a-3684-47e2-8849-c8c87ebe5896'::uuid,'82480d0f39fb3f061f8e580b00df657c','The target is the first sentence. It supports the conclusion and has no support of its own. Predict: a premise.','Goal','Goal'),
('8b4c7808-551e-4002-a35e-98c711a9ad06'::uuid,'f4665fe621eaa0d45e9e16b340f7b8f4','On Main Conclusion and Role, the conclusion is usually found earlier than the support, but in this case it was the final sentence, signified by "Hence". Because this is Role, we want to be highly alert for whether that "Hence" is actually just an Intermediate Conclusion, but in this case we can tell it''s the main conclusion because the 1st and 3rd claim combine to support this 4th claim. There are four claims in this argument, and structurally they go in this order:
    1. Premise
    2. Counterpoint (although)
    3. Premise
    4. Conclusion (hence)
    We''re being asked about the first sentence, which was one of the two premises for the conclusion in the final sentence.','Evaluate','Evaluate'),
('590aeacf-663b-4031-8953-c7c6fe3e9d29'::uuid,'99975be4383a4e1465899b7551190657','The stem asks about the first sentence, one of the two premises. Predict: a premise that supports the conclusion that a widespread grassroots push for stricter air pollution controls is unlikely right now.','Goal','Goal'),
('d42ea42a-23c0-465d-a5ca-6a5a43183410'::uuid,'fb01e37436b1a9057b36ce716c998932','On Role and Main Conclusion, the conclusion very often sits in the first sentence or right after a pivot. So hear the first sentence as a possible opinion: our mastery of Latin and Ancient Greek is "at best imperfect." If the rest of the passage supports it, it''s the main conclusion.

It does. The second sentence sets up a contrast. On one side, the best students of a modern language can immerse themselves where it is spoken and get close to perfect knowledge. On the other side, you can''t spend a year abroad at Plato''s Academy. Immersion is open for living languages and closed for ancient ones. That contrast is why the classicist thinks mastery of the ancient languages falls short.

Notice what the Plato''s Academy line is. It isn''t a general statement that ancient immersion is impossible. It is one vivid case that makes the point.','Evaluate','Evaluate'),
('d1b5c182-d05e-4fe3-9bca-613753f99083'::uuid,'0226cdf72604b474d28c9bc224855808','The target claim is the second half of the contrast, given as a concrete case. Predict: support for the first sentence, possibly described as an example or as one side of a comparison.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;