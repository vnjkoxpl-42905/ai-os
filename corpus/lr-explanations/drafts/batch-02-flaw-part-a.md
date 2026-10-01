---
type: draft
subject: LR Flaw batch 02, part A, 20 slots
status: draft, not loaded
created: 2026-10-01
---

# Flaw explanations: batch 02, part A

Source: the designated bank (`../ai-os-projects/lsatu-wt-glossary/public/data/`) and the 2026-10-01 post-batch-01 database pull. Batch 02 is every remaining slot tagged Flaw or Flawed Reasoning: 40 in all. This file holds the first 20 in gap-list order.

Slot states in this part: PT107-S3-Q7 needs only its missing C note (steps and four notes exist). PT120-S1-Q23 has steps and needs all five notes. PT120-S1-Q8 and the five PT121/PT122 slots are in the database with no explanation. The remaining 12 (PT127 onward) are not in the database at all; loading them will also insert the question and choices from the bank.

The `Modelled on` references are picks from `models/Flaw.md`, matched by sub-pattern. `neighbors.py` was not run: it is hard-wired to the pilot's `picks.json` and relative `pilot/` paths. All choice-note tags occur in the batch 01 vocabulary. Quoted question text is bank wording, with whitespace normalized; bank glitches are left as found and listed under each slot. No bank or database edits are part of this draft.

## PT107-S3-Q7 | Flaw | E

**Notes only: supplies the missing C note.** The existing Conclusion, Evidence, Evaluate and Goal steps and the A, B, D and E notes stay as they are.

**Modelled on:** PT134-S3-Q6 (correlation, reverse cause), PT141-S4-Q3 (groups not fair to compare).

> Newsletter for community-center volunteers: Retired persons who regularly volunteer their time to help others generally display fewer and milder effects of aging than their nonvolunteering contemporaries: in social resources, mental outlook, physical health, economic resources, and overall functioning, they are found to be substantially stronger than nonvolunteers. V olunteering is often described as doing good works to improve the lives of others. How good to know that there is evidence that it can equally benefit your own well-being!
>
> The inference drawn above is unwarranted because
>
> (A) the center has a self-interested motive to attract new volunteers
> (B) it interprets “well-being” as including the factors of social and economic resources, mental outlook, physical health, and overall functioning
> (C) some of those who do not volunteer might be older than some volunteers and so could not be considered their peers
> (D) growing older might not necessarily result in a change in mental outlook
> (E) those with better resources, health, outlook, and functioning are more able to work as volunteers

Bank glitch: "V olunteering" has a stray space. The database stimulus is already loaded and is not touched.

### Choice Notes

**(C) No Impact.** This tries the "groups not fair to compare" objection, so test it. The volunteers are compared with their *contemporaries*, people of roughly the same age. A few nonvolunteers being somewhat older than a few volunteers would not explain gaps in money, social resources and outlook across the whole group. The comparison is fair enough on age. The real problem is the direction of cause, which is what (E) supplies.

## PT120-S1-Q8 | Flaw | E

**Modelled on:** PT155-S1-Q20 (unproven vs proven false), PT113-S2-Q3 (test each prefix).

> Fortune-teller: Admittedly, the claims of some selfproclaimed “psychics” have been shown to be fraudulent, but the exposure of a few charlatans cannot alter the fundamental fact that it has not been scientifically proven that there is no such thing as extrasensory perception (ESP). Furthermore, since the failed attempts to produce such a proof have been so numerous, one must conclude that some individuals do possess ESP.
>
> The reasoning in the fortune-teller’s argument is most vulnerable to criticism on the grounds that the argument
>
> (A) takes for granted that proof that many people lack a characteristic does not establish that everyone lacks that characteristic
> (B) takes for granted that the number of unsuccessful attempts to prove a claim is the only factor relevant to whether one should accept that claim
> (C) overlooks the possibility that some of the scientific studies mentioned reached inaccurate conclusions about whether ESP exists
> (D) takes for granted that there is no scientific way to determine whether some individuals possess ESP
> (E) takes for granted that the fact that a claim has not been demonstrated to be false establishes that it is true

### Argument Breakdown

**Conclusion:** Some individuals do possess ESP.

**Evidence:** No one has scientifically proven that ESP does not exist, and many attempts to prove that have failed.

**Evaluate:** Look at what the evidence actually establishes: nobody has disproven ESP. Does that prove ESP is real? Imagine a friend says, "No one has proven I *didn't* eat the last cookie, so I must have eaten it." The failure to prove something false leaves the question open. It does not settle it in favor of the claim. Many failed attempts make the open question feel weightier, but they still are not evidence that anyone actually has ESP.

**Goal:** Look for the move from "not proven false" to "true."

### Choice Notes

**(A) Not an Objection.** This is about the charlatans: exposing a few frauds does not show that everyone lacks ESP. The fortune-teller does rely on that idea, but it is a reasonable idea. Negate it and you get "proof that many lack a trait shows everyone lacks it," which is plainly false. Relying on a true principle is not the flaw.

**(B) Too Strong.** The fortune-teller does not need the number of failed attempts to be the *only* relevant factor. She treats it as enough, but she would be just as wrong if other factors mattered too.

**(C) Out of Scope.** The studies she mentions are attempts to *disprove* ESP that failed. If some of them reached inaccurate conclusions, we learn nothing about the leap from "not disproven" to "proven." The flaw survives untouched.

**(D) Not Assumed.** She says the attempts so far have failed, not that no scientific method could ever settle the question. Her conclusion would be just as flawed if a perfect test existed but had not yet been run.

**(E) Correct.** "It has not been proven that there is no ESP" becomes "some people have ESP." That treats a claim's not being shown false as proof that it is true. This is the classic unproven vs proven false flaw, run in the positive direction.

## PT120-S1-Q23 | Flaw | D

