from pathlib import Path

ROOT = Path(__file__).resolve().parent
INK = "#173047"
MUTED = "#526679"
PAPER = "#f7f6f1"
TEAL = "#087e83"
LIGHT = "#d8e4e6"
PURPLE = "#7356a8"
GOLD = "#c18124"


def start(title: str, desc: str, height: int) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{title}</title><desc id="desc">{desc}</desc>',
        f'<rect width="920" height="{height}" rx="22" fill="{PAPER}"/>',
        f'<text x="38" y="48" fill="{INK}" font-family="Arial,sans-serif" font-size="27" font-weight="700">{title}</text>',
    ]


def label(x: int, y: int, value: str, size: int = 18, color: str = INK, weight: int = 400) -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}">{value}</text>'


def book(x: int, y: int, hardcover: bool) -> str:
    fill = TEAL if hardcover else LIGHT
    stroke = TEAL if hardcover else "#8fa6af"
    page = "#ffffff" if hardcover else "#607987"
    return (
        f'<g transform="translate({x},{y})">'
        f'<rect width="52" height="70" rx="5" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        f'<line x1="10" y1="3" x2="10" y2="67" stroke="{page}" stroke-width="2"/>'
        f'<line x1="20" y1="19" x2="43" y2="19" stroke="{page}" stroke-width="3"/>'
        f'<line x1="20" y1="27" x2="39" y2="27" stroke="{page}" stroke-width="3"/>'
        '</g>'
    )


rows = [
    ("Some: minimum", 1, 132),
    ("Most: minimum", 5, 242),
    ("All: exact count", 8, 352),
]
parts = start("One shelf, three different claims", "Eight books in each row. One hardcover book satisfies some, five satisfy most, and eight are required for all.", 470)
parts.append(label(38, 80, "Teal books are hardcover. Each row has eight books.", 17, MUTED))
for title, count, y in rows:
    parts.append(label(38, y + 43, title, 19, INK, 700))
    for i in range(8):
        parts.append(book(335 + i * 68, y, i < count))
    parts.append(label(335, y + 95, f"{count} of 8 hardcover", 16, MUTED))
parts.append('</svg>')
(ROOT / "book-quantity-cases.svg").write_text("\n".join(parts), encoding="utf-8")

for name, title, cases in [
    ("some-books.svg", "SOME: at least one", [("Minimum", 1), ("Also possible", 8)]),
    ("most-books.svg", "MOST: more than half", [("Minimum", 5), ("Also possible", 8)]),
    ("all-books.svg", "ALL: every one", [("Required", 8)]),
]:
    height = 320 if len(cases) == 2 else 215
    parts = start(title, f"Eight books. Hardcover counts shown: {', '.join(str(count) for _, count in cases)}.", height)
    parts.append(label(38, 79, "Teal books are hardcover.", 17, MUTED))
    for row, (caption, count) in enumerate(cases):
        y = 105 + row * 110
        parts.append(label(38, y + 42, f"{caption}: {count} of 8", 19, INK, 700))
        for i in range(8):
            parts.append(book(335 + i * 68, y, i < count))
    parts.append('</svg>')
    (ROOT / name).write_text("\n".join(parts), encoding="utf-8")

parts = start("What each word permits", "For eight existing books, some permits one to eight hardcover, most permits five to eight, and all permits exactly eight.", 340)
parts.append(label(38, 80, "Number of hardcover books, out of eight", 17, MUTED))
for y, name, first in [(128, "Some", 1), (201, "Most", 5), (274, "All", 8)]:
    parts.append(label(38, y + 26, name, 20, INK, 700))
    for value in range(9):
        x = 262 + value * 72
        active = value >= first
        parts.append(f'<circle cx="{x}" cy="{y+18}" r="23" fill="{TEAL if active else LIGHT}"/>')
        parts.append(f'<text x="{x}" y="{y+25}" text-anchor="middle" fill="{"#ffffff" if active else MUTED}" font-family="Arial,sans-serif" font-size="20" font-weight="700">{value}</text>')
parts.append('</svg>')
(ROOT / "book-quantity-ranges.svg").write_text("\n".join(parts), encoding="utf-8")

parts = start("Two majorities must meet", "Of ten club members, six study law and six work part time. Members five and six have both traits.", 300)
parts.append(label(38, 80, "Ten club members. Each trait belongs to at least six.", 17, MUTED))
for i in range(10):
    x = 84 + i * 83
    color = PURPLE if i in (4, 5) else TEAL if i < 4 else GOLD
    parts.append(f'<circle cx="{x}" cy="161" r="29" fill="{color}"/>')
    parts.append(f'<text x="{x}" y="169" text-anchor="middle" fill="#ffffff" font-family="Arial,sans-serif" font-size="20" font-weight="700">{i+1}</text>')
parts.append(f'<line x1="84" y1="211" x2="499" y2="211" stroke="{TEAL}" stroke-width="5"/>')
parts.append(f'<line x1="416" y1="234" x2="831" y2="234" stroke="{GOLD}" stroke-width="5"/>')
parts.append(label(232, 203, "Study law", 16, TEAL, 700))
parts.append(label(551, 268, "Work part time", 16, GOLD, 700))
parts.append(label(392, 203, "Both", 16, PURPLE, 700))
parts.append('</svg>')
(ROOT / "club-majority-overlap.svg").write_text("\n".join(parts), encoding="utf-8")
