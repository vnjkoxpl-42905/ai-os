-- PT148-S4-Q11 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=11 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (should)$lsat$,$lsat$We should rehire Hall Dining next year.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$Other things being equal, we should adhere to the preferences of the majority of students.

Most students surveyed said they would prefer that the current food vendor be replaced with a different food vendor next year.

The only alternative to the current vendor is Hall Dining, which actually *was* the university's food vendor until this previous year.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$*Given that ...* we're going to go with what most students want
*and that* ... most students want to bail from the current vendor
*and that* ... Hall Dining is the only alternative vendor,
*How could we still say ...* we should **not** rehire Hall Dining next year?

This argument is pretty tough to fight, given the constraints put on us by the premises. If we're following what most students want (and if we assume the survey is representative of that), then we should switch vendors. And since Hall Dining is our only option for switching, then we would switch to Hall Dining.

But, there was something weird about learning that Hall Dining was the old vendor for this university. If they were the vendor up until last year, it makes us wonder why we switched away from them a year ago.

Did the prices changes? Was the university less happy about the deal they were getting? Or were the students unhappy with the quality of food or service they were getting? If Hall Dining was bad enough to bail from a year ago, does it really make sense to go back to it?$lsat$),(3,$lsat$Goal$lsat$,$lsat$It's hard to know how to phrase our objection, but we need a way to argue that we **shouldn't** switch back to our old vendor. We'll probably either say the survey is problematic or that something would be different (in a worse way) if we were to revert back to having Hall Dining as our food vendor.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given Bell's Claims$lsat$,$lsat$1. Commentators in the media are wrong to criticize the policies Klein implemented.

2. Klein's policies are unpopular.

3. Klein's policies avoided an impending catastrophe.

4. Klein is just the person we need making important decisions in the future.$lsat$),(1,$lsat$Evaluate Soltan's Responses$lsat$,$lsat$1. no comment
2. potentially agrees
3. potentially agrees
4. disagrees

For claim #2, by saying, "Klein's policies have been effective," Soltan is potentially agreeing with Bell that Klein's policies avoided an impending catastrophe. And by saying "she will not have the political support to make them," Soltan potentially agrees that Klein's policies are unpopular. Neither of these are definite, but at best they would be points that both speakers **agree** on. We're being asked for their point of disagreement, and there's no evidence that they disagree about claim #2 or claim #3.$lsat$),(2,$lsat$Goal$lsat$,$lsat$We'll look for an answer that addresses claim #4. Beware of answers that describe claim #2 or #3, which are potential points of agreement, not disagreement.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q3 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=3 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given that ...$lsat$,$lsat$People in the study were not willing to pay more than $5 for a certain coffee mug.$lsat$),(1,$lsat$Why is it that ...$lsat$,$lsat$If they were given that type of mug and asked to sell it, most of them wanted more than $5 for it.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$We need a way to explain why the mug only seems to be worth "max $5" when they're considering buying it, but seems to be worth "over $5" when they're considering selling it.

The correct answer should point to a distinction about how we think about the value of things we might buy vs. how we think about the value of things we might sell.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q4 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=4 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (which suggests)$lsat$,$lsat$The function of the decorations is to attract females [not to protect nestlings from parasites].$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Before finding a mate, male starlings decorate their nests with fragments of aromatic plants rich in compounds known to kill parasitic insects.

Males cease to incorporate such greenery once egg laying starts.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument attempts to explain a curious fact: why do male starlings decorate their nests with fragments of aromatic plants?

There are actually two arguments that we need to keep track of. There's an attribution ("Some researchers") which indicates an Opposing Conclusion: the decorations protect nestlings—baby birds—from parasites. And there's some Opposing Evidence for this position indicated by "since": the decorations are made of plants with compounds known to kill parasites.

The pivot indicator "however" tells us we're pivoting away from the Opposing Idea and into the ecologist's argument, which is the argument we're tasked with strengthening. This is the one that we want to strengthen.$lsat$),(3,$lsat$Goal$lsat$,$lsat$One way to strengthen a rebuttal is to provide evidence *against* the Opposing Idea. For example, maybe the plant fragments only kill parasites that don't bother starlings.

But, because the stem specifically asks us to strengthen the *support* for the ecologist's conclusion, we might expect the right answer to support the plausibility of the "attract a female" explanation, showing that this cause (decorating) is associated with the effect (getting the girl).

Because Strengthen questions aren't super predictable, though, we need to read each answer with an open mind and consider how it might impact the argument. Beware answers that strengthen the Opposing Argument made by the researchers!$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Evidence (Since)$lsat$,$lsat$The commission's report [on disaster preparedness] will not be effective unless the commission speaks with a unified voice.

Individual members of the commission have repeatedly expressed their own opinions about disaster preparedness in the news media well in advance of completion of the report.$lsat$),(1,$lsat$Conclusion (will not)$lsat$,$lsat$It [the report] will not be effective.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Part of the challenge in this question lies in accurately identifying the premises (evidence) and the conclusion. It's useful to notice that the last statement is a prediction. Predictions are normally conclusions.

It's also helpful that the final sentence follows a common pattern:

Premise Indicator - Premise - Comma - Conclusion

The premise indicator "since" at the start of the final sentence is followed immediately by the premise about individual members expressing their own opinions. There's a comma after that premise, followed by the conclusion that the report will not be effective.

Once we identify the conclusion, we can go back and see how the first and second sentences connect to it. The first sentence seems like background information. It doesn't support or contradict the conclusion.

The second sentence is a conditional statement that could potentially support the conclusion:

If the commission does not speak with a unified voice, the commission's report will not be effective.

~unified voice → report not effective

In order for this statement to fully support the argument's conclusion, we need to know that the commission is not speaking with a unified voice. But that's not what the other premise tells us. The other premise just states that individual members of the commission have expressed their own opinions in the news media.

If we learn that these individual members of the commission are expressing contrasting opinions in the news media—in other words, they are not speaking with a unified voice—we can connect that with the conditional premise, and the conclusion would follow logically:

**~unified voice**

~unified voice → report not effective

Therefore, report not effective$lsat$),(3,$lsat$Goal$lsat$,$lsat$Expect a correct answer to state that the individual commission members are not all expressing the same opinions in the news media—in other words, they're not speaking with a unified voice.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Implied, Likewise)$lsat$,$lsat$Blocking out some of the sun to slow or reverse global warming is analogous to making wide roads free of obstructions to reduce accidents.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$With wide, unobstructed roads, drivers feel like they can take more risks, so the expected uptick in driving safety is somewhat offset by this riskier driving.

With blocking out some of the sun's rays to cool the earth, people/corporations would feel like they can emit more CO2, so the expected cooling effect is somewhat offset by higher emissions.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$It's a stretch to call this an *argument*, as the question stem does. And it's a stretch to call this a *Necessary Assumption* question as our tagging does.

But when we're given an argument and asked which principle in the answer choices best conforms to that argument, it's similar to being asked, "Which of these answers was the author clearly thinking, in making that reasoning move?", which is the gist of a Necessary Assumption question.

There are a handful of Necessary Assumption questions on the last 20 LSATs that are really analogies. Most of them still have identifiable conclusions, but some don't. In either case, we want to focus on thinking about the intended analogy.

Analogies are two different sets of specifics, which share some general trait / relationship / truism.

The correct answer to these will feel like it's speaking to something that is true in both cases.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We want something like, "Attempts to improve X can backfire". "As you reduce a threat, other people feel more emboldened to fill that vacuum."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Therefore)$lsat$,$lsat$Urushiol probably did not evolve in plants like poison oak as a chemical defense.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Only humans seem to get a painful rash from touching it. Wood rats even use branches from the poison oak plant to build nests.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since we want to support the idea that urushiol **didn't** evolve for reason X, we can strengthen two different ways:

- show a different reason, reason Y, why plants evolved urushiol
- add another fact that makes reason X seem implausible$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for an answer giving us a different reason why these plants evolved urushiol: "It wasn't a chemical self-defense mechanism, it was [to attract pollinators]."

Or let's look for more evidence that urushiol **isn't** a chemical defense mechanism: *animals take baths in the stuff*.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

