from pathlib import Path
import importlib.util
import re
from bs4 import BeautifulSoup
from markdownify import markdownify

folder = Path(__file__).resolve().parent
root = folder.parents[1]
spec = importlib.util.spec_from_file_location("recap_builder", root / ".agents/skills/post-session-recap/references/session-manual/build_session_manual.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
source = (folder / "recap.src.html").read_text(encoding="utf8")
outputs = {"recap.html": source.replace("/*CSS*/", builder.CSS)}
for name, kicker, marker in [
    ("necessary-assumption.md", "Reference · Keep it open while you drill", "yahunatan-necessary-assumption-reference"),
    ("primer-negation-station.md", "Before you start · Negation Station", "yahunatan-2026-10-20-negation-primer"),
]:
    outputs[name.replace(".md", ".html")] = builder.from_md(str(folder / name), kicker, marker)
for name, html in outputs.items():
    builder.lint(name, html)

canonical = root / "students/yahunatan-zetvy/recaps/2026-10-20-recap.md"
old = canonical.read_text(encoding="utf8")
frontmatter = re.match(r"---.*?---", old, re.S).group()
private = old[old.index("<!-- PRIVATE CONTINUATION"):]
soup = BeautifulSoup(source, "html.parser")
for element in soup.select("script, style, head, .footer-note"):
    element.decompose()
# Explicit separators prevent labels and hidden answers running into adjacent text.
for element in soup.select(".tag, .name, .sec-kicker, .kicker"):
    element.insert_before("\n")
    element.insert_after("\n")
for element in soup.select("b, strong"):
    element.insert_after(" ")
for element in soup.select(".ans"):
    element.insert_before(" ")
public = markdownify(str(soup.body), heading_style="ATX").strip()
if "**The evidence**Accept" in public or "arrived.·" in public:
    raise ValueError("Markdown labels or hidden answers lost their spacing")
for name, html in outputs.items():
    (folder / name).write_text(html, encoding="utf8")
canonical.write_text(frontmatter + "\n\n" + public + "\n\n" + private, encoding="utf8")
print("Synced three HTML notes and canonical Markdown with label/answer spacing.")
