"""Build the current recap with two concrete, numbered opening scenarios."""
from pathlib import Path
import importlib.util
import html
import json
import re

HERE = Path(__file__).resolve().parent
RECAP = HERE.parents[1] / 'students/yahunatan-zetvy/recaps/2026-09-16-recap.md'
OUTPUT = HERE / 'conditional-reasoning-v7.html'
BEGIN = '<!-- BEGIN CURRENT STUDENT LESSON V7 -->'
END = '<!-- END CURRENT STUDENT LESSON V7 -->'
spec = importlib.util.spec_from_file_location('recap_v6', HERE / 'build-preview-v6.py')
previous = importlib.util.module_from_spec(spec)
spec.loader.exec_module(previous)


def source_text():
    canonical = RECAP.read_text(encoding='utf-8-sig')
    if BEGIN in canonical or END in canonical:
        if canonical.count(BEGIN) != 1 or canonical.count(END) != 1:
            raise ValueError('Expected exactly one V7 source block')
        return canonical.split(BEGIN, 1)[1].split(END, 1)[0].strip(), 'canonical V7 source block'
    return (HERE / 'concept-lesson-v7.md').read_text(encoding='utf-8-sig').strip(), 'V7 review draft'


def opening(source):
    intro = source.split('\n## 01 |', 1)[0]
    sections = re.split(r'\n### ([12]) \| ([^\n]+)\n\n', intro)
    lead = sections[0].split('\n\n', 1)[1].strip()
    methods = []
    for index in (1, 4):
        number, title, text = sections[index:index + 3]
        fields = dict(re.findall(r'\*\*([^*]+):\*\* (.*?)(?=\n\n|$)', text, re.S))
        labels = ('Fact', 'Rule') if number == '1' else ('Rule 1', 'Rule 2')
        givens = ''.join('<div class="intro-given"><dt>' + label + '</dt><dd>' + previous.base.inline(fields[label]) + '</dd></div>' for label in labels)
        anchor = 'section-3' if number == '1' else 'section-5'
        link_label = 'Apply a rule, step by step' if number == '1' else 'Link rules, step by step'
        methods.append('<article class="intro-method method-' + number + '"><h2><span class="method-number">' + number + '</span><span>' + html.escape(title) + '</span></h2><dl>' + givens + '</dl><div class="intro-conclusion"><span>Conclusion</span><strong>' + previous.base.inline(fields['Conclusion']) + '</strong></div><p class="intro-why">' + previous.base.inline(fields['Why']) + '</p><p class="intro-result">' + previous.base.inline(fields['Result']) + '</p><a class="intro-link" href="#' + anchor + '">' + link_label + ' <span aria-hidden="true">→</span></a></article>')
    acceptance = intro.rsplit('\n\n', 1)[1].strip()
    return '<header class="opening"><div class="opening-story"><p class="intro-lead">' + previous.base.inline(lead) + '</p><div class="intro-methods">' + ''.join(methods) + '</div><p class="intro-acceptance">' + previous.base.inline(acceptance) + '</p></div></header>'


