update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('b297870f-c027-4cf8-9986-89f93ab41452'::uuid,'f75b2a78ab1e07e8cc15ff4a9fefcd1b','The fix for the definition problem is to define medieval epistemology as "the epistemological beliefs of the medieval epistemologists." The historian claims this definition will finally tell us what does and does not belong in medieval epistemology.','Conclusion','Conclusion'),
('99121926-d49a-415e-a029-61f6329177ef'::uuid,'c40c3da66fcd9ab270095c4d082bde2e','Historians have failed to produce a definition that settles what belongs in medieval epistemology.

With the new definition, the test for any epistemological claim is simple: did any medieval epistemologist believe it? If one did, the claim is in. If one believed the opposite, the opposite claim is in too.','Evidence','Evidence'),
('92039a68-223d-42f3-9bd9-b5a531bf5340'::uuid,'b8fd0f832774cb291edef382e9b6527a','The test has one input: a list of the medieval epistemologists. Everything depends on having that list. How would we know who belongs on it? Presumably they are the thinkers who did medieval epistemology. But that is the very thing we are trying to define.

So given that the definition sounds tidy, how could we argue it still fails to settle what is included? Show that we cannot agree on who the medieval epistemologists were. Then the test has nothing to run on.

Notice what is NOT a problem for the historian: disagreement. The historian already says that if one epistemologist believed X and another believed the opposite, both claims count. Contradictions among the epistemologists were built into the plan.','Evaluate','Evaluate'),
('7d3ea25e-dd71-4ada-937c-ae04e2252a50'::uuid,'6989e6cd9e24ea1fb8402f28a2d73a12','Look for an answer that makes it hard to identify who the medieval epistemologists were. If we can''t pick them out, the definition can''t tell us what is included.

Watch out for answers about epistemologists contradicting each other. The historian built that into the plan, so it doesn''t weaken it.','Goal','Goal'),
('d1c38a19-c55c-4bbc-99be-1c6bb16adb74'::uuid,'73bc0ca4f66db6db2dd7ea9ccdfe67d3','The consumer advocate''s worry is a chain of links:

drug crop → pollen drifts into a nearby field of the same species
pollen fertilizes the ordinary crop → ordinary crop becomes drug-producing
drug-producing crop is harvested for food → drug ends up in the food supply

The stimulus describes how the first two links could happen. The last link is simply assumed. A plant that produces a drug somewhere in its tissue is not the same as a drug in the food we take from that plant.

Given that the pollen could convert a neighboring crop, how could we argue the drug still won''t reach the food supply? Show that the converted crop''s food part wouldn''t carry the drug.

Also notice how mild the conclusion is: it only says the development "raises the possibility" of drugs in the food supply. To weaken it, an answer has to cut a link in the chain. Making the outcome less harmful, less widespread, or easier to deal with afterward leaves the possibility standing.','Evaluate','Evaluate'),
('28c5b825-0584-4296-ba19-94bc4225d797'::uuid,'7666df51fff25e6864f078fbf63a1115','Look for an answer that breaks a link in the chain, most likely the last one: even if an ordinary crop turns into a drug-producing crop, the drug never gets into the food.

Skip answers about how dangerous the drugs are, how much of the food supply is involved, or what we could do after contamination. None of those touch whether the drugs could get in.','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;