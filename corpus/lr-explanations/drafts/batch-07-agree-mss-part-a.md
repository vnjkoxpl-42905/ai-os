---
type: draft
subject: LR batch 07, part A, 24 slots (every remaining Agree/Disagree gap)
status: loaded 2026-10-02
created: 2026-10-02
---

# Batch 07, part A: the last Agree/Disagree gaps

Source: the bank on current main (worktree `../ai-os-projects/lsatu-wt-bankfix-b02`) and the post-batch-06 database pull. Sixteen are in the database with no explanation. PT116-S3-Q6 and PT142-S2-Q7 already have five notes and need steps only. Six are not in the database; loading them inserts the question and choices from the bank.

Two of the unloaded six are filed as Agree/Disagree but are not: PT156-S2-Q7 asks how Ms. Yerky's response proceeds (Method), and PT156-S2-Q21 asks why the philosopher's reasoning is flawed (Flaw). They are typed and explained as what they are.

Modelled on `models/MC-Role-Agree.md`:
- Go through the first speaker's claims one at a time and ask whether the second speaker takes the opposite side.
- Test every choice for both positions. Name the side that is missing, in that speaker's words.
- Separate "is" from "should", "can" from "will", and a concession from a disagreement.

Labels: [Speaker]'s Position / [Speaker]'s Position / Evaluate / Goal (Method and Flaw: Conclusion / Evidence / Evaluate / Goal). Tags: Correct, Half Scope, Both Agree, Out of Scope, Too Strong; Method and Flaw use their own vocabulary.

## PT113-S4-Q7 | Agree/Disagree | C

> Hazel: Faster and more accurate order processing would help our business. To increase profits, we should process orders electronically rather than manually, because customers' orders will then go directly to all relevant parties. Max: We would lose money if we started processing orders electronically. Most people prefer to interact with human beings when placing orders. If we switch to electronic order processing, our business will appear cold and inhuman, and we will attract fewer customers.
>
> Hazel and Max disagree over whether
>
> (A) electronic order processing is faster and more accurate than is manual order processing
> (B) faster and more accurate order processing would be financially beneficial to their business
> (C) switching to electronic order processing would be financially beneficial to their business
> (D) their business has an obligation to be as profitable as possible
> (E) electronic order processing would appear cold and inhuman to most of their customers

### Argument Breakdown

**Hazel's Position:** Switching to electronic order processing would make orders faster and more accurate, so it would increase profits.

**Max's Position:** Switching would lose money, because customers want a human and would go elsewhere.

**Evaluate:** Max never disputes that electronic processing is faster or more accurate. Max goes straight at the bottom line: Hazel says profits go up, Max says "we would lose money". That is a clean, head-on clash.

**Goal:** Whether switching to electronic processing would help the business financially.

### Choice Notes

**(A) Half Scope.** Hazel thinks electronic processing is faster and more accurate. Max never says it isn't. Max's objection is about how customers feel, not about speed.

**(B) Half Scope.** This is the most popular wrong answer, and it is close. Hazel says faster, more accurate processing would help. But Max never talks about speed or accuracy at all. Max talks about what *electronic* processing would do. B swaps the switch for its benefits, and Max has no stated view on the benefits.

**(C) Correct.** Hazel: switching will "increase profits". Max: "We would lose money if we started processing orders electronically." Both sides are stated outright.

**(D) Out of Scope.** Neither speaker talks about an obligation to be as profitable as possible. They both want profit; the fight is over how to get it.

**(E) Half Scope.** Max thinks customers would find the business cold and inhuman. Hazel never addresses how customers would feel.

## PT115-S4-Q2 | Agree/Disagree | A

> Tom: Critics of recent high court decisions claim that judges' willingness to abide by earlier decisions is necessary to avoid legal chaos. Since high courts of the past often repudiated legal precedents and no harm to the legal system ensued, these critics' objections must be politically motivated and ought to be ignored. Mary: High courts have repudiated precedents in the past, but they were careful to do so only when the previous rulings were old and had clearly become outdated. The recently overturned rulings were themselves recent. Overturning any recent legal ruling diminishes the law, which comes to be viewed as unstable and capricious.
>
> Which one of the following most accurately expresses the point at issue between Tom and Mary?
>
> (A) whether the overturning of recent high court precedents will harm the legal system
> (B) whether the overturning of recent high court precedents was politically motivated
> (C) whether critics of recent high court decisions in fact advanced the claim Tom cites
> (D) whether a precedent that is clearly outdated is in need of being overturned
> (E) whether judicial decisions that seem progressive at first can quickly become outdated

### Argument Breakdown

**Tom's Position:** Past high courts often repudiated precedents and no harm followed. So the critics' worry about legal chaos is politically motivated and should be ignored. In short: the recent reversals won't hurt the legal system.

**Mary's Position:** Past courts only overturned old, outdated rulings. These rulings were recent, and overturning any recent ruling diminishes the law, making it look unstable and capricious.

**Evaluate:** Mary grants Tom's fact (courts have repudiated precedents before) and then attacks Tom's analogy: the past cases were old rulings, these are recent ones. So the real question is whether *these* reversals will do damage. Tom says no harm, as in the past. Mary says it diminishes the law.

**Goal:** Whether overturning recent precedents will harm the legal system.

### Choice Notes

**(A) Correct.** Tom uses the past to argue that no harm will follow and the chaos worry can be ignored. Mary says overturning a recent ruling "diminishes the law". That is harm versus no harm.

**(B) Half Scope.** This is the most popular wrong answer. Read Tom closely: Tom says the *critics' objections* are politically motivated, not the court's decisions. And Mary says nothing about anyone's motives. Neither side is supported.

**(C) Half Scope.** Mary never questions whether the critics actually made the claim Tom cites. Mary argues about the claim, not about who said it.

**(D) Half Scope.** Mary implies outdated precedents may be overturned, but whether they *need* to be is a stronger claim. Tom says nothing about outdated precedents.

**(E) Out of Scope.** Neither speaker talks about decisions that "seem progressive" or how fast they go out of date.

## PT116-S2-Q1 | Agree/Disagree | C

