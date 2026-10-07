---
type: draft
subject: LR Necessary Assumption batch 05, part A, 21 slots (the last NA gaps but one)
status: loaded 2026-10-01
created: 2026-10-01
---

# Necessary Assumption explanations: batch 05, part A

Source: the bank on current main (`403d488`, worktree `../ai-os-projects/lsatu-wt-bankfix-b02`) and the post-batch-04 database pull. Every remaining Necessary Assumption gap except PT119-S3-Q20, which has two overlapping step sets plus notes stored under other styles; it needs a cleanup decision, not more rows, and is logged in `fixes/index.md`.

Eleven slots are in the database: ten with no explanation, and PT147-S4-Q6 with an empty explanation row (and tags) that this batch fills. Ten are not in the database; loading them also inserts the question and choices from the bank. PT149-S4-Q16 is filed as Necessary Assumption in the bank, but its stem asks what "most logically completes" the argument, so it is loaded and explained as a fill-in-the-conclusion question.

Quality bar for this batch (Joshua, 2026-10-01: "personable and particular ... highest quality possible"):
- The Evaluate says out loud whether we are hunting a link or a defender, and why, using this stimulus's own words.
- The Goal predicts the answer before the choices.
- The correct note always negates the answer as a sentence and shows the argument breaking.
- The most-picked wrong answer (from `lr_answer_choices.student_percent`) gets the fullest note: why it pulls, then exactly where it fails.
- Each question carries one transferable move, stated once, in plain words.

Labels: Conclusion / Evidence / Evaluate / Goal. Tags from the existing NA vocabulary. Quoted question text is inserted from the bank by script.

## PT115-S4-Q25 | Necessary Assumption | C

> Political commentator: Voters tend to elect the candidate whose visual image most evokes positive feelings. Thus, laws designed to increase the fairness of elections should not allow one candidate to buy significantly more media exposure than any rival candidates can afford.
>
> Which one of the following is an assumption on which the political commentator's argument depends?
>
> (A) Elections are unfair only if at least one of the candidates has more resources than any rival candidate has.
> (B) People have positive feelings toward election candidates only when they find the candidates' visual images familiar.
> (C) The tendency of a candidate's visual image to evoke positive feelings in voters at least sometimes increases as media exposure increases.
> (D) Candidates invariably buy as much media exposure as they can afford and campaign laws allow.
> (E) Any candidate whose visual image does not evoke many positive feelings in voters will not be elected.

### Argument Breakdown

**Conclusion:** Fair election laws should not let one candidate buy far more media exposure than rivals can afford.

**Evidence:** Voters tend to elect the candidate whose visual image stirs the most positive feelings.

**Evaluate:** Look at the two nouns. The evidence is about a candidate's *image*. The conclusion is about *media exposure*. The commentator never says how one leads to the other. If more airtime did nothing for how voters feel about a candidate's image, buying more of it would be harmless. This is a link question: the answer will tie exposure to image.

**Goal:** A link: more media exposure can make a candidate's image land better with voters.

### Choice Notes

**(A) Too Strong.** "Unfair *only if*" makes resources the single possible source of unfairness. The commentator only needs this one kind of imbalance to be unfair, not every unfair election to trace back to money.

**(B) Too Strong.** Familiarity might be one route to positive feelings, but "only when" shuts out every other route. The argument does not need that.

**(C) Correct.** Notice how gentle "at least sometimes" is. That is what you want in a necessary assumption: just enough to hold the argument up. Negate it: "more media exposure *never* makes a candidate's image evoke more positive feelings." Now buying airtime gives no edge at all, and there is nothing for the fairness law to prevent.

**(D) Too Strong.** Whether candidates always spend to the limit does not matter. The worry is that some *can* buy much more, and that it would help them.

**(E) Too Strong.** "Will not be elected" turns a tendency into a guarantee. The commentator only says voters *tend* to pick the candidate with the stronger image.

## PT116-S3-Q12 | Necessary Assumption | C

> Some argue that because attaining governmental power in democracies requires building majority coalitions, it is a necessary evil that policymakers do not adhere rigorously to principle when dealing with important issues, but rather shift policies as they try to please different constituents at different times. But it is precisely this behavior that allows a democracy to adapt more easily to serve public interests, and thus it is more a benefit than an evil.
>
> Which one of the following is an assumption required by the argument?
>
> (A) Government policymakers cannot retain power if they ignore any of the various factions of their original winning coalition.
> (B) Democracies are more likely than nondemocratic forms of government to have policymakers who understand the complexity of governmental issues.
> (C) In the formulation of government policy, the advantage conferred by adaptability to diverse or fluctuating public interests outweighs the detriment associated with a lack of strict fidelity to principle.
> (D) In dealing with an important issue, policymakers in a democracy appeal to a principle in dealing with an issue only when that principle has majority support.
> (E) Democracies appear to be more flexible than nondemocratic forms of government, but are not actually so.

### Argument Breakdown

**Conclusion:** Policymakers shifting their policies to please different groups is more a benefit than an evil.

**Evidence:** That shifting is exactly what lets a democracy adapt to serve public interests.

**Evaluate:** The author concedes there is a cost (no strict loyalty to principle) and names a benefit (adaptability). Then the author declares the benefit bigger. But nothing in the evidence weighs the two. Whenever an argument says "more X than Y," it needs X to outweigh Y, and that weighing is the gap.

**Goal:** A link: the benefit of adaptability outweighs the cost of not sticking to principle.

### Choice Notes

**(A) Too Strong.** The argument is about whether shifting is good on balance. It does not need policymakers to lose power over ignoring *any* faction.

