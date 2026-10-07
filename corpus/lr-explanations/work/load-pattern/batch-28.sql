-- PT148-S3-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$By reducing excessive chocolate consumption, adults can almost certainly improve their mood.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In a study of 1,000 diverse adults, it was found that those who ate the most chocolate were the most likely to feel depressed.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is interpreting the meaning of a study, we can use our Curious Fact / Explanation mindset. The evidence presents a **Curious Comparison** and the author makes a **causal** assumption that one thing causes another in order to get to her conclusion.

*Curious Fact ...* Why were the adults who ate the most chocolate the ones that were most likely to feel depressed?

*Author's Explanation ...* The chocolate is causing their depression

We need to undress this Conclusion for the bare Cause/Effect claim I just said. If I were to say, "By reading less Twitter, adults can almost certainly become less stressed" I am implying that "Reading Twitter causes more stress".

Whenever we see the Curious Fact / Explanation template, we have two pressure points to consider:
1. Alternate Explanations for the curious fact
2. Plausibility of the Author's Explanation

How **else** could we explain why the people eating the most chocolate were the most depressed?

Maybe we could say that the depression came first, and eating chocolate is just their coping mechanism when they're depressed? (This common type of alternate explanation is usually called *Reverse Causality*)

Maybe we could say that the people who eat the most chocolate are people who are unemployed, so the chocolate isn't causing the depression, the *being-unemployed* is causing both the frequent chocolate snacking and the depression. (This common type of alternate explanation is often called *Third Factor)*$lsat$),(3,$lsat$Goal$lsat$,$lsat$If we're doing Flaw and we see Curious Fact / Explanation type arguments, 98% of them will provide correct answers either describing the author's overconfident causal assumption (based on a mere correlation) or they will say the author failed to consider some alternative explanation, such as *Reverse Causality* or *Third Factor*.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (clearly = opinion)$lsat$,$lsat$Scientific fraud is a widespread problem among the author submitting to that journal.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Dozens of authors submitted digital images that had been manipulated in ways that violated a journal of cellular biology's guidelines.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author is reacting to a curious fact with a causal interpretation, so we can use our *Explain Curious Fact* mindset.

*Curious Fact ...* why is this software tool showing that dozens of authors have submitted digital images that have been manipulated in ways that violate the journal's guidelines?

*Author's Explanation ...* these authors are committing scientific fraud / they are manipulating images in fraudulent ways.

The concept of "scientific fraud" really jumps out of nowhere, so we may otherwise (or in addition) have reacted to this argument by just noticing this *New Concept in the Conclusion*.

With *Explain Curious Fact* arguments, we have the same two pressure points:
1. *Alternate Explanations* for the curious fact
2. the *plausibility* of the author's explanation$lsat$),(3,$lsat$Goal$lsat$,$lsat$The author has to assume there *isn't* some other explanation for why dozens of authors had submitted images that violated the journal's guidelines (i.e. they were **not** just oblivious to the guidelines / they did **not** just mistakenly violate the guidelines / the violations were **not** insignificant things like the wrong file type or image dimensions).

