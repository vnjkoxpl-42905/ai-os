"""Builds out/famous-flaws.html: the full Famous Flaws note, from the Lanae shell plus source data.

Standard library only. Run: py -I build-famous-flaws-full.py
Writes: out/flaws.data.json, out/adaptations.json, out/famous-flaws.html.
Inputs are read-only: sources/, shell/, out/svg/, out/extras.json, out/famous-flaws.layer.{css,js}.
Run make-svgs.py first if out/svg/ is missing.
"""
import html as H
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "out"
SEC = "§"  # the section sign used in the source

IDS = [
    "necessary-vs-sufficient", "causal", "part-vs-whole", "unproven-vs-proven-false", "ad-hominem", "sampling",
    "circular-reasoning", "internal-contradiction", "equivocation", "inappropriate-appeal",
    "sleight-of-hand", "sleazy-sales-pitch", "universal-desires", "value-assumptions", "secret-downsides",
]
NAME_CHECK = ["Necessary", "Causal", "Part vs", "Unproven", "Ad Hominem", "Sampling", "Circular", "Internal",
              "Equivocation", "Inappropriate", "Sleight", "Sleazy", "Universal", "Value", "Secret"]
GROUP_SHORT = {1: "Frequently the real flaw", 2: "Frequently the distractor", 3: "Named by me, super common"}
GROUP_CHIP = {1: "Group 1 · Real flaw", 2: "Group 2 · Distractor", 3: "Group 3 · Named by me"}

raw = (ROOT / "sources/05_compiled_content_voiced.md").read_text(encoding="utf-8")
ts = (ROOT / "sources/flaws.ts").read_text(encoding="utf-8")
shell = (ROOT / "shell/note-shell.html").read_text(encoding="utf-8")
extras = json.loads((OUT / "extras.json").read_text(encoding="utf-8"))
layer_css = (OUT / "famous-flaws.layer.css").read_text(encoding="utf-8")
layer_js = (OUT / "famous-flaws.layer.js").read_text(encoding="utf-8")

# ------------------------------------------------------------------ scope of the source
i_note2 = raw.index("## Note 2 · Famous Flaws Catalog")
i_mech = raw.index("## Invented · Answer Choice Disguise Library")
i_matrix = raw.index("## Invented · Flaw vs. Flaw Disambiguation Matrix")
i_end = raw.index("**END OF VOICE-LOCKED CONTENT**")
scope = raw[i_note2:i_end]

# ------------------------------------------------------------------ adaptations (closed table)
manifest = []


def adapt(text, rule, frm, to, flaw=""):
    assert text.count(frm) == 1, f"adaptation span not found exactly once: {frm[:60]!r}"
    manifest.append({"rule": rule, "flaw": flaw, "from": frm, "to": to})
    return text.replace(frm, to)


def slug_spans(text):
    out = []
    for m in re.finditer(r" · slug: `[a-z0-9-]+`", text):
        out.append(m.group(0))
    return out


for sp in slug_spans(scope):
    scope = adapt(scope, "R7", sp, "")
