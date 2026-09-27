-- PT111-S1-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=1 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$P's Conclusion$lsat$,$lsat$Computers should be introduced in kindergarten, and computer languages should be required in high school.$lsat$),(1,$lsat$P's Evidence$lsat$,$lsat$Children will need computer skills to deal with tomorrow's world.$lsat$),(2,$lsat$Q's Conclusion$lsat$,$lsat$[Introducing computers in kindergarten and teaching computer languages in high school] would be pointless.$lsat$),(3,$lsat$Q's Evidence$lsat$,$lsat$Tech advances so quickly that the computers / languages that K-12 would be working on would be obsolete by the time these kids became adults.$lsat$),(4,$lsat$Evaluate$lsat$,$lsat$*Given that ...* the computers / languages that kindergarteners and high schoolers would be working on would be obsolete by the time they reached adulthood

*How could we argue ...* it *wouldn't* be pointless -- there is still some value to introducing computers in kindergarten and introducing computer languages in high school?

Maybe using a computer mouse improves hand-eye coordination. Maybe even though the computers the kindergarteners are using will be obsolete, they will still be learning transferable computer **skills** or awareness (like copy / paste / typing / trash, etc.). Maybe some high schoolers will be able to get a part time job coding in the language they're learning (which would not be obsolete at the time they're learning it).$lsat$),(5,$lsat$Goal$lsat$,$lsat$We just need some way of saying, "Even though the tech and language would be obsolete, there is still some point in doing this plan to teach computers more in K-12".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S3-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=3 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It is inaccurate to say that a diet high in refined sugar cannot cause adult-onset diabetes.

*rephrase:* a diet high in refined sugar **can** cause adult onset diabetes.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$A high-sugar diet can make a person overweight, and being overweight can predispose a person to adult-onset diabetes.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The evidence presents a causal chain:
high sugar >> overweight >> adult diabetes

The author has thus shown a causal path from high sugar to adult diabetes.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want two premises that form a causal chain:
Prem: A can lead to B
Prem: B can lead to C

and then a Conc that connects them (or that denies that they can't be connected)
Conc: A can lead to C
or
Conc: It's wrong to say that A can't lead to C$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S3-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=3 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Information$lsat$,$lsat$Zoos function both as education and entertainment.

*Causal Chain*
Removing animals from natural habitats to stock the first zoos **reduced** the populations of those species, which then **endangered** the survival of some of those species.

*Contrast*
Modern zoos get most of their animals not by removing them from natural habitats but by breeding new animals in captivity (i.e. at the zoo).

*Causal Difference-Maker*
Maintaining breeding stocks for continued propagation of various species **makes possible** efforts to reestablish endangered species in the wild.$lsat$),(1,$lsat$Evaluate / Goal$lsat$,$lsat$This is a pretty varied mix of claims with no obvious momentum for combining facts, so I would head to the answers. We're on guard against language that is Too Strong, makes an Unknown Comparison, goes Against the Passage, or just brings up something Out of Scope.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S3-Q26 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=3 AND q.question_number=26 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$People ought to take into account a discipline's blemished origins when assessing the scientific value of that discipline.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Chemistry, for example, had some of its landmark results discovered by alchemists, who believed in crazy stuff like superstitions and magic and helped develop early chemical theory.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is a weird argument Let's think about the Anti-Conclusion client we're representing:
*When we're assessing the value of a scientific discipline, such as chemistry, we do NOT need to take into account its blemished origins.*

Given that early chemical theory sounds like some superstitious / magical non-scientific rubbish, how can we argue that this is irrelevant (does not need to be taken into account) when it comes to assessing what value the discipline of chemistry has.

I guess we would argue that even though it has an embarrassing, scientifically dubious origin story, it's still a really successful scientific theory, and some of our fanciest inventions are based on the correct predictions of chemical reactions, according to the laws of chemistry.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying "chemistry is an unrepresentative sample", or an answer saying that "the bad stuff about chemistry's early days doesn't have impact on how we assess the current value of chemistry".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT111-S3-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=111 AND q.section=3 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Opponent's Conclusion$lsat$,$lsat$The projected benefits of drilling new oil wells are not worth the risk of environmental disaster.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The oil currently extracted from these areas provides only 4 percent of our daily oil requirement, and the new wells would add just one-half of 1 percent.$lsat$),(2,$lsat$Proponent's Reply$lsat$,$lsat$That's as dumb as saying we shouldn't allow new farms, since no single farm could feed the country even for a day.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$We need to respond to the proponent. The proponent counters with an analogy, arguing that just because a new oil well contributes a small amount to overall oil supply, it doesn’t mean it should be dismissed, just as new farms, which don't provide the entire food supply, shouldn't be prohibited.

To weaken the drilling proponent's reply, we should look for a flaw in this analogy or a reason why the analogy doesn't hold.$lsat$),(4,$lsat$Goal$lsat$,$lsat$Let's find an answer that highlights a dissimilarity between offshore oil drilling and starting new farms, or shows why the proponent's analogy is misleading or flawed.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT112-S1-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=1 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Information$lsat$,$lsat$*conditionals* (if = suff, unless = if-not)

Slater --> McG app head
wins of Planning C

Polls are --> Slater
pretty accurate wins

*contrast*

Yerxes is more qualified to head the Planning C than McG is, since she's an architect who's been on Planning C for 15 years.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Whenever we see conditionals on Must Be True / Most Supported, we have two immediate questions:

1. Can I chain this conditional up with any other conditionals?
2. Can I apply this conditional (usually via contrapositive) to a fact that was provided?

We had two conditionals (signified by If / Unless), so we should investigate #1. Do they have a common term that would allow them to chain?

Yes, they're both talking about Slater winning. So the chain looks like this:

Polls are → Slater → McG app head
pretty accurate wins of Planning C

We could look for a "first to last" inference like, "If the polls aren't grossly inaccurate, then McG will be appointed head of Planning Committee".

What about the middle sentence? Is that just filler or is it usable?

We know that "If McG is appointed head, then a more qualified person (Yerxes) didn't get the job".$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for something rewarding us for chaining the conditionals together and possibly using the middle sentence, like, "If the polls aren't grossly inaccurate, then the person appointed head of the Planning Commission will not be the most qualified candidate".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT112-S1-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=1 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (implied)$lsat$,$lsat$Juicers are a waste of money; just eat the whole fruit or vegetable if you want the juice.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$There is no indication that juice separated from the pulp contains any special properties compared to when it is unseparated.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$GIVEN THAT juice separated from the pulp has no additional benefits over whole fruits and vegetables, HOW CAN WE DEFEND juicers?

To weaken this conclusion, we need to show a benefit or advantage of using a juicer that justifies the expense, regardless of the intrinsic properties of the juice.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that presents a reason why owning a juicer might still be beneficial or desirable, even though the juice isn't inherently more beneficial than the solid food from which it comes.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT112-S1-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=112 AND q.section=1 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$A program concerning scientific issues gives rise to no equal-time obligation.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Equal-time obligations arise for programs on social issues because (1) social issues almost always have important political implications, and (2) social issues seldom can be definitely settled on the basis of available evidence.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is a weird argument, where the author is trying to explain why we DON'T need equal time for science stuff based on why we DO need equal time for social stuff.

If I said, "You don't have to worry about me acting weird around your sister. The other reason I acted weird around your friend was because I have a crush on your friend", that would imply a difference: *it implies that I don't have a crush on your sister*.

We're arguing that these two situations are different because there's some underlying difference that matters.

So this author is also *Assuming a Difference*, thinking that the reasons we need equal time for social issues **don't** apply to science issues.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for an answer that helps us argue that we DO need an equal time obligation for science issues.

It'll probably attack the assumed differences, so it might say that science issues ALSO have important political implications or that science issues ALSO can rarely be settled on the basis of available evidence.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

