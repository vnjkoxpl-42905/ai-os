"""Build post-session notes in the Session Desk look (model: Finding the Conclusion by Asking Why, approved 2026-11-13).

Usage, from anywhere:
  uv run --with markdown python -I build_session_desk.py <build-folder> ^
      "<primer.md>|Before you start · <drill name>|<lesson-marker>" ^
      "<reference.md>|Reference · Keep it open while you drill|<lesson-marker>"

  <build-folder>/recap.src.html  ->  <build-folder>/recap.html
  each Markdown file             ->  the same name with .html

  --model   rebuild model-finding-the-conclusion.html from its .src.html (no folder needed)

Every page is checked before any file is written. A failed check writes nothing.
"""
import html, json, os, re, sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
read = lambda *p: open(os.path.join(*p), encoding="utf8").read()
CSS = read(HERE, "session-desk.css")
JS = read(HERE, "session-desk.js")
COPY_EXCLUSIONS = json.loads(read(HERE, "..", "session-manual", "student-copy-exclusions.json"))["phrases"]
MAX_BYTES = 500_000
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..700;1,9..144,400..600'
         '&family=Outfit:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">')
CHROME = '<div class="progress" aria-hidden="true"><i></i></div>\n<nav class="rail" aria-label="Sections"><ol></ol></nav>\n'
KINDS = {"describe", "assume", "object", "neutral"}


def recap(src_path):
    src = read(src_path)
    for slot in ("/*CSS*/", "/*JS*/"):
        if src.count(slot) != 1:
            raise ValueError(f"{os.path.basename(src_path)}: expected exactly one {slot} slot")
    return src.replace("/*CSS*/", CSS).replace("/*JS*/", JS)


def from_md(md_path, kicker, marker):
    import markdown
    t = read(md_path)
    title = re.search(r"^# (.+)$", t, re.M).group(1)
    body = re.sub(r"^# .+$", "", t, count=1, flags=re.M).strip()
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    intro, sections = parts[0].strip(), list(zip(parts[1::2], parts[2::2]))

    def md(s):
        out = markdown.markdown(s, extensions=["tables", "fenced_code"])
        out = out.replace("<table>", '<div class="table-wrap"><table class="t">').replace("</table>", "</table></div>")
        out = out.replace("<ol>", '<ol class="steps">')
        out = re.sub(r"<blockquote>\s*<p><strong>(.+?)</strong>\s*", r'<div class="callout"><span class="tag">\1</span><p>', out)
        return out.replace("<blockquote>", '<div class="callout">').replace("</blockquote>", "</div>")

    label = re.split(r"\s*[·|:]\s*", kicker.strip(), maxsplit=1)[0]
    suffix = {"before you start": "Before you start", "reference": "Reference"}.get(label.casefold(), "Session notes")
    # The first paragraph is the lede. Anything else before the first "## " becomes an opening plane.
    first, _, rest = intro.partition("\n\n")
    lede = md(first).replace("<p>", '<p class="lede">', 1) if first else ""
    planes = ""
    if rest.strip():
        planes += f'<section><div class="wrap"><div class="sec-kicker">{html.escape(suffix)}</div>{md(rest)}</div></section>\n'
    for heading, text in sections:
        planes += f'<section><div class="wrap"><div class="sec-kicker"></div><h2>{html.escape(heading.strip())}</h2>{md(text)}</div></section>\n'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="lsatu-interactive-lesson" content="{html.escape(marker)}">
