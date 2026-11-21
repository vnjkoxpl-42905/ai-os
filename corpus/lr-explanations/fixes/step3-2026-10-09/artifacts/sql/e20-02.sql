update lr_explanation_choice_notes t set body=v.nb from (values
('1f09730b-aa9b-4b7e-b943-461b5db1c335'::uuid,'beba3bee5f9c8203d4498abddb6fbc97','A says that in many ancient cultures, agriculture came first and fire-clearing came later. That says nothing about why this society burned its land. If anything, it hints that a society clearing land with fire already farmed, which leans the wrong way. It gives no hunter-gatherer reason for the fires.'),
('8980f5f9-efad-4832-b05f-632bf82a814e'::uuid,'942968786756f6c79115f4d225d04053','Cooking and heat explain campfires, not the burning of "large areas of land." Farmers cook and keep warm too, so this use of fire fits both stories equally. A strengthener has to explain the large-scale burning in a way the hunter-gatherer story predicts and the farming story does not.'),
('e5cf4e7f-0af4-4f90-98b2-00502ec1cb44'::uuid,'72f2b7b1048725b61b3b6ca5dd051966','C says fire releases the seeds of certain plants. That is a fact about plants, not about why this society burned land. The seeds are "inedible," so it does not give foragers a food reason to burn. And if fire helps plants spread, it might even suggest a planting motive. No link to hunter-gatherers, so no strengthening.'),
('1719a8e0-8f29-49c6-bc52-2ff43f0ea6b8'::uuid,'f0cfc2dbd343290440bcc6e0dcc53b35','D supplies the missing reason. Hunter-gatherers are known to burn land to move animal populations from one area to another. Now the fires have an explanation that fits the author''s story, and the lack of cultivation afterward is exactly what we would expect: the fires were for hunting, not planting. The burning stops counting as evidence for farming.

The move to repeat: when an argument picks one explanation for a fact over a rival, look for an answer that explains the fact under the author''s story. A fact only the rival story can explain is a liability until an answer like D removes it.'),
('d222714c-739f-40ce-9fdf-43712069449c'::uuid,'73113ade47524e58221e690bfec86bc2','E undercuts one possible farming motive: burning to enrich the soil. But the farming story in the stimulus is about clearing ground for planting, not adding nutrients, so E leaves it standing. And weakening a farming motive still gives hunter-gatherers no reason to burn large areas, which is what the argument needs.'),
('0202d8c0-b410-4b0e-aa2d-42044621f900'::uuid,'7676e800adba17c3f6103dcffd91ac4d','A says common sense usually solves daily-life problems. That does not tell us which kind of course better prepares students, so it cuts the same way against both. If anything, it makes all coursework matter less for daily life, which gives the educator''s recommendation no help.'),
('7799cd57-36fa-4da9-8fc9-9ee1424424d1'::uuid,'002ceb480561c724e1bc0fbd854a30b6','B gives a reason to keep the current system: most teachers do a better job with single-discipline courses. If teaching quality drops when schools switch, students might learn less under the educator''s plan. That pushes against the conclusion, so it cannot strengthen it.'),
('931c94e9-77fe-45ff-8308-696b53363bdd'::uuid,'3cf43a0cabb0c14331f7ff868c046251','C answers the objection we built. Students who take only single-discipline courses "are rarely able to combine knowledge from those disciplines." Put that next to the premise: daily-life problems need knowledge from more than one discipline, and these students rarely put disciplines together. So single-discipline courses leave students short, and courses that combine the disciplines for them make sense.

The move: when a recommendation is built on a need, ask how the current approach might already meet that need. The answer that says it does not is the strengthener.'),
('e4b87a42-1013-4f48-b7a9-4f263d4945a7'::uuid,'d560010ec62b8b2235efa60f05b2a214','D says most students in single-discipline courses "can effectively solve many problems faced in daily life." If they already handle those problems, the case for switching gets weaker. D is the objection from the Evaluate step stated as fact, so it weakens.'),
('36af108a-ee4c-430d-8b59-948d7a6a54d8'::uuid,'0e9bbe87c94b5b34ceb46ee1fff3aaa6','E says most interdisciplinary courses are not designed to teach daily-life problem solving. If the courses the educator wants do not aim at that goal, switching to them looks less useful. That is a reason to doubt the plan, not to support it.'),
('69112128-691d-47b6-a008-628b3a139085'::uuid,'313a536ec01b92875d36ed41510c33fc','A says blood pressure medication does not stop the rises during speech. That tells us the rise is hard to block, not what causes it. A rise driven by stress and a rise driven by physical exertion could both get past medication, so A favors neither cause.'),
('4b9fdb27-d274-4df2-99c9-49b443c128de'::uuid,'816b0d0d54abab344d7c943aa9e854fd','B links a person''s typical blood pressure to how much it rises under stress. It never separates stress from physical exertion. If anything, it opens an alternate explanation: if introverts had lower typical pressure, their surges could be bigger without speaking being any more stressful for them.'),
('2bbcd858-e618-42a4-b6bb-4ec8a4c1bb13'::uuid,'355c015c595284ba2bf7fad0103f38cd','C says introverts often sense the rises when they talk. Noticing a change says nothing about what caused it. An introvert could feel the rise whether it came from stress or from the physical work of speaking, so C does not help the psychologist.'),
('89f3a439-df4b-456a-bd8c-dc1d2f79ee48'::uuid,'0323b847eb16c406d901b96ace9d9992','D builds the test we wanted. Signing is communication with no vocal speech production. Moving the hands for other reasons takes similar physical effort with no communication. Blood pressure rises for signing and shows "no change" for the other hand movements. With the physical effort held roughly constant, only communication changes, and blood pressure follows communication. That cuts down the physical-exertion explanation and supports the stress of communicating.

The move: when an argument picks between two causes that always show up together, the strongest support finds a case where they come apart and shows the effect tracking the author''s cause.'),
('0ed5b5cd-0c23-4dde-aa4d-c486b504d77f'::uuid,'5679bbe9484249e43d72d33cdb3e7581','E looks relevant because it is about extroverts and blood pressure, but it weakens. If extroverts are more likely to take blood pressure medication, the medication could be what keeps their surges mild. That is an alternate explanation for the very difference the psychologist credits to stress.'),
('926ede8d-cc27-4508-a22c-d276094388d5'::uuid,'76f29fdb5c3bd336a2bb54c5b32a5a38','A says most people who buy a pan with a warranty "would seek reimbursement" if it failed. Now follow the chain. If the pan were bad, many buyers would claim, the manufacturer would have to reimburse many customers, and by the premise it would not offer the warranty. So a pan with a warranty is one the manufacturer expects to work well and last. That is why even a buyer who would never claim should buy it.

The move: when a premise says a party avoids a cost, check what makes the cost real. Here the cost depends on buyers actually claiming, and A supplies that.'),
('a8655c27-9884-4436-8064-4aa63507a69f'::uuid,'de9239a83fe30df3c5d1af8f43ac1dda','B compares pans only "at the time of purchase." The argument cares whether a pan will keep working and last long, which is what a warranty is supposed to signal. A pan can match the others on day one and still fail in a year. B also says nothing about why manufacturers offer warranties, so it does not connect the premise to the conclusion.'),
('500d8893-bc1c-41bb-b6c1-a0157417e472'::uuid,'fd1cb5113567a6d71109bd042baa6a5e','C ties price to warranties. It does not show that a warranty means a good pan. The conclusion already accepts paying more, so learning that pans with warranties tend to cost more adds no reason to buy them.'),
('d3817786-71a8-4beb-babd-7fff4c5458c4'::uuid,'2c22b07bf176a54c33271dbfe743dba0','D ties price to quality. The conclusion says to buy pans with a warranty, not expensive pans. Even if the priciest pans last longest, that gives no reason to prefer a pan with a warranty over one without at the same price.'),
('513c2131-a3bf-416d-b267-cd5c95fcfeff'::uuid,'2c1f0a61b920f1fbe0d33b6025afc0f7','E says most warranties "provide for full customer satisfaction." That describes what a claim gets you. But the buyer in the conclusion would never make a claim, so the warranty''s terms do not matter to them. E also does not explain why a manufacturer would avoid putting a warranty on a bad pan.'),
('65750e5e-9b29-4c54-83ed-64e151e80a0d'::uuid,'f960180b6db13b01bd9ba8814655aa5c','If many robbers are driven by "thrill-seeking and risk-taking," they are not carefully weighing costs, and a longer sentence may even add to the risk they enjoy. Either way, a bigger penalty is unlikely to stop them. That supports the claim.'),
('928882e6-b545-40eb-98d5-ebd431a15301'::uuid,'7a73e59e85e06ff4cf2f1e8110cd891c','B is an analogy. A longer prison term for embezzlement did not change how often that crime was committed. If longer terms failed to deter a similar crime, that is some reason to expect the same for robbery. It supports the claim, as far as the two crimes are alike.'),
('8fe2f2a7-a4bb-476a-89dc-5bb4d29062b2'::uuid,'470919646f36126e338e1f769bb00305','C is about the past: robbery terms "have generally decreased in length recently." The claim is about what would happen if terms went up. Knowing that terms went down tells us nothing about whether raising them would deter anyone. C gives no reason to believe the claim, so it is the exception.

The move on Strengthen EXCEPT: list the kinds of support before reading the choices. Here that list was robbers who do not know the sentence, do not expect to be caught, or do not weigh costs, plus a similar case. The answer that fits none of them is the one to pick.'),
('a0d5bed2-5993-4708-a4b1-e0910d43ca8a'::uuid,'c9496830f78d31f5af13cad7ee6eac6a','If most robbers believe "they will not get caught," they do not expect any sentence to apply to them. The length of a term they never expect to serve cannot weigh much in their decision. That supports the claim.'),
('b8247c03-271a-4dac-98bb-02dec610ed00'::uuid,'eedc4ae9e034061aaae1ec59f288d8a5','If most robbers "have no idea what the average sentence for robbery is," they would not notice a longer one. A penalty you do not know about cannot deter you. That supports the claim.'),
('a9ad1aad-ad09-4492-9333-23ced104dce8'::uuid,'563932e34a3fa50032e38384847b77e3','A gives a daytime-only hazard: only during the day do unsafe vehicles outnumber safe ones. Every daytime driver shares the road with more unsafe vehicles, so the higher daytime death count reflects real risk, not just more traffic. That strengthens.'),
('1351a44c-5b03-490f-8c56-5315ac1401ea'::uuid,'eba06efa2509c52609d3610317ad1f08','B says there is less law enforcement during the day. Less enforcement plausibly means more reckless driving goes unchecked, which raises the risk for each daytime driver. That is a day-specific reason for the extra fatal accidents, so it strengthens.'),
('5b35563d-8f14-485f-b9d9-90cf2fec3c8d'::uuid,'1e588ab8dc90138ac9b4f54a61843721','C says people drive more cautiously at night. That makes each night trip safer than a day trip, which explains the extra daytime fatal accidents with something other than traffic volume. It strengthens.'),
('df83e2aa-29d5-49f2-b7b5-b2dd4836b084'::uuid,'062b8a6ca66c90a399577a7617d04174','D is the exception. More travelers per vehicle over the past ten years is a trend across day and night alike. It might raise deaths per accident, but nothing in D says the change hits daytime harder. Without a day-versus-night difference, it does nothing to show the day is more dangerous for an individual.

The move on a Strengthen EXCEPT built on a comparison: each strengthener has to favor one side of the comparison. An answer that applies equally to both sides cannot help.'),
('5a57d2c0-480d-498d-8004-5e02b9025d8c'::uuid,'ea7807e43ea033731ba1eca91c7b0866','E says people drive faster during the day than during the night. Higher speeds make crashes more likely and more deadly, so each daytime trip carries more risk than a night trip. That is another day-specific risk, so it strengthens.'),
('22ea66a2-1b49-4d4a-9e6b-06db83e87cc6'::uuid,'152c6a8815cd02652af588e33c6fad9f','A says people who act spontaneously are well liked. That is about acting spontaneously and being liked, not about appearing cautious and being resented, and it never mentions prudence. The gap is between resentment and imprudence, and A touches neither side of it.'),
('d3bfaf37-b722-48ff-8344-0335eec1d047'::uuid,'ff102199a9569a00e732d6763be8a653','B starts from imprudent people:
~P → acts instantly and intuitively
That puts imprudent on the trigger side, but we need to prove imprudent, so it has to be on the outcome side. B also talks about how people act, while the argument is about how they appear. It cannot finish the chain.'),
('0a252cd3-c2c0-4c71-9d51-5fca62ff3efa'::uuid,'3921673794a324aa44f7a97f54a885e3','C says people resent those less prudent than themselves. That is about who gets resented, and it points at the less prudent, not the cautious people in the premise. It never says that being resented is imprudent, so the conclusion still does not follow.'),
('22cc2a02-2e4b-4448-a2ae-b5104d4db920'::uuid,'f828fc07d531089f4c239c65bf4445d8','D is about whether intuitive people know instantly when they like someone. The argument needs a link from being resented to being imprudent. D mentions neither resentment nor prudence, so adding it leaves the gap where it was.'),
('f533f925-38b7-477d-8ab3-151992ee45fe'::uuid,'2200e0544bcbb4cd2bdb1caae40d8974','E says it is imprudent to cause people to resent you:
R → ~P
Chain it to the premise: appearing prudent gets you resented, and causing resentment is imprudent, so appearing prudent is imprudent.

The move on Sufficient Assumption: find the idea in the conclusion that no premise mentions (imprudent), find the premise idea that never reaches the conclusion (resented), and pick the answer that joins them in the right direction.'),
('042aef57-bc70-4eec-9d97-b1e39ee1c248'::uuid,'a2d03d4de07ce72f28dee1bee656940c','A says there can be no rule of law without social integrity:
```
RL → SI
```
That is the link we need, backwards. With IF → SI and RL → SI, both arrows end at SI, so nothing carries us from IF to RL. Watch for this reversal on any chain question.'),
('ef210e79-2019-4dc6-b357-a516021df7fd'::uuid,'fff7ed88b89040264c2c88dd3467997f','B says there can be no social integrity without the rule of law:
```
SI → RL
```
Hook it onto the first premise: IF → SI → RL, so IF → RL. That is the conclusion.

The move: when the conclusion has a term no premise mentions (the rule of law), the assumption must run from the end of the premise chain to that new term.'),
('2537095c-c154-420b-815c-fd855119d919'::uuid,'c49587d45f4884ad4d8ea9714661096c','C says one cannot pursue the good life without the rule of law:
```
GL → RL
```
That helps only if we can get from IF to GL, and we cannot. The premise gives GL → SI, and nothing leads into GL. C would work only if the good-life premise were reversed (SI → GL).'),
('dfac5e14-f75c-471d-ae82-62ace6cd97fd'::uuid,'6daae033e99c3efd86e22ac9973d909f','D says social integrity is possible only if individual freedom prevails:
```
SI → IF
```
That reverses the first premise. It points back toward IF, and RL never appears, so the conclusion''s new term is still out of reach.'),
('dc8d503e-f9f3-4b83-a1ff-c57a13053453'::uuid,'2637a8b68a991254bb4cd76a4228b4ca','E says there can be no rule of law without individual freedom:
```
RL → IF
```
That is the conclusion reversed. Assuming the reverse of what we want to prove does not establish it.')
) v(id,ob,nb) where t.id=v.id and md5(t.body)=v.ob returning t.id;