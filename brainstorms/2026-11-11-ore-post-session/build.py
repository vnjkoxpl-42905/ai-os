"""Build Oreoluwa's 2026-11-11 notes from the Lanae shell.

Reads wiki/homework-assigning/model-note/note-shell.html, fills the slots, and never
touches its CSS or script. Writes three self-contained HTML files next to this script
and a plain-text fallback of the teaching note.

Run: py -I brainstorms/2026-11-11-ore-post-session/build.py
"""
import html
import re
from pathlib import Path

ROOT = Path(r"C:/Users/Joshu/dev/ai-os")
SHELL = ROOT / "wiki/homework-assigning/model-note/note-shell.html"
OUT = ROOT / "brainstorms/2026-11-11-ore-post-session"

shell = SHELL.read_text(encoding="utf-8")
HERO_START = shell.index('<header class="hero">')
MAIN_END = shell.index("</main>") + len("</main>")


# Fix (2026-11-14): below 760px the 3D stack sits under the lede and its top card rises into the
# last line of text. Give the stage room above it. Scoped to this note; the shared shell is untouched.
EXTRA_CSS = "@media (max-width:760px){header.hero{gap:64px}.stage{margin-top:28px}}"


def build(lesson_id, title, body):
    out = shell[:HERO_START] + body + shell[MAIN_END:]
    out = out.replace("</style>", EXTRA_CSS + "</style>", 1)
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


def kind_card(cls, name, what, looks, test):
    return (
        '<div class="kind %s" data-tilt="5"><span class="bar"></span><div class="name">%s</div>'
        '<p class="what">%s</p><div class="words"><b>Looks like</b> <span>%s</span></div>'
        '<div class="test"><b>Test</b>%s</div></div>' % (cls, name, what, looks, test)
    )