**Notes only: supplies all five notes.** The existing Conclusion, Evidence, Evaluate and Goal steps stay as they are.

**Modelled on:** PT151-S4-Q23 (illegal reversal), PT113-S2-Q3 (diagram the rule).

> Columnist: Neuroscientists have found that states of profound creativity are accompanied by an increase of theta brain waves, which occur in many regions of the brain, including the hippocampus. They also found that listening to music increases theta waves dramatically. Thus, one can attain a state of profound creativity merely by listening to a tape of recorded music.
>
> The columnist’s reasoning is most vulnerable to criticism on the grounds that it
>
> (A) takes for granted that there is a causal connection between the hippocampus and being in a state of profound creativity
> (B) fails to consider that music is not necessary for one to be in a state of profound creativity
> (C) does not rule out the possibility that listening to music by means other than a tape recording also increases theta waves
> (D) ignores the possibility that an increase in theta waves may not always be accompanied by a state of profound creativity
> (E) provides insufficient reasons to believe that people who are not in states of profound creativity have low levels of theta brain waves

### Choice Notes

**(A) Out of Scope.** The hippocampus is just one place theta waves occur. The argument's leap is from theta waves to creativity; no claim about the hippocampus causing anything is needed.

**(B) Not an Objection.** The columnist says music is *enough* for creativity, not that it is *required*. Pointing out that people can be creative without music agrees with everything the columnist said.

**(C) No Impact.** If live music or a phone speaker also raises theta waves, that is perfectly consistent with the argument. It would only widen the conclusion, not undermine it.

**(D) Correct.** The rule is creativity → more theta waves. The columnist runs it backward: more theta waves → creativity. Ask, "Could theta waves rise without creativity showing up?" If yes, music can raise theta waves and leave you no more creative than before. A fever comes with a rising temperature, but warming up in a sauna does not give you a fever.

**(E) Bad Description.** This one is close, so check the wording. The evidence and conclusion are about an *increase* in theta waves. (E) is about people having *low levels* of them. Someone could start with moderate theta levels, get an increase from music, and still not be creative. The gap is whether an increase guarantees creativity, which (D) states directly; a claim about baseline levels does not capture it.

## PT121-S4-Q17 | Flaw | C

**Modelled on:** PT120-S3-Q8 (a factor is not the only factor), PT141-S4-Q3 (anti-causal objections).

> A large amount of rainfall in April and May typically leads to an increase in the mosquito population and thus to an increased threat of encephalitis. People cannot change the weather. Thus people cannot decrease the threat of encephalitis.
>
> The reasoning in the argument above is flawed in that the argument
>
> (A) takes for granted that because one event precedes another the former must be the cause of the latter
> (B) presumes, without providing justification, that a certain outcome would be desirable
> (C) ignores the possibility that a certain type of outcome is dependent on more than one factor
> (D) takes for granted that a threat that is aggravated by certain factors could not occur in the absence of those factors
> (E) draws a conclusion about what is possible from a premise about what is actually the case

### Argument Breakdown

**Conclusion:** People cannot decrease the threat of encephalitis.

**Evidence:** Heavy spring rain increases mosquitoes and so increases the threat. People cannot change the weather.

**Evaluate:** Grant both premises. Rain is one thing that drives the threat, and we cannot control rain. Does that leave us with no way to reduce the threat? What about draining standing water, spraying for mosquitoes, using nets, or a vaccine? The argument treats one uncontrollable cause as if it were the only lever. If the threat depends on other things too, we can push on those.

**Goal:** Find the answer saying the threat depends on more than just the rainfall.

### Choice Notes

**(A) Wrong Flaw.** The link from rain to mosquitoes to encephalitis is given as a premise ("typically leads to"). The argument does not infer that link from the order of events, so there is no post hoc move to criticize.

**(B) Out of Scope.** Nothing in the argument depends on whether a lower threat is desirable. Obviously it is, but the question is whether it is possible.

**(C) Correct.** The threat may depend on rainfall *and* on mosquito control, standing water, protection from bites and more. If so, being unable to change the weather does not stop us from lowering the threat through the other factors. One factor we cannot control is not every factor.

**(D) Not Assumed.** The argument does not claim encephalitis disappears without heavy rain. Even if the threat existed in dry years too, the author would still conclude that it cannot be reduced. Negate (D) and nothing changes.

**(E) Bad Description.** "People cannot change the weather" is already a premise about what is possible. The argument moves from one claim about possibility to another. The problem is the missing factors, not a jump from actual to possible.

## PT122-S1-Q20 | Flaw | B

**Modelled on:** PT147-S1-Q6 (wrong group observed), PT141-S4-Q3 (anti-causal).

> The people most likely to watch a televised debate between political candidates are the most committed members of the electorate and thus the most likely to have already made up their minds about whom to support. Furthermore, following a debate, uncommitted viewers are generally undecided about who won the debate. Hence, winning a televised debate does little to bolster one's chances of winning an election.
>
> The reasoning in the argument is most vulnerable to criticism because the argument fails to consider the possibility that
>
> (A) watching an exciting debate makes people more likely to vote in an election
> (B) the voting behavior of people who do not watch a televised debate is influenced by reports about the debate
> (C) there are differences of opinion about what constitutes winning or losing a debate
> (D) people's voting behavior may be influenced in unpredictable ways by comments made by the participants in a televised debate
> (E) people who are committed to a particular candidate will vote even if their candidate is perceived as having lost a televised debate

### Argument Breakdown

**Conclusion:** Winning a televised debate does little to help a candidate win the election.

**Evidence:** Most viewers already know whom they support, and the uncommitted viewers usually cannot say who won.

**Evaluate:** Every piece of evidence is about people who *watch* the debate. But a debate can reach voters who never saw it. The next day's headlines say "Smith wins debate," clips circulate, and friends talk about it. Undecided voters who skipped the debate could be swayed by that coverage. The argument checks only the direct audience and concludes about the debate's whole effect.

