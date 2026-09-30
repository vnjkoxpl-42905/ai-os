"""Build the review-only recap upgrade from its two Markdown teaching sources."""
from pathlib import Path
import ast
import html
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECAP = ROOT / "students/yahunatan-zetvy/recaps/2026-09-16-recap.md"
UPGRADE = HERE / "integration-upgrade.md"
OUTPUT = HERE / "conditional-reasoning-v2.html"


def original_literals():
    """Reuse presentation/interaction assets without executing the old note writer."""
    tree = ast.parse((HERE / "build-preview.py").read_text(encoding="utf-8-sig"))
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {"css", "js", "model"}:
                    result[target.id] = ast.literal_eval(node.value)
    if set(result) != {"css", "js", "model"}:
        raise ValueError("Original preview presentation assets could not be located")
    return result


def student_source(text):
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)
    divider = re.search(r"\n---\s*\n\s*## Notes for me", text)
    if not divider:
        raise ValueError("Private recap divider missing; refusing to include private notes")
    return text[:divider.start()].strip()


def inline(text):
    value = html.escape(text)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return value


class Renderer:
    def __init__(self, model):
        self.counter = 0
        self.model = model
        self.model_used = False

    def check(self, prompt, answer):
        self.counter += 1
        index = self.counter
        return f'''<section class="check" data-check="{index}"><form><label for="answer-{index}">{inline(prompt)}</label><textarea id="answer-{index}" rows="3" required placeholder="Write your answer and explain why."></textarea><button type="submit">Check my answer</button></form><div class="feedback" hidden tabindex="-1"><strong>Compare your reasoning</strong><p>{inline(answer)}</p><p class="small">Your response stays above. Compare the direction, the complete conditions, and the strength of the claim. This exercise does not automatically grade your reasoning.</p><button class="again" type="button">Try again</button></div><noscript><p><strong>Worked answer:</strong> {inline(answer)}</p></noscript></section>'''

    def prose(self, block):
        lines = block.splitlines()
        if all(re.match(r"^\d+\. ", line) for line in lines):
            return "<ol>"+"".join("<li>"+inline(re.sub(r"^\d+\. ", "", line))+"</li>" for line in lines)+"</ol>"
        if all(line.startswith("- ") for line in lines):
            return "<ul>"+"".join("<li>"+inline(line[2:])+"</li>" for line in lines)+"</ul>"
        if block.startswith("|"):
            if not self.model_used and "Should undergo mediation" in block:
                self.model_used = True
                return self.model
            rows = [line.strip().strip("|").split("|") for line in lines if line.strip().startswith("|")]
            rows = [[cell.strip() for cell in row] for row in rows]
            rows = [row for row in rows if not all(re.match(r"^:?-+:?$", cell) for cell in row)]
            if not rows:
                raise ValueError("Empty Markdown table")
            return '<div class="table-scroll"><table class="decision-table"><thead><tr>'+"".join("<th scope=\"col\">"+inline(cell)+"</th>" for cell in rows[0])+"</tr></thead><tbody>"+"".join("<tr>"+"".join("<td>"+inline(cell)+"</td>" for cell in row)+"</tr>" for row in rows[1:])+"</tbody></table></div>"
        if (" → " in block or " -> " in block) and len(block) < 150:
            return '<p class="formula">'+inline(block).replace("\n", "<br>")+"</p>"
        return "<p>"+inline(block).replace("\n", " ")+"</p>"

    def render(self, text, prefix):
        blocks = re.split(r"\n\s*\n", text.strip())
        rendered = []
        chapter = False
        index = 0
        chapter_count = 0
        while index < len(blocks):
            block = blocks[index].strip()
            if block.startswith("# "):
                index += 1
                continue
            if block.startswith("## "):
                if chapter:
                    rendered.append("</section>")
                chapter_count += 1
                rendered.append(f'<section class="chapter" id="{prefix}-{chapter_count}"><h2>'+inline(block[3:])+"</h2>")
                chapter = True
            elif block.startswith("### "):
                rendered.append("<h3>"+inline(block[4:])+"</h3>")
            elif index+1 < len(blocks) and blocks[index+1].startswith("**Worked answer:**"):
                answer = blocks[index+1][len("**Worked answer:**"):].strip()
                rendered.append(self.check(block, answer))
                index += 1
            elif block.startswith("**Worked answer:**"):
                raise ValueError("Worked answer is missing its preceding prompt")
            elif block == "---":
                rendered.append("<hr>")
            else:
                rendered.append(self.prose(block))
            index += 1
        if chapter:
            rendered.append("</section>")
        return "".join(rendered)