scope = adapt(scope, "R7", "Procedural-reference mode. Fifteen entries across three groups. Each entry is a quick-reference card built for a student stuck mid-drill who needs to look up a flaw fast. Modular subsections, dense bullets, voice still on.\n\n", "")
scope = adapt(scope, "R7", " The catalog lives next to the drills, not inside them.", "")
scope = adapt(scope, "R7", "**Cross-link.** The Causation module covers this in depth. The catalog entry is the Flaw-recognition surface only.\n\n", "", "causal")
stage3 = re.search(r"> \*\*Stage 3 implementation note:\*\*[^\n]*\n\n", scope).group(0)
scope = adapt(scope, "R7", stage3, "")
drill = re.search(r"### How to drill the matrix\n\n[^\n]*\n\n", scope).group(0)
scope = adapt(scope, "R7", drill, "")
scope = adapt(scope, "R1", "Joshua-Named, Super Common (5)", "Named by me, super common (5)")
scope = adapt(scope, "R2", "it's probably Trap Pattern 4 (Wrong Flaw).", "it's probably a wrong-flaw trap.")
scope = adapt(scope, "R2", f"(Trap 4 Wrong Flaw, Trap 5 Contradicted from {SEC} 5)", "(a wrong flaw, or one the stimulus contradicts)")
scope = adapt(scope, "R2", f"Wrong Flaw (Trap 4 from {SEC} 5) is the trap pattern that costs", "Choosing the wrong flaw is the trap that costs")
scope = adapt(scope, "R2", "The Master Guide teaches you the flaws.", "The list above teaches you the flaws.")
scope = adapt(scope, "R2", "The per-flaw disguise lists are embedded in each catalog entry above.", "The per-flaw disguise lists are in each flaw's panel above.")
scope = adapt(scope, "R3", "Dolores vs. Victor (PT 16.2.19).", "Dolores vs. Victor.", "sleazy-sales-pitch")
scope = adapt(scope, "R3", "The robot engineer (PT 16.2.10).", "The robot engineer.", "value-assumptions")
scope = adapt(scope, "R3", "The Ethicist meat argument (June 2007.3.21).", "The Ethicist meat argument.", "sleight-of-hand")
scope = adapt(scope, "R4", "Dr. Fauci, the government's leading expert in infectious diseases,", "The government's leading expert in infectious diseases", "inappropriate-appeal")
scope = adapt(scope, "R4", "Dr. Fauci must be wrong!", "The expert must be wrong!", "inappropriate-appeal")
scope = adapt(scope, "R4", "Billy says his uncle was related to Elvis,", "Billy says his uncle was related to a famous singer,", "unproven-vs-proven-false")
scope = adapt(scope, "R4", "Thus, Billy's uncle was not related to Elvis.", "Thus, Billy's uncle was not related to the singer.", "unproven-vs-proven-false")
assert "—" not in scope and "–" not in scope, "source scope contains a dash: add R5 entries"


# R6: the four Group 2 What-if slots come from flaws.ts
def ts_counter(fid):
    m = re.search(r"id:\s*'%s'.*?counterQuestion:\s*'((?:[^'\\]|\\.)*)'" % re.escape(fid), ts, flags=re.S)
    assert m, f"no counterQuestion for {fid}"
    return m.group(1).replace("\\'", "'")


R6 = {fid: ts_counter(fid) for fid in ("circular-reasoning", "internal-contradiction", "equivocation", "inappropriate-appeal")}
for fid, c in R6.items():
    manifest.append({"rule": "R6", "flaw": fid, "from": None, "to": c})

# ------------------------------------------------------------------ parse
lines = scope.split("\n")
LABELS = [
    ("definition", "Definition", r"\*\*Definition\.\*\*"),
    ("tells", "Stimulus tells", r"\*\*Stimulus tells\.\*\*"),
    ("disguises", "Answer-choice disguises", r"\*\*Answer-choice disguises\.\*\*"),
    ("example", "Canonical worked example", r"\*\*Canonical worked examples?\.\*\*"),
    ("whatif", 'The "What if" counter', r'\*\*The "What if" counter\.\*\*'),
    ("disamb", "Disambiguate from", r"\*\*Disambiguate from:\*\*"),
    ("right", "When it IS the right answer", r"\*\*When it IS the right answer\.\*\*"),
    ("pairs", "Real LSAT phrase pairs the test exploits", r"\*\*Real LSAT phrase pairs the test exploits:\*\*"),
]
LABEL_RE = [(k, n, re.compile("^" + pat + r"\s*(.*)$")) for k, n, pat in LABELS]

groups, entries = {}, []
cur_group = cur = None
i = 0
mech_start = next(k for k, l in enumerate(lines) if l.startswith("## Invented · Answer Choice"))
matrix_start = next(k for k, l in enumerate(lines) if l.startswith("## Invented · Flaw vs. Flaw"))
note_lines = lines[:mech_start]
for l in note_lines:
    m = re.match(r"### Group (\d) · (.*?) \((\d+)\)\s*$", l)
    if m:
        cur_group = int(m.group(1)); cur = None
        groups[cur_group] = {"n": cur_group, "title": m.group(2), "count": int(m.group(3)), "intro": []}
        continue
    m = re.match(r"#### (\d+) · (.*)$", l)
    if m:
        cur = {"num": int(m.group(1)), "name": m.group(2).strip(), "group": cur_group, "meta": None, "blocks": [], "_lines": []}
        entries.append(cur)
        continue
    if l.strip() == "---":
        cur = None if cur is not None and cur["meta"] else cur
        continue
    if cur is None:
        if cur_group and l.strip() and not l.startswith("#") and not l.startswith(">"):
            groups[cur_group]["intro"].append(l.strip())
        elif l.startswith("> **How to read this catalog:**"):
            groups.setdefault(0, {"howto": l[2:].strip()})
        continue
    cur["_lines"].append(l)

