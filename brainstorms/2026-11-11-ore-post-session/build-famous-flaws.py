"""Three variations of Oreoluwa's Famous Flaws note, built from the Lanae shell.

Content source: Joshua's compiled Famous Flaws catalog (15 flaws in 3 groups):
  raw/sources/lsat-curriculum/.../Flaw and Famous Flaws/_HANDOFF/05_compiled_content_voiced.md
  lsatu/src/bootcamps/fallacy-flaw-v2/data/flaws.ts
Shell: wiki/homework-assigning/model-note/note-shell.html (CSS and script are never edited).

Run: py -I brainstorms/2026-11-11-ore-post-session/build-famous-flaws.py
"""
import re
from pathlib import Path

ROOT = Path(r"C:/Users/Joshu/dev/ai-os")
SHELL = ROOT / "wiki/homework-assigning/model-note/note-shell.html"
OUT = ROOT / "brainstorms/2026-11-11-ore-post-session"

shell = SHELL.read_text(encoding="utf-8")
HERO_START = shell.index('<header class="hero">')
MAIN_END = shell.index("</main>") + len("</main>")


def build(lesson_id, title, body):
    out = shell[:HERO_START] + body + shell[MAIN_END:]
    out = re.sub(r'(<meta name="lsatu-interactive-lesson" content=")[^"]*(">)', r"\g<1>%s\g<2>" % lesson_id, out, count=1)
    out = re.sub(r"<title>.*?</title>", "<title>%s</title>" % title, out, count=1, flags=re.S)
    assert "{{" not in out, "unfilled slot"
    return out


def chip(kind, item, stamp, ans):
    return (
        '<div class="chip" data-k="%s" role="button" tabindex="0" aria-expanded="false">'
        '<span>%s</span><span class="stamp" aria-hidden="true">%s</span><span class="ans">%s</span></div>'
        % (kind, item, stamp, ans)
    )


def card(cls, name, what, looks, test):
    return (
        '<div class="kind %s" data-tilt="5"><span class="bar"></span><div class="name">%s</div>'
        '<p class="what">%s</p><div class="words"><b>Looks like</b> <span>%s</span></div>'
        '<div class="test"><b>Test</b>%s</div></div>' % (cls, name, what, looks, test)
    )


def table(headers, rows):
    head = "".join("<th>%s</th>" % h for h in headers)
    body = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return '<div class="table-wrap"><table class="t"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, body)


def opposite(a_name, a_text, b_name, b_text):
    return '<div class="opposite"><div><b>%s</b>%s</div><div><b>%s</b>%s</div></div>' % (a_name, a_text, b_name, b_text)


def gate(sw1, sw2, v0, v1, v2, v3, hint):
    return (
        '<div class="gate" data-state="0"><h3>Try the two checks</h3><p class="hint">%s</p><div class="gate-body">'
        '<button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>%s</span></button>'
        '<button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>%s</span></button>'
        '<div class="verdict" role="status"><i class="lamp"></i><span class="v0">%s</span><span class="v1">%s</span><span class="v2">%s</span><span class="v3">%s</span></div>'
        "</div></div>" % (hint, sw1, sw2, v0, v1, v2, v3)
    )


def section(kicker, h2, inner):
    return '<section><div class="wrap"><div class="sec-kicker">%s</div><h2>%s</h2>%s</div></section>' % (kicker, h2, inner)


def steps(items, todo=False):
    return '<ol class="steps%s">%s</ol>' % (" todo" if todo else "", "".join("<li><b>%s</b> %s</li>" % i for i in items))


def callout(tag, text, trap=False):
    return '<div class="callout%s"><span class="tag">%s</span> %s</div>' % (" trap" if trap else "", tag, text)


def stage(base_label, base, c2, c1):
    return (
        '<div class="stage" aria-hidden="true"><div class="stack" data-tilt="10">'
        '<div class="slab base"><i>%s</i><b>%s</b></div><div class="slab c2"><i>CHECK 2</i><b>%s</b></div>'
        '<div class="slab c1"><i>CHECK 1</i><b>%s</b></div></div></div>' % (base_label, base, c2, c1)
    )


