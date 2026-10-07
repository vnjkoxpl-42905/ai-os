-- PT148-S3-Q26 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=26 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Thus)$lsat$,$lsat$If a country is new, it is probably not ruled by a monarch.$lsat$),(1,$lsat$Evidence (since)$lsat$,$lsat$Most countries are not ruled by monarchs.

The older a country is, the more likely it is to be ruled by a monarch.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Since we're seeing *conditional logic* (if)*, quantifiers* (most), a *volume dial* (the more x, the more y), and *repeating ideas* (new/old, ruled by monarch), it seems like we should turn this argument into abstract algebra.

We have two premises:

P1: Most countries are not *Most C's are ~M*
ruled by monarchs

P2: The older a country, *The more O,*
the more likely it's *the more likely M*
ruled by a monarch

C: If a country is new, *If ~O,*
it's probably not ruled *then prob ~M*
by a monarch

This argument's logic is pretty sound. Say there are 100 countries. We know at most 49 of them are ruled by monarchs.

From that claim, we could say "If it's a country, then it's probably not ruled by a monarch", but we wouldn't be able to say "if it's a *new* country, then it's probably not ruled by a monarch."

Why? Because the *new* countries might be atypical. It might be that all the new countries are ruled by monarchs, but only 30% of countries are new. If all the other countries are **not** ruled by monarchs, then it would be true that "most countries are not ruled by monarchs", but it *wouldn't* be true that "if a country is new, it's probably ruled by a monarch".

But, the other premise removes this possibility. It's impossible for the new ones to be the ones ruled by monarchs and the older ones to be the ones not ruled by monarchs when we add the premise that "the older the country, the more likely it's ruled by a monarch".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Knowing the logical validity can sometimes help, but it's mainly important that we see the structure. If it truly stays to form, we have some signature ingredients to look for:

**a "most" premise**
Most A's are not B

**a "volume dial" premise**
the more X, more likely B

**a "conditional" conclusion**
if A has less X, then probably not B.

How do they relate to each other?

The 2nd half of the "volume dial" should sound like the *opposite* of the 2nd half of the conclusion (more likely to be ruled by monarch vs. probably not ruled by a monarch).

The 2nd half of the "most" should sound like the 2nd half of the conclusion (not ruled by monarchs vs. probably not ruled by monarchs)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q5 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=5 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$Jenkin's conclusion must be rejected.

*rephrase: The movie 'Firepower' was intended to provoke antisocial behavior*$lsat$),(1,$lsat$Evidence (because)$lsat$,$lsat$The movie has clearly produced antisocial behavior among many of those who have seen it.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Our author is rebutting Jenkins' conclusion. Jenkins concluded that *Firepower* wasn't intended to provoke antisocial behavior, based on the premise that it would be in the director's interest to prevent such behavior.

So our author is arguing that, "since the movie has provoked antisocial behavior among many who've seen it, then we can conclude the movie **was** intended to provoke antisocial behavior".

This is kind of a crazy argument. Just because something happened doesn't mean people *intended* it to happen. If Gary breaks his wrist while snowboarding, would we conclude "he intended to break his wrist while snowboarding"?

Of course not. This is a semi-famous flaw (Top 15, but not Top 10) we call **Intent vs. Result.**$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for an answer saying the author is assuming that a result was *intended* to occur, or failing to consider that things we do sometimes have ramifications that we never intended.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q6 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=6 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$News reporters shouldn't use the term "loophole" in their stories unless they provide evidence of wrongdoing.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$"Loophole" is a loaded, partisan word that implies wrongdoing and scandal, so when it creeps into news stories, they start to read like editorials.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$On Principle-Justify tasks like this, we usually just predict an "If Premise, Then Conclusion" linking idea.

We're trying to conclude that reporters **should avoid** using a term (unless they've met some exception). So more than anything, as we judge answers, we can ask ourselves, "Can I use this principle, apply it to the word 'loophole', and strengthen the idea that news reporters *shouldn't use* "loophole".

Conditionally, we could say,

