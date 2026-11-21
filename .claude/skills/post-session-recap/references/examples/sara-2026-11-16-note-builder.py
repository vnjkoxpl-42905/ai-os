"""Build Sara Altuwaijri's 2026-11-16 note from the Lanae shell.

Reads wiki/homework-assigning/model-note/note-shell.html, fills it from the block lists below, and
never touches the shell's CSS or script. Writes recap.html (self-contained) and recap.fallback.md
(the plain-text version of the same note, for the student recap record).

Each section is a list of blocks. One renderer makes the HTML and another makes the markdown, so the
two cannot drift apart.

Run: python -I brainstorms/2026-11-16-sara-altuwaijri-post-session/build.py
"""
import html
import re
from pathlib import Path

ROOT = Path(r"C:/Users/Joshu/dev/ai-os")
SHELL = ROOT / "wiki/homework-assigning/model-note/note-shell.html"
OUT = ROOT / "brainstorms/2026-11-16-sara-altuwaijri-post-session"

LESSON_ID = "sara-2026-11-16-necessary-assumptions"
TITLE = "Necessary Assumption"
TITLE_L1, TITLE_L2 = "Necessary", "Assumption"

# Palette, 2026-11-17 (Joshua): no beige. Near-white page, pure white cards, near-black text, thin neutral rings.
# The shared shell file is untouched; these override its color variables, and WARM_TO_NEUTRAL swaps its hardcoded warm shadows and edges.
PALETTE = (
    ":root{--ground:#F4F4F1;--plane:#FFFFFF;--card:#FFFFFF;--well:#F2F2EF;--char:#151515;--char-2:#262626;"
    "--ink:#101010;--ink-soft:#383838;--ink-mute:#666666;--line:#E3E3DF;--edge:#D9D9D4;"
    "--brass:#C99A12;--brass-text:#755500;--brass-wash:rgba(224,170,20,.12);"
    "--green:#2D6A1B;--green-wash:rgba(45,106,27,.09);--red:#A8123D;--red-wash:rgba(168,18,61,.07);"
    "--lift-0:0 0 0 1px rgba(0,0,0,.06),0 1px 1px rgba(0,0,0,.04);"
    "--lift-1:0 0 0 1px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.05),0 14px 28px -20px rgba(0,0,0,.25);"
    "--lift-2:0 0 0 1px rgba(0,0,0,.07),0 2px 4px rgba(0,0,0,.06),0 24px 44px -26px rgba(0,0,0,.35)}"
    "body{background-image:none;background-color:var(--ground)}"
)
WARM_TO_NEUTRAL = {
    "rgba(60,45,20,": "rgba(0,0,0,", "rgba(40,30,15,": "rgba(0,0,0,", "rgba(50,38,18,": "rgba(0,0,0,",
    "#c9bca3": "#d6d6d1", "#d3c8b2": "#dcdcd7", "#c3b69c": "#cfcfca", "#fffdf8": "#ffffff", "#6b645a": "#666666",
}