**Goal:** Look for a way winning could help through people other than the viewers the author examined.

### Choice Notes

**(A) No Impact.** If an exciting debate raises turnout, that boosts voting generally. It does not say more of those voters choose the debate's winner, so it does not show that winning helps.

**(B) Correct.** Non-watchers can learn who won through news reports. If those reports shape their votes, winning a debate can matter a lot even though the viewers themselves are committed or confused. This names exactly the group the evidence left out.

**(C) Strengthens, if anything.** Disagreement over who won fits the author's point that uncommitted viewers are unsure of the winner. If anything, it makes "winning" seem less able to move votes.

**(D) No Impact.** Unpredictable effects do not favor the winner. To weaken the conclusion, we need a reason that *winning* helps, not just a reason that something unpredictable happens.

**(E) Strengthens, if anything.** Committed voters sticking with their candidate after a loss supports the claim that the debate result does little to change votes.

## PT122-S2-Q5 | Flaw | A

**Modelled on:** PT154-S1-Q12 (ad hominem, "you do it too"), PT155-S1-Q20 (rebuttal flaws).

> Letter to the editor: Middle-class families in wealthy nations are often criticized for the ecological damage resulting from their lifestyles. This criticism should not be taken too seriously, however, since its source is often a movie star or celebrity whose own lifestyle would, if widely adopted, destroy the environment and deplete our resources in a short time.
>
> The reasoning in the letter to the editor is vulnerable to criticism in that it
>
> (A) criticizes a characteristic of the people giving an argument rather than criticizing the argument itself
> (B) takes failure to act consistently with a belief as an indication of the sincerity with which that belief is held
> (C) presumes that a viewpoint must be unreasonable to accept simply because some of the grounds advanced to support it do not adequately do so
> (D) fails to recognize that evidence advanced in support of a conclusion actually undermines that conclusion
> (E) generalizes about the behavior of all people on the basis of the behavior of a few
>
### Argument Breakdown

**Conclusion:** The criticism of middle-class families' ecological damage should not be taken too seriously.

**Evidence:** The critics are often celebrities whose own lifestyles are far more damaging.

**Evaluate:** Suppose the celebrities really are hypocrites. Does that make middle-class lifestyles any less damaging? No. A smoker who tells you smoking is bad for you is still right. The letter answers the criticism by pointing at the critics, and never says a word about whether the damage is real.

**Goal:** Expect the ad hominem answer: rejecting a claim because of something about the people making it.

### Choice Notes

**(A) Correct.** The letter attacks the critics' lifestyles, not the substance of their criticism. Whether the critics live up to their own standard does not affect whether middle-class lifestyles cause ecological damage. This is the "you do it too" version of ad hominem.

**(B) Bad Description.** This tempts because the letter does point to inconsistency between the celebrities' words and their lives. But the letter never draws a conclusion about how *sincerely* they hold their views. It uses the inconsistency to dismiss the criticism, which is (A).

**(C) Bad Description.** The letter never examines the critics' grounds at all, adequate or not. It dismisses the criticism by looking at who makes it.

**(D) Out of Scope.** No evidence in the letter backfires on its conclusion. The celebrities' lifestyles are a different topic from middle-class families' damage.

**(E) Not Sampling.** The letter does not generalize from a few people to everyone. It describes one group of critics and then dismisses their argument.

## PT122-S4-Q6 | Flaw | A

**Modelled on:** PT107-S4-Q18 (could be vs is), PT120-S3-Q8 (alternate explanation).

> The simultaneous and apparently independent development in several ancient cultures of a myth of creatures who were half human and half horse parallels the increased use of horses in these cultures. But despite the nobility and gentleness traditionally ascribed to the horse, the mythical half-horse, half-humans were frequently portrayed as violent and savage. Many human cultures use myth to express unconscious thoughts, so these mythical creatures obviously reflect people's unconscious fear of the horse.
>
> The reasoning in the argument is flawed because the argument
>
> (A) fails to show that the mythical creature mentioned represents the horse in people's minds
> (B) fails to consider that people might have good reason to fear horses
> (C) confuses the expression of unconscious thoughts with the suppression of them
> (D) fails to demonstrate that the myth was not borrowed from one of the cultures by the others
> (E) fails to explain why people use myth for the expression of unconscious thoughts
>
### Argument Breakdown

**Conclusion:** The violent half-horse, half-human creatures reflect people's unconscious fear of the horse.

**Evidence:** The myths arose as these cultures used horses more. The creatures were savage even though horses were thought noble and gentle. Many cultures use myth to express unconscious thoughts.

**Evaluate:** Grant that the myth expresses some unconscious fear. Fear of *what*? The creature is half human. It might stand for a person on horseback: the mounted raiders who arrived as horses spread. Then the myth would reflect fear of armed riders, not of horses. The argument assumes the creature means "horse" without showing it.

**Goal:** Look for the gap between "the creature is part horse" and "the creature stands for the horse."

### Choice Notes

**(A) Correct.** For the creatures to reveal a fear *of the horse*, they must represent the horse in people's minds. They might represent people, riders or something else entirely. The argument never shows which, yet its conclusion depends on it.

**(B) Not an Objection.** Whether the fear is reasonable does not matter. A fear can be both justified and unconscious. This would not cast doubt on the claim that the myth expresses that fear.

**(C) Bad Description.** The argument speaks only of myths *expressing* unconscious thoughts. It never mentions suppression, so it cannot confuse the two.

**(D) Out of Scope.** The stimulus calls the developments "apparently independent." Even if one culture borrowed the myth, the borrowed version could still express fear of horses. Borrowing does not touch the gap between creature and horse.

