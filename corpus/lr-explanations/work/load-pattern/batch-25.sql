-- PT138-S3-Q12 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=3 AND q.question_number=12 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Dried parsley should never be used in cooking.$lsat$),(1,$lsat$Evidence (for)$lsat$,$lsat$It is far less tasty and healthful than fresh parsley is.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Our default mode of prephrasing on Strengthen-Principle is to just write a "IF premise, THEN, conclusion" rule.

We're trying to prove "should never be used in cooking" about *dried parsley* and what we know about *dried parsley* is that it's less tasty and less healthful than fresh parsley.$lsat$),(3,$lsat$Goal$lsat$,$lsat$So let's look for an answer like any of these:
*if it's less tasty → then should never be*
*than fresh parsley used in cooking*

*if it's less healthful → then should never be*
*than fresh parsley used in cooking*

*if it's less tasty and*
*and less healthful → then should never be*
*than fresh parsley used in cooking*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT138-S3-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*Volume Dial* (the more x, the more y)
The size of northern fur seals is a good indicator of their population levels:

**The smaller the size, the larger the population.**

Over an 800 year period, the average body size did not vary significantly.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$By applying our *Volume Dial* relationship to this provided fact, we should be able to derive the idea that

*Over this 800 year period, the average population size of seals did not vary significantly*.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Since there are only two claims, and the overlapping concept is "body size", we're being sent a strong message that we're supposed to apply this rule to this fact.

So let's look for an answer saying or reinforcing the idea that "in this 800 year period where northern fur seals were hunted for food by Native peoples in North America, average population size of northern fur seals stayed pretty constant".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT138-S3-Q3 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=3 AND q.question_number=3 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Hence)$lsat$,$lsat$Adding specially marked bike lanes to existing roads is unlikely to enhance the safety of bicyclists.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$More collisions between bikes and vehicles occur on roads with specially marked bike lanes than without them.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is an *Anti-Causal* conclusion, because the author is saying that specially marked bike lanes *won't* enhance the safety of people biking.

Since our job here is to object to the author's conclusion, we have to try to argue that "Adding marked bike lanes to existing roads **would** increase safety for bikers."

The author will retaliate by saying, "Then how come we see more collisions between bikes and cars on roads *with* special bike lanes than on roads *without* such markings? These statistics make it seem like having a bike lane is actually increasing the danger for bikers!"

We would have to *Make an Excuse* for that evidence, as we often do on Anti-Causal arguments.

*Given our view ...* bike lanes **do** increase safety
*How can we explain why ...* more collisions occur on roads with bike lanes?

It's probably because bike lanes are on really busy roads, and most collisions occur on really busy roads. It's also possible that bike lanes usually aren't added to a road unless it's a road where collisions between vehicles and bikes are more likely to occur.

Similarly, you would only install speed bumps on a street if that street had a preexisting problem with people speeding through it.

A parallel argument to this could say, "Statistics reveal that more healthcare dollars are spend on people who suffer from medical conditions than on those who don't. Hence, spending money on healthcare is unlikely to reduce one's suffering from medical conditions."$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying the argument fails to consider that bike lanes are taking a bad situation (an area where bikes keep getting hit by cars) and making them a better situation (bikes get hit *less,* once the bike lanes are installed, even though the number of collisions in these high traffic areas still outnumbers those in mellower roads where bike lanes aren't needed.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT138-S3-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=3 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given$lsat$,$lsat$Over the last few PO -causes↣ SR
decades, **public**
**outcries** against
pollution have
brought about
**stricter regulations**
of emissions.

The cities that had
the most polluted air
30 years ago now
have greatly
improved air quality.

This [**improved air** SR -causes↣ IAQ
**quality**] would not
have happened
**without** these
**stricter regulations**.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT138-S3-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=3 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$Lichens can effectively replace expensive pollution monitoring devices without loss of information.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Tests have shown that lichens are just as accurate as the best equipment available in measuring copper pollution.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is a "Strengthen" question where we need to find an answer that reinforces the conclusion about lichens being a viable replacement for pollution monitoring devices. Since the evidence only directly mentions copper, the conclusion's broad claim might be vulnerable to questions about lichens' effectiveness with other pollutants.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that demonstrates lichens' effectiveness across a range of pollutants, thereby reinforcing the conclusion that they can replace existing devices broadly.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT138-S4-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=138 AND q.section=4 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The effort to set up rehab centers in order to save sea otters from the oil spill wasn't worthwhile.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$900 of the otters the rehab center counted were already dead. 222 of the 357 that were alive were saved. But only 1/5 of the otters that died were ever found.$lsat$),(2,$lsat$Evaluation$lsat$,$lsat$This question stem specifically asks us to undermine the *evidence*, as opposed to the typical wording: undermine the *argument/reasoning*.

What could be wrong with the evidence? It seems like we could say, "saving 222 of 357 is still worthwhile!". Maybe without saving those 222, this sea otter population would have *no* chance to recover, but saving this many of them at least lets these otters one day rebuild their numbers.

The last claim is also perplexing: they only found 1/5 of the otters that died. How do they know that the dead ones they've found are 1/5 of the dead ones? Where'd they get that total from?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something making the evidence seem less trustworthy or less likely to lead us to conclude that these efforts weren't worthwhile.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT139-S4-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=139 AND q.section=4 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (clearly)$lsat$,$lsat$The certification process at Plumb-Ace is not very difficult.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$Nearly everyone who takes the written portion of the certification exam passes it very easily.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$*Given that ...* nearly everyone who takes the written portion passes it,
*How could we still argue that ...* the certification process **is** very difficult?

For me, this took me back to being 16 again. The written portion of the driver's license test wasn't scary. Almost everyone I knew passed that with little prep. But the *driving* portion of the driver's license test was famous for flunking people. You had to master 3-point turns, parallel parking, checking blind spots, hands at 10 & 2, etc.

Similarly, maybe it's easy to pass the written portion of this plumbing certification but it's really hard to pass other portions of the test (like where you have to rebuild a toilet from scratch).

This argument seems to resemble one of our top 10 famous flaws, *Part vs. Whole*. The argument is thinking that because PART of the process is not very difficult (almost everyone passes it very easily) it must be that the WHOLE process is not very difficult.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for an answer choice pointing out that *other* aspects of the test might be really hard to pass.

Or look for an answer describing this flawed move from Part to Whole.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT141-S4-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=141 AND q.section=4 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Biodiversity does not require the survival of every currently existing species.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$While life does require various niches to be filled, many niches can be filled by more than one species.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we do Main Conclusion (or Role) we remind ourselves that the 85-90% of the time the conclusion will be **earlier** than the evidence.

It's usually the First Sentence or some Pivot / Rebuttal idea in the middle.

Does this first sentence sound like an opinion from the author? Not really. There's no opinion indicator in there. It sounds more like a science-y nature fact.

But does the paragraph go on to support that first claim? Yes!

All the claims in this argument sound like science-y nature facts, so we can't differentiate the Conclusion by sorting out which claim is the opinion vs. which is the fact.

So we have to use our other tool ("Which claim is being *supported* by at least one other claim") and if possible to use our test savvy and lean in to the expectation that the conclusion usually is earlier than the evidence.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want to find the answer choice that gives us the best meaning match for "biodiversity does not require the survival of every currently existing species".

We might rephrase that as something like, "Some currently existing species could go extinct without threatening biodiversity".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

