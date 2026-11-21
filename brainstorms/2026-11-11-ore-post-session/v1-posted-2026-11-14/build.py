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
  <p class="lede">A flaw question asks what is wrong with an argument. Most students read the answer choices and wait for one to sound right. The choices are written in abstract language, so two of them often sound right at once and you end up guessing. There is a shorter path. More than half of flaw questions are built on one of four mistakes, so you can name the mistake in the stimulus first and then look for the choice that says it. The four are: enough treated as required, together treated as because, a group and its members confused, and no proof treated as proof of the opposite.</p>
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
  <p>On the practice question from our session, a counselor argued that harsh criticism is necessary for people to change. You named the flaw correctly: sufficient treated as necessary. That is the hardest part, and the rest comes easily once you have it. The next step is to hold that flaw in your head as one plain sentence, so the choices become a matching job.</p>
  <ol class="steps">
    <li><b>Find the conclusion and the evidence.</b> The conclusion is what the author wants you to accept. The evidence is the reason. "A doctor's note gets you excused from the exam. So a note is the only way to be excused." The second sentence is the conclusion.</li>
    <li><b>Say exactly what the evidence gives.</b> Not what it sounds like. This evidence says a note is enough to get you excused. It does not say a note is required.</li>
    <li><b>Say exactly what the conclusion adds.</b> It says a note is the only way. That is a bigger claim than "enough."</li>
    <li><b>Say the flaw in your own words.</b> "The evidence shows one route works. The author says it is the only route." Now read A to E looking for the choice that says that.</li>
  </ol>
  <div class="callout"><span class="tag">The lesson is the order</span> Name the flaw first, then read the choices. If you read the choices first, you are deciding between sentences you only half understand.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">Two kinds</div>
  <h2>Sufficient or necessary?</h2>
  <p>This is the flaw in the counselor question, and it is one of the two most common flaws on the test. You need to tell these two ideas apart without stopping to think.</p>
  <div class="kinds">
    KIND_SUFF
    KIND_NEC
  </div>
  <div class="callout trap"><span class="tag">A guaranteed way is not the only way</span> A doctor's note gets you excused. That does not make it the only way, because a family emergency might get you excused too. The same goes for "work hard and study and you will do well." Someone who skipped all of that and still did well does not break the rule. The rule named one guaranteed path. It never said it was the only one.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The check</div>
  <h2>Two questions, one flaw</h2>
  <p>Run both questions on any conclusion that sounds like it is about what gets a result.</p>
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
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The trap</div>
  <h2>A word like cause does not name the flaw</h2>
  <div class="flags"><span class="flag">cause</span><span class="flag">because</span><span class="flag">leads to</span><span class="flag">only</span></div>
  <p>Words like these tell you what the sentence is about. They do not tell you what is wrong with it. The word <em>cause</em> tells you the author is talking about causes. It does not tell you the author made a causal mistake. In the counselor question the evidence showed that harsh criticism gives a person a motive to change, and the conclusion said only harsh criticism will do. The conclusion used a cause word, but the flaw was the word <em>only</em>.</p>
  <div class="callout trap"><span class="tag">The trap that costs the most</span> Seeing the word cause and choosing correlation versus causation. A real causal flaw has two parts: the evidence reports that two things go together, and the conclusion says why. If the evidence does not report that, the word may be a decoy. Ask what the conclusion adds to the evidence instead.</div>
  <div class="quote">You said it yourself. You saw the word cause and thought causation. Then you read the conclusion again and asked, <em>"Why is it only harsh criticism? ... It could be gentle, it could be constructive ... it could be other things."</em> That second read is the method. It is the sufficient-versus-necessary question in your own words.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The other three</div>
  <h2>Together is not the same as because</h2>
  <p>On the test the evidence usually reports a study: two things happen together. The conclusion then says one of them is why the other happens. A correlation is easy to show. A cause is very hard to prove.</p>
  <div class="kinds">
    KIND_CORR
    KIND_CAUS
  </div>
  <div class="callout trap"><span class="tag">Three stories fit the same fact</span> Reading could keep students in school. Staying in school could give students more time to read. Or richer parents could give a child more books and more help, and that drives both. A correlation does not choose between them. Sometimes two things go together by coincidence. When the author picks one story, ask which others are still standing.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The other three</div>
  <h2>A group is not each of its members</h2>
  <p>What is true of a whole is not necessarily true of each part. What is true of one part is not necessarily true of the whole. The flaw runs in both directions.</p>
  <div class="kinds">
    KIND_WHOLE
    KIND_PART
  </div>
  <div class="callout"><span class="tag">You already do this</span> You told me you had seen questions like this and it felt like common sense. Your words were, <em>"Just because the team does well overall doesn't mean every single player on the team does well."</em> The name is new. The reasoning is yours. Watch for a noun that changes size between the evidence and the conclusion: a team and a player, a campus and a building.</div>
</div></section>

