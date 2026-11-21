# All student-visible prose for the Famous Flaws note (Ore, v3).
# Example markup: <ev>evidence</ev>, <con>conclusion</con>, <j>the jump word</j>.

LESSON_ID = "ore-2026-11-14-famous-flaws-v3"

HERO = {
    "kicker": "Famous Flaws",
    "title": "Famous Flaws",
    "lede": ("Ten famous flaws, grouped by how often they show up. Keep this sheet beside you while you practice, and name the flaw before you read the choices."),
}

HOW = {
    "kicker": "How to use it",
    "h2": "Which flaw is that?",
    "intro": "De-abstractify the choices. Put them in plain words, using the people and things in the argument.",
    "steps": [
        ("What's the conclusion?", "What does the author want me to believe?"),
        ("What did the evidence actually show?", "Keep that separate from what the author concludes."),
        ("Which flaw is that?", "Then ask which choice says it in plain words. Review the wrong choices too."),
    ],
    "legend": 'In the examples, <ev>green</ev> marks the evidence, <con>gold</con> marks the conclusion, and <j>red</j> marks the words that connect them.',
    'said': "You asked how to be sure of an answer when you're stuck between two. That's the right question, and here's the answer: put both choices in plain words and check them against the argument, then build familiarity by reviewing the wrong choices too.",
}

TIERS = [
    {
        "id": "tier-common",
        "kicker": "The five most common",
        "h2": 'Start with these five',
        "p": 'Over half of flaw questions fall into these five fallacies. Learn what each one does, then look for it in the argument.',
        "img": "divider-common",
        "alt": "Ink drawing of five blank index cards in a row on a desk, a magnifying glass resting on the first card, a cup of coffee and a pencil nearby.",
    },
    {
        "id": "tier-less",
        "kicker": "Not-so-common",
        "h2": 'Know what the other five describe',
        "p": 'These show up less often as the flaw. Some, like the appeals, mostly show up as wrong answers.',
        "img": "divider-less-common",
        "alt": "Ink drawing of a wooden cabinet of curiosities with open drawers holding a mirror, a snake eating its tail, a balance scale, a megaphone and a mask.",
    },
]

# Each flaw: tier index, id, name, what, examples (list), why (list of paragraphs), whatif, wording (list), lookalike, question key
HANDOUT_DEF = {'necessary-vs-sufficient': 'Presenting a conditional rule and then using it in an illegal backwards or opposite fashion to get to the conclusion (i.e. an illegal reversal or illegal negation). This is frequently the actual flaw on Flaw and Parallel Flaw questions.', 'causal': 'Overconfidently concluding one possible causal interpretation of a curious fact, usually a correlation, when other possible interpretations exist.', 'part-vs-whole': 'Assuming that a trait that is true of each part of a collective is therefore true of the whole, or vice versa.', 'unproven-vs-proven-false': "Acting like X must be false, either because there's no evidence that X is true, or because someone made a faulty argument for X being true.", 'ad-hominem': 'Dismissing a point of view because the source has a biased interest or has conflicting past behavior.', 'sampling': 'Extrapolating/generalizing too readily from a small sample, while failing to consider that the sample might be biased, too small, or unrepresentative.', 'inappropriate-appeal': 'Your evidence is a plea for sympathy, you cite an "authority" without establishing credibility, or you favor one source\'s opinion over another source\'s, without justifying your pick. Almost always wrong answers:', 'circular-reasoning': 'The premise of an argument restates or assumes the conclusion.', 'internal-contradiction': 'Something the author says undermines or contradicts something else they say.', 'equivocation': 'Using the same "term" or concept to mean two very different things.'}