EXTRA_CSS = PALETTE + (
    # Plain, editorial pull quote for what the student said. No dark box, no giant quote glyph.
    ".said{margin:28px 0 6px;padding:2px 0 2px 20px;border-left:3px solid var(--ink)}"
    ".said>b{display:block;margin-bottom:8px;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink-mute)}"
    ".said .q{margin:0 0 6px;font-family:var(--serif);font-size:20px;line-height:1.4;color:var(--ink)}"
    ".said .takeaway{margin:10px 0 0;font-size:17px;color:var(--ink-soft)}"
    # Flatten the decorative touches on the two-kind cards: no ruler ticks, no giant quote glyph.
    ".kind .bar,.kind.apply .bar{height:6px;background:var(--c)}"
    ".kind.link::after{content:none}"
    "@media (max-width:760px){header.hero{gap:64px}.stage{margin-top:28px}}"
    # Three fixed markings. Green = evidence, brass = conclusion, red dashed = the unstated assumption.
    "mark.ev,mark.co,mark.as{color:inherit;padding:.04em .28em;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}"
    "mark.ev{background:rgba(45,106,27,.15);box-shadow:inset 0 -2px 0 var(--green)}"
    "mark.co{background:var(--brass-wash);box-shadow:inset 0 -2px 0 var(--brass)}"
    "mark.as{background:var(--red-wash);box-shadow:inset 0 -2px 0 var(--red)}"
    # The argument laid out like an equation: evidence, a rule line, conclusion.
    ".arg{margin:26px 0 10px;padding:12px;display:flex;flex-direction:column;gap:6px;border-radius:22px;background:var(--card);"
    "box-shadow:inset 0 1px 0 #fff,0 1px 0 var(--edge),0 2px 0 var(--edge),0 18px 28px -20px rgba(60,45,20,.45)}"
    ".arg .row{position:relative;display:grid;grid-template-columns:132px 1fr;gap:12px;align-items:center;padding:15px 20px;border-radius:14px;box-shadow:none}"
    ".arg .row b{display:flex;align-items:center;gap:8px;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.13em;text-transform:uppercase;line-height:1.4}"
    ".arg .row b::before{content:'';flex:none;width:7px;height:7px;border-radius:2px;background:currentColor;transform:rotate(45deg)}"
    ".arg .row span{font-family:var(--serif);font-size:20px;line-height:1.3;color:var(--ink)}"
    ".arg .ev{background:#EAF1E5;box-shadow:inset 0 0 0 1px rgba(45,106,27,.30)}"
    ".arg .ev b{color:var(--green)}"
    ".arg .as{background:var(--red-wash);border:1.5px dashed rgba(168,18,61,.70)}"
    ".arg .as b{color:var(--red)}"
    ".arg .co{background:var(--brass-wash);box-shadow:inset 0 0 0 1px rgba(201,154,18,.45)}"
    ".arg .co b{color:var(--brass-text)}"
    ".arg .co span{font-size:22px;font-weight:600}"
    ".arg .eqplus{height:14px;line-height:14px;text-align:center;font-family:var(--serif);font-size:19px;color:var(--ink-mute)}"
    ".arg .eqline{display:flex;align-items:center;gap:12px;height:auto;margin:2px 6px;border:0;border-radius:0;background:none;box-shadow:none;"
    "color:var(--ink-mute);font-family:var(--serif);font-style:italic;font-size:15px}"
    ".arg .eqline::before,.arg .eqline::after{content:'';flex:1;border-top:2px solid var(--ink);opacity:.75}"
    ".arg.fall .co span{text-decoration:line-through;text-decoration-thickness:2px;opacity:.6}"
    ".arg.fall .co{background:repeating-linear-gradient(135deg,rgba(184,152,63,.10) 0 9px,transparent 9px 18px),var(--card)}"
    "@media (max-width:760px){.arg{padding:10px}.arg .row{grid-template-columns:1fr;gap:4px;padding:13px 16px}}"
    # The ladder: each amount, and whether it is necessary (required) and sufficient (enough).
    ".ladder{margin:24px 0 10px;padding:12px;border-radius:22px;background:var(--card);"
    "box-shadow:inset 0 1px 0 #fff,0 1px 0 var(--edge),0 2px 0 var(--edge),0 18px 28px -20px rgba(60,45,20,.45)}"
    ".ladder .lhead,.ladder .lrow{display:grid;grid-template-columns:minmax(0,1fr) 148px 148px;gap:10px;align-items:center}"
    ".ladder .lhead{padding:4px 16px 8px;font-family:var(--mono);font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink-mute)}"
    ".ladder .lhead span:nth-child(2){color:var(--green)}.ladder .lhead span:nth-child(3){color:var(--brass-text)}"
    ".ladder .lrow{margin-top:6px;padding:14px 16px;border-radius:14px;background:#F7F7F5;box-shadow:inset 0 0 0 1px rgba(0,0,0,.07)}"
    ".ladder .lrow.main{background:var(--brass-wash);box-shadow:inset 0 0 0 1.5px var(--brass)}"
    ".ladder .tagm{display:block;margin-bottom:4px;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--brass-text)}"
    ".ladder .amt strong{display:block;font-family:var(--serif);font-size:20px;line-height:1.25;font-weight:600;color:var(--ink)}"
    ".ladder .amt small{display:block;margin-top:3px;font-size:14.5px;line-height:1.4;color:var(--ink-soft)}"
    ".lad-pill{display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:8px 10px;border-radius:999px;font-family:var(--mono);font-size:11px;"
    "letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}"
    ".lad-pill.req{background:#E4EEDD;color:var(--green);box-shadow:inset 0 0 0 1px rgba(45,106,27,.40)}"
    ".lad-pill.enough{background:var(--brass-wash);color:var(--brass-text);box-shadow:inset 0 0 0 1px rgba(201,154,18,.55)}"
    ".lad-pill.no{background:transparent;color:var(--ink-mute);border:1px dashed rgba(102,102,102,.55)}"
    "@media (max-width:760px){.ladder .lhead{display:none}.ladder .lrow{grid-template-columns:1fr 1fr}.ladder .amt{grid-column:1 / -1}}"
)

shell = SHELL.read_text(encoding="utf-8")
HERO_START = shell.index('<header class="hero">')
MAIN_END = shell.index("</main>") + len("</main>")

e = html.escape


MARK = re.compile(r"\[\[(ev|co|as):(.+?)\]\]")


def plain(s):
    return MARK.sub(r"\2", s.replace("**", ""))


# ---------------------------------------------------------------- content
HERO = (
    "A necessary assumption is an idea the author has to agree with and never says. The trap is an answer the author only might agree with. "
    "Take the answer away and see whether the conclusion still stands."
)
SLABS = ("A necessary assumption", "Does it fall without it?", "What did the author never say?")

