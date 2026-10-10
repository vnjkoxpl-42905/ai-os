update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('f23671f1-a452-49dc-b932-5172e154f330'::uuid,'4b44f027948580f8db31ed44576c2842','Rain is the only effective check on grass and brush fires.
When rainfall stays below normal for an extended period, there are many more of these fires.','Given That','Given That'),
('c8a11028-e252-4971-a598-7046817c23c7'::uuid,'9fbe49fd4a4558fb6472aa3131a6e932','Line the two periods up side by side:
```
Severe Drought        vs.   Normal Rain
many more fires             fewer fires
less $ damage               more $ damage
from fires                  from fires
```
Total damage is the number of fires times the damage each fire does. Drought brings many more fires, so if the drought total is lower, the average drought fire must be doing far less damage than the average fire in a normal year.

So ask: what is different about a fire in a wet period that lets it do more damage? Rain does more than put fires out. Rain also grows plants, and plants are what these fires burn. A long drought leaves less to burn.

Goal: look for an answer that makes each normal-rainfall fire bigger or costlier, or each drought fire smaller. Be suspicious of any answer that is equally true in drought and in normal rainfall. A fact that does not change between the two periods cannot explain a gap between them.','Evaluate / Goal','Evaluate / Goal'),
('dfd0a1a1-b154-4f26-8541-e0651f776943'::uuid,'0a8e2efad8169cce719f06af1b8dcd38','Since we know rescue squads save the lives of climbers, how would getting rid of the rescue squad lead to fewer climbing deaths and injuries?
There must be something else different in a world without rescue squads that would lead to fewer climbing deaths and injuries. Maybe having a rescue squad emboldens people to take risks they wouldn''t otherwise take. It''s like if you take away the safety net from a trapeze, a lot fewer people are going to attempt the trapeze, and so maybe you get a net reduction in trapeze injuries.','Evaluate','Evaluate'),
('6138ce7b-e290-43db-ab1d-8ffaf0fe97c8'::uuid,'3850bfb9bab87c73f99281431b1cd921','Look for something that would be different in a world without rescue squads, something that would put fewer climbers in danger in the first place. The likeliest shape: the squads change who climbs, or how carefully they climb, by making the mountains feel safer than they are. If the squads draw enough extra people into danger, removing them could cut the toll even though each rescue saves a life.','Goal','Goal'),
('c7a81d9b-e963-497e-8042-2e432a697a8f'::uuid,'24515d00c53f27365475d2b46db18137','Jimmy replaced the old gas water heater with a new, pilotless, gas water heater that is rated as highly efficient. After that, Jimmy''s gas bills increased.','Apparent Paradox','Apparent Paradox'),
('a6a23aa9-aaaa-4593-b1bd-99de298dc8b6'::uuid,'f981f7fe9de480f9de00d9c7462d296d','This is less a paradox than a surprise. A highly efficient heater sounds like it should lower the bill. But the bill depends on two things: how much gas the whole household burns, and the price of each unit of gas. The water heater is only one of the things in the house that burns gas.

So the bill can rise, even with a better heater, by two routes.

Route one: more gas used somewhere in the household. More people, a new gas appliance, more heating.

Route two: a higher price for each unit of gas.

The new heater''s efficiency only shrinks the heater''s own use. It does nothing about the rest of the house or the price.','Evaluate','Evaluate'),
('64c64245-41ef-40e8-93d3-dc2e23e5b14f'::uuid,'e619346b426a76a08ea7cabd62d0c472','Notice what the stimulus measures: the retail profit margin, meaning how much profit stores keep out of what they take in on PC sales. Rising demand might make us expect fat margins, since stores could charge more and still find buyers. But demand is only one input. A margin depends on the price the store charges and on what it costs the store to make each sale.

So there are two routes to a thin margin.

Price is held down: heavy competition, or stores choosing to keep PC prices low on purpose.

Costs are pushed up: expenses that come with selling PCs in particular, such as extra staff time or stock that loses value.

The stimulus also compares PCs with other popular high-tech items, so the strongest explanations hit PCs harder than those items.','Evaluate','Evaluate'),
('2ecfc5bb-81ac-4888-9b83-615ca55fdd7d'::uuid,'9e668710e36356fca16d64f0f04fd02f','We need to find four reasons why PC''s have a lower profit margin (or why other popular high-tech items have a higher profit margin). Each one should either lower what stores can charge for PCs or raise what it costs stores to sell them. The exception will do neither. Watch for an answer that is about PCs and their buyers but never touches the store''s price or cost.','Goal','Goal'),
('847bb3f5-435f-48a5-9ebd-c3907c2d2900'::uuid,'86a3f4c443e9560696900460c515719d','This is less a paradox than a result to explain. We might expect bottling up upsetting feelings to backfire, yet the repressors come out ahead on every measure: less shy and anxious, better frustration tolerance, better social skills, higher grades, more self-esteem.

An answer contributes if it gives a reason for any one of those advantages. There are a few ways in.

Something about repressing helps directly: it keeps repressors focused, or keeps them from pushing people away.

Something about sensitizers drags them down. The finding is a comparison, so a sensitizer disadvantage explains the gap just as well.

Something outside the students treats repressors better.

So we eliminate four answers that give a reason for at least one advantage. The exception will explain something else, such as why repressors repress in the first place, rather than why they have the advantages.','Evaluate / Goal','Evaluate / Goal'),
('6ea0a928-0732-4f7d-8489-f6b316a10c6f'::uuid,'230d5e9f0cc2da5424470d1b016b55a4','Premise: People who have never been asked to do more than they can easily do never do all they can.
(Never pushed → never does all they can.)
Premise: Alex has not done all that Alex is capable of doing.
Conclusion: No one has ever pushed Alex to do more than what comes easily.','Original Argument','Original Argument'),
('2e179b89-b749-4bf4-8adb-9d1284ecddf1'::uuid,'db028c37a4f47d3b7e079f87ebd04fd1','The flaw is affirming the consequent, also called mistaking a necessary condition for a sufficient one. The rule says: never pushed → does not do all they can. The argument sees the right side (Alex is not doing all Alex can) and concludes the left side (Alex was never pushed).

But the rule only runs one way. Someone who was pushed hard might still fall short: laziness, illness, bad luck. Falling short is necessary for being never pushed (everyone never pushed falls short), but it is not sufficient to prove it. The argument treats Alex falling short as enough to prove Alex was never pushed.

In plain shape:
All A are B.
X is B.
So X is A.','Evaluate','Evaluate'),
('24c39abf-6eb6-48c7-88c3-ba3de8524ecf'::uuid,'b4cd3e00959a193e04eb74dd221af45a','Find an answer with the same shape: a rule (A → B), a fact that something has B, and a conclusion that it has A.

For each answer, diagram the rule, then ask two questions. Does the evidence land on the rule''s right side? Does the conclusion land on its left side? Expect two kinds of traps: an answer that negates the left side instead (a different flaw), and an answer that runs a valid contrapositive (no flaw at all).','Goal','Goal'),
('29df0386-d9ee-4487-bccc-5ed11a66c7be'::uuid,'58028f141b637437941ea97925e444f7','The evidence is a comparison between two groups: people who use a tax preparation service get refunds about 50 percent higher, on average, than people who do not. The conclusion turns that into advice: use a service to get a large refund. That move assumes the service causes the bigger refund.

How else could the gap arise? Maybe the people who hire a service are the ones with complicated returns, more income or more deductions, and they would get big refunds whoever did the paperwork. The big refund might be the reason they paid for help, not the result of it.

This is a causal flaw: a correlation between two groups treated as proof that one thing produces the other, then used to recommend it.','Evaluate','Evaluate')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;