**(B) Irrelevant Comparison.** Democracies versus other governments never comes up. The author compares a benefit and a cost inside a democracy.

**(C) Correct.** This is the weighing, stated outright. Negate it: "the harm of abandoning principle outweighs the advantage of adaptability." Then shifting is more evil than benefit, the exact opposite of the conclusion.

**(D) Out of Scope.** When policymakers appeal to principle is a different question from whether shifting is worth it.

**(E) Opposite.** If democracies are not actually flexible, the benefit the author relies on disappears. An author never assumes something that sinks their own argument.

## PT118-S1-Q3 | Necessary Assumption | B

> A reason Larson cannot do the assignment is that she has an unavoidable scheduling conflict. On the other hand, a reason Franks cannot do the assignment is that he does not quite have the assertiveness the task requires. So, the task must be assigned to Parker, the only supervisor in the shipping department other than Larson and Franks.
>
> The argument depends on assuming which one of the following?
>
> (A) Larson has the assertiveness the task requires.
> (B) The task cannot be assigned to anyone other than a supervisor in the shipping department.
> (C) Franks would be assigned the task if Franks had the assertiveness the task requires.
> (D) The task cannot be assigned to anyone who has any kind of scheduling conflict.
> (E) No one who is not a supervisor in the shipping department has the assertiveness this task requires.

### Argument Breakdown

**Conclusion:** The task must go to Parker.

**Evidence:** Larson has an unavoidable scheduling conflict. Franks lacks the needed assertiveness. Parker is the only other supervisor in the shipping department.

**Evaluate:** The author crosses off two names and declares the third the winner. That only works if the list of candidates is complete. Why does it have to be a shipping supervisor at all? Someone from another department, or a non-supervisor, could take it. This is a process-of-elimination argument, and those always assume the field of options is closed.

**Goal:** A defender: the task can only go to a supervisor in the shipping department.

### Choice Notes

**(A) Not Necessary.** Larson is already out because of her schedule. Her assertiveness changes nothing.

**(B) Correct.** Negate it: "the task *can* be assigned to someone outside the shipping supervisors." Then knocking out Larson and Franks does not leave only Parker, and "must" falls apart.

**(C) Not Necessary.** What would happen in a world where Franks were more assertive does not matter. In this one, he is out.

**(D) Too Strong.** The argument only needs Larson's conflict, which is unavoidable, to rule her out. It does not need every conflict of every kind to disqualify someone.

**(E) Too Strong.** This rules out outsiders for one reason only, assertiveness. An outsider could still be barred for some other reason, so the argument does not need this. It needs the broader point in B.

## PT118-S3-Q16 | Necessary Assumption | C

> Numerous paintings and engravings representing warfare can be found in remains of all civilizations going back to and including the Neolithic period, when agriculture was first developed. However, no paintings or engravings of warfare are found dating from before the Neolithic period. Therefore, warfare must have first developed as a result of the transition to an agricultural society.
>
> Which one of the following is an assumption required by the argument?
>
> (A) Paintings and engravings were the dominant forms of artistic expression during the Neolithic period.
> (B) Warfare in the Neolithic period was always motivated by territorial disputes over agricultural land.
> (C) There was no warfare prior to the period in which paintings and engravings of warfare were first created.
> (D) Warfare is the inevitable result of the development of a civilization.
> (E) Paintings and engravings of agricultural life began to be made at the same time as paintings and engravings of warfare.

### Argument Breakdown

**Conclusion:** Warfare first developed as a result of the move to agriculture.

**Evidence:** Paintings and engravings of warfare appear in every civilization from the Neolithic period on, when agriculture began. None appear before it.

**Evaluate:** The author jumps from "no *pictures* of war" to "no *war*." Those are different things. People could have fought for thousands of years without painting it. When an argument treats the absence of a record as the absence of the thing, the answer defends that leap.

**Goal:** A defender: there was no warfare before people started painting and engraving it.

### Choice Notes

**(A) Out of Scope.** Whether painting was the dominant art form says nothing about whether war existed before it.

**(B) Too Strong.** The argument says agriculture led to warfare. It does not need every Neolithic war to be about farmland.

**(C) Correct.** Negate it: "there *was* warfare before the first war paintings." Then the lack of earlier pictures proves nothing, and warfare could predate agriculture.

**(D) Too Strong.** "Inevitable result of civilization" is a much bigger claim than the author makes or needs.

**(E) Not Necessary.** This is the most popular wrong answer, and it is tempting because it seems to tie farming and war together in the art. But the argument does not care when people started painting farms. Negate it: "paintings of farm life began at a different time than paintings of war." The argument is untouched, because it rests on when war paintings appear, not farm paintings.

## PT118-S4-Q13 | Necessary Assumption | B

> Art theft from museums is on the rise. Most stolen art is sold to wealthy private collectors. Consequently, since thieves steal what their customers are most interested in buying, museums ought to focus more of their security on their most valuable pieces.
>
> The argument depends on assuming which one of the following?
>
> (A) Art thieves steal both valuable and not-so-valuable art.
> (B) Art pieces that are not very valuable are not very much in demand by wealthy private collectors.
> (C) Art thieves steal primarily from museums that are poorly secured.
> (D) Most museums provide the same amount of security for valuable and not-so-valuable art.
> (E) Wealthy private collectors sometimes sell their stolen art to other wealthy private collectors.

### Argument Breakdown

**Conclusion:** Museums should focus more of their security on their most valuable pieces.

**Evidence:** Most stolen art goes to wealthy private collectors, and thieves steal what their customers most want to buy.

**Evaluate:** Follow the chain: thieves steal what collectors want, so protect the valuable pieces. The missing step is that collectors want the *valuable* pieces. If wealthy collectors were just as eager for modest works, the thieves would go after those too, and the advice would point nowhere.

