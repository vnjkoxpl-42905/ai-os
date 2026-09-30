"""Render the current student concept lesson as a self-contained review preview."""
from pathlib import Path
import html
import json
import re

HERE = Path(__file__).resolve().parent
RECAP = HERE.parents[1] / "students/yahunatan-zetvy/recaps/2026-09-16-recap.md"
DRAFT = HERE / "concept-lesson-v3.md"
OUTPUT = HERE / "conditional-reasoning-v3.html"
BEGIN = "<!-- BEGIN CURRENT STUDENT LESSON V3 -->"
END = "<!-- END CURRENT STUDENT LESSON V3 -->"


def source_text():
    canonical = RECAP.read_text(encoding="utf-8-sig")
    if BEGIN in canonical or END in canonical:
        if canonical.count(BEGIN) != 1 or canonical.count(END) != 1:
            raise ValueError("Current lesson markers must appear exactly once")
        text = canonical.split(BEGIN, 1)[1].split(END, 1)[0].strip()
        origin = "canonical current student lesson V3 marker block"
    else:
        text = DRAFT.read_text(encoding="utf-8-sig").strip()
        origin = "concept-lesson-v3.md review draft"
    if "Notes for me" in text or "teacher_note" in text:
        raise ValueError("Private material found in student lesson")
    return text, origin


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def route(nodes, label="Rule diagram"):
    return '<div class="route" role="group" aria-label="'+html.escape(label)+'">'+"<span class=\"arrow\" aria-hidden=\"true\">→</span>".join('<span class="node">'+inline(n)+'</span>' for n in nodes)+"</div>"


FACT_LAB = '''<section class="fact-lab" aria-label="Explore what a fact lets you conclude"><div class="lab-kicker">A little experiment</div><h2>Change the fact.</h2><p class="lab-rule">Every late application requires special approval.</p><label for="fact-choice">What do we know about this application?</label><select id="fact-choice"><option value="late">It was submitted late.</option><option value="notapproval">It does not require special approval.</option><option value="approval">It requires special approval.</option><option value="notlate">It was not submitted late.</option></select><div class="fact-display" aria-live="polite"><span class="eyebrow" id="fact-move">Apply forward</span><p id="fact-result">It requires special approval.</p><p id="fact-reason">The fact meets the rule's starting condition. The requirement follows.</p></div><p class="lab-foot">One rule. Four different facts. Two support a new conclusion.</p></section>'''

VISUALS = {
    "TWO-MOVES": '<figure class="two-moves"><div><span class="eyebrow">01 · Start at the condition</span>'+route(["Submitted late", "Requires approval"])+"<p>A late application cannot escape the approval requirement.</p></div><div><span class=\"eyebrow\">02 · Deny the required result</span>"+route(["Does not require approval", "Not submitted late"])+"<p>If the result is absent, the starting condition cannot hold.</p></div><figcaption>Two directions of reasoning. One unchanged policy.</figcaption></figure>",
    "CASE-GRID": '''<figure class="case-grid"><div class="case-heading"><span>Submitted late?</span><span>Requires approval?</span><span>Fits the rule?</span></div><div><span>Yes</span><span>Yes</span><b>Allowed</b></div><div class="impossible"><span>Yes</span><span>No</span><b>Ruled out</b></div><div><span>No</span><span>Yes</span><b>Allowed</b></div><div><span>No</span><span>No</span><b>Allowed</b></div><figcaption>A rule rules out a combination. It does not establish which allowed combination actually occurs.</figcaption></figure>''',
    "CHAIN-LAB": '<section class="chain-lab" aria-label="Explore which rule can link"><span class="lab-kicker">Match the middle</span><h3>Can these rules form a chain?</h3><div class="chain-first">'+route(["Submitted late", "Requires special approval"])+'''</div><label for="chain-choice">Choose the second rule</label><select id="chain-choice"><option value="match">Requires special approval → Needs a signature</option><option value="received">Has received special approval → Needs a signature</option><option value="shared">Submitted late → Needs a signature</option><option value="reversed">Needs a signature → Requires special approval</option></select><div id="chain-display" aria-live="polite"></div><p class="lab-foot">The destination of one rule must match the starting condition of the next.</p></section>''',
    "SHARED-TRIGGER": '<figure class="fork"><span class="fork-root">Submitted late</span><div class="fork-lines" aria-hidden="true">↙ &nbsp; ↘</div><div class="fork-results"><span>Requires approval</span><span>Needs a signature</span></div><figcaption>Both results follow for a late application. The diagram supplies no arrow between the results.</figcaption></figure>',
    "MODALITY": '''<figure class="word-contrast"><div><span class="eyebrow">What the rule says</span><strong>Should be inspected</strong><small>A claim about what ought to happen.</small></div><span class="not-equal" aria-label="does not mean">≠</span><div><span class="eyebrow">What an answer might add</span><strong>Has been inspected</strong><small>A claim about what actually happened.</small></div><figcaption>Dropping one word can change the whole condition.</figcaption></figure>''',
    "NEGATION": '''<figure class="negation"><div><span class="eyebrow">To fail an AND requirement</span><div class="logic-parts"><span>Not reviewed</span><b>OR</b><span>Not authorized</span></div><p>At least one required part is missing.</p></div><div><span class="eyebrow">To fail an OR requirement</span><div class="logic-parts"><span>No badge</span><b>AND</b><span>No invitation</span></div><p>Every permitted route is missing.</p></div><figcaption>Negate each part and switch the connector.</figcaption></figure>''',
}