CSS = r'''
.hero .opening{display:block;margin:0}.hero .opening-story{max-width:none}.hero .lesson-title{font-size:clamp(43px,5.5vw,65px);margin-bottom:25px}.hero{padding:35px 42px 30px}.hero .opening-story>p.intro-lead{max-width:900px!important;font-size:24px!important;line-height:1.5!important;margin-bottom:34px!important}.intro-methods{display:grid;grid-template-columns:1fr 1fr;gap:38px}.intro-method{min-width:0;padding-top:24px;border-top:2px solid #cda9ff}.intro-method.method-2{border-top-color:#93e8d0;padding-left:35px;border-left:1px solid #496291}.intro-method h2{display:flex;gap:19px;align-items:center;font-size:26px;line-height:1.25;margin:0 0 27px;color:#fff}.method-number{font-size:53px;line-height:1;font-weight:800;color:#d8bcff}.method-2 .method-number{color:#9bedd9}.intro-method dl{margin:0}.intro-given{margin-bottom:21px}.intro-given dt{font-size:12px;font-weight:700;letter-spacing:.04em;color:#c7d7f4;margin-bottom:5px}.intro-given dd{font-size:21px;line-height:1.5;margin:0;color:#fff}.intro-conclusion{margin:25px 0 19px;border-top:1px solid #6685bb;padding-top:19px}.intro-conclusion>span{display:block;color:#9bedd9;font-size:12px;font-weight:700;margin-bottom:9px}.intro-conclusion strong{display:block;font-size:25px;line-height:1.35;color:#9bedd9}.intro-method .intro-why{font-size:17px;line-height:1.65;color:#e0eaff;margin:0 0 16px}.intro-method .intro-result{font-size:15px;line-height:1.55;color:#bcd0f0;margin:0 0 23px}.intro-link{font-size:13px;font-weight:700;color:#d5e5ff;text-decoration:none;display:inline-block;padding:7px 0}.intro-link:hover{text-decoration:underline}.hero .opening-story>p.intro-acceptance{max-width:none!important;margin:31px 0 0!important;padding-top:22px!important;border-top:1px solid #496291!important;font-size:15px!important;line-height:1.65!important;color:#cbdaf2!important}.intro-methods strong{color:inherit!important}
@media(max-width:740px){.hero{padding:30px 25px}.intro-methods{grid-template-columns:1fr;gap:35px}.intro-method.method-2{border-left:0;padding-left:0}.hero .opening-story>p.intro-lead{font-size:22px!important}.intro-method h2{font-size:26px}.intro-given dd{font-size:21px}.intro-conclusion strong{font-size:25px}.intro-method .intro-why{font-size:17px}.intro-method .intro-result{font-size:16px}}
@media(max-width:480px){.hero{padding:28px 21px}.hero .lesson-title{font-size:42px;line-height:1.05}.method-number{font-size:47px}.intro-method h2{font-size:24px;gap:16px}.intro-given dd{font-size:20px}}
'''


def main():
    text, origin = source_text()
    renderer = previous.Renderer()
    title, body = renderer.render(text)
    body = re.sub(r'<header class="opening">.*?</header>', lambda _: opening(text), body, count=1, flags=re.S)
    body = body.replace('<a href="#section-2">Contrapositives</a>', '<a href="#section-2">Rules</a>').replace('<a href="#section-3">Linking</a>', '<a href="#section-3">Applying</a>').replace('<a href="#section-5">Whole ideas</a>', '<a href="#section-4">Negating</a><a href="#section-5">Linking</a>')
    body = body.replace('Name the move. Explain what the statements guarantee.', 'Write your conclusion and the rule or chain that proves it.')
    body = body.replace('<h2>Follow the fact.</h2>', '<h2>What does this fact let you conclude?</h2>').replace('<span class="eyebrow">Use the moves</span>', '<span class="eyebrow">Conditional reasoning practice</span>')
    if renderer.checks != 7 or len(renderer.practice) != 4:
        raise ValueError('Expected seven checks and four mixed problems')
    data = json.dumps(renderer.practice, ensure_ascii=False).replace('<', '\\u003c')
    hero_title = '<h1 class="lesson-title"><span>Facts,</span><span>Rules,</span><span>and What Follows</span></h1>'
    body = '<section class="hero">' + hero_title + body.replace('</header>', '</header></section>', 1)
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="yahunatan-2026-09-16-conditional-reasoning"><title>{html.escape(title)} | LSAT U</title><style>{previous.CSS}{previous.HERO_CSS}{previous.READING_CSS}{previous.V6_CSS}{CSS}</style></head><body><header class="top"><b>LSAT U</b><div class="top-right"><span>Notes and recaps</span><button type="button" id="motion-toggle" aria-pressed="false">Pause motion</button></div></header><main class="lesson-shell">{body}</main><script>const practice={data};{previous.base.JS}{previous.EXTRA_JS}</script></body></html>'''
    for rejected in ['Read each whole idea.', 'Find what the statements guarantee.', 'Keep only what must follow.', 'Conditional reasoning uses general rules', 'First, understand each statement.', 'concept lesson', '\u2014']:
        if rejected in page:
            raise ValueError('Rejected copy remains: ' + rejected)
    if len(page.encode('utf-8')) >= 500_000:
        raise ValueError('Package too large')
    OUTPUT.write_text(page, encoding='utf-8')
    print(f'{OUTPUT}\nSource: {origin}\nChecks: {renderer.checks}; mixed: {len(renderer.practice)}; bytes: {len(page.encode("utf-8"))}')


if __name__ == '__main__':
    main()