# ---- 1. Read it first
S1 = dict(kicker="Read it first", h2="An assumption is a premise nobody wrote down", blocks=[
    ("p", "In everyday talk, to assume means to guess. On the LSAT it means a premise the author needs and never states. Here's an argument."),
    ("argument", "You want to go to a top law school.", "You should apply to USC."),
    ("steps", [
        ("Find the conclusion.", "What does the author want you to believe? [[co:That you should apply to USC.]]"),
        ("Name the evidence.", "What reason does the author give? [[ev:That you want to go to a top law school.]] Accept it as true."),
        ("Ask what the author never wrote.", "The argument only works if [[as:USC is a top law school]]. Nobody said so. That unstated premise is the assumption."),
        ("Grant nothing that isn't on the page.", "The LSAT is written like a contract. Anything you fill in for the author counts against you."),
    ]),
    ("p", "Put the missing premise back and the argument holds together."),
    ("argument", "You want to go to a top law school.", "You should apply to USC.", "USC is a top law school."),
    ("callout", "What you're practicing", "Don't ask whether the argument sounds reasonable. Ask what has to be on the page for the conclusion to follow.", False),
    ("p", "That's because valid is strict here. An argument is valid only if the conclusion can't be false when the evidence is true. "
          "There's no halfway, and almost every argument on the LSAT falls short. The assumption is what closes the gap."),
    ("said", ["“There's a missing link … whether USC is a top law school or not, because we're assuming that it is.”"],
     "That's the move. A missing link is a missing premise, and a missing premise is an assumption."),
])

# ---- 2. Two kinds
S2 = dict(kicker="Two kinds", h2="Required, or enough?", blocks=[
    ("p", "Necessary and sufficient assumptions sound alike but answer different questions. Take a cash register. A pack costs $20 and the customer puts $18 on the counter."),
    ("argument", "The customer puts $18 on the counter.", "The $20 pack is paid for.", "The customer pays $2 more."),
    ("p", "[[as:The $2 in between is the assumption.]] So what does the customer have to be able to pay? Check each amount two ways. "
          "Is it required to cover the $2? That's necessary. Is it enough to cover the $2? That's sufficient."),
    ("ladder", [
        ("At least 50 cents", "The customer has to be able to pay this much, but it's far short of $2.", True, False, False),
        ("At least $1.95", "The customer has to be able to pay this much. It's still 5 cents short, so it isn't enough.", True, False, False),
        ("At least $2", "The customer has to be able to pay this much, and it covers the $2 exactly.", True, True, True),
        ("$10", "More than enough, but the customer didn't have to pay this much.", False, True, False),
    ]),
    ("kinds", [
        ("apply", "Necessary assumption",
         "What the conclusion requires. The customer has to be able to pay at least $1.95. It's the floor, so the right answer is usually weak.",
         "The customer can pay at least $1.95.",
         "If this were false, would the conclusion fail?"),
        ("link", "Sufficient assumption",
         "Enough to guarantee the conclusion. At least $2 is the least that's enough, and more is fine, so the right answer is usually strong.",
         "The customer puts down $10.",
         "If this were true, would the conclusion have to follow?"),
    ]),
    ("callout", "Where they meet", "At exactly $2, the least that's required and the least that's enough are the same amount. "
                "I call that the main assumption: the perfect bridge, not one penny too much or too little. It's why one statement can be both kinds.", False),
    ("p", "A question only has to give you one required idea, and any of them can be the answer. Under “USC is a top law school” sits “USC has a law school.” "
          "It's obvious and it's required. That's why necessary answers can look too easy to be right."),
])