> Pettengill: Bebop jazz musicians showed their distaste for jazz classics by taking great liberties with them, as though the songs could be made interesting only through radical reshaping. Romney: Only compelling, versatile songs can stand such radical reshaping. Bebop musicians recognized this, and their revolutionary approach to the jazz classics enabled them to discover previously unknown depths in the music.
>
> Pettengill and Romney disagree over whether
>
> (A) bebop jazz was radically different from the jazz music that preceded it
> (B) bebop jazz was an improvement on the jazz classics that preceded it
> (C) bebop musicians showed appreciation for jazz classics in radically reshaping them
> (D) jazz music requires musicians to adhere closely to the original version in order to be widely popular
> (E) bebop musicians were influenced by the more conservative styles of their predecessors

### Argument Breakdown

**Pettengill's Position:** By taking great liberties with the jazz classics, bebop musicians showed distaste for them.

**Romney's Position:** Only strong songs can survive that kind of reshaping. Bebop musicians knew this, so the reshaping shows they valued the classics and found new depth in them.

**Evaluate:** Both agree on the fact: bebop radically reshaped the classics. They disagree about what the reshaping *meant*. Pettengill reads it as contempt. Romney reads it as respect.

**Goal:** Whether reshaping the classics showed appreciation or distaste.

### Choice Notes

**(A) Both Agree.** Pettengill describes "radical reshaping" and Romney repeats the phrase. Neither denies bebop was radically different.

**(B) Half Scope.** This is the most popular wrong answer. Romney says bebop found new depths in the classics, which is not the same as saying bebop was *better* than them. Pettengill never ranks the two either.

**(C) Correct.** Pettengill: the reshaping showed "distaste". Romney: it came from recognizing the songs were compelling enough to stand it. Appreciation versus distaste.

**(D) Out of Scope.** Nobody talks about what jazz needs in order to be "widely popular".

**(E) Out of Scope.** Neither speaker says bebop was influenced by more conservative styles.

## PT116-S3-Q6 | Agree/Disagree | E

**Steps only.** The five existing notes stay as they are.

> Antonia: The stock market is the best place to invest your money these days; although it is often volatile, it provides the opportunity to make a large profit quickly. Maria: I agree that the stock market provides the opportunity to make large profits quickly, but one is just as likely to take a huge loss. I think it is better to invest in savings bonds, which provide a constant, reliable income over many years.
>
> Antonia's and Maria's statements provide the most support for holding that they disagree about whether
>
> (A) the stock market is often volatile but provides the opportunity to make a large profit quickly
> (B) savings bonds can provide a large return on one's investment
> (C) the stock market provides the opportunity for an investor to make a constant, reliable income over many years
> (D) it is safer to invest in savings bonds than to invest in the stock market
> (E) it is preferable to pick an investment offering a reliable income over a riskier opportunity to make a large profit quickly

### Argument Breakdown

**Antonia's Position:** The stock market is the best place to invest. It is volatile, but it gives you a shot at a large, quick profit.

**Maria's Position:** Yes, you can make a large profit quickly, but you are just as likely to take a huge loss. Savings bonds are better, because they pay a constant, reliable income.

**Evaluate:** Look at what Maria concedes. Maria agrees about the quick profits, and Antonia already admitted the volatility. So the facts are shared. What they disagree about is the tradeoff: Antonia picks the big upside despite the risk; Maria picks the steady income. Antonia never mentions "reliable income" by name, but calling the volatile market the *best* place to invest puts Antonia on the other side of that choice.

**Goal:** Whether a reliable income is better than a risky chance at a fast, large profit.

## PT117-S2-Q6 | Agree/Disagree | B

> Chai: The use of the word “tree” to denote both deciduous and coniferous plant forms, while acceptable as a lay term, is scientifically inadequate; it masks the fact that the two plant types have utterly different lineages. Dodd: But the common name highlights the crucial fact that both are composed of the same material and have very similar structures; so it is acceptable as a scientific term.
>
> The conversation provides the strongest grounds for holding that Chai and Dodd disagree over whether
>
> (A) it is advisable to use ordinary terms as names for biological forms in scientific discourse
> (B) using the same term for two biological forms with different lineages can be scientifically acceptable
> (C) both deciduous and coniferous plant forms evolved from simpler biological forms
> (D) it is important that the lay terms for plant forms reflect the current scientific theories about them
> (E) biological forms with similar structures can have different lineages

### Argument Breakdown

**Chai's Position:** Using "tree" for both deciduous and coniferous plants is fine in everyday speech, but scientifically inadequate, because it hides that the two have completely different lineages.

**Dodd's Position:** The shared name highlights that both are made of the same material with very similar structures, so it is acceptable as a scientific term.

**Evaluate:** Dodd does not deny the different lineages. Dodd just thinks something else matters more for a scientific name. So the clash is narrow: can one term for two forms with different lineages be scientifically acceptable? Chai says no, Dodd says yes.

**Goal:** Whether one scientific term can acceptably cover two forms with different lineages.

### Choice Notes

**(A) Too Strong.** Both speakers talk only about the word "tree". Neither makes a general claim that ordinary terms are advisable, or inadvisable, as scientific names. Dodd only says this one is acceptable, and acceptable is weaker than advisable.

**(B) Correct.** Chai calls "tree" scientifically inadequate because the lineages differ. Dodd calls it "acceptable as a scientific term" while accepting that they differ. That is yes versus no on B.

**(C) Out of Scope.** Neither speaker says anything about the plants evolving from simpler forms.

**(D) Out of Scope.** Chai says "tree" is acceptable as a lay term. Nobody says lay terms should reflect current theory.

**(E) Half Scope.** Chai believes this: the two plant types have similar structure but different lineages. Dodd never denies it. Dodd argues from the similar structure without disputing the lineages.

## PT118-S1-Q6 | Agree/Disagree | D

> Maria: Popular music is bad art because it greatly exaggerates the role love plays in everyday life and thereby fails to represent reality accurately. Theo: Popular music is not supposed to reflect reality; it performs other artistic functions, such as providing consoling fantasies and helping people create some romance in their often difficult lives. You should understand popular music before you condemn it.
>
> The dialogue provides the most support for the claim that Maria and Theo disagree over whether
>
> (A) most good art creates consoling illusions
> (B) some bad art exaggerates the role love plays in everyday life
> (C) art should always represent reality as it could be, not as it is
> (D) art need not represent reality accurately to be good art
> (E) popular music should not be considered to be an art form

### Argument Breakdown

