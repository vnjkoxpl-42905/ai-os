-- PT114-S2-Q3 (Unexplained)
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=114 AND q.section=2 AND q.question_number=3 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=2 AND q.question_number=3 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$David's Explicit Claims$lsat$,$lsat$1. Forbidding companies from hiring permanent replacements for striking employees would be very unfair.

2. Companies who aren't allowed to hire permanent replacements would have little leverage in negotiating with strikers.$lsat$),(1,$lsat$Lin's Responses$lsat$,$lsat$1. UNCLEAR - Lin doesn't quite come out and say "it's fair to forbid companies from hiring permanent replacements". We'd have to infer that belief purely from "No", and that's not a super sound basis.

2. DISAGREES - he says they *would* still have plenty of leverage.$lsat$),(2,$lsat$Goal$lsat$,$lsat$The question stem isn't actually *Agree / Disagree*, so it's not clear whether that's how we should be thinking or not. There is an explicit disagreement, so on the first pass let's look for an answer about whether or not companies who can't hire permanent replacements would have a decent amount of leverage with striking workers.

But since it's just a Most Supported question, we just want the most provable answer.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=2 AND q.question_number=3 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$David *absolutely* believes that being able to hire temps gives companies leverage. He thinks that forbidding them from being able to hire temps means they are left with almost no leverage.$lsat$),($lsat$B$lsat$,$lsat$We can tell they both think that companies should have at least *a good bit* of leverage in negotiations with striking employees.

But it's getting overly precise to weigh in on whether they both think that companies deserve equal leverage as the striking employees.$lsat$),($lsat$C$lsat$,$lsat$Well, even though this didn't have a *Disagree* question stem, it played out just like a Disagree question. We can tell that David and Lin disagree about how much leverage is lost by forbidding companies from hiring permanent replacements.

David thinks it takes companies all the way down to "little leverage", whereas Lin doesn't think it takes them down that far. She thinks they still have plenty of leverage.

When it comes to the four answer that mention Lin, this is really the only idea we have any ammunition to weigh in on. The only thing she said is that a company who can't hire replacements still has sufficient leverage.$lsat$),($lsat$D$lsat$,$lsat$Although David is using normative language (unfair), Lin is only using descriptive language, so we have no idea how much leverage she thinks a company *should* have. She only comments on how much they *would* have.$lsat$),($lsat$E$lsat$,$lsat$This is David's position. We don't officially know Lin's position, but if anything it looks like she's disagreeing with this.$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=114 AND q.section=2 AND q.question_number=3;

-- PT114-S2-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$Arguing that I violate the laws of conversation would be like arguing that some physicist violates the laws of physics.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$I have studied and thoroughly mastered the laws of logic.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$LSAC loves to clown this haughty logician, by having him (it's gotta be a him, right?) boast about his logic skillz in a Flaw question.

We accept that this logician has thoroughly studied the laws of logic.

How can we reject his conclusion and argue,
*saying that you sometimes violate the laws of logic is* **not** *like arguing that some physicists violate the laws of physics*

When we're evaluating **Comparisons** and we want to think of objections, most commonly we're just trying to think of some salient difference between the two things being compared.

In this case, is "a logician breaking the laws of logic" like "a physicist breaking the laws of physics"?

No, because it's *possible* to break the laws of logic. You can be illogical. You have the freedom to do so. (Cable news *exists* because of that premise.)

Meanwhile, it's not *possible* to break the laws of physics. They govern our universe always and everywhere.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer complaining about the unfair comparison between being illogical vs. doing something physically impossible.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT114-S4-Q13 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=4 AND q.question_number=13 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (reveals that)$lsat$,$lsat$Television advertising does not significantly affect children's preferences for breakfast cereals.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The study compared two groups of children: one that watched no television and another that watched average amounts. Both groups showed a strong preference for heavily advertised sugary cereals.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is an Anti-Causal argument, because the conclusion is saying that one thing **doesn't** affect another thing.

GIVEN THAT kids showed a preference for sweet cereals whether they watched TV or not, HOW CAN WE ARGUE THAT tv ads *do* significantly affect kids' preferences for cereal?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that provides evidence or a causal mechanism indicating that TV advertising does, in fact, influence cereal preferences, contrary to the conclusion.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT114-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The government-owned gas company is within its rights to sell stoves and other gas appliances.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$A private gas company would be allowed to sell such appliances without anyone seeing anything wrong with it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument leaps from "a private gas company would be allowed to" to "the government-owned gas company is within its rights to." That works only if government-owned companies have the same rights as private ones (in this domain). The argument needs a principle that licenses transferring permissions from private companies to government-owned companies.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that says: government-owned companies have the right to do what private businesses have the right to do.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT114-S4-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=114 AND q.section=4 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$We can expect an increased incidence of headaches, fatigue, and shortness of breath.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$A survey of oil-refinery workers who work with MBTE found an alarming incidence of complaints about headaches, fatigue, and shortness of breath.

Gasoline with MBTE will soon be widely used.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$There is a causal assumption happening as the author goes from evidence to conclusion.

CURIOUS FACT: how come there is a higher incidence of headaches, fatigue, and shortness of breath among these workers who work with MBTE.

EXPLANATION: The MBTE causes those symptoms.

We can strengthen by making it more plausible that MBTE leads to such symptoms or by ruling out an alternate explanation for why those workers have those symptoms.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Eliminate the four answers that help us argue that as MBTE become more widely used, these symptoms will become more widespread.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT115-S2-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=115 AND q.section=2 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Explanation$lsat$,$lsat$GIVEN THAT ...

Crossing at a crosswalk is safer than jaywalking, since drivers are expecting people to cross at a sidewalk.

HOW CAN IT BE THAT

More pedestrians die crossing the crosswalk than jaywalking?

EVALUATE

This is an often used LSAT trope. More people die using the crosswalk because way more people cross there than jaywalking.

It's kinda like saying, "Flying in a plane is safer than jumping out of a place, but more people die flying in a plane". That's because millions of people fly every year, but only thousands jump out of a plane.

Or like saying, "Covid is a much milder illness than Ebola. Yet, more people die of covid than die of Ebola." That's because tens of millions of people get covid and only a few thousand get Ebola.

We measure safety in terms of %, nor raw numbers. Only 1% of people who get covid die from it, whereas 20% of people who get Ebola die from it. But 1% of 10,000,000 is still a bigger raw number than 20% of 1,000.

Similarly, maybe only 1% of people die from using the crosswalk, whereas 15% of people die from jaywalking. But 1% of a much bigger number is still a higher total than 15% of small number.

GOAL

Look for an answer resolving the paradox by saying that way more people use the crosswalk than jaywalk. (note: we usually can't predict the answer to Paradox questions, but in this case, it's just a familiar LSAT pattern that it's hard to resist).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT115-S4-Q22 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=115 AND q.section=4 AND q.question_number=22 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Audiences will enjoy Warner's latest play.$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$The play features superb acting. The chemistry between the actors is intense. Ziegler convincingly captures the emotions of guilt and despair as the family grows estranged.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We need four answer choices that cast doubt on the conclusion that audiences will enjoy the play.

Maybe audiences are bummed out by guilt and despair, even when it's well acted.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Get rid of four answers that give us some way to argue "audiences won't enjoy the play" or that somehow undercut the evidence provided.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