assert len(entries) == 15, len(entries)
for e, chk in zip(entries, NAME_CHECK):
    assert chk in e["name"], (e["name"], chk)

for e, fid in zip(entries, IDS):
    e["id"] = fid
    body = [l for l in e["_lines"]]
    while body and not body[0].strip():
        body.pop(0)
    meta = body.pop(0)
    mm = re.match(r"^\*\*(Group \d · .*)\*\*$", meta)
    assert mm, meta
    e["meta"] = mm.group(1)
    cur_b = None
    for l in body:
        hit = None
        for key, name, rx in LABEL_RE:
            mt = rx.match(l)
            if mt:
                tok = re.match(r"^\*\*(.+?)\*\*", l).group(1).rstrip(".:")
                hit = (key, tok, mt.group(1))  # keep the source's own label text (singular or plural)
                break
        if hit:
            cur_b = {"key": hit[0], "label": hit[1], "lines": []}
            if hit[2].strip():
                cur_b["lines"].append(hit[2])
            e["blocks"].append(cur_b)
        elif cur_b is not None:
            cur_b["lines"].append(l)
    for b in e["blocks"]:
        while b["lines"] and not b["lines"][-1].strip():
            b["lines"].pop()
    del e["_lines"]

# What-if for Group 2 from flaws.ts (rule R6)
for e in entries:
    if not any(b["key"] == "whatif" for b in e["blocks"]) and e["id"] in R6:
        pos = next(k for k, b in enumerate(e["blocks"]) if b["key"] == "example") + 1
        e["blocks"].insert(pos, {"key": "whatif", "label": 'The "What if" counter', "lines": [R6[e["id"]]], "supplement": "R6"})

# mechanics and matrix
mech_lines = lines[mech_start:matrix_start]
mech_intro, mechs, curm = [], [], None
for l in mech_lines[1:]:
    m = re.match(r"### Mechanic (\d+) · (.*)$", l)
    if m:
        curm = {"n": int(m.group(1)), "title": m.group(2).strip(), "lines": []}
        mechs.append(curm)
    elif l.strip() in ("---", ""):
        continue
    elif curm is None:
        mech_intro.append(l.strip())
    else:
        curm["lines"].append(l)
matrix_lines = lines[matrix_start:]
matrix_intro, rows = [], []
for l in matrix_lines[1:]:
    if l.startswith("| **"):
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        assert len(cells) == 3, l
        rows.append(cells)
    elif l.strip() and not l.startswith("|") and l.strip() != "---":
        matrix_intro.append(l.strip())

n_disg = sum(len([x for x in b["lines"] if x.startswith("- ")]) for e in entries for b in e["blocks"] if b["key"] == "disguises")
assert n_disg == 68, n_disg
assert len(rows) == 10 and len(mechs) == 5, (len(rows), len(mechs))
assert sum(1 for e in entries for b in e["blocks"] if b["key"] == "whatif" and not b.get("supplement")) == 11
assert sum(1 for e in entries for b in e["blocks"] if b["key"] == "disamb") == 9

# ------------------------------------------------------------------ rendering
def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def render_lines(ls):
    out, para, ul, bq = [], [], [], []

    def fp():
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para))); para.clear()

    def fu():
        if ul:
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in ul)); ul.clear()

    def fb():
        if bq:
            out.append("<blockquote><p>%s</p></blockquote>" % inline(" ".join(bq))); bq.clear()

    for l in ls:
        s = l.strip()
        if not s:
            fp(); fu(); fb(); continue
        if s.startswith("- "):
            fp(); fb(); ul.append(s[2:])
        elif s.startswith("> "):
            fp(); fu(); bq.append(s[2:])
        else:
            fu(); fb(); para.append(s)
    fp(); fu(); fb()
    return "".join(out)