**Goal:** A link: what collectors want is the valuable art.

### Choice Notes

**(A) Not Necessary.** Thieves taking some of both kinds does not affect where the extra security should go.

**(B) Correct.** Stated from the other side: the less valuable pieces are not in demand. Negate it: "less valuable pieces *are* very much in demand by wealthy collectors." Then thieves target them too, and there is no reason to shift security toward the most valuable pieces.

**(C) Out of Scope.** How well a museum is secured overall is a different issue from which pieces inside it to guard.

**(D) Not Necessary.** This is the top trap, and it sounds like a premise for "focus *more*." But the recommendation works from any starting point. Even if museums already favor their valuable art, the argument says to favor it further. Negate D and nothing breaks.

**(E) Out of Scope.** What collectors do with stolen art afterward does not affect which art gets stolen.

## PT120-S3-Q13 | Necessary Assumption | A

> Writer: In the diplomat’s or lawyer’s world, a misinterpreted statement can result in an international incident or an undeserved prison term. Thus, legal and diplomatic language is stilted and utterly without literary merit, since by design it prevents misinterpretation, which in these areas can have severe consequences.
>
> The writer’s argument requires assuming which one of the following?
>
> (A) Language that has literary value is more likely to be misunderstood than language without literary value.
> (B) Literary documents are generally less important than legal or diplomatic documents.
> (C) Lawyers and diplomats are much less likely to be misunderstood than are novelists.
> (D) The issues that are of interest to lawyers and diplomats are of little interest to others.
> (E) People express themselves more cautiously when something important is at stake.

### Argument Breakdown

**Conclusion:** Legal and diplomatic language is stilted and has no literary merit.

**Evidence:** It is designed to prevent misinterpretation, because misreading it can have severe consequences.

**Evaluate:** "Prevents misinterpretation" goes in; "no literary merit" comes out. Why would avoiding misreadings cost a text its literary value? Only if literary qualities are the kind of thing that invites misreading. That is the bridge the writer never builds.

**Goal:** A link: literary language is more open to misinterpretation than plain language.

### Choice Notes

**(A) Correct.** Negate it: "literary language is *no more* likely to be misunderstood than non-literary language." Then designing against misreading gives no reason to strip out literary merit, and the conclusion loses its support.

**(B) Irrelevant Comparison.** Which documents are more important never comes up.

**(C) Irrelevant Comparison.** Comparing lawyers with novelists does not connect misinterpretation to literary merit.

**(D) Out of Scope.** Who finds these issues interesting has nothing to do with how the language reads.

**(E) Not Necessary.** This is the most tempting wrong answer, because it echoes the idea of care under high stakes. But the argument is about how the language is *designed*, not about people's general caution. Negate it and the argument still runs on the design point.

## PT122-S1-Q6 | Necessary Assumption | D

> Patti: Most parents are eager for their preschoolers to learn as much as possible. However, instead of providing general opportunities for their children to learn, parents often direct their children's learning to their own personal concerns. Because children have a natural curiosity and thirst for knowledge, they learn an enormous amount simply through growing and adapting to the world. Therefore, this type of directed learning is unlikely to improve a child's preschool education.
>
> Which one of the following is an assumption on which Patti's argument depends?
>
> (A) Parents who use the type of directed learning in question have been exposed to misguided psychological theories about children.
> (B) Children will have difficulty adapting to the world without the unique help and guidance of their parents.
> (C) The type of directed learning in question is likely to enhance the general opportunities for children to learn.
> (D) The type of directed learning in question is not a necessary part of the process of growing and adapting to the world.
> (E) General opportunities to learn are not typical of the early years of formal education.

### Argument Breakdown

**Conclusion:** Directed learning is unlikely to improve a child's preschool education.

**Evidence:** Children learn an enormous amount just by growing and adapting to the world.

**Evaluate:** Patti says children learn plenty on their own, so the parents' steering adds nothing. But what if that steering is part of how children grow and adapt? Then it would be feeding the very learning Patti praises. The answer needs to keep directed learning separate from natural learning.

**Goal:** A defender: directed learning is not a necessary part of growing and adapting to the world.

### Choice Notes

**(A) Out of Scope.** Where parents got the idea for directed learning does not affect whether it helps.

**(B) Weakens.** If children struggle to adapt without parental guidance, directed learning may be exactly what they need.

**(C) Opposite.** This is the most popular wrong answer. It mentions the right things (directed learning, general opportunities), but it points the wrong way. If directed learning enhances learning opportunities, it would *improve* a child's education. Patti would never assume that.

**(D) Correct.** Negate it: "directed learning *is* a necessary part of growing and adapting." Then it is part of how children learn that enormous amount, and Patti cannot say it fails to help.

**(E) Out of Scope.** Formal schooling comes after preschool. The argument is about preschoolers.

## PT122-S4-Q13 | Necessary Assumption | B

> It is due to a misunderstanding that most modern sculpture is monochromatic. When ancient sculptures were exhumed years ago, they were discovered to be uncolored. No one at the time had reason to believe, as we now do, that the sculptures had originally been colorfully painted, but that centuries of exposure to moisture washed away the paint.
>
> Which one of the following is an assumption on which the argument depends?
>
> (A) The natural beauty of the materials out of which modern sculptures are made plays a part in their effect.
> (B) Modern sculpture has been influenced by beliefs about ancient sculpture.
> (C) Ancient sculptures were more susceptible to moisture damage than are modern sculptures.
> (D) Some ancient paintings known to early archaeologists depicted sculptures.
> (E) As modern sculptors come to believe that ancient sculpture was painted, they will begin to create polychromatic works.

