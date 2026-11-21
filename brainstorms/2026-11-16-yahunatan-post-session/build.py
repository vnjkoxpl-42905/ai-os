"""Build Yahunatan Zetvy's two 2026-11-16 notes from the Lanae shell.

Copied from skills/claude/post-session-recap/references/examples/sara-2026-11-16-note-builder.py.
Reads wiki/homework-assigning/model-note/note-shell.html and never edits the shell. Writes each note as one
self-contained HTML file plus a Markdown fallback of the same text, so the two cannot drift. Also runs a copy lint
and a strict word count (hidden answers included).

Run: python -I brainstorms/2026-11-16-yahunatan-post-session/build.py
"""
import html
import re
from pathlib import Path

ROOT = Path(r"C:/Users/Joshu/dev/ai-os")
SHELL = ROOT / "wiki/homework-assigning/model-note/note-shell.html"
OUT = ROOT / "brainstorms/2026-11-16-yahunatan-post-session"
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
    "box-shadow:inset 0 1px 0 #fff,0 1px 0 var(--edge),0 2px 0 var(--edge),0 18px 28px -20px rgba(0,0,0,.28)}"
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
    "box-shadow:inset 0 1px 0 #fff,0 1px 0 var(--edge),0 2px 0 var(--edge),0 18px 28px -20px rgba(0,0,0,.28)}"
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
        '  <div class="slab base"><i>%s</i><b>%s</b></div>\n'
        '  <div class="slab c2"><i>%s</i><b>%s</b></div>\n'
        '  <div class="slab c1"><i>%s</i><b>%s</b></div>\n'
        "</div></div></header>" % (e(n["l1"]), e(n["l2"]), esc(n["hero"]), e(n["labels"][0]), e(s[0]), e(n["labels"][1]), e(s[1]), e(n["labels"][2]), e(s[2]))
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
    out = re.sub(r"<!-- HERO\.[^\n]*?-->\n?", "", out, count=1)
    assert "{{" not in out, "unfilled slot"
    assert "<!--" not in out, "template comment left in output"
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


# ================================================================ Note 1: Reading an Argument in Three Steps
A_HERO = (
    "When a question won't click, you're usually missing one of five points. Three of them live in the stimulus: where the argument starts and ends, "
    "how it gets from one to the other, and what it leaves out. Run them on every argument and you'll see exactly where you got stuck."
)
A_SLABS = ("The missing piece", "How does it get there?", "Where does it start and end?")
A_LABELS = ("STEP 3", "STEP 2", "STEP 1")

A1 = dict(kicker="Read it first", h2="Five points, and where they sit", blocks=[
    ("p", "Here are five points to run on Logical Reasoning questions. Three of them work on the stimulus. Two work on the answer choices. "
          "This note covers the three on the stimulus."),
    ("steps", [
        ("Structure.", "Where does the argument start, and where does it end?"),
        ("Method of reasoning.", "How does the author get from the start to the end?"),
        ("Assumption.", "What did the author leave out?"),
    ]),
    ("p", "The other two points are keyword mapping and putting abstract answer choices in plain English. They're in the next note, Mapping Abstract Answers Back to the Argument."),
    ("callout", "The steps show you where you got stuck",
     "When a question isn't connecting, run them in order. The first one you can't answer is the one to work on. After a miss, do the same. "
     "It takes a lot of practice to get good at this, so use it on every argument.", False),
])

