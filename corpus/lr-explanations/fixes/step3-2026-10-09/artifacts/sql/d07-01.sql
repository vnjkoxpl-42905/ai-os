update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('9bfcc23e-1bbd-44ba-962f-dadd6f3f30d1'::uuid,'87aa246af8d119485253371bcb032b91','Causal chain:
Electrified instruments → each musician plays louder → fewer musicians per band, on average

Pivot (nevertheless):
Electrified instruments → more musicians playing popular music professionally','Facts','Facts'),
('981bba23-7b58-4924-a7f4-1cb69e2341a9'::uuid,'99027f44fae36d54aa76c4fa28cfc13b','On a Most Supported question, cause and effect is the first thing to read for, and this paragraph is full of it: electrification enabled more volume, the extra volume shrank the average band, and electrification also raised the number of professional musicians.

Then the pivot word "Nevertheless" sets two results of electrification against each other:
1. Fewer musicians per band, on average.
2. More professional musicians overall.

When a pivot creates a math tension like this, the correct answer usually resolves it. So ask: if each band has fewer people, how can there be more people in total?

There have to be more bands. Run numbers. Say there used to be 80 bands of 10, which is 800 musicians. If bands now average 5 and we have 1,000 musicians, we need 200 bands. Smaller bands plus more musicians forces the number of bands up.','Evaluate','Evaluate'),
('777c8a66-eae6-4c4c-8411-1e960acb9087'::uuid,'288a7e03e3c55b9807749772810805dc','Look for an answer that says the number of bands has gone up. A safe answer could also simply restate the chain from electrification to smaller bands, but the math inference about more bands is the one the paragraph is built to test.','Goal','Goal'),
('e58b20ed-9724-4eb6-9e88-0a23a49369da'::uuid,'8f79c9d206e53da6051a26f1a1ec16c6','The study gives us a result: afternoon exercisers got 33 percent more deep sleep than the control group. Then the researcher explains why: afternoon exercise raises body temperature slightly until after bedtime, and "this extra heat induces deeper sleep."

That last clause is the key. The researcher does not say exercise itself deepens sleep. The researcher says the extra heat does. So the cause is the heat, and exercise is just one way to produce it. Anything else that leaves you slightly warmer at bedtime should have the same effect.','Evaluate','Evaluate'),
('9d4092fb-98d3-4c44-aa6a-00bd3cb999c9'::uuid,'33655bde1729410e38f7d937a0c94574','Look for an answer that applies the heat mechanism to some other source of warmth near bedtime, worded modestly ("likely", "tends to"). Expect the wrong answers to overreach with words like "required", "the best way", or "no one".','Goal','Goal'),
('febec16a-0f3f-4bf7-8753-0efc9f41822d'::uuid,'22bea25ccf7ebf635dd0249e914f7ba0','The Sapir-Whorf hypothesis: a society''s world view is influenced by the language its members speak.

Pivot (but): the hypothesis lacks the verifiability of hypotheses in physical science.

Reason (since): it is not clear that the hypothesis could be tested.','Given','Statements'),
('863d68ce-2bf8-4261-a390-0d946de21044'::uuid,'4de6152130e7fd297486f97cc5f549f2','1. Articles criticizing the environmental movement now appear regularly in newspapers.

2. Winslow''s explanation: this is due less to antienvironmental bias in the media than to editors preferring articles that seem "daring," because they seem to challenge prevailing political positions.

3. The commentator agrees: "It is true that editors like to run antienvironmental pieces mainly because they seem to challenge the political orthodoxy."

4. Pivot (but): serious environmentalism is not politically orthodox, so antienvironmentalists are not really dissidents, even if they have succeeded in selling themselves as renegades.','Given','Statements'),
('f8806d83-8d1b-400b-bd14-682593ffa525'::uuid,'04e515feac1d0d275bebe137188777fd','1. Boat engine noise runs from 100 to 3,000 hertz, a range that overlaps the range killer whales use to communicate.

2. Pivot (though): the whales do not seem to behave differently around running engines, but engine noise can be loud enough to damage their hearing over time.

3. Therefore, _______ .','Given','Statements'),
('16bc259f-9356-424d-b0bb-99672b30c4e0'::uuid,'3648e8ab5f36c681f7da2e600f77103e','All of this is about early times, before irrigation became feasible away from water.

Early urban societies could not have been maintained without large-scale farming nearby.
Early urban society → large-scale farming nearby

This is because other methods of food acquisition, such as foraging, cannot support populations as dense as urban ones.

Large-scale farming requires irrigation, which remained unfeasible in areas far from rivers or lakes until more recent times.
Large-scale farming → irrigation
Early times and far from rivers or lakes → no irrigation','Given','Statements'),
('6bebcdb5-73b8-4213-a5d4-ace8df4b040b'::uuid,'defac56876d7f7c40eea3d8131101cdd','Any good garden compost may appropriately be used for soil drainage and fertility.
Good compost → appropriate for drainage and fertility

The best compost is 40 to 60 percent organic matter and is dark brown in color.
Best compost → 40 to 60 percent organic and dark brown

However, compost that emits a strong ammonia smell should not be used for drainage and fertility, for that smell means that the organic matter has not sufficiently decomposed.
Strong ammonia smell → not appropriate for drainage and fertility
Strong ammonia smell → not sufficiently decomposed','Given','Statements')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;