<title>{html.escape(title)} · {suffix}</title>
{FONTS}
<style>
{CSS}</style>
</head>
<body>
{CHROME}<div class="page">
<header class="hero solo"><div class="wrap"><div class="kicker">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1>{lede}</div></header>
<main>
{planes}</main>
<div class="footer-note"><span class="mark">LSAT U</span></div>
</div>
<script>
{JS}</script>
</body>
</html>
"""


class StudentCopy(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.ignored = [], []
    def handle_starttag(self, tag, attrs):
        if tag in {"style", "script"}: self.ignored.append(tag)
        if self.ignored: return
        for key, value in attrs:
            if key in {"aria-label", "title", "placeholder", "value", "alt"} and value:
                self.parts.append(value)
    def handle_endtag(self, tag):
        if self.ignored and tag == self.ignored[-1]: self.ignored.pop()
    def handle_data(self, value):
        if not self.ignored: self.parts.append(value)


def lint_copy(t):
    """Wording every student-facing page must pass, revealed answers and labels included."""
    copy = StudentCopy(); copy.feed(t)
    rendered = " ".join(copy.parts)
    problems = ["rejected phrase: " + p for p in COPY_EXCLUSIONS
                if re.search(r"(?<!\w)" + r"\s+".join(re.escape(w) for w in p.split()) + r"(?!\w)", rendered, re.I)]
    problems += ["rejected wording: " + repr(x) for x in ["—", "–", "~", "concept lesson", "establish"] if x in rendered]
    return problems


def check_page(t):
    """Rules for every Session Desk page."""
    p = []
    body = t.split("</head>", 1)[-1]
    body = re.sub(r"<script>.*?</script>", "", body, flags=re.S)
    marker = re.search(r'<meta name="lsatu-interactive-lesson" content="([^"]*)">', t)
    if not marker or not marker.group(1).strip(): p.append("missing lsatu-interactive-lesson marker")
    elif "preview" in marker.group(1): p.append("marker still says preview")
    if len(t.encode()) > MAX_BYTES: p.append(f"page is over {MAX_BYTES} bytes")
    if len(re.findall(r"<h1[ >]", body)) != 1: p.append("need exactly one h1")
    if '<div class="kicker">' not in body: p.append("missing hero kicker")
    if '<span class="mark">LSAT U</span>' not in body: p.append("missing LSAT U footer mark")
    if re.search(r'\sstyle="', body): p.append("inline style attribute found; put the rule in session-desk.css")
    if re.search(r"<(img|iframe|video|script src)", body): p.append("outside media or script found; pages stay self-contained")
    for cal in re.findall(r'<div class="callout[^"]*">(.*?)</div>', body, re.S):
        if '<span class="tag">' not in cal: p.append("a callout has no tag line")
    return p


def check_recap(t):
    """Extra rules for the session recap: everything the model has, wired the same way."""
    p = []
    body = t.split("</head>", 1)[-1]
    if not re.search(r"<title>[^<]+ · Session recap</title>", t): p.append('title must end " · Session recap"')
    if not re.search(r'<div class="kicker">Session recap · [A-Z][a-z]+ \d{1,2}</div>', body): p.append('kicker must read "Session recap · <Month day>"')
    if '<p class="lede">' not in body: p.append("missing lede")
    stage = re.search(r'<div class="stage" aria-hidden="true">(.*?)</header>', body, re.S)
    if not stage: p.append("missing hero stage (aria-hidden)")
    else:
        for cls in ("slab base", "slab c2", "slab c1"):
            if stage.group(1).count(f'class="{cls}"') != 1: p.append(f"hero stage needs exactly one .{cls.replace(' ', '.')}")
        if 'class="stack" data-tilt="10"' not in stage.group(1): p.append('hero stack needs data-tilt="10"')
    sections = re.findall(r"<section>(.*?)</section>", body, re.S)
    if not 5 <= len(sections) <= 9: p.append(f"recap has {len(sections)} sections; the model has 7 (allowed 5 to 9)")
    for i, s in enumerate(sections, 1):
        if not re.search(r'<div class="sec-kicker">[^<]+</div>', s): p.append(f"section {i} has no kicker text")
        if "<h2>" not in s: p.append(f"section {i} has no h2")
    drills = re.findall(r'<div class="drill">(.*?)</div>\s*</div>\s*(?=<div class="drill">|</div></section>)', body, re.S)
    n_drills = body.count('<div class="drill">')
    if not 2 <= n_drills <= 3: p.append(f"recap has {n_drills} practice checks; need 2 or 3")
    if body.count('<div class="drill-head">') != n_drills: p.append("every .drill needs a .drill-head")
    if len(re.findall(r'<div class="drill-head"><div>\s*<h3>[^<]+</h3>\s*<p class="hint">', body)) != n_drills:
        p.append("every .drill-head needs an h3 and a p.hint")
    chips = re.findall(r'<div class="chip"([^>]*)>(.*?)</div>', body, re.S)
    if len(chips) < 5: p.append(f"only {len(chips)} tap-to-check rows; need at least 5 across the practice checks")
    if body.count('class="chip"') != len(chips): p.append("a .chip is not a <div> or contains a nested <div>")
    for i, (attrs, inner) in enumerate(chips, 1):
        k = re.search(r'data-k="([^"]*)"', attrs)
        if not k or k.group(1) not in KINDS: p.append(f"chip {i}: data-k must be one of {sorted(KINDS)}")
        for need in ('role="button"', 'tabindex="0"', 'aria-expanded="false"'):
            if need not in attrs: p.append(f"chip {i}: missing {need}")
        if not re.match(r'\s*<span>[^<]', inner): p.append(f"chip {i}: the sentence must be the first <span>")
        if len(re.findall(r'<span class="stamp" aria-hidden="true">[^<]{2,14}</span>', inner)) != 1: p.append(f"chip {i}: needs one .stamp (aria-hidden, 2 to 14 characters)")
        ans = re.search(r'<span class="ans">(.*)</span>\s*$', inner, re.S)
        if not ans: p.append(f"chip {i}: needs a closing .ans explanation")
        elif ans.group(1).lstrip().startswith("·"): p.append(f"chip {i}: drop the leading dot from the answer")
    gates = body.count('<div class="gate"')
    if gates > 1: p.append("at most one .gate per recap")
    if gates:
        g = re.search(r'<div class="gate" data-state="0">(.*?)</div>\s*</div>\s*</div>', body, re.S)
        if not g: p.append('.gate must start as data-state="0"')
        else:
            if len(re.findall(r'<button class="sw" type="button" role="switch" aria-checked="false">', g.group(1))) != 2: p.append(".gate needs exactly two switches, both off")
            for v in ("v0", "v1", "v2", "v3"):
                if g.group(1).count(f'<span class="{v}">') != 1: p.append(f".gate verdict is missing .{v}")
            if '<div class="verdict" role="status"><i class="lamp"></i>' not in g.group(1): p.append(".gate verdict needs role=status and the lamp")
    if not 1 <= body.count('<div class="quote">') <= 2: p.append("need one or two credit lines (.quote)")
    if body.count('<ol class="steps todo">') != 1: p.append('need exactly one <ol class="steps todo"> for the student\'s work')
    if not sections or '<ol class="steps todo">' not in sections[-1]: p.append("the student's work must be the last section")
    return p


def main(argv):
    if argv and argv[0] == "--model":
        jobs = [(os.path.join(HERE, "model-finding-the-conclusion.html"), recap(os.path.join(HERE, "model-finding-the-conclusion.src.html")), True)]
    else:
        folder = argv[0]
        jobs = [(os.path.join(folder, "recap.html"), recap(os.path.join(folder, "recap.src.html")), True)]
        for spec in argv[1:]:
            md_name, kicker, marker = spec.split("|")
            jobs.append((os.path.join(folder, md_name.replace(".md", ".html")), from_md(os.path.join(folder, md_name), kicker, marker), False))
    failed = False
    for path, t, is_recap in jobs:
        problems = lint_copy(t) + check_page(t) + (check_recap(t) if is_recap else [])
        name = os.path.basename(path)
        if problems:
            failed = True
            print(f"{name}: FAILED")
            for x in problems: print("  - " + x)
        else:
            print(f"{name}: {len(t.encode())} bytes ok")
    if failed:
        raise SystemExit("Nothing was written. Fix the problems above and run again.")
    for path, t, _ in jobs:
        open(path, "w", encoding="utf8", newline="\n").write(t)


if __name__ == "__main__":
    main(sys.argv[1:])
