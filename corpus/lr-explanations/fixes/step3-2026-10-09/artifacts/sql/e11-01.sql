update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('305069f9-4d24-4a4c-a055-1c1eeed9cd2c'::uuid,'bd78d02311013561221bbea47f3af46f','```
opposable thumbs → primate
primate indigenous to Madagascar → lemur
lemur → lower primate
living diurnal lower primate → lemur (certain species)
higher primate → thought to have evolved from one diurnal lower-primate species
```','Information','Information'),
('82c5e9d7-930d-43d7-8f41-8564cd2d04a3'::uuid,'bd3166ab64889bfd9b7b2454c137ec5a','On a Must Be True question, we look for a concept that shows up more than once and try to link through it. Here the bridge is "lemur." The only primates native to Madagascar are lemurs, and lemurs are lower primates. Put those together: every primate native to Madagascar is a lower primate.

Now ask what that rules out. Lower primates and higher primates are two separate groups, so a lower primate is not a higher primate. That means no primate native to Madagascar is a higher primate. Not a diurnal one, not a nocturnal one, not any kind.

The last sentence is the tempting one, because it looks like it chains with the lemur sentence. Higher primates are thought to have evolved from one diurnal lower-primate species, and certain lemurs are the only living diurnal lower primates. Does that make the ancestor a lemur? No. The lemur claim covers only living lower primates, and the ancestor could be a species that no longer exists. On top of that, "are thought to have evolved" only reports what people believe. Nothing about ancestry is proven here.','Evaluate','Evaluate'),
('ce66f17f-5b51-4866-8b4a-fcdbf9284a50'::uuid,'541da1ac93eca1ca782f59532dbcc224','Predict the Madagascar chain: no primate native to Madagascar is a higher primate.

Expect the answer to dress that up. If an answer adds a detail that only narrows the group of higher primates (say, diurnal ones), it is still proven: if no higher primate is native to Madagascar, no smaller slice of higher primates is either. Be suspicious of any answer that treats the ancestral species and the lemurs as the same thing.','Goal','Goal'),
('23d5102b-96fc-41ac-8764-fe1960b791f9'::uuid,'355bfcda86ac4c3ab1178389435a3511','Rational Choice Theory: The reason various political parties are popular is that individual voters make a deliberate decision to support the party they think has policies that will yield them the greatest economic advantage. Many Sociologists: This theory is wrong. A complex phenomenon such as the rise of a political organization cannot be caused by a simple phenomenon.','Statements','Statements'),
('bc3a398f-5239-4954-85b8-150de15bb487'::uuid,'ff0c24f92cdbc2a82e8786f81369feb7','Match up the parts of the sociologists'' response. The theory says that X (popular support for political parties) is explained by Y (individual voters deliberately backing the party whose policies they think will give them the greatest economic advantage). The sociologists object that a complex phenomenon cannot be caused by a simple phenomenon.

That objection only lands if Y is a simple phenomenon. If voters'' economic decisions were themselves complex, the sociologists'' rule would not touch the theory. So the sociologists apparently assume that Y is simple.','Evaluate','Evaluate'),
('47832198-bd32-4ead-ae25-2ab4f3e8e78b'::uuid,'3cac3607eb855e85ea3599bb155829aa','Look for an answer saying the sociologists treat voters'' economically driven decisions as a simple phenomenon, or at least as something that isn''t automatically complex.

The stem asks what the sociologists believe, so we can only credit them with what their objection commits them to. A modestly worded answer ("need not," "can be") is easier to prove than a sweeping one.','Goal','Goal'),
('9257949a-230b-4b41-a4c4-abd07679c010'::uuid,'c9a998b9e12adcb03ecffd9cb25966bb','The citizen predicts a chain: a major tax cut for upper-income citizens, then a correspondingly large increase in investment, then new jobs. The conclusion that we urgently need the cut depends on that first step actually happening.

How could we argue the plan fails? Suppose upper-income citizens get the money and have no way to put it toward investment. Then the cut produces no investment, no new jobs, and no reason to call it urgent.

So the citizen needs, at a minimum, that the tax-cut money can go toward investment. It''s a small requirement, but the whole plan rests on it.','Evaluate','Evaluate'),
('2ba7efc6-5622-4ad3-8663-b4ca174d2aea'::uuid,'ecb824d3b71df012431583a3964da8a9','Expect a defender: an answer that rules out the objection "the tax-cut money can''t end up as investment." It may be worded weakly, with "could" or "can." On Necessary Assumption, weak wording is a good sign, because the argument only needs the possibility to exist. Negate each choice and see whether the investment step breaks.','Goal','Goal'),
('f1ab5847-6ef7-4571-97c9-15d2dac5a986'::uuid,'9be7417684d2b25aab48dc45a98b0b74','The scientist argues by analogy. Selective breeding is a crude form of genetic engineering, and people have done it for millennia, so genetic engineering is not unethical.

What has to be true about selective breeding for that to work? It has to be acceptable. If selective breeding were itself unethical, showing that genetic engineering resembles it would only put genetic engineering in bad company. The millennia of practice don''t settle that question either. A practice can be very old and still wrong.

There''s a second gap: is choosing which animals breed really the same kind of thing as directly manipulating genetic codes? The scientist treats them as one category, and a critic could dispute that. But the first gap is the one the argument can''t do without. The scientist never says selective breeding is ethical.','Evaluate','Evaluate'),
('e81c2c4a-d249-4334-b88c-446aad548525'::uuid,'3eb152713dcbfce68a168c3bc9da2de0','The answer will most likely protect the base of the analogy: selective breeding itself is not unethical. It could also defend the comparison, saying breeding and genetic-code manipulation are relevantly alike. Negate each choice and ask whether the scientist''s evidence still clears genetic engineering.','Goal','Goal'),
('7b91f97d-2de9-4390-ab49-d7c537e4a795'::uuid,'089fe55cad76fef3e04cb2314b3b1417','The evidence gives a trade-off. Presoaking saves time. Skipping it gives plumper beans. The conclusion says that when quality matters more than speed, skip the soak.

Notice the jump. The evidence talks about plumper beans. The conclusion talks about the dish''s quality. Those aren''t the same idea. How could we argue against the author? Suppose plumper beans don''t make a dish any better. Then the only real difference between the two methods is cooking time, and there''s no quality reason to skip the soak.

So the author has to assume that plumper beans make for a better dish.','Evaluate','Evaluate')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;