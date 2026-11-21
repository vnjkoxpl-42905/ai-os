update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('96be1514-f9da-47c9-9782-e02eb3ea4590'::uuid,'bf1d923a7bd3b8f250576eb536dcfae5','Contrary to recent speculations, no hardware store will be opening in the shopping plaza.','Conclusion','Conclusion'),
('9079926a-ee5e-4a51-8546-5c6f2cb2cb00'::uuid,'95788adb889f2c37af3e6714c0eef4d1','It is a given that to be an intriguing person, one must be able to inspire the perpetual curiosity of others.

Intriguing → Inspires others'' curiosity

This explains why inspiring curiosity matters. It is not offered as support for the claim that follows.','Problem','Context'),
('53dc91b2-d899-497d-92c0-bbf5821c8dc3'::uuid,'0620e6fa99dbd32aab8ac497ae931c19','Constantly broadening one''s abilities and extending one''s intellectual reach [perpetually expanding one''s mind] will enable one to inspire that curiosity.

Expands mind → Inspires others'' curiosity','Conclusion','Conclusion'),
('633d69ab-fbf0-4cef-acfa-3b1535d1fdcb'::uuid,'f723ce5ad9e123bd7aa8873cc5a26a0f','For such a perpetual expansion of one''s mind makes it impossible to be fully comprehended, making one a constant mystery to others.

Expands mind → Not fully comprehended → Constant mystery','Premise','Evidence (For)'),
('dbdd8c0f-ffab-4046-b111-38329719d11b'::uuid,'d46231313a83670f5e5239d3d60f36e2','Many people think that if human language evolved, then something like it must be present in those species most closely related to humans, such as chimpanzees.','Opposing Evidence','Opposing Point'),
('60c18f69-02c7-4cfc-bd71-ecc476c46302'::uuid,'7aaa39e01db7d479d3ab9eec9f2dc820','They reason that since new traits evolve gradually, something like human language, albeit cruder, must exist in some species from which humans evolved.','Opposing Point','Opposing Evidence'),
('f649ca28-ceb7-4917-9196-ccc1cdf772f1'::uuid,'245b6efe6652ffc783002123f1f3a62d','This general line of argument may be reasonable, but it simply does not follow that chimpanzees have anything like human language.','Evidence','Conclusion'),
('742572f9-a5a5-45c3-902a-e374fcf00f4d'::uuid,'64dae0e7fc68e6adf6ed00ad6efefac2','Humans did not evolve from chimpanzees. Chimpanzees are closely related to humans only because both evolved from a common ancestor, and the evolution of human language might easily have begun after the extinction of that common ancestor.','Conclusion','Evidence'),
('faeec81a-8f99-4993-b190-fdb631d6d733'::uuid,'9c7a82eee8d8bb9bac6710d9e1be18d1','The reason is that reforms are generally undertaken early in a new government.
(*why should we believe that?*)','Intermediate Conclusion','Intermediate Conclusion'),
('17884611-816c-465a-97e6-8a2062b1a24f'::uuid,'129beca1aa6c5fed133bba8ce0f54e8a','If leaders don''t act quickly to solve a problem and it becomes an issue later, they must either deny there is a problem or deny that anything could have been done about it. Otherwise, they have to admit responsibility for the problem persisting. Waiting puts leaders in that bind, which is why reform tends to come early.','Evidence','Evidence'),
('37b696bf-f5fe-452b-80bb-a04d449faf90'::uuid,'ef9b4386c4a3146c2eaefd26a4b41ef2','Whenever we''re doing Main Conclusion, we prime our brain before reading the paragraph: "Remember, on Main Conclusion and Role, the conclusion usually appears **earlier** than its support."

For these questions, the conclusion is usually
- the first sentence
or
- a rebuttal

When we read this first sentence, we''re asking ourselves, "Is this the author''s conclusion? Does it sound like the pundit''s opinion?"

The normative language "it is good to X" tells us that the first sentence is an opinion. If the rest of the paragraph tries to support that claim, then we''ll know that the first sentence was the main conclusion.

The second sentence telegraphs that support is being provided by saying "the **reason** is that ..."

The third sentence explains why reforms come early. A leader who waits on a problem has to deny the problem, deny anything could have been done, or admit responsibility for it. Each layer supports the one above it, and the first sentence supports nothing else. That is the main conclusion.','Evaluate','Evaluate'),
('dd7d6e60-de99-4bde-b1b3-11fb9b0bbfd8'::uuid,'d00ecbdf54239996a386d4b9502acf76','Find an answer that says the same thing as the first sentence: it is good for national leaders to be voted out of office after a few years. Watch for answers that restate the support about reforms coming early, or that invent new claims about motivation or time in office.','Goal','Goal'),
('3709b645-473e-4c56-9f12-87e7130f8a61'::uuid,'fbefa5ef6f436d44d4e74063e3c7bb04','Many people with access to the Internet express a longing for emotional connection to a global human community, which often leads them to use the Internet to learn about other cultures.','Opposing Ideas','Context'),
('1a438dd8-b976-47a9-9499-c31e240741a1'::uuid,'44539ecb91ddb89bfc3c06feeff56e4d','This argument follows a pattern you will see often on Main Conclusion: setup, pivot, conclusion, reason.

The first two sentences describe what many people do: they long for a connection to a global community, so they use the Internet to learn about other cultures. Then "However" turns the paragraph. The columnist doesn''t dispute that people do this; the claim is that it probably won''t work. "for" then introduces the reason: the Internet is used mainly for acquiring information, not for developing feelings of interconnectedness.

Check with the support test. Why believe that learning about other cultures online won''t satisfy the longing? Because the Internet is mainly an information tool. The reason fits, so the sentence between "However" and "for" is the conclusion.

Keep its boundaries in mind: it is about learning through the Internet, it is hedged with "probably," and it is about the longing for emotional connection.','Evaluate','Evaluate'),
('1f6ab750-57ee-49a9-b386-eb84a74794c1'::uuid,'c87f97d8fcd30c41d8866ddda6714419','Expect the correct answer to say that, for people who long for emotional connection to a global community, learning about other cultures through the Internet probably won''t satisfy that longing. Keep the hedge and the Internet setting.','Goal','Goal'),
('33828dbe-43ee-4861-b7df-b175a3adf075'::uuid,'065088003de8a7e4c9018dd8109dbe82','Banking industry visionaries foresee a bright day in the near future when customers will be able to transact all their financial business by means of computers or telephones from the comfort of their own homes.','Opposing Evidence','Opposing Point'),
('094f289f-7210-494a-85ae-098afcfce9b5'::uuid,'a943bcce0cc14025bd11f253e33ef7a5','As banks eliminate their branch offices and customer-service employees, customers will have to serve as their own tellers, and pay more transaction fees for their efforts.','Evicence','Evidence'),
('34c9d326-a55d-4f8d-a204-c0e5e8a6d76c'::uuid,'5f6d7d4002474afbaf7f54adc2bd31e1','Main Conclusion paragraphs often open with someone else''s view and then push back. This one does. The first sentence belongs to the banking industry visionaries, who see home banking as a bright day. Then "But" turns the paragraph: that may be more of a paradise for banks than for their customers. That sentence is the author''s own view.

Run the support test. Why believe home banking helps banks more than customers? Because banks will cut branches and staff, and customers will do the tellers'' work and pay more fees for it. The last sentence answers the question, so it is evidence, and the sentence after "But" is the conclusion.

Notice the claim is a comparison (banks more than customers) and it is hedged with "may."','Goal','Evaluate'),
('a78e131c-aa9f-4d01-977d-4b3d44c056fa'::uuid,'8377cb46f26d7ae7832362c690f59b7c','This is a three-layer argument, and the indicator words map it for us.

"After all" means the sentence that follows supports the one before it. So the first sentence is the main conclusion, and the claim that social movements have adopted popular music is support for it. Inside that sentence, "since" adds a deeper layer: movements adopt popular music because it can help convert nonmembers, raise morale and express solidarity.

Music can convert, raise morale, express solidarity
→ Social movements have adopted popular music to express their viewpoints
→ Popular music has been used for religious and political messages, which many listeners don''t realize

Now look at what the support actually proves. Social movements using music to express their viewpoints shows that popular music does more than entertain. It shows nothing about what listeners realize. So the part of the conclusion the evidence backs is this: popular music has been used for something besides enjoyment. Expect the right answer to state that core in its own words.','Evaluate','Evaluate'),
('9499c2a9-a70b-48aa-bf1c-d84142bcc9b2'::uuid,'6052306e4744d9ce5ae2a3f63b0bc15a','Look for an answer that captures the point of the first sentence: popular music has served purposes beyond simple enjoyment, such as carrying religious and political messages. The answer may be more general than the stimulus. Watch for answers that inflate the evidence about social movements or bring in claims the author never makes.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;