**(E) Out of Scope.** The argument relies on the fact that myths express unconscious thoughts. It does not need to explain *why* they do. An answer asking for more explanation of a premise is not the flaw.

## PT122-S4-Q12 | Flaw | A

**Modelled on:** PT154-S1-Q9 (two conditionals, contrapositive), PT101-S3-Q25 (assumption prefixes).

> Politician: The huge amounts of money earned by oil companies elicit the suspicion that the regulations designed to prevent collusion need to be tightened. But just the opposite is true. If the regulations designed to prevent collusion are not excessively burdensome, then oil companies will make profits sufficient to motivate the very risky investments associated with exploration that must be made if society is to have adequate oil supplies. But recent data show that the oil industry's profits are not the highest among all industries. Clearly, the regulatory burden on oil companies has become excessive.
>
> The reasoning in the politician's argument is most vulnerable to criticism on the grounds that the argument
>
> (A) fails to justify its presumption that profits sufficient to motivate very risky investments must be the highest among all industries
> (B) attacks the character of the oil companies rather than the substance of their conduct
> (C) fails to justify its presumption that two events that are correlated must also be causally related
> (D) treats the absence of evidence that the oil industry has the highest profits among all industries as proof that the oil industry does not have the highest profits among all industries
> (E) illicitly draws a general conclusion from a specific example that there is reason to think is atypical
>
### Argument Breakdown

**Conclusion:** The regulatory burden on oil companies is excessive.

**Evidence:** Not excessively burdensome → profits sufficient to motivate risky exploration. Oil profits are not the highest of any industry.

**Evaluate:** The contrapositive is valid: profits *not* sufficient → regulations excessive. So the politician needs "profits not sufficient." What the data give us is "profits not the highest." Those are different. Profits can fall short of first place and still be plenty to fund risky exploration. The second-best paid job in a company can still pay the rent. The argument works only if "sufficient" requires "highest."

**Goal:** Look for the hidden link: sufficient profits must be the highest profits.

### Choice Notes

**(A) Correct.** To get from "not the highest" to "not sufficient," the politician must assume sufficient profits have to be the highest among all industries. Nothing justifies that. Negate it (sufficient profits need not be the highest) and the conclusion no longer follows.

**(B) Bad Description.** The politician does not criticize oil companies at all. The argument defends them from tighter regulation.

**(C) Wrong Flaw.** The argument is conditional, not causal. It does not infer a cause from two things occurring together.

**(D) Bad Description.** The politician has actual data: profits are not the highest. That is evidence, not an absence of evidence. The problem is what the data are taken to show.

**(E) Not Sampling.** The data concern the whole oil industry compared with other industries. No single example is generalized.

## PT127-S1-Q4 | Flaw | C

**Modelled on:** PT107-S4-Q18 (could be vs is), PT113-S2-Q3 (negate the "takes for granted" content).

> Columnist: Donating items to charity may be a sign of generosity, but any generosity it may demonstrate is rarely a permanent virtue, since most donors make donations only intermittently.
>
> Which one of the following most accurately describes a flaw in the columnist’s argument?
>
> (A) The argument takes for granted that truly generous people are the most virtuous.
> (B) The argument attacks the character of those whose values are different from those of the columnist.
> (C) The argument takes for granted that a character trait is present only when manifested.
> (D) The argument generalizes from too small a sample of cases.
> (E) The argument takes for granted that most people donate out of generosity.

Bank glitch: the stem's apostrophe is damaged in the bank file ("columnist�s"). It is quoted here with a standard apostrophe; repair the bank before load.

### Argument Breakdown

**Conclusion:** The generosity shown by donating is rarely a permanent virtue.

**Evidence:** Most donors give only from time to time.

**Evaluate:** Does a trait vanish between the moments it shows? A pianist is still a pianist while asleep. A kind person is still kind while waiting for the bus. Donors who give now and then could be generous all the time and simply express it now and then. The columnist reads "intermittent giving" as "intermittent generosity."

**Goal:** Look for the assumption that a trait exists only while it is being acted on.

### Choice Notes

**(A) Out of Scope.** Ranking generosity against other virtues has nothing to do with whether the generosity is permanent.

**(B) Bad Description.** The columnist does not attack anyone's character or contrast the donors' values with his own. He draws a conclusion about how lasting their generosity is.

**(C) Correct.** The columnist moves from "donors give only intermittently" to "their generosity is rarely permanent." That works only if generosity exists only when it shows up in a donation. Negate it, so that a trait can persist between its displays, and the argument falls apart.

**(D) Not Sampling.** The evidence is about *most* donors. There is no small sample here; the problem is what intermittent giving says about character.

**(E) Not Assumed.** The columnist hedges: donating "may be" a sign of generosity, and "any generosity it may demonstrate" is the subject. He does not need most donors to be generous. Negate (E) and his reasoning about permanence is unchanged.

## PT127-S1-Q12 | Flaw | B

**Modelled on:** PT113-S2-Q3 (prefix test on assumption answers), PT101-S3-Q25 (new concept in the conclusion).

> Many people say that the press should not pry into the personal lives of private individuals. But the press has the right to publish any story of interest to the public unless that story is libelous. So, if a story about a private individual is not libelous, the press has an obligation to publish it, for such information is clearly of interest to the public.
>
> The argument’s reasoning is vulnerable to criticism on the grounds that the argument presumes, without giving warrant, that
>
> (A) the press can publish nonlibelous stories about private individuals without prying into their personal lives
> (B) one’s having a right to do something entails one’s having an obligation to do it
> (C) the publishing of information about the personal lives of private individuals cannot be libelous
> (D) if one has an obligation to do something then one has a right to do it
> (E) the press’s right to publish always outweighs the individual’s right not to be libeled

### Argument Breakdown

**Conclusion:** If a story about a private individual is not libelous, the press has an *obligation* to publish it.