FLAWS = [
    {
        "tier": 0, "id": "necessary-vs-sufficient", "name": "Necessary vs. Sufficient", "q": "nec",
        "what": HANDOUT_DEF['necessary-vs-sufficient'],
        "spot": 'A rule gets reversed or negated, or enough becomes required.',
        "img_alt": 'A person walks against a one-way arrow.',
        "examples": [
            "<ev>People who have seen “The 13th” have a great understanding of the US prison system.</ev> <j>Since</j> <ev>Megan still hasn’t seen that documentary,</ev> <con>she must have a poor understanding of the US prison system.</con>",
            "<ev>People who have seen “The 13th” have a great understanding of the US prison system. Jane understands the US prison system really well,</ev> <j>so clearly</j> <con>she has seen “The 13th.”</con>",
        ],
        "why": ['A guaranteed way is not the only way. Megan could understand the prison system without seeing the film. Jane could understand it for the same reason. Neither conclusion follows from the rule.'],
        "wording": [
            "takes a condition that is enough to bring about a result to be required for that result",
            "treats an event that can cause a certain result as though that event is necessary to bring about that result",
            "confuses a condition that is required for something with a condition that guarantees it",
        ],
        "lookalike": {
            "name": "Causal",
            "text": "takes a correlation between two things as proof that one causes the other",
            "tell": 'Enough becomes required here. A causal flaw instead decides what caused something.',
        },
        "diagram": "nec",
        'said': "You asked, “why is it only harsh criticism,” and suggested it could be gentle or constructive; that's exactly why enough doesn't mean required. You also said, “I saw the word cause,” which explains the first guess, but the word alone didn't identify the flaw.",
    },
    {
        "tier": 0, "id": "causal", "name": "Causal", "q": "causal",
        "what": HANDOUT_DEF['causal'],
        "spot": 'The evidence shows a pattern; the conclusion decides what caused it.',
        "img_alt": 'A proud rooster crows at sunrise.',
        "examples": [
            "<ev>People who are enlisted in the military are more likely than those who haven't to have excellent physiques.</ev> <j>Evidently,</j> <con>military recruitment officers select their future soldiers in large part based on the applicant’s fitness and strength.</con>",
        ],
        "why": ['Soldiers tend to be fit. Does that tell us recruiters chose them for their fitness? Training could have made them fit. Or another factor could explain both their fitness and their choice to enlist.'],
        "wording": [
            "takes for granted that because two things occur together, one must have caused the other",
            "fails to consider that the supposed effect may actually be the cause",
            "overlooks the possibility that some other factor is responsible for both",
        ],
        "lookalike": {
            "name": "Sampling",
            "text": "uses evidence drawn from a sample that is unlikely to be representative",
            "tell": 'Sampling questions who was counted. Causal questions why the pattern happened.',
        },
        "diagram": "causal",
    },
    {
        "tier": 0, "id": "part-vs-whole", "name": "Part vs. Whole", "q": "part",
        "what": HANDOUT_DEF['part-vs-whole'],
        "spot": 'A trait moves between the parts and the whole.',
        "img_alt": 'A wall of polished bricks leans to one side.',
        "examples": [
            "<ev>The military is part of the government, and the military is conducted with lots of honor and discipline.</ev> <j>Thus,</j> <con>the government overall is conducted with lots of honor and discipline.</con>",
            "<j>Since</j> <ev>rat poison is very harmful if ingested,</ev> <con>each ingredient in rat poison would be very harmful if ingested.</con>",
        ],
        "why": ["The military's discipline doesn't tell us how the rest of the government operates. The poison example goes the other way. A harmful mixture could contain a harmless ingredient used as bait."],
        "wording": [
            "illicitly presumes that a whole must lack a certain quality if all of its parts lack that quality",
            "presumes that a characteristic of a group as a whole is shared by each member of that group",
            "reaches a conclusion about one member of a group merely on the basis of the performance of the group as a whole",
        ],
        "lookalike": {
            "name": "Sampling",
            "text": "takes the condition of one member of a category to be representative of the category in general",
            "tell": 'Sampling uses some people to speak for others. Part versus whole concerns the parts and what they make up together.',
        },
        "diagram": "part",
        'said': "You put it plainly: just because the team does well overall doesn't mean every player does well. That's the whole idea: the team's performance doesn't establish each player's performance.",
    },
    {
        "tier": 0, "id": "unproven-vs-proven-false", "name": "Unproven vs. Proven False", "q": "unproven",
        "what": HANDOUT_DEF['unproven-vs-proven-false'],
        "spot": 'The author rejects a claim because proof is missing or an argument for it failed.',
        "img_alt": 'A stamp and magnifying glass sit beside an empty evidence box.',
        "examples": [
            "<ev>Billy says that his uncle was related to Elvis, but he hasn't been able to connect them on Ancestry.com.</ev> <j>Thus,</j> <con>Billy’s uncle was not related to Elvis.</con>",
            "<ev>Some claim that the Atlanta Braves should change their name because they are the only major sports team that still has a Native American mascot. However, the Chicago Blackhawks still have a Native American mascot.</ev> <j>Thus,</j> <con>the Braves should not change their name.</con>",
        ],
        "why": ["A lack of evidence is not evidence of lacking. Failing to find the family connection doesn't prove there isn't one. The Braves argument points out a problem with one reason for changing the name. That doesn't settle whether the name should change."],
        "wording": [
            "takes for granted that something that has not been proven to be true is for that reason shown to be false",
            "takes lack of evidence for a claim as evidence undermining that claim",
            "infers that a claim is false merely on the grounds that no satisfactory evidence for it has been offered",
        ],
        "lookalike": {
            "name": "The mirror image",
            "text": "concludes that a claim is true merely on the grounds that it has not been proven false",
            "tell": 'Ask whether the author lacks proof or attacks the person making the claim.',
        },
        "diagram": "unproven",
        'said': "You compared it to saying, “because I can't prove you're innocent, you're guilty.” You were right: failing to prove one side doesn't prove the other.",
    },
    {
        "tier": 0, "id": "ad-hominem", "name": "Ad Hominem", "q": "adhom",
        "what": HANDOUT_DEF['ad-hominem'],
        "spot": 'The author dismisses a claim by attacking its source.',
        "img_alt": 'A paper airplane hits a speaker in the hat.',
        "examples": [
            "<ev>My friend Sameer says that social workers would be better at responding to domestic abuse calls than would armed police officers.</ev> <con>But we can ignore this notion,</con> <j>since</j> <ev>Sameer is a social worker and so his industry would benefit were cities to make this switch.</ev>",
            "<ev>My running coach tells me I should stretch before every run, but she skipped stretching for twenty years.</ev> <j>So</j> <con>I can ignore her advice about stretching.</con>",
        ],
        "why": ["Sameer could benefit from the change and still be right. His interest doesn't tell us whether social workers would respond better. The coach could fail to follow her own advice and still give good advice."],
        "wording": [
            "attacks the people making an argument rather than addressing their argument",
            "disputes a claim on the basis of a supposed motive for making the claim rather than by assessing the evidence relevant to the claim",
            "rejects a claim merely on the grounds that its proponent holds another view inconsistent with it",
        ],
        "lookalike": {
            "name": "Inappropriate Appeal",
            "text": "relies on the word of a scholar who is unqualified in the area in question",
            "tell": 'An appeal trusts a source without support. Ad Hominem dismisses a claim by attacking its source.',
        },
        "diagram": "adhom",
    },
    {
        "tier": 1, "id": "sampling", "name": "Sampling", "q": "sampling",
        "what": HANDOUT_DEF['sampling'],
        "spot": 'Evidence about a few people becomes a claim about others.',
        "img_alt": 'A spoon selects terracotta marbles from a mixed jar.',
        "examples": [
            "<ev>Charlie, a staunch Republican, is from San Francisco and works for a theater company.</ev> <j>Since</j> <ev>Shelia is also from San Francisco and also works for a theater company,</ev> <con>she is probably a staunch Republican too.</con>",
            "<con>Today’s youth prefer comic books to literature.</con> <j>After all,</j> <ev>at a survey conducted at last year’s Comic-Con, over 85% of the young people surveyed reported liking comic books much more than novels.</ev>",
        ],
        "why": ["Sharing a city and a workplace doesn't establish a shared political view. And Comic-Con attracts people who like comics. Their preferences don't tell us what young people overall prefer."],
        "wording": [
            "relies on the opinions of a group unlikely to be representative of the group at issue in the conclusion",
            "bases an overly broad generalization on just a few instances",
            "treats high school students from a particular medium-sized city as if they are representative of high school students nationwide",
        ],
        "lookalike": {
            "name": "Part vs. Whole",
            "text": "assumes that what is true of each member of a group is true of the group as a whole",
            "tell": 'Ask whether the conclusion concerns other people or what the parts make up together.',
        },
        "diagram": "sampling",
    },
    {
        "tier": 1, "id": "inappropriate-appeal", "name": "Inappropriate Appeal", "q": "appeal",
        "what": HANDOUT_DEF['inappropriate-appeal'],
        "spot": "Sympathy or a source's opinion stands in for support, with no reason to trust that source.",
        "img_alt": 'A cat with a stethoscope sits on medical books.',
        "examples": [
            "<ev>I know I was speeding, Officer, but</ev> <con>you shouldn’t give me a ticket</con> <j>because</j> <ev>it would ruin my Anniversary.</ev>",
            "<ev>The state geologist says the hillside behind the school is stable.</ev> <con>But she’s wrong,</con> <j>for</j> <ev>my neighbor says the ground there shifts.</ev>",
        ],
        "why": ["Ruining an anniversary gives the officer a reason to feel sympathy. It doesn't show the ticket is unwarranted. Why trust the neighbor over the geologist? The argument never establishes the neighbor's credibility or gives a reason to prefer that source."],
        "wording": [
            "treats a claim as true merely because many people believe it",
            "accepts the view of someone who has no expertise on the matter at hand",
            "appeals to emotion rather than offering evidence for its conclusion",
        ],
        "lookalike": {
            "name": "Ad Hominem",
            "text": "attacks the person making the claim at issue rather than addressing the claim",
            "tell": 'An appeal trusts a source without support. Ad Hominem dismisses a claim by attacking its source.',
        },
        "diagram": "appeal",
    },
    {
        "tier": 1, "id": "circular-reasoning", "name": "Circular Reasoning", "q": "circular",
        "what": HANDOUT_DEF['circular-reasoning'],
        "spot": 'Accepting the premise already requires accepting the conclusion.',
        "img_alt": 'A dog chases its tail.',
        "examples": [
            "<con>The LSAT is clearly the hardest grad school test,</con> <j>because</j> <ev>all the other tests people take to go to grad school pale in comparison to the difficulty of the LSAT.</ev>",
        ],
        "why": ['Saying every other graduate test is easier already says the LSAT is the hardest. Would you already have to accept the conclusion to accept the premise? Here, yes. A weak or off-topic premise is a different problem.'],
        "wording": [
            "restates its conclusion and offers it as a reason",
            "presupposes the truth of the conclusion it is attempting to establish",
            "takes for granted the very conclusion it is trying to prove",
        ],
        "lookalike": {
            "name": "An ordinary assumption",
            "text": "presupposes without justification that one event prevents another",
            "tell": "It's circular only if accepting the premise already requires accepting the conclusion.",
        },
        "diagram": "circular",
    },
    {
        "tier": 1, "id": "internal-contradiction", "name": "Internal Contradiction", "q": "contradiction",
        "what": HANDOUT_DEF['internal-contradiction'],
        "spot": 'The author relies on two claims that cannot both hold.',
        "img_alt": 'Two signpost arrows point in opposite directions.',
        "examples": [
            "<ev>LSAT is an incredibly challenging test for anyone who takes it.</ev> <j>However,</j> <con>if you commit to Eddie Spaghetti’s Steady LSAT Readiness protocol, you will soon be feeling like LSAT is no harder than a kindergarten spelling quiz.</con>",
        ],
        "why": ["The word 'feeling' matters. A challenging test can feel easy to someone who's prepared, so the example can be read as consistent. A true contradiction requires two claims that cannot both hold. In the PCB question below, the author rejects any scientifically valid inference from a study, then uses that study as proof."],
        "wording": [
            "makes two claims that cannot both be true",
            "its conclusion contradicts an implicit principle on which an earlier part of the argument is based",
            "relies on premises that cannot all be true",
        ],
        "lookalike": {
            "name": "Ad Hominem",
            "text": "rejects a claim merely on the grounds that its proponent holds another view inconsistent with it",
            "tell": "Whose claims conflict? Here they're claims the author relies on together.",
        },
        "diagram": "contradiction",
    },
    {
        "tier": 1, "id": "equivocation", "name": "Equivocation", "q": "equiv",
        "what": HANDOUT_DEF['equivocation'],
        "spot": 'The same term changes meaning between the evidence and conclusion.',
        "img_alt": 'A bench sits on a riverbank opposite a bank building.',
        "examples": [
            "<ev>Some question whether Egypt condones Romania’s recent military buildup on their eastern border.</ev> <j>But clearly</j> <con>Egypt sanctions this activity,</con> <j>since</j> <ev>in the weeks following the Romanian military’s actions, Egypt issued sanctions against Romania.</ev>",
        ],
        "why": ["'Sanction' can mean approve, or it can refer to a penalty. Here the evidence says Egypt imposed penalties. Does that establish approval? No, the conclusion uses the other meaning."],
        "wording": [
            "relies on a word that is used with two different meanings",
            "uses a key term in two different senses",
            "overlooks the possibility that the speaker is referring to two different kinds of right",
        ],
        "lookalike": {
            "name": "A shift in terms",
            "text": "makes an irrelevant shift from discussing retail prices to discussing production costs",
            "tell": 'Find the term and state both meanings. Switching to a different term is a different problem.',
        },
        "diagram": "equiv",
    },
]