def read_svg(name):
    return (OUT / "svg" / f"{name}.svg").read_text(encoding="utf-8")


def first_sentence(t):
    t = re.sub(r"\*+", "", t)
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    return m.group(1) if m else t


def freq_of(meta):
    m = re.search(r"requency: ([^·]+)", meta)
    return (m.group(1).strip() if m else "").upper()


def block(e, key):
    return next((b for b in e["blocks"] if b["key"] == key), None)


def render_panel(e):
    fid, g = e["id"], e["group"]
    short = re.sub(r"\s*\(a\.k\.a\..*\)$", "", e["name"])
    d = block(e, "definition")
    sentence = first_sentence(d["lines"][0]) if d else ""
    parts = ['<div class="fx-fig">%s</div>' % read_svg(fid)]
    parts.append('<div class="fx-part"><span class="fx-label">Frequency</span><p>%s</p></div>' % inline(e["meta"]))
    for b in e["blocks"]:
        cls = "fx-part"
        parts.append('<div class="%s"><span class="fx-label">%s</span>%s</div>' % (
            cls, H.escape(b["label"]),
            ('<div class="fx-ask">%s</div>' % inline(b["lines"][0])) if b["key"] == "whatif" else render_lines(b["lines"])))
    x = extras["say_first"][fid]
    parts.append(
        '<div class="fx-try"><span class="fx-new">New example</span><p class="st">%s</p>'
        '<button class="fx-btn fx-reveal" type="button" aria-expanded="false">Check my answer</button>'
        '<div class="rv"><strong>%s.</strong> %s</div></div>' % (H.escape(x["stimulus"]), H.escape(x["answer"]), H.escape(x["reason"])))
    parts.append('<div class="session-quote" data-slot="quote-%s" hidden></div>' % fid)
    return (
        '<article class="fx-panel" id="flaw-%s" data-g="%d">'
        '<button class="fx-head" type="button" aria-expanded="false" aria-controls="body-%s">'
        '<span class="tt"><span class="k">Group %d · %s</span><h3>%s</h3>'
        '<span class="session-slot fx-session" data-slot="session-%s"></span><span class="def">%s</span></span>'
        '<span class="chev" aria-hidden="true">▾</span></button>'
        '<div class="fx-body" id="body-%s" hidden>%s</div></article>'
        % (fid, g, fid, g, GROUP_SHORT[g], H.escape(e["name"]), fid, H.escape(sentence), fid, "".join(parts))
    ), short, sentence


def section(kicker, h2, inner, comment=""):
    return '%s<section><div class="wrap"><div class="sec-kicker">%s</div><h2>%s</h2>%s</div></section>' % (comment, kicker, h2, inner)


# ----- cards and panels
cards, panels_by_group = [], {1: [], 2: [], 3: []}
for e in entries:
    panel, short, sentence = render_panel(e)
    panels_by_group[e["group"]].append(panel)
    n = len([x for b in e["blocks"] if b["key"] == "disguises" for x in b["lines"] if x.startswith("- ")])
    fl = "RIGHT ANSWER · " if e["group"] == 2 else "FREQ · "
    cards.append(
        '<a class="fx-card" href="#flaw-%s" data-g="%d" data-target="flaw-%s"><span class="k">Group %d · %s</span><h3>%s</h3>'
        '<p>%s</p><span class="m"><span>%s%s</span><span>%d disguises</span></span></a>'
        % (e["id"], e["group"], e["id"], e["group"], GROUP_SHORT[e["group"]].split(",")[0], H.escape(short), H.escape(sentence), fl, H.escape(freq_of(e["meta"])), n))

group_html = ""
for gn in (1, 2, 3):
    gi = groups[gn]
    group_html += '<div class="fx-gh" data-g="%d"><h3>Group %d · %s (%d)</h3>%s</div>' % (
        gn, gn, H.escape(gi["title"]), gi["count"], "".join("<p>%s</p>" % inline(p) for p in gi["intro"]))
    group_html += "".join(panels_by_group[gn])