### Argument Breakdown

**Conclusion:** Most modern sculpture is monochromatic because of a misunderstanding.

**Evidence:** Ancient sculptures were dug up uncolored. At the time, no one knew the paint had washed off over the centuries.

**Evaluate:** The evidence is a mistake about *ancient* sculpture. The conclusion blames that mistake for how *modern* sculpture looks. That only works if modern sculptors were taking their cue from the ancient ones. Without that, the old mistake is just a fun fact.

**Goal:** A link: modern sculpture was shaped by beliefs about ancient sculpture.

### Choice Notes

**(A) Out of Scope.** The natural beauty of the materials is a different explanation for plain sculpture, and the argument does not need it.

**(B) Correct.** Negate it: "modern sculpture has *not* been influenced by beliefs about ancient sculpture." Then the misunderstanding about the ancients cannot explain why modern work is monochromatic.

**(C) Irrelevant Comparison.** This is the top trap, because the stimulus talks about moisture washing paint away. But how modern sculpture holds up to moisture has nothing to do with why it is made without color.

**(D) Not Necessary.** Paintings that show sculptures might be a clue someone missed, but the argument does not need that clue to exist.

**(E) Not Necessary.** This predicts the future. The argument explains the past, and works whether or not sculptors change course.

## PT124-S2-Q7 | Necessary Assumption | A

> In Western economies, more energy is used to operate buildings than to operate transportation. Much of the decline in energy consumption since the oil crisis of 1973 is due to more efficient use of energy in homes and offices. New building technologies, which make lighting, heating, and ventilation systems more efficient, have cut billions of dollars from energy bills in the West. Since energy savings from these efficiencies save several billion dollars per year today, we can conclude that 50 to 100 years from now they will save more than $200 billion per year (calculated in current dollars).
>
> On which one of the following assumptions does the argument rely?
>
> (A) Technology used to make buildings energy efficient will not become prohibitively expensive over the next century.
> (B) Another oil crisis will occur in the next 50 to 100 years.
> (C) Buildings will gradually become a less important consumer of energy than transportation.
> (D) Energy bills in the West will be $200 billion lower in the next 50 to 100 years.
> (E) Energy-efficient technologies based on new scientific principles will be introduced in the next 50 to 100 years.

### Argument Breakdown

**Conclusion:** In 50 to 100 years, these efficiencies will save more than $200 billion a year.

**Evidence:** Building efficiencies save several billion dollars a year now and have cut billions from Western energy bills.

**Evaluate:** This is a prediction, and predictions assume the road ahead stays open. "Several billion now" becomes "over $200 billion later" only if people keep using these technologies. What could stop them? The technology could become too expensive to use, or be abandoned. The answer will rule out something like that.

**Goal:** A defender: nothing will stop people from keeping and expanding these efficiencies, such as the technology becoming too expensive.

### Choice Notes

**(A) Correct.** Negate it: "the technology *will* become prohibitively expensive." Then buildings stop using it, the savings shrink instead of growing, and $200 billion a year is out of reach.

**(B) Out of Scope.** Another oil crisis might raise prices, but the argument does not need one.

**(C) Opposite.** If buildings become a smaller share of energy use, savings from buildings would matter less. The author would not assume that.

**(D) Not Necessary.** This restates the conclusion in different words. An assumption is something the argument relies on to get to the conclusion, not the conclusion itself.

**(E) Not Necessary.** This is the most popular wrong answer, and it feels right: how else would savings grow so much? But growth can come from using today's technology in more buildings. The argument does not need brand-new science. Negate E and the prediction can still come true.

## PT126-S4-Q14 | Necessary Assumption | B

> In 1963, a young macaque monkey was observed venturing into a hot spring to retrieve food which had fallen in. Soon, other macaques began to enter the spring, and over a few years this behavior was adopted by the entire troop. Prior to 1963, no macaques had ever been observed in the hot spring; by 1990, the troop was regularly spending time there during the winters. Thus, these macaques are able to adopt and pass on new patterns of social behavior, and are not complete captives of their genetic heritage.
>
> Which one of the following is an assumption required by the argument above?
>
> (A) Mutations in the genetic heritage of a certain variety of macaques can occur over a time span as short as a few years or decades.
> (B) New patterns of behavior that emerge in macaque populations over the course of a few years or decades are not necessarily genetically predetermined.
> (C) Only when behaviors become typical among an animal population can we conclude that a genetic alteration has occurred in that variety or species.
> (D) The social behaviors of macaques are completely independent of their genetic heritage.
> (E) The macaques' new pattern of behavior will persist over several generations.

### Argument Breakdown

**Conclusion:** These macaques can adopt and pass on new social behavior, and are not complete captives of their genes.

**Evidence:** One macaque went into a hot spring in 1963. Within a few years the whole troop did it, and by 1990 the troop regularly spent winters there.

**Evaluate:** The author reads the spread of the behavior as learning. But what if the behavior was genetic all along, waiting for the right moment to show up? Then it would not be a new behavior passed on socially. The answer has to rule out that the genes explain it.

**Goal:** A defender: the new behavior was not simply set by the macaques' genes.

### Choice Notes

**(A) Opposite.** If genes can change in a few years, a genetic explanation becomes *more* plausible. That hurts the author.

**(B) Correct.** "Not necessarily" is soft, and soft is exactly what a necessary assumption should be. Negate it: "new behaviors that appear in a few years *are* genetically predetermined." Then the hot spring habit came from genes, not social learning, and the conclusion falls.

**(C) Out of Scope.** This sets a rule for concluding that genes changed. The author is concluding the opposite.