**Evidence:** The press has the *right* to publish any story of public interest unless it is libelous, and stories about private individuals are of public interest.

**Evaluate:** The premises deliver a right. The conclusion announces an obligation. Those are different. You have the right to paint your house purple; you have no duty to. Watch for a word in the conclusion that never appears in the evidence. "Obligation" is that word here.

**Goal:** Look for the assumption that a right brings an obligation with it.

### Choice Notes

**(A) Not Assumed.** Whether publishing requires prying does not matter to the argument. Negate it (publishing such stories does involve prying) and the author still reaches the same conclusion, since he has brushed the prying objection aside.

**(B) Correct.** This bridges the gap exactly. The evidence establishes a right to publish; the conclusion claims an obligation to publish. Negate (B) (having a right does not entail an obligation) and the conclusion no longer follows.

**(C) Not Assumed.** The conclusion is conditional: *if* a story is not libelous. The author allows that some stories about private lives might be libelous.

**(D) Backwards.** This runs the link the wrong way: obligation → right. The argument needs right → obligation.

**(E) Out of Scope.** Libelous stories are set aside by the conclusion's "if not libelous" condition. No weighing of the two rights is involved.

## PT128-S2-Q9 | Flaw | C

**Modelled on:** PT110-S2-Q11 (best way vs only way), PT154-S2-Q12 (status quo defense).

> A proposed amendment would allow the city council to decide that certain city elections be conducted solely by mail. But voting is a sacred right in democracies, one that has always been exercised by voting in person and not by mail. Therefore, voting by mail should not be allowed, and the proposed amendment should be rejected.
>
> The reasoning in the argument is most vulnerable to criticism on the grounds that the argument
>
> (A) presumes, without providing justification, that the right to vote is not violated unless elections are conducted solely by mail
> (B) presumes, without providing justification, that if citizens have always had a certain legal right, they will continue to have that right in the future
> (C) presents an appeal to tradition as the only reason for rejecting the proposal
> (D) fails to consider the possibility that, even if it gains the power to do so, the city council might never require voting by mail
> (E) has a premise that is logically incompatible with the main conclusion

### Argument Breakdown

**Conclusion:** Voting by mail should not be allowed, so the amendment should be rejected.

**Evidence:** Voting is a sacred right, and it has always been exercised in person.

**Evaluate:** Grant that voting is sacred. Why does that rule out mail? The only reason given is that voting has always been done in person. But "we have always done it this way" is not a reason it must stay that way. Elections once used a show of hands; switching to secret ballots did not betray the right to vote. The argument needs some reason mail voting harms the right, and gives none.

**Goal:** Find the answer saying the author relies only on tradition.

### Choice Notes

**(A) Bad Description.** The author never says the right is violated only when elections are held solely by mail. This garbles the argument rather than describing it.

**(B) Out of Scope.** Whether the right will continue has nothing to do with *how* it should be exercised. The author takes the right as given; the question is mail vs in person.

**(C) Correct.** The sole support for rejecting mail voting is that voting has "always" been done in person. That is an appeal to tradition. "Sacred right" tells us voting matters; it does not tell us mail voting threatens it.

**(D) Not an Objection.** The author argues mail voting should not be *allowed* at all. Saying the council might never use the power does not touch that reasoning. The argument would be just as flawed if the council certainly would use it.

**(E) Contradiction.** The premises and conclusion fit together without conflict. Voting has been in person, and the author wants it to stay that way. The flaw is weak support, not a contradiction.

## PT134-S1-Q5 | Flaw | A

**Modelled on:** PT134-S3-Q6 (correlation, reverse cause), PT141-S4-Q3 (anti-causal).

> Kennel club members who frequently discipline their dogs report a higher incidence of misbehavior than do members who rarely or never discipline their dogs. We can conclude from this that discipline does not improve dogs' behavior; on the contrary, it encourages misbehavior.
>
> The argument is flawed in that it fails to consider the possibility that
>
> (A) dogs' misbehavior is the cause of, rather than the result of, frequent discipline
> (B) dogs learn from past experience how their owners are likely to react to misbehavior
> (C) discipline does not cause misbehavior on the part of animals other than dogs
> (D) kennel club members tend to be more skilled at raising dogs than are other dog owners
> (E) kennel club members are more likely to use discipline than are other dog owners

### Argument Breakdown

**Conclusion:** Discipline does not improve dogs' behavior; it encourages misbehavior.

**Evidence:** Members who discipline often report more misbehavior than members who rarely or never discipline.

**Evaluate:** This is a correlation: more discipline goes with more misbehavior. The author concludes discipline causes misbehavior. Whenever you see that move, try the reverse. Which dogs get disciplined a lot? The badly behaved ones. Owners of calm dogs rarely need to discipline them. The misbehavior could be causing the discipline.

**Goal:** Expect reverse causation: misbehavior leads to discipline.

### Choice Notes

**(A) Correct.** If misbehaving dogs are the ones that get disciplined often, the correlation is explained without discipline causing anything. It could even be that discipline helps, and those dogs would be worse without it.

**(B) Out of Scope.** Dogs learning how owners react does not explain why frequently disciplined dogs misbehave more, and it does not offer a rival cause.

**(C) Out of Scope.** The conclusion is about dogs. Other animals do not matter.

**(D) Irrelevant Comparison.** The study compares kennel club members with each other. How they compare with other dog owners tells us nothing about the correlation inside the club.

**(E) Irrelevant Comparison.** Same problem as (D). Members versus nonmembers is not the comparison the argument rests on.

## PT134-S3-Q2 | Flaw | E

**Modelled on:** PT143-S3-Q18 (untriggered conditional), PT113-S2-Q3 (diagram the rule).

