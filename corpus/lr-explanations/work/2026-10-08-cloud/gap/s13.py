from prop import *
IT='Inline diagrams flattened (PT118-S1-Q21, PT118-S4-Q22, PT113-S4-Q20, PT139-S4-Q21, PT112-S1-Q26)'
T='transcription'
W='The diagram lost its column layout in transcription, so the two sides of the arrow were interleaved word by word; the rebuild puts the chain on its own line with each side intact and no wording changed.'
# PT118-S1-Q21
q='PT118-S1-Q21'; ev='Choice A: "If there were a consistent causal link between major meteor impacts and mass extinctions, then all major meteor impacts would be followed by mass extinctions."'
P(IT,q,'2e5ba491-d8ed-4bdc-881d-5b550ea8203a',[("**If** major meteor impacts **Then** there is no and mass extinctions → consistent causal occur many times w/o link between them the other occurring",
 "**If** major meteor impacts and mass extinctions occur many times w/o the other occurring → **Then** there is no consistent causal link between them")],T,W,
 'Conclusion: "there is no consistent causal link between major meteor impacts and mass extinctions"')
P(IT,q,'335ada11-9554-47e6-a49b-59d7d7cbaf9e',[("**If** some major meteor **Then** there is impacts are NOT → NOT a consistent followed by mass causal link between extinctions MMI's and ME's",
 "**If** some major meteor impacts are NOT followed by mass extinctions → **Then** there is NOT a consistent causal link between MMI's and ME's")],T,W,ev)
P(IT,q,'6b7a59bd-fa15-4bd6-92d4-75dc7b423556',[("It is **not** the case that Major meteor impacts many mass extinctions → and mass extinctions have followed major cannot be consistently meteor impacts causally linked",
 "It is **not** the case that many mass extinctions have followed major meteor impacts → Major meteor impacts and mass extinctions cannot be consistently causally linked")],T,W,
 'Choice B: "Major meteor impacts and mass extinctions cannot be consistently causally linked unless many mass extinctions have followed major meteor impacts."')
P('Overbroad rule found while fixing PT118-S1-Q21',q,'6857ddd2-293a-4a42-a39d-408eae7bb8bc',[('"If Conclusion is true" is always wrong on LSAT.','"If Conclusion is true" is always wrong on Sufficient Assumption.')],'register',
 'Narrows a rule stated for the whole LSAT to the question type where it holds.','Choice D: "If there is no consistent causal link ... then not all mass extinctions could have followed major meteor impacts."')
# PT118-S4-Q22
q='PT118-S4-Q22'
P(IT,q,'ecdc5a9e-62ad-4160-8ecb-4eba9c9ae314',[
 ("positive restatements: No A's are B = All A's are ~B Few A's are B = Most A's are ~B Not all A's are B = Some A's are ~B",
  "positive restatements:\n  No A's are B = All A's are ~B\n  Few A's are B = Most A's are ~B\n  Not all A's are B = Some A's are ~B"),
 ("So that conditional looks like preexisting recording → record companies transferred to CD think will be profitable",
  "So that conditional looks like\n  preexisting recording transferred to CD → record companies think will be profitable"),
 ("Since the conclusion is trying to create this path Most classic --------------> not jazz recordings transferred\nand we currently have these two pieces: Most classic → not played jazz recordings on radio\nRC's don't → not think will be transferred profitable",
  "Since the conclusion is trying to create this path\n  Most classic jazz recordings --------------> not transferred\nand we currently have these two pieces:\n  Most classic jazz recordings → not played on radio\n  RC's don't think will be profitable → not transferred")],T,
 W+' The three quantifier translations are also put on separate lines.','Stimulus: "The only preexisting recordings that are transferred onto compact disc are those that record companies believe will sell well enough on compact disc to be profitable."')