A2 = dict(kicker="Structure", h2="Find where the argument starts and ends", blocks=[
    ("p", "An argument starts with evidence, which is the premise, and ends with the conclusion. On the page the conclusion can come first, but the reasoning still runs from the evidence to it. That's the structure. Here's a short one."),
    ("p", "Some people say the new bus line is too slow. A few routes do run late. [[ev:But it cut the average commute by ten minutes]], so [[co:the city should keep it]]."),
    ("argument", "It cut the average commute by ten minutes.", "The city should keep the new bus line."),
    ("p", "Two sentences in there aren't the evidence or the conclusion. Mark them anyway, because they show you where the author is headed. Here are four kinds of sentence like that. The first two are in the passage above. The last two show up in other arguments."),
    ("ul", [
        ("Opposing view.", "What other people say. The author brings it up to push back on it. “Some people say the new bus line is too slow.”"),
        ("Concession.", "The author grants a point, then pushes back. “A few routes do run late.”"),
        ("Background information.", "Context that sets the scene. It isn't a reason for the conclusion."),
        ("Intermediate conclusion.", "A claim that has support and also gives support. If it has support, it's a conclusion. If it gives support, it's a premise. If it does both, it's an intermediate conclusion."),
    ]),
    ("p", "To test whether a claim is a conclusion, ask yourself why you should believe it. If the author gives you a reason, it's a conclusion."),
])

A3 = dict(kicker="Method of reasoning", h2="Then name how the author gets there", blocks=[
    ("p", "You can get from Florida to Canada by plane, train or bus. Any of them works if you do it properly. An argument is the same. "
          "Say the start is that you study hard and the finish is a 160. There's more than one way to get from one to the other."),
    ("kinds", [
        ("apply", "Conditional",
         "Uses a rule. If one thing is true, the other has to be.",
         "If you study hard, you'll score a 160.",
         "Is something that's only required being treated as enough?"),
        ("link", "Causal",
         "Says one thing produces another.",
         "Studying hard will cause you to score a 160.",
         "Does the evidence show a cause, or only that the two go together?"),
        ("warn", "Comparative",
         "Says what happened to one case will happen to another.",
         "Richard studied the way you do and scored a 160, so you will too.",
         "Are the two cases alike where it matters?"),
    ]),
    ("p", "Those are the most common. There are others, like generalizing from a group (“Everyone in the study group who studied hard scored a 160”) or ruling out alternatives. "
          "The list isn't complete. Name whichever you see. Sometimes it's more than one."),
    ("callout", "Name the method and you know where it breaks",
     "In a flawed argument, the conclusion goes wrong somewhere, and the method points at the spot. “People who study hard are more likely to score a 160” is a correlation. "
     "“Studying hard will cause a 160” is a cause. They aren't the same claim.", False),
    ("argument", "People who study hard are more likely to score a 160.", "Studying hard will cause you to score a 160.", None, {"con_label": "Doesn't follow", "fall": True}),
    ("said", ["“This reminds me of flaws ... if it's a comparison, then I'm looking for that in the answer choice.”"],
     "That's the link. The method tells you which flaw to expect, and you already do this on flaw questions."),
])

A4 = dict(kicker="Assumption", h2="Then find what the author left out", blocks=[
    ("p", "An assumption is a missing piece of evidence. The author left it out, so the evidence doesn't guarantee the conclusion. "
          "If the argument already says it, it isn't the assumption."),
    ("p", "A common mistake with a conditional is treating a requirement as if it were a guarantee, or treating something that is enough as if it were required."),
    ("argument", "Studying hard is required to score a 160. You study hard.", "You'll score a 160.", "If you study hard, you'll score a 160."),
    ("p", "Required isn't enough. Put the missing sentence back and the argument works. Leave it out and the conclusion doesn't follow."),
    ("p", "A license is required to rent a car. Having one doesn't get you a car. You still need a deposit and a car on the lot."),
    ("said", ["“It doesn't mean that you're going to get a 160 ... You can't say that it guarantees anything.”"],
     "That's it. A requirement is something you need. It doesn't guarantee the result."),
    ("h3", "All three steps on one argument"),
    ("p", "[[ev:Some meals that critics call plain taste wonderful. A meal is excellent only if it tastes wonderful.]] So [[co:some meals that critics call plain are excellent]]."),
    ("steps", [
        ("Structure.", "The conclusion is that some of those meals are excellent. The two sentences before it are the evidence."),
        ("Method of reasoning.", "The second sentence is a conditional. As an if/then: if a meal is excellent, then it tastes wonderful. "
                                 "The contrapositive: if it doesn't taste wonderful, it isn't excellent. Those two say the same thing. "
                                 "“If it tastes wonderful, it's excellent” says something different, and the rule doesn't give it to you."),
        ("Assumption.", "The conclusion treats tasting wonderful as if it made a meal excellent."),
    ]),
    ("argument", "Some meals that critics call plain taste wonderful. A meal is excellent only if it tastes wonderful.",
     "Some meals that critics call plain are excellent.", "If a meal tastes wonderful, it's excellent."),
    ("p", "Tasting wonderful is required for excellent. The argument needs it to be enough. You caught the same swap on a real question in the session. "
          "The conclusion replaced one idea with another and treated them as the same thing."),
])

