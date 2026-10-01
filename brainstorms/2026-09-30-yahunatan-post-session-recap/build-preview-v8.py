"""Build V8 from its explicit review source, preserving the established visuals."""
from pathlib import Path
import importlib.util
import html
import json
import re

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('v7', HERE / 'build-preview-v7.py')
v7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v7)

def main():
    source = (HERE / 'concept-lesson-v8.md').read_text(encoding='utf-8')
    renderer = v7.previous.Renderer()
    title, body = renderer.render(source)
    opening_source = re.sub(r'\n\n\*\*(?:Fact|Rule) means:\*\* [^\n]+', '', source)
    opening = v7.opening(opening_source).replace('href="#section-5"', 'href="#section-4"')
    opening = opening.replace('<div class="intro-methods">', '<div class="intro-definitions"><div><strong>Fact</strong><p>Something established as true about a case or group. “Mira is trained.”</p></div><div><strong>Rule</strong><p>What must be true if a condition is met. “Every trained person has a badge.”</p></div></div><div class="intro-methods">')
    body = re.sub(r'<header class="opening">.*?</header>', lambda _: opening, body, count=1, flags=re.S)
    body = re.sub(r'<h3>(Fact [1-4]:.*?)</h3>', r'<h4>\1</h4>', body)
    nav = '<nav class="jump" aria-label="Lesson sections">' + ''.join(f'<a href="#section-{n}">{label}</a>' for n,label in [(1,'Facts'),(2,'Rules'),(3,'Apply'),(4,'Link'),(5,'Add a fact'),(6,'Invalid moves'),(7,'Contrapose'),(8,'Wording'),(10,'Practice')]) + '</nav>'
    body = re.sub(r'<nav class="jump".*?</nav>', lambda _: nav, body, count=1, flags=re.S)
    body = body.replace('Name the move. Explain what the statements guarantee.', 'Write your conclusion and the rule or chain that proves it.').replace('<h2>Follow the fact.</h2>', '<h2>What does this fact let you conclude?</h2>').replace('<span class="eyebrow">Use the moves</span>', '<span class="eyebrow">Conditional reasoning practice</span>')
    assert renderer.checks == 7 and len(renderer.practice) == 4
    data = json.dumps(renderer.practice, ensure_ascii=False).replace('<', '\\u003c')
    body = '<section class="hero"><h1 class="lesson-title"><span>Facts,</span><span>Rules,</span><span>and What Follows</span></h1>' + body.replace('</header>', '</header></section>', 1)
    extra = '.chapter h4{font-size:21px;margin:32px 0 18px;color:var(--blue)}.intro-definitions{display:grid;grid-template-columns:1fr 1fr;gap:38px;margin:0 0 35px;padding:22px 0;border-top:1px solid #496291;border-bottom:1px solid #496291}.intro-definitions strong{display:block;font-size:23px;color:#d8bcff!important}.intro-definitions>div+div strong{color:#9bedd9!important}.intro-definitions p{font-size:18px;line-height:1.6;margin:10px 0 0;color:#e4edff}.intro-definitions+ .intro-methods{margin-top:25px}@media(max-width:740px){.intro-definitions{grid-template-columns:1fr;gap:25px}}'
    p = v7.previous
    page = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="yahunatan-2026-09-16-conditional-reasoning"><title>{html.escape(title)} | LSAT U</title><style>{p.CSS}{p.HERO_CSS}{p.READING_CSS}{p.V6_CSS}{v7.CSS}{extra}</style></head><body><header class="top"><b>LSAT U</b><div class="top-right"><span>Notes and recaps</span><button type="button" id="motion-toggle" aria-pressed="false">Pause motion</button></div></header><main class="lesson-shell">{body}</main><script>const practice={data};{p.base.JS}{p.EXTRA_JS}</script></body></html>'
    for rejected in ['Read each whole idea.', 'Find what the statements guarantee.', 'concept lesson', '\u2014']:
        assert rejected not in page, rejected
    ids = re.findall(r'\bid="([^"]+)"', page)
    assert len(ids) == len(set(ids)), 'Duplicate ids'
    assert all(anchor in ids for anchor in re.findall(r'href="#([^"]+)"',page)), 'Broken section link'
    output = HERE / 'conditional-reasoning-v8.html'
    output.write_text(page, encoding='utf-8')
    print(f'{output}\nChecks: {renderer.checks}; mixed: {len(renderer.practice)}; bytes: {len(page.encode("utf-8"))}')

if __name__ == '__main__':
    main()