class Renderer:
    def __init__(self):
        self.checks = 0
        self.practice = []

    def check(self, prompt, answer):
        self.checks += 1
        n = self.checks
        return f'''<aside class="check" data-check="{n}"><span class="eyebrow">Try it · {n:02}</span><p>{inline(prompt)}</p><form><label for="answer-{n}">Your answer and reasoning</label><textarea id="answer-{n}" rows="3" required placeholder="Write what follows, and why."></textarea><button type="submit">Compare with the worked answer <span aria-hidden="true">↗</span></button></form><div class="feedback" hidden tabindex="-1"><span class="eyebrow">Worked answer</span><p>{inline(answer)}</p><p class="small">Your response stays above. Compare the conclusion and the reasoning. This exercise does not automatically grade your writing.</p><button class="again" type="button">Edit my answer</button></div><noscript><p><strong>Worked answer:</strong> {inline(answer)}</p></noscript></aside>'''

    def prose(self, block):
        if block.startswith("|"):
            rows = [[v.strip() for v in line.strip().strip("|").split("|")] for line in block.splitlines()]
            rows = [r for r in rows if not all(re.fullmatch(r":?-+:?", v) for v in r)]
            return '<div class="table-scroll"><table><thead><tr>'+"".join('<th scope="col">'+inline(v)+"</th>" for v in rows[0])+"</tr></thead><tbody>"+"".join("<tr>"+"".join("<td>"+inline(v)+"</td>" for v in r)+"</tr>" for r in rows[1:])+"</tbody></table></div>"
        if block.startswith("**") and " -> " in block:
            label, value = block.split(":**", 1)
            nodes = value.strip().rstrip(".").split(" -> ")
            return '<div class="rule-line"><span class="eyebrow">'+inline(label.strip("*"))+"</span>"+route(nodes)+"</div>"
        return "<p>"+inline(block).replace("\n", " ")+"</p>"

    def render(self, source):
        blocks = re.split(r"\n\s*\n", source)
        title = blocks.pop(0).removeprefix("# ")
        opening = []
        while blocks and not blocks[0].startswith("## "):
            b = blocks.pop(0)
            if b == "<!-- FACT-LAB -->":
                continue
            opening.append(self.prose(b))
        body = '<header class="opening"><div class="opening-story">'+"".join(opening)+"</div>"+FACT_LAB+"</header>"
        body += '<nav class="jump" aria-label="Lesson sections"><a href="#section-1">Facts</a><a href="#section-2">Contrapositives</a><a href="#section-3">Linking</a><a href="#section-5">Whole ideas</a><a href="#section-8">Practice</a></nav>'
        section = False
        i = 0
        while i < len(blocks):
            b = blocks[i].strip()
            if b.startswith("## "):
                if section:
                    body += "</section>"
                number, heading = b[3:].split(" | ", 1)
                body += f'<section class="chapter" id="section-{int(number)}"><h2><span>{number}</span>'+inline(heading)+"</h2>"
                section = True
            elif b.startswith("### "):
                body += "<h3>"+inline(b[4:])+"</h3>"
            elif b.startswith("<!-- "):
                name = b.removeprefix("<!-- ").removesuffix(" -->")
                if name not in VISUALS:
                    raise ValueError("Unknown visual hook: "+name)
                body += VISUALS[name]
            elif i+1 < len(blocks) and blocks[i+1].startswith("**Worked answer:**"):
                answer = blocks[i+1].removeprefix("**Worked answer:**").strip()
                if b.startswith("**Practice "):
                    prompt = re.sub(r"^\*\*Practice \d+:\*\*\s*", "", b)
                    self.practice.append({"prompt": prompt, "answer": answer})
                    if len(self.practice) == 1:
                        body += '<section class="practice" id="mixed-practice" aria-label="Mixed practice"><div class="practice-head"><span class="eyebrow">Use the moves</span><span id="practice-count">1 of 4</span></div><h3>What follows?</h3><div class="practice-columns"><p id="practice-prompt"></p><form id="practice-form"><label for="practice-answer">Your conclusion and reasoning</label><textarea id="practice-answer" rows="5" required placeholder="Name the move. Explain what the statements guarantee."></textarea><button type="submit">Compare reasoning</button></form></div><div id="practice-feedback" hidden tabindex="-1"><span class="eyebrow">Worked answer</span><p id="practice-worked"></p><p class="small">Compare for yourself. There is no automatic grading of your explanation.</p></div><div class="practice-actions"><button type="button" id="practice-edit" hidden>Edit my answer</button><button type="button" id="practice-next" hidden>Next problem →</button></div></section>'
                    body += '<noscript><p>'+inline(prompt)+"</p><p><strong>Worked answer:</strong> "+inline(answer)+"</p></noscript>"
                else:
                    body += self.check(re.sub(r"^\*\*Try it:\*\*\s*", "", b), answer)
                i += 1
            elif b.startswith("**Worked answer:**"):
                raise ValueError("Unpaired answer")
            else:
                body += self.prose(b)
            i += 1
        if section:
            body += "</section>"
        return title, body


