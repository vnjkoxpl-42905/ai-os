-- PT121-S4-Q15 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=121 AND q.section=4 AND q.question_number=15 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (so)$lsat$,$lsat$The museum could not have remained open had it not been for the coverage from the local media.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The museum could not have remained open if the attendance at the exhibit had been low, and the coverage from the local media contributed to the record-breaking attendance.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$To argue against this conclusion, we're trying to think about how we can make the case that "even if there hadn't been local media coverage, the museum **could** have remained open".

We have a logic rule we have to deal with -- it couldn't have remained open if the attendance at the exhibit had been low. So we'll need to argue that "even without local media coverage, the attendance at the exhibit wouldn't have been low".

We know that the media coverage contributed to *record-breaking* attendance, but without media coverage would attendance have still been pretty strong?

Remember, we don't need there to be record-breaking attendance. All we need to make our case is the possibility that attendance would "not have been low".

Formally, the conclusion is trying to argue this:
*Without ---------------------------------> museum*
*media closes*

The evidence presented is this:
*Without --> less low --------> museum*
*media attendance attendance closes*

The missing link is whether "having **less** attendance, without the media coverage, would mean that the exhibit had **low** attendance".$lsat$),(3,$lsat$Goal$lsat$,$lsat$The author never established that the local media coverage was necessary to avoid having low attendance. She's assuming that "If X helped this event have record-breaking attendance, then X prevented the event from having low attendance".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT121-S4-Q25 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=121 AND q.section=4 AND q.question_number=25 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (This shows that)$lsat$,$lsat$50 weekly behavioral therapy sessions are all that most people need.$lsat$),(1,$lsat$Evidence (study)$lsat$,$lsat$In a study of 60 different psychological problems, 75% of them consistently cleared up within 50 weeks of behavioral therapy.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$*Given that ...* within this study, most **problems** cleared up with 50 weeks (75%),

*How could we still argue that ...* most **people** would need more than 50 weekly behavioral sessions?

Actually, we have several options:

- maybe the study is messed up for some reason. We know that it's a "large and diverse sample", though, so it is unlikely that the sample is too unrepresentative.

- maybe there's a different way to explain the results. We know that within 50 weeks, 75% of problems cleared up, but do we know they cleared up **because** of the therapy sessions? Maybe these people were also trying *other new things* during these 50 weeks (more exercise, better diet, meditation) and *those* are really responsible for the improvement.

- maybe it was the therapy that cleared up the problems, but we can still argue that 50 sessions are **not** all that most people need. Perhaps 50 sessions is enough to "clear up" the problem, but it will recur soon thereafter if we stop regularly having sessions. Perhaps "most people" suffer from a problem that wasn't tested by the study.$lsat$),(3,$lsat$Goal$lsat$,$lsat$There are lots of different options for attacking an argument that has Sampling concerns, Causal reasoning concerns, and a term shift from "50 weeks was all that was needed for most *problems*" to "50 weeks is all that is needed for most *people*".

We'll have to judge each answer to see if passes our two part checklist:
1. Is it descriptively true?
2. if so, does this sound like a logical complaint?$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S1-Q16 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=1 AND q.question_number=16 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Curious Fact$lsat$,$lsat$Why is the price of rice on world markets higher?$lsat$),(1,$lsat$Author's Explanation$lsat$,$lsat$Most of the world's rice production isn't sold on world markets. Most of it is controlled by governments, who distribute it for local consumption.

Since the open market for rice has a relatively small supply, the decrease in rice production can have a significant affect on rice available to world markets.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$We weaken causal explanations in one of two ways:
- Point to some *other way* to explain the curious fact
or
- Undermine the plausibility of the *author's way*$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer that provides
some **other way** to explain why the
price of rice on world markets is higher.
or
Undermine the story that *these decreases*
*in production have significantly affected*
*the amount of rice available on world markets*.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S1-Q21 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=1 AND q.question_number=21 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*Quantifiers* (many / significant #)

Many *successful graph* = years of formal
*designers* training

Many *successful graph* = learned trade
*designers* informally on job

*Quantifier / Conditional* (no)

Successful → Did not ignore
designer wishes of a client$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Whenever we see a conditional rule on Inference questions, we think,

1. Are there any other conditional rules that might chain together with this one?
*Here, there are no other conditional claims. The other two claims are unspecific quantities like 'many' and 'a significant number'.*

2. Can I apply this conditional rule to any of the provided facts? (Might have to contrapose the conditional in order to see its relevance)

In this case, yes! We could apply our conditional rule to the two facts we were given about "successful designers", because "successful designer" triggers our rule and tells us that they definitely "didn't ignore clients' wishes".

We know many successful graphic designers began their careers after years of formal training, *and did not ignore the wishes of their clients*.

And we know that a bunch of successful graphic designers learned on the job, *and did not ignore the wishes of their clients*.

If we prefer thinking of this in terms of *Quantifiers,* this problem is basically giving us these ingredients:

*Some Formal Train <-> Successful*
*Some Learn on Job <-> Successful*
*Successful --> ~ignore*
We can derive
*Some Formal Train ---> ~ignore*
*Some Learn on Job ---> ~ignore*$lsat$),(2,$lsat$Goal$lsat$,$lsat$Find a provable answer, most likely connecting "formal training + don't ignore wishes" or connecting "learned on job + don't ignore wishes".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S1-Q22 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=1 AND q.question_number=22 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$A society ought never to allow any of its explicit rules to be broken with impunity.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$violations of any people chaos
explicit rule go → left without → results
routinely moral
unpunished guidance$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author is assuming that society ought to avoid chaos, and we should probably go along with that common sense assumption. It would be an unlikely answer to say, "this is vulnerable to criticism because maybe chaos is awesome! Who says we don't want chaos?"

The contrapositive of that conditional chain would say,

"If you don't want chaos, then don't leave people without moral guidance, and so don't let any of society's explicit rules go routinely unpunished."

Isn't that what the conclusion is saying? Let's look closer.

What we said:
*don't let any explicit rule go routinely unpunished*

What the conclusion says:
*never allow any explicit rule to go unpunished*

What's the difference? The contrapositive of the chain the author presented in the evidence is saying we shouldn't let a rule go **routinely** unpunished. The conclusion is saying we shouldn't **ever** let a rule go unpunished.

Consider an example -- society has an explicit rule that you're not allowed to run a red light. You're a cop and you pull someone over for running a red light. They tell you that they're having a bathroom emergency and are rushing home / or you see they have a pregnant person in the backseat about to give birth. Should you punish them for running the red light or let them go unpunished?

According to the conclusion, you should **never** let any rule go unpunished!

But according to the evidence, it's potentially fine to let this rule go unpunished. You can't make a **habit** out of letting people run red lights with impunity, otherwise they'll all start doing it and chaos will result. But we weren't told of any danger associated with **occasionally** letting a broken rule go unpunished.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's look for an answer saying that the conclusion is *stronger* than what's warranted by the evidence. The author would be correct to say "a society ought to avoid letting rules go *routinely* unpunished", but it's an unwarranted leap to say "a society ought to avoid letting rules **ever** go unpunished".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S1-Q23 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=1 AND q.question_number=23 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Perception can't be a relationship between a conscious being and a material object that causes that being to have beliefs about that object.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$We have beliefs about many imperceptible material objects.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Wow! This is all-timer in terms of being intractable to read. We can make it to the correct answer with a poor-man's understanding of what going on if we can see some of the structural features and overlapping ideas.

CONC: Term X can't be defined as something with Y and Z.
EVID: There are many cases of Y and Z that we wouldn't call Term X.

X = perception
Y = material object
Z = beliefs about that object

In conversational terms, the conclusion is saying that "Perception is a relationship between a physical object and something with sight/smell/taste/touch/hearing. When I smell that grapefruit, I perceive it. When I touch that doorknob, I perceive it."

And the author is shooting down that definition by saying, "You can't see your car, which is parked outside your house right now, but you still have a belief about it! So this definition of Perception fails."

The flaw is that the author is essentially doing a Necessary vs. Sufficient backwards move. The definition of Perception is saying,
*IF you're perceiving, you've got a relationship between material object / belief*
and the author is acting like it said
*ANY TIME you have a relationship between material object / belief, you have perception*

Her putative counterexample is aimed at this 2nd, incorrect, rendering of the definition. She's thinking, "What about your parked car on the street? You have beliefs about that material object, even if you're not perceiving the car right now (i.e. not looking at it)."$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying "You can't define X as a combo of Y and Z, because sometimes Y and Z occur but it's not X"$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT122-S1-Q24 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=122 AND q.section=1 AND q.question_number=24 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Some limited nonconsensual medical research should be allowed.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Even though in general it's wrong to not get consent first, if we don't occasionally bypass consent in medical emergencies, we won't be able to get knowledge of the best treatment for emergency conditions.$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$Since there's no other way to get this knowledge (the conditional "only if" prevents us from arguing in that style), we could only object to this author by saying, "Sorry, I know you want that knowledge, but consent is a right we can't ignore."

The author is apparently assuming that this knowledge is valuable enough that it supersedes people's right to give consent to experimental treatments.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