P(IT,q,'5052a476-2be4-4a81-9f3b-d5ffc3303d17',[("Most classic → **not played** jazz recordings **on radio →**",
 "Most classic jazz recordings → not played on radio → **RC's don't think will be profitable** → not transferred")],T,
 'The chain was interleaved and cut off after "on radio →"; the rebuild completes it with the link the Goal sentence just named, bolding the missing piece.',
 'Goal: "We need to get from \\"not played on radio\\" to \\"record companies don\'t believe it will sell enough on CD to be profitable\\"."')
P(IT,q,'62fccf3d-b0f1-42d2-b96e-8f1c2b53b1bd',[
 ("All [recordings not are [ **not** ones record companies believe played on radio] will be profitable]",
  "All [recordings not played on radio] are [ **not** ones record companies believe will be profitable]"),
 ("not played → not a recording record on radio companies believe will be profitable if transferred",
  "not played on radio → not a recording record companies believe will be profitable if transferred")],T,W,
 'Choice E: "No recording that is not played on the radio is one that record companies believe would be profitable if transferred to compact disc."')
# PT113-S4-Q20
q='PT113-S4-Q20'
P(IT,q,'70c39486-0b55-482b-a55d-607871b254ff',[("proving that someone doesn't deserve aid:","proving that someone doesn't deserve praise:"),
 ("action is not motivated → don't deserve by a desire to help others praise for it","action is not motivated by a desire to help others → don't deserve praise for it")],T,
 W+' Also "deserve aid" is corrected to "deserve praise", which is what the rule proves.','Stimulus: "people merit praise only for those actions motivated by a desire to help others"')
P(IT,q,'b52fe6c1-907d-4e2b-9369-6ca1b65f6bc8',[("aiding primarily out → not motivated by of a desire for praise desire to help others",
 "aiding primarily out of a desire for praise → not motivated by desire to help others")],T,W,
 'Conclusion: "one who aids others primarily out of a desire for praise does not deserve praise for that aid"')
P(IT,q,'1986cc6b-d325-4d7b-9a7f-0d8b6b32bac6',[
 ("motivated by desire for → not motivated by favorable opinion of others desire to help others","motivated by desire for favorable opinion of others → not motivated by desire to help others"),
 ("CONCLUSION aiding others don't primarily out of ----------------------------> deserve desire 4 praise praise\n\nEVIDENCE not motiv don't by desire to ---> deserve help others praise THIS ANSWER aiding others by not motiv desire for [praise] -------> by desire to help others",
  "```\nCONCLUSION\naiding others primarily out of desire 4 praise ---------> don't deserve praise\n\nEVIDENCE\nnot motiv by desire to help others ---> don't deserve praise\n\nTHIS ANSWER\naiding others by desire for [praise] ---> not motiv by desire to help others\n```")],T,W,
 'Choice A: "An action that is motivated by a desire for the favorable opinion of others cannot also be motivated by a desire to help others."')
P(IT,q,'d94b6013-4c0e-464a-b991-2e8b3219fd3b',[("not motivated by don't desire to help others → deserve (i.e. indifferent to the praise welfare of others)",
 "not motivated by desire to help others (i.e. indifferent to the welfare of others) → don't deserve praise")],T,W,
 'Choice C: "People who are indifferent to the welfare of others do not deserve praise."')
P(IT,q,'e11848c9-4a50-4292-a629-b70547fd3c9b',[("not motivated by desire → don't deserve to help others praise","not motivated by desire to help others → don't deserve praise")],T,W,
 'Stimulus: "people merit praise only for those actions motivated by a desire to help others"')
P('Typo found while fixing PT113-S4-Q20',q,'5c0786ba-c291-4ba0-aa77-3b6eee427a45',[("One who aids other primarily","One who aids others primarily")],'slip','"aids other" is a typo for "aids others".','Stimulus: "one who aids others primarily out of a desire for praise"')
# PT139-S4-Q21
q='PT139-S4-Q21'
P(IT,q,'564c60a0-e4ef-4caf-b4c4-33c560e82d32',[("The book is as important and as well → Skiff will be promoted written as Skiff claims",
 "The book is as important and as well written as Skiff claims → Skiff will be promoted")],T,W,'Stimulus: "if Skiff\'s book is as important and as well written as Skiff claims, he will be promoted"')
