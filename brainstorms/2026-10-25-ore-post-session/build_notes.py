"""Build Ore's draft pages from the canonical public recap and companion Markdown."""
from pathlib import Path
import html
import importlib.util
import re
import markdown

ROOT = Path(__file__).resolve().parents[2]
FOLDER = Path(__file__).parent
spec = importlib.util.spec_from_file_location("note_builder", ROOT / ".agents/skills/post-session-recap/references/session-manual/build_session_manual.py")
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)

# The canonical record owns teaching text. Never replace its private history.
record = (ROOT / "students/ore/recaps/2026-10-23-recap.md").read_text(encoding="utf-8")
if "<!-- PRIVATE CONTINUATION" not in record:
    raise ValueError("Canonical record needs its private boundary")
public = record.split("<!-- PRIVATE CONTINUATION", 1)[0]
public = re.sub(r"\A---\n.*?\n---\n", "", public, count=1, flags=re.S).strip()
match = re.match(r"# (.+)\n", public)
if not match:
    raise ValueError("Canonical public recap needs one title")
title = match.group(1)
body = public[match.end():].strip()
parts = re.split(r"^## (.+)$", body, flags=re.M)
def render(value):
    return markdown.markdown(value, extensions=["tables"]).replace("<table>", '<table class="t">')
lede = render(parts[0]).replace("<p>", '<p class="lede">', 1)
sections = "".join('<section><div class="wrap"><h2>' + html.escape(heading) + '</h2>' + render(content) + '</div></section>' for heading, content in zip(parts[1::2], parts[2::2]))
old_src = (FOLDER / "recap.src.html").read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", old_src, re.S).group(1)
if "/*CSS*/" not in style:
    raise ValueError("Recap source must use the shared CSS placeholder")
words = title.rsplit(" ", 1)
hero_title = "<br>".join(html.escape(word) for word in words)
source = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="ore-2026-10-23-evidence-and-conclusion"><title>' + html.escape(title) + ' · Session recap</title><style>' + style + '</style></head><body><header class="hero"><div class="wrap"><div class="kicker">Session recap · October 23</div><h1>' + hero_title + '</h1>' + lede + '</div></header>' + sections + '<footer class="footer-note"><div class="wrap"><span class="mark">LSAT U</span></div></footer></body></html>'
jobs = [("recap.html", source.replace("/*CSS*/", shared.CSS))]
for filename, kicker, marker in [
    ("primer-recall.md", "Before you start · Your section and follow-up work", "ore-2026-10-23-recall-primer"),
    ("argument-reference.md", "Reference · Keep it open while you drill", "ore-argument-connection-reference"),
]:
    jobs.append((filename.replace(".md", ".html"), shared.from_md(str(FOLDER / filename), kicker, marker)))
# Validate every page before changing any generated output.
for filename, content in jobs:
    shared.lint(filename, content)
(FOLDER / "recap.src.html").write_text(source, encoding="utf-8")
for filename, content in jobs:
    (FOLDER / filename).write_text(content, encoding="utf-8")
print("Built three draft pages; canonical public text and private history left intact")
