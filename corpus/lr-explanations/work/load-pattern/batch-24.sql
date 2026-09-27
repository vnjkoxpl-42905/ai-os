-- PT127-S1-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=127 AND q.section=1 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The average citizen of this town is more likely than ever to become a victim of a violent crime.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Local law enforcement agencies have responded to 17 percent more calls involving violent crimes compared to last year.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author is interpreting a statistical change, so we can use our Explain Curious Fact mindset.

CURIOUS FACT: why have local law enforcement agencies responded to 17% more calls involving violent crime?

EXPLANATION: there is more violent crime!

We can weaken by suggesting an alternative reason for the increased number of calls or undermining the assumption that more calls equate to increased crime rates.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that provides an alternate explanation for the increased call volume or hurts the plausibility of the idea that violent crime is actually on the rise.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT127-S1-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=127 AND q.section=1 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (clearly)$lsat$,$lsat$At least one type of memory does not suffer as a person ages.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In a study, participants had to remember to make a telephone call to a certain number at a specified time. The time when the participants called was recorded electronically.

In the group of 65-75 year olds, only one person failed to make the call at the right time. In the group of college students, 14 of them failed to make the call at the right time.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author is using this experiment in which all but 1 person from the 65-75 year old group remembered to make a phone call at a certain time as a way to support the idea that this "type of memory" is just as strong in these 65-75 year olds as it was when they were younger.

How could we accept that they almost all remembered to make this call but still argue that their memory for phone numbers and appointment times **has** gotten worse as they've aged?

Maybe when they were 50, they could have just memorized this number and call-time but nowadays, knowing that their memories are on the decline, the 65-75 year olds went to great lengths to write down reminders for themselves.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is an EXCEPT question, we're looking for four answers that could strengthen, that could be helpful in establishing the conclusion.

They will either strengthen by ruling out a possible objection to the existing argument, or they will strengthen by providing more plausibility to the author's claim that memory for numbers / appointments is a type of memory that does not suffer as we age.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT128-S2-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=128 AND q.section=2 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (concluded / thus)$lsat$,$lsat$The Neanderthals inhabited this campsite year-round and thus were not nomadic.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The gazelle teeth we found at the campsite were hunted throughout the year.

Meanwhile, at a campsite of Cro-Magnon nomads, we found gazelle teeth that were all killed during the same season.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is looking at archaeological evidence and interpreting its meaning / significance / backstory, we can se our *Explain Curious Fact* mindset.

*Curious Fact ...* Why are we finding a year's worth of gazelle teeth at this Neanderthal campsite?

*Author's Explanation ...* The Neanderthals lived at the campsite year-round and hunted gazelle all year.

Whenever we use this template, we know we're supposed to ask ourselves:
1. Could there be some *Alternate Explanation* for the curious fact?
2. How plausible is the *Author's Explanation*?

If we were trying to defend the Anti-Conclusion, that these Neanderthals **didn't** live at the campsite year round or **were** nomads, then how could we explain the year's worth of gazelle teeth?

Maybe they roamed all around, saving gazelle teeth wherever they went (perhaps they used it to make jewelry), and they were at this campsite for a bit and happened to lose their stash?

How could we hurt the plausibility of the story that they camped here year-round and hunted gazelle throughout the year?

Maybe we could say this campsite wouldn't have been survivable during certain weather extremes throughout a year. Maybe we could say that you wouldn't be able to hunt gazelle for a full year from this campsite, because the gazelle aren't always close enough to the campsite for Neanderthals to go hunt them and then return to the campsite by bedtime.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Weaken, we primarily expect an *Alternate Explanation* for why there's a year's worth of gazelle teeth at this campsite.

But we'll also consider any answer that hurts the plausibility of the storyline that the Neanderthals stayed at this site year round, hunting gazelle.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT128-S3-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=128 AND q.section=3 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$If writers were to follow Johnson's advice, works of fiction would be unrealistic.

i.e.
if writers were to refrain from attributing attractive qualities to immoral characters, then works of fiction would be unrealistic.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$There isn't really any premise, so it's using the term "argument" pretty loosely in the question stem. We know the first sentence is SJ's argument, because it says, "Samuel Johnson **argued** that X, **since** Y". So X was SJ's conclusion and Y was SJ's support.