CSS = r'''
:root{--ink:#173047;--teal:#007f79;--paper:#fffdfa;--muted:#5e6f76;--line:#cadbd7;--pale:#edf5f2}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:18px/1.7 Georgia,"Times New Roman",serif}button,input,select,textarea{font:inherit}button,select{font-family:system-ui,sans-serif}button,a,select,textarea{outline-offset:5px}button{min-height:44px;border:0;border-radius:5px;padding:10px 17px;background:var(--teal);color:white;font-size:14px;font-weight:650;cursor:pointer}button:hover{background:#006963}a{color:var(--teal)}button:focus-visible,a:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid #bf780f}header.top{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding:18px max(24px,calc((100vw - 1120px)/2));font:13px system-ui,sans-serif;background:#fff}header.top b{font-size:19px;letter-spacing:-.5px}header.top span{color:var(--muted)}main{max-width:1080px;margin:auto;padding:52px 32px 80px}.dateline{font:12px system-ui,sans-serif;color:var(--muted);letter-spacing:1.8px;text-transform:uppercase}h1{font:700 clamp(34px,4.8vw,54px)/1.1 system-ui,sans-serif;letter-spacing:-2px;margin:18px 0 40px;max-width:850px}.opening{display:grid;grid-template-columns:1.08fr 1fr;gap:52px;align-items:start}.opening-story p:first-child{font-size:26px;line-height:1.4;margin-top:0}.opening-story p{font-size:18px}.opening-story strong{font-weight:700}.fact-lab{background:#edf3ee;padding:26px 28px 20px;border-radius:11px;box-shadow:0 3px 0 #d7e5dd}.lab-kicker,.eyebrow{font:600 11px/1.5 system-ui,sans-serif;text-transform:uppercase;letter-spacing:1.7px;color:var(--teal);display:block}.fact-lab h2{font:650 25px/1.2 system-ui,sans-serif;margin:12px 0}.lab-rule{font:19px/1.45 Georgia,serif;border-left:3px solid var(--teal);padding-left:14px}.fact-lab label,.chain-lab label,form label{font:600 13px/1.5 system-ui,sans-serif;display:block;margin:18px 0 8px}select{width:100%;padding:12px 10px;min-height:48px;border:1px solid #a1b9b1;background:#fff;color:var(--ink);font-size:14px;white-space:normal}.fact-display{padding:20px 0 5px}.fact-display #fact-result{font:650 21px/1.4 system-ui,sans-serif;margin:8px 0}.fact-display #fact-reason{font-size:16px;margin:8px 0}.lab-foot{font:12px/1.6 system-ui,sans-serif;color:var(--muted);border-top:1px solid var(--line);padding-top:14px;margin-bottom:0}.jump{display:flex;gap:22px;flex-wrap:wrap;padding:22px 0;margin:34px 0 5px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);font:13px system-ui,sans-serif}.jump a{text-decoration:none;padding:5px 0}.chapter{max-width:720px;margin:75px auto 0;scroll-margin-top:25px}.chapter h2{font:650 27px/1.3 system-ui,sans-serif;letter-spacing:-.6px;margin:0 0 30px;display:flex;gap:18px;align-items:baseline}.chapter h2>span{font:13px ui-monospace,monospace;color:var(--teal);letter-spacing:0;flex:0 0 24px}.chapter h3{font:650 21px/1.4 system-ui,sans-serif;margin:40px 0 16px}.chapter p{margin:19px 0}code{font:15px ui-monospace,monospace;background:#edf3ee;padding:3px 5px;white-space:normal}strong{font-weight:700}figure{margin:30px 0 38px}figcaption{font:12px/1.6 system-ui,sans-serif;color:var(--muted);margin-top:14px}.rule-line{margin:24px 0}.route{display:flex;align-items:center;gap:12px;margin-top:12px}.node{background:#e9f1ed;border-bottom:2px solid #78aca0;flex:1;padding:15px 14px;font:600 15px/1.5 system-ui,sans-serif;text-align:center}.arrow{font:26px system-ui,sans-serif;color:var(--teal)}.two-moves{border-top:2px solid var(--teal);padding-top:24px}.two-moves>div+div{margin-top:30px}.two-moves p{font-size:16px}.case-grid{font:14px system-ui,sans-serif}.case-grid>div{display:grid;grid-template-columns:1fr 1.1fr .8fr;border-bottom:1px solid var(--line);gap:12px;padding:16px}.case-grid .case-heading{font-size:12px;font-weight:650;background:var(--pale)}.case-grid .impossible{background:#fcf0e7;color:#8b4424}.case-grid b{font-weight:600}.chain-lab{background:#edf5f2;padding:28px;border-radius:10px;margin:35px -25px}.chain-lab h3{margin:10px 0 20px}.chain-lab #chain-display{padding-top:20px}.chain-lab #chain-display strong{font-family:system-ui,sans-serif;font-size:17px}.chain-lab #chain-display p{font-size:16px}.chain-first .node{background:#fff}.fork{text-align:center;padding:26px 20px 20px;background:#f3f0f7}.fork-root{display:inline-block;background:#fff;padding:15px 30px;font:650 16px system-ui,sans-serif}.fork-lines{font-size:35px;color:#7d6594;letter-spacing:80px;margin-left:80px;line-height:1.6}.fork-results{display:flex;gap:28px;justify-content:center}.fork-results span{padding:15px;background:#fff;font:600 14px/1.5 system-ui,sans-serif;flex:1}.word-contrast{display:grid;grid-template-columns:1fr 35px 1fr;align-items:center;gap:18px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:28px 0}.word-contrast strong{display:block;font:650 20px/1.5 system-ui,sans-serif;margin:12px 0}.word-contrast small{font-size:15px;line-height:1.5;display:block}.not-equal{font-size:32px;color:#946144}.word-contrast figcaption{grid-column:1/-1}.negation>div{padding:22px 0;border-top:1px solid var(--line)}.logic-parts{display:flex;align-items:center;gap:15px;margin-top:16px;font:15px/1.5 system-ui,sans-serif}.logic-parts span{padding:13px;background:#f0eee3;flex:1;text-align:center}.logic-parts b{color:#906323}.negation p{font-size:16px}.check{background:#edf5f2;border-left:3px solid #75b4a8;padding:24px 27px;margin:35px 0 42px}.check p{font-size:17px;line-height:1.65}.check form label{margin-top:20px}textarea{display:block;width:100%;background:#fff;border:1px solid #a6bbb5;border-radius:4px;padding:12px;color:var(--ink);resize:vertical;font:16px/1.5 system-ui,sans-serif;min-height:88px}.check form button{margin-top:13px}.feedback{margin-top:24px;border-top:1px solid var(--line);padding-top:20px}.small{font:12px/1.6 system-ui,sans-serif!important;color:var(--muted)}.again{background:transparent;color:var(--teal);border:1px solid #91b9ac}.table-scroll{overflow-x:auto;margin:30px 0}table{width:100%;border-collapse:collapse;font:14px/1.6 system-ui,sans-serif}th,td{text-align:left;padding:16px 12px;border-bottom:1px solid var(--line);vertical-align:top}th{background:var(--pale);font-size:12px}.practice{background:#193b40;color:#f7fbf9;padding:30px;margin:35px -55px;border-radius:10px}.practice-head{display:flex;justify-content:space-between;align-items:center}.practice .eyebrow{color:#a2d7c5}.practice #practice-count{font:12px system-ui,sans-serif;color:#b9d9ce}.practice h3{margin:12px 0 24px;font-size:27px}.practice-columns{display:grid;grid-template-columns:1fr 1fr;gap:32px}.practice #practice-prompt{font-size:21px;line-height:1.55;margin-top:0}.practice form label{margin-top:0;color:#d9eee4}.practice form button{margin-top:14px;background:#b8e2d1;color:#173e36}.practice textarea{background:#fffdfa}.practice #practice-feedback{border-top:1px solid #547873;margin-top:25px;padding-top:20px}.practice .small{color:#c5ded3}.practice-actions{display:flex;justify-content:flex-end;gap:12px;margin-top:20px;flex-wrap:wrap}.practice-actions button{background:transparent;border:1px solid #8db8a9;color:#dff5eb}footer{max-width:720px;margin:65px auto 0;padding-top:24px;border-top:1px solid var(--line);font:13px system-ui,sans-serif;color:var(--muted)}[hidden]{display:none!important}
@media(max-width:850px){.opening{grid-template-columns:1fr;gap:24px}.fact-lab{max-width:620px}.opening-story{max-width:680px}.practice{margin-left:0;margin-right:0}.chain-lab{margin-left:0;margin-right:0}.chapter{margin-top:58px}}@media(max-width:600px){main{padding:32px 20px 60px}h1{letter-spacing:-1px;margin-bottom:30px}.opening-story p:first-child{font-size:23px}.fact-lab{padding:23px 20px}.jump{gap:15px;margin-top:30px}.chapter h2{font-size:23px;gap:10px}.chapter h2>span{flex-basis:22px}.route{gap:7px}.node{padding:12px 8px;font-size:13px}.arrow{font-size:21px}.chain-lab{padding:22px 16px}.case-grid>div{padding:14px 7px;gap:8px;font-size:13px}.case-grid .case-heading{font-size:11px}.fork{padding:23px 14px}.fork-results{gap:12px}.fork-results span{padding:12px 7px;font-size:13px}.word-contrast{gap:10px;grid-template-columns:1fr 24px 1fr}.word-contrast strong{font-size:17px}.word-contrast small{font-size:14px}.logic-parts{gap:8px;font-size:13px}.check{padding:21px 18px}.check button{width:100%}.practice{padding:24px 20px}.practice-columns{grid-template-columns:1fr;gap:20px}.practice #practice-prompt{font-size:20px}header.top{padding:17px 20px}header.top span{font-size:11px}.table-scroll table{min-width:540px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{transition:none!important;animation:none!important}}
'''

