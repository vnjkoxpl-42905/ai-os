"""Render post-session notes in the Session Manual look (model: Reading Flaw Answer Choices, 2026-08-05)."""
import markdown, re, sys, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "session-manual.css"), encoding="utf8").read()

def recap(folder):
    src = open(os.path.join(folder, "recap.src.html"), encoding="utf8").read()
    return src.replace("/*CSS*/", CSS)

def from_md(md_path, kicker, marker):
    t = open(md_path, encoding="utf8").read()
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
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="lsatu-interactive-lesson" content="{marker}"><title>{html.escape(title)} · Session Manual</title><style>{CSS}</style></head><body>
<header class="hero"><div class="wrap"><div class="kicker">{html.escape(kicker)}</div><h1>{html.escape(title)}</h1>{lede}</div></header>
{secs}<div class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></div></body></html>"""

def lint(name, t):
    body = re.sub(r"<style>.*?</style>", "", t, flags=re.S)
    bad = [x for x in ["—", "–", "~", "concept lesson", "establish"] if x in body]
    print(f"{name}: {len(t.encode())} bytes", "BAD " + ",".join(bad) if bad else "ok")

if __name__ == "__main__":
    folder = sys.argv[1]
    jobs = [("recap.html", recap(folder))]
    for spec in sys.argv[2:]:
        md_name, kicker, marker = spec.split("|")
        jobs.append((md_name.replace(".md", ".html"), from_md(os.path.join(folder, md_name), kicker, marker)))
    for name, t in jobs:
        open(os.path.join(folder, name), "w", encoding="utf8").write(t)
        lint(name, t)