# ---------------------------------------------------------------- teaching note
TEACH_BODY = """<header class="hero"><div class="wrap">
  <div class="kicker">Session recap · November 11</div>
  <h1>Naming the Flaw<br>Before the Choices</h1>
  <p class="lede">A flaw question asks what is wrong with an argument. Most students read the answer choices and wait for one to sound right. The choices are written in abstract language, so two of them often sound right at once. There is a shorter path: name the mistake in the stimulus first, then look for the choice that says it. More than half of flaw questions are built on one of four mistakes, and this note gives you all four.</p>
</div>
<div class="stage" aria-hidden="true"><div class="stack" data-tilt="10">
  <div class="slab base"><i>RESULT</i><b>Name the flaw</b></div>
  <div class="slab c2"><i>CHECK 2</i><b>What does the conclusion add?</b></div>
  <div class="slab c1"><i>CHECK 1</i><b>What does the evidence give?</b></div>
</div></div></header>

<main>

<section><div class="wrap">
  <div class="sec-kicker">Read it first</div>
  <h2>Say the flaw before you look at A</h2>
  <p>On the practice question from our session, a counselor argued that harsh criticism is necessary for people to change. You named the flaw correctly: sufficient treated as necessary. That is the hardest part. The next step is to hold that flaw in your head as one plain sentence, so the choices become a matching job.</p>
  <ol class="steps">
    <li><b>Find the conclusion and the evidence.</b> The conclusion is what the author wants you to accept. The evidence is the reason. "If you win the raffle, you get a bicycle. So winning is the only way to get a bicycle." The second sentence is the conclusion.</li>
    <li><b>Say exactly what the evidence gives.</b> Not what it sounds like. This evidence says winning is enough. It does not say winning is required.</li>
    <li><b>Say exactly what the conclusion adds.</b> It says winning is the only way. That is a bigger claim than "enough."</li>
    <li><b>Say the flaw in your own words.</b> "The evidence shows one route works. The author says it is the only route." Now read A to E looking for the choice that says that.</li>
  </ol>
  <div class="callout"><span class="tag">The lesson is the order</span> Name the flaw first, then read the choices. If you read the choices first, you are deciding between sentences you only half understand.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The four at a glance</div>
  <h2>Four mistakes cover most flaw questions</h2>
  <p>Learn these four names and the question each one asks. The next four sections take them one at a time, in the same order.</p>
  <div class="table-wrap"><table class="t">
<thead><tr><th>#</th><th>The flaw</th><th>The author's mistake</th><th>Ask yourself</th></tr></thead>
<tbody>
<tr><td>1</td><td>Sufficient versus necessary</td><td>Treats <em>enough</em> as <em>the only way</em></td><td>Is this the only route, or just one that works?</td></tr>
<tr><td>2</td><td>Correlation versus causation</td><td>Sees two things go together, then picks one as the reason</td><td>What else could explain it?</td></tr>
<tr><td>3</td><td>Part versus whole</td><td>Slides a trait between a group and its members</td><td>Did a noun change size?</td></tr>
<tr><td>4</td><td>Unproven versus proven false</td><td>Reads no proof for a claim as proof against it</td><td>Has anyone shown the opposite, or only nothing?</td></tr>
</tbody>
</table></div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Flaw 1 of 4 · Sufficient versus necessary</div>
  <h2>Enough is not the only way</h2>
  <p>If you win the raffle, you get a bicycle. That rule says winning is enough. It does not say winning is the only way, because someone can buy a bicycle. A rule that says <em>enough</em> can be misused in two ways, and both show up on the test. Take this rule: anyone who has seen a certain documentary understands the prison system well.</p>
  <div class="rule">Saw the documentary <span class="ar">→</span> understands the prison system well</div>
  <div class="opposite"><div><b>Illegal reversal</b>Jane understands the prison system really well, so she must have seen the documentary.</div><div><b>Illegal negation</b>Megan has not seen the documentary, so she must have a poor understanding of the prison system.</div></div>
  <div class="gate" data-state="0">
    <h3>Try the two checks</h3><p class="hint">Flip each switch and see what the argument is doing.</p>
    <div class="gate-body">
      <button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>The evidence says this is enough to get the result</span></button>
      <button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>The conclusion says this is the only way to get the result</span></button>
      <div class="verdict" role="status"><i class="lamp"></i>
        <span class="v0">Neither is on. This argument is not about "enough" or "only," so look for a different flaw.</span>
        <span class="v1">Only the first. The evidence says "enough" and the conclusion stays with that, so this pair is not the flaw. If the conclusion says that without it the result cannot happen, turn on the second switch.</span>
        <span class="v2">Only the second. The conclusion says "only," but the evidence does not say this route is enough. Check whether the evidence gives any other reason to think nothing else works. If it does not, the conclusion has gone past its support.</span>
        <span class="v3">Both. The evidence shows "enough" and the conclusion claims "only." That is sufficient treated as necessary.</span></div>
    </div>
  </div>
  <div class="flags"><span class="flag">cause</span><span class="flag">because</span><span class="flag">leads to</span><span class="flag">only</span></div>
  <div class="callout trap"><span class="tag">The trap that costs the most</span> Seeing the word <em>cause</em> and choosing correlation versus causation. In the counselor question the evidence showed that harsh criticism gives a person a motive to change, and the conclusion said only harsh criticism will do. The word was a decoy. The flaw was the word <em>only</em>. Ask what the conclusion adds to the evidence.</div>
  <div class="quote">You said it yourself. You saw the word cause and thought causation. Then you read the conclusion again and asked, <em>"Why is it only harsh criticism? ... It could be gentle, it could be constructive ... it could be other things."</em> That second read is the method. It is the sufficient-versus-necessary question in your own words.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Flaw 2 of 4 · Correlation versus causation</div>
  <h2>Together is not the same as because</h2>
  <p>On the test the evidence usually reports a study: two things happen together. The conclusion then says one of them is why the other happens. A correlation is easy to show. A cause is very hard to prove.</p>
  <div class="rule">Evidence: readers drop out less <span class="ar">→</span> Conclusion: reading keeps students in school</div>
  <div class="opposite"><div><b>The evidence gives</b>People who read a lot are less likely to drop out of high school. The two go together.</div><div><b>The conclusion claims</b>Reading is the reason students stay in school.</div></div>
  <div class="callout"><span class="tag">Three stories fit the same fact</span> Reading could keep students in school. Staying in school could give students more time to read. Or richer parents could give a child more books and more help, and that drives both. A correlation does not choose between them. When the author picks one story, ask which others are still standing.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Flaw 3 of 4 · Part versus whole</div>
  <h2>A group is not each of its members</h2>
  <p>What is true of a whole is not necessarily true of each part. What is true of one part is not necessarily true of the whole. The flaw runs in both directions, and the clue is a noun that changes size.</p>
  <div class="rule">Team <span class="ar">→</span> player, or player <span class="ar">→</span> team</div>
  <div class="opposite"><div><b>Whole to part</b>The team is a star team, so every player on it is a superstar.</div><div><b>Part to whole</b>She is the best guard in the country, so her team must be great.</div></div>
  <div class="callout"><span class="tag">You already do this</span> You told me you had seen questions like this and it felt like common sense. Your words were, <em>"Just because the team does well overall doesn't mean every single player on the team does well."</em> The name is new. The reasoning is yours. Watch for a team and a player, a campus and a building.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Flaw 4 of 4 · Unproven versus proven false</div>
  <h2>No proof is not proof of the opposite</h2>
  <p>A lack of evidence is not evidence of lacking. If nobody has shown a claim is true, all you know is that nobody has shown it. You do not know it is false. The newer version of this flaw: someone knocks down one bad argument for a claim and says the claim itself is false. A bad argument for X is not proof of not-X.</p>
  <div class="rule">Nobody has shown it is true <span class="ar">→</span> so it is false</div>
  <div class="opposite"><div><b>Unproven</b>No one has shown the claim is true. All we know is that it has not been shown.</div><div><b>Proven false</b>Someone has shown the claim is false. The records put you in another city that night.</div></div>
  <div class="callout"><span class="tag">It fails in both directions</span> <em>"Because I can't prove you're innocent, you're guilty."</em> And the reverse: because I can't prove you're guilty, you're innocent. You put it that way yourself, and I called it the best example. The same move shows up whenever an author says nobody has shown X, so not X.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Try it</div>
  <h2>Name the flaw, then tap to check</h2>
  <div class="drill">
    <div class="drill-head"><div><h3>Say it out loud first</h3><p class="hint">Which of the four is it? Answer in your own words before you tap.</p></div></div>
    <div class="chips">
      CHIPS
    </div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">On every question</div>
  <h2>Turn each answer choice into a plain question</h2>
  <p>Flaw answer choices are written in abstract language. They sound like a foreign language until you have seen them a few times. Your job is to translate them into plain questions about the stimulus.</p>
  <figure class="screen"><div class="bezel"><div class="panes">
    <div class="pane left"><b>Stimulus</b><i></i><i></i><i class="hit"></i><i></i></div>
    <div class="pane right"><b>Answer choices</b><i data-l="A"></i><i data-l="B"></i><i data-l="C"></i><i data-l="D"></i><i data-l="E"></i></div>
  </div></div><figcaption>Name the flaw on the left. Match it on the right.</figcaption></figure>
  <ol class="steps">
    <li><b>Name the flaw first.</b> One plain sentence about what the author did.</li>
    <li><b>Translate each choice into a question.</b> A choice that says the author refutes an opposing argument becomes: did the author attack anyone's argument? In the counselor question nothing was refuted, so that choice described something that never happened.</li>
    <li><b>Cut a choice for a reason you can say.</b> You told me you sometimes just know a choice is wrong. Write the reason, even a short one: "The stimulus never talks about avoiding anything." That reason is the skill.</li>
    <li><b>Read the wrong choices after the question, not only your pick.</b> Look up what each one means. A wrong choice today can be the right answer on the next question. After you have seen the same language a few times, it stops sounding abstract.</li>
  </ol>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Your work</div>
  <h2>What to do next</h2>
  <ol class="steps todo">
    <li><b>Flaw - First Taste.</b> Read the Before you start note first. Then do the seven guided questions. Before you read any choice, say the flaw out loud in your own words, then find the choice that says it. Famous Flaw (Easier) Set 1 and Abstract + Flaw (set 1) follow on later days.</li>
    <li><b>Keep the Famous Flaws note open beside every flaw question.</b> Find the flaw in it before you read the choices. Write the name of the flaw next to your answer. When you miss one, write which flaw it was. In a week the pattern in your misses will show.</li>
    <li><b>Read one or two Reading Comprehension passages every other day.</b> Keep it light. The goal is to get used to the density of the language before we start the RC modules. Any Reading Comprehension passage works for this.</li>
    <li><b>Send me a message on the platform if you have a question.</b> I'll be able to get back to you.</li>
  </ol>
</div></section>

</main>"""

