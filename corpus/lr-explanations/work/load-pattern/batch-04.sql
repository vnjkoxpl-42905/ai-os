-- PT104-S4-Q14 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=14 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*Conditionals (any, all =* Left side, sufficient)

Book critical of → censor supposed to
country Y's govt. prohibit its publication

New book legally → approved by censor
published after 1712

*Comparison (*1st censor vs. 2nd censor)
*Quantitative* (1/2 vs. 1/4 vs. same number)

**1st censor 2nd censor**

same number approved

50% rejected 25% rejected
(50% approved) (75% approved)$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$They've given us a couple conditional and some math facts to work with. The conditionals don't link together. Even though they both discuss the "censor", the first rule would be about whether or not the govt of Y wants the censor to prohibit it. The other rule is about whether or not the censor prohibits it.

We don't know how much the censors actual approvals / prohibitions will line up with the government's *intent* when they appointed this censor.

The math facts, meanwhile, do combine to tell us something. We see the pivot word **but** introducing the last math fact. It creates a paradox-like tension. When we see pivot words (on Inference questions) do this sort of thing, we want to pause to try to **Reconcile the Pivot**.

(Like if I say Marsha just got a raise, **yet** her salary is the same percent of her rent it was last year .... *this creates a tension, which we could mathematically resolve saying that last year her rent increased too*)

Given that the 1st censor was rejecting 50% of its submissions, whereas the 2nd censor was rejecting only 25% of the manuscripts she reviewed, how did they end up with the **same** number of approved manuscripts?

If Mary says **no** to more people asking her on a date more often than Jane does, but they go on an equal number of dates, that means .... *Mary is asked out on dates more than Jane*.

In this example, if the 1st censor said **no** more often but ended up with the same number of approved manuscripts, she must have read through more submissions.

If this math doesn't seem intuitively clear to you, but your spidey-sense tells you that LSAC *is* trying to test something math-y, then consider throwing some easy numbers on the page.

If both censors read 100 manuscripts, then according to our 1/2 and 1/4 facts,
1st censor -- approved 50, rejected 50
2nd censor -- approved 75, rejected 25

Do these numbers fit the last claim -- **the number of books approved was the same**?

No, the number approved from the 2nd censor is larger. How would you make it the same?

What if 1st censor read 200 and 2nd censor read 100?
1st censor -- approved 100, rejected 100
2nd censor -- approved 75, rejected 25

Well, that was too far, because now the 1st censor approved more books, but we can see that in order to fix the original mismatch (when 1st censor has fewer approvals), we need to **increase** the number of submissions for increase the number of submissions that the 1st censor reviewed in order to make the # of books approved equal out.

If you really want to see numbers that work out, consider these:
1st censor (120 submissions)
60 approved, 60 rejected

