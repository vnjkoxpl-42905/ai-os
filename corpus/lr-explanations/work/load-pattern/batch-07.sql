-- PT107-S3-Q22 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=3 AND q.question_number=22 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$Some say the reason there are tons of small goats on islands is a response to evolutionary pressure to ensure a diverse gene pool.
(breeding with something that is very genetically similar to you, f.e. inbreeding, is less healthy than breeding with a member of your species that has a lot of genetic differences).

**However**,

A trait will only become frequent in a population if the trait contributes to reproductive success. So the only kind of reproductive pressure that would make goats smaller is if being a smaller goat resulted in more reproductive success than did being a larger goat.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Often, when an Inference paragraph gives us a prominent **Pivot**, then the correct answer ends up being a safe way to synthesize what comes before the pivot with what comes after (**Reconcile the Pivot**).

If we were to relate what comes after the "however" to what came before, it seems like this biologist does not quite agree with the "some people" in the first sentence.

They were saying that there are tons of small goats because having a diverse gene pool would be good for the goat species, and she is saying, "evolutionary pressure doesn't work like that. It's not about what's good for the overall species. It's about traits that lead to more reproductive success (i.e. offspring) becoming more and more frequent. So *smallness* would only be an adaptive evolutionary trait if being smaller led to more offspring."

In short, "the reason for the high frequency of small goats is **not** a response to evolutionary pressure to diversify the gene pool".

In addition to Pivot words, we're also reading Inference paragraphs with an eye for Conditional and Causal words, and the last two claims are both Conditional ideas. They don't chain together. The last one is an application of the first one.

Because of this rule
*doesn't influence → doesn't influence*
*reprod. success freq in population*