TEACH_BODY = TEACH_BODY.replace(
    "CHIPS",
    "\n      ".join(
        [
            chip(
                "describe",
                "A clear syllabus will cause students to start, because it gives them a plan. Students need a plan before they can start. So a clear syllabus is the only thing that gets students started.",
                "Sufficient, not necessary",
                "Sufficient treated as necessary. The word cause is a decoy. A syllabus is enough to get students started. The conclusion says it is the only way.",
            ),
            chip(
                "assume",
                "People who walk to work report better moods. So walking to work improves your mood.",
                "Correlation, not cause",
                "Correlation versus causation. The evidence says walking and good mood go together. People in good moods may be the ones who walk, or something like a free morning could drive both.",
            ),
            chip(
                "object",
                "The restaurant has a great reputation, so every dish on its menu must be great.",
                "Whole to part",
                "Whole to part. A restaurant can have a great reputation while one dish on the menu is poor.",
            ),
            chip(
                "object",
                "The lead engineer on the project is brilliant, so the project must be going well.",
                "Part to whole",
                "Part to whole. One brilliant member does not make the whole project go well.",
            ),
            chip(
                "neutral",
                "Nobody has shown the old footbridge is unsafe, so it must be safe.",
                "Unproven, not proven false",
                "Unproven versus proven false. No one showing it is unsafe is not the same as someone showing it is safe. All we know is that nothing has been shown.",
            ),
        ]
    ),
)