**If .... Then ...**
having the word in your
news story makes it should not
read like an editorial use that
or → word in
the word is loaded and your news
implies wrongdoing story
(and)
you've provided no
evidence of wrongdoing$lsat$),(3,$lsat$Goal$lsat$,$lsat$Find an answer that says we shouldn't imply wrongdoing without providing evidence of it, or we shouldn't use words that make news stories read like editorials.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q7 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=7 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$Widespread food shortages are inevitable.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The planet’s resources will only allow for production to increase up to a certain limit, beyond which it cannot grow.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This is a "Strengthen" question where the task is to support the argument that widespread food shortages will occur. To strengthen the conclusion, we need to ensure that the demand (population) will eventually exceed the supply (food production), potentially by highlighting ongoing or future increases in population.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Identify an answer choice that suggests the population will continue to increase beyond the planet's food production capacity, making shortages more likely.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q8 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=8 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Premise$lsat$,$lsat$But in newer video games,
players often control the
movements of detailed
human figures.

The players can see that
the figures represent other
people.$lsat$),(1,$lsat$Intermediate Conclusion$lsat$,$lsat$It is **hard for players to** HI
**identify** with these figures.$lsat$),(2,$lsat$Main Conclusion$lsat$,$lsat$Thus, in this respect the LC
technical sophistication of
the newer video games
often makes them **less**
**compelling** to players.$lsat$),(3,$lsat$Evaluate$lsat$,$lsat$The argument assumes that HI → LC
when games make it harder
for players to identify with
the figure who they control,
they find the game less
compelling.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q9 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=9 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Given that ...$lsat$,$lsat$There are many regions in North America where the growing season is long enough that you could grow pumpkins without risking frost damage.$lsat$),(1,$lsat$Why is it that ...$lsat$,$lsat$Most pumpkin production in North America takes place in regions that do have a risk of frost damage?$lsat$),(2,$lsat$Evaluate / Goal$lsat$,$lsat$If we're counterintuitively growing pumpkins in areas that risk frost damage (when other areas with longer growing seasons don't carry that risk), then there must be something really **good** about those areas with long, cold winters or something really **bad** about those areas with longer growing seasons.

Look for an answer helping us to justify why it's worth putting up with the frost risk in the regions where we do most of our pumpkin production (better land? easier distribution? etc.)$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q1 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=1 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$We can be confident that this year's cleanup will be a success.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Before last year's community cleanup, only 77 of the local residents signed up to participate.

Well over 100 actually participated.

This year, 85 residents have signed up to participate.

Our community cleanup will be a success if we have at least 100 participants.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$This argument makes a very "confident" prediction about this year's cleanup: it will be a success. That seems to be based on the conditional "if 100+ **→** success." But do we have enough information to actually *trigger* that conditional? No way. We only have 85 people signed up. Just because more people showed up than signed up last year doesn't mean that will happen again this year.$lsat$),(3,$lsat$Goal$lsat$,$lsat$A correct answer might describe this as a type of sampling error: basing a prediction on too small of a sample. It also might point out what we sometimes call a "predictive flaw": predicting the future based on what happened in the past or what's happening in the present. Beware of answers that sound relevant but describe things that don't actually happen in the argument. Also beware of answers that describe other famous flaws which do not occur in this argument.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S4-Q10 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=4 AND q.question_number=10 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$For the most part, only govt-sponsored research investigates agricultural techniques that do not use commercial products.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$No private for-profit corporation will sponsor research that is unlikely to lead to marketable products.

Crop rotation is an agricultural technique that does not use commercial products (and it may solve problems at least as well as techniques like pesticides that do use commercial products).$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The argument seems to boil down to a move from "If private, for-profit corporations won't sponsor research of Type X, then for the most part only government-sponsored research of Type X will occur."

Isn't that kind of a **False Choice**? Does research have to be sponsored either by private, for-profit corporations or by government? (The wording "for the most part" softens this and doesn't make it a true False Choice, but in a gist-y sense it's still that)

How else, besides government or private / for-profit corporations, could we see research into something like crop rotation get done?

- nonprofit corporations
- volunteer organizations
- curious individuals
- academic institutions

The other issue with this argument is that it never spells out its **Missing Link** assumption that "agricultural techniques that don't use commercial products **are unlikely to lead to** marketable products". That assumption is what would make the author think that for-profit corporations aren't going to be doing this type of research.$lsat$),(3,$lsat$Goal$lsat$,$lsat$The correct answer will probably strengthen by helping the author get closer to her either/or of "If for-profit corporations aren't doing it, then for the most part it will be the government" by **ruling out** some other possibility for who might conduct this type of research.

Or it will supply the author's assumption that this type of research is unlikely to lead to marketable products (and thus for-profits are unlikely to undertake this research).$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