# ---- 3. The check
S3 = dict(kicker="The check", h2="Two directions, one test", blocks=[
    ("p", "In the guessing game you asked true or false questions to find the person I had in mind. Singer, American and male all had to be true. "
          "Alive had to be false, because a living person can't be Michael Jackson. So a necessary assumption comes in two kinds."),
    ("opposite", ("Linking: has to be true",
                  "A missing idea the author has to agree with. You're repairing the argument, so stay inside what the author said and find the link. Treat it like a Must Be True question."),
                 ("Defender: has to be false",
                  "An objection that would sink the argument. The author has to reject it, even if nobody raised it. It can bring in something the author never mentioned.")),
    ("p", "Two checks sort any answer. Did the author say it? Does the conclusion fail without it?"),
    ("gate", dict(
        h3="Try the two checks",
        sw=("The author never said it", "The conclusion fails without it"),
        v=("Neither. This isn't an assumption the argument needs.",
           "Only unstated. It may add something the argument can do without.",
           "Only required. If it's already written, it's evidence, not an assumption.",
           "Both pass. This is a necessary assumption."),
    )),
    ("p", "The second check is the one to practice:"),
    ("steps", [
        ("Say what the answer claims.", "Use plain words."),
        ("Negate it.", "Treat it as not true. Leave the author's evidence alone."),
        ("Pull it out like a block from a Jenga tower.", "If the conclusion falls, the author needed the answer. If it still stands, the answer wasn't required."),
    ]),
    ("p", "Example. Take the USC argument and the answer [[as:“USC is a top law school.”]] Negate it, and leave the evidence alone."),
    ("argument", "You want to go to a top law school.", "You should apply to USC.", "USC is not a top law school.", {"con_label": "Falls", "fall": True}),
    ("p", "There's now no reason to apply to USC. The conclusion falls, so the answer was required."),
    ("callout", "Negating a rule",
     "“Unless you have a passport, you can't enter Canada” means “If you don't have a passport, you can't enter.” "
     "To negate it, make the rule fail: no passport, and you enter anyway. "
     "You said, “if you don't have a passport, you will enter Canada.” As one person who gets in, that's the negation. "
     "As a rule about everyone without a passport, it claims too much, so write it as one case. "
     "Quantities negate their own way: the negation of all is not all, and the negation of some is none.", False),
])

# ---- 4. Answer strength
S4 = dict(kicker="Answer strength", h2="Necessary answers ask for as little as possible", blocks=[
    ("flags", ["only", "most", "all", "every"]),
    ("p", "A necessary assumption is the least the argument needs, so the right answer is usually weak. A strong claim usually asks for more than the argument requires. "
          "Slow down when you see these words."),
    ("p", "Judge the idea, not the word. “The author requires the capacity to feel emotion” sounds firm, but it only asks that you can feel one emotion, ever. "
          "That's a low bar. And weak wording doesn't make an answer right either. It still has to be needed."),
    ("callout", "The trap that costs the most",
     "Choosing an answer the author might also agree with, or one that helps the argument. The author may like it, but the argument doesn't need it. "
     "A necessary assumption is one the author has to agree with. Negate the answer and see whether the argument still stands. If it does, the answer wasn't required.", True),
    ("said", ["“I'm always looking for a stronger answer choice. And for necessary, we're looking for the weaker answer choice.”",
              "“Too strong for a necessary assumption.”"],
     "The second line was your reason for cutting an answer with only. Both are the right reasons. Keep using them."),
])

# ---- 5. The route
S5 = dict(kicker="The route", h2="Name how the author gets from evidence to conclusion", blocks=[
    ("p", "The evidence is where the author starts. The conclusion is where the author ends up. The method of reasoning is how the author travels between them, "
          "like flying or taking the train to the same city. There are three."),
    ("ul", [
        ("Conditional.", "“If you work really hard, you'll get a 170.”"),
        ("Causal.", "“Working hard leads to a 170.”"),
        ("Comparative.", "“Michael studied really hard and got a 170, so you will too.”"),
    ]),
    ("p", "Each one breaks in its own way. A conditional breaks when a requirement is treated as a guarantee: "
          "“Working hard is required for a 170. You work hard. So you'll get a 170.” Required isn't enough."),
    ("callout", "Name it as you read",
     "You said the conditional and the causal versions were “kind of saying the same thing.” They're close, which is why you name the route every time. "
     "Spot a conditional and expect a missing link between the evidence and the conclusion.", False),
])

# ---- 6. Try it
S6 = dict(kicker="Try it", h2="Check yourself", blocks=[
    ("drill", dict(
        h3="Say it out loud, then tap to check",
        hint="A ticket costs $15 and the customer put $12 on the counter, so $3 is owed. For each payment, is it required, enough, or both?",
        passage=None,
        chips=[
            ("assume", "The customer can pay at least $2.50.", "Required only",
             "Required only. The customer has to be able to pay that much. It still leaves 50 cents owed, so it isn't enough."),
            ("describe", "The customer can pay at least $3.", "Both",
             "Both. Anything less leaves the debt unpaid, and this much covers it. This is the main assumption."),
            ("neutral", "The customer puts down $20.", "Enough only",
             "Enough only. It covers the debt with room to spare. The customer didn't need to pay that much."),
        ],
    )),
    ("argument", "The café added a second register.", "Lines will get shorter."),
    ("drill", dict(
        h3="Negate it. Does the conclusion fall?",
        hint="Treat each answer as not true, leave the evidence alone, and ask whether the conclusion still stands.",
        passage=None,
        chips=[
            ("describe", "A second register will be staffed.", "Necessary",
             "Necessary. Negate it: the second register won't be staffed. Then adding it changes nothing, and the conclusion falls."),
            ("object", "The owner wants shorter lines.", "Not required",
             "Not required. The author might agree with it. Negate it and lines can still get shorter."),
            ("object", "Every customer will use the second register.", "Too strong",
             "Too strong. Negate it: some customers still use only the first register. Lines can still get shorter."),
        ],
    )),
    ("drill", dict(
        h3="Is the argument valid?",
        hint="Valid means the conclusion can't be false if the evidence is true.",
        passage="Say what the rule is, then ask whether the evidence meets what the rule needs.",
        chips=[
            ("describe", "If you work really hard, you'll get a 170. Dana works really hard. So Dana will get a 170.", "Valid",
             "Valid. The if part of the rule is met, so the result has to follow."),
            ("object", "Working hard is required for a 170. Dana works really hard. So Dana will get a 170.", "Not valid",
             "Not valid. In your words, “just because that's a requirement doesn't mean that you're going to get that.” Required isn't enough."),
            ("object", "If you're in Toronto, you're in Canada. Dana is from Toronto. So Dana is in Canada.", "Not valid",
             "Not valid. You caught this in the session: “Just because someone's from there doesn't mean they're there right now.” The rule is about being in Toronto. The evidence is about where she's from."),
        ],
    )),
])