A5 = dict(kicker="Try it", h2="Check yourself", blocks=[
    ("drill", dict(
        h3="Say it out loud, then tap to check",
        hint="Which part of the argument is each sentence?",
        passage="Some say the museum should keep its entry fee. It's true that fees bring in money. But free entry would double attendance, so the museum should drop the fee.",
        chips=[
            ("assume", "Some say the museum should keep its entry fee.", "Opposing view",
             "Opposing view. The author mentions it to push back on it."),
            ("neutral", "It's true that fees bring in money.", "Concession",
             "Concession. The author grants a point, then pushes back."),
            ("describe", "Free entry would double attendance.", "Evidence",
             "Evidence. It's the reason the author gives for the conclusion."),
            ("object", "The museum should drop the fee.", "Conclusion",
             "Conclusion. It's where the argument ends, and the evidence is the reason to believe it."),
        ],
    )),
    ("drill", dict(
        h3="Name the method",
        hint="Is each one conditional, causal, comparative or something else?",
        passage=None,
        chips=[
            ("describe", "If the pool is open, the lifeguard is on duty.", "Conditional",
             "Conditional. It's an if/then rule."),
            ("assume", "Heavy traffic makes people late.", "Causal",
             "Causal. It says one thing produces another."),
            ("neutral", "Ana trains the way Maya does, and Maya ran a marathon. So Ana will run one too.", "Comparative",
             "Comparative. It says what happened to one case will happen to another."),
            ("describe", "Every student in the study group who practiced daily improved, so you will too.", "Generalization",
             "Generalization. It takes what happened to a group and applies it to you."),
            ("object", "People who study hard tend to score higher, so studying hard causes higher scores.", "Causal",
             "Causal. The evidence is only a correlation, so the conclusion breaks."),
        ],
    )),
    ("drill", dict(
        h3="Find the assumption",
        hint="Which one is the missing piece?",
        passage="Only members may use the pool. Lena is a member. So Lena can use the pool today.",
        chips=[
            ("neutral", "Lena can use the pool today.", "Conclusion",
             "Conclusion. It's where the argument ends."),
            ("describe", "Only members may use the pool.", "Evidence",
             "Evidence. It's stated, so it can't be the assumption."),
            ("object", "Being a member is enough to use the pool today.", "Assumption",
             "Assumption. Nobody said it, and the conclusion needs it. A requirement isn't a guarantee."),
            ("assume", "Lena is a member.", "Evidence",
             "Evidence. It's stated too."),
        ],
    )),
])

A6 = dict(kicker="On every argument", h2="The three steps, in order", blocks=[
    ("p", "Do this in the stimulus, before you read the answer choices."),
    ("screen", "Stimulus on the left. Choices on the right."),
    ("steps", [
        ("Mark the structure.", "Find the conclusion, then the evidence. Note any opposing viewpoint or concession."),
        ("Name the method.", "Conditional, causal, comparative or something else. Say it out loud: “This is a conditional.”"),
        ("Ask what's missing.", "With a conditional, is something required being treated as enough? With a cause, is the evidence only a correlation? "
                                "With a comparison, are the two cases alike where it matters?"),
    ]),
])

