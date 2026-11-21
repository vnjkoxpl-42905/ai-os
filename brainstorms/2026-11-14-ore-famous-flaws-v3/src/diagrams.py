# Ten inline SVG diagrams, one per flaw. viewBox width 360; colours are the note's tokens.
INK, SOFT, MUTE = "#1F1C19", "#4A453F", "#766F66"
CARD, WELL, LINE, EDGE = "#FDFBF6", "#EFE8D9", "#DCD2BF", "#CFC3AB"
BRASS, BRT = "#B8983F", "#7A5C10"
GREEN, RED = "#3F6212", "#9F1239"
GW, RW, BW = "#E6EAD6", "#F4E1E3", "#F2E8CD"
SANS = "Outfit,Segoe UI,sans-serif"
SERIF = "Fraunces,Georgia,serif"
MONO = "JetBrains Mono,Consolas,monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(id_, h, title, desc, body):
    return (f'<svg class="dg-svg" viewBox="0 0 360 {h}" role="img" aria-labelledby="{id_}-t {id_}-d" xmlns="http://www.w3.org/2000/svg">'
            f'<title id="{id_}-t">{esc(title)}</title><desc id="{id_}-d">{esc(desc)}</desc>'
            f'<defs><marker id="{id_}-a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="{INK}"/></marker>'
            f'<marker id="{id_}-r" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="{RED}"/></marker>'
            f'<marker id="{id_}-g" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 10 5 0 10z" fill="{GREEN}"/></marker></defs>'
            f'{body}</svg>')


