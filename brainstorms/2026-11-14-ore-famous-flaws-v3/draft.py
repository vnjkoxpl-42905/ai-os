from pathlib import Path
import copy
import build as b

practice = {
"nec": ("A library course teaches everyone who takes it how to use the archive. Mina knows how to use the archive. She must have taken the course.", "Mina could have learned from a librarian. The rule gives us one way to learn.", "treats a way to learn the archive as the only way to learn it", "takes a failed argument for taking the course as proof Mina skipped it", "Nobody's argument was shown to fail.", "assumes everyone who uses the archive has mastered every library service", "The conclusion concerns the course. It makes no claim about other services."),
"causal": ("Students who study in the library finish more assignments. Studying in the library must make students finish more assignments.", "Students who plan their work might both choose the library and finish more. The pattern leaves that explanation open.", "treats a pattern as proof of what caused it", "uses library visitors to estimate how often all students visit the library", "Nobody estimates how often students visit.", "claims that each library visitor finishes every assignment", "The argument compares groups. It makes no claim about every visitor."),
"part": ("Each track on the album is short. So the album must be short.", "Twenty short tracks can add up to a long album.", "attributes a feature of each track to the album as a whole", "uses a few tracks to estimate the length of the remaining tracks", "The premise covers every track.", "assumes a short album contains only short tracks", "That would go from the album to its tracks."),
"unproven": ("We found no record that the tree was planted in 1902. It must have been planted in another year.", "The record could be missing even if the tree was planted in 1902.", "takes missing evidence for a claim as proof that the claim is false", "rejects the planting date because a historian has a reason to lie", "There's no attack on a historian.", "assumes the planting record gives two different dates", "The argument says no record was found."),
"adhom": ("A bus driver says the new route would cut travel time. Drivers want the route changed, so her claim is false.", "The driver can want the change and be right about travel time.", "dismisses a claim because its source has a stake in the outcome", "assumes that every rider supports the change because a few riders do", "The conclusion is about travel time.", "accepts a claim solely because its source is an expert", "The driver’s claim is dismissed."),
"sampling": ("Everyone I asked at the chess club wants a chess tournament. So most students at school want one.", "Chess club members have more reason to want a chess tournament than students chosen across the school.", "draws a conclusion about the school from a group unlikely to represent it", "assumes a tournament would cause more students to join the chess club", "The conclusion predicts no effect on membership.", "assumes that what is true of the school as a whole is true of each club member", "The inference runs from the club members to the wider school."),
"appeal": ("A famous actor says the old bridge can support trucks. The city can safely reopen it to trucks.", "The actor might know bridges. The argument gives us no reason to think so.", "relies on someone whose credibility on the issue is never established", "rejects a safety warning because its author would benefit from repairs", "No warning is rejected.", "assumes that each component is safe because the bridge is safe", "The conclusion concerns the bridge itself."),
"circular": ("This is the most reliable bus route. Every other route is less reliable than this one.", "To accept that every other route is less reliable, you already have to accept that this route is the most reliable.", "offers the conclusion in different words as its support", "predicts reliability from too few rides", "There are no observations about rides.", "assumes that popularity makes a route reliable", "The premise says nothing about popularity."),
"contradiction": ("A poll of three riders cannot tell us what most riders want. That same poll proves that most riders want later buses.", "The author rules out exactly the inference they then draw.", "takes inconsistent positions about what the poll can establish", "treats support for later buses as the cause of higher ridership", "The argument makes no claim about ridership changing.", "rejects the poll because riders have a stake in the schedule", "The objection concerns what the poll can establish."),
"equiv": ("A feather is light. Light is what lets us see in a dark room. So a feather can help us see in the dark.", "The first light means low in weight. The second means illumination.", "uses the same word in two different senses", "assumes every part of a feather weighs as much as the whole feather", "The argument never discusses parts of a feather.", "generalizes from one feather to every feather", "The conclusion concerns the feather in the premise."),
}