**Maria's Position:** Popular music is bad art because it exaggerates love and so fails to represent reality accurately.

**Theo's Position:** Popular music isn't supposed to reflect reality. It does other artistic jobs, like consoling fantasy and romance.

**Evaluate:** Maria's argument only works if art has to represent reality accurately to be good. Theo attacks exactly that: popular music can do valuable artistic work without reflecting reality. So the clash is the standard Maria is using.

**Goal:** Whether art has to represent reality accurately to be good art.

### Choice Notes

**(A) Too Strong.** Theo says popular music provides consoling fantasies. Theo never says *most good art* does. Maria never talks about consoling illusions at all.

**(B) Half Scope.** Maria believes some bad art (popular music) exaggerates love. Theo never denies that popular music exaggerates love; Theo says it doesn't have to be realistic. So we can't put Theo on the other side.

**(C) Too Strong.** This is the most popular wrong answer. Theo's view is that popular music isn't supposed to reflect reality, not that all art should "always" show reality "as it could be". And Maria wants reality as it is, but says nothing about "as it could be". Neither position is supported.

**(D) Correct.** Maria calls popular music bad art *because* it fails to represent reality accurately. Theo says it isn't supposed to reflect reality and still performs artistic functions. So Maria says accuracy is needed for good art, and Theo says it isn't.

**(E) Both Agree.** Both treat popular music as art. Maria calls it "bad art" and Theo talks about its "artistic functions".

## PT118-S1-Q10 | Agree/Disagree | A

> Rachel: Though contemporary artists are pleased to be free of the constraints that bound their predecessors, this freedom has caused a decline in the quality of art. Great art can be produced only when artists struggle to express themselves within externally imposed boundaries. James: People have always been critical of the art of their own time. They forget all but the greatest art from past eras. Since inferior contemporary artworks have not yet been forgotten, people today mistakenly think that contemporary art is generally inferior to earlier art.
>
> On the basis of their statements, Rachel and James are committed to disagreeing with each other about whether
>
> (A) contemporary art is of lower quality than earlier art
> (B) contemporary artists are bound by the same constraints as their predecessors
> (C) great art is produced only when an artist struggles against limitations
> (D) inferior art from past eras is generally forgotten
> (E) one can correctly assess the quality of art only if it was produced in past eras

### Argument Breakdown

**Rachel's Position:** Freedom from old constraints has caused a decline in the quality of art. Great art needs outside boundaries to struggle against.

**James's Position:** People only think contemporary art is worse because they have forgotten the bad art of the past and haven't yet forgotten today's. They are mistaken.

**Evaluate:** Rachel says art has declined, which means contemporary art is worse than earlier art. James says the belief that contemporary art is generally inferior is a mistake. James never discusses Rachel's reason (constraints). James goes after Rachel's conclusion.

**Goal:** Whether contemporary art is actually worse than earlier art.

### Choice Notes

**(A) Correct.** Rachel: freedom "has caused a decline in the quality of art". James: people "mistakenly think that contemporary art is generally inferior to earlier art". Worse versus not worse.

**(B) Half Scope.** This is the most popular wrong answer. Rachel does say today's artists are free of their predecessors' constraints, so Rachel would deny B. But James says nothing about constraints, so we can't place James.

**(C) Half Scope.** Rachel says this almost word for word. James never talks about how great art gets made.

**(D) Half Scope.** James says this: people forget all but the greatest past art. Rachel never addresses it.

**(E) Out of Scope.** James explains why people misjudge contemporary art, but James never says quality can be judged *only* for past art. Rachel doesn't touch this either.

## PT119-S2-Q1 | Agree/Disagree | D

> Cox: The consumer council did not provide sufficient justification for its action when it required that Derma-35 be recalled from the market. Crockett: I disagree. Derma-35 in fact causes inflammation, but in citing only the side effect of blemishes as the justification for its decision, the council rightly acknowledged that blemishes are a legitimate health concern.
>
> Cox and Crockett disagree over whether
>
> (A) Derma-35 should remain on the market
> (B) blemishes are sometimes caused by inflammation
> (C) the council based its decision on the threat of inflammation or on the threat of blemishes
> (D) the council gave an adequate reason for its decision to recall Derma-35
> (E) inflammation is a serious health threat

### Argument Breakdown

**Cox's Position:** The council did not give sufficient justification for recalling Derma-35.

**Crockett's Position:** "I disagree." The council cited blemishes, and it was right that blemishes are a legitimate health concern. So the justification was adequate.

**Evaluate:** Crockett says "I disagree" right after Cox's only claim, so the disagreement is Cox's claim itself. Notice what Crockett does *not* do: Crockett mentions inflammation as a fact, but defends the council on blemishes alone.

**Goal:** Whether the council's stated reason was enough to justify the recall.

### Choice Notes

**(A) Half Scope.** Cox objects to the justification, not the recall itself. A decision can be right but poorly justified. So we don't know that Cox thinks the drug should stay on the market.

**(B) Out of Scope.** Neither speaker connects blemishes to inflammation.

**(C) Half Scope.** Crockett says the council cited only blemishes. Cox never says what the council based its decision on.

**(D) Correct.** Cox: not "sufficient justification". Crockett: the council "rightly" relied on a legitimate concern. Adequate versus not.

**(E) Half Scope.** Crockett says Derma-35 causes inflammation but never says how serious inflammation is. Cox says nothing about it.

## PT120-S1-Q4 | Agree/Disagree | B

> Aaron: A prominent judge, criticizing “famous lawyers who come before courts ill-prepared to argue their cases,” recently said, “This sort of cavalier attitude offends the court and can do nothing but harm to the client’s cause.” I find the judge’s remarks irresponsible. Belinda: I find it natural and an admirable display of candor. Letting people know of the damage their negligence causes is responsible behavior.
>
> The point at issue between Aaron and Belinda is whether
>
> (A) ill-prepared lawyers damage their clients’ causes
> (B) the judge’s criticism of lawyers is irresponsible
> (C) a lawyer’s being ill-prepared to argue a client’s case constitutes negligence
> (D) famous lawyers have a greater responsibility to be well prepared than do lawyers who are not famous
> (E) it is to be expected that ill-prepared lawyers would offend the court in which they appear

### Argument Breakdown

**Aaron's Position:** The judge's remarks were irresponsible.