**(D) Too Strong.** This is the most popular wrong answer, and it is easy to see why: it sounds like the conclusion. But the author says the macaques are not *complete* captives of their genes. That leaves room for genes to matter a lot. "Completely independent" goes far beyond what the argument needs.

**(E) Not Necessary.** The argument is about the ability to adopt and pass on behavior. It does not need this habit to last for generations.

## PT141-S2-Q1 | Necessary Assumption | C

> Editorial: The city has chosen a contractor to upgrade the heating systems in public buildings. Only 40 percent of the technicians employed by this contractor are certified by the Heating Technicians Association. So the city selected a contractor 60 percent of whose technicians are unqualified, which is an outrage.
>
> Which one of the following is an assumption required by the argument in the editorial?
>
> (A) Certified technicians receive higher pay than uncertified technicians.
> (B) There are no contractors with fewer than 40 percent of their technicians certified.
> (C) Technicians who lack certification are not qualified technicians.
> (D) Qualified technicians installed the heating systems to be upgraded.
> (E) The contractor hired by the city has personal ties to city officials.

### Argument Breakdown

**Conclusion:** The city picked a contractor with 60 percent unqualified technicians.

**Evidence:** Only 40 percent of the contractor's technicians are certified.

**Evaluate:** "Not certified" goes in; "unqualified" comes out. Those are not the same word. A technician can be skilled and experienced without holding this one association's certificate. When an argument quietly swaps one term for another, the answer equates them.

**Goal:** A link: uncertified technicians are unqualified.

### Choice Notes

**(A) Out of Scope.** Pay has nothing to do with qualification.

**(B) Not Necessary.** Other contractors being worse would not change whether this one's technicians are qualified.

**(C) Correct.** Negate it: "some technicians who lack certification *are* qualified." Then the 60 percent figure is not a count of unqualified people, and the outrage loses its basis.

**(D) Out of Scope.** Who installed the old systems says nothing about the contractor's workers.

**(E) Out of Scope.** Personal ties might be another reason to object, but the editorial's argument is about qualifications.

## PT143-S1-Q1 | Necessary Assumption | B

> Pundit: Our city made a mistake when it sold a private company the rights to assess and collect parking fees. The private company raised parking fees and so has been able to reap profits far greater than what it paid for the rights to assess and collect the fees. If the city had not sold the rights, then that money would have gone to the city.
>
> The pundit’s argument requires the assumption that
>
> (A) other private companies would have been willing to pay for the rights to assess and collect parking fees
> (B) the city could have raised parking fees had it not sold the rights
> (C) municipal functions like assessing and collecting parking fees should always be handled directly by the municipality in question
> (D) the revenue from parking fees is not the only factor that cities need to consider in setting the rates for parking fees
> (E) private companies assess and collect parking fees more efficiently than cities do

### Argument Breakdown

**Conclusion:** The city made a mistake selling the parking fee rights, because that money would have gone to the city.

**Evidence:** The private company raised fees and earned far more than it paid for the rights.

**Evaluate:** The company's big profits came from *raising fees*. The pundit assumes the city would have earned that same money. But that only follows if the city could have raised fees the same way. If it could not (say, it lacked the authority or the political room), the city would never have seen those profits.

**Goal:** A defender: the city could have done what the company did and raised the fees.

### Choice Notes

**(A) Not Necessary.** Other bidders do not matter. The question is whether the city could have kept the money itself.

**(B) Correct.** Negate it: "the city *could not* have raised parking fees." Then the company's extra profits came from something the city could never have done, and that money would not have gone to the city.

**(C) Too Strong.** "Always" handle it directly is a sweeping rule. The pundit only claims this one sale was a mistake.

**(D) Out of Scope.** Other factors in setting rates do not affect whether the city could have earned this money.

**(E) Weakens.** If private companies collect fees more efficiently, the city might have earned less than the company did. That is a point against the pundit.

## PT143-S3-Q2 | Necessary Assumption | B

> While sales of other highly fuel-efficient automobiles are in decline, sales of the Hydro are rising. The Hydro’s manufacturers attribute its success to the Hydro’s price and very low fuel consumption. However, the Hydro is comparable in price and fuel efficiency to its competitors, so it is more likely that its success is due to the fact that people want to appear environmentally conscious to their neighbors.
>
> Which one of the following is an assumption required by the argument?
>
> (A) The Hydro is the most popular highly fuel-efficient automobile available.
> (B) The Hydro is recognizable as environmentally friendly in a way that its competitors are not.
> (C) The Hydro has a better safety record than its competitors.
> (D) Hydro buyers are more likely to have neighbors who also drive Hydros.
> (E) Hydro buyers have less interest in environmental causes than buyers of other highly fuel-efficient automobiles.

### Argument Breakdown

**Conclusion:** The Hydro's success is more likely due to people wanting to appear environmentally conscious to their neighbors.

**Evidence:** The Hydro's sales are rising while other fuel-efficient cars decline. It matches its competitors on price and fuel efficiency.

**Evaluate:** This is a comparison. The author's explanation has to account for the *difference* between the Hydro and its competitors. But every fuel-efficient car signals environmental concern. If the neighbors cannot tell a Hydro apart from the rest, wanting to look green would help all of them equally. For the explanation to work, the Hydro has to stand out.

**Goal:** A defender: the Hydro is seen as green in a way its competitors are not.

### Choice Notes

**(A) Not Necessary.** The Hydro does not need to be the best-seller, only to be gaining while others lose.

**(B) Correct.** Negate it: "the Hydro is *not* recognizable as environmentally friendly in any way its competitors are not." Then the urge to look green helps every competitor just as much, and it cannot explain why only the Hydro is rising.