And the author has to assume whatever bare minimums there are for her explanation to be plausible (i.e. the scientists violating the guidelines were aware of the guidelines and intentionally manipulated images in a way that gives off a fraudulent impression).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Modern artists are wrong to think that their art lets people get more aesthetic joy than they would get without that artwork. (The works of modern artists don't give people more aesthetic fulfillment than they'd otherwise have)$lsat$),(1,$lsat$Evidence$lsat$,$lsat$There's such a surplus of great art in the world, more than you could ever consume in a lifetime and capable of satisfying virtually any taste.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Jeez, man. You're giving me a lot of FOMO here. "Even if you lived 100 years, you wouldn't scratch the surface of all the great art available."

How can we accept this premise but fight the conclusion and somehow argue that *the works of modern artists* **do** *provide some aesthetic fulfillment that wouldn't otherwise be satisfied*?

This is a really tough riddle for me to crack. If you think about music, as an example, does any new song fulfill an aesthetic need we couldn't have otherwise fulfilled?

An exotic counterexample that comes to my mind is to argue that if you don't have access to internet, you don't have The World's Great Catalogue of music available to you.

You live in Antarctica or the Galapagos Islands, and you miss your Swedish death metal. You can't get it online. You don't have it with you. Then, what's this? Sven, who works at the same lab as you, shares his artwork with you. Lo and behold it's Swedish death metal. You two sit together at the lab cafeteria forevermore.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that is less stupid than that, but similarly allows us to argue that
*even though*
more than enough great art exists
*there's still some way for*
a modern artist to be useful in a way that provides someone with something they wouldn't otherwise have.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*Govt:* We definitely won't pay for patients to take the flu medicine Antinfia until PharmCo provides detailed info about its cost-effectiveness.

*PharmCo*: We'd have to do massive clinical trials to obtain that detailed info, and doing massive clinical trials requires that the drug is in widespread circulation, which only happens if the government health service pays for Antinfia.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$The question stem reads a little atypically, but it has the same function as a normal Most Supported stem: *assuming everything in this paragraph is true, what can we best derive*?

Both the government and PharmCo are saying things with very absolute language. So we could potentially represent their ideas conditionally.

*Government*
don't have detailed info → won't pay for Antinfia
about cost-effectiveness

*PharmCo*
Detailed → massive → drug is → govt pays for
info clinical in wide Antinfia
trials circulation

Since PharmCo's statements involved listing requirements (*require / cannot be until / only if*), we're chaining these together by remembering that **A → B** can be read as "A requires B".

The info the govt wants requires clinical trials, which requires wide circulation, which requires the government paying for the drug.

If we synthesize this chain and just go head to tail, then we see that PharmCo is saying, "Detailed info **requires** govt pays for Antinfia".

By contrapositive, they're saying, "If the government health service doesn't pay for Antinfia, then we can't get detailed info about cost-effectiveness".

And the government said, "If we can't get detailed info about cost-effectiveness, then we aren't paying for Antinfia"

Basically, we're at a stalemate. It's like trying to exchange ransom for a hostage. "I'm not giving you this money until the hostage comes over here." "Yeah? well I'm not letting go of this hostage until I get that money".$lsat$),(2,$lsat$Goal$lsat$,$lsat$Let's look for an answer expressing this stalemate.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q18 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=18 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$A dislike of vegetables is in at least some cases genetically determined.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$In a study people were separated into a group that said they like veggies and one that said they didn't. Blood samples were taken. All the people in the veggie-hating group had a gene in common (gene X, we'll say).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since the author is drawing a *causal* conclusion (in some cases X is **determined** by Y), we can use our Curious Fact / Explanation mindset.

*Curious Fact ...* why did all the people in the veggie-hating group have gene X in common?

*Author's Explanation ...* gene X causes them to hate veggies

On Flaw questions, we need to either criticize the author's failure to consider **Alternate Explanations** for the Curious Fact, or raise some possible objection that would make the Author's Explanation seem **implausible**.

If we were trying to contradict the author's conclusion, we'd be arguing the position of "dislike of vegetables is **never** genetically determined".

So we'd have to find some way to explain away why everyone in the veggie-hating group had this gene in common.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer complaining that the author has overconfidently assumed one causal explanation for the evidence, even though others may exist, or an answer that gives us way to say that even though they all had a gene in common, the veggie-hating might not be genetically determined.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q19 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=19 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Ana's 1st Claim$lsat$,$lsat$On libertarian, principles, I oppose the proposed smoking ban.
*Does Pankaj say he does not oppose the smoking ban?*

No, nothing definitive. He pushes back against Ana's opposition, but that doesn't necessarily mean that he supports the ban. On LSAT, it's common for someone to disagree with person A's rationale for reaching position X, even though they don't necessarily disagree with position X.$lsat$),(1,$lsat$Ana's 2nd Claim$lsat$,$lsat$It isn't the government's business to prevent people from doing things that harm only themselves.
*Does Pankaj say he thinks that it* **is** *the government's business sometimes to prevent people from doing things that harm only themselves?*

No, he doesn't say anything about the government or what its role is.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since Pankaj didn't disagree with any of Ana's explicit claims, we should start asking ourselves what Ana was *assuming*, because maybe Pankaj is disagreeing with an assumption.

The connection between Ana's two sentences assumes that "the proposed smoking ban *is trying to prevent people from doing things that harm only themselves*".

Does Pankaj disagree with this?

Yes! He's saying that people are still allowed to smoke all they want in private (it's not preventing people from doing things that harm only themselves). The ban applies only to smoking public spaces (so it's aimed at preventing people from doing things that harm *others*, in this case preventing cigarette smokers from harming others with their secondhand smoke).$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something like "Whether the ban is preventing people from doing things that harm only themselves".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