# Explanations for each real question: right = why the correct choice; others = per wrong letter
EXPLAIN = {
    "nec": {
        "right": "This is the harsh-criticism question we worked through. Unpleasant criticism provides a motive, so harsh criticism is enough to provide one. But the counselor concludes it's the only way. A guaranteed way is not the only way: sufficient has become necessary.",
        "B": "What other goals can criticism serve? That doesn't settle whether harsh criticism is required for change. The unsupported restriction is “only.”",
        "C": "The counselor doesn't say everyone with a motive will change. The error is making harsh criticism the only way to provide that motive.",
        "D": "A motive to do something and a motive to avoid something aren't confused here. As you noticed, the argument never discusses avoiding anything.",
        "E": "What argument did the counselor refute? None. The counselor builds a case for harsh criticism without tearing down someone else's evidence. This choice describes a move that never happened.",
    },
    "causal": {
        "right": "Anxious people tend to have high blood pressure. That shows the two occur together. It doesn't establish which causes which: high blood pressure could make people anxious instead.",
        "A": "The argument tells us what the term means: nervous and anxious. A missing definition isn't what prevents the causal conclusion from following.",
        "B": "The traits don't have to be permanent for this argument. We need to ask whether occurring together establishes the proposed cause.",
        "C": "The correlation is evidence separate from the conclusion, so the argument isn't circular. The mistake is using that correlation to establish a cause.",
        "E": "Leaving out other traits doesn't by itself undermine a claim about anxiety and blood pressure.",
    },
    "part": {
        "right": "Ask how many copies the twelve titles could sell together. Even if no one title is likely to sell 100,000, their combined sales could pass 100,000. A limit on each title doesn't establish that limit on the company's total.",
        "A": "If the novel sold fewer copies, that would help the executive's conclusion. It wouldn't expose the mistake.",
        "B": "What happens to profit after 100,000 copies doesn't settle whether sales will reach 100,000.",
        "C": "The argument stays within one year. It doesn't switch from overall profitability to profitability in a particular year.",
        "E": "The argument says nothing about advertising. We can't identify it as the mistake here.",
    },
    "unproven": {
        "right": "There isn't a study linking ginseng to stress relief. That leaves the benefit unproved. It doesn't establish that the benefit is absent, so calling the claim false goes further than the evidence allows.",
        "A": "The author points to missing support for the claim. Nobody's credibility is attacked.",
        "C": 'No sample is used. The evidence is that a supporting study is missing.',
        "D": "Why people buy the tea doesn't tell us whether ginseng relieves stress.",
        "E": "The author rejects a claim about ginseng. Facts about other ingredients wouldn't settle that claim.",
    },
    "adhom": {
        "right": "What does the advisor's behavior in his youth tell us about this economic advice? The editorial never supplies that connection. It rejects the advice because of his past without assessing the advice itself.",
        "A": "The editorial doesn't discuss how the plan would be carried out, so that isn't the basis of its rejection.",
        "B": "The editorial doesn't ask us to accept anything out of fear.",
        "D": "This would be unproven versus proven false. The editorial's reason is the advisor's past, rather than a lack of evidence for the advice.",
        "E": "The advisor's past is a separate premise, so this isn't a restatement of the conclusion. The problem is rejecting advice on that basis.",
    },
    "sampling": {
        "right": "Who is included in “everyone I know”? A narrow group of acquaintances, who may have similar views. Their votes don't establish how the country voted.",
        "B": "The speaker's friends voted one way; the conclusion concerns the country. Those are different claims, so the premise doesn't simply repeat the conclusion.",
        "C": "The speaker doesn't attack the people who supported the proposal.",
        "D": "The argument concerns how people voted. It doesn't make a claim about how they should have voted.",
        "E": "The speaker isn't saying a belief is true because it's popular. The speaker uses acquaintances' votes to infer the country's votes.",
    },
    "appeal": {
        "right": "Does popularity establish accuracy? A book can sell well and still get the facts wrong. The evidence about popularity doesn't answer Jaaks's criticism about accuracy.",
        "A": "The author argues against Jaaks. Her word isn't being used to support the conclusion.",
        "B": "The author describes Jaaks as respected and doesn't attack her as a person.",
        "D": "The author doesn't draw a general conclusion from a sample. The move is from popularity to accuracy.",
        "E": "The author doesn't say other methods fail. The unsupported move is treating popularity as evidence of accuracy.",
    },
    "circular": {
        "right": "The author explains Cotrell's superior articles by assuming Cotrell couldn't have written anything better than average. But that's what the author is trying to prove. To accept this explanation for the articles, we'd already have to accept the conclusion about Cotrell.",
        "A": "The author does address the superior articles. The problem is explaining them away by assuming Cotrell couldn't have written them.",
        "B": "The superior articles aren't the basis of a generalization. The author dismisses them as evidence of Cotrell's ability.",
        "D": 'There are no experts whose views the argument relies on.',
        "E": 'No lapse in performance is mentioned. The articles being explained away are unusually good.',
    },
    "contradiction": {
        "right": 'First the author says no scientifically valid inference can be drawn from the study. Then the author says that study proves the PCB ban worked. Both claims cannot hold: using the study as proof requires drawing an inference from it.',
        "B": "The argument concerns PCBs. It doesn't make a claim about other chemicals.",
        "C": "The author says the study proves the result. That isn't a move from “not proved false” to “true.”",
        "D": "The ban came decades before the lower PCB levels. Those later levels couldn't have caused the earlier ban, so reversing cause and effect doesn't describe this argument.",
        "E": "Later health effects wouldn't settle whether the ban reduced exposure. Reduced exposure is what the conclusion concerns.",
    },
    "equiv": {
        "right": "Put “afford” in plain words each time. The mayor says the city lacks the money. The citizen says losing the building would cost the government too much respect. A cost in respect doesn't answer the objection about money; the meaning has changed.",
        "A": "The citizen offers a reason about keeping respect for the government by preserving history. The argument isn't based on emotion alone.",
        "C": "The citizen disagrees with the mayor. The mayor's authority isn't a reason for the citizen's conclusion.",
        "D": "The citizen accepts that restoration would be expensive. That isn't an unsupported assumption here.",
        "E": "The words this choice points to belong to the mayor. The citizen doesn't rely on them to make the case for restoration.",
    },
}

NEXT = {
    "kicker": "Your work",
    "h2": "What to do next",
    "steps": [
        ('Answer the ten questions in this note.', 'Keep the list beside you. Matching each argument to a flaw is how you learn what these mistakes look like in questions. Then review every choice, including the ones you ruled out.'),
        ('Start “Flaw - First Taste” when it opens on November 16.', "Name the flaw before reading the choices. If you're between two answers, put each in plain words and check what actually happened in the argument."),
        ('Do “Famous Flaw (Easier) Set 1” from November 18 and “Abstract + Flaw (set 1)” from November 20.', "Keep using the list as you practice. For each wrong choice, explain what flaw it describes and why that flaw isn't in this argument. Seeing those descriptions repeatedly is how you get familiar with the language."),
        ('Send me a message if a question still leaves you unsure.', "Tell me which two choices you're between and what you think each means, so we can work through the difference."),
    ],
}
