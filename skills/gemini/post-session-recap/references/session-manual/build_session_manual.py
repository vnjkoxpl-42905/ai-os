"""Render post-session notes in the Session Manual look (model: Reading Flaw Answer Choices, 2026-08-05)."""
import markdown, re, sys, os, html, json
from html.parser import HTMLParser
HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "session-manual.css"), encoding="utf8") as css_file:
    CSS = css_file.read()
with open(os.path.join(HERE, "student-copy-exclusions.json"), encoding="utf8") as rules_file:
    COPY_EXCLUSIONS = json.load(rules_file)["phrases"]

def recap(folder):
    with open(os.path.join(folder, "recap.src.html"), encoding="utf8") as source_file:
        src = source_file.read()
    return src.replace("/*CSS*/", CSS)

def from_md(md_path, kicker, marker):
    with open(md_path, encoding="utf8") as markdown_file:
        t = markdown_file.read()
    title = re.search(r"^# (.+)$", t, re.M).group(1)
    body = re.sub(r"^# .+$", "", t, count=1, flags=re.M).strip()
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    lede_md, sections = parts[0], list(zip(parts[1::2], parts[2::2]))
    md = lambda s: markdown.markdown(s, extensions=["tables", "fenced_code"]).replace("<table>", '<table class="t">')
    lede = md(lede_md).replace("<p>", '<p class="lede">', 1) if lede_md.strip() else ""
    secs = "".join(f'<section><div class="wrap"><h2>{html.escape(h)}</h2>{md(b)}</div></section>' for h, b in sections)
    if not sections:
        secs = ""
        lede = lede.replace('<p class="lede">', '<p class="lede">', 1)
    label = re.split(r"\s*[·|:]\s*", kicker.strip(), maxsplit=1)[0]
    suffix = {"before you start": "Before you start", "reference": "Reference", "session recap": "Session recap"}.get(label.casefold(), "Session notes")
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="lsatu-interactive-lesson" content="{marker}"><title>{html.escape(title)} · {suffix}</title><style>{CSS}</style></head><body>
<header class="hero"><div class="wrap"><div class="kicker">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1>{lede}</div></header>
{secs}<div class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></div></body></html>"""

class StudentCopy(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.ignored = []
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

def lint(name, t):
    copy = StudentCopy()
    copy.feed(t)
    rendered = " ".join(copy.parts)
    rejected = [phrase for phrase in COPY_EXCLUSIONS
                if re.search(r"(?<!\w)" + r"\s+".join(re.escape(word) for word in phrase.split()) + r"(?!\w)", rendered, re.I)]
    if rejected:
        raise ValueError("Student-facing copy contains rejected phrase(s): " + ", ".join(rejected))
    bad = [x for x in ["—", "–", "~", "concept lesson", "establish"] if x in rendered]
    if bad:
        raise ValueError("Student-facing copy contains rejected wording: " + ", ".join(bad))
    print(f"{name}: {len(t.encode())} bytes", "ok")

if __name__ == "__main__":
    folder = sys.argv[1]
    jobs = [("recap.html", recap(folder))]
    for spec in sys.argv[2:]:
        md_name, kicker, marker = spec.split("|")
        jobs.append((md_name.replace(".md", ".html"), from_md(os.path.join(folder, md_name), kicker, marker)))
    # Reject any page before replacing any existing generated artifact.
    for name, t in jobs:
        lint(name, t)
    for name, t in jobs:
        open(os.path.join(folder, name), "w", encoding="utf8").write(t)