# ---------------------------------------------------------------- before you start
BEFORE_BODY = """<header class="hero solo"><div class="wrap">
  <div class="kicker">Before you start · Flaw - First Taste</div>
  <h1>Flaw - First Taste</h1>
  <p class="lede">Seven guided flaw questions. This is your first drill on this question type, so the aim is one habit: name the flaw before you read the answer choices.</p>
</div></header>

<main>

<section><div class="wrap">
  <div class="sec-kicker">What these questions look like</div>
  <h2>The stem asks what is wrong with the reasoning</h2>
  <p>A flaw question gives you an argument and asks what is wrong with it. The stem usually reads like "The reasoning is flawed because it" or "The argument is vulnerable to criticism on the grounds that it." The answer choices describe the mistake in abstract language, so at first they read like a foreign language.</p>
  <p>Your one job is to describe the mistake yourself before you read them.</p>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">What to expect</div>
  <h2>Most of these come down to a short list of famous flaws</h2>
  <p>Here are four to start with. The Famous Flaws note has all fifteen, with every way the answer choices disguise each one.</p>
  <div class="table-wrap"><table class="t">
<thead><tr><th>If the argument</th><th>The flaw is probably</th></tr></thead>
<tbody>
<tr><td>Treats something that is enough as something that is required</td><td>Sufficient versus necessary</td></tr>
<tr><td>Reports that two things go together, then says why</td><td>Correlation versus causation</td></tr>
<tr><td>Moves from a group to one member, or one member to the group</td><td>Part versus whole</td></tr>
<tr><td>Says nobody has shown X, so not X</td><td>Unproven versus proven false</td></tr>
</tbody>
</table></div>
  <div class="callout trap"><span class="tag">One trap</span> The word <em>cause</em> in a conclusion does not by itself mean a causal flaw. Check what the conclusion adds to the evidence before you decide.</div>
  <div class="callout"><span class="tag">One habit</span> Say the flaw out loud in your own words before you read A. Then read the choices looking for the one that says it.</div>
</div></section>

</main>"""