def box(x, y, w, h, lines, fill=CARD, stroke=EDGE, color=INK, size=12.5, font=SANS, weight=500, r=10, sw=1.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    n = len(lines)
    lh = size * 1.25
    y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.36
    for i, t in enumerate(lines):
        out += f'<text x="{x + w / 2}" y="{y0 + i * lh:.1f}" text-anchor="middle" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}">{esc(t)}</text>'
    return out


def label(x, y, t, color=BRT, size=10.5, anchor="start", font=MONO, ls=".12em", weight=500):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-size="{size}" font-weight="{weight}" letter-spacing="{ls}" fill="{color}">{esc(t)}</text>'


def text(x, y, t, color=SOFT, size=12, anchor="start", font=SANS, weight=400, italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}"{st}>{esc(t)}</text>'


def arrow(x1, y1, x2, y2, id_, kind="a", color=INK, sw=1.8, dash=None, curve=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    if curve:
        cx, cy = curve
        return f'<path d="M{x1} {y1} Q{cx} {cy} {x2} {y2}" fill="none" stroke="{color}" stroke-width="{sw}"{d} marker-end="url(#{id_}-{kind})"/>'
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d} marker-end="url(#{id_}-{kind})"/>'


def nec():
    i = "dg-nec"
    b = '<rect x="0" y="0" width="360" height="85" rx="12" fill="#e9eddf"/>'
    b += label(16, 22, "THE RULE", GREEN, 10)
    b += text(16, 49, "Saw the film", INK, 16, weight=600)
    b += arrow(123, 44, 178, 44, i, "g", GREEN)
    b += text(194, 49, "Understands the system", INK, 14, weight=600)
    b += text(16, 70, "Seeing the film is enough to understand the system.", SOFT, 13)

    rows = [
        (113, "JANE: REVERSAL", "Understands the system", "Must have seen the film",
         "Jane could have learned it another way."),
        (192, "MEGAN: NEGATION", "Hasn't seen the film", "Must not understand it",
         "Megan could have learned it another way."),
    ]
    for y, name, fact, claim, reason in rows:
        b += label(16, y, name, RED, 10)
        b += text(16, y + 23, fact, INK, 13.5, weight=500)
        b += text(180, y + 23, "⇏", RED, 19, "middle", font="Segoe UI Symbol,sans-serif")
        b += text(194, y + 23, claim, INK, 13.5, weight=500)
        b += text(16, y + 44, reason, SOFT, 13)
    b += f'<path d="M16 170H344" stroke="{LINE}"/>'

    return svg(i, 246, "Necessary vs. Sufficient",
               "Seeing the film guarantees understanding the system. Jane's understanding does not prove she saw the film. Megan's not seeing it does not prove she lacks understanding. Both could have learned it another way.", b)


def causal():
    i = "dg-cau"
    b = label(180, 20, "THE FACT", BRT, anchor="middle")
    b += box(70, 28, 92, 36, ["Enlisted"], fill=BW, stroke=BRASS)
    b += box(198, 28, 92, 36, ["Very fit"], fill=BW, stroke=BRASS)
    b += f'<line x1="162" y1="46" x2="198" y2="46" stroke="{BRASS}" stroke-width="2" stroke-dasharray="3 3"/>'
    b += text(180, 82, "These go together. Why?", MUTE, 12, "middle", italic=True)
    cols = [(10, "AUTHOR'S PICK", ["Fit people", "get picked"], INK, BW, BRASS),
            (126, "REVERSED", ["Training", "makes people fit"], SOFT, CARD, EDGE),
            (242, "THIRD CAUSE", ["Love of sport", "drives both"], SOFT, CARD, EDGE)]
    for x, lab, lines, c, f, s in cols:
        b += arrow(180, 92, x + 54, 120, i, "a", MUTE, 1.3)
        b += box(x, 124, 108, 52, lines, fill=f, stroke=s, color=c, size=12)
        b += label(x + 54, 194, lab, BRT if x == 10 else MUTE, 10, "middle")
    b += text(180, 216, "Three stories fit the same fact. The author picks one.", SOFT, 12, "middle", weight=500)
    return svg(i, 228, "Causal",
               "One fact, enlisted people are fit, has three explanations: recruiters pick fit people, training makes people fit, or love of sport drives both. The author chooses one and ignores the rest.", b)


def part():
    i = "dg-part"
    b = label(16, 20, "THE PARTS", BRT)
    parts = [("Military", "honor", True), ("Courts", "?", False), ("Agencies", "?", False), ("Congress", "?", False)]
    for k, (n, t, on) in enumerate(parts):
        x = 16 + k * 84
        b += box(x, 30, 76, 52, [n, t], fill=GW if on else CARD, stroke=GREEN if on else EDGE, color=INK if on else MUTE, size=12)
    b += f'<path d="M16 92 L16 100 L328 100 L328 92" fill="none" stroke="{EDGE}" stroke-width="1.5"/>'
    b += arrow(172, 102, 172, 128, i, "r", RED, 2)
    b += box(60, 132, 240, 46, ["Government as a whole: honor?"], fill=RW, stroke=RED, color=INK, size=13, font=SERIF, weight=600)
    b += text(180, 202, "One part's trait does not carry up to the whole.", SOFT, 12, "middle", weight=500)
    b += text(180, 220, "Or down: a harmful mix can hold harmless parts.", MUTE, 12, "middle", italic=True)
    return svg(i, 232, "Part vs. Whole",
               "Four parts of government: only the military is marked with honor; the others are question marks. An arrow up to the whole government asks whether it has honor too. A trait of one part does not carry to the whole, and a trait of the whole does not carry down to each part.", b)


def unproven():
    i = "dg-unp"
    b = f'<rect x="16" y="50" width="328" height="34" rx="17" fill="{WELL}" stroke="{EDGE}" stroke-width="1.5"/>'
    b += f'<rect x="16" y="50" width="96" height="34" rx="17" fill="{GW}" stroke="{GREEN}" stroke-width="1.5"/>'
    b += f'<rect x="248" y="50" width="96" height="34" rx="17" fill="{RW}" stroke="{RED}" stroke-width="1.5"/>'
    b += text(64, 72, "Shown true", GREEN, 12, "middle", weight=600)
    b += text(180, 72, "Not shown either way", SOFT, 12, "middle", weight=500)
    b += text(296, 72, "Shown false", RED, 12, "middle", weight=600)
    b += f'<circle cx="180" cy="104" r="6" fill="{INK}"/>'
    b += text(180, 128, "Billy's evidence lands here", INK, 12, "middle", weight=500)
    b += arrow(186, 44, 290, 44, i, "r", RED, 2.2, dash="5 4", curve=(238, 4))
    b += label(238, 20, "THE LEAP", RED, 9.5, "middle")
    b += text(180, 160, "Missing proof leaves the question open.", SOFT, 12, "middle", weight=500)
    b += text(180, 178, "It doesn't settle it as false.", MUTE, 12, "middle", italic=True)
    return svg(i, 190, "Unproven vs. Proven False",
               "A three-zone meter: shown true, not shown either way, shown false. Billy's evidence sits in the middle zone. A red dashed arrow leaps from the middle to shown false: that leap is the flaw.", b)


def adhom():
    i = "dg-adh"
    b = label(96, 20, "THE PERSON", RED, anchor="middle")
    b += label(264, 20, "THE CLAIM", GREEN, anchor="middle")
    b += f'<circle cx="96" cy="78" r="46" fill="{RW}" stroke="{RED}" stroke-width="1.8"/>'
    b += text(96, 74, "Sameer,", INK, 12.5, "middle", weight=600)
    b += text(96, 90, "a social worker", SOFT, 12, "middle")
    b += f'<circle cx="264" cy="78" r="46" fill="{CARD}" stroke="{GREEN}" stroke-width="1.8" stroke-dasharray="5 4"/>'
    b += text(264, 70, "Social workers", INK, 12, "middle", weight=600)
    b += text(264, 85, "handle these calls", INK, 12, "middle", weight=600)
    b += text(264, 100, "better", INK, 12, "middle", weight=600)
    b += box(118, 150, 124, 34, ["The argument"], fill=WELL, stroke=EDGE, size=12)
    b += arrow(140, 150, 112, 128, i, "r", RED, 2.2)
    b += text(264, 146, "never examined", GREEN, 11, "middle", italic=True)
    b += text(180, 208, "The attack hits the speaker. The claim is left untouched.", SOFT, 12, "middle", weight=500)
    return svg(i, 220, "Ad Hominem",
               "Two targets: the person, Sameer, and the claim, that social workers handle these calls better. The argument's arrow hits the person. The claim is never examined.", b)


def sampling():
    i = "dg-sam"
    import random
    rnd = random.Random(7)
    b = f'<rect x="12" y="28" width="336" height="128" rx="14" fill="{CARD}" stroke="{EDGE}" stroke-width="1.5"/>'
    b += label(24, 20, "ALL YOUNG PEOPLE", BRT)
    pts = []
    for r in range(6):
        for c in range(16):
            x = 30 + c * 20 + rnd.uniform(-3, 3)
            y = 46 + r * 19 + rnd.uniform(-3, 3)
            if 236 < x < 318 and 70 < y < 136:
                continue
            col = BRASS if rnd.random() < 0.3 else MUTE
            pts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{col}" opacity=".85"/>')
    for k in range(9):
        x = 252 + (k % 3) * 20 + rnd.uniform(-2, 2)
        y = 84 + (k // 3) * 18 + rnd.uniform(-2, 2)
        pts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{BRASS}"/>')
    b += "".join(pts)
    b += f'<circle cx="272" cy="102" r="40" fill="none" stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>'
    b += label(272, 172, "THE COMIC-CON SAMPLE", RED, 10, "middle")
    b += text(24, 178, "Gold = loves comics", BRT, 11, weight=500)
    b += text(180, 204, "The sample is all gold. The group isn't.", SOFT, 12, "middle", weight=500)
    return svg(i, 214, "Sampling",
               "A field of dots stands for all young people, with only some gold dots for comic fans. A small circled cluster, the Comic-Con sample, is entirely gold. The sample does not look like the group.", b)


def appeal():
    i = "dg-app"
    rows = [("Sympathy", "“it would ruin my anniversary”"), ("An unjustified pick", "“my neighbor says so”"), ("Popularity", "“the book sells well”")]
    b = label(16, 20, "WHAT IS OFFERED", BRT)
    b += label(344, 20, "WHAT IT NEEDS TO SUPPORT", BRT, anchor="end")
    for k, (n, q) in enumerate(rows):
        y = 32 + k * 56
        b += box(16, y, 150, 44, [n, q], fill=BW, stroke=BRASS, size=11.5)
        b += f'<line x1="170" y1="{y + 22}" x2="206" y2="{y + 22}" stroke="{MUTE}" stroke-width="1.8" stroke-dasharray="3 3"/>'
        b += f'<path d="M210 {y + 14} l6 16 M218 {y + 14} l6 16" stroke="{RED}" stroke-width="2" stroke-linecap="round"/>'
    b += box(236, 52, 108, 104, ["The claim", "is true"], fill=CARD, stroke=INK, size=13.5, font=SERIF, weight=600)
    b += text(180, 214, "None of these is evidence the claim is true.", SOFT, 12, "middle", weight=500)
    return svg(i, 226, "Inappropriate Appeal",
               "Three things offered as support, sympathy, an unjustified pick of one source, and popularity, each connect to the claim through a broken line. None is evidence the claim is true.", b)


def circular():
    i = "dg-cir"
    b = box(20, 30, 140, 74, ["Premise:", "the other tests pale", "next to the LSAT"], fill=GW, stroke=GREEN, size=12)
    b += box(200, 30, 140, 74, ["Conclusion:", "the LSAT is", "the hardest test"], fill=BW, stroke=BRASS, size=12)
    b += arrow(160, 48, 198, 48, i, "a", INK, 2)
    b += arrow(220, 110, 140, 110, i, "a", INK, 2, curve=(180, 150))
    b += f'<circle cx="180" cy="80" r="13" fill="{RW}" stroke="{RED}" stroke-width="1.6"/>'
    b += text(180, 85, "=", RED, 16, "middle", weight=700)
    b += text(180, 168, "Same claim, two wordings. Nothing new goes in.", SOFT, 12, "middle", weight=500)
    return svg(i, 180, "Circular Reasoning",
               "The premise card and the conclusion card say the same thing in different words, joined by an equals sign, with arrows running in a loop between them.", b)


def contradiction():
    i = "dg-con"
    b = label(16, 20, "THE SAME AUTHOR SAYS", BRT)
    b += box(16, 30, 150, 62, ["“No valid inferences", "can be drawn”"], fill=CARD, stroke=INK, size=12)
    b += box(194, 30, 150, 62, ["“This proves the", "ban worked”"], fill=CARD, stroke=INK, size=12)
    b += f'<rect x="90" y="108" width="180" height="30" rx="8" fill="{RED}"/>'
    b += text(180, 128, "Can't both be true", "#FDFBF6", 12.5, "middle", weight=600)
    b += f'<line x1="91" y1="92" x2="120" y2="108" stroke="{RED}" stroke-width="2"/><line x1="269" y1="92" x2="240" y2="108" stroke="{RED}" stroke-width="2"/>'
    b += text(180, 166, "One claim knocks out the other.", SOFT, 12, "middle", weight=500)
    return svg(i, 178, "Internal Contradiction",
               "From the real question below: the author says no valid inferences can be drawn from a study, then says the study proves the ban worked. A red bar joins them: can't both be true.", b)


def equiv():
    i = "dg-equ"
    b = box(130, 22, 100, 40, ["sanction"], fill=CARD, stroke=INK, size=17, font=SERIF, weight=600)
    b += arrow(160, 64, 92, 104, i, "a", INK, 1.8)
    b += arrow(200, 64, 268, 104, i, "a", INK, 1.8)
    b += box(16, 108, 152, 50, ["meaning 1: approve"], fill=BW, stroke=BRASS, size=12.5)
    b += box(192, 108, 152, 50, ["meaning 2: a penalty"], fill=GW, stroke=GREEN, size=12.5)
    b += label(92, 176, "USED IN THE CONCLUSION", BRT, 10, "middle")
    b += label(268, 176, "USED IN THE EVIDENCE", GREEN, 10, "middle")
    b += text(180, 204, "The word stays the same. The meaning switches.", SOFT, 12, "middle", weight=500)
    return svg(i, 216, "Equivocation",
               "The word sanction forks into two meanings: approve, used in the conclusion, and a penalty, used in the evidence. The argument switches meanings midway.", b)


DIAGRAMS = {"nec": nec, "causal": causal, "part": part, "unproven": unproven, "adhom": adhom,
            "sampling": sampling, "appeal": appeal, "circular": circular, "contradiction": contradiction, "equiv": equiv}