A_CLOSE = dict(h2="What to do next", steps=[
    ("Read the next note.", "It covers the last two points: keyword mapping, and putting abstract answer choices in plain English. "
                            "It's called Mapping Abstract Answers Back to the Argument."),
    ("Do Describing Arguments (set 1).", "Five questions on conclusions, evidence and the author's method. Read its instructions first. "
                                         "Start it before our follow-up, and try to finish it by Friday, November 20."),
    ("Wednesday, November 18, 7:30 PM.", "A short follow-up, about 30 to 40 minutes, to go over your practice."),
    ("Reading Comprehension gets its own session.", "You asked to work on it, and we'll do a full session. Parts of this routine carry over to it."),
    ("Send me a message on the platform if you have a question.", "I'll be able to get back to you."),
])


# ================================================================ Note 2: Mapping Abstract Answers Back to the Argument
B_HERO = (
    "The LSAT writes many answer choices abstractly. Say the same thing in plain English and it's usually easy to see. "
    "The last two points do that: put each abstract word in plain English, then find each keyword in the argument."
)
B_SLABS = ("A real match", "Where is it in the argument?", "What is it in plain English?")
B_LABELS = ("RESULT", "CHECK 2", "CHECK 1")

B1 = dict(kicker="Read it first", h2="Put the abstract word in plain English", blocks=[
    ("p", "When an answer choice sounds abstract, swap the abstract word for a plain one. Plain English and keyword mapping both work on the answer choices only. "
          "They don't apply to the stimulus."),
    ("ul", [
        ("Explanation.", "Means causation. What's explained is the effect. The explanation is the cause."),
        ("Illustration.", "Means example. A specific instance of a general idea."),
        ("Presupposes, assumes, supposes.", "Think assumption: something the author takes for granted and never says."),
        ("Justify.", "Think evidence or premise: the reason given for the conclusion."),
        ("Principle.", "A general rule that applies to many cases, not just one."),
    ]),
    ("said", ["“I always see them say justify, like all the time.”"],
     "Then justify goes on your list. You'll see the same words again and again."),
    ("callout", "Build your own list of these words",
     "Write each abstract word with its plain meaning beside it. Add to it every time you meet a new one.", False),
    ("callout", "An assumption is never stated",
     "On an assumption question, an answer that only repeats something the argument already says can't be the assumption. An assumption is a belief the author never says.", False),
])

B2 = dict(kicker="Keyword mapping", h2="Then find each keyword in the argument", blocks=[
    ("p", "Keyword mapping means taking the key words in an answer choice and finding them in the argument. "
          "When an answer describes the argument, as on flaw, method and role questions, and you can't find one, that part of the answer doesn't describe this argument. On strengthen, weaken and assumption questions, a right answer can add something new. Check each answer for these:"),
    ("steps", [
        ("Nouns.", "If the answer says “a certain property,” which property? Name it, then find it in the argument."),
        ("Adjectives.", "Does the adjective match what the argument actually says?"),
        ("What the author does.", "If the answer says the author claims something, does the author really claim it?"),
        ("A form of logic.", "If the answer mentions a conditional or a cause, the argument has to contain one. A correlation isn't a cause."),
        ("Abstract words.", "Put each in plain English before you look for the others, using your list."),
    ]),
    ("p", "Here's one in action."),
    ("argument", "A license is required to rent a car at this shop. Dev has a license.", "Dev can rent a car at this shop.", None, {"con_label": "Doesn't follow", "fall": True}),
    ("p", "Say one answer choice is: “It takes a condition that's necessary for an outcome to be sufficient for it.”"),
    ("steps", [
        ("Plain English.", "A requirement treated as if it were enough."),
        ("Find the nouns.", "The outcome is renting a car. The condition is having a license."),
        ("Check the form of logic.", "The argument is a conditional, so this answer is a contender."),
    ]),
    ("p", "Say another is: “It concludes that every member of a group has a trait because a few do.” There's no group and no sample here, "
          "so the nouns don't map. Not this one."),
    ("callout", "Naming the method narrows the choices",
     "That's why you name the method of reasoning first. If the argument is only about a cause, an answer about necessary and sufficient conditions has nothing to match.", False),
])