P(IT,q,'e564841b-5274-4776-841d-cc96c23c78f7',[],T,
 'The two conditionals were run together on one line; each now sits on its own line, and "recommends S\'s book" is corrected to what Nguyen actually recommends, Skiff\'s promotion.',
 'Stimulus: "If Skiff\'s book is published this year, Professor Nguyen vows she will urge the dean to promote Skiff ... the dean will surely promote Skiff if Nguyen recommends it."',
 new="Skiff's book is published → Nguyen recommends promoting Skiff\nN recommends promoting Skiff → dean will promote Skiff")
P(IT,q,'66105f8e-657e-4174-91ba-02d59e5370f0',[
 ("We can chain together the two conditionals: Skiff's book is → Nguyen will → Dean will published recommend promote Skiff to dean Since our goal",
  "We can chain together the two conditionals:\n  Skiff's book is published → Nguyen will recommend to dean → Dean will promote Skiff\nSince our goal"),
 ("logic conveyor belt ride to \"the book getting promoted\". Do we have","logic conveyor belt ride to \"Skiff getting promoted\".\nDo we have"),
 ("in our correct answer. The conclusion is teasing","in our correct answer.\nThe conclusion is teasing")],T,
 W+' Also "the book getting promoted" is corrected to Skiff, who is the one promoted.','Stimulus: "the dean will surely promote Skiff if Nguyen recommends it"')
P(IT,q,'1f5892dd-6878-4476-815f-4e5135a985cf',[("If it's as important → the book will be published\nas he claims\n","If it's as important as he claims → the book will be published\n")],T,W,
 'Choice A: "Skiff\'s book will be published this year if it is as important as he claims it is."')
P(IT,q,'93f319a6-a47e-4afe-9b27-8f3718ffb83b',[
 ("if as imp and well-written → book will be\nas Skiff claimed published","if as imp and well-written as Skiff claimed → book will be published"),
 ("if not as important book will not\nand well-written → be published\nas Skiff claimed","if not as important and well-written as Skiff claimed → book will not be published")],T,W,
 'Choice D: "Skiff\'s book will not be published unless it is as important and as well written as he claims it is."')
# PT112-S1-Q26
q='PT112-S1-Q26'
P(IT,q,'fbe8ae4c-6587-417a-a01f-8e233bbc094e',[
 ("We're pre-phrasing a verbatim idea that connects the pieces we have. Existing evidence: many of the props were expensive Conclusion we're trying to prove: V didn't re-use props because he just didn't have other props he could use. How we get from evidence to conclusion: many props were → recurrent use wasn't expensive from lack of props",
  "We're pre-phrasing a verbatim idea that connects the pieces we have.\nExisting evidence: many of the props were expensive\nConclusion we're trying to prove: V didn't re-use props because he just didn't have other props he could use.\nHow we get from evidence to conclusion:\n  many props were expensive → recurrent use wasn't from lack of props")],T,W,
 'Stimulus: "Yet we know that many of the props Vermeer used were expensive. Thus ... it was clearly not for lack of props that the recurrent items were used."')
P(IT,q,'507d31fe-e7d4-44ea-9e53-584c758b8330',[
 ("if we contrapose this answer it says: if we find expensive a dearth of props props in any → did **not** account for of V's paintings the recurrent objects We **do** find",
  "if we contrapose this answer it says:\n\nif we find expensive props in any of V's paintings → a dearth of props did **not** account for the recurrent objects\n\nWe **do** find")],T,W,
 'Choice E: "If a dearth of props accounted for the recurrent objects in Vermeer\'s paintings, we would not see expensive props in any of them."')
P('Typo found while fixing PT112-S1-Q26',q,'5b724ffb-2368-499a-9eb3-24d811cb8098',[("special sentimental important for him","special sentimental importance for him")],'slip','"important" is a typo for "importance".','Choice D: "had special sentimental importance for him"')