# ---- 7. On every question
S7 = dict(kicker="On every question", h2="Before you read the answer choices", blocks=[
    ("p", "Do the work on the left, in the stimulus. The choices on the right are where you check the idea, not where you find it."),
    ("screen", "Stimulus on the left. Choices on the right."),
    ("steps", [
        ("Read the stem.", "“Depends on,” “requires,” “presupposes” and “relies on” ask for a necessary assumption. “What would make the conclusion follow” asks for a sufficient one."),
        ("Find the conclusion and the evidence.", "Say them in plain words. Accept the evidence."),
        ("Predict what's missing.", "What has to be on the page for the conclusion to follow? Is the answer likely a link or a defender?"),
        ("Check the choices against your prediction.", "Negate the one you like. If the conclusion still stands, it wasn't required."),
    ]),
])

CLOSE = dict(h2="What to do next", steps=[
    ("Rephrase in your own words.", "Put the stimulus and each answer choice into words you'd say out loud. I'm assigning a drill for this."),
    ("Do the necessary assumption questions.", "I'm assigning them with a note. Read the note first."),
    ("Practice negation.", "I'm assigning a drill on negating conditional, quantity and correlation statements. It makes the negate-it check automatic."),
    ("Wednesday, November 18.", "We'll go into statement types and argument parts, the same skill as role questions."),
    ("Send me a message on the platform if you have a question.", "I'll be able to get back to you."),
])

# S5 (The route) moved to the second note, Method of Reasoning, on 2026-11-17.


# ---------------------------------------------------------------- html renderers
def esc(t):
    """Escape text, then turn [[ev:...]], [[co:...]] and [[as:...]] into the three colored marks."""
    return MARK.sub(lambda m: '<mark class="%s">%s</mark>' % (m.group(1), m.group(2)), e(t, quote=False))


def steps_html(steps, cls=""):
    return '<ol class="steps%s">%s</ol>' % (
        " " + cls if cls else "",
        "".join("<li><b>%s</b> %s</li>" % (esc(h), esc(t)) for h, t in steps),
    )


def kind_card(cls, name, what, looks, test):
    return (
        '<div class="kind %s"><span class="bar"></span><div class="name">%s</div>'
        '<p class="what">%s</p><div class="words"><b>Looks like</b> <span>%s</span></div>'
        '<div class="test"><b>Test</b>%s</div></div>' % (cls, esc(name), esc(what), esc(looks), esc(test))
    )


def chip(kind, item, stamp, ans):
    return (
        '<div class="chip" data-k="%s" role="button" tabindex="0" aria-expanded="false">'
        '<span>%s</span><span class="stamp" aria-hidden="true">%s</span><span class="ans">%s</span></div>'
        % (kind, esc(item), esc(stamp), esc(ans))
    )


def drill_html(d):
    pas = '<p class="passage"><em>%s</em></p>' % esc(d["passage"]) if d["passage"] else ""
    return (
        '<div class="drill">\n<div class="drill-head"><div><h3>%s</h3><p class="hint">%s</p></div></div>\n%s\n<div class="chips">\n%s\n</div>\n</div>'
        % (esc(d["h3"]), esc(d["hint"]), pas, "\n".join(chip(*c) for c in d["chips"]))
    )


def gate_html(g):
    sw = '<button class="sw" type="button" role="switch" aria-checked="false"><span class="track"><span class="knob"></span></span><span>%s</span></button>'
    return (
        '<div class="gate" data-state="0">\n<h3>%s</h3><p class="hint">Flip each switch and see what kind of statement it is.</p>\n<div class="gate-body">\n%s\n%s\n'
        '<div class="verdict" role="status"><i class="lamp"></i>\n<span class="v0">%s</span><span class="v1">%s</span><span class="v2">%s</span><span class="v3">%s</span></div>\n</div>\n</div>'
        % (esc(g["h3"]), sw % esc(g["sw"][0]), sw % esc(g["sw"][1]), *[esc(x) for x in g["v"]])
    )