The rebuttal pivot (but, yet, **however**) signals to us that the last sentence is the author.

We're trying to prove the claim that, "if you were writing fiction and you **didn't** attribute attractive qualities to immoral characters, your work would be unrealistic."$lsat$),(2,$lsat$Goal$lsat$,$lsat$So the author must be assuming that, "in reality (realistic), immoral people **do** have attractive qualities."

Or if we want to predict a conditional version of the answer,

"If a fiction writer isn't attributing attractive qualities to immoral characters, then their work will be unrealistic."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT128-S3-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=128 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Other countries contemplating such labeling should refrain, because it would necessitate production alternatives that are dangerous and pesticide intensive.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The UK required labels on foods with genetically altered ingredients. Producers got rid of these ingredients because they feared consumers would see the labels as warnings.

Many genetically altered crops are pest-resistant, so without demand for these crops, alternative production methods would need to be used.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The environmentalist is concerned that labeling will lead to a drop in demand for genetically altered (a.k.a. pest-resistant) crops, pushing producers to switch to more dangerous, pesticide-heavy alternatives. How's the argument moving from "this happened in the UK" to "so you shouldn't do this elsewhere"?

The argument heavily relies on the assumption that what happened in the UK will also happen in other countries. If producers around the world react the same way as those in the UK, then the environmentalist's conclusion seems plausible.

Moreover, it assumes that consumers interpret these labels as warnings, prompting behavior changes—specifically avoiding the products.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for assumptions that either connect the UK experience with potential reactions in other countries or deal with consumer interpretation of labels as warnings.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT130-S3-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=130 AND q.section=3 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Explanation$lsat$,$lsat$Only people who are **willing to compromise** should undergo **mediation** to resolve their conflicts.

M → WC

Actual **litigation** should be pursued only when one is **sure** that one's position is **correct**.

L → SC

People whose **conflicts are based on ideology** are **unwilling to compromise**.

I → ~WC$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT134-S1-Q18 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=134 AND q.section=1 AND q.question_number=18 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Explanation$lsat$,$lsat$The resultant **increase** ~ICM → ↑~TF
**in rush-hour traffic**
**flow** would not have
occurred had the city
not **invested in**
**computer modeling**
**technology** last year.

The city's **financial** ↑~TF → ~RFP
**predicament would**
**not have been**
**resolved** if the **traffic**
**flow** across the
bridge during rush
hour had **not been**
**increased**.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT137-S2-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=137 AND q.section=2 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (not wise / this is why)$lsat$,$lsat$Paying senior staff with stock options is not wise.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$Stock options allow senior staff to earn more when the enterprise prospers. This dramatically increases the difference in income between senior staff and employees who are paid a fixed salary.

Profitability is reduced by anything that undermines employee morale.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We need to get from "paying senior staff with stock options" to "unwise".

They tell us that paying senior staff with stock options will increase the difference in income between senior staff and employees.

So the author is assuming that it's "**unwise** to dramatically increase the pay disparity between top brass and regular employees".

But the conclusion indicator "This is why" at the start of the 2nd sentence also tells us that the 1st sentence is an important part of the logic.

It's telling us that when you undermine employee morale, you reduce a business's profitability. The idea of "reduced profitability" is probably intended as a match for "not a wise policy".

So the author seems to be thinking that when we dramatically increase the pay disparity between senior staff and fixed salary employees, that will undermine employee morale.

The author's overall reasoning chain looks like this:

*Pay SS greatly lower reduce not*
*w/ stock → increase → emp → profit → wise*
*pay gap morale*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for that missing internal link, that "greatly increasing the pay disparity will undermine employee morale".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT137-S3-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=137 AND q.section=3 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Explanation$lsat$,$lsat$Some nurseries **label** N ↢some↣ Min
any nectarine trees
of the **Stark Sweet**
**Melody** variety as
"**miniature**."

Others do **not**. N ↢some↣ ~Min

If a variety of fruit
tree is **not suitable**
**for growing in a tub**
**or a pot**, no tree of
that variety can be
**correctly labeled** Min + CL → SGP
**"miniature."**$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