# ---------------------------------------------------------------- reference
REF_BODY = """<header class="hero solo"><div class="wrap">
  <div class="kicker">Reference · Keep it open while you drill</div>
  <h1>The Four Flaws to Know First</h1>
  <p class="lede">Keep this open beside a flaw question. Name the flaw in the stimulus from this list before you read the answer choices. Learn the four cards first, then the one to learn last, then the six to cross out.</p>
</div></header>

<main>

<section><div class="wrap">
  <div class="sec-kicker">The list</div>
  <h2>Four flaws, one card each</h2>
  <div class="kinds">
    <div class="kind assume" data-tilt="5"><span class="bar"></span><div class="name">1 · Sufficient versus necessary</div><p class="what">Treats something that is enough as something that is required, or runs the rule backwards.</p><div class="words"><b>Looks like</b> <span>People who have seen that documentary understand the prison system well. Jane understands it well, so she must have seen it.</span></div><div class="test"><b>Ask</b>Is this the only route, or just one that works?</div></div>
    <div class="kind assume" data-tilt="5"><span class="bar"></span><div class="name">2 · Correlation versus causation</div><p class="what">Reports that two things go together, then picks one story for why.</p><div class="words"><b>Looks like</b> <span>People enlisted in the military are more likely than others to have excellent physiques. So recruiters must select soldiers for fitness.</span></div><div class="test"><b>Ask</b>What else could explain it?</div></div>
    <div class="kind assume" data-tilt="5"><span class="bar"></span><div class="name">3 · Part versus whole</div><p class="what">Pushes a trait of the group onto each member, or a trait of one member onto the group.</p><div class="words"><b>Looks like</b> <span>Rat poison is very harmful if ingested, so each ingredient in it must be very harmful if ingested.</span></div><div class="test"><b>Ask</b>Did a noun change size?</div></div>
    <div class="kind assume" data-tilt="5"><span class="bar"></span><div class="name">4 · Unproven versus proven false</div><p class="what">Treats a lack of evidence for a claim as evidence against it.</p><div class="words"><b>Looks like</b> <span>Billy could not connect his uncle to a famous singer on a genealogy site, so his uncle was not related to the singer.</span></div><div class="test"><b>Ask</b>Has anyone shown the opposite, or only nothing?</div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The tell</div>
  <h2>What to look for in the wording</h2>
  <div class="table-wrap"><table class="t">
<thead><tr><th>Flaw</th><th>How often</th><th>The tell in the wording</th></tr></thead>
<tbody>
<tr><td>1 · Sufficient versus necessary</td><td>Most common</td><td>must, only, unless, requires, or a rule about what is enough</td></tr>
<tr><td>2 · Correlation versus causation</td><td>Very common</td><td>a study, survey or statistic in the evidence and a because in the conclusion</td></tr>
<tr><td>3 · Part versus whole</td><td>Common</td><td>a noun that changes size: one member to the organization, one ingredient to the product</td></tr>
<tr><td>4 · Unproven versus proven false</td><td>Common</td><td>no evidence that, has not been shown, cannot prove</td></tr>
</tbody>
</table></div>
  <div class="callout trap"><span class="tag">A cause word alone does not make it a causal flaw</span> If the conclusion says cause but the evidence does not report two things going together, look at what the conclusion adds to the evidence. In the practice question it was a sufficient condition treated as necessary.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Learn last</div>
  <h2>One more: sampling</h2>
  <p>The author generalizes from a group that may be biased, too small or not representative of the people the conclusion is about. <em>Today's youth prefer comics to literature. After all, in a survey at last year's comics convention, over 85% of the young people surveyed said they liked comics much more than novels.</em></p>
  <div class="callout"><span class="tag">Run it as a check, not your first guess</span> No study samples an entire population, so "the sample was imperfect" is not enough. The sample has to be skewed toward the very thing being concluded. Use this on study questions, after the four above.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Six to cross out</div>
  <h2>These show up as wrong answers, almost never as the flaw</h2>
  <p>You are not learning these to find them in a stimulus. You are learning them so you can read a choice, name it and cross it out fast.</p>
  <div class="table-wrap"><table class="t">
<thead><tr><th>Name</th><th>What it is</th><th>Quick check</th></tr></thead>
<tbody>
<tr><td>Ad hominem</td><td>Dismissing a view because the source is biased, has something to gain, or once said the opposite.</td><td>Attacks the arguer, not the argument.</td></tr>
<tr><td>Inappropriate appeal</td><td>A plea for sympathy, an authority with no sign of real expertise, or picking one source over another for no stated reason.</td><td>Same family as ad hominem.</td></tr>
<tr><td>Circular reasoning</td><td>The premise restates or quietly assumes the conclusion.</td><td>Offered often, right almost never.</td></tr>
<tr><td>Equivocation</td><td>One term doing two different jobs.</td><td>Rare enough that it stands out when real.</td></tr>
<tr><td>Internal contradiction</td><td>Something the author says undercuts something else the author says.</td><td>Check both claims before you take it.</td></tr>
<tr><td>Straw man</td><td>Beating a distorted, easier version of the other side's position and calling the real one defeated.</td><td>Compare what was said to what got answered.</td></tr>
</tbody>
</table></div>
  <div class="callout"><span class="tag">Almost never is not never</span> One of these is the answer once in a while, and when it is, it usually stands out because it is so rare. Read the choice, name it, then decide.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">How to use it</div>
  <h2>Keep this open beside a flaw question</h2>
  <ol class="steps">
    <li><b>Name the flaw before the choices.</b> Read the stimulus and say the flaw in your own words. Then look for the choice that says it.</li>
    <li><b>Match it to the list.</b> Which of the four is it? If none fits, say what the author did in plain words and read the choices with that sentence in mind.</li>
    <li><b>Write the flaw next to your answer.</b> One or two words is enough.</li>
    <li><b>Log the ones you miss.</b> Write which of the four it was. In a week the pattern in your misses shows.</li>
  </ol>
  <p>Know the causal flaw especially well. Strengthen and weaken questions use the same idea, and they ask you to apply it, not only to recognize it.</p>
</div></section>

</main>"""

