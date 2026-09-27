-- PT101-S3-Q13 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Watching TV has a bad influence on the dietary habits of television viewers.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$The foods and beverages mentioned or consumed on many TV programs are extremely low in nutritional value.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument is saying that when we watch a show, the people on the show are eating junk food. Therefore, watching this show has a bad influence on our dietary habits.

That seems to assume watching the show will somehow affect my dietary habits. If I see Tony Soprano eat a Big Mac, does that mean that I'm now more likely to eat a Big Mac? (By that logic, watching Tony Soprano kill a dude makes me more likely to kill a dude?)$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying that "at least some people are more likely to eat food X if they see food X being consumed on a TV show".$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=101 AND q.section=3 AND q.question_number=13 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT101-S3-Q14 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Given That$lsat$,$lsat$Soda sales are usually highest during the summer months, and Foamy Soda lowered its prices in an effort to boost sales.$lsat$),(1,$lsat$How Can it Be That$lsat$,$lsat$Foamy Soda's sales dropped during the summer months.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$We need to find four different ways to explain Foam's lower sales numbers.

An answer might say that "lower prices" somehow caused lower sales (a contrast between normal price and lower price.

An answer might use a contrast between what happens for typical sodas (good sales during summer) vs. what happens for Foamy (they're different from other sodas in some worse way).

An answer might use a contrast between typical summers (high soda sales) and this summer (bad soda sales for some reason).

But basically we need to know why this summer isn't like typical summers, Foamy isn't like other sodas, lower-price Foamy isn't like regular priced Foamy, or some other mechanism that can explain why Foamy had disappointing sales this summer.

We can preface our reading of every answer choice by saying, "Foamy had poor sales during the summer months, because .... [answer choice]."$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=101 AND q.section=3 AND q.question_number=14 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q19 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Statements$lsat$,$lsat$In Most Supported / Must Be True, we're primarily reading for Conditional, Causal, Quantified, or Pivot wording.

The first sentence gives a *correlation*:

most playful period | | most rapid growth of
of young mammal's life neural connections

The second sentences gives a *Conditional* / **Causal** **Difference-Maker** type idea.

*Without* these neural connections **created by** frequent play, the mammal's survival and well-being as an adult would be threatened.$lsat$),(1,$lsat$Goal$lsat$,$lsat$We're looking for an answer that goes *against* part of this causal story or at least fails to be derived from this causal story:

lots of play ⇢ lots of neural ⇢ ability to survive
when young connections and be well$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=19 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q2 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion (it follows that)$lsat$,$lsat$No matter how high a salary is offered, no one will apply for this job.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$No one wants this job as much as Josh, and he's not applying for it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Uhh, if the salary is $1 million / year, I might like to apply. Can I hear the job description?

This argument is clearly silly, since even if Josh doesn't want this job, one of us might (especially given the conclusion's range of "no matter how high the salary"). But how do we put this into something abstract and portable.

The copycat ideas are This job / Josh / applying.

We could try to translate the argument as written.

P: No one wants X as much as Y.
P: Y isn't doing Z.
C: so no one will be doing Z.

Or we might say something more generic like:

P: No one wants X as much as Y.
P: Y isn't pursuing X.
C: so no one will pursue X.

Or an even more gisty version:
P: the Person You'd Most Expect isn't doing it
C: so no one's gonna do it$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for an argument saying that, "since the Person You'd Most Expect isn't doing it, no one's gonna do it". If we have multiple contenders, we'll get even more picky with the form.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=2 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

UPDATE lr_explanation_choice_notes n SET body=v.b FROM (VALUES ($lsat$A$lsat$,$lsat$The premise ain't so bad, since it could definitely fit into
"Since the person you'd most expect [to spot an error] hasn't done so ..."

But the matching conclusion we'd need is,
"then NOBODY's gonna be able to spot an error."

This takes a completely diff turn and says,
"Beth will eventually spot the error; it's just later in the program"$lsat$),($lsat$B$lsat$,$lsat$The premise works, since it's saying
"Since the person you'd most expect [to decipher this incription] can't do so ..."

But the matching conclusion we'd need is,
"then NOBODY's gonna be able to decipher this insciprtion."

But instead, this says
"We'll have to ask someone else."$lsat$),($lsat$C$lsat$,$lsat$The premise is saying
"Since the person you'd most expect [to buy Anna's plot of land] isn't pursuing it,"

And so we'd want the conclusion to say,
"then NOBODY's gonna buy it"

And that is what is says, in pretentious LSAT-speak!

This even preserved the "no matter how tempting you make it financially" part of the original conclusion.$lsat$),($lsat$D$lsat$,$lsat$The premise works, since it's saying
"Since the person you'd most expect [to obtain the contract] isn't pursuing it ..."

But the matching conclusion we'd need is,
"then NOBODY's gonna pursue the contract."

But instead, this says
"Everyone else will pursue it twice as hard."$lsat$),($lsat$E$lsat$,$lsat$This doesn't work on any level.

Paul isn't identified as "the most likely suspect" for something.

And the conclusion isn't a prediction that "no one will do [something]". It's a volume dial expression: *the more X, the more Y*.$lsat$)) v(l,b), lr_explanations e, lr_questions q WHERE n.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=2 AND e.style='single' AND n.letter=v.l AND n.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q20 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Determinism is false.
*rephrase:* some events that are presently occurring didn't *have* to happen. They could have failed to occur. They were not caused by the preceding state of the universe, a moment ago.$lsat$),(1,$lsat$Intermediate Conclusion (because)$lsat$,$lsat$It's impossible to know the compete state of the universe at any given moment.$lsat$),(2,$lsat$Evidence (since)$lsat$,$lsat$It's impossible to measure accurately both the position and velocity of any given subatomic particle at a particular time.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$(If you want to sound super cool around your friends, that final premise is known as the Heisenberg Uncertainty Principle in quantum mechanics.)

The missing link from the Premise to the Intermediate Conclusion is that "If you can't measure position and velocity of a given particle at a given time, then it's impossible to know the complete state of the universe".

The author is assuming that, *in order to know the complete state of the universe, you need to know the position and velocity of all subatomic particles at any particular time*.

Maybe that's not the case; maybe it counts as *knowing the complete state* as long as we can say the probability of each particle having a certain position or velocity. But overall, it's unlikely that they're testing us on that move.

So let's focus on the move from Intermediate Conclusion to Main Conclusion: "if it's impossible to know the complete state of the universe at any given moment, then it's not the case that each present moment is a necessary consequence of the state of the universe a moment ago".

We can think, "*Given that ...* it's impossible to know the complete state of the universe at any given moment, *How can we argue that ...* determinism is **right**."

Determinism is the idea that every event is caused by previous events. Each new complete state of the universe is a necessary result of the previous complete state of the universe.

What does the premise have to do with the conclusion? Whether or not we **know** what the complete state of the universe is at any given moment doesn't tell us anything about whether there *is* a complete state at that moment.$lsat$),(4,$lsat$Goal$lsat$,$lsat$Look for an answer saying something like, "even if it's impossible for us to completely determine the state of the universe at any given time, that doesn't mean that the complete state of the universe isn't causally determined by the preceding moment."$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=20 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q3 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Setup Claims$lsat$,$lsat$Many people limit calories / cholesterol in their diet, to lose weight reduce blood cholesterol.

*causal chain*

lose ⇢ fat cells ⇢ cholesterol spilled
weight smaller, into bloodstream
but same #$lsat$),(1,$lsat$Conclusion (therefore)$lsat$,$lsat$When someone goes on a low-cal, low-cholesterol diet ...$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Based on this info, what is caused by a low-cal / low-cholesterol diet? It never officially says, but the first claim insinuates that going on such a diet is thought to lead to lower weight and lower blood cholesterol.

If the person loses weight, their fat cells spill cholesterol into the bloodstream.

So one of the goals is undermining the other goal. The two goals of this diet were "losing weight" and "lowering blood cholesterol". But the causal chain tells us that when you lose weight it actually increases the blood in your cholesterol (at least in one way).$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for a safely worded answer that rewards our understanding that losing weight results in higher blood cholesterol (in at least one sense, because fat cells are dumping their cholesterol into the bloodstream).

Maybe something like, "A person who goes on a low-cal / low cholesterol diet *in order to both lower weight and lower cholesterol* may find that achieving the first thing messes up the second thing".$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=3 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q4 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion (should = opinion)$lsat$,$lsat$The color-changing ink should be adopted, rather than microprinting.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Even though the color-changing ink is more expensive, it would allow anyone to detect photocopied counterfeit currency easily.

Meanwhile, microprinting would be easily detected by experts but not by normal people (which is why counterfeits of microprinting often circulate widely before being detected, i.e. those counterfeit bills get used in a lots of different financial transactions before someone realizes the bill is a fake).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We're choosing between Option A (microprinting) and Option B (color-changing ink).

They each have a stated advantage and disadvantage.

Microprinting wins when it comes to being less costly, but loses when it comes to the fact that it's hard for non-experts to detect counterfeit bills when microprinting is the giveaway.

Color-changing ink loses when it comes to being more costly, but wins when it comes to the fact that it's easy for *anyone* (including non-experts) to detect a counterfeit bill.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Since we're *Weighing Tradeoffs,* we would want to strengthen by adding another positive to colored-ink, another negative to microprinting, or to hear that the positive about colored-ink outweighs the negative.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=4 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

-- PT102-S2-Q5 fix formatting
UPDATE lr_explanation_steps s SET label=v.l, body=v.b FROM (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Special ink should be adopted, despite the expense.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$The cheaper alternative, microprinting, allows for counterfeits that circulate widely before being detected (it's easy for experts to detect that they're fakes, but it sounds like it's not so easy for non-experts, which is why it circulates widely).

Special ink would make it easy for non-experts to recognize fakes.$lsat$),(2,$lsat$Goal$lsat$,$lsat$We need some way to argue that special ink *isn't* a good idea. Maybe we could defend microprinting as a better option. Maybe there's a third option we haven't heard. Maybe we can hear something negative about special ink.$lsat$)) v(p,l,b), lr_explanations e, lr_questions q WHERE s.explanation_id=e.id AND e.question_id=q.id AND q.preptest=102 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND s.position=v.p AND s.created_at > timestamptz '2026-09-27 07:00:00+00';