B3 = dict(kicker="Strong wording", h2="Strong words are harder for the argument to prove", blocks=[
    ("flags", ["most", "all", "every"]),
    ("p", "Most means more than half. All and every mean no exceptions. The more an answer claims, the more the argument has to prove. "
          "So slow down when you see these words. It's a reason to check carefully, not a reason to cut the answer."),
    ("ul", [
        ("Must Be True and Most Strongly Supported.", "Lean toward weaker answers. The stronger the claim, the less likely the argument guarantees it."),
        ("Necessary assumption.", "Lean weak. It's the least the argument needs."),
        ("Sufficient assumption.", "Strong wording is fine. It has to be enough."),
        ("Flaw and Method answers.", "The answer has to describe the argument accurately. If it says every society, the argument has to be about every society."),
    ]),
    ("p", "Weak wording still has to be relevant, and strong wording is sometimes required. Judge the idea, not only the word."),
])

B4 = dict(kicker="Try it", h2="Check yourself", blocks=[
    ("drill", dict(
        h3="Say it out loud, then tap to check",
        hint="What does each phrase say in plain English?",
        passage=None,
        chips=[
            ("describe", "The argument offers an explanation of the trend.", "Cause",
             "Cause. An explanation is a cause. The trend is the effect."),
            ("assume", "The author gives an illustration of the idea.", "Example",
             "Example. An illustration is a specific example of a general idea."),
            ("neutral", "The author presupposes that sales were steady.", "Assumption",
             "Assumption. It's something the author takes for granted and never says."),
            ("describe", "The author cites the survey to justify the claim.", "Evidence",
             "Evidence. The survey is the reason given for the claim."),
            ("assume", "The author appeals to a principle.", "General rule",
             "General rule. It applies to many cases, not just this one."),
        ],
    )),
    ("drill", dict(
        h3="Does the answer describe this argument?",
        hint="Find the answer's keywords in the passage.",
        passage="The café's sales rose after it changed its menu. So the new menu caused the rise.",
        chips=[
            ("describe", "It concludes that one thing caused another because the first came earlier.", "Matches",
             "Matches. There's a cause in the passage. The menu change is the cause and the rise in sales is the effect."),
            ("object", "It applies a rule about a group to one member of that group.", "Not this one",
             "Not this one. There's no group and no rule in the passage to find."),
            ("object", "It treats something required as if it were enough.", "Not this one",
             "Not this one. Nothing in the passage is required. There's no conditional to find."),
            ("object", "It rejects an opposing view without answering its evidence.", "Not this one",
             "Not this one. No one disagrees with the author here, so there's no opposing view to find."),
        ],
    )),
    ("drill", dict(
        h3="How much does each answer claim?",
        hint="Which one claims the least, and which claims the most?",
        passage=None,
        chips=[
            ("assume", "Most customers liked the new menu.", "Stronger",
             "Stronger. More than half have to have liked it."),
            ("object", "Every customer liked the new menu.", "Strongest",
             "Strongest. One customer who didn't like it makes it false."),
            ("describe", "Some customers liked the new menu.", "Weakest",
             "Weakest. One customer is enough to prove it."),
        ],
    )),
])

B5 = dict(kicker="On every question", h2="Before you commit to an answer", blocks=[
    ("screen", "Stimulus on the left. Choices on the right."),
    ("steps", [
        ("Run the three stimulus steps first.", "Structure, method of reasoning, assumption. They tell you what a good answer has to match."),
        ("Find the abstract words.", "Put each in plain English."),
        ("Map the keywords back.", "Nouns, adjectives, what the author does, the form of logic. On flaw, method and role questions, if you can't find one in the argument, that answer isn't describing it."),
        ("Watch for strong words.", "Most, all and every ask a lot. Check them carefully."),
    ]),
])