**Belinda's Position:** The remarks were natural and admirable. Telling people about the damage their negligence causes is responsible behavior.

**Evaluate:** This is as direct as these get. Aaron calls the remarks irresponsible; Belinda calls them responsible. Aaron never says the judge was wrong about the facts, only that saying it was irresponsible. So stay with the one word they fight over.

**Goal:** Whether the judge's criticism was irresponsible.

### Choice Notes

**(A) Half Scope.** Belinda implies ill-prepared lawyers do damage. Aaron never disputes that; Aaron objects to the judge saying it.

**(B) Correct.** Aaron: "irresponsible". Belinda: "responsible behavior". Opposite sides, both stated.

**(C) Half Scope.** Belinda calls it negligence. Aaron says nothing about whether being ill-prepared is negligent.

**(D) Out of Scope.** Neither speaker compares famous lawyers with other lawyers.

**(E) Out of Scope.** The judge says ill-prepared lawyers offend the court. Neither Aaron nor Belinda takes a position on whether that is to be expected.

## PT120-S1-Q25 | Agree/Disagree | E

> Claude: Because of the relatively high number of middle-aged people in the workforce, there will be fewer opportunities for promotion into upper-management positions. Since this will decrease people’s incentive to work hard, economic productivity and the quality of life will diminish. Thelma: This glut of middle-aged workers will lead many people to form their own companies. They will work hard and thus increase economic productivity, improving the quality of life even if many of the companies ultimately fail.
>
> On the basis of their statements, Claude and Thelma are committed to agreeing about which one of the following?
>
> (A) The quality of life in a society affects that society’s economic productivity.
> (B) The failure of many companies will not necessarily have a negative effect on overall economic productivity.
> (C) How hard a company’s employees work is a function of what they think their chances for promotion are in that company.
> (D) The number of middle-aged people in the workforce will increase in the coming years.
> (E) Economic productivity will be affected by the number of middle-aged people in the workforce.

### Argument Breakdown

**Claude's Position:** So many middle-aged workers means fewer promotions, less incentive, and so lower productivity and quality of life.

**Thelma's Position:** The glut of middle-aged workers will push people to start companies. They will work hard and raise productivity and quality of life.

**Evaluate:** This one asks what they *agree* on. They predict opposite results, but they share a starting point: the large number of middle-aged workers will change productivity. Claude says down; Thelma says up. Either way, it has an effect.

**Goal:** That the number of middle-aged workers will affect economic productivity.

### Choice Notes

**(A) Half Scope.** Thelma says productivity improves quality of life, which runs the other way from A. Claude says both will fall but never says quality of life drives productivity. Neither commits to A.

**(B) Half Scope.** Thelma says productivity rises "even if many of the companies ultimately fail", so Thelma would accept B. Claude never talks about companies failing.

**(C) Half Scope.** Claude ties hard work to promotion chances. Thelma's workers work hard in companies they founded, so Thelma isn't committed to C, and may reject it.

**(D) Unsupported.** This is the most popular wrong answer. Both speakers describe a large number of middle-aged workers *now* ("relatively high number", "this glut"). Neither says the number will increase.

**(E) Correct.** Claude: the number of middle-aged workers will lower productivity. Thelma: it will raise productivity. Both say it will affect productivity.

## PT120-S3-Q5 | Agree/Disagree | D

> Azadeh: The recent increase in the amount of organically produced food indicates that consumers are taking a greater interest in the environment. Thus, there is new hope for a healthier planet. Ben: No, Azadeh, if you interviewed people who buy organic produce, you’d see that they’re actually as selfish as everyone else, since they’re motivated only by worries about their own health.
>
> Azadeh’s and Ben’s statements provide the most support for holding that they disagree about whether
>
> (A) it is likely that a healthy planet can be maintained if most people continue in their present eating habits
> (B) people can become healthier by increasing their consumption of organic foods
> (C) people ought to be more concerned about the environment than they currently are
> (D) the rise in organic food production shows people to have a greater concern for the environment than they had before
> (E) people can be persuaded to have a greater concern for the environment than they now have

### Argument Breakdown

**Azadeh's Position:** More organic food production shows that consumers care more about the environment.

**Ben's Position:** "No." Organic buyers are motivated only by worry about their own health.

**Evaluate:** Ben's "No" lands on Azadeh's first claim: that the organic increase shows environmental concern. Ben offers a different motive and never addresses the planet's future, or whether people ought to care.

**Goal:** Whether the rise in organic food shows more concern for the environment.

### Choice Notes

**(A) Out of Scope.** Neither speaker talks about present eating habits keeping the planet healthy.

**(B) Half Scope.** Ben implies buyers *think* organic food is healthier. Whether it actually makes people healthier, neither says, and Azadeh never mentions health at all.

**(C) Out of Scope.** Neither says how concerned people *ought* to be.

**(D) Correct.** Azadeh: the increase "indicates" greater environmental interest. Ben: the buyers care "only" about their own health.

**(E) Out of Scope.** Neither speaker talks about persuading anyone.

## PT120-S4-Q16 | Agree/Disagree | E

> Logan: Newspapers have always focused on ephemeral matters while ignoring important societal changes. For this and other reasons, old newspapers are useless to both amateur and professional historians. Mendez: But news stories, along with popular art, provide a wealth of information about what the people of an era thought and felt.
>
> On the basis of their statements, Logan and Mendez are committed to disagreeing over whether
>
> (A) newspapers accurately report the most important changes taking place in a society
> (B) the study of previous eras should include investigations of the conventions of newspaper reporting
> (C) popular art is an important source of information about what the people of previous eras thought and felt
> (D) newspapers ought to focus more on the types of stories they have glossed over in the past
> (E) newspaper reports from former eras are useful sources of material for understanding the past

### Argument Breakdown

**Logan's Position:** Newspapers focus on passing matters and ignore important changes, so old newspapers are useless to historians.

**Mendez's Position:** "But" news stories give a wealth of information about what people of an era thought and felt.

**Evaluate:** Mendez doesn't fight Logan's premise about what newspapers cover. Mendez goes after the conclusion: old news stories are useful, because they show what people thought and felt.

**Goal:** Whether old newspapers are useful for understanding the past.

### Choice Notes

**(A) Half Scope.** Logan says newspapers ignore important changes, so Logan would deny A. Mendez never disputes Logan on that, and changes the subject to thoughts and feelings.

