update lr_explanation_steps t set body=v.nb, label=case when v.nl='' then t.label else v.nl end from (values
('53fcb575-8e3c-4cd6-861b-eb92df5bceae'::uuid,'3eff3679ce513f8907ef0d7923298971','The study measured two things. Speed at processing new information went up. Integrating new information with past information went down. The premise tells us integration matters more to management than speed, so the psychologist reads the trade as a loss.

But the conclusion is about overall management ability. Is managing only speed and integration? Hardly. Think about attention to detail, staying calm with a difficult client, or energy late in the day. And even on the two measured abilities, "integration matters more" does not tell us how big each change was.

Given that extra coffee hurt integration, how could we argue that it still did not impair overall management ability? Suppose the extra coffee also made those managers far more alert and focused in ways the study never measured. Or suppose the speed gain was huge and the integration loss was tiny. Either way, the gains could outweigh the integration loss, and overall ability would hold steady or even improve.

The psychologist jumps from two measured changes to a verdict about overall ability. That jump only works if nothing the coffee did in the experiment made up for the integration loss.','Evaluate','Evaluate'),
('b78d8539-5163-430b-b27f-22a233ace4ee'::uuid,'06b969dc897f74c3b9e84455e61e9c95','Look for a Defender: an answer ruling out the possibility that the extra coffee produced benefits, from the faster processing or from abilities the study did not measure, large enough to outweigh the integration loss. Negate the right answer and you should get our objection back: the extra coffee helped overall management in some way that more than made up for the loss.','Goal','Goal'),
('0e76c443-a2c4-4adc-9310-3cfe1103fc78'::uuid,'a106551545830b94e0aaf5c6eb4b8958','The information introduced by the chorus in a play is sometimes not consistent with the rest of the information in the play.','Evidence (since)','Evidence (since)'),
('64cfec38-2b0e-4301-8b93-4b272a491c89'::uuid,'3f7d9215c804b859beede4195b8ca4a1','Most of this stimulus is background. Chorus and narrator share a lot: each brings in a point of view not tied to any character, and each lets the author comment on the action and supply context. Then the pivot, "However," brings the actual argument: since the chorus sometimes introduces information inconsistent with the rest of the play, the chorus is not equivalent to the narrator.

That shape is "X and Y are not the same, since X does thing A." What has to be true for that to work? Y must not do thing A. If I said, "Max owns a Lebron jersey, so Max and Karen are not equally big Lebron fans," I would be assuming that Karen does not own one too. If Karen also owned one, the jersey would be something they share, not a difference.

Same here. The author is Assuming a Difference. If narrators can also introduce inconsistent information, inconsistency is a shared trait and cannot prove the two are different.','Evaluate','Evaluate'),
('3541bb89-c5f4-4fc9-b95a-6e01d01cc757'::uuid,'d59dfeed6324c3b9a3399e007c46ca0a','So let''s look for an answer saying that a narrator in a novel does not introduce information that is inconsistent with the rest of the novel. Negated, it should say narrators can do the same thing the chorus does.','Goal','Goal'),
('b2e8e91b-42f7-4831-b9ad-7c235b408b34'::uuid,'c2ee21d51f4a4d1a871b65ef79178f81','We could predict a Linking assumption like, "If transporting basic materials through space would be extremely costly, then it won''t be economically feasible to colonize Mars." But this argument is practical and real world, so the answer is more likely to defend against an objection than to spell out a link.

So let''s argue with it. Given that a colony needs tremendous quantities of basic materials on site, and that shipping those materials through space would cost a fortune, how could we argue that colonizing Mars could still be economically feasible?

We can''t get around the need for the materials. Can we get around shipping them through space? What if we find usable materials on Mars itself, so nothing has to make the trip? What if some future technology moves materials without conventional space transport?

Now accept that the materials really must be shipped at great cost. Is there still a way? Maybe the colony would pay for itself. Suppose Mars held a mineral so valuable that companies would gladly cover the shipping bill to mine it. Expensive is not the same as unaffordable when the payoff is big enough.','Evaluate','Evaluate'),
('11335347-84c9-48bf-8f02-a4104a507262'::uuid,'64b4e158506d1427a71edad4990bc636','Look for a Defender answer that shuts down one of these objections, saying something like:

"Mars cannot supply the materials itself."
"There is no cheaper way to get the materials there."
"The colony would not produce enough value to cover the cost."

Negate the right answer and it should hand us one of those objections.','Goal','Goal'),
('2112e6d7-0f77-4cc5-a82a-ad44bd21084d'::uuid,'f2d8d6193d9823cebe1477743c883927','If two stars are in the same distant galaxy, the difference in their distances from Earth is negligible.','Evidence','Evidence'),
('f8974692-c638-4c6e-8e57-5237e9b6455f'::uuid,'d98916752848e78f8029859c7274bc46','There are two moves here, so we can test each one.

Move one goes from the premise that the stars in one distant galaxy are all about the same distance from us to the claim that any significant difference in their apparent brightness comes from how brightly each star is actually burning. The distance part is reasonable. If one star is 10,000,000 light-years away and another is 10,000,050, the gap barely matters. But is distance the only thing that can make a star look dimmer? A cloud of dust in front of one star could dim it. Another star sitting right behind it, along our line of sight, could make it look brighter. So this move has some wiggle room.

Move two goes from that claim to the conclusion that we can find how actual brightness correlates with other characteristics by studying these stars. A correlation needs two things to compare. We now have a way to rank the stars by actual brightness. What do we compare that ranking with? Some other characteristic, such as color or size. And we have to be able to observe that characteristic from Earth, because that is where the study happens. If no other characteristic of these distant stars can be seen from here, we have brightness figures and nothing to line them up against.','Evaluate','Evaluate'),
('80145eb7-c868-4f62-a13a-49b7e59bc156'::uuid,'290d45f486cedcc70566318bcbaa80be','The answer could target either move. For move one, look for a Defender such as, "Nothing other than distance and actual brightness significantly affects how bright a distant star appears." For move two, look for an answer saying we can observe, from Earth, at least some characteristic of stars in distant galaxies besides their brightness. Negate that one and the plan has nothing to correlate brightness with.','Goal','Goal'),
('02d6150a-f77b-4cc0-915a-b5d1cd17553a'::uuid,'57a4313438ad6f31e06c611eee240326','These bovines were found in an arid region with people and no other large mammals. If there had been a natural source of water available to these bovines, then there would have been other large mammals in the area.','Evidence','Evidence'),
('24d6aff9-8e44-4be2-8be9-9fde247f1c8c'::uuid,'911bb055b6cde97804ecdab6fdee3549','There is a small inference to make with the premises first. We have a conditional:
```
Natural source of water available → other large mammals in the area
```
And we are told there were no other large mammals in the area. By the contrapositive, there was no natural source of water available to these bovines.

So the bovines were living in an arid region with people around and no natural water. The author concludes the bovines were domesticated: people were keeping them and bringing them water. That sounds like early herding, so the people were no longer only hunting and gathering.

How could we argue otherwise? Given that there was no natural water, how could wild bovines still have been there? Maybe bovines can go a long time on very little water, getting moisture from plants. Maybe the remains are of animals that wandered in during a drought and died, which would explain why remains were found at all. If wild bovines could plausibly be there without natural water, their presence proves nothing about domestication.','Evaluate','Evaluate'),
('28fcdfc5-cf41-4456-8dd5-1651a8049d7f'::uuid,'5805699fe83bd12f0c0ab65b772e998c','The argument makes a Linking move: no natural water, yet bovines were there, so people must have been keeping them. Look for an answer saying wild bovines would not be found in a region without natural water. That same answer defends against our objection; negate it and wild bovines could have been there on their own.

The second half of the conclusion also assumes that people who domesticated bovines were not exclusively hunter-gatherers, but that step is close to a definition.','Goal','Goal'),
('c0b527ac-8c98-416c-9627-6bf94d203b8a'::uuid,'47ea47258ea970ff9dbbd9c54fe640bf','The troubles from which a patient seeks relief do not have purely internal causes. They result in part from the patient''s relationships with other people.','Evidence','Evidence'),
('cb1ac25c-0240-4bce-9f4b-2cfe240c85b0'::uuid,'991caa71a863a8e4bd416d18df8ebe9f','The logic seems to be: since the troubles are partly caused by relationships, the patient can''t heal unless the therapist focuses on changing those relationships. So the author is assuming something like, "If a problem is partly caused by X, then solving it requires addressing X."

Is that true? Not always. A headache might be partly caused by a noisy office, yet a painkiller can still end it without anyone touching the noise. Given that the troubles are partly relational, how could we argue the therapist doesn''t have to focus on relationships? Maybe working on the internal causes alone, such as raising self-esteem or easing anxiety, does enough good that the patient heals, even though the relationships never changed.','Evaluate','Evaluate'),
('ea1ad4ea-d0c6-4783-b43d-fa8052cf888b'::uuid,'77045f73e9c48559d80e2eec1c76b45a','Whenever a conclusion says, "to get X, you must do Y," the author is assuming that nothing other than Y will get you X. Here, that means no route to healing skips the relationships. So look for an answer saying something like, "A patient can''t be healed by working on the internal causes alone." Negate it and you get our objection back.

Be careful with the reverse idea, that Y is guaranteed to work. A "must" claims Y is required, not that Y is enough.','Goal','Goal'),
('5958ba1d-859e-46a3-a562-d3538f2c49e6'::uuid,'fa5dae2db9fd5d625df28bb969188ef4','We have a new term in the conclusion: "decreased revenues." The evidence never mentions revenue. It only talks about a ratings drop for first-run episodes. So there is a missing link: a ratings drop for first-run episodes can lead to decreased revenues for the network.

Picture how this works. A hit comedy airs new episodes on its network every Sunday night. The producers sell reruns to other stations while the show is still running, and they make a lot of money doing it. But now fans can get their fix from reruns any night of the week, so fewer of them tune in on Sunday for the new episode. Ratings for the first-run episodes drop.

Why would that hurt the network''s revenue? Presumably because the network earns money from its audience, through advertising, and fewer viewers means less money. The argument never says so. It also assumes the network doesn''t share in the big payout the producers get from syndication, since that money could make up for the loss.','Evaluate','Evaluate'),
('c93cd3b3-9ed0-4e7b-b363-08ecd0638710'::uuid,'1aa00929acac613870a4e8d23a21f82e','There is no reason to believe that the hypothesis is correct. Rephrase: there is no reason to believe that an invisible "light-absorbing medium" exists in outer space.','Conclusion','Conclusion'),
('27f74a90-b4a4-4956-8be0-9736b1a2056a'::uuid,'77ea45713caa053cea745e55ba665a3c','The professor''s reasoning: the scientists'' support for the medium is that it would explain the low visibility of other star systems. But relativity already completely explains that low visibility. So the support is gone.

The author seems to be thinking,
```
low visibility completely explained by relativity → no reason to believe the medium hypothesis
```
Let''s argue with it. Given that relativity completely explains why other star systems are hard to see, how could we argue that there is still some reason to believe in the medium?

One way: maybe relativity''s explanation isn''t separate from the medium at all. Suppose relativity''s account of the low visibility only works if the medium exists. Then the more convincing relativity is, the more reason we have to believe in the medium. Think of two witnesses, Eddie and Laura. If Eddie''s complete account of what happened includes Laura''s key detail, Eddie''s account doesn''t make Laura''s detail unnecessary. It confirms it.','Evaluate','Evaluate'),
('74beed47-7cac-4105-b985-6c63de8b7eb3'::uuid,'61b2a3f005abe769a03e4739fcad7308','Look for a Defender that rules out this overlap: relativity''s explanation does not depend on the medium. Negate it and relativity becomes a reason to believe in the medium. Or look for the principle behind the reasoning, something like, "If one theory completely explains X on its own, X gives no reason to believe a rival hypothesis."','Goal','Goal')
) v(id,ob,nb,ol,nl) where t.id=v.id and md5(t.body)=v.ob returning t.id;