> Principle: If you sell an item that you know to be defective, telling the buyer that the item is sound, you thereby commit fraud. Application: Wilton sold a used bicycle to Harris, knowing very little about its condition. Wilton told Harris that the bicycle was in good working condition, but Harris soon learned that the brakes were defective. Wilton was therefore guilty of fraud.
>
> The application of the principle is most vulnerable to criticism on the grounds that
>
> (A) the application fails to establish whether Wilton was given the opportunity to repair the brakes
> (B) the application fails to indicate how much money Wilton received for the bicycle
> (C) the application uses the word “defective” in a sense that is crucially different from how it is used in the statement of the principle
> (D) Harris might not have believed Wilton’s statement about the bicycle’s condition
> (E) asserting something without justification is not the same as asserting something one knows to be false

### Argument Breakdown

**Conclusion:** Wilton committed fraud.

**Evidence:** Principle: sell an item you *know* is defective + tell the buyer it is sound → fraud. Wilton knew very little about the bicycle, said it was in good condition, and the brakes turned out to be defective.

**Evaluate:** Check each part of the trigger. Sold an item: yes. Told the buyer it was sound: yes. *Knew* it was defective: no. The stimulus says Wilton knew very little about its condition. He spoke carelessly, but the principle only covers sellers who know the item is bad. Without that piece, the rule never fires.

**Goal:** Look for the missing knowledge condition.

### Choice Notes

**(A) Out of Scope.** The principle says nothing about a chance to repair. Fraud under it depends on knowledge and the seller's statement.

**(B) Out of Scope.** The price is irrelevant to whether the principle applies. An answer asking for a number is almost never the flaw.

**(C) Not Equivocation.** "Defective" means the same thing in both places: the item does not work properly. The brakes were defective in that sense.

**(D) Out of Scope.** The principle does not require the buyer to believe the seller. Fraud is defined by what the seller knows and says.

**(E) Correct.** Wilton asserted the bicycle was sound without good reason to think so. That is not the same as asserting it while *knowing* it was defective, which is what the principle requires. The application treats careless assertion as knowing falsehood.

## PT134-S3-Q4 | Flaw | B

**Modelled on:** PT113-S2-Q3 (illegal negation), PT124-S2-Q11 (necessary vs sufficient).

> Journalist: A manufacturers’ trade group that has long kept its membership list secret inadvertently sent me a document listing hundreds of manufacturing companies. A representative of the trade group later confirmed that every company listed in the document does indeed belong to the trade group. Because Bruch Industries is not listed on the document, it is evidently not a member of the trade group.
>
> The journalist’s reasoning in the argument is flawed in that the journalist
>
> (A) gives no reason to think that Bruch Industries would want to belong to the trade group
> (B) does not present any evidence that the document names every member of the trade group
> (C) does not explain how it is that the trade group could have inadvertently sent out a secret document
> (D) presents no reason why Bruch Industries would not want its membership in the trade group to be known
> (E) takes for granted the accuracy of a statement by a representative who had a reason to withhold information

### Argument Breakdown

**Conclusion:** Bruch Industries is not a member.

**Evidence:** Every company on the list is a member. Bruch is not on the list.

**Evaluate:** The rule is: on the list → member. The journalist reasons: not on the list → not a member. That is the illegal negation. The list could be partial. A class photo shows only students, but a student absent that day is still a student. Being listed is enough to prove membership; it is not required for it.

**Goal:** Look for the formal answer (treating sufficient as necessary) or the conversational one (the list may not be complete).

### Choice Notes

**(A) Out of Scope.** Whether Bruch wants to belong is beside the point. The question is whether the document proves it does not.

**(B) Correct.** The conclusion requires the list to be complete. If the document names only some members, Bruch's absence proves nothing. The journalist never shows the list is complete.

**(C) Out of Scope.** How the document was sent has no bearing on whether it lists every member.

**(D) Out of Scope.** Bruch's possible reasons for secrecy do not affect what the list shows.

**(E) No Impact.** This tempts because the representative did have a reason for secrecy. But the representative only confirmed that the listed companies are members, and the journalist's inference about Bruch goes wrong even if that confirmation is perfectly accurate. The gap is the list's completeness.

## PT136-S2-Q1 | Flaw | E

**Modelled on:** PT154-S2-Q12 (false choice), PT150-S2-Q4 (plan).

> Mayor: There has been a long debate in city council about how to accommodate projected increases in automobile traffic. Today, our choice is clear: either we adopt my plan to build a new expressway, or we do nothing. Doing nothing is not a viable option because our existing system of roads would be in gridlock within ten years given even a conservative estimate of future traffic levels. City council should therefore adopt my plan.
>
> The reasoning in the mayor's argument is most vulnerable to which one of the following criticisms?
>
> (A) It bases a projection only on conservative estimates rather than considering a wider range of estimates.
> (B) It takes for granted that the options it considers are mutually exclusive.
> (C) It fails to consider the possibility that the rate of increase in traffic will start to diminish after ten years.
> (D) It fails to address the issue of the cost of traffic gridlock to the city's economy.
> (E) It presents a choice that is limited to two options, without giving reasons for not considering any other options.

### Argument Breakdown

**Conclusion:** The council should adopt the mayor's expressway plan.

**Evidence:** The only options are the expressway or nothing, and doing nothing leads to gridlock.

**Evaluate:** Grant that doing nothing is a bad idea. Does that make the expressway the answer? Only if there are no other options. What about better public transit, widening existing roads, or changing traffic signals? The mayor narrows the menu to two items, rejects one, and declares the other the winner.

**Goal:** Expect the false choice answer: the argument ignores other options.

### Choice Notes

**(A) Strengthens, if anything.** A conservative estimate already predicts gridlock. Higher estimates would make doing nothing look even worse.

**(B) Bad Description.** Building an expressway and doing nothing really are mutually exclusive, so taking that for granted is fine. The problem is not that the two options overlap but that they are *not the only ones*. Watch the difference between "exclusive" and "exhaustive."

