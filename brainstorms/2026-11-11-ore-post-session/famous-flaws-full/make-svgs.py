"""Writes out/svg/<flaw-id>.svg and out/svg/cake-on-blocks.svg (hand-drawn, inline-safe).

Every SVG has a <title> and <desc>, uses only classes defined in out/famous-flaws.layer.css,
and has ids prefixed with its flaw id so they stay unique when inlined into one page.
Run: py -I make-svgs.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "out" / "svg"
OUT.mkdir(parents=True, exist_ok=True)


def svg(fid, title, desc, body, vb="0 0 360 150"):
    return (
        f'<svg class="fx-svg" viewBox="{vb}" role="img" aria-labelledby="{fid}-t {fid}-d" xmlns="http://www.w3.org/2000/svg">'
        f'<title id="{fid}-t">{title}</title><desc id="{fid}-d">{desc}</desc>{body}</svg>'
    )


def arrow(x1, y1, x2, y2, cls="lg"):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    h = 9
    p1 = (x2 - h * math.cos(a - 0.45), y2 - h * math.sin(a - 0.45))
    p2 = (x2 - h * math.cos(a + 0.45), y2 - h * math.sin(a + 0.45))
    return (f'<path class="{cls}" d="M{x1} {y1}L{x2} {y2}"/>'
            f'<path class="{cls}" d="M{p1[0]:.1f} {p1[1]:.1f}L{x2} {y2}L{p2[0]:.1f} {p2[1]:.1f}"/>')


def cross(cx, cy, r=9):
    return f'<path class="lr" d="M{cx-r} {cy-r}L{cx+r} {cy+r}M{cx+r} {cy-r}L{cx-r} {cy+r}"/>'


def T(x, y, s, cls="t", anchor="middle"):
    return f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{s}</text>'


S = {}

S["necessary-vs-sufficient"] = svg(
    "necessary-vs-sufficient",
    "Enough sits inside required",
    "A small oval labelled enough, sufficient, sits inside a larger oval labelled required, necessary. A solid arrow goes from enough to required. A dashed arrow going back is crossed out.",
    '<ellipse class="fgt lg" cx="108" cy="82" rx="100" ry="58"/>'
    '<ellipse class="fg2 lg" cx="84" cy="84" rx="50" ry="34"/>'
    + T(84, 82, "Enough", "tb") + T(84, 97, "SUFFICIENT", "ts")
    + T(108, 22, "REQUIRED = NECESSARY", "ts")
    + arrow(222, 62, 330, 62) + T(276, 50, "enough, so required")
    + '<path class="ln dash" d="M330 108H232"/><path class="ln" d="M240 101L231 108L240 115"/>'
    + cross(281, 108) + T(281, 132, "required, so enough?") + T(281, 144, "does not follow", "ts"),
)

S["causal"] = svg(
    "causal",
    "Four stories fit the same fact",
    "At the top, two things A and B happen together. Below are four possible stories: A causes B, B causes A, a third factor C causes both, or it is coincidence.",
    '<circle class="fgt lg" cx="140" cy="26" r="16"/>' + T(140, 31, "A", "tb")
    + '<circle class="fgt lg" cx="220" cy="26" r="16"/>' + T(220, 31, "B", "tb")
    + '<path class="ln dash" d="M158 26H202"/>' + T(180, 55, "A and B go together", "ts")
    # story 1
    + '<g transform="translate(6 78)"><circle class="fg2 lg" cx="18" cy="20" r="12"/>' + T(18, 24, "A", "tb")
    + '<circle class="fg2 lg" cx="62" cy="20" r="12"/>' + T(62, 24, "B", "tb") + arrow(31, 20, 48, 20)
    + T(40, 52, "A causes B", "ts") + "</g>"
    # story 2
    + '<g transform="translate(96 78)"><circle class="fg2 lg" cx="18" cy="20" r="12"/>' + T(18, 24, "A", "tb")
    + '<circle class="fg2 lg" cx="62" cy="20" r="12"/>' + T(62, 24, "B", "tb") + arrow(49, 20, 32, 20)
    + T(40, 52, "B causes A", "ts") + "</g>"
    # story 3
    + '<g transform="translate(186 70)"><circle class="fgt lg" cx="40" cy="8" r="12"/>' + T(40, 12, "C", "tb")
    + '<circle class="fg2 lg" cx="12" cy="40" r="12"/>' + T(12, 44, "A", "tb")
    + '<circle class="fg2 lg" cx="68" cy="40" r="12"/>' + T(68, 44, "B", "tb")
    + arrow(34, 18, 19, 31) + arrow(46, 18, 61, 31) + T(40, 70, "C causes both", "ts") + "</g>"
    # story 4
    + '<g transform="translate(276 78)"><circle class="fg2 lg" cx="14" cy="20" r="12"/>' + T(14, 24, "A", "tb")
    + '<circle class="fg2 lg" cx="58" cy="20" r="12"/>' + T(58, 24, "B", "tb")
    + '<path class="ln dash" d="M27 20H45"/>' + T(36, 52, "chance", "ts") + "</g>",
)

S["part-vs-whole"] = svg(
    "part-vs-whole",
    "Parts and the whole they make",
    "On the left, three star parts. On the right, one large whole made from them. An arrow from the parts to the whole and an arrow from the whole to the parts are both marked with a question mark: a trait of one does not carry over to the other.",
    '<g>' + "".join(f'<circle class="fgt lg" cx="{x}" cy="{y}" r="17"/><path class="fg" d="M{x} {y-9}l2.6 5.6 6 .7-4.5 4.1 1.2 6-5.3-3-5.3 3 1.2-6-4.5-4.1 6-.7z"/>'
                     for x, y in ((46, 40), (96, 40), (71, 90)))
    + T(71, 126, "each part", "ts") + "</g>"
    + '<rect class="fgt lg" x="236" y="28" width="104" height="82" rx="20"/>' + T(288, 64, "the whole", "tb") + T(288, 80, "(the team)", "ts")
    + arrow(128, 50, 226, 50) + T(177, 42, "parts great, so whole great?", "ts")
    + arrow(226, 92, 128, 92, "lg") + T(177, 112, "whole great, so each part great?", "ts")
    + cross(177, 71, 8),
)

S["unproven-vs-proven-false"] = svg(
    "unproven-vs-proven-false",
    "A meter from shown false to shown true",
    "A horizontal bar has three zones: shown false, nothing shown, and shown true. A pointer sits in the middle zone, nothing shown. A dashed arrow jumping from nothing shown to shown false is crossed out.",
    '<rect class="fp" x="20" y="60" width="106" height="30" rx="8" style="fill:var(--strike);opacity:.22"/>'
    '<rect class="fp" x="126" y="60" width="108" height="30" rx="0" style="fill:var(--ink-mute);opacity:.2"/>'
    '<rect class="fp" x="234" y="60" width="106" height="30" rx="8" style="fill:var(--g);opacity:.25"/>'
    + T(73, 80, "SHOWN FALSE", "ts") + T(180, 80, "NOTHING SHOWN", "ts") + T(287, 80, "SHOWN TRUE", "ts")
    + '<path class="lg" d="M180 52V36"/><path class="fg" d="M172 52h16l-8 9z"/>' + T(180, 28, "no proof either way", "tb")
    + '<path class="ln dash" d="M170 106Q122 128 84 106"/><path class="ln" d="M92 100L83 106L94 111"/>' + cross(127, 122) + T(180, 144, "failing to prove is not proving the opposite", "ts"),
)

S["ad-hominem"] = svg(
    "ad-hominem",
    "Aim at the claim, not the speaker",
    "A speaker figure on the left and a speech bubble holding the claim on the right. A red arrow hits the speaker, marked wrong target. A green arrow points at the claim, marked right target.",
    '<circle class="fgt lg" cx="62" cy="52" r="18"/><path class="fgt lg" d="M30 120a32 30 0 0 1 64 0z"/>' + T(62, 140, "the speaker", "ts")
    + '<rect class="fp ln" x="196" y="30" width="144" height="64" rx="14"/><path class="fp ln" d="M214 94l-8 16 24-16"/>'
    + T(268, 58, "the claim", "tb") + T(268, 74, "and its evidence", "ts")
    + arrow(172, 40, 100, 66, "lr") + T(140, 30, "WRONG TARGET", "ts")
    + arrow(172, 112, 214, 84) + T(190, 132, "RIGHT TARGET", "ts"),
)

dots = [(40 + 24 * i + (10 if j % 2 else 0), 34 + 22 * j) for j in range(5) for i in range(7)]
S["sampling"] = svg(
    "sampling",
    "A small clustered sample standing for a whole population",
    "A large field of dots represents the population. A small group of highlighted dots in one corner is the sample. An arrow from the sample to the label everyone is marked as a mismatch.",
    '<rect class="fgt ln" x="14" y="14" width="214" height="124" rx="16"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="4.2" class="{"fg" if (x < 86 and y < 70) else "dotm"}"/>' for x, y in dots)
    + '<rect class="lg dash" x="26" y="22" width="68" height="54" rx="10"/>' + T(60, 94, "the sample", "ts")
    + T(121, 132, "the population", "ts")
    + arrow(236, 76, 300, 76) + T(318, 70, "everyone", "tb") + T(318, 84, "?", "tb") + cross(268, 76, 8),
)

S["circular-reasoning"] = svg(
    "circular-reasoning",
    "The conclusion holds up its own premise",
    "Two boxes, premise and conclusion, joined by two arrows that form a loop: the premise supports the conclusion and the conclusion supports the premise.",
    '<rect class="fgt lg" x="30" y="56" width="110" height="38" rx="10"/>' + T(85, 79, "premise", "tb")
    + '<rect class="fgt lg" x="220" y="56" width="110" height="38" rx="10"/>' + T(275, 79, "conclusion", "tb")
    + '<path class="lg" d="M140 66Q180 36 214 62"/><path class="lg" d="M204 54L215 62L203 68"/>'
    + '<path class="lg" d="M220 88Q180 118 146 90"/><path class="lg" d="M157 82L145 89L158 95"/>'
    + T(180, 26, "says the same thing twice", "ts") + T(180, 138, "no new support", "ts"),
)

S["internal-contradiction"] = svg(
    "internal-contradiction",
    "Two claims that cannot both be true",
    "Two claim boxes side by side joined by a bar with a not equal sign and the words cannot both be true.",
    '<rect class="fgt lg" x="20" y="46" width="116" height="52" rx="12"/>' + T(78, 69, "Claim 1", "tb") + T(78, 85, "the author says", "ts")
    + '<rect class="fgt lg" x="224" y="46" width="116" height="52" rx="12"/>' + T(302, 69, "Claim 2", "tb") + T(302, 85, "also says", "ts")
    + '<path class="lr" d="M144 72H216"/><circle class="fp lr" cx="180" cy="72" r="14"/>'
    + '<path class="lr" d="M173 66h14M173 78h14M175 82l10-20"/>' + T(180, 118, "CANNOT BOTH BE TRUE", "ts"),
)

S["equivocation"] = svg(
    "equivocation",
    "One word, two meanings",
    "The word sanctions in the centre splits into two paths: one meaning, approves, is the sense used in the conclusion and the other meaning, penalizes, is the sense used in the premise.",
    '<rect class="fgt lg" x="130" y="14" width="100" height="34" rx="17"/>' + T(180, 36, "sanctions", "tb")
    + arrow(160, 50, 80, 92) + arrow(200, 50, 280, 92)
    + '<rect class="fp ln" x="22" y="94" width="116" height="36" rx="10"/>' + T(80, 112, "approves", "tb") + T(80, 124, "conclusion's meaning", "ts")
    + '<rect class="fp ln" x="222" y="94" width="116" height="36" rx="10"/>' + T(280, 112, "penalizes", "tb") + T(280, 124, "premise's meaning", "ts")
    + '<path class="lr dash" d="M144 112H216"/>' + T(180, 108, "swapped", "ts"),
)

S["inappropriate-appeal"] = svg(
    "inappropriate-appeal",
    "An authority badge that does not match the topic",
    "A badge with a star labelled famous, popular or pitiable on the left, a card on the right labelled the topic at hand, and a mismatch mark between them.",
    '<circle class="fgt lg" cx="70" cy="64" r="34"/><path class="fg" d="M70 40l7 15 16 2-12 11 3.5 16L70 76l-14.5 8L59 68 47 57l16-2z"/>'
    + T(70, 114, "famous, popular,", "ts") + T(70, 127, "or pitiable", "ts")
    + '<rect class="fp ln" x="214" y="34" width="130" height="62" rx="12"/>' + T(279, 62, "the topic at hand", "tb") + T(279, 78, "needs expertise on it", "ts")
    + '<path class="lr dash" d="M112 64H206"/>' + cross(159, 64, 9) + T(159, 100, "not an expert here", "ts"),
)

S["sleight-of-hand"] = svg(
    "sleight-of-hand",
    "Two different terms treated as the same",
    "A box holding the term used in the evidence and a box holding a different term used in the conclusion with a large not-equal sign between them.",
    '<rect class="fgt lg" x="18" y="44" width="124" height="56" rx="12"/>' + T(80, 66, "term in the", "ts") + T(80, 84, "evidence", "tb")
    + '<rect class="fgt lg" x="218" y="44" width="124" height="56" rx="12"/>' + T(280, 66, "new term in the", "ts") + T(280, 84, "conclusion", "tb")
    + '<text x="180" y="86" text-anchor="middle" style="font:700 44px var(--serif);fill:var(--strike)">&#8800;</text>'
    + T(180, 128, "nothing is basically the same", "ts"),
)

S["sleazy-sales-pitch"] = svg(
    "sleazy-sales-pitch",
    "A one-sided comparison",
    "A balance scale. The left pan shows the strengths of option A and the right pan shows the weaknesses of option B. Two dashed pans below are hidden: the weaknesses of A and the strengths of B.",
    '<path class="ln" d="M180 20V84M120 84h120"/><path class="ln" d="M70 34H290"/>'
    '<path class="ln" d="M70 34L46 70M70 34L94 70M290 34L266 70M290 34L314 70"/>'
    '<path class="fgt lg" d="M36 70h68l-8 18H44z"/><path class="fgt lg" d="M256 70h68l-8 18H264z"/>'
    + T(70, 112, "A: strengths shown", "t") + T(290, 112, "B: weaknesses shown", "t")
    + '<rect class="ln dash" x="26" y="118" width="108" height="24" rx="8"/>' + T(80, 134, "A's weaknesses ?", "ts")
    + '<rect class="ln dash" x="226" y="118" width="108" height="24" rx="8"/>' + T(280, 134, "B's strengths ?", "ts"),
)

crowd = []
for r in range(2):
    for c in range(8):
        crowd.append((52 + c * 36, 44 + r * 40, not (r == 1 and c in (2, 6))))
S["universal-desires"] = svg(
    "universal-desires",
    "Not everyone wants the goal",
    "A crowd of sixteen people. Fourteen are filled in as wanting the goal and two are outlined with a no-thanks label. The argument counts all sixteen as wanting it.",
    "".join(f'<circle cx="{x}" cy="{y}" r="12" class="{"fg" if on else "fp lr"}"/>' for x, y, on in crowd)
    + T(160, 130, "no thanks", "ts") + T(268, 130, "no thanks", "ts")
    + T(180, 18, "the argument counts everyone as wanting it", "ts"),
)

S["value-assumptions"] = svg(
    "value-assumptions",
    "A fact jumping across a gap to a loaded word",
    "A fact box on the left, a dashed gap in the middle, and a loaded judgment word on the right in a pink box. An arrow jumps over the gap.",
    '<rect class="fgt lg" x="14" y="46" width="108" height="54" rx="12"/>' + T(68, 68, "the fact", "ts") + T(68, 86, "50 mpg", "tb")
    + '<path class="ln dash" d="M148 100V50M212 100V50"/>' + T(180, 124, "gap the premises never cross", "ts")
    + '<path class="lg" d="M122 62Q180 14 240 62"/><path class="lg" d="M229 55L240 62L227 67"/>'
    + '<rect class="pinkbox" x="238" y="46" width="108" height="54" rx="12"/>' + T(292, 68, "the verdict", "ts") + T(292, 86, "&#8220;best&#8221;", "tb"),
)

S["secret-downsides"] = svg(
    "secret-downsides",
    "The visible benefit above the waterline and the hidden cost below",
    "A wavy waterline. Above it a small tip labelled benefit shown. Below it a much larger mass labelled cost never mentioned.",
    '<path class="fgt lg" d="M150 66L180 20L210 66z"/>' + T(180, 44, "benefit", "ts") + T(280, 40, "what the argument shows", "ts", "middle")
    + '<path class="ln" d="M20 66Q50 56 80 66T140 66T200 66T260 66T340 66"/>'
    + '<path class="pinkbox lg" d="M120 70L240 70L226 120L180 140L134 120z" style="opacity:.8"/>' + T(180, 100, "cost", "tb") + T(180, 114, "never mentioned", "ts")
    + T(60, 100, "below the line", "ts") + T(298, 96, "the argument", "ts") + T(298, 110, "never looks here", "ts"),
)

# Cake-on-Blocks, the validity model. Groups carry ids used by the layer script.
S["cake-on-blocks"] = svg(
    "cake",
    "The Cake-on-Blocks model of a valid argument",
    "Four premise blocks hold up a plank and the cake of the conclusion sits on the plank. When the Object button is pressed the right-hand blocks slide away, the plank tips and the cake falls.",
    '<path class="ln" d="M20 132H340"/>'
    '<g id="cake-left"><rect class="blk" x="64" y="104" width="44" height="28" rx="3"/>' + T(86, 123, "P1", "blkt") +
    '<rect class="blk" x="68" y="78" width="36" height="26" rx="3"/>' + T(86, 96, "P2", "blkt") + "</g>"
    '<g id="cake-right"><rect class="blk" x="252" y="104" width="44" height="28" rx="3"/>' + T(274, 123, "P3", "blkt") +
    '<rect class="blk" x="256" y="78" width="36" height="26" rx="3"/>' + T(274, 96, "P4", "blkt") + "</g>"
    '<g id="cake-plank"><rect class="plank" x="52" y="68" width="256" height="10" rx="2"/>'
    '<g id="cake-top"><path class="cakebody" d="M146 68V46q17-8 34 0t34 0V68z"/><rect class="cakeband" x="146" y="54" width="68" height="14"/>'
    '<rect class="candle" x="178" y="30" width="4" height="12"/><path class="flame" d="M180 24q-3 4 0 7q3-3 0-7z"/>'
    + T(180, 65, "CONCLUSION", "cktext") + "</g></g>"
    + T(180, 148, "FLOOR: where an objection lives", "ts"),
    vb="0 0 360 160",
)

for name, body in S.items():
    (OUT / f"{name}.svg").write_text(body, encoding="utf-8", newline="\n")
print("wrote", len(S), "svgs:", ", ".join(sorted(S)))