howto = groups[0]["howto"]
howto_tag = re.match(r"\*\*(.+?):\*\*\s*(.*)$", howto)

hero = (
    '<header class="hero solo"><div class="wrap"><div class="kicker"><!--SLOT:hero-kicker-->Famous Flaws</div>'
    "<h1>Famous Flaws</h1>"
    '<p class="lede">A flaw question asks what is wrong with an argument. The wrong answers are written to sound right, so you need to know the famous flaws well enough to name them before you read the choices. There are fifteen. This note takes each one apart: what it is, how it shows up in the stimulus, every way the answer choices disguise it, a worked example, and how to tell it from the flaws it gets confused with.</p>'
    "</div></header>"
)

counts = "".join(
    '<div class="fx-count" data-g="%d"><b>%d</b><span>%s</span><i>Group %d</i></div>' % (g, groups[g]["count"], H.escape(groups[g]["title"]), g)
    for g in (1, 2, 3))

s1 = section("How to use it", "Name the flaw, then find the choice",
             '<ol class="steps">'
             "<li><b>Find the conclusion and the evidence.</b> The conclusion is what the author wants you to accept. The evidence is the reason.</li>"
             "<li><b>Say what the author did, in your own words.</b> Do this before you read A.</li>"
             "<li><b>Find it in the list.</b> Each flaw below has a stimulus tell: the signal in the argument that gives it away.</li>"
             "<li><b>Then read the choices for the one that says it.</b> The choice will say it in abstract words. Every flaw lists the ways the LSAT disguises it.</li>"
             "</ol>"
             '<div class="callout"><span class="tag">%s</span> %s</div>' % (inline(howto_tag.group(1)), inline(howto_tag.group(2)))
             + '<div class="fx-counts">%s</div>' % counts)

s2 = section("The model", "Cake on blocks: where every flaw lives",
             "<p>Those blocks are your premises. The cake is your conclusion. A valid conclusion has to be true if its premises are true.</p>"
             "<p><strong>You don't argue with the blocks.</strong> The premises are given. <strong>You argue with whether the blocks actually hold up the cake.</strong> Validity lives in the connection between the premises and the conclusion. Not in any single premise. The space between them. That's where every flaw lives. That's where you go hunting.</p>"
             '<div class="fx-cake" data-g="1"><div class="state"><span class="state-now">STATE: VALID ARGUMENT</span><span>Specimen: validity, illustrated</span></div>'
             + read_svg("cake-on-blocks")
             + '<p class="out" aria-live="polite">Each premise is a block. If the blocks guarantee the conclusion, the cake stays up.</p>'
             '<div class="bar"><button id="fx-reset" class="fx-btn dark" type="button">Reset</button>'
             '<button id="fx-object" class="fx-btn pink" type="button">Object: &ldquo;What if&hellip;&rdquo;</button></div></div>'
             '<div class="callout"><span class="tag">Remember</span> Don\'t burn down your blocks. Argue with whether the blocks hold up the cake.</div>')

chips = (
    '<div class="fx-chips" role="group" aria-label="Filter the fifteen flaws"><span class="fx-lab">Filter</span>'
    '<button class="fx-chip" type="button" data-filter="all" aria-pressed="true"><span class="dot"></span>All 15</button>'
    + "".join('<button class="fx-chip" type="button" data-filter="%d" data-g="%d" aria-pressed="false"><span class="dot"></span>%s · %d</button>'
              % (g, g, GROUP_CHIP[g], groups[g]["count"]) for g in (1, 2, 3))
    + "</div>"
)
s3 = section("The list", "Fifteen flaws, three groups",
             "<p>Three colours, three groups, fifteen entries. Open any card to see the whole breakdown.</p>" + chips
             + '<div class="fx-grid">%s</div><p class="fx-new" id="fx-live" aria-live="polite">15 of 15 flaws shown</p>' % "".join(cards))

s4 = section("The breakdowns", "Every flaw, taken apart",
             '<p>Each panel gives the definition, the stimulus tells, every phrasing the answer choices use, a worked example, and the way to tell the flaw from the ones it gets confused with. Panels open and close, and nothing is left out.</p>'
             '<div class="fx-bar"><button class="fx-btn dark" id="fx-open-all" type="button">Open all</button><button class="fx-btn" id="fx-close-all" type="button">Close all</button></div>'
             + group_html)