**(C) No Impact.** Gridlock arrives within ten years either way. A slower increase afterward does not rescue the do-nothing option or help any alternative.

**(D) Out of Scope.** The economic cost of gridlock would, if anything, add to the case against doing nothing. It does not reveal the missing options.

**(E) Correct.** The mayor offers only two choices and never explains why others are off the table. Eliminating one of two options proves the other only if those two are all there are.

## PT136-S2-Q8 | Flaw | B

**Modelled on:** PT155-S1-Q20 (rebuttal of a rebuttal), PT154-S1-Q12 (two-speaker rebuttal flaws).

> Robinson: Wexell says that the museum wasted its money in purchasing props and costumes from famous stage productions, because such items have no artistic significance outside the context of a performance. But many of the props and costumes are too old and fragile for use in a performance. So clearly, the museum did not waste its money, for displaying these items is the only way of making them available to the public.
>
> The reasoning in Robinson's argument is most vulnerable to criticism on the grounds that it
>
> (A) offers anecdotal evidence insufficient to support a general claim
> (B) gives reasons that do not address the point made in Wexell's argument
> (C) attacks the person making the argument rather than the substance of the argument
> (D) concludes that a claim is false merely on the grounds that the evidence for it is insufficient
> (E) takes a condition that is sufficient for the conclusion to be true as one that is necessary for the conclusion to be true

### Argument Breakdown

**Wexell's claim:** The money was wasted because the props and costumes have no artistic significance outside a performance.

**Robinson's conclusion:** The money was not wasted.

**Robinson's evidence:** The items are too fragile to perform with, so display is the only way the public can see them.

**Evaluate:** Wexell's point is that the items mean nothing artistically once they are off the stage. Robinson replies that display is the only way to show them. Grant that. Does it show the items have artistic significance on display? No. If Wexell is right, displaying them is the only way to show the public something without artistic value. Robinson answered a question Wexell never asked.

**Goal:** Look for the answer saying Robinson's reasons miss Wexell's point.

### Choice Notes

**(A) Bad Description.** Robinson's evidence is about these particular props and costumes. He is not generalizing from anecdotes.

**(B) Correct.** Wexell's argument turns on artistic significance outside a performance. Robinson talks only about availability. Even if display is the only way to show the items, that does not answer whether they are worth showing.

**(C) Not Ad Hominem.** Robinson does not mention anything about Wexell personally.

**(D) Bad Description.** Robinson never claims Wexell's evidence is insufficient. He offers new reasons of his own, which happen to miss the point.

**(E) Wrong Flaw.** "The only way" might suggest necessary vs sufficient, but there is no reversed conditional here. The trouble is relevance, not a scrambled condition.

## PT136-S4-Q1 | Flaw | A

**Modelled on:** PT147-S1-Q6 (unrepresentative sample).

> According to the official results of last week's national referendum, 80 percent voted in favor of the proposal. But those results must be rigged. Everyone I know voted against the proposal, which is clear evidence that most people voted against it.
>
> Which one of the following most accurately describes a flaw in the reasoning of the argument?
>
> (A) The argument uses evidence drawn from a sample that is unlikely to be representative of the general population.
> (B) The argument presumes the truth of the conclusion that it sets out to prove.
> (C) The argument rejects a claim by attacking the proponents of the claim rather than addressing the claim itself.
> (D) The argument fails to make a needed distinction between how people should have voted and how they actually voted.
> (E) The argument defends a claim solely on the grounds that most people believe it.

### Argument Breakdown

**Conclusion:** The official results were rigged; most people voted against the proposal.

**Evidence:** Everyone the speaker knows voted against it.

**Evaluate:** The people you know are not a random slice of the country. They tend to live near you, work with you and share your views. A national vote can easily go 80 to 20 while your whole circle sits in the 20 percent. The speaker's friends are a sample of the wrong population.

**Goal:** Expect the sampling answer: the speaker's acquaintances are not representative.

### Choice Notes

**(A) Correct.** "Everyone I know" is a sample chosen by who the speaker happens to know, not by any method that reflects the nation. It is likely to share the speaker's views, so it cannot show how the country voted.