**(C) Weakens.** A better safety record is a different explanation for the Hydro's success, which works against the author.

**(D) Out of Scope.** Whether neighbors drive Hydros is beside the point. The question is whether the car signals anything to them.

**(E) Out of Scope.** The argument is about *appearing* environmentally conscious. How much buyers actually care about the environment does not matter.

## PT145-S2-Q3 | Necessary Assumption | E

> The current sharp decline in commercial honeybee populations has been attributed to the same viral and bacterial infections, pesticide poisonings, and mite infestations that devastated bees in the past. Whichever of these adverse conditions is the immediate cause, it is highly likely that there is also a long-ignored underlying condition, and that is inbreeding. Decades of breeding practices meant to maximize pollinating efficiency have limited honeybees’ genetic diversity.
>
> Which one of the following is an assumption that is required by the argument?
>
> (A) Commercial honeybees are more vulnerable to problems with inbreeding than wild honeybees are.
> (B) The results of decades of breeding practices cannot be quickly undone.
> (C) The genetic diversity of the honeybee population continues to decline.
> (D) In the past, viral infections and mites have devastated genetically diverse honeybee populations.
> (E) Lack of genetic diversity can make honeybees more vulnerable to adverse conditions.

### Argument Breakdown

**Conclusion:** Inbreeding is likely an underlying cause of the current decline in commercial honeybees.

**Evidence:** Decades of breeding for pollinating efficiency have limited honeybees' genetic diversity.

**Evaluate:** The evidence shows low genetic diversity. The conclusion says that low diversity is helping kill the bees. Nothing connects the two. The author also says the immediate causes are the familiar ones: infections, poisons, mites. So the link has to be that low diversity makes bees more vulnerable to exactly those things.

**Goal:** A link: low genetic diversity makes honeybees more vulnerable to these threats.

### Choice Notes

**(A) Irrelevant Comparison.** Wild bees never come up. The argument is about commercial bees.

**(B) Not Necessary.** Whether the damage can be undone quickly is a question about the fix, not the cause.

**(C) Not Necessary.** Diversity does not need to keep falling. Being low is enough for the argument.

**(D) Weakens.** If threats wiped out genetically diverse populations in the past, diversity does not protect bees. That cuts against the idea that low diversity is the hidden problem.

**(E) Correct.** Negate it: "lack of genetic diversity *cannot* make honeybees more vulnerable to adverse conditions." Then inbreeding does nothing to help the infections and mites along, and it is no underlying cause at all.

## PT147-S4-Q6 | Necessary Assumption | B

> Scientist: Laboratory animals have access to ample food, and they get relatively little exercise. These factors can skew the results of research using animals, since such studies often rely on the assumption that the animal subjects are healthy. For instance, animal studies that purport to show that extreme caloric restriction can extend lifespans take for granted that their subjects were not overfed to begin with.
>
> The scientist’s argument requires assuming which one of the following?
>
> (A) Laboratory animals are healthy if they are fed a carefully restricted diet and get plenty of exercise.
> (B) Laboratory conditions that provide animals with ample food but relatively little exercise can be unhealthy for the animals.
> (C) It is not unusual for animals outside of laboratory settings to have access to ample food and get relatively little exercise.
> (D) Some animal studies take into consideration the differences between the living conditions of laboratory animals and those of other animals.
> (E) When provided with unlimited food over a long period of time, animals show little day-to-day variation in their eating habits.

### Argument Breakdown

**Conclusion:** Ample food and little exercise can skew the results of animal research.

**Evidence:** Lab animals get ample food and little exercise. Many studies assume their subjects are healthy. The caloric restriction studies, for example, assume their animals were not overfed to begin with.

**Evaluate:** The skewing only happens if lab conditions make the animals *unhealthy*. If eating freely and exercising little left them perfectly healthy, the studies' assumption would be true, and nothing would be skewed. The scientist never says the conditions are bad for the animals.

**Goal:** A link: ample food and little exercise can be unhealthy for lab animals.

### Choice Notes

**(A) Reversal.** This is the most popular wrong answer. It flips the scientist's idea: the scientist needs bad conditions to *cause* poor health, not good conditions to *guarantee* good health. A restricted diet and plenty of exercise could still leave an animal unhealthy for other reasons, and the argument would be fine.

**(B) Correct.** Negate it: "these conditions *cannot* be unhealthy for the animals." Then the animals are healthy, the studies' assumption holds, and there is nothing to skew the results.

**(C) Out of Scope.** Animals outside the lab are not part of the argument.

**(D) Out of Scope.** What some studies take into account does not affect whether the conditions can skew results.

**(E) Out of Scope.** How steady their eating habits are says nothing about whether the habits are healthy.

## PT149-S4-Q16 | Must Be True (fill in the blank) | D

> Economist: Currently, many countries rely primarily on taxing income to fund government expenditures. But taxing income does nothing to promote savings and investment. Taxing consumption, on the other hand, would encourage savings. The most important challenge facing these countries is improving their economies, and the only way to accomplish this is to increase their savings rates.
>
> Which one of the following most logically completes the economist’s argument?
>
> (A) most governments should stop taxing savings and investment
> (B) the economies of countries will rapidly improve if their governments adopt tax policies that encourage savings and investment
> (C) in most countries taxes on consumption alone could raise adequate revenues to fund government expenditures
> (D) the tax laws of many countries should be revised to focus on taxing consumption rather than income
> (E) it is detrimental to the economic improvement of any country to continue to tax income

### Argument Breakdown

**Conclusion:** The blank: the policy the economist's facts point to.