**(B) Out of Scope.** Neither speaker talks about studying the conventions of news reporting.

**(C) Half Scope.** Mendez says popular art is a source. Logan never mentions popular art.

**(D) Out of Scope.** Neither says what newspapers ought to cover.

**(E) Correct.** Logan: old newspapers are "useless" to historians. Mendez: news stories provide "a wealth of information" about past eras.

## PT122-S2-Q1 | Agree/Disagree | D

> Ilana: Carver's stories are somber and pessimistic, which is a sure sign of inferior writing. I have never read a single story of his that ends happily. Gustav: Carver was one of the finest writers of the past 30 years. Granted, his stories are characterized by somberness and pessimism, but they are also wryly humorous, compassionate, and beautifully structured.
>
> On the basis of their statements, Ilana and Gustav are committed to disagreeing over whether
>
> (A) Carver's stories are truly compassionate
> (B) Carver's stories are pessimistic in their vision
> (C) stories that are characterized by somberness and pessimism can appropriately be called humorous
> (D) stories that are well written can be somber and pessimistic
> (E) there are some characteristics of a story that are decisive in determining its aesthetic value

### Argument Breakdown

**Ilana's Position:** Carver's stories are somber and pessimistic, and that is "a sure sign of inferior writing".

**Gustav's Position:** Carver was one of the finest writers in 30 years. Yes, his stories are somber and pessimistic, but they are also humorous, compassionate, and beautifully structured.

**Evaluate:** They agree on the facts: the stories are somber and pessimistic. The fight is over what that means. Ilana's "sure sign" is a conditional: somber means inferior. Gustav refutes it with a counterexample: Carver is somber *and* one of the finest writers.

**Goal:** Whether well-written stories can be somber and pessimistic.

### Choice Notes

**(A) Half Scope.** Gustav says the stories are compassionate. Ilana never talks about compassion.

**(B) Both Agree.** Ilana calls them pessimistic, and Gustav says "Granted".

**(C) Half Scope.** Gustav says Carver's somber stories are also wryly humorous. Ilana never discusses humor.

**(D) Correct.** Ilana: somber and pessimistic is a "sure sign of inferior writing", so good writing can't be somber. Gustav: Carver's somber stories are fine writing.

**(E) Half Scope.** Ilana treats somberness as decisive. Gustav weighs several features, but Gustav never says *no* feature can be decisive. We can't put Gustav on the other side.

## PT122-S2-Q10 | Agree/Disagree | E

> Megan: People pursue wealth beyond what their basic needs require only if they see it as a way of achieving high status or prestige. Channen: Not everybody thinks that way. After all, money is the universal medium of exchange. So, if you have enough of it, you can exchange it for whatever other material goods you may need or want even if you are indifferent to what others think of you.
>
> Megan and Channen disagree over whether
>
> (A) people ever pursue wealth beyond what is required for their basic needs
> (B) it is irrational to try to achieve high status or prestige in the eyes of one's society
> (C) the pursuit of monetary wealth is irrational only when it has no further purpose
> (D) it is rational to maximize one's ability to purchase whatever one wants only when the motive for doing so is something other than the desire for prestige
> (E) the motive for pursuing wealth beyond what one's basic needs require is ever anything other than the desire for prestige or high status

### Argument Breakdown

**Megan's Position:** People pursue wealth beyond their basic needs only if they see it as a route to status or prestige.

**Channen's Position:** "Not everybody thinks that way." Money buys whatever goods you want, even if you don't care what others think.

**Evaluate:** Megan's claim is a conditional: extra wealth requires a status motive. Channen refutes it by offering a different motive: buying goods you want. So they disagree about whether any other motive exists.

**Goal:** Whether status is the only motive for pursuing extra wealth.

### Choice Notes

**(A) Both Agree.** This is the most popular wrong answer. Both speakers take for granted that people do pursue extra wealth. They argue about *why*.

**(B) Out of Scope.** Neither speaker calls anything rational or irrational.

**(C) Out of Scope.** Again, rationality never comes up.

**(D) Out of Scope.** Same problem, with an extra twist about "maximizing" purchasing power. Neither speaker says anything like it.

**(E) Correct.** Megan: the motive is always status. Channen: some people want the money for goods, "even if you are indifferent to what others think of you".

## PT126-S4-Q8 | Agree/Disagree | A

> Larew: People in the lowest income quintile had a much higher percentage increase in average income over the last ten years than did those in the highest quintile. So their economic prosperity increased relative to the highest quintile's. Mendota: I disagree. The average income for the lowest quintile may have increased by a greater percentage, but the absolute amount of the increase in average income was surely greater for the highest quintile.
>
> Larew and Mendota disagree about whether
>
> (A) change in the economic prosperity of the lowest income quintile relative to the highest is accurately measured by comparing their percentage changes in average income
> (B) change in the economic prosperity of the lowest income quintile is more accurately measured in terms relative to the highest income quintile than in terms relative only to the lowest income quintile
> (C) changes in the average income of people in the lowest quintile should ever be compared to changes in the average income of people in the highest quintile
> (D) there were any improvements at all in the economic situation of those in the lowest income quintile during the ten years being considered
> (E) the average income of people in the lowest quintile increased by a greater percentage over the last decade than did that of people in the highest quintile

### Argument Breakdown

**Larew's Position:** The lowest quintile's average income rose by a much higher percentage than the highest quintile's, so their prosperity rose relative to the highest.

**Mendota's Position:** "I disagree." The percentage may have been bigger, but the dollar increase was surely bigger for the highest quintile.

**Evaluate:** Read Mendota's concession carefully: "may have increased by a greater percentage". Mendota isn't disputing the numbers. Mendota disputes what they show. Larew measures relative prosperity by percentage change; Mendota says the absolute dollar change matters. Picture it: 10% of $10,000 is $1,000, and 5% of $200,000 is $10,000. The gap in dollars grew even though the poorer group's percentage was higher.

**Goal:** Whether comparing percentage changes is the right way to measure relative prosperity.

### Choice Notes

**(A) Correct.** Larew moves straight from "higher percentage increase" to "prosperity increased relative" to the top, so Larew treats percentages as the right measure. Mendota rejects that and points to absolute amounts.

**(B) Out of Scope.** Neither speaker measures the lowest quintile only against itself. Both compare it to the highest.

