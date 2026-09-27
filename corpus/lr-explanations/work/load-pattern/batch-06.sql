-- PT106-S2-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=2 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$These patients whose mental disorders result from chemical imbalances can be effectively treated only with medication that will reduce or correct the imbalance.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In some patients mental disorders result from chemical imbalances affecting the brain.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$There's not really much of a premise here, is there? The first two sentences are really providing background or counterpoint. The symptoms of mental disorders include behavioral, cognitive, and emotional problems (all of which sound psychological in nature).

And some mental disorders are effectively treated with psychotherapy. But the author seems to think that a chemically-caused case of mental disorder has to be treated chemically (i.e. with drugs / medicines / chemicals).

He must be assuming that the type of cause dictates the type of treatment: *if your MD is caused by X, then it can only be treated by something similar in form to X*.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer showing the author's move:
*if it's caused by a chemical imbalance, then it can only be fixed by chemically balancing it.*

Or an answer that rules out some objection about alternative possible treatments:
*Patients with mental disorders from chemical imbalances* **can not** *be effectively treated with psychotherapy as well.*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S3-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=3 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The republic's recruitment rates for 18-year-olds depend substantially on recruitment rates for high school dropouts.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$There was a correlation from 1980 and 1986 between an uptick in the % of 18-year-olds recruited by the armed services and an uptick in the % of young people who dropped out of high school.

18-year-olds are generally either high school graduates or high school dropouts.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the evidence is presenting a *changing statistic*, and the conclusion is assuming a causal explanation for that statistic, we can use our *Explain Curious Fact* mindset:

*Curious Fact ...* why was there an uptick in the % of 18-year-olds recruited into the armed services between 1980-1986? (why was this correlated with an uptick in % of 18-year-olds that were dropouts?)

*Author's Explanation*.... the armed forces try hard to recruit high school dropouts, so during this period when there were more high school dropouts, they were able to recruit more 18-year-olds into the armed services.

We can Weaken an *Explain Curious Fact* argument two ways:
1. (more common) suggest an **Alternate Explanation** for the curious fact
2. hurt the **plausibility** of the **Author's Explanation**

Any time an author presents a correlation between X and Y and then assumes/concludes that X causes Y, we're supposed to reflexively consider these two *Alternate Explanations*:

- could it be **Reverse Cause** (in this case -- could the rise in recruits have come first, and that somehow inspired more 18-year-olds to drop out?)

- could there be some **Third Factor** responsible for both? (maybe a foreign invading army is causing people to drop out of school and sign up for the military)$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an alternate way to explain the correlation between more dropouts and more armed service recruits.