# --------------------------------------------------------------- shared content
SESSION_ITEMS = [
    ("describe", "A doctor's note gets you excused from the exam. Jo has no note, so she will not be excused.", "Necessary vs. Sufficient",
     "Necessary vs. Sufficient. A note is enough to get you excused. The author treats it as required. Jo may have another reason."),
    ("assume", "People who read a lot are less likely to drop out of high school. So reading keeps students in school.", "Causal",
     "Causal. The evidence says two things go together. The conclusion picks one cause. Richer parents could drive both, or students who stay in school could read more."),
    ("object", "The restaurant has a great reputation, so every dish on its menu must be great.", "Part vs. Whole",
     "Part vs. Whole. A trait of the whole is pushed onto each part. One dish can be poor in a great restaurant."),
    ("neutral", "Nobody has shown the old footbridge is unsafe, so it must be safe.", "Unproven vs. Proven False",
     "Unproven vs. Proven False. Nobody showing it is unsafe is not the same as someone showing it is safe."),
    ("describe", "Maya says the new bus route is too slow, but she drives for a taxi company, so we can ignore her.", "Ad Hominem",
     "Ad Hominem. The author rejects the claim by pointing at Maya's job. Whether the route is slow is a separate question."),
    ("assume", "Three students I asked at the gym said the library is too quiet, so students at this school find the library too quiet.", "Sampling",
     "Sampling. Three students at the gym are a small, unrepresentative sample of a whole school."),
]

TRAP_ITEMS = [
    ("neutral", "This is the hardest graduate school test, because every other graduate school test is easier than this one.", "Circular Reasoning",
     "Circular Reasoning. The reason repeats the conclusion in other words. Usually the trap, but here it is real because the argument says the same thing twice."),
    ("neutral", "Some question whether Egypt condones Romania's military buildup. Clearly it sanctions the buildup, since it issued sanctions against Romania afterward.", "Equivocation",
     "Equivocation. Sanctions means approves in one place and penalizes in the other. The same word does two jobs."),
    ("neutral", "Most people believe the Earth is the center of the universe, so it must be.", "Inappropriate Appeal",
     "Inappropriate Appeal. Popularity is the only reason given. It is sometimes the answer, so check what the author actually leans on."),
    ("neutral", "The test is incredibly hard for anyone. However, follow this plan and it will feel no harder than a kindergarten spelling quiz.", "Internal Contradiction",
     "Internal Contradiction. The two claims cannot both be true. This one is almost never the answer, so be very suspicious of it in a choice."),
]

JOSHUA_ITEMS = [
    ("assume", "This diet helps you lose weight. So it will make you healthier.", "Sleight of Hand",
     "Sleight of Hand. Healthier is a new term in the conclusion. Losing weight is not basically the same thing. Nothing is basically the same on the LSAT."),
    ("assume", "We should elect John because he is a great public speaker.", "Sleazy Sales Pitch",
     "Sleazy Sales Pitch. You hear one strength of one option and nothing about the other candidate or about any drawback."),
    ("assume", "Everyone should switch to the new low-fat diet because it will help them lose weight.", "Universal Desires Assumption",
     "Universal Desires Assumption. Some people want to gain weight and some do not care. The conclusion assumes everyone shares the goal."),
    ("assume", "This car gets 50 miles per gallon, so it is the best car on the market.", "Value Assumptions",
     "Value Assumptions. Best is a loaded word the evidence never defined. Good mileage is one fact, not a verdict."),
    ("assume", "We should switch to solar energy to save money on electricity.", "Secret Downsides",
     "Secret Downsides. Only the benefit is named. The cost of installation could erase the savings."),
]

NEXT_STEPS = [
    ("Flaw - First Taste.", "Read the Before you start note first. Then do the seven guided questions. Name the flaw before you read any choice, then find the choice that says it."),
    ("Keep this note open beside every flaw question.", "Write the name of the flaw next to your answer. When you miss one, write which flaw it was. In a week the pattern in your misses will show."),
    ("Read one or two Reading Comprehension passages every other day.", "Keep it light. The goal is to get used to the density of the language before we start the RC modules. Any passage works."),
    ("Send me a message on the platform if you have a question.", "I'll be able to get back to you."),
]