**Evidence:** Improving their economies is these countries' biggest challenge. The only way to do it is to raise savings rates. Taxing income does nothing for savings. Taxing consumption would encourage them.

**Evaluate:** Line the facts up and the conclusion almost writes itself. The goal needs higher savings. Income taxes do not help with that, and consumption taxes do. So these countries should move from taxing income to taxing consumption. A completion answer should land exactly where the evidence points, and go no further.

**Goal:** These countries should shift from taxing income toward taxing consumption.

### Choice Notes

**(A) Out of Scope.** The economist never says anyone taxes savings. Stopping a tax that was never mentioned does not follow.

**(B) Too Strong.** Higher savings are the *only* way to improve, but that does not make them a guarantee of improvement, let alone a rapid one.

**(C) Out of Scope.** Whether consumption taxes alone could pay for everything is never discussed.

**(D) Correct.** This is the conclusion the evidence builds toward: switch the tax focus to the one that encourages savings. Every piece of the argument supports it, and it claims nothing extra.

**(E) Too Strong.** "Detrimental" to "any country" goes well past the evidence. The economist only says income taxes do nothing for savings, not that they actively hurt every economy.

## PT156-S4-Q11 | Necessary Assumption | B

> A law is futile unless most of the parties subject to it abide by it willingly. Thus, there can be no comprehensive international solution to the problem of pollution, since few nations would willingly give up their power over their own industries.
>
> Which one of the following is an assumption required by the argument?
>
> (A) A comprehensive solution to the problems of pollution would require major changes in international law.
> (B) Some nations would be required to give up some of their power over their own industries as part of any comprehensive solution to the problem of pollution.
> (C) If most nations were willing to abide by international law, then there could be a comprehensive solution to the problem of pollution.
> (D) The problems created by pollution affect most of the world’s nations, but the pollution itself is produced by the industries of relatively few nations.
> (E) Most of the current international laws concerning pollution do not require nations to give up any of their power over their own industries.

### Argument Breakdown

**Conclusion:** There can be no comprehensive international solution to pollution.

**Evidence:** A law is futile unless most of the parties under it obey willingly. Few nations would willingly give up power over their own industries.

**Evaluate:** The reluctance only matters if a solution would actually *ask* nations to give up that power. If a comprehensive solution could be built without touching anyone's control over their industries, nobody's reluctance would get in the way.

**Goal:** A link: any comprehensive solution would require some nations to give up some power over their industries.

### Choice Notes

**(A) Not Necessary.** Changes to international law may or may not be involved. The argument turns on giving up power over industries.

**(B) Correct.** Notice the "some ... some" wording: modest and exactly enough. Negate it: "a comprehensive solution would require *no* nation to give up *any* power over its industries." Then the reluctance is irrelevant, and the conclusion has no support.

**(C) Reversal.** This says willing obedience would be enough for a solution. The argument needs the reverse: no willing obedience means no solution.

**(D) Out of Scope.** Who produces the pollution and who suffers from it is never discussed.

**(E) Out of Scope.** What current laws require says nothing about what a comprehensive solution would require.

## PT156-S4-Q20 | Necessary Assumption | B

> Azalea bushes flourish in acidic soil. Clay soil, while rarely acidic, can be mixed with other types of soil to create a soil that is acidic. Hence, azalea bushes can be made to flourish in clay soil.
>
> Which one of the following is an assumption on which the argument depends?
>
> (A) Mixing an acidic soil with another type of soil always results in an acidic soil.
> (B) Clay soil that is mixed with certain other types of soil is still clay soil.
> (C) Whenever clay soil is mixed with other types of soil, an acidic soil results.
> (D) Some plants do not flourish in acidic soil.
> (E) Azalea bushes do as well in treated clay soils as in naturally acidic soils.

### Argument Breakdown

**Conclusion:** Azalea bushes can be made to flourish in clay soil.

**Evidence:** Azaleas flourish in acidic soil. Clay soil, mixed with other soils, can become acidic.

**Evaluate:** Here is the sleight of hand. Once you mix clay with other soils, is it still *clay soil*? If the mixture counts as something else, the azaleas are flourishing in a new soil, not in clay. The conclusion depends on the mixture keeping its name.

**Goal:** A link: clay soil mixed with other soils still counts as clay soil.

### Choice Notes

**(A) Too Strong.** "Always" is far more than needed. The stimulus only says clay *can* be mixed into something acidic.

**(B) Correct.** Negate it: "clay soil mixed with other soils is *no longer* clay soil." Then the azaleas grow in a different soil, and the claim about clay soil falls apart.

**(C) Too Strong.** The argument needs only some mixtures to turn acidic, not every one.

**(D) Out of Scope.** Other plants are beside the point.

**(E) Too Strong.** Azaleas only need to flourish. They do not need to do *as well* as they do in naturally acidic soil.

## PT159-S1-Q6 | Necessary Assumption | E

> Prominent government officials have denied that their policies have produced serious environmental degradation. But the facts show otherwise. Last year, at the urging of certain mining companies, the government repealed a long-standing provision prohibiting the dumping of mining wastes into streams. Since that time, hundreds of miles of vital streams have been buried under bulldozed mining wastes.
>
> The argument relies on which one of the following assumptions?
>
> (A) Without the urging of certain mining companies, the government would not have lifted the ban on dumping mining wastes into streams.
> (B) The prominent government officials who deny that government policies have produced serious environmental degradation do not really believe what they are claiming.
> (C) The mining companies that urged repeal of the ban on dumping mining wastes in streams were among those that buried hundreds of miles of streams under mining wastes.
> (D) The government is generally more responsive to pressures from the mining industry than from environmentalists.
> (E) If the ban on dumping mining wastes in streams had not been repealed, considerably less mining waste would have found its way into streams.

