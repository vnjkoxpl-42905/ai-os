-- PT117-S3-Q24 (Unexplained)
INSERT INTO lr_explanations (question_id, style) SELECT q.id, 'single' FROM lr_questions q WHERE q.preptest=117 AND q.section=3 AND q.question_number=24 ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=3 AND q.question_number=24 AND e.style IN ('single','standard')  AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Facts$lsat$,$lsat$*causality (identified by, because, and so)*

Mass + >> indicates whether Brown Dwarf
Atmos Lith

incomplete mixing stars as big as Sun
of elements in >> still have lithium
nuclear furnace

*complete mixing stars smaller than Sun*
*of elements in >> have no lithium*
*nuclear furnace*

BD lacks fully funct >> BD still has lithium
nuclear furnace in its atmosphere

*comparison*
MASS
planets < BD's < stars$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Well what should we do with this hot mess of celestial facts? There are bunch of causal ideas, but they don't seem to form any causal chain because they're about three different categories of things (stars as big as the Sun, stars smaller than the Sun, and brown dwarfs).

The overlapping concepts are things like whether or not your nuclear furnace is fully mixed, how massive you are, and whether or not you still have lithium.

If we think about the 2nd sentence, saying that we use how massive you are and whether or not you have lithium to figure out whether something is a brown dwarf, we could now spell out what that means, based on the last three facts:

*To be a brown dwarf, we'd expect you to still have lithium in you, but be smaller than a star, and bigger than a planet.*$lsat$),(2,$lsat$Goal$lsat$,$lsat$As always on Most Supported, we just want the most provable/derivable answer. It's hard to guess where this one is headed.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;
INSERT INTO lr_explanation_choice_notes (explanation_id, letter, body)
SELECT e.id, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=3 AND q.question_number=24 AND e.style='single') e, (VALUES ($lsat$A$lsat$,$lsat$We heard about three categories of things:

1. stars as massive as the Sun (have lithium)
2. stars less massive than Sun (no lithium)
3. brown dwarfs less massive than stars (have lithium)

We can say, "if you're a stay with less mass than the Sun, then you are a celestial object without lithium in the atmosphere".

But this answer is the reversal of that. We don't know if smaller-stars are THE ONLY celestial objects that have no lithium in their atmosphere.

Maybe planets, moons, comets, or asteroids are also celestial objects without lithium in their atmosphere.$lsat$),($lsat$B$lsat$,$lsat$We heard about three categories of things:

1. stars as massive as the Sun (have lithium)
2. stars less massive than Sun (no lithium)
3. brown dwarfs less massive than stars (have lithium)

It is true that the two things from this list (1 and 3) that have lithium in their atmosphere also have incomplete furnace mixing.

But we don't know if big-stars and brown dwarfs are THE ONLY celestial objects that have lithium in their atmosphere.

Maybe planets, moons, comets, or asteroids are also celestial objects with lithium in their atmosphere. They don't even have nuclear furnaces!$lsat$),($lsat$C$lsat$,$lsat$The double negative is tough, so consider a couple moves:

1. rewrite one of the negatives so that it doesn't sound like a second negative.

e.g. let's rewrite "has no lithium in its atmosphere" as "Lithium-Free".

*No celestial object that's Lithium-Free is a brown dwarf.*

That's easier to translate.
"If it's Lithium-Free, then it's **not** a brown dwarf"

2. The other move is to turn into a logic robot and cite your translation rule for "No A's are B". Robot knows that looks like "If A, then ~B".

We knew that to be a brown dwarf you had to have lithium and be in between the mass of planets and stars.

So it's true to say,
"If something is Lithium-Free, then it's not a brown dwarf".

This answer is really just derived from the final sentence.$lsat$),($lsat$D$lsat$,$lsat$We heard about three categories of things:

1. stars as massive as the Sun (have lithium)
2. stars less massive than Sun (no lithium)
3. brown dwarfs less massive than stars (have lithium)

#3 contradicts this answer. Brown dwarfs are celestial objects with lithium in their atmosphere, and they **do** have less mass than the Sun.$lsat$),($lsat$E$lsat$,$lsat$We heard about three categories of things:

1. stars as massive as the Sun (have lithium)
2. stars less massive than Sun (no lithium)
3. brown dwarfs less massive than stars (have lithium)

We can't assume that 1 and 3 are the only things in the universe with lithium in their atmosphere, just because they're the only things *mentioned* in the paragraph.

Maybe planets, moons, comets, or asteroids have lithium in their atmosphere (they're all celestial objects less massive than a brown dwarf).$lsat$)) v(l,b)
ON CONFLICT DO NOTHING;
UPDATE lr_questions q SET is_explained=true WHERE q.preptest=117 AND q.section=3 AND q.question_number=24;

-- PT117-S3-Q25 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=3 AND q.question_number=25 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$This perception is an illusion.

*rephrase:* Native speakers are wrong to hear sentences of their own language as sequences of separate words (or, "sentences spoken by native speakers are **not** sequences of separate words")$lsat$),(1,$lsat$Evidence (this is shown by the fact)$lsat$,$lsat$Travelers who don't know a local language hear an unintelligible, uninterrupted stream of sound, not sentences with distinct words.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument boils down to this structure.

*People X say Thing A.*
*But they're wrong.*
*This is shown by the fact that People Y say Thing A isn't true.*

We sometimes nickname this a *He Said / She Said* argument, meaning that it's one person's word / point of view vs. another's. The author often arbitrarily sides with one view over the other without justifying their pick (or their attempt to justify favoring one side over the other is super sketchy).

When I listen to Spanish speaking radio, I have a very hard time separating the stream of sound into distinct words. Meanwhile, I'm guessing a Spanish-speaking listener does can comfortably hear the distinct words in a sentence.

So which of us has the "correct" perception?

We could say that my perception is more accurate, since I have fresh ears and am not biased by familiarity. We could say that their perception is more accurate, because they have the necessary faculty (they know Spanish) to accurately judge whether sentences are comprised of distinct words.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer establishing a *Linking* idea like, "If people who don't know a language perceive sentences a certain way, then that is the correct way to perceive those sentences."

Or look for an answer stating the author's assumed preference in this *He Said / She Said* debate: "It's better to trust the opinion of the travelers who don't speak the language than to trust the opinion of the natives who do."

Or look for an answer ruling out an objection: "The travelers are **not** a poor judge of whether sentences have distinct words, given their ignorance of the distinct words in that language".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT117-S4-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=117 AND q.section=4 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Jones did not swallow the chemical.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$If Jones had swallowed the chemical, it would result in a deficiency of a mineral, leading to inflammation of the skin. Since Jones's skin was not inflamed when he was admitted to the emergency room, the physician concluded he had not swallowed the chemical.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$**Given that** the chemical would lead to inflammation of the skin **and that** his skin wasn't inflamed, **how could we argue that** he *did* swallow the chemical?$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that shows why inflammation might not yet be evident in Jones, even if he did swallow the chemical, thus weakening the conclusion.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S3-Q17 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=3 AND q.question_number=17 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$GIVEN THAT ...$lsat$,$lsat$This chicken pox antidote has no serious side effects and is very effective at limiting the duration / severity of chicken pox.$lsat$),(1,$lsat$WHY IS IT THAT ...$lsat$,$lsat$Researchers are warning that widespread use of this antidote could be dangerous.$lsat$),(2,$lsat$GOAL$lsat$,$lsat$We basically need to look for an answer that gives us some story to tell where lots of people take this antidote and bad stuff happens.

If you have outside knowledge about how chicken pox is mild if you have it when you're young but can be much more severe if you get it as an adult, you might be having some premonition here that the "bad stuff" could relate to that.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S3-Q18 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=3 AND q.question_number=18 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$It's unfortunate how scholars studying artifacts tend to overspecialize nowadays (it'd be better if they had a broader range of expertise).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Their understanding of whatever art period they're studying could be enhanced by studying earlier art that influenced it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$When we're trying to extract an implicit principle, we're sort of doing the upfront work of Parallel reasoning, except we wouldn't usually be diagramming anything, just trying to think of the general essence without referencing the specific topic.

The passage is saying that focusing too much on one thing can lead to a deficient understanding of it. You could potentially understand that thing better by also focusing on some of its influential precursors.$lsat$),(3,$lsat$Goal$lsat$,$lsat$I'd probably be looking for something like,
"You could better understand X if you also developed an appreciation for earlier stuff that influenced X."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT118-S3-Q2 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=118 AND q.section=3 AND q.question_number=2 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$There would be less environmental damage if cotton fiber rather than nylon were used to make products like thread and rope.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$The process by which nylon is manufactured releases large amounts of nitrous oxide, which is harmful to the environment.

The processing of cotton fiber does not release environmentally harmful gases.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument is a straightforward comparison of environmental impacts between nylon and cotton fiber. The author suggests that switching from nylon to cotton fiber would lead to less environmental damage.

To weaken this argument, we need to introduce a factor that counteracts the environmental benefit claimed, perhaps highlighting that the switch to cotton fiber might have its environmental drawbacks or other consequences that were not considered.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Let's find an answer that shows how using cotton fiber instead of nylon does not necessarily reduce overall environmental damage, or that it brings an alternative issue that the argument fails to consider.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