**(C) Both Agree.** Both speakers compare the two quintiles. Neither says they shouldn't be compared.

**(D) Both Agree.** Both accept that the lowest quintile's income went up.

**(E) Both Agree.** This is the most popular wrong answer. Larew says it outright, and Mendota concedes it: "may have increased by a greater percentage". A concession is not a disagreement. Mendota's objection is about what the percentage *means*.

## PT126-S4-Q13 | Agree/Disagree | C

> Sherrie: Scientists now agree that nicotine in tobacco is addictive inasmuch as smokers who try to stop smoking suffer withdrawal symptoms. For this reason alone, tobacco should be treated the same way as other dangerous drugs. Governments worldwide have a duty to restrict the manufacture and sale of tobacco. Fran: By your own admission, "addictive" is broad enough to include other commonly consumed products, such as coffee and soft drinks containing caffeine. But of course the manufacture and sale of these products should not be restricted.
>
> The dialogue above lends the most support to the claim that Sherrie and Fran disagree with each other about which one of the following statements?
>
> (A) The manufacture and sale of all drugs should be regulated by governments.
> (B) Coffee and soft drinks that contain caffeine should not be regulated by governments.
> (C) Agreement by scientists that a substance is addictive justifies government restrictions on products containing that substance.
> (D) Scientists are not proper authorities with respect to the question of whether a given substance is addictive.
> (E) Scientists and governments have a duty to cooperate in regulating drugs to protect the public health.

### Argument Breakdown

**Sherrie's Position:** Scientists agree nicotine is addictive. "For this reason alone," tobacco should be treated like other dangerous drugs, and governments should restrict it.

**Fran's Position:** By that standard, caffeinated coffee and soft drinks are addictive too, and of course they shouldn't be restricted.

**Evaluate:** "For this reason alone" tells us Sherrie thinks addictiveness by itself justifies restriction. Fran uses a counterexample to deny exactly that: caffeine is addictive in the same sense, and restriction would be absurd. Fran never disputes that nicotine is addictive.

**Goal:** Whether scientists finding a substance addictive is enough to justify restricting it.

### Choice Notes

**(A) Too Strong.** Sherrie compares tobacco to "other dangerous drugs". Sherrie never says *all* drugs should be regulated, and Fran says nothing about drugs in general.

**(B) Half Scope.** Fran clearly holds B. Sherrie never mentions coffee or soft drinks. Sherrie's principle may commit Sherrie to restricting them, which is Fran's whole point, but Sherrie never says so. C states the principle directly, so it is the stronger answer.

**(C) Correct.** Sherrie: addictiveness alone justifies restricting tobacco. Fran: addictiveness doesn't justify restricting caffeine products, so it can't be enough.

**(D) Out of Scope.** Neither questions the scientists' authority. Fran grants the definition ("By your own admission").

**(E) Out of Scope.** Neither speaker talks about scientists cooperating with governments.

## PT128-S2-Q16 | Agree/Disagree | C

> Laurel: Modern moral theories must be jettisoned, or at least greatly reworked, because they fail to provide guidance in extreme cases, which are precisely the times when people most need guidance. Miriam: A moral theory, like an overcoat, can be quite useful even if it is not useful in every possible situation. Being useful in a wide variety of common circumstances is all we need from a moral theory.
>
> Laurel's and Miriam's statements provide the most support for the claim that they disagree about whether
>
> (A) it is preferable to develop a moral theory that provides solutions to all the moral dilemmas that could arise
> (B) people abandoned earlier moral theories when they encountered dilemmas that those theories did not adequately address
> (C) a moral theory's adequacy depends on its ability to provide guidance in extreme cases
> (D) just as people need different overcoats in different climates, so too do they need different moral theories on different occasions
> (E) a moral theory developed in the light of extreme cases is unlikely to provide adequate guidance in more usual cases

### Argument Breakdown

**Laurel's Position:** Modern moral theories must be discarded or greatly reworked, because they fail to guide us in extreme cases, when we need guidance most.

**Miriam's Position:** A moral theory, like an overcoat, can be useful without working in every situation. Working well in common circumstances is all we need.

**Evaluate:** Laurel treats failure in extreme cases as fatal. Miriam says a theory only needs to handle common cases. So they disagree about the standard a moral theory has to meet: does it have to work in the extreme cases?

**Goal:** Whether a moral theory is inadequate if it fails in extreme cases.

### Choice Notes

**(A) Half Scope.** Laurel wants guidance in extreme cases, not answers to every possible dilemma. And Miriam never says a complete theory wouldn't be *preferable*. Miriam says we don't *need* one. "Preferable" and "needed" are different claims.

**(B) Out of Scope.** Neither speaker talks about what people did with earlier moral theories.

**(C) Correct.** Laurel: theories that fail in extreme cases must go. Miriam: being useful in "a wide variety of common circumstances is all we need".

**(D) Out of Scope.** This twists the analogy. Miriam's overcoat point is that one coat can be useful even if it doesn't suit every situation, not that we need different theories for different occasions.

**(E) Out of Scope.** Nobody talks about theories built around extreme cases, or how they do in usual cases.

## PT128-S3-Q4 | Agree/Disagree | D

> Huang: Most people who commit violent crimes do not carefully consider whether or how they will be punished for these crimes. And those who don't commit violent crimes have no inclination to do so. Rather than impose harsh mandatory sentences, we should attend to the root causes of violence to reduce the rate of violent crime. Suarez: Would you say the same about nonviolent crimes, such as tax evasion? Surely mandatory penalties are a useful deterrent in these cases. At any rate, I am confident that mandatory sentences prevent most people who would otherwise physically harm others from doing so.
>
> The dialogue between Huang and Suarez most strongly supports the claim that they disagree about whether
>
> (A) the best way to reduce violent crime is to address the root causes of violence
> (B) people who commit violent crimes deserve harsh punishment
> (C) people who commit violent crimes carefully consider how they will be punished for their crimes
> (D) mandatory sentences will deter most people who might otherwise commit violent crimes
> (E) severe penalties reduce the incidence of tax evasion

### Argument Breakdown

**Huang's Position:** Violent criminals don't think about punishment, and people who don't commit violence don't want to. So instead of harsh mandatory sentences, we should address the root causes of violence.

**Suarez's Position:** Mandatory penalties deter nonviolent crimes like tax evasion. And mandatory sentences prevent most people who would otherwise physically harm others from doing it.