STEPS_READ = [
    ("Find the conclusion and the evidence.", "The conclusion is what the author wants you to accept. The evidence is the reason."),
    ("Say what the author did, in your own words.", "\"The evidence shows one route works. The author says it is the only route.\" Do this before you read A."),
    ("Find it in the list.", "Look for the tell: the signal in the stimulus that gives the flaw away."),
    ("Then read the choices looking for it.", "The choice will say it in abstract words. You are matching, not deciding from scratch."),
]

QUOTE_COMMON_SENSE = "You told me these felt like common sense: <em>\"It is kind of like a common sense thing.\"</em> That is right. The names are new. The reasoning is yours. A name gives you something to look for."

# =============================================================== VARIATION 1: catalog
G1 = table(
    ["Flaw", "What the author does", "The tell"],
    [
        ["Necessary vs. Sufficient<br><em>In our session</em>",
         "Mistakes what is required for what is guaranteed. Runs an if-then rule backwards, or negates it.<br><em>People who have seen the documentary understand the prison system. Megan has not seen it, so she does not understand it.</em>",
         "An if-then rule in the evidence. The conclusion reverses it or negates it. The choice says: treats a condition under which something occurs as the only condition under which it occurs."],
        ["Causal<br><em>In our session</em>",
         "Picks one cause for a correlation when other explanations exist. The author ignores reverse cause, a third factor and coincidence.<br><em>People who enlist in the military are more likely to have excellent physiques. So recruiters must select applicants for fitness.</em>",
         "A correlation or coincidence in the evidence, then one cause in the conclusion. The choice says: fails to consider that a third factor may explain the correlation."],
        ["Part vs. Whole<br><em>In our session</em>",
         "Assumes what is true of the parts is true of the whole, or the reverse.<br><em>Rat poison is harmful if swallowed, so each ingredient in it must be harmful if swallowed.</em>",
         "A trait is shown for every member and concluded for the group, or the other way round. The choice says: infers from a property of a collective a property of its members."],
        ["Unproven vs. Proven False<br><em>In our session</em>",
         "Treats a lack of evidence as evidence of the opposite, or knocks down a weak argument and calls the claim false.<br><em>Billy says his uncle was related to a famous singer, but he cannot find the link on a genealogy site. So the uncle was not related to the singer.</em>",
         "The author points out missing evidence, then concludes the opposite. The choice says: takes an absence of evidence to be evidence of absence."],
        ["Ad Hominem",
         "Dismisses a claim by attacking the person who made it, not the claim. On the LSAT it is often a point about bias or self-interest, not an insult.<br><em>Sameer says social workers would handle domestic abuse calls better than armed police. We can ignore him, since he is a social worker and would benefit.</em>",
         "The author rejects a claim by pointing at the speaker's bias, motive or identity. The choice says: attempts to undermine credibility instead of addressing the argument."],
        ["Sampling",
         "Generalizes from a sample that is too small, biased or unrepresentative.<br><em>Today's youth prefer comic books to novels. After all, 85% of the young people surveyed at a comic convention said so.</em>",
         "A study, a survey or a few examples, then a sweeping claim about a much larger group. The choice says: generalizes from a sample unlikely to be representative."],
    ],
)

G2 = table(
    ["Flaw", "What it is", "Why it is usually the trap"],
    [
        ["Circular Reasoning", "The premise restates the conclusion in other words.", "Real circular reasoning is short and repeats itself. When a choice says circular, check that the stimulus really says the same thing twice."],
        ["Internal Contradiction", "Two things the author says cannot both be true.", "Almost never the answer. Be very suspicious."],
        ["Equivocation", "One word means two different things in the same argument. Sanctions can mean approves and penalizes.", "Rare but possible. The key word has to change its meaning, not just appear in different places."],
        ["Inappropriate Appeal", "Leans on sympathy, popularity or an authority with no expertise on the topic.", "Sometimes the answer. Look for \"someone famous said so\" or \"everyone thinks so\" as the only reason."],
    ],
)