the author can derive her final idea
*if we're not saying not an evolutionary*
*that small goats → pressure that could*
*have more reprod. influence frequency*
*success of small goats*$lsat$),(2,$lsat$Goal$lsat$,$lsat$We have to be flexible, since we're just looking for the most provable answer, but our instincts might be suggesting an answer that sounds like safely worded version of the biologist's rebuttal takeaway.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S4-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=4 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evaluate$lsat$,$lsat$Often I would go claim-by-claim through the first person's paragraph, trying to figure out whether the second person seemed to disagree. But in this case, the Supervisor's paragraph is pretty explicit about where the disagreement is.

**Supervisor: the latest closed furnaces are extremely fuel-efficient**

So, what comment did the Plant Manager make about "latest closed furnaces" that sounds like, "the latest closed furnaces are **not** extremely fuel-efficient"?

The only negative complaint about the new closed furnaces that relates to fuel-efficiency is this one:

**Plant Manager: the new process costs more to run than the current process**$lsat$),(1,$lsat$Goal$lsat$,$lsat$Look for an answer saying, "whether or not the latest closed furnaces are extremely fuel-efficient", or, interchangeably, an answer saying, "whether or not the new closed furnaces cost more to run than the current open ones".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S4-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=4 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$Overall, adopting the new process will cost much bring the company no profit.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The equipment for the new process is expensive to buy and install. The new process costs more to run than the current process (because the copper has to cool and then be re-heated).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author's conclusion is about profit, it's about a *Net Gain / Loss* between expenses and revenue.

The author builds her case that this new process is not profitable by listing two ways in which expenses will rise:
1. new one-time expense of buying and installing equipment
2. new recurring expense of higher processing costs

If we are trying to argue with the conclusion and argue that this new process could still be profitable, we need to point to some other expense that goes down, some revenue that goes up, or both.

All we're told so far is that the new process would greatly reduce the amount of sulfur dioxide released into the atmosphere. Can we turn that into a smaller expense or bigger revenue?

Maybe there's some environmental tax the plant has to pay based on sulfur emissions, and it would save so much money by releasing less sulfur into the atmosphere that it would more than offset the extra money being spent on the equipment / installation / processing.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer pointing to the possibility that this new process could still be profitable, if it leads to a reduction in some expense or to an increase in revenue (that could offset the higher expenses of installing and running the new process).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S4-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=4 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$We shouldn't do police lineups of suspects if the eyewitnesses can hear each other's assessments.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$There's little correlation between the accuracy of someone's account and the confidence they have in it. And certain factors can affect a witness's confidence without affecting their accuracy.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument kind of makes a curious jump from the first two sentences to the last idea. What does "confidence and accuracy are two very different things" have to do with "don't let eyewitnesses hear each other at police lineups"?

Since the second sentence is talking about "certain factors" affecting the confidence of eyewitness accounts, I'm presuming that the author is worried that *hearing someone else's* assessment of a police lineup might influence the confidence of that person's own assessment of the police lineup.

I'm not really sure why the author cares if someone's confidence is impacted by hearing another witness's assessment; maybe she thinks that someone who *wouldn't* have sounded confident in their inaccurate pick will now be biased into sounding more confident about their inaccurate pick.

Or vice versa -- the person *would* have sounded confident in their accurate pick, but based on hearing other eyewitnesses, they become less confident about their accurate pick.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find something that feels like it takes us from "witnesses can have their confidence affected by things, and confidence and accuracy are two separate things" and gets us closer to "we shouldn't allow witnesses to hear each other's answers to the police lineup.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT107-S4-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=107 AND q.section=4 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Profit motive is not at fault for the lack of available housing that leads to homelessness.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In general, if the market allows private investors to make a profit, housing will be provided. It's unrealistic to expect investors to take risks if they're not going to get benefit in return.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The easiest way to locate the conclusion here is two-fold:
- any time we're reading an argument on Role or Main Conclusion, we should be priming our brain with a reminder that most of these conclusions are an opinionated first sentence or a rebuttal opinion.

The word “should” in the first sentence shows the opinion.

We verify that the first option is the Conclusion by using the Support Test: *why should we believe that profit motive isn't to blame for the lack of affordable housing?*

Because private investors would provide housing if the market allowed them to make a profit doing so, and it's unrealistic (unfair) to expect them to take risks with their property unless they get some benefit in return.

The question stem is asking us for the role of the intro to the first sentence, which was the Main Conclusion. What is the role of the into clause? It sounds like it *qualifies* the conclusion. It allows for the idea that profit motive might be at fault for other aspects of homelessness, but wants to say that profit motive isn't to blame for *lack of affordable housing*.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something like, “identifies the specific part of homelessness that the profit motive shouldn't be blamed for”.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT108-S2-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=108 AND q.section=2 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Ramona's Explicit Claims$lsat$,$lsat$1. One of the primary values of college is mental growth from being exposed to wide range of ideas.

2. Too many students miss out on this growth because they pick a technical major that will make them more employable later.

3. Recent pressures to graduate as quickly as possible are worsening this trend.$lsat$),(1,$lsat$Martin's Position on R's Claims$lsat$,$lsat$1. He doesn't indicate what he considers *a primary* value of college, although in a much milder way he seems to agree it is good for students to be exposed to different stuff. He brings up "even tech majors are required to take some liberal arts classes" in a way that suggests, "tech majors are getting some of that (good) wide exposure you're talking about".

2. He somewhat disagrees with this claim by telling us that tech majors are required to take some liberal arts classes. It suggests "tech majors aren't missing out on exposure to a wide range of ideas".

3. He makes no comment on whether recent pressures are doing anything to change anything.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$As is typical on Agree questions, the 2nd speaker doesn't seem to explicitly agree with any of the 1st speakers claims. So we start looking for background assumptions or beliefs they both seem to share.

In this case, they both seem to recognize some students pick technical majors in order to improve their chances on the job market. Nontechnical majors (such as English major) might have a harder time getting a good job after graduation.

And they both seem to think it would be good for technical majors to be exposed to a wider range of ideas, since Martin defends the status quo by saying, "Don't worry, colleges do force technical majors to take some liberal arts classes."$lsat$),(3,$lsat$Goal$lsat$,$lsat$I would have a hard time predicting a specific idea here. We just need to find an answer that feels like it can be supported by each paragraph, even if the support is somewhat gist-y, invisible, or innuendo.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