**Evaluate:** Huang's premises add up to one claim: punishment doesn't deter violent crime. Those who commit it don't weigh punishment, and everyone else didn't need deterring. Suarez's last sentence denies exactly that. The tax evasion example is a side point Huang never addresses.

**Goal:** Whether mandatory sentences deter people who would otherwise commit violent crimes.

### Choice Notes

**(A) Half Scope.** Huang holds this. Suarez defends mandatory sentences but never says addressing root causes isn't the best approach.

**(B) Out of Scope.** Neither speaker talks about what violent criminals deserve.

**(C) Half Scope.** Huang says they don't carefully consider punishment. Suarez says sentences prevent violence, but Suarez never says criminals *carefully* weigh their punishment. Deterrence could work without that.

**(D) Correct.** Huang's reasons imply mandatory sentences don't deter violent crime. Suarez: they "prevent most people who would otherwise physically harm others from doing so".

**(E) Half Scope.** Suarez says this. Huang never mentions tax evasion.

## PT142-S2-Q7 | Agree/Disagree | D

**Steps only.** The five existing notes stay as they are.

> Talbert: Chess is beneficial for school-age children. It is enjoyable, encourages foresight and logical thinking, and discourages carelessness, inattention, and impulsiveness. In short, it promotes mental maturity. Sklar: My objection to teaching chess to children is that it diverts mental activity from something with societal value, such as science, into something that has no societal value.
>
> Talbert’s and Sklar’s statements provide the strongest support for holding that they disagree with each other over whether
>
> (A) chess promotes mental maturity
> (B) many activities promote mental maturity just as well as chess does
> (C) chess is socially valuable and science is not
> (D) children should be taught to play chess
> (E) children who neither play chess nor study science are mentally immature

### Argument Breakdown

**Talbert's Position:** Chess is beneficial for school-age children. It is enjoyable, builds foresight and logic, and promotes mental maturity.

**Sklar's Position:** I object to teaching children chess, because it diverts mental effort from things with social value, like science, into something with none.

**Evaluate:** Sklar never challenges any of Talbert's benefits. Sklar doesn't say chess fails to build maturity. Sklar's objection is that chess takes time from something more valuable. So they agree on nothing in particular, but they land on opposite sides of one practical question: should children be taught chess?

**Goal:** Whether children should be taught to play chess.

## PT156-S2-Q7 | Method | A

> Mr. Xu: The arctic squirrel gets so cold while hibernating that its blood temperature falls well below the temperature at which water freezes. Although the squirrel’s blood is about 70 percent water, the blood never freezes while the squirrel is hibernating. The squirrel’s blood, therefore, must contain a substance that prevents the blood from freezing at the temperature at which water freezes. Ms. Yerky: The blood contains no such substance. Laboratory experiments involving a number of animals, including the arctic squirrel, have shown that a vial of blood from any of the animals freezes at just the same temperature as does a vial of water.
>
> Ms. Yerky’s response proceeds by
>
> (A) presenting evidence that supports a conclusion inconsistent with Mr. Xu’s conclusion
> (B) showing that the evidence offered by Mr. Xu was collected by means of unreliable methods
> (C) offering an alternative explanation for why the squirrel’s blood fails to freeze at the temperature at which water freezes
> (D) showing that a key term used by Mr. Xu is ambiguous
> (E) showing that the evidence provided by Mr. Xu has no bearing on the point at issue

### Argument Breakdown

**Conclusion:** Ms. Yerky: the squirrel's blood contains no antifreeze substance.

**Evidence:** In lab experiments, a vial of blood from each animal tested, including the arctic squirrel, froze at the same temperature as a vial of water.