G3 = table(
    ["Flaw", "What the author does", "The tell"],
    [
        ["Sleight of Hand", "A new term appears in the conclusion that the evidence never mentioned, and the author treats it as basically the same as something in the evidence. Nothing is basically the same on the LSAT.<br><em>This diet helps you lose weight. So it will make you healthier.</em>",
         "A key word in the conclusion appears nowhere in the evidence. The choice says: treats two fundamentally different concepts as essentially the same."],
        ["Sleazy Sales Pitch", "Compares two things and praises one without the full story: its strengths and the other's weaknesses, nothing on the rest.", "One option gets only strengths and the other only weaknesses."],
        ["Universal Desires Assumption", "Assumes everyone wants the goal: lose weight, save money, be healthier.<br><em>Everyone should switch to the new low-fat diet because it will help them lose weight.</em>",
         "The conclusion says someone should do something to reach a goal, and never shows they want it."],
        ["Value Assumptions", "Uses a loaded word in the conclusion (moral, appropriate, good, should) that the evidence never defined.", "An evaluative word in the conclusion that the evidence never sets up."],
        ["Secret Downsides", "Recommends an action for its benefits and never looks at its costs.<br><em>We should switch to solar energy to save money on electricity.</em> The installation cost could erase the savings.",
         "Benefits only, no costs. Like Sleazy Sales Pitch, but with no comparison."],
    ],
)

V1 = (
    '<header class="hero solo"><div class="wrap"><div class="kicker">Session recap · November 11</div><h1>Famous Flaws</h1>'
    '<p class="lede">A flaw question asks what is wrong with an argument. The answer is almost always one of fifteen reasoning errors. Six are usually the real flaw. Four are usually the trap. Five are ones I named myself because they show up everywhere. In our session we went through four of the six. Learn those six first.</p></div></header><main>'
    + section("How to use it", "Name the flaw, then find the choice",
              steps(STEPS_READ) + '<div class="quote">' + QUOTE_COMMON_SENSE + "</div>")
    + section("Group 1", "Usually the real flaw",
              "<p>If you spot one of these in the stimulus, look for the choice that names it. These are the heavy hitters. In our session I called Necessary vs. Sufficient and Causal the two most common.</p>" + G1)
    + section("Group 2", "Usually the trap",
              "<p>These show up in wrong answer choices much more often than in right ones. When a choice names one, be suspicious. Check that the stimulus really does it before you pick it.</p>" + G2)
    + section("Group 3", "Named by me, and everywhere",
              "<p>These do not have textbook names. They may be the most common errors on the test anyway. Treat them with the same priority as Group 1.</p>" + G3)
    + section("Easy to mix up", "Five pairs, and the question that separates them",
              opposite("Necessary vs. Sufficient", "Is the link an if-then rule, or one thing making another happen? A rule is about guarantees.", "Causal", "A cause is about making something happen. Ask what else could explain it.")
              + opposite("Equivocation", "One word, two meanings.", "Sleight of Hand", "Two different words, treated as equivalent.")
              + opposite("Ad Hominem", "The target is the speaker.", "Unproven vs. Proven False", "The target is the evidence, or the lack of it.")
              + opposite("Sampling", "From a sample to a population.", "Part vs. Whole", "From a part to the whole it belongs to.")
              + opposite("Value Assumptions", "You can point at the loaded word. Call it this.", "Sleight of Hand", "You cannot. Call it this."))
    + section("Try it", "Name the flaw, then tap to check",
              '<div class="drill"><div class="drill-head"><div><h3>Say it out loud first</h3><p class="hint">Which flaw is it? Say it in your own words before you tap.</p></div></div><div class="chips">'
              + "".join(chip(*c) for c in SESSION_ITEMS) + "</div></div>")
    + section("Your work", "What to do next", steps(NEXT_STEPS, todo=True))
    + "</main>"
)

# =============================================================== VARIATION 2: teaching
THREE_GROUPS = (
    opposite("Usually the flaw (6)", "Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem, Sampling. These are the right answer again and again. Learn these first.",
             "Usually the trap (4)", "Circular Reasoning, Internal Contradiction, Equivocation, Inappropriate Appeal. These fill wrong choices. When a choice names one, check that the stimulus really does it.")
    + callout("Named by me (5)", "Sleight of Hand, Sleazy Sales Pitch, Universal Desires Assumption, Value Assumptions and Secret Downsides. They have no textbook names and show up everywhere. Treat them with the same priority as the first group.")
)