FILES = [
    ("recap.html", "ore-2026-11-11-naming-the-flaw", "Naming the Flaw Before the Choices · Session recap", TEACH_BODY),
    ("before-you-start-flaw-first-taste.html", "ore-2026-11-11-before-flaw-first-taste", "Flaw - First Taste · Before you start", BEFORE_BODY),
    ("reference-four-flaws.html", "ore-2026-11-11-four-flaws-reference", "The Four Flaws to Know First · Reference", REF_BODY),
]

for name, lesson_id, title, body in FILES:
    (OUT / name).write_text(build(lesson_id, title, body), encoding="utf-8", newline="\n")
    print("wrote", name)


# ---------------------------------------------------------------- plain-text fallback
def to_md(body):
    s = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    s = re.sub(r'<div class="stage".*?</div></div></header>', "</header>", s, flags=re.S)
    s = re.sub(r'<figure class="screen">.*?</figure>', "", s, flags=re.S)
    s = re.sub(r'<div class="gate".*?</div>\s*</div>\s*</div>', "", s, flags=re.S)
    s = re.sub(r'<span class="stamp"[^>]*>.*?</span>', "", s, flags=re.S)
    s = re.sub(r'<div class="sec-kicker">.*?</div>', "", s)
    s = re.sub(r'<div class="kicker">.*?</div>', "", s)
    s = re.sub(r"<h1>(.*?)</h1>", lambda m: "\n# " + re.sub(r"<br>", " ", m.group(1)) + "\n", s)
    s = re.sub(r"<h2>(.*?)</h2>", lambda m: "\n## " + m.group(1) + "\n", s)
    s = re.sub(r'<span class="tag">(.*?)</span>', r"**\1.**", s)
    s = re.sub(r'<div class="name">(.*?)</div>', r"\n**\1.** ", s)
    s = re.sub(r'<div class="(?:words|test)"><b>(.*?)</b>\s*(?:<span>)?(.*?)(?:</span>)?</div>', r"\1: \2 ", s)
    s = re.sub(r"<li>", "\n1. ", s)
    s = re.sub(r"<b>(.*?)</b>", r"**\1**", s)
    s = re.sub(r"<em>(.*?)</em>", r"*\1*", s)
    s = re.sub(r'<span class="flag">(.*?)</span>', r"\1, ", s)
    s = re.sub(r'<span class="ans">(.*?)</span>', r" Answer: \1", s)
    s = re.sub(r'<div class="chip"[^>]*>', "\n- ", s)
    s = re.sub(r"<(?:/p|/div|/li|/ol|/section|/tr|br)[^>]*>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip() + "\n"


(OUT / "recap.fallback.md").write_text(to_md(TEACH_BODY), encoding="utf-8", newline="\n")
print("wrote recap.fallback.md")