def screen_html(caption):
    return (
        '<figure class="screen"><div class="bezel"><div class="panes">'
        '<div class="pane left"><b>Stimulus</b><i></i><i></i><i class="hit"></i><i></i></div>'
        '<div class="pane right"><b>Answer choices</b><i data-l="A"></i><i data-l="B"></i><i data-l="C"></i><i data-l="D"></i><i data-l="E"></i></div>'
        '</div></div><figcaption>%s</figcaption></figure>' % esc(caption)
    )


def block_html(blk):
    k = blk[0]
    if k == "p":
        return "<p>%s</p>" % esc(blk[1])
    if k == "h3":
        return "<h3>%s</h3>" % esc(blk[1])
    if k == "steps":
        return steps_html(blk[1])
    if k == "ul":
        return "<ul>%s</ul>" % "".join("<li><strong>%s</strong> %s</li>" % (esc(h), esc(t)) for h, t in blk[1])
    if k == "callout":
        return '<div class="callout%s"><span class="tag">%s</span> %s</div>' % (" trap" if blk[3] else "", esc(blk[1]), esc(blk[2]))
    if k == "quote":
        return '<div class="quote">%s</div>' % esc(blk[1])
    if k == "said":
        return ('<div class="said"><b>What you said</b>%s<p class="takeaway">%s</p></div>'
                % ("".join('<p class="q">%s</p>' % esc(q) for q in blk[1]), esc(blk[2])))
    if k == "kinds":
        return '<div class="kinds">\n%s\n</div>' % "\n".join(kind_card(*c) for c in blk[1])
    if k == "opposite":
        return '<div class="opposite"><div><b>%s</b>%s</div><div><b>%s</b>%s</div></div>' % (
            esc(blk[1][0]), esc(blk[1][1]), esc(blk[2][0]), esc(blk[2][1]))
    if k == "gate":
        return gate_html(blk[1])
    if k == "flags":
        return '<div class="flags">%s</div>' % "".join('<span class="flag">%s</span>' % e(w) for w in blk[1])
    if k == "drill":
        return drill_html(blk[1])
    if k == "screen":
        return screen_html(blk[1])
    if k == "ladder":
        def pill(on, yes, no, cls):
            return '<span class="lad-pill %s">%s</span>' % (cls if on else "no", ("✓ " + yes) if on else ("✗ " + no))
        rows = []
        for amt, why, req, enough, main in blk[1]:
            rows.append(
                '<div class="lrow%s"><div class="amt">%s<strong>%s</strong><small>%s</small></div>%s%s</div>'
                % (" main" if main else "", '<span class="tagm">Main assumption</span>' if main else "", esc(amt), esc(why),
                   pill(req, "Required", "Not required", "req"), pill(enough, "Enough", "Not enough", "enough")))
        return ('<div class="ladder" role="group" aria-label="Each amount, and whether it is required and whether it is enough">'
                '<div class="lhead"><span>The customer can pay</span><span>Necessary</span><span>Sufficient</span></div>%s</div>' % "".join(rows))
    if k == "argument":
        opt = blk[4] if len(blk) > 4 else {}
        missing = ('<div class="eqplus" aria-hidden="true">+</div><div class="row as"><b>%s</b><span>%s</span></div>' % (esc(opt.get("label", "Assumption")), esc(blk[3]))) if len(blk) > 3 and blk[3] else ""
        fall = " fall" if opt.get("fall") else ""
        return ('<div class="arg%s" role="group" aria-label="An argument: evidence above the line, conclusion below"><div class="row ev"><b>Evidence</b><span>%s</span></div>%s'
                '<div class="eqline" aria-hidden="true">so</div><div class="row co"><b>%s</b><span>%s</span></div></div>'
                % (fall, esc(blk[1]), missing, esc(opt.get("con_label", "Conclusion")), esc(blk[2])))
    raise ValueError(k)


def section_html(S):
    inner = '<div class="sec-kicker">%s</div>\n<h2>%s</h2>\n%s' % (esc(S["kicker"]), esc(S["h2"]), "\n".join(block_html(b) for b in S["blocks"]))
    return '<section><div class="wrap">\n%s\n</div></section>' % inner


def hero_html(n):
    s = n["slabs"]
    return (
        '<header class="hero"><div class="wrap">\n'
        '  <div class="kicker">Session recap · November 16</div>\n'
        "  <h1>%s<br>%s</h1>\n"
        '  <p class="lede">%s</p>\n</div>\n'
        '<div class="stage" aria-hidden="true"><div class="stack" data-tilt="10">\n'
        '  <div class="slab base"><i>RESULT</i><b>%s</b></div>\n'
        '  <div class="slab c2"><i>CHECK 2</i><b>%s</b></div>\n'
        '  <div class="slab c1"><i>CHECK 1</i><b>%s</b></div>\n'
        "</div></div></header>" % (e(n["l1"]), e(n["l2"]), esc(n["hero"]), e(s[0]), e(s[1]), e(s[2]))
    )