NS_PAIR = (
    '<div class="kinds">'
    + card("apply", "Sufficient", "Enough to guarantee the result. If you have it, the result happens.", "A doctor's note gets you excused from the exam.", "If this is true, does the result have to follow?")
    + card("link", "Necessary", "Required for the result. Without it, the result cannot happen.", "You must be enrolled in the course to sit the exam.", "If this is missing, is the result impossible?")
    + "</div>"
)
CAUSAL_PAIR = (
    '<div class="kinds">'
    + card("apply", "Correlation", "Two things happen together. That is all it says.", "People who read a lot are less likely to drop out of high school.", "Does this only say they go together?")
    + card("link", "Causation", "One thing is the reason the other happens.", "Reading keeps students in school.", "Does this say why?")
    + "</div>"
)
PART_PAIR = (
    '<div class="kinds">'
    + card("apply", "Whole to part", "A trait of the group gets pushed onto each member.", "The team is a star team, so every player on it is a superstar.", "Can the group have this trait while one member does not?")
    + card("link", "Part to whole", "A trait of one member gets pushed onto the group.", "She is the best guard in the country, so her team must be great.", "Can one member have this trait while the group does not?")
    + "</div>"
)
UNPROVEN_PAIR = (
    '<div class="kinds">'
    + card("apply", "Unproven", "No one has shown the claim is true. All we know is that it has not been shown.", "The prosecution could not prove you are guilty.", "Has anyone shown the opposite, or has no one shown anything?")
    + card("link", "Proven false", "Someone has shown the claim is false.", "The records show you were in another city that night.", "Is there evidence for the opposite, not just a lack of evidence?")
    + "</div>"
)
LAST_TWO = (
    '<div class="kinds">'
    + card("apply", "Ad Hominem", "Dismisses a claim by attacking the source, not the claim.", "We can ignore Maya's view on the bus route. She drives for a taxi company.", "Is the author attacking the claim, the evidence, or the speaker?")
    + card("link", "Sampling", "Generalizes from a sample that is too small, biased or unrepresentative.", "Three students at the gym find the library too quiet, so the whole school does.", "Does the sample look like the group the conclusion is about?")
    + "</div>"
)

V2_CHIPS = [SESSION_ITEMS[0], SESSION_ITEMS[1], SESSION_ITEMS[2], SESSION_ITEMS[3], TRAP_ITEMS[1], JOSHUA_ITEMS[0]]

