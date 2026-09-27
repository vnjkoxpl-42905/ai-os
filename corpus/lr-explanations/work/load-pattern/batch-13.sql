-- PT113-S4-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=4 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$When people express dissatisfaction with their legislative representatives, we can be assured that these representatives are simply doing what they were elected to do.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Representatives were elected to compete for the government's scarce funds, which requires compromises.

Those compromises give off the impression of ineffectuality, which people express dissatisfaction about.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The conclusion is saying that reps are doing what they are elected to do, and it builds that case by defining what they're elected to do (compete for funds), telling us what's required of that (make compromises), and telling us a by-product of that requirement (you look ineffectual to some people).

One of the most helpful observations we can make while reading this one is its *Conditional Conclusion*.

We don't have to symbolize it, but if we did, it would look like this:

*People expressing Reps doing*
*dissatisfaction with - - - - - - - - -> what they were*
*their legislative reps elected to do*

Fighting / Refuting / Rebutting / Contradicting a conditional means saying, "it's possible that the left side is true and the right side is false".

So if we want to fight this conclusion, we need to argue that "it's possible that people are expressing dissatisfaction with their legislative reps, but the reps are **not** doing what they are elected to do".

The evidence only deals with one specific complaint people make. People will complain that their reps are ineffectual, the author ably shows us how apparent ineffectuality is simply the manifestation of them doing something required of their job.

But what about other complaints? What people complain that "their representatives are making personally-enriching deals with foreign leaders"?

Is that the representatives simply doing what they were elected to do?