def close_html(c):
    return (
        '<section><div class="wrap">\n<div class="sec-kicker">Your work</div>\n<h2>%s</h2>\n%s\n</div></section>'
        % (esc(c["h2"]), steps_html(c["steps"], "todo"))
    )


def build(n):
    body = hero_html(n) + "\n\n<main>\n\n" + "\n\n".join(section_html(S) for S in n["sections"]) + "\n\n" + close_html(n["close"]) + "\n\n</main>"
    head = shell[:HERO_START]
    for warm, neutral in WARM_TO_NEUTRAL.items():
        head = head.replace(warm, neutral)
    out = head + body + shell[MAIN_END:]
    # Render check 2026-11-17: below 760px the 3D stack rises into the last line of the lede. A second
    # <style> block after the shell's own carries the fix, so the shell's CSS and script stay byte-identical.
    out = out.replace("</style>", "</style>\n<style>" + EXTRA_CSS + "</style>", 1)
    out = re.sub(r'(<meta name="lsatu-interactive-lesson" content=")[^"]*(">)', r"\g<1>%s\g<2>" % n["lesson_id"], out, count=1)
    out = re.sub(r"<title>.*?</title>", "<title>%s · Session recap</title>" % e(n["title"]), out, count=1, flags=re.S)
    assert "{{" not in out, "unfilled slot"
    return out


# ---------------------------------------------------------------- markdown renderer
def block_md(blk):
    k = blk[0]
    if k == "p":
        return blk[1]
    if k == "h3":
        return "### %s" % blk[1]
    if k == "steps":
        return "\n".join("%d. **%s** %s" % (i + 1, h, t) for i, (h, t) in enumerate(blk[1]))
    if k == "ul":
        return "\n".join("- **%s** %s" % (h, t) for h, t in blk[1])
    if k == "callout":
        return "> **%s.** %s" % (blk[1], blk[2])
    if k == "quote":
        return "> %s" % blk[1]
    if k == "said":
        return "> **What you said:** %s\n>\n> %s" % (" ".join(blk[1]), blk[2])
    if k == "kinds":
        return "\n\n".join("**%s.** %s Looks like: %s Test: %s" % (c[1], c[2], c[3], c[4]) for c in blk[1])
    if k == "opposite":
        return "**%s.** %s\n\n**%s.** %s" % (blk[1][0], blk[1][1], blk[2][0], blk[2][1])
    if k == "gate":
        g = blk[1]
        return "Two checks: (1) %s. (2) %s. If neither: %s If only the first: %s If only the second: %s If both: %s" % (g["sw"][0], g["sw"][1], *g["v"])
    if k == "flags":
        return "Words to slow down on: %s." % ", ".join(blk[1])
    if k == "drill":
        d = blk[1]
        lines = ["**%s** %s" % (d["h3"], d["hint"])]
        if d["passage"]:
            lines += ["", "*%s*" % d["passage"]]
        lines.append("")
        for _kind, item, stamp, ans in d["chips"]:
            rest = ans[len(stamp):].lstrip(". ") if ans.startswith(stamp) else ans
            lines.append("- %s **%s.** %s" % (item, stamp, rest))
        return "\n".join(lines)
    if k == "screen":
        return "*%s*" % blk[1]
    if k == "ladder":
        return "\n".join("- **%s.** %s Necessary: %s. Sufficient: %s.%s" % (a, w, "yes" if r else "no", "yes" if s else "no", " This is the main assumption." if m else "")
                         for a, w, r, s, m in blk[1])
    if k == "argument":
        opt = blk[4] if len(blk) > 4 else {}
        mid =("\n> **%s:** %s" % (opt.get("label", "Assumption"), blk[3])) if len(blk) > 3 and blk[3] else ""
        return "> **Evidence:** %s%s\n> **%s:** %s" % (blk[1], mid, opt.get("con_label", "Conclusion"), blk[2])
    raise ValueError(k)


def fallback_md(n):
    L = ["# %s" % n["title"], "", plain(n["hero"]), ""]
    for S in n["sections"]:
        L += ["## %s" % S["h2"], ""]
        for b in S["blocks"]:
            L += [block_md(b), ""]
    L += ["## %s" % n["close"]["h2"], "", "\n".join("- [ ] **%s** %s" % (h, t) for h, t in n["close"]["steps"])]
    return MARK.sub(r"\2", "\n".join(L)) + "\n"