V2 = (
    '<header class="hero"><div class="wrap"><div class="kicker">Session recap · November 11</div><h1>Famous Flaws<br>Name Them First</h1>'
    '<p class="lede">A flaw question asks what is wrong with an argument. Most students read the answer choices and wait for one to sound right. The choices are written in abstract language, so two of them often sound right at once. There is a shorter path: flaw answers come from a short list of famous mistakes. Name the mistake in the stimulus first, then find the choice that says it.</p></div>'
    + stage("RESULT", "Pick the choice that says it", "Which famous flaw is it?", "What did the author do?")
    + "</header><main>"
    + section("Read it first", "Say the flaw before you look at A", steps(STEPS_READ)
              + callout("The lesson is the order", "Name the flaw first, then read the choices. If you read the choices first, you are deciding between sentences you only half understand."))
    + section("The list", "Fifteen flaws in three groups",
              "<p>Joshua's list is fifteen flaws, but they do not carry equal weight. In our session we went through four of the first group. The rest of this note teaches those four and then finishes the list.</p>".replace("Joshua's list is", "The list is")
              + THREE_GROUPS)
    + section("Flaw one", "Sufficient or necessary?",
              "<p>In our session I called this one of the two most common flaws. You need to tell these two ideas apart without stopping to think.</p>" + NS_PAIR
              + callout("A guaranteed way is not the only way", "A doctor's note gets you excused. That does not make it the only way, because a family emergency might get you excused too. The rule named one guaranteed path. It never said it was the only one.", trap=True)
              + gate("The evidence says this is enough to get the result", "The conclusion says this is the only way to get the result",
                     'Neither is on. This argument is not about "enough" or "only," so look for a different flaw.',
                     'Only the first. The evidence says "enough" and the conclusion stays with that, so this pair is not the flaw. If the conclusion says that without it the result cannot happen, turn on the second switch.',
                     'Only the second. The conclusion says "only," but the evidence does not say this route is enough. Check whether the evidence gives any other reason to think nothing else works. If it does not, the conclusion has gone past its support.',
                     'Both. The evidence shows "enough" and the conclusion claims "only." That is sufficient treated as necessary.',
                     "Flip each switch and see what the argument is doing."))
    + section("The trap", "A word like cause does not name the flaw",
              '<div class="flags"><span class="flag">cause</span><span class="flag">because</span><span class="flag">leads to</span><span class="flag">only</span></div>'
              "<p>Words like these tell you what the sentence is about. They do not tell you what is wrong with it. In the practice question from our session, a counselor argued that harsh criticism is necessary for people to change. The conclusion used a cause word, but the flaw was the word <em>only</em>.</p>"
              + callout("The trap that costs the most", "Seeing the word cause and choosing Causal. A real causal flaw has two parts: the evidence reports that two things go together, and the conclusion says why. If the evidence does not report that, the word may be a decoy. Ask what the conclusion adds to the evidence instead.", trap=True)
              + '<div class="quote">You said it yourself. You saw the word cause and thought causation. Then you read the conclusion again and asked, <em>"Why is it only harsh criticism? ... It could be gentle, it could be constructive ... it could be other things."</em> That second read is the method. It is the sufficient-versus-necessary question in your own words.</div>')
    + section("Flaw two", "Together is not the same as because",
              "<p>The evidence usually reports a study: two things happen together. The conclusion says one is why the other happens. A correlation is easy to show. A cause is hard to prove.</p>" + CAUSAL_PAIR
              + callout("Three stories fit the same fact", "Reading could keep students in school. Staying in school could give students more time to read. Or richer parents could give a child more books and more help, and that drives both. Sometimes the link is coincidence. When the author picks one story, ask which others are still standing.", trap=True))
    + section("Flaws three and four", "A group is not its members, and no proof is not proof of the opposite",
              "<p>What is true of a whole is not necessarily true of each part, and the reverse. And a lack of evidence is not evidence of lacking.</p>" + PART_PAIR + UNPROVEN_PAIR
              + callout("You already do this", "You said: <em>\"Just because the team does well overall doesn't mean every single player on the team does well.\"</em> And: <em>\"Because I can't prove you're innocent, you're guilty.\"</em> I called that the best example. The names are new. The reasoning is yours."))
    + section("Two more heavy hitters", "Ad Hominem and Sampling",
              "<p>These two are also usually the real flaw, so they belong in your first six.</p>" + LAST_TWO)
    + section("Handle with care", "Four flaws that are usually the trap",
              "<p>Circular Reasoning, Internal Contradiction, Equivocation and Inappropriate Appeal show up in wrong choices far more than in right ones.</p>"
              + callout("When a choice names one", "Be suspicious. Go back to the stimulus and check that the author really does it. Real circular reasoning is short and repeats itself. Equivocation needs one word that truly changes its meaning.", trap=True))
    + section("Try it", "Name the flaw, then tap to check",
              '<div class="drill"><div class="drill-head"><div><h3>Say it out loud first</h3><p class="hint">Which famous flaw is it? Answer in your own words before you tap.</p></div></div><div class="chips">'
              + "".join(chip(*c) for c in V2_CHIPS) + "</div></div>")
    + section("Your work", "What to do next", steps(NEXT_STEPS, todo=True))
    + "</main>"
)

# =============================================================== VARIATION 3: sort and spot
SHAPES = (
    '<div class="rule"><b>Necessary vs. Sufficient</b><br>Enough to get it <span class="ar">→</span> required for it.</div>'
    '<div class="rule"><b>Causal</b><br>They go together <span class="ar">→</span> one caused the other.</div>'
    '<div class="rule"><b>Part vs. Whole</b><br>Every part has it <span class="ar">→</span> the whole has it. Or the reverse.</div>'
    '<div class="rule"><b>Unproven vs. Proven False</b><br>No proof it is true <span class="ar">→</span> it is false.</div>'
    '<div class="rule"><b>Ad Hominem</b><br>The source has a motive <span class="ar">→</span> the claim is wrong.</div>'
    '<div class="rule"><b>Sampling</b><br>A few cases <span class="ar">→</span> everyone.</div>'
)

