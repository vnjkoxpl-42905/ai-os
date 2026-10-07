-- PT148-S3-Q20 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=20 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (So)$lsat$,$lsat$Apples were probably not cultivated in this region 5,000 years ago.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$The only remains of apples found are from apples that are the same size as the wild apples native to this region.

Cultivated apples found in supermarkets are much bigger than these.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Given this evidence, how can we argue that apples **were** cultivated in this region 5,000 years ago? Can we say the remains of apples that we found *were* cultivated apples?

The author will respond, "Of course they weren't. They were the same size as wild apples."

Why does that mean they couldn't be cultivated? Do we know that cultivated apples would have been bigger?

No, we just know that supermarket apples are bigger. But maybe that's just because the grocers who stock supermarkets grab the biggest apples they can find to put on the store shelves. We don't know if cultivated apples are all that big.

The author is failing to consider that some cultivated apples could be as small as the wild apples of this region. She's failing to consider that supermarket apples are an unrepresentative sample of cultivated apples. Perhaps supermarket apples are much larger on average than cultivated apples are on average.$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for a way that we can argue that the apple remains that were found were from *cultivated* apples. We have to "make an excuse" for why they're smaller than supermarket apples, or we can just pick any answer that names the author's reasoning move: "takes for granted that if the apples whose remains were found were the size of wild apples, then the apple was automatically a wild apple".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q21 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=21 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (thus)$lsat$,$lsat$The happy life tends to be the good life (the morally virtuous life).$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Happiness consists in one's sense of approval of one's character and projects.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author has a couple moments here where she says, "defined not as X, but as Y". We should focus more on how she *is* defining things than on how she isn't.

According to the evidence, "the happy life" would be one where one *approves of one's character and projects*.

According to the conclusion, "the happy life" is a *morally virtuous* life.