B_CLOSE = dict(h2="What to do next", steps=[
    ("Do the Abstract course.", "It's on your account now. Work through it in order, and read each note before its drill. "
                                "It's the practice for putting abstract answer choices in plain English."),
    ("Keep your list of abstract words.", "Add each new word with its plain meaning."),
    ("Wednesday, November 18, 7:30 PM.", "A short follow-up, about 30 to 40 minutes, to go over your practice."),
    ("Send me a message on the platform if you have a question.", "I'll be able to get back to you."),
])

NOTES = [
    dict(
        key="reading", lesson_id="yahunatan-2026-11-16-reading-an-argument", title="Reading an Argument in Three Steps",
        l1="Reading an Argument", l2="in Three Steps", hero=A_HERO, slabs=A_SLABS, labels=A_LABELS,
        sections=[A1, A2, A3, A4, A5, A6], close=A_CLOSE,
        html_name="recap.html", md_name="recap.fallback.md",
    ),
    dict(
        key="mapping", lesson_id="yahunatan-2026-11-16-mapping-abstract-answers", title="Mapping Abstract Answers Back to the Argument",
        l1="Mapping Abstract Answers", l2="Back to the Argument", hero=B_HERO, slabs=B_SLABS, labels=B_LABELS,
        sections=[B1, B2, B3, B4, B5], close=B_CLOSE,
        html_name="recap-mapping-abstract-answers.html", md_name="recap-mapping-abstract-answers.fallback.md",
    ),
]

# ---------------------------------------------------------------- lint and counts
import json as _json

BANNED = [  # wiki/COPY-CORRECTIONS.md rejected phrases, plus the recap builder's student-copy exclusions
    "manual", "recognition drill", "candidate assumption", "two complete conditions", "grammatical shape", "step zero", "the finalist",
    "concept lesson", "session manual", "establish", "preserve", "stipulated", "classify", "expression", "the other one", "makes a promise",
    "depends on", "nothing to stand on", "practise", "recall rephrase colour", "the model", "build the arrow", "door",
    "delve", "unlock", "seamless", "robust", "game-changer", "great question", "certainly", "dive deep", "supercharge", "elevate",
    "moreover", "furthermore", "additionally", "logic games", "the raffle", "patterns", "color-mix(", "~", chr(0x2014), chr(0x2013),
    "{{", "http://", "https://", "gemini", "transcript", "drill 1", "intro training", "ready to begin", "save and continue",
]
# "move" and "statement" were rejected as student words; check as whole words. "route" is avoided by choice.
BANNED_WORDS = ["move", "moves", "statement", "statements", "route", "card", "cards", "beat", "beats", "chunk", "intake", "briefing", "phase", "tab", "target", "relationship", "relationships"]


def visible_text(doc):
    t = re.sub(r"<(script|style)\b.*?</\1>", " ", doc, flags=re.S | re.I)
    t = re.sub(r"<head\b.*?</head>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return html.unescape(t)


def strict_count(doc):
    return len(re.findall(r"\S+", visible_text(doc)))


def lint(doc, md):
    text = visible_text(doc).lower()
    hits = []
    for phrase in BANNED:
        if phrase in text:
            hits.append(phrase)
    for w in BANNED_WORDS:
        if re.search(r"\b%s\b" % re.escape(w), text):
            hits.append("word:" + w)
    for ch in (chr(0x2014), chr(0x2013)):
        if ch in doc or ch in md:
            hits.append("dash in output")
    return sorted(set(hits))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for n in NOTES:
        doc = build(n)
        md = fallback_md(n)
        (OUT / n["html_name"]).write_text(doc, encoding="utf-8")
        (OUT / n["md_name"]).write_text(md, encoding="utf-8")
        print(n["html_name"], len(doc.encode("utf-8")), "bytes", strict_count(doc), "words (strict, hidden answers included)", "lint:", lint(doc, md) or "clean")