**(B) Bad Description.** The premise (the speaker's acquaintances voted no) is different from the conclusion (most people voted no). The argument is weak, but not circular.

**(C) Not Ad Hominem.** The speaker attacks the results, not the people who announced them or voted for the proposal.

**(D) Out of Scope.** The argument is about how people actually voted. "Should" never enters it.

**(E) Wrong Flaw.** The speaker is not appealing to popular belief. If anything, he rejects the majority result. His mistake is the sample, not an appeal to what most people think.

## PT138-S3-Q5 | Flaw | A

**Modelled on:** PT120-S3-Q8 (a factor is not the only factor), PT128-S3-Q14 ("a" vs "the only").

> Editorialist: Many professional musicians claim that unauthorized music-sharing services, which allow listeners to obtain music for free, rob musicians of royalties. While it is true that musicians are deprived of royalties they deserve, music-sharing services are not to blame since record companies, publishers, managers, and other intermediaries take an inequitably large cut of the revenues from music sales.
>
> The reasoning in the editorialist’s argument is most vulnerable to criticism on the grounds that the argument
>
> (A) concludes that one party is not blameworthy merely because another party is blameworthy
> (B) attempts to promote a particular behavior simply by showing that many people engage in that behavior
> (C) attacks a position based solely on the character of the people who hold that position
> (D) tries to show that a position is false simply by pointing out an undesirable consequence of holding that position
> (E) treats a necessary condition for blameworthiness as though it were a sufficient condition for blameworthiness

### Argument Breakdown

**Conclusion:** Music-sharing services are not to blame for musicians' lost royalties.

**Evidence:** Intermediaries take an unfairly large cut of music revenue.

**Evaluate:** Grant that the intermediaries take too much. Can the sharing services still be to blame? Of course. Two roommates can both have eaten the cake. Blame is not a single prize that goes to one party. The editorialist finds one culprit and acquits the other without examining it.

**Goal:** Look for the answer saying one party's blame does not clear another.

### Choice Notes

**(A) Correct.** The only reason given for clearing the sharing services is that the intermediaries are at fault. Both can contribute to musicians' losses, so blaming one does not excuse the other.

**(B) Out of Scope.** The editorialist does not promote any behavior by citing its popularity.

**(C) Not Ad Hominem.** The editorialist does not attack the musicians' character. He grants that they are deprived of royalties.

**(D) Bad Description.** No undesirable consequence of the musicians' view is used against it.

**(E) Wrong Flaw.** There is no conditional rule about blameworthiness here to scramble. The error is treating blame as if only one party could have it.

## PT139-S1-Q20 | Flaw | B

**Modelled on:** PT144-S3-Q15 (aggregate vs subgroup), PT120-S4-Q23 (do the arithmetic).

> Medical reporter: Studies have consistently found that taking an aspirin a day thins the blood slightly, thereby helping to prevent or reduce the severity of heart disease. Since heart disease is one of the most common types of ill health in industrialized nations, most people in such nations would therefore be in better health if they took an aspirin a day.
>
> The reasoning in the doctor's argument is most vulnerable to criticism on which one of the following grounds?
>
> (A) It takes for granted that if medication can reduce the severity of heart disease, it can also prevent some cases of heart disease.
> (B) It overlooks the possibility that even if a disease is one of the most common in a nation, most people in that nation are not in significant danger of developing that disease.
> (C) It overlooks the possibility that preventing or reducing the severity of heart disease has little or no effect on any of the other most common diseases in industrialized nations.
> (D) It fails to address the possibility that taking an aspirin a day is not the single most effective measure for preventing heart disease.
> (E) It fails to address the possibility that the studies on the beneficial effects of aspirin were conducted only in industrialized nations.

Stem note: the bank stem says "the doctor's argument" while the speaker is a medical reporter. That matches the bank's own wording; it is quoted as found.

### Argument Breakdown

**Conclusion:** *Most* people in industrialized nations would be healthier taking an aspirin a day.

**Evidence:** Aspirin helps prevent or lessen heart disease, and heart disease is one of the most common illnesses in those nations.

**Evaluate:** "One of the most common" is a ranking, not a majority. Put numbers on it. Say heart disease is the top illness and 15 people in 100 will ever face it. Aspirin might help those 15. What about the other 85? They gain nothing from protection against a disease they were never going to get. The argument jumps from "common disease" to "most people benefit."

**Goal:** Look for the gap between a disease being common and most people being at risk of it.

### Choice Notes

**(A) Not Assumed.** The premise already says aspirin helps *prevent or reduce* heart disease. The argument does not need to infer prevention from reduced severity.

**(B) Correct.** A disease can top the list and still threaten only a minority. If most people are not at significant risk, most people would not be healthier from protection against it. That breaks the step to "most people."

**(C) Not an Objection.** The argument never claims aspirin helps with other diseases. People helped against heart disease are healthier even if nothing else changes.

**(D) Out of Scope.** Aspirin does not have to be the *best* measure to make people healthier. A good measure can still help.

**(E) Strengthens, if anything.** The conclusion is about industrialized nations. Studies done there would fit the conclusion, not undermine it.

## PT139-S4-Q22 | Flaw | E

**Modelled on:** PT113-S2-Q3 (illegal negation), PT151-S4-Q23 (formal and conversational answers).

> If the magazine's circulation continues to rise as it has over the last ten years, in another ten years it will be the largest-selling martial arts magazine in the world. Unfortunately, it has now become clear that the magazine's publisher will not allow the managing editor to make the changes she has proposed, and without these changes, the magazine's circulation will not rise as quickly over the next ten years as it has over the last ten. So the magazine will not be the largest-selling martial arts magazine ten years from now.
>
> The argument's reasoning is flawed because the argument
>
> (A) identifies some changes required for the magazine's circulation to continue its rapid increase and concludes from this that no other changes are needed
> (B) equates a reduction in the rate at which the magazine's circulation is increasing with a decline in the magazine's circulation
> (C) draws a conclusion that simply restates a claim that is presented in support of that conclusion
> (D) takes a single fact that is incompatible with a general claim as enough to show that claim to be false
> (E) treats an occurrence that will ensure a certain outcome as something that is required for that outcome

### Argument Breakdown

**Conclusion:** The magazine will not be the largest-selling martial arts magazine in ten years.

**Evidence:** Rise at the same rate → largest-selling. Without the editor's changes, circulation will not rise at that rate, and the changes will not happen.

**Evaluate:** Diagram it. Same rate → largest. We learn: not same rate. The author concludes: not largest. That is the illegal negation. The same rate *guarantees* the top spot, but the magazine could get there another way: a slower rise might still be enough if competitors shrink. Running a marathon in three hours guarantees you finish; finishing in four still counts.

**Goal:** Look for the formal answer: something sufficient treated as necessary.

### Choice Notes

**(A) Bad Description.** The author never says no other changes are needed. The argument is about what follows when the changes do not happen.

**(B) Bad Description.** The author says circulation will rise *less quickly*, not that it will fall. The argument keeps those apart; it just draws the wrong conclusion from the slower rise.

**(C) Bad Description.** The conclusion is not a restatement of a premise. It is drawn, badly, from the conditional.

**(D) Wrong Flaw.** There is no general claim refuted by a counterexample. The argument misuses a conditional.

**(E) Correct.** Continuing the past rate *ensures* the magazine becomes the largest. The argument treats it as *required*, so that missing the rate means missing the goal. Those are different, and the magazine might reach the top by some other path.