mech_html = ""
for m in mechs:
    mech_html += '<div class="fx-mech"><span class="n">Mechanic %d</span><h3>%s</h3>%s</div>' % (m["n"], inline(m["title"]), render_lines(m["lines"]))
s5 = section("The disguises", "Five ways the answer choices disguise a flaw",
             "".join("<p>%s</p>" % inline(p) for p in mech_intro) + '<div class="fx-mechs">%s</div>' % mech_html,
             comment="<!-- Draft section: written in the earlier build, not in the owner's own words. Review before posting. -->")

matrix_rows = []
for idx, (pair, looks, how) in enumerate(rows):
    drill_ = extras["matrix_drills"][idx]
    mh = re.match(r"^(.*?)\s*\*\*(Ask: .*)\*\*\s*$", how)
    assert mh, how
    opts = list(drill_["options"])
    if idx % 2 == 1:
        opts.reverse()
    quiz = (
        '<div class="fx-quiz" data-right="%s"><span class="fx-new">New example</span><p class="st">%s</p><div class="fx-opts">%s</div>'
        '<p class="rv"><strong class="res"></strong>%s</p></div>'
        % (H.escape(drill_["right"]), H.escape(drill_["stimulus"]),
           "".join('<button class="fx-opt" type="button" data-label="%s">%s</button>' % (H.escape(o), H.escape(o)) for o in opts),
           H.escape(drill_["reason"])))
    matrix_rows.append("<tr><td data-label=\"Pair\">%s</td><td data-label=\"What looks similar\">%s</td><td data-label=\"How to tell them apart\">%s<div class=\"fx-ask\">%s</div>%s</td></tr>" % (
        inline(pair.strip("*")), inline(looks), inline(mh.group(1)), inline(mh.group(2)), quiz))
s6 = section("Flaw vs. flaw", "Ten pairs that get confused",
             "".join("<p>%s</p>" % inline(p) for p in matrix_intro)
             + '<div class="table-wrap fx-matrix"><table class="t"><thead><tr><th>Pair</th><th>What looks similar</th><th>How to tell them apart</th></tr></thead><tbody>%s</tbody></table></div>' % "".join(matrix_rows),
             comment="<!-- Draft section: the matrix was written in the earlier build, not in the owner's own words. Review before posting. -->")

s7 = section("Your work", "What to do next", '<ol class="steps todo"><li>SLOT:next-steps</li></ol>')

main_html = "<main>" + s1 + s2 + s3 + s4 + s5 + s6 + s7 + "</main>"

# ------------------------------------------------------------------ assemble from the shell
HERO_START = shell.index('<header class="hero">')
MAIN_END = shell.index("</main>") + len("</main>")
page = shell[:HERO_START] + hero + main_html + shell[MAIN_END:]
page = re.sub(r'(<meta name="lsatu-interactive-lesson" content=")[^"]*(">)', r"\g<1>famous-flaws-full\g<2>", page, count=1)
page = re.sub(r"<title>.*?</title>", "<title>Famous Flaws · Note</title>", page, count=1, flags=re.S)
i_style = page.index("</style>") + len("</style>")
page = page[:i_style] + "\n<style>\n" + layer_css + "\n</style>" + page[i_style:]
i_script = page.rindex("</script>") + len("</script>")
page = page[:i_script] + "\n<script>\n" + layer_js.replace(
    "$$('.fx-card, .fx-panel')", "$$('.fx-card, .fx-panel, .fx-gh')") + "\n</script>" + page[i_script:]
assert "{{" not in page

(OUT / "famous-flaws.html").write_text(page, encoding="utf-8", newline="\n")
(OUT / "adaptations.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
data = {"groups": {k: v for k, v in groups.items() if k}, "entries": entries, "mechanics": mechs, "matrix": rows}
(OUT / "flaws.data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
print("entries", len(entries), "disguises", n_disg, "matrix rows", len(rows), "mechanics", len(mechs),
      "adaptations", len(manifest), "bytes", len(page.encode("utf-8")))