# ================================================================ Note 2: Method of Reasoning
# Split out of Necessary Assumption on 2026-11-17 (Joshua): a different scope gets its own, shorter note.
M1 = dict(kicker="Read it first", h2="The author starts somewhere and ends somewhere", blocks=[
    ("p", "Every argument starts with evidence and ends with a conclusion. The method of reasoning is how the author gets from one to the other, "
          "like flying or taking the train to the same city."),
    ("argument", "You work really hard.", "You'll get a 170."),
    ("p", "Same start, same finish. There are three ways to get there."),
    ("kinds", [
        ("apply", "Conditional",
         "Uses a rule. If one thing is true, another has to be.",
         "If you work really hard, you'll get a 170.",
         "Is the if part actually met?"),
        ("link", "Causal",
         "Says one thing produces another.",
         "Working hard leads to a 170.",
         "Could something else explain it, or could it run the other way?"),
        ("warn", "Comparative",
         "Says what happened to one case will happen to another.",
         "Michael studied really hard and got a 170, so you will too.",
         "Are the two cases alike where it matters?"),
    ]),
    ("callout", "Don't read past it",
     "When you see a conditional, a cause or a comparison, don't read past it. The author is using it to get from the evidence to the conclusion, "
     "so check whether it can carry that weight.", False),
])

M2 = dict(kicker="Where it breaks", h2="Each route fails in its own way", blocks=[
    ("p", "Once you know the route, you know where to look for the gap."),
    ("h3", "Conditional: a requirement is not a guarantee"),
    ("p", "This is the break to expect. The author treats something that's required as if it were enough."),
    ("argument", "Working hard is required for a 170. You work hard.", "You'll get a 170.", None, {"con_label": "Doesn't follow", "fall": True}),
    ("p", "Working hard is required. It isn't enough. In your words, “just because that's a requirement doesn't mean that you're going to get that.”"),
    ("h3", "Causal: another cause, or the other direction"),
    ("p", "The author says one thing produces another. Ask whether something else could explain the same result, or whether it runs the other way."),
    ("h3", "Comparative: the two cases have to be alike"),
    ("p", "The author says what happened to one case will happen to another. Ask whether the two differ in a way that matters."),
])

M3 = dict(kicker="Why it matters", h2="The route points at the missing idea", blocks=[
    ("p", "On a necessary assumption question, name the route before you read the choices. A conditional points at a missing link. "
          "A cause points at another explanation the author has to rule out. A comparison points at a similarity the author needs."),
    ("callout", "Name it every time",
     "You said the conditional and the causal versions were “kind of saying the same thing.” They're close, which is why you name the route every time. "
     "Each one fails differently.", False),
])

M4 = dict(kicker="Try it", h2="Name the route", blocks=[
    ("drill", dict(
        h3="Say it out loud, then tap to check",
        hint="Is each sentence conditional, causal or comparative?",
        passage=None,
        chips=[
            ("describe", "If the museum is open, the lights are on.", "Conditional",
             "Conditional. It's an if/then rule."),
            ("assume", "Heavy rain makes the river flood.", "Causal",
             "Causal. It says one thing produces another."),
            ("neutral", "Her sister took the class and passed, so she will pass too.", "Comparative",
             "Comparative. It says what happened to one case will happen to another."),
            ("describe", "Only members may enter the library.", "Conditional",
             "Conditional. “Only” sets a requirement: if you enter, you're a member."),
        ],
    )),
])

M_CLOSE = dict(h2="What to do next", steps=[
    ("Name each statement type.", "As you read, label every statement as conditional, causal or comparison. I'm assigning practice for this."),
    ("Wednesday, November 18.", "We'll go into statement types and argument parts, the same skill as role questions."),
    ("Send me a message on the platform if you have a question.", "I'll be able to get back to you."),
])

NOTES = [
    dict(
        key="necessary", lesson_id=LESSON_ID, title=TITLE, l1=TITLE_L1, l2=TITLE_L2, hero=HERO, slabs=SLABS,
        sections=[S1, S2, S3, S4, S6, S7], close=CLOSE,
        html_name="recap.html", md_name="recap.fallback.md",
    ),
    dict(
        key="method", lesson_id="sara-2026-11-16-method-of-reasoning", title="Method of Reasoning", l1="Method of", l2="Reasoning",
        hero="Every argument gets from evidence to conclusion by some route. Name the route as you read, "
             "and you know where that argument is most likely to break.",
        slabs=("A method of reasoning", "What carries it to the conclusion?", "Where does the author start?"),
        sections=[M1, M2, M3, M4], close=M_CLOSE,
        html_name="recap-method-of-reasoning.html", md_name="recap-method-of-reasoning.fallback.md",
    ),
]


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n in NOTES:
        (OUT / n["html_name"]).write_text(build(n), encoding="utf-8")
        (OUT / n["md_name"]).write_text(fallback_md(n), encoding="utf-8")
        print("wrote", OUT / n["html_name"], (OUT / n["html_name"]).stat().st_size, "bytes")