JS = r'''
const factCases={late:['Apply forward','It requires special approval.',"The fact meets the rule's starting condition. The requirement follows."],notapproval:['Use the contrapositive','It was not submitted late.',"A late application would require approval. Because that requirement is absent, lateness is ruled out."],approval:['Keep the other side open','Whether it was late is unknown.',"An on-time application could require approval for another reason. Requiring approval does not prove lateness."],notlate:['Keep the other side open','Whether it requires approval is unknown.',"The rule covers late applications. It leaves open what requirements an on-time application may have."]};
function factUpdate(){const c=factCases[document.querySelector('#fact-choice').value];document.querySelector('#fact-move').textContent=c[0];document.querySelector('#fact-result').textContent=c[1];document.querySelector('#fact-reason').textContent=c[2]}
document.querySelector('#fact-choice').addEventListener('change',factUpdate);
const chainCases={match:['The middle matches.','Submitted late → Requires special approval → Needs a signature','The first result meets the second starting condition. A late application needs a signature.'],received:['The whole ideas differ.','Requires approval ≠ Has received approval','A requirement can be unfulfilled. The rules do not prove that a late application has received approval or has a signature.'],shared:['Two results share a starting point.','Late → Requires approval; Late → Needs a signature','A known late application has both requirements. But requiring approval alone does not establish that it needs a signature. There is no link from one result to the other.'],reversed:['Both rules point into the middle.','Late → Requires approval ← Needs a signature','Requiring approval does not tell you which starting condition applies. An application could require approval while being on time and not needing a signature.']};
function chainUpdate(){const c=chainCases[document.querySelector('#chain-choice').value];const box=document.querySelector('#chain-display');box.replaceChildren();const strong=document.createElement('strong');strong.textContent=c[0];const line=document.createElement('p');line.className='chain-conclusion';line.textContent=c[1];const reason=document.createElement('p');reason.textContent=c[2];box.append(strong,line,reason)}document.querySelector('#chain-choice').addEventListener('change',chainUpdate);chainUpdate();
document.querySelectorAll('.check').forEach(card=>{const form=card.querySelector('form'),feedback=card.querySelector('.feedback'),text=card.querySelector('textarea');form.addEventListener('submit',e=>{e.preventDefault();if(!text.value.trim()){text.focus();return}feedback.hidden=false;feedback.focus();});card.querySelector('.again').addEventListener('click',()=>{feedback.hidden=true;text.focus()});});
let practiceIndex=0;const responses=practice.map(()=>''),seen=new Set();const answer=document.querySelector('#practice-answer'),form=document.querySelector('#practice-form'),feedback=document.querySelector('#practice-feedback'),next=document.querySelector('#practice-next'),edit=document.querySelector('#practice-edit');
function showPractice(){document.querySelector('#practice-count').textContent=`${practiceIndex+1} of ${practice.length}`;document.querySelector('#practice-prompt').textContent=practice[practiceIndex].prompt;answer.value=responses[practiceIndex];document.querySelector('#practice-worked').textContent=practice[practiceIndex].answer;feedback.hidden=true;next.hidden=true;edit.hidden=true;next.textContent=practiceIndex===practice.length-1?'Start again ↺':'Next problem →';}
form.addEventListener('submit',e=>{e.preventDefault();if(!answer.value.trim()){answer.focus();return}responses[practiceIndex]=answer.value;seen.add(practiceIndex);feedback.hidden=false;next.hidden=false;edit.hidden=false;feedback.focus();if(practiceIndex===practice.length-1)document.querySelector('#practice-count').textContent=`${seen.size} of ${practice.length} comparisons completed`;});edit.addEventListener('click',()=>{feedback.hidden=true;answer.focus()});next.addEventListener('click',()=>{responses[practiceIndex]=answer.value;practiceIndex=(practiceIndex+1)%practice.length;showPractice();document.querySelector('#practice-prompt').scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'});answer.focus({preventScroll:true})});showPractice();
'''


def main():
    text, origin = source_text()
    renderer = Renderer()
    title, body = renderer.render(text)
    if renderer.checks != 6 or len(renderer.practice) != 4:
        raise ValueError("Expected six integrated checks and four mixed problems")
    data = json.dumps(renderer.practice, ensure_ascii=False).replace("<", "\\u003c")
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="lsatu-interactive-lesson" content="yahunatan-2026-09-16-conditional-reasoning"><title>{html.escape(title)} | LSAT U</title><style>{CSS}</style></head><body><header class="top"><b>LSAT U</b><span>Classroom · Notes and recaps</span></header><main><div class="dateline">Conditional reasoning · Concept lesson</div><h1>{html.escape(title)}</h1>{body}<footer>Start with what is given. Keep the whole idea. Follow only the direction the rule supports.</footer></main><script>const practice={data};{JS}</script></body></html>'''
    if len(page.encode("utf-8")) >= 500_000:
        raise ValueError("Lesson exceeds 500KB")
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"{OUTPUT}\nSource: {origin}\nChecks: {renderer.checks}; mixed practice: {len(renderer.practice)}; bytes: {len(page.encode('utf-8'))}")


if __name__ == "__main__":
    main()