<section><div class="wrap">
  <div class="sec-kicker">The other three</div>
  <h2>No proof is not proof of the opposite</h2>
  <p>A lack of evidence is not evidence of lacking. If nobody has shown a claim is true, all you know is that nobody has shown it. You do not know it is false.</p>
  <div class="kinds">
    KIND_UNPROVEN
    KIND_FALSE
  </div>
  <div class="callout"><span class="tag">It fails in both directions</span> <em>"Because I can't prove you're innocent, you're guilty."</em> And the reverse: because I can't prove you're guilty, you're innocent. You put it that way yourself, and I called it the best example. The same move shows up on the test whenever an author says nobody has shown X, so not X.</div>
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
    <li><b>Keep the reference note, The Four Flaws to Know First, open.</b> Put it beside every flaw question. Write the name of the flaw next to your answer. When you miss one, write which of the four it was. In a week the pattern in your misses will show.</li>
    <li><b>Read one or two Reading Comprehension passages every other day.</b> Keep it light. The goal is to get used to the density of the language before we start the RC modules. Any Reading Comprehension passage works for this.</li>
    <li><b>Send me a message on the platform if you have a question.</b> I'll be able to get back to you.</li>
  </ol>
</div></section>

</main>"""

TEACH_BODY = TEACH_BODY.replace(
    "KIND_SUFF",
    kind_card(
        "apply",
        "Sufficient",
        "Enough to guarantee the result. If you have it, the result happens.",
        "A doctor's note gets you excused from the exam.",
        "If this is true, does the result have to follow?",
    ),
).replace(
    "KIND_NEC",
    kind_card(
        "link",
        "Necessary",
        "Required for the result. Without it, the result cannot happen.",
        "You must be enrolled in the course to sit the exam.",
        "If this is missing, is the result impossible?",
    ),
).replace(
    "KIND_CORR",
    kind_card(
        "apply",
        "Correlation",
        "Two things happen together. That is all it says.",
        "People who read a lot are less likely to drop out of high school.",
        "Does this only say they go together?",
    ),
).replace(
    "KIND_CAUS",
    kind_card(
        "link",
        "Causation",
        "One thing is the reason the other happens.",
        "Reading keeps students in school.",
        "Does this say why?",
    ),
).replace(
    "KIND_WHOLE",
    kind_card(
        "apply",
        "Whole to part",
        "A trait of the group gets pushed onto each member.",
        "The team is a star team, so every player on it is a superstar.",
        "Can the group have this trait while one member does not?",
    ),
).replace(
    "KIND_PART",
    kind_card(
        "link",
        "Part to whole",
        "A trait of one member gets pushed onto the group.",
        "She is the best guard in the country, so her team must be great.",
        "Can one member have this trait while the group does not?",
    ),
).replace(
    "KIND_UNPROVEN",
    kind_card(
        "apply",
        "Unproven",
        "No one has shown the claim is true. All we know is that it has not been shown.",
        "The prosecution could not prove you are guilty.",
        "Has anyone shown the opposite, or has no one shown anything?",
    ),
).replace(
    "KIND_FALSE",
    kind_card(
        "link",
        "Proven false",
        "Someone has shown the claim is false.",
        "The records show you were in another city that night.",
        "Is there evidence for the opposite, not just a lack of evidence?",
    ),
).replace(
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
  <p class="lede">Keep this open beside a flaw question. Name the flaw in the stimulus from this list before you read the answer choices.</p>
</div></header>

<main>

<section><div class="wrap">
  <div class="sec-kicker">The list</div>
  <h2>Four flaws, what they look like, and the tell</h2>
  <div class="table-wrap"><table class="t">
<thead><tr><th>Flaw</th><th>What the author does</th><th>The tell</th></tr></thead>
<tbody>
<tr><td>Sufficient versus necessary</td><td>Treats something that is enough as something that is required, or runs the rule backwards.<br><em>A doctor's note gets you excused. Jo has no note, so she will not be excused.</em></td><td>Must, only, unless, requires, or a rule about what is enough.</td></tr>
<tr><td>Correlation versus causation</td><td>Reports that two things go together, then picks one story for why.<br><em>People who read a lot are less likely to drop out of high school, so reading keeps students in school.</em></td><td>A study, survey or statistic in the evidence and a because in the conclusion.</td></tr>
<tr><td>Part versus whole</td><td>Pushes a trait of the group onto each member, or a trait of one member onto the group.<br><em>The campus is decent, so the law building on it is decent.</em></td><td>A noun that changes size: team to player, campus to building, ingredient to product.</td></tr>
<tr><td>Unproven versus proven false</td><td>Treats a lack of evidence for a claim as evidence against it.<br><em>I can't prove you are innocent, so you are guilty.</em></td><td>No evidence that, has not been shown, cannot prove.</td></tr>
</tbody>
</table></div>
  <div class="callout trap"><span class="tag">A cause word alone does not make it a causal flaw</span> If the conclusion says cause but the evidence does not report two things going together, look at what the conclusion adds to the evidence. In the practice question it was a sufficient condition treated as necessary.</div>
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