What if people complain that their representatives are making racist / sexist remarks? Is that the reps simply doing what they were elected to do?$lsat$),(3,$lsat$Goal$lsat$,$lsat$The correct answer will either lock us into the subject matter of the evidence, by giving some *Linking* idea like,

"Whenever people express dissatisfaction with their legislative reps, they are complaining about apparent ineffectuality"

or it will be a *Defender* answer ruling out one of these other reasons,

"People do **not** often complain about their legislative reps making personally-enriching deals with foreign leaders".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S4-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=4 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The one-sided facial rash was caused by prolonged contact with telephones.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Several patients had a rash on just one side of their faces, and in each case the rash was on the same side as the patient's telephone use.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$When we're dealing with a "diagnosis / hypothesis / explanation", we know we're dealing with *Explain Curious Fact*.

CURIOUS FACT:
Why do these patients have a rash on one side of their face?

EXPLANATION:
It's caused by prolonged contact with telephones.

Whenever we're dealing with this template, we know we can strengthen by
1. **ruling out** an Alternate Explanation for the curious fact
2. making the Author's Explanation **more plausible**$lsat$),(3,$lsat$Goal$lsat$,$lsat$We need to get rid of four answers that strengthen. Typically, with EXCEPT questions, three of those four will do it one way and the other one will do it a different way.

So we might get three answers making the phone hypothesis more plausible and one answer ruling out the idea that the rash comes from something else (e.g. the side of their face that lays on their pillow at night).

The correct answer will either weaken or be irrelevant.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S4-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=4 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Speed limit reduction can reduce traffic fatalities.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Since we lowered the speed limit a year ago, there have been way fewer highway fatalities than in the previous year.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$There is a **Curious Comparison** -- why are this year's traffic fatalities so much lower than last year's?

The author assumes a **Causal Explanation** for it -- the new speed limit caused the reduction in fatalities.

What are the two lenses through which we evaluate every Curious Fact / Explanation argument?
- is there some **Other Way** to explain the curious fact?
- how plausible is the **Author's Way**?

How else could one explain a reduction in traffic fatalities?
- fewer drivers
- better road conditions
- more policing, which deters aggressive driving
etc.

How would we assess the plausibility of the author's hypothesis?
- in nearby areas where the speed limit didn't change, were the fatalities still as high as last year?
- are people obeying the new speed limit? i.e., has average driving speed actually decreased?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since this is Necessary Assumption, we would primarily look to **rule out** an **Alternate Explanation** for why fatalities are lower this year, but we'd also consider an answer that states something required for the author's story to be plausible (such as "drivers have started driving differently in response to the new speed limits").$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT113-S4-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=113 AND q.section=4 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Background$lsat$,$lsat$After 1950, farmers greatly increased fertilizer use, which led to a doubling of farmland productivity by 1985.

Since 1985, they've been trying to increase productivity even more.$lsat$),(1,$lsat$Surprising Claim$lsat$,$lsat$And yet, since 1985, they've started using less fertilizer.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$*Given that ...* fertilizer was so effective at increasing productivity from 1950-1985
*Why is it that* ... since 1985, the effort to increase productivity has involved using slightly *less* fertilizer than before?

It seems like the answer will have to say something like, "Fertilizer stopped working to increase productivity" or "Something else was even better / cheaper as a means of increasing productivity".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT114-S1-Q24 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=1 AND q.question_number=24 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$A young child's taste preferences can be affected by the type of food he or she has been exposed to.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$One-year-olds usually prefer sweet to salty. But if you feed a one-year-old salty food for a year, by age two they will choose salty over sweet.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The "experiment" described does involve exposing 1-year olds to salty foods and does involve their taste preferences changing a year later.

So there doesn't seem to be a Missing Link in terms of what the evidence vs. conclusion are talking about. The only difference is that the conclusion is Causal (*affected by*) and the evidence is just Chronological (*a year later, something has changed*).

Just because the salty food exposure was followed by a change in preference doesn't mean that the salty food exposure *caused* the change in preference.

This is essentially an *Explain Curious Fact* argument where the author is wondering why the kid switches from preferring sweet to preferring salty and chalks it up to that year of exposure to salty foods.

For that type of argument, the author has to assume,
*there isn't some Alternate Explanation for the evidence*
*+ the Author's Explanation is plausible*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer ruling out an alternate explanation for why the kids prefer salty foods a year later, or look for something required for the author's story (that exposure to salty changed their preference to salty) to be plausible.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT114-S2-Q22 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=2 AND q.question_number=22 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Information$lsat$,$lsat$Some organisms form from endosymbiosis, when organism X engulfs organism Y, and Y becomes a functioning part of X.

We found a weird nucleomorph within a plant called a chlorarachniophyte.

Two versions of a gene were found in the nucleomorph.

If the nucleomorph were not the remains of an engulfed organism's nucleus, then we would expect to find only a single version of the gene.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Yikes! This is one of the harder Science-laden stimuli we'll see in LR.

We can get started, though, by focusing on what we typically read Inference paragraphs looking for:

1. overlapping information
2. conditional / causal / math-y wording

Nucleomorphs is mentioned a few times, and engulfed organism shows up twice. The final sentence gives us a conditional rule, signified by **if**.

Inference questions love to provide a conditional and then provide a fact that triggers the contrapositive of the rule, to test us on whether we're shrewd enough to infer the outcome of that contrapositive.

We were told
*N were not remains → find only a*
*of engulfed org's nuc single gene*

Contrapositive
*find more than → N is remains of an*
*a single gene engulfed org's nucleus*

They told us that they *did* find "**two** versions of the gene".

So according to this rule, that nucleomorph is the the remains of an engulfed organism's nucleus. Where in the paragraph did we hear about "engulfed organism" before?

The first sentence said that endosymbiosis is a process in which one organism engulfs another. So is that what's going on with this nucleomorph?$lsat$),(2,$lsat$Goal$lsat$,$lsat$While we can't be certain, it seems like we're being guided towards the suspicion that this nucleomorph (which we know from the final two ideas is the remains of an engulfed organism's nucleus) was involved in some endosymbiosis.

Endosymbiosis involves one organism engulfing another until the latter is part of the former. Since we know that this nucleomorph was part of an organism that was engulfed, and since we know that now it's hanging out inside a plant called a chlorarachniophyte, we could support the idea that the chlora plant engulfed the nucleomorph's former organism.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