### Argument Breakdown

**Conclusion:** Government policies have caused serious environmental damage, contrary to the officials' denials.

**Evidence:** The government repealed the ban on dumping mining waste into streams. Since then, hundreds of miles of streams have been buried under it.

**Evaluate:** This is a before-and-after argument: the ban went away, then the streams were buried. To blame the *policy*, the repeal has to make a difference. If the mining waste would have ended up in the streams anyway (say, the ban was widely ignored), the repeal caused nothing.

**Goal:** A defender: without the repeal, much less waste would have reached the streams.

### Choice Notes

**(A) Not Necessary.** Why the government lifted the ban does not matter. What matters is what happened after.

**(B) Out of Scope.** Whether the officials believe their own denials does not affect whether the policy caused damage.

**(C) Not Necessary.** It does not matter which companies did the dumping, only that the repeal led to it.

**(D) Irrelevant Comparison.** Comparing the mining industry with environmentalists does not connect the policy to the damage.

**(E) Correct.** Negate it: "even with the ban, about the same amount of waste would have reached the streams." Then the buried streams are not the policy's doing, and the facts no longer contradict the officials.

## PT159-S1-Q17 | Necessary Assumption | A

> Essayist: It would be wrong to defend current testing procedures for new medications simply by appealing to the fact that test subjects are volunteers who are both apprised of and compensated for the risks involved. For while it is not wrong to pay people to do something if they are freely choosing to do it, the same cannot be said if the choice is made under duress.
>
> Which one of the following is an assumption required by the essayist’s argument?
>
> (A) Possessing information about the possible consequences of the choices one makes does not ensure that one’s choices are free.
> (B) No transaction can be justified merely on the grounds that those participating in the transaction do so voluntarily.
> (C) Anyone who acts without complete freedom is acting under some form of externally imposed duress.
> (D) There is nothing wrong with accepting money for putting oneself at risk.
> (E) People should be permitted to perform any action so long as that action is freely chosen.

### Argument Breakdown

**Conclusion:** It is wrong to defend current drug testing *simply* because the subjects are informed volunteers who are paid.

**Evidence:** Paying people is fine when they choose freely, but not when the choice is made under duress.

**Evaluate:** The defense rests on two facts: the subjects are informed, and they volunteer. The essayist answers by bringing up duress. But duress only matters if being informed is not enough to make a choice free. If knowing the risks guaranteed a free choice, the defense would hold. So the essayist has to assume information and freedom can come apart.

**Goal:** A link: knowing the risks does not guarantee the choice is free.

### Choice Notes

**(A) Correct.** Negate it: "being informed about the consequences *does* guarantee the choice is free." Then informed volunteers are choosing freely, paying them is fine, and the defense the essayist rejects is actually sound.

**(B) Too Strong.** "No transaction" can ever be justified by voluntariness alone? The essayist does not go that far. They say voluntariness plus payment is not enough *here* because duress is possible.

**(C) Too Strong.** Linking every limit on freedom to outside duress is a broad claim the argument never needs.

**(D) Out of Scope.** The essayist is not saying risk-for-money is wrong in itself, only that it is wrong under duress.

**(E) Too Strong.** "Any action" freely chosen should be allowed is a sweeping principle, and it points the wrong way for this argument.

## PT159-S3-Q2 | Necessary Assumption | B

> Entertainment reporter: Unlike most major motion pictures, the release of the upcoming film Escapade II has not been preceded by free, advance screenings that show the film to select audiences for promotional purposes. With movie research showing awareness of the film at 96 percent, and with around 60 percent of filmgoers indicating “definite interest” in the film, the film’s distributors must have decided not to do anything that could reduce interest in the film.
>
> The entertainment reporter’s explanation for why there have been no advance screenings of Escapade II relies on assuming that the distributors believe that
>
> (A) advance screenings of Escapade II would cost them a significant amount that could much more effectively be spent on advertising
> (B) advance screenings of Escapade II might lead to a dampening of the enthusiasm of filmgoers who would otherwise have an interest in seeing the film
> (C) the select audiences who would normally be invited to free, advance screenings of a major motion picture would probably not enjoy Escapade II
> (D) if 96 percent of the public is aware of the upcoming release of Escapade II, it is probable that 96 percent of the public intends to see the film
> (E) the film Escapade II would most likely be viewed by approximately 60 percent of the public if no advance screenings are given

### Argument Breakdown

**Conclusion:** The distributors skipped advance screenings because they decided not to do anything that could reduce interest in the film.

**Evidence:** Awareness of the film is at 96 percent, and about 60 percent of filmgoers say they are definitely interested.

**Evaluate:** The reporter explains skipping screenings as a way to protect interest. That only makes sense if the distributors thought screenings *could* hurt interest. If they thought screenings could only help, avoiding them would not protect anything. The question even tells you the answer is about what the distributors *believe*.

**Goal:** A link: the distributors believed screenings might reduce interest in the film.

### Choice Notes

**(A) Weakens.** Cost is a different reason to skip the screenings. That competes with the reporter's explanation instead of supporting it.

**(B) Correct.** Negate it: "the distributors believed screenings would *not* dampen anyone's enthusiasm." Then skipping them does nothing to protect interest, and the reporter's explanation stops making sense.

**(C) Too Strong.** The distributors only need to think screenings *might* hurt interest. They do not need to predict that the audiences would dislike the film.

**(D) Out of Scope.** Whether awareness turns into ticket sales is not part of the explanation.

**(E) Not Necessary.** A specific prediction about how many people see the film goes beyond what the explanation needs.
