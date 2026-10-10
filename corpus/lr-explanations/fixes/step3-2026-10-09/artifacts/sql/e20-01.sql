update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('60b131b6-a973-463f-aafe-09362438b040'::uuid,'1fa2b7bed1f7c7ff676682ad74491c4c','This is a curious fact with two competing stories. The fact: this society burned large areas of land. The rival story: the burning cleared ground for planting, so the society was turning to large-scale agriculture. The author''s story: the society was still hunting and gathering.

The author''s only support is an absence: little evidence of cultivation after the fires. That is a fair point against the farming story, but it leaves a hole. If these people were hunter-gatherers, why were they burning large areas of land at all? Right now the burning has an explanation under the farming story and none under the author''s.

Given that the society burned large areas of land, how could we still argue that it was farming? We could say crops were planted but left little trace, or that the land was burned for some other farming purpose. Nothing in the argument answers the basic question: what would hunter-gatherers want with a big fire?','Evaluate','Evaluate'),
('3d637c76-8c6a-4650-9ad8-8fa720de43bd'::uuid,'75db097a9839b538c6dcc71607b175ae','Look for an answer that gives hunter-gatherers a reason to burn large areas of land. That turns the burning from evidence for farming into something the author''s story expects. A second acceptable shape: more evidence that the burning was not done to clear ground for planting. Answers about small fires, or about farming in other societies, will not do this work.','Goal','Goal'),
('bba7ef62-0a16-4a9f-ade3-0a0b759dd2ba'::uuid,'ca9e52dd1b063c3b6779b3f539ab4710','The premise is about problems: most daily-life problems need knowledge from more than one discipline. The conclusion is about courses: schools should require interdisciplinary courses instead of single-discipline ones. The gap is the jump from what problems need to how courses must be built.

Given that most daily-life problems need more than one discipline, how could we still argue that schools should keep single-discipline courses? Easy. Students could take several single-discipline courses and then combine what they learned when a real problem shows up. If students can do that combining on their own, interdisciplinary courses are not needed.

So the educator is assuming that students in single-discipline courses will not put their knowledge together on their own.','Evaluate','Evaluate'),
('a9b995df-a258-4b59-bd78-4ed1b9edaf72'::uuid,'354350dfedf7be45f7be72dd9ccf084c','Look for an answer that shuts down that objection: students who take only single-discipline courses do not, or cannot, combine what they learned. A second acceptable shape links premise to conclusion directly: if daily-life problems need several disciplines, schools should teach across disciplines. A strengthener does not have to prove the conclusion. It only has to make it more likely.','Goal','Goal'),
('e4f2e465-fe3c-43e5-88ed-ac3bb4c78929'::uuid,'f3ef18453d82d6c84053e7a2fe04438e','The psychologist presents a correlation:
```
more stressed by speaking (introverts)  ||  bigger blood pressure rise
```
Then the psychologist concludes that one causes the other: the stress of communicating drives the rise, not the physical work of producing speech.

That is a Curious Fact → Causal Explanation argument, so we check two things:
1. Is there an alternate explanation for why introverts'' surges are bigger?
2. How plausible is the author''s explanation?

Given the correlation, how could we still argue that physical exertion causes the rise? Maybe introverts and extroverts differ in some physical way when they talk, or in some health factor that changes how much their pressure moves. The bigger problem: whenever someone speaks, communicating and the physical act of speaking happen together. The argument never pulls them apart.','Evaluate','Evaluate'),
('179a492d-c909-420b-b1ca-629f60a75a89'::uuid,'e54656de8271afd4bf8884adf13fbdf7','Look for an answer that separates communication from the physical work of speaking and shows blood pressure following communication. The ideal case: communication without vocal speech, or similar physical effort without communication. A second acceptable shape rules out an alternate explanation for why extroverts'' surges are milder.','Goal','Goal'),
('709e28bc-36a1-4abe-aa2a-c5b77ae40e96'::uuid,'d51297a607323439f52baf4042d74aba','This premise is conditional. By contrapositive, it tells us something about every frying pan that comes with a warranty.
```
manufacturer offers a warranty  →  manufacturer does not expect to reimburse many customers
```
So the author says we should only buy pans with a warranty, because a warranty means the manufacturer is not worried about paying out a lot of claims.

The author assumes the manufacturer is not worried because the pan is good: it is not expected to fail for many buyers.

But maybe the manufacturer is not worried for a different reason. It might expect plenty of pans to fail and still bet that few customers will bother to claim.','Evaluate','Evaluate'),
('c11586d4-6ad8-4cf4-bd8b-acd63bc0cd8b'::uuid,'7aff3cf06d16ac1c285c729fa13f2546','Look for an answer that closes that gap: a pan that does not work well or last long really would cost its manufacturer, because many buyers would seek reimbursement. Then a warranty can only sit on a pan the manufacturer expects to hold up.

Notice who the conclusion is talking to: a buyer who would never bother to claim. So the answer has to be about other buyers. Their claims are what make the warranty mean something.','Goal','Goal'),
('19040624-732b-4a02-93a5-00bc449fc4b1'::uuid,'1da894e9961221f7d72f7ac853691554','There is no evidence here, just one claim. So our job is to find reasons to believe it.

Think about how a longer prison term is supposed to work. It deters only if a would-be robber knows the penalty, expects it to apply, and weighs it before acting. So the claim gets support from anything that breaks that chain: robbers who do not know the sentence, robbers who do not expect to be caught, robbers who are not weighing costs at all. It also gets support from a similar case where a longer term made no difference.','Evaluate','Evaluate'),
('d0bb375a-3648-4bd9-a02b-6fb47fef2005'::uuid,'d1a9ac878bfd22657a7ac15c7cdedb18','Four answers will give one of those reasons to believe a longer term would not discourage robbery. The answer we want gives none. Expect it to have no clear impact on what a longer term would do, or to cut against the claim.','Goal','Goal'),
('a6cc6932-a37b-44fd-8e4c-ab06d99aef6d'::uuid,'433ee42bc32ebb5505515ddc93f0439b','The evidence counts fatal accidents: in each of the last ten years, more happened during the day than during the night. The conclusion is about risk to "an individual": driving by day is more dangerous for each driver.

Given that more fatal accidents happen by day, how could we still argue that night driving is just as dangerous? Count the drivers. If far more people drive during the day, the day could have more fatal accidents and still be safer per driver. A bigger total is not a bigger rate.

So the argument needs a reason the danger itself is higher during the day: something about daytime driving that raises the risk for each driver.','Evaluate','Evaluate'),
('d5fd6170-1471-444c-b0a0-ed19be5c4538'::uuid,'47b6a1649fa355a8e179c25143131710','Four answers will strengthen by giving a day-specific risk: something that makes each daytime trip more dangerous, or each nighttime trip safer. The correct answer will not. Expect it to show no day-versus-night difference at all, so it cannot explain why the day is more dangerous.','Goal','Goal'),
('db6c1efe-c0d1-456f-ad76-549a53a60d6a'::uuid,'5fc6e19a861f9c46291ae21afa949b47','Those persons who are perceived as forming opinions of others only after cautiously gathering and weighing the evidence are generally resented.

In short: appearing prudent gets you resented.
AP → R','Evidence','Evidence'),
('82c7591b-dce5-49e2-8b20-53233f5721ef'::uuid,'7ddd6f1e241fe30a76d4cac1f8ed8689','It is imprudent to appear prudent.
AP → ~P

Here ~P means not prudent.','Conclusion','Conclusion'),
('e81ea5ed-4f01-491d-9945-b76f6fc53393'::uuid,'b30e3f786835b3e3aa530a8469ad8ed9','Line the two up. The premise starts at appearing prudent and ends at being resented. The conclusion starts at appearing prudent and ends at imprudent. Same start, different finish. Being resented shows up only in the premise, and imprudent shows up only in the conclusion, so the missing piece has to connect them:
R → ~P
In words: causing people to resent you is imprudent. Add that and the chain runs
AP → R → ~P
which is the conclusion.

The first sentence, that people want to be instantly and intuitively liked, explains why cautious people are resented. It is background. It never reaches the conclusion''s new idea.','Evaluate','Evaluate'),
('3d1ff9f9-4099-40e6-9e1e-86fcaf485884'::uuid,'852d0958abb0efb920df32145377a603','Both premises use without. A sentence of the form no X without Y means X needs Y: X → Y.
```
IF → SI
GL → SI
```
Individual freedom requires social integrity. Pursuing the good life requires social integrity.','Evidence','Evidence'),
('74c50797-a803-4897-ad50-3044f024d32d'::uuid,'dd20859981dbcefaa2255fae635ac5ac','```
IF → RL
```
Individual freedom requires the rule of law. The rule of law appears only here. No premise mentions it.','Conclusion','Conclusion'),
('9560d25c-6fa3-40ec-ac88-b074d3779532'::uuid,'512fc7dee4d211b751eb303aa9c5a9af','Start from the conclusion''s trigger, IF. The first premise takes us from IF to SI. Then we are stuck: nothing takes us from SI to RL. Supply that link and the chain runs
```
IF → SI → RL
```
which gives IF → RL.

The second premise, about the good life, is a distraction. GL also points to SI, so two arrows lead into SI and none lead out. The good life never connects to individual freedom, so it cannot help.','Evaluate','Evaluate')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;