V3 = (
    '<header class="hero"><div class="wrap"><div class="kicker">Session recap · November 11</div><h1>Famous Flaws<br>Spot Them Fast</h1>'
    '<p class="lede">Most flaw answers are one of fifteen famous mistakes. You do not need to memorize fifteen paragraphs. You need to know the shape of each mistake, the tell that gives it away, and which ones are usually the trap.</p></div>'
    + stage("RESULT", "Pick the choice that says it", "Match it to a shape", "Say what the author did")
    + "</header><main>"
    + section("The shapes", "Six mistakes, one line each",
              "<p>These are the six that are usually the real flaw. In our session we went through the first four.</p>" + SHAPES
              + callout("Say it, then match it", "Before you read A, say the shape in your own words. Then read the choices looking for the one that says it."))
    + section("The tells", "What gives each one away",
              '<div class="flags"><span class="flag">must, only, unless</span><span class="flag">a study shows</span><span class="flag">every member</span><span class="flag">no evidence that</span><span class="flag">biased, stands to gain</span><span class="flag">a survey of a few</span></div>'
              "<p>In order: Necessary vs. Sufficient, Causal, Part vs. Whole, Unproven vs. Proven False, Ad Hominem, Sampling. A tell is a clue, not a verdict. Check what the conclusion does with the evidence.</p>"
              + gate("The evidence shows two things go together", "The conclusion says one of them caused the other",
                     "Neither is on. This is not a causal argument, so look for a different flaw.",
                     "Only the first. A correlation is reported and nothing more is claimed. That is not a flaw yet.",
                     "Only the second. A cause is claimed, but the evidence does not show the two go together. Check what the evidence offers instead.",
                     "Both. The evidence shows a correlation and the conclusion picks one cause. That is the Causal flaw. Ask about reverse cause, a third factor and coincidence.",
                     "Flip each switch and see what the argument is doing."))
    + section("Round one", "Name the flaw",
              '<div class="drill"><div class="drill-head"><div><h3>Which of the six?</h3><p class="hint">Say it in your own words, then tap.</p></div></div><div class="chips">'
              + "".join(chip(*c) for c in SESSION_ITEMS) + "</div></div>")
    + section("Round two", "Real flaw or trap?",
              "<p>Circular Reasoning, Internal Contradiction, Equivocation and Inappropriate Appeal are usually the trap. When a wrong choice names one, you cross it out. When the stimulus really does it, it is the answer. Tap each one to see which.</p>"
              '<div class="drill"><div class="drill-head"><div><h3>Does the stimulus really do it?</h3><p class="hint">Name it, then tap.</p></div></div><div class="chips">'
              + "".join(chip(*c) for c in TRAP_ITEMS) + "</div></div>")
    + section("Round three", "The five I named",
              "<p>No textbook names, but they may be the most common errors on the test. Sleight of Hand alone may be the most common flaw of all.</p>"
              '<div class="drill"><div class="drill-head"><div><h3>What is missing from the argument?</h3><p class="hint">A new word, a one-sided story, a goal assumed, a loaded word, or a hidden cost.</p></div></div><div class="chips">'
              + "".join(chip(*c) for c in JOSHUA_ITEMS) + "</div></div>")
    + section("Your work", "What to do next", steps(NEXT_STEPS, todo=True))
    + "</main>"
)

FILES = [
    ("famous-flaws-v1-catalog.html", "ore-2026-11-11-famous-flaws-catalog", "Famous Flaws · Session recap", V1),
    ("famous-flaws-v2-teaching.html", "ore-2026-11-11-famous-flaws-teaching", "Famous Flaws · Session recap", V2),
    ("famous-flaws-v3-sort-and-spot.html", "ore-2026-11-11-famous-flaws-sort-and-spot", "Famous Flaws · Session recap", V3),
]
for name, lid, title, body in FILES:
    (OUT / name).write_text(build(lid, title, body), encoding="utf-8", newline="\n")
    print("wrote", name)