2nd censor (80 submissions)
60 approved, 20 rejected$lsat$),(2,$lsat$Goal$lsat$,$lsat$Look for an answer saying something like the 1st censor reviewed more manuscripts than the 2nd censor did.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S4-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Beauty is not subjective (it's objective).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$If you look at what earlier cultures considered most beautiful, you'll be stunned by how similar it is to our standards of beauty. What was considered beautiful then is still considered beautiful now.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$*Given That [evidence]*
Earlier cultures seemed to share similar standards of beauty with our current society

*How Can We Still Argue That [anti-conclusion]*
Beauty is **subjective**?

I guess we could say that the standards then and the standards now are both subjective, but they happen to match.

For example, it might be the case that an answer to the question "which flavor of ice cream is the best?" is subjective, even if an entire school bus full of 3rd graders comes to the consensus of "chocolate".

Maybe it's even causally related. Like the answer to the question, "Which sport is better: basketball or baseball?" is subjective, but maybe me and my dad and his dad and *his* dad all pick baseball, because each of us was raised in a house that revered baseball.

In that way, the fact that our Dad's subjective preference was for baseball may have influenced our subjective preference for baseball. The fact that everyone in our family seems to prefer baseball doesn't make that an objective (or hereditary) evaluation. It could just be that one person's subjectivity gets carried down the line and impacts others'.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Stay flexible, and look for a way to explain how "even though our standards of beauty are very similar to those of earlier cultures, it's still the case that beauty is subjective".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S4-Q18 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=18 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (therefore)$lsat$,$lsat$Publishers now, more than ever, are more interested in making money than in publishing books of intrinsic value.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Book publishers traditionally published a few books they thought had intrinsic value, even though they knew the book was unlikely to make a profit.

Nowadays, fewer of those books are being published.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The evidence introduces a *Curious Fact*, an asymmetric comparison:

*Curious Fact ...* why is it that nowadays there are **fewer** books published that have intrinsic value but are unlikely to make a profit?

*Author's Explanation* ... nowadays, publishers are more interested in making money than in publishing books that have intrinsic value.

As always, with *Explain Curious Fact* arguments, we have a two-pronged mindset:
- Could there be an **Alternate Explanation** for the curious fact?
- How **plausible** is the Author's Explanation?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Most correct answers that Weaken an *Explain Curious Fact* argument provide an alternate explanation.

So let's primarily look for an **alternate** **way to** **explain** why fewer books with intrinsic merit but low profitability are being published.

But we'll keep an open mind to an answer that **hurts the plausibility** of the claim that publishers nowadays are more interested in profit > intrinsic value than were publishers of the past.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S4-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Robbins cannot pass judgment on Stuart's art.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Robbins does not understand Stuart's art well enough to praise it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$When an author says, "*While* X is true, Y is true", that 2nd idea is the one that matters. The first one is a concession.

So we have a really skimpy argument. R doesn't understand S's art well enough to praise it. Therefore, R cannot pass judgment on S's art.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We can predict the "If Prem, then Conc" missing link assumption:

*Don't understand X → can't pass judgment*
*well enough to praise it on X*

We can also get our ears ready for the contrapositive version of that same thing:

*Can* *pass judgment → do understand X well*
*on X enough to praise it*$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S4-Q21 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=21 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evaluate$lsat$,$lsat$At first the author is considering a blanket rule that goes like, "if a word ends in *-ee*, then it designates the person affected in action by someone else".

Then she considers *absentee* and realizes there's no someone else who is absenteeing the absentee.

(Whereas there was a someone else who is employing an employee, someone else who is paying the payee, someone else who is detaining the detainee).

So the author adds a little caveat, another qualification to the rule, so that *absentee* would no longer qualify:
"if a word ends in -ee, **and** the word refers to one party in a two-party transaction, then the *-ee* refers to the party receiving the action".

Let's look for "adds a qualifier / a caveat / another condition".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT104-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=104 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Therefore)$lsat$,$lsat$The commissioner's suggestion is not financially feasible.
*Rephrase:* It's not financially feasible to pave our roads with rubberized asphalt.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Rubberized asphalt is more expensive than plain asphalt and the city's budget for building and maintaining roads cannot be increased.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$If we were to predict a *Linking* answer here, it would just sound like, "If a budget can't be increased, the it's not financially feasible to buy a more expensive ingredient than the one you're currently using."

But it seems like this very real-world argument is meant for us to analyze with our *Objection / Defender* brain:

*Given that ...* we can't increase the budget, and rubberized asphalt costs more than plain asphalt,

*How could we still argue that ...* it **would** be financially feasible to pave the roads with rubberized asphalt?

- Maybe we could say that even though we can't increase the budget, we still have money left in the budget, so we could afford to spend more on rubberized.

- Maybe rubberized is more expensive, per unit, but you don't need to buy as much? Or maybe we can get some donations of surplus rubberized asphalt from other cities that have extra?

- Maybe we have to spend more money to procure rubberized asphalt, but then since it makes ice removal easier and causes "less of a strain on the road-maintenance budget" we end up saving the extra money we spent.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer ruling out one of these aforementioned objections (or one we didn't think of):

- We **can't** get free asphalt donated to us from anyone
- We **don't** have extra money left in our current budget that we could use on rubberized asphalt
- The money rubberized asphalt would save us on our road-maintenance budget would **not** offset the extra cost of the rubberized asphalt$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