Or look for a way to hurt the story that the armed services go after these high school dropouts.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S3-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=3 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Humans are no better than apes at investing (they don't attain a better return on their investments than apes do).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$They gave five stock analysts and one chimp $1350 each to invest.

After one month, the chimp won, having increased its net worth by $210. The net worth of the analyst who came in second increased by only $140.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$*Given that ....* in this game show, the chimp got a better return on its investment than the humans did,

*How could we argue that ....* Humans **are** better than apes at investing (humans **do** attain a better return on their investments)?

Within the experiment itself, it's hard to argue with the fact that the chimp attained a better return than the humans.

So if we're going to fight the conclusion, we'll need to argue that what's going on in this game show experiment is not applicable more broadly to humans and apes.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for four answers that would help us argue that "even though *in this experiment*, the chimp attained a better return on investments than the humans did, *in general* humans **are** better at investing than apes are."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT106-S3-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=106 AND q.section=3 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Hence)$lsat$,$lsat$Depictions of violence among teenagers should be prohibited from movies and television programs, if only in those programs and movies promoted to young audiences.$lsat$),(1,$lsat$Intermed. Conc. (we have good reason)$lsat$,$lsat$Depictions of violence cause young people to engage in violent behavior.$lsat$),(2,$lsat$Evidence$lsat$,$lsat$TV programs and movies that depict violence among teenagers are extremely popular. These media are influential.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The author has established that shows and movies depicting violence are popular and influential, but she hasn't given any solid support for the notion that they're influential in the sense of "seeing these depictions of violence influences kids in a negative way / these depictions make young people more likely to engage in violent behavior".

So one way to strengthen Jane's argument would be to provide some evidence that watching violent shows and movies makes teens more likely to engage in violent behavior, or that "shows that are popular / influential can lead to people imitating the behavior they see on those shows".

The conclusion also makes an interesting caveat, saying that at the very least we should prohibit teen-violence from shows and movies promoted to young audiences.

Jane seems to be assuming that shows and movies promoted to young audiences are more likely to be seen by young audiences.

If we were arguing the anti-conclusion, we might say, "You *shouldn't* prohibit violence, because depicting it has these advantages, which outweigh the disadvantages these depictions may have." We might also say, "What about us mature adults who aren't going to engage in violent behavior but (for whatever reason) want entertainment that involves depictions of teen violence?"$lsat$),(4,$lsat$Goal$lsat$,$lsat$Look for anything helping to bolster the connection between teens watching depictions of teen violence and teens engaging in violent behavior, or look for an answer ruling out some potential objection to the idea of prohibiting teen violence from movies and TV aimed at young audiences.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S1-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=1 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (However)$lsat$,$lsat$It's actually quite common for species to change the environment in ways that help their survival.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The plankton is one example of a non-highly-evolved species that alters the environment for their own benefit.

They cool the earth by releasing a gas that ultimately facilitates cloud cover (and thus more sunlight reflecting back into space).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$On Method, we're just trying to characterize the type of evidence or type of reasoning move used. There's about 8 of them that the test tends to go back to over and over again: *analogy / (counter)example / implications of logic / ruling out other options / suggest alternate explanation / call out dubious assumption / raise an overlooked consideration*

It seems like this would fall into the category of **example / counterexample**.

The author is trying to support a very general conclusion by means of a specific story about plankton (which is prefaced by "**for example**").

A generalization is usually assumed:
*only the most highly evolved species alter their environment in ways that aid their own survival*

The author is offering a counterexample, a case in which a **not**-highly evolved species (plankton) alters its environment in ways that aid in its own survival.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Our standard on Method is simply, "If it matches, it's right." If it's descriptively true, take it. But we might assume we're probably going to hear something like, "discuss a specific example that undermines a general assumption many have".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S1-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=1 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Explanation$lsat$,$lsat$GIVEN THAT
Cats spend a lot of time sleeping, waking up only to stretch and yawn.

HOW CAN IT BE THAT
They have strong, agile muscles?

EVALUATE
Essentially, we're wondering how cats are looking so jacked when they just nap. Most animals would have to exercise strenuously to have these strong, agile muscles.

GOAL
Find an answer that explains how cats could have these awesome muscles, even though they mostly sleep.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S3-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=3 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (it follows that)$lsat$,$lsat$Anyone who is accustomed to reading braille can easily adapt to the use of the new thermal electronic screen.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Braille uses raised dots that are read by touch.

The new technology allows flat computer screens to be heated in patterns identical to braille symbols.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument follows a comparative reasoning pattern. The key idea is that because the thermal device uses the same braille symbol system, the tactile ability required for reading braille should carry over to reading a heated, flat surface.

In other words, the argument assumes that someone who can discriminate braille’s raised-dot patterns will be equally skilled at interpreting similar patterns produced by heat.

To fight the conclusion, we'd have to say that even though someone might be good at reading raised-dot Braille, they wouldn't find it easy to read on a heated flat surface.

That seems plausible! I mean, feeling for a shape via raised dots seems pretty different than feeling for a shape via its heat imprint on a flat surface. Someone might be good at the former but struggle at the latter.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer choice that articulates the required connection: namely, that the tactile ability to interpret braille’s raised dots applies to interpreting similar patterns on a flat, heated surface.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