def main():
    if not UPGRADE.exists():
        raise SystemExit("Missing integration-upgrade.md; the new concept source must exist before building")
    source = student_source(RECAP.read_text(encoding="utf-8-sig"))
    extension = re.search(r"^## \d{4}-\d{2}-\d{2} concept extension:", source, flags=re.M)
    if extension:
        source = source[:extension.start()].strip()
    upgrade = UPGRADE.read_text(encoding="utf-8-sig").strip()
    if "Notes for me" in upgrade or "teacher_note" in upgrade:
        raise ValueError("Upgrade contains private notes; keep teaching prose separate")
    assets = original_literals()
    renderer = Renderer(assets["model"])
    title_match = re.search(r"^# (.+)$", source, flags=re.M)
    if not title_match:
        raise ValueError("Canonical recap title missing")
    title = title_match[1]
    split = source.find("\n## Put the requirement on the right")
    if split < 0:
        raise ValueError("Expected concept insertion point missing; inspect the updated recap")
    body = renderer.render(source[:split], "opening")
    upgrade = re.sub(r"\A# ", "## ", upgrade, count=1)
    body += '<div id="concept-upgrade">'+renderer.render(upgrade, "concept")+"</div>"
    body += renderer.render(source[split:], "session")
    if not renderer.model_used:
        raise ValueError("Canonical truth-case table not found; original interaction would be lost")
    if renderer.counter < 11:
        raise ValueError("Upgrade must add an answer-as-you-go check to the original ten")
    css = assets["css"]+'''code{font:0.95em ui-monospace,monospace}.table-scroll{overflow-x:auto;margin:25px 0}.decision-table{color:#172a30;border:1px solid #cbd9d6}.decision-table th,.decision-table td{border-bottom:1px solid #cbd9d6;padding:14px;vertical-align:top}.decision-table th{background:#e8f1ef}#concept-upgrade{border-left:3px solid #368281;padding-left:24px;margin:34px 0}#concept-upgrade .chapter:first-child{border-top:0}hr{border:0;border-top:1px solid #d4dfdd;margin:30px 0}@media(max-width:600px){#concept-upgrade{padding-left:14px}.decision-table{font-size:14px}.decision-table th,.decision-table td{padding:10px}}'''
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="yahunatan-2026-09-16-conditional-reasoning"><title>{html.escape(title)} | LSAT U</title><style>{css}</style></head><body><header><span>LSAT U</span><span>Classroom · Notes and recaps</span></header><main><div class="dateline"><time datetime="2026-09-16">2026-09-16</time></div><h1>{html.escape(title)}</h1>{body}<footer>Write the whole idea. Check the direction. Keep only what follows.</footer></main><script>{assets['js']}</script></body></html>'''
    if len(page.encode("utf-8")) >= 500_000:
        raise ValueError("Interactive lesson exceeds the package size limit")
    OUTPUT.write_text(page, encoding="utf-8")
    print(json_summary(OUTPUT, renderer.counter, page))


def json_summary(path, checks, page):
    return f"{path}\nTyped checks: {checks}\nHTML bytes: {len(page.encode('utf-8'))}\nInputs: canonical student recap + integration-upgrade.md; no canonical or private note writes."


if __name__ == "__main__":
    main()