**Evaluate:** Mr. Xu reasons from a fact (the blood doesn't freeze) to a cause (it must contain a substance). Ms. Yerky doesn't dispute his fact or explain it another way. She simply offers evidence that the substance isn't there, which means her conclusion contradicts his.

**Goal:** Something like "presents evidence for the opposite of Xu's conclusion".

### Choice Notes

**(A) Correct.** Her lab evidence supports "the blood contains no such substance", which is inconsistent with Xu's "must contain a substance".

**(B) Bad Description.** She never says Xu's evidence was gathered badly. She doesn't challenge his observation about the hibernating squirrel at all.

**(C) Bad Description.** This is the tempting one. If she had said "the blood doesn't freeze because the squirrel's body does X," C would be right. But she gives no explanation of why the blood stays liquid. She only denies Xu's.

**(D) Bad Description.** No key term is said to be ambiguous.

**(E) Bad Description.** She doesn't say Xu's evidence is irrelevant. She answers it with different evidence.

## PT156-S2-Q21 | Flaw | D

> Philosopher: For some kinds of art, there is truth to the adage that beauty is in the eye of the beholder. A painting or sculpture that strikes one person as having artistic value may strike another as lacking such value. Consequently, there are no valid objective standards for determining the artistic value of a painting or a sculpture.
>
> The philosopher’s reasoning is flawed because it
>
> (A) relies exclusively on an old adage whose truth has not been demonstrated
> (B) ignores the fact that there are other kinds of art, such as literature and poetry, that may also occasion disagreement
> (C) fails to consider whether there are valid objective standards for evaluating nonvisual art, such as music
> (D) fails to consider that people who disagree about the artistic value of a given painting may be incorrectly applying the same evaluation criteria to that painting
> (E) fails to consider that the individuals judging and disagreeing about works of art may be experts in making such judgments

### Argument Breakdown

**Conclusion:** There are no valid objective standards for judging the artistic value of a painting or sculpture.

**Evidence:** For some art, beauty is in the eye of the beholder: a painting one person finds valuable may strike another as lacking value.

**Evaluate:** The argument goes from "people disagree" to "there is no correct standard". That is a gap. People disagree about math problems too, and math still has right answers. One way the gap shows up: two people might share the same standard and one of them applies it badly.

**Goal:** The argument overlooks that disagreement can come from mistakes, not from the absence of a standard.

### Choice Notes

**(A) Bad Description.** The adage isn't the only support. The philosopher also points to actual disagreement between viewers. And the flaw isn't that the adage is unproven; even granting it, the conclusion doesn't follow.

**(B) Out of Scope.** The conclusion is only about paintings and sculpture. Other art forms don't matter here.

**(C) Out of Scope.** Same problem. Music is outside the conclusion, so failing to consider it is not a flaw.

**(D) Correct.** If both viewers use the same criteria and one applies them wrongly, there is a standard, and the disagreement is just an error. The philosopher never rules this out.

**(E) Bad Description.** If the judges were experts and still disagreed, that would, if anything, help the philosopher. It doesn't expose a gap.

## PT156-S4-Q3 | Agree/Disagree | D

> James: The world is increasingly divided between the computer literate and the computer illiterate. The economic gap between rich and poor is partly responsible for causing this division, but the economic gap will widen because of the increasing importance of computer literacy. Ariel: I disagree. Because of businesses’ increasing need for computer-literate employees, companies will have to train nearly all workers in computer skills. This will lessen the division between the computer literate and the computer illiterate. So whatever might cause the economic gap between rich and poor to widen in the future, it won’t be the importance of computer literacy.
>
> James and Ariel disagree over whether
>
> (A) the economic gap between rich and poor will widen
> (B) the economic gap between rich and poor is now partly responsible for causing the division between the computer literate and the computer illiterate
> (C) businesses’ need for computer-literate employees will increase
> (D) the economic gap between rich and poor will widen as a result of the increasing importance of computer literacy
> (E) companies will have to train their employees in computer skills

### Argument Breakdown

**James's Position:** The economic gap partly causes the divide between the computer literate and illiterate. And the economic gap will widen because computer literacy is becoming more important.

**Ariel's Position:** "I disagree." Companies will have to train nearly everyone, which will shrink the divide. So whatever widens the economic gap, it won't be the importance of computer literacy.

**Evaluate:** Ariel's last sentence aims at James's last clause. Notice what Ariel leaves open: "whatever might cause the economic gap ... to widen". Ariel doesn't deny the gap will widen, only that computer literacy will be the cause.

**Goal:** Whether the importance of computer literacy will cause the economic gap to widen.

### Choice Notes

**(A) Half Scope.** James says the gap will widen. Ariel leaves that open ("whatever might cause" it), so Ariel isn't on the other side.

**(B) Half Scope.** James says this. Ariel never talks about what is causing the divide now.

**(C) Both Agree.** Ariel says businesses' need will increase, and James talks about the "increasing importance of computer literacy". Neither denies it.

**(D) Correct.** James: the gap will widen "because of the increasing importance of computer literacy". Ariel: "it won't be the importance of computer literacy".

**(E) Half Scope.** Ariel says companies will have to train workers. James never addresses training.

## PT159-S1-Q3 | Agree/Disagree | B

> Hernandez: Celebrities’ public pronouncements can warp a debate because people grant more weight to celebrities’ opinions than to ordinary people’s. For that reason, celebrities should avoid talking publicly about controversial issues on which they have no expertise. Liu: But celebrities are full members of their communities. It is not their fault if people give their opinions more credence than they should. So it is absurd that they should not feel free to join controversial debates.
>
> Hernandez and Liu disagree with each other about which one of the following?
>
> (A) People grant more weight to celebrities’ opinions than to ordinary people’s.
> (B) Celebrities should avoid talking publicly about controversial issues on which they have no expertise.
> (C) Celebrities’ pronouncements on controversial issues can warp debates on those issues.
> (D) The public should disregard what celebrities say about controversial issues.
> (E) Celebrities are responsible for the fact that people give their opinions more credence than they should.

### Argument Breakdown

**Hernandez's Position:** People give celebrities' opinions too much weight, so celebrities can warp a debate. So they should avoid talking publicly about controversial issues they know nothing about.

**Liu's Position:** Celebrities are full members of their communities. It's not their fault people overrate their opinions. So it's absurd to say they shouldn't feel free to join debates.

**Evaluate:** Liu concedes the fact: people give celebrities "more credence than they should". Liu disagrees with what Hernandez wants to *do* about it. Hernandez: they should stay out. Liu: they should feel free to join.

**Goal:** Whether celebrities should avoid speaking publicly on controversial issues outside their expertise.

### Choice Notes

**(A) Both Agree.** Hernandez says it, and Liu concedes it: people give celebrities' opinions "more credence than they should".

**(B) Correct.** Hernandez says they should avoid these debates. Liu says it's "absurd that they should not feel free to join" them.

**(C) Half Scope.** Hernandez says celebrities can warp debates. Liu never denies it; Liu just says it isn't their fault.

**(D) Out of Scope.** Neither says what the public should do with celebrities' opinions.

**(E) Half Scope.** Liu says it's not their fault. Hernandez never blames celebrities. Telling them to stay out of debates is not the same as saying they caused the problem.

## PT159-S3-Q3 | Agree/Disagree | C

> Anthropology professor: The new class I’m offering has been listed in the course catalog as a literature class, but it should be listed instead as an anthropology class. The texts we will study are all novels, but we will be examining them as sources of information about different cultures. Dean: The class is listed as it should be. All the readings in the class are works of literature.
>
> The dialogue provides the most support for the claim that the anthropology professor and the dean disagree over whether
>
> (A) all of the books that will be read in the new class are novels
> (B) a class can be listed as both an anthropology class and a literature class
> (C) the approach taken to the readings should be a crucial determinant of how a class is listed
> (D) the dean has the power to decide how a new class is to be listed
> (E) an anthropology professor should be permitted to teach a literature class

### Argument Breakdown

**Professor's Position:** The class should be listed as anthropology, not literature. The texts are novels, but the class studies them as sources about cultures.

**Dean's Position:** The listing is right, because all the readings are works of literature.

**Evaluate:** They agree on what is being read: novels, which are literature. The professor classifies by *how* the texts are studied. The dean classifies by *what* the texts are. So the clash is over which one should decide the listing.

**Goal:** Whether the approach to the readings should determine how the class is listed.

### Choice Notes

**(A) Both Agree.** The professor says the texts "are all novels" and the dean says they're all works of literature.

**(B) Out of Scope.** Neither speaker talks about listing a class under both departments.

**(C) Correct.** The professor: list it by approach (studying cultures). The dean: list it by content (literature). Whether approach is a crucial factor is exactly where they split.

**(D) Out of Scope.** Neither speaker discusses who has the power to decide listings.

**(E) Out of Scope.** Neither questions whether an anthropology professor may teach literature.