So it seems like the author is assuming some missing link between "approving of your character and projects" and "being morally virtuous".$lsat$),(3,$lsat$Goal$lsat$,$lsat$Look for something like "if you approve of your character and projects, then you tend to be living a morally virtuous life".$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q22 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=22 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion (Hence)$lsat$,$lsat$Returning organic wastes to the soil is a good way for small-scale organic farms to solve their waste disposal problems.$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Returning organic wastes to the soil is a good way to solve waste disposal problems **only if** the wastes are nontoxic and not too much energy is expended in transporting them.

For small-scale organic farms, the wastes are nontoxic and not too much energy is expended in transporting them.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$Whenever we do Parallel Flaw, we prime our brains for the Top 5 famous flaws (Necessary vs. Sufficient / Part vs. Whole / Unproven vs. Proven False / Causal / Ad Hominem).

Whenever we do Flaw or Parallel Flaw and see any *Conditional Logic* in the argument, then we know there's like a 95% chance that we're being tested on Necessary vs. Sufficient, the flaw in which an author presents a conditional logic premise but then applies that conditional rule using some *Illegal Reversal* or *Negation*.

The first sentence of this argument gave us a conditional logic rule, signified by "only if", which always indicates the necessary idea that goes on the right side of the arrow:

*Returning organic wastes Wastes are nontoxic*
*to soil is good solution to → and*
*waste disposal problems Low Trsnpt energy*

We would then anticipate that the author will either say, "Since the right side is true, the left side must be true" (this is an illegal reversal, and this is what the argument does), or the author will say "Since the left side isn't true, the right side must not be true" (this is an illegal negation).

The author establishes that for small farms, the two ideas on the right side are true, and then she illicitly concludes (by reading the rule backwards) that the left side must be true about small organic farms.$lsat$),(3,$lsat$Goal$lsat$,$lsat$We just want something that provides a conditional logic premise and then argues via an illegal reversal, i.e.

Premise 1: X → Y
Premise 2: For thing A, Y is true.
Conclusion: For thing A, X is true.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q23 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=23 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion / Hypothesis$lsat$,$lsat$Phenazines serve as molecular pipelines that give interior bacteria access to essential nutrients in the environment surrounding the colony.$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$There isn't any support provided for this hypothesis, so we're not evaluating an argument. Normally when we see the word 'hypothesis' we use our Curious Fact / Explanation mindset.

Here, the Curious Fact would just be, "What the heck are these phenazine things all about?"

However, we already have one valid answer -- they're antibiotic molecules that fend off other bacteria. The scientist's hypothesis is speculating an *additional* possible explanation for phenazines.

Usually with Curious Fact / Explanation problems, we're thinking about affecting the argument in two different ways:
- considering Alternate Explanations for the curious fact
- considering the plausibility of the Author's Explanation

But since we already have an explanation for phenazines, we wouldn't waste any time worrying, "Could there be some *other* reason for phenazines?" We already know that fending off bacteria is one reason.

So all we're concerned with is the plausibility of the author's additional explanation -- that phenazines act like pipelines that give interior bacteria access to essential nutrients in the environment surrounding the colony?

Picture a bacterial growth on a piece of moldy bread. It ends up looking like a big oval type shape. That whole shape is full of molecules of bacterium. The colony grows outward as it consumes more nutrients that facilitate its growth. But how do the molecules of bacterium on the inside of the colony get food? They're just surrounded by more bacteria, not by more bread to consume.

According to this scientist, phenazines are taking the nutrients from the not-yet-moldy bread on the exterior of the colony and shuttling it into the interior of the moldy spot in order to feed the bacteria living at "city center" (it's almost like when metropolitan cities are surrounded by a Beltway, and there are some roads that lead from the Beltway to the city center).$lsat$),(2,$lsat$Goal$lsat$,$lsat$We just need an answer that makes it seem somewhat more plausible that phenazines act like a pipeline that shuttles nutrients from outside the moldy circle to the inside of the circle.

The most common way that LSAT strengthens the argument is "No Cause, No Effect", so that would mean something like, "When there aren't phenazines, there *isn't* the piping of nutrients from the outside to the inside."$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q24 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=24 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Statements$lsat$,$lsat$*quantified* (most, some)

Most *culturally significant*
*medieval manuscripts* will be restored

Some *dubiously authentic*
*medieval manuscripts* will be restored

*conditionals* (only, will not)

Will be → manuscript's safety can be
restored ensured during restoration

Not frequently → won't be
consulted manuscript restored$lsat$),(1,$lsat$Evaluate$lsat$,$lsat$Beyond the quantified and conditional statements, there are also a couple *Causal* connectors (due to / this means that), so it's possible the correct answer will deal with those relationships.

But there's a *Pivot* word (however) introducing the final sentence, which usually suggests that our thinking job is to integrate that *however* sentence with what came before. The *However* sentence gives us two conditionals. Do they chain together? Do they have any overlapping term?

They both deal with the concept of "will / will not be restored", but they don't chain together. They both start from the same trigger, though.

*Manuscript will safety can frequently*
*be restored → be ensured* **and** *consulted*

We can combine this with the quantified facts we got earlier about certain manuscripts being restored.

Since we were told that
*most "culturally significant" manuscripts will be restored*

We can apply this conditional rule and derive that
*most "culturally significant" manuscripts are frequently consulted and their safety can be ensured during the restoration process.*

Since we were told that
some "dubious authenticity" manuscripts will be restored

We can apply this conditional rule and derive that
some "dubious authenticity" manuscripts are frequently consulted and their safety can be ensured during the restoration process.$lsat$),(2,$lsat$Goal$lsat$,$lsat$Look for anything provable, but it will probably involve applying "frequently consulted", "safety can be ensured", or both, to the one of the types of manuscripts that we were told are going to be restored.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

-- PT148-S3-Q25 (Notes-only)
INSERT INTO lr_explanation_steps (explanation_id, position, label, body)
SELECT e.id, v.p, v.l, v.b FROM (SELECT e.id FROM lr_explanations e JOIN lr_questions q ON q.id=e.question_id WHERE q.preptest=148 AND q.section=3 AND q.question_number=25 AND e.style IN ('single','standard') AND EXISTS (SELECT 1 FROM lr_explanation_choice_notes n WHERE n.explanation_id=e.id) AND NOT EXISTS (SELECT 1 FROM lr_explanation_steps s WHERE s.explanation_id=e.id) ORDER BY (e.style='single') DESC LIMIT 1) e, (VALUES (0,$lsat$Conclusion$lsat$,$lsat$The perception that direct-mail advertising is bad for the environment is misguided.
(i.e. direct-mail advertising is **not** bad for the environment)$lsat$),(1,$lsat$Evidence$lsat$,$lsat$Because of direct-mail advertising, millions of people buy products by phone or online. These products would otherwise require use of a car to go buy, and the car would add pollutants to the air.$lsat$),(2,$lsat$Evaluate$lsat$,$lsat$The author's argument is that direct-mail creates a **Net Gain** for the environment (or at worst it's neutral).

She thinks that there is an environmental "savings" happening because people are buying products that are then shipped to their house, rather than driving to the store to buy them.

We have to analyze all the environmental tradeoffs between the world with direct-mail advertising and the one without.

With direct-mail, they aren't driving to the store to pick up the toaster they ordered, but isn't Target driving the toaster to their house? Are we sure that the exhaust saved by the customer not driving to pick up the toaster isn't offset by the exhaust used by the Target delivery driver bringing it to their house?

Maybe personal vehicles are more likely to be electric / low-emission, whereas delivery trucks are more likely to be gas-guzzling / high-emission.

What if it's less environmentally efficient for me to have Target and Pier 1 and Bed, Bath, & Beyond all deliver me stuff than for me to get in my car and drive to the shopping center that has all of them in one place.

We also have to consider the environmental harm of all the paper that goes into sending out the direct-mail ads. What resources are used to make those ads? What damage is potentially done by all the direct-mail trash?$lsat$),(3,$lsat$Goal$lsat$,$lsat$The argument would be weakened if we could say "the practice of direct-mail has [this environmental cost] that wouldn't exist in a world without direct-mail advertising."

So we can strengthen this argument by ruling out any potential environmental cost.

We can also strengthen by learning any information that makes direct-mail sound more environmentally friendly, or that makes the direct-mail World seem more environmentally friendly than the world without direct-mail.$lsat$)) v(p,l,b)
ON CONFLICT DO NOTHING;