versions = {
"quick-reference": ("Keep this beside your practice", "Find the conclusion. Say what the evidence actually shows. Then name the flaw in your own words.", "Name the flaw before opening the explanation."),
"guided": ("Work through the reasoning", "Underline what the author wants you to believe. Then ask what would have to be true for the evidence to get you there.", "Say what the evidence gives you. What would you still need to know?"),
"choices": ("When two choices sound right", "Say the flaw before reading the choices. If two sound right, put each in plain words using the people and things in the argument.", "Say the flaw first. Then check what each choice says happened."),
}
original_how = b.how
original_question = b.question
b.C.HOW["said"] = ("You had it down to A and E. A says the counselor treats a way to get a motive as something you need to get one. E says the counselor took apart somebody else's argument and called their conclusion false. Where did the counselor do that? The counselor gave reasons for harsh criticism. There was no other argument to take apart.")
b.C.NEXT["steps"] = [
    ("Keep the list beside you during flaw practice.", "Name the mistake before reading the choices. You’ll get quicker as you see the same mistakes again."),
    ("Review every choice.", "For each one you ruled out, say what it describes and point to where that would have happened in the argument."),
]
for f in b.C.FLAWS:
    if f["q"] == "nec":
        f["said"] = "A guaranteed way is not the only way. You asked why it had to be harsh criticism. Gentle criticism could give someone a motive too. The word “cause” in a choice doesn't tell you which mistake the counselor made."
    if f["q"] == "causal":
        f["why"] = ["Soldiers tend to be fit. The author says recruiters chose them for their fitness. What else could explain the pattern? Training could have made them fit. People who play sports might also be more likely to enlist. Sometimes a pattern can be a coincidence."]
    if f["q"] == "unproven":
        f["lookalike"]["tell"] = "Which claim does the author treat as settled? The same mistake can run in either direction."
for mode, (heading, lede, instruction) in versions.items():
    b.C.LESSON_ID = "ore-famous-flaws-" + mode
    b.C.HERO["lede"] = lede
    b.C.HOW["h2"] = heading
    b.C.HOW["intro"] = "Put an abstract choice in plain words. Use the people and things in the argument."
    def question(f):
        stimulus, reason, right, d1, e1, d2, e2 = practice[f["q"]]
        if mode != "choices":
            prompt = "What does the evidence show?" if mode == "guided" else "What did the author assume?"
            first = f'<details><summary>{prompt}</summary><p>{b.e(stimulus.split(". ")[0])}.</p></details>' if mode == "guided" else ""
            return f'<div class="q" style="padding:18px"><p class="plabel">Practice</p><p>{b.e(instruction)}</p><div class="passage">{b.e(stimulus)}</div>{first}<details><summary>Check your reasoning</summary><p>{b.e(reason)}</p></details></div>'.replace('class="q"', 'class="q practice"').replace('class="q practice"', 'class="practice" style="background:var(--card);border:1px solid var(--edge);border-radius:12px;margin-top:20px"').replace('" style="padding:18px"', ';padding:18px"')
        index = next(i for i, item in enumerate(b.C.FLAWS) if item["q"] == f["q"])
        items = [(right,reason),(d1,e1),(d2,e2)]
        offset = index % 3
        items = items[-offset:] + items[:-offset] if offset else items
        letters = dict(zip("ABC",items))
        key = "ABC"[offset]
        b.Q[f["q"]] = dict(stimulus=stimulus, questionStem="The argument is flawed because it", answerChoices={k:v[0] for k,v in letters.items()}, correctAnswer=key)
        b.C.EXPLAIN[f["q"]] = {"right":reason, **{k:v[1] for k,v in letters.items()}}
        return original_question(f).replace("Try a real one","Practice").replace("A real LSAT question. Say the flaw in your own words first, then pick the choice that describes it.",instruction)
    b.question = question
    b.main()
    path = Path("out/famous-flaws.html")
    html = path.read_text(encoding="utf8")
    if mode != "choices":
        html = html.replace("</head>", "<style>.fi-progress,.fi-sr{display:none}.practice summary{cursor:pointer;font-weight:600}.practice details{margin-top:12px}</style></head>")
    out = Path("out") / (mode + ".html")
    out.write_text(html,encoding="utf8")
    assert html.count('class="plabel">Practice') == 10
    assert "Try a real one" not in html
