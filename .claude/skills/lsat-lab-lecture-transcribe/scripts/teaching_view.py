"""Render a private, one-moment-at-a-time teaching cue sheet."""
import base64
import html
import json
import mimetypes
from pathlib import Path


def prepare_steps(lesson, manifest, output):
    sections = {segment["id"]: segment for segment in manifest["segments"]}
    questions = {}
    for question in lesson.get("question_bank", []):
        identifier = question.get("id", question.get("question_id"))
        if not identifier or identifier in questions:
            raise ValueError("Question bank needs unique IDs")
        choices = question.get("choices", {})
        if isinstance(choices, list):
            choices = {choice["label"]: choice["text"] for choice in choices}
        if set(choices) != set("ABCDE") or not question.get("stimulus") or not question.get("stem"):
            raise ValueError(f"Question {identifier} needs stimulus, stem and all five choices")
        questions[identifier] = {**question, "choices": choices}
    cards, assets, ids = [], {}, set()
    for item in lesson.get("steps", []):
        identifier = item["id"]
        if identifier in ids or item["section_id"] not in sections:
            raise ValueError(f"Duplicate step or unknown section: {identifier}")
        ids.add(identifier)
        kind = item["type"]
        if kind not in {"say", "ask", "wait", "expected", "board", "question"}:
            raise ValueError(f"Invalid teaching step: {identifier}")
        step = dict(item)
        if kind != "question" and not str(step.get("text", "")).strip():
            raise ValueError(f"Empty teaching step: {identifier}")
        if kind == "say" and len(step["text"].split()) > 100:
            raise ValueError(f"SAY step exceeds 100 words; split it into short teaching moments: {identifier}")
        if step.get("question_id"):
            if step["question_id"] not in questions:
                raise ValueError(f"Unresolved question: {identifier}")
            step["question"] = questions[step["question_id"]]
        if kind == "question" and "question" not in step:
            raise ValueError(f"Question step needs a question-bank entry: {identifier}")
        image = step.get("image_path")
        if not image and kind == "question":
            image = step["question"].get("source_image", step["question"].get("image_path"))
        if not image and kind == "ask" and step.get("question_id"):
            image = step["question"].get("source_image", step["question"].get("image_path"))
        if image:
            path = (output / image).resolve()
            if not path.is_relative_to((output / "screenshots").resolve()) or not path.is_file():
                raise ValueError(f"Missing or misplaced teaching image: {image}")
            data = path.read_bytes()
            assets[Path(image).as_posix()] = data
            mime = mimetypes.guess_type(image)[0] or "image/png"
            step["image"] = f"data:{mime};base64,{base64.b64encode(data).decode('ascii')}"
        work_boundary = cards and kind == "ask" and any(entry["type"] == "wait" and entry.get("duration_seconds") for entry in cards[-1])
        if kind in {"ask", "wait", "expected"} and cards and not work_boundary and cards[-1][0]["section_id"] == step["section_id"]:
            cards[-1].append(step)
        else:
            cards.append([step])
    if not cards:
        raise ValueError("No teaching moments supplied")
    expected_questions = {segment["question_id"] for segment in manifest["segments"] if segment["kind"] == "question"}
    shown_questions = {step.get("question_id") for card in cards for step in card if step["type"] == "question"}
    if not expected_questions <= shown_questions:
        raise ValueError("Every worked question needs its complete question teaching card")
    for section_id, section in sections.items():
        source = " ".join(section["script"].split())
        for correction in lesson.get("voice_replacements", []):
            source = source.replace(" ".join(correction["old"].split()), " ".join(correction["new"].split()))
        spoken = " ".join(" ".join(step["text"].split()) for card in cards for step in card if step["type"] == "say" and step["section_id"] == section_id)
        if source not in spoken:
            raise ValueError(f"Teaching moments do not preserve the complete script for {section_id}")
    return cards, assets


STYLE = """*{box-sizing:border-box}body{margin:0;background:#f2f1ed;color:#17313b;font-family:system-ui,sans-serif}header{padding:18px 28px;background:#fff;border-bottom:1px solid #d1d8d6}h1{font-size:22px;margin:0 0 12px}.bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap}button,select,input{font:16px system-ui}button{padding:10px 15px;border:1px solid #a5b4b5;border-radius:6px;background:white;color:#17313b;cursor:pointer}button:hover{background:#e9f0ee}button:disabled{opacity:.45;cursor:default}select{padding:10px;max-width:100%}a{color:#175873}main{max-width:1240px;margin:auto;padding:28px}.moment{background:#fff;border:1px solid #d5ddda;border-radius:12px;padding:28px;min-height:400px}.eyebrow{font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:.09em;color:#59747b;margin:0 0 10px}.moment h2{font-size:20px;margin:0 0 22px;color:#4b656c}.block{padding:20px 0;border-top:1px solid #e3e8e6}.block:first-of-type{border-top:0}.labelrow{display:flex;justify-content:space-between;align-items:center;gap:15px;margin-bottom:12px}.label{font-size:14px;font-weight:800;letter-spacing:.08em}.spoken{font-family:Georgia,serif;font-size:var(--sayfont,30px);line-height:1.7;max-width:30em;white-space:pre-line}.ask{background:#edf6f2;padding:20px;border-radius:8px}.ask .spoken{font-size:24px}.wait{background:#fff6dd;border-left:4px solid #ba9543;padding:15px;margin-top:16px;line-height:1.6}.expected{margin-top:20px}.expected div{font:18px/1.7 system-ui;padding:16px;background:#edf0f6;white-space:pre-wrap}.board{font:24px/1.7 ui-monospace,Consolas,monospace;white-space:pre-wrap;background:#f5f7f5;border:1px solid #d9e2de;padding:24px;overflow:auto}.question{font:20px/1.7 Georgia,serif;white-space:pre-wrap}.choices{list-style:none;padding:0;margin:20px 0}.choices li{margin:14px 0}.withimage{display:grid;grid-template-columns:1.15fr 1fr;gap:26px;align-items:start}.frame img{width:100%;cursor:zoom-in;border:1px solid #cdd7d3}.frame p{font-size:14px;color:#5e7278}.bottom{display:flex;justify-content:space-between;align-items:center;margin-top:22px;gap:15px}#next{background:#173d47;color:white;min-width:130px}#status{font-size:14px;min-height:22px;color:#48666b;margin-top:15px}dialog{width:94vw;max-width:1800px;border:0;padding:24px;border-radius:12px}dialog::backdrop{background:#0009}dialog img{width:100%}#prep{max-width:900px;max-height:85vh;overflow:auto;font:18px/1.7 system-ui}.private{font-size:13px;color:#687b7e}#fallback{width:100%;min-height:180px;font:17px/1.6 ui-monospace} [hidden]{display:none!important}@media(max-width:850px){main{padding:15px}.moment{padding:22px}.withimage{display:block}.frame{margin-top:20px}.spoken{font-size:26px}header{padding:18px}.bar label{font-size:14px}.question{font-size:19px}}"""

SCRIPT = """const data=JSON.parse(document.querySelector('#lesson-data').textContent);const cards=data.cards,select=document.querySelector('#sections'),holder=document.querySelector('#card'),counter=document.querySelector('#count'),prev=document.querySelector('#prev'),next=document.querySelector('#next'),status=document.querySelector('#status');let current=0;const textNode=(tag,text,cls)=>{const n=document.createElement(tag);n.textContent=text;if(cls)n.className=cls;return n;};function questionText(q){return q.stimulus+'\\n\\n'+q.stem+'\\n\\n'+Object.entries(q.choices).map(([key,value])=>key+'. '+value).join('\\n\\n');}async function copyText(text,label){try{if(!navigator.clipboard)throw Error('clipboard unavailable');await navigator.clipboard.writeText(text);status.textContent=label+' copied. Paste it into your live board or notes.';}catch(error){const fallback=document.querySelector('#copy-fallback'),area=document.querySelector('#fallback');area.value=text;fallback.showModal();area.focus();area.select();status.textContent='Clipboard access unavailable. Text selected: press Ctrl+C or Command+C.';}}function copyButton(text,label){const b=textNode('button','Copy '+label);b.type='button';b.onclick=()=>copyText(text,label);return b;}function showImage(step,parent){if(!step.image)return;const frame=document.createElement('div');frame.className='frame';const image=document.createElement('img');image.src=step.image;image.alt=step.title||'Original lecture frame';image.onclick=()=>{const zoom=document.querySelector('#zoom');zoom.querySelector('img').src=step.image;zoom.querySelector('img').alt=image.alt;zoom.showModal();};frame.append(image,textNode('p','Original source frame. Click to enlarge.'));parent.append(frame);}function render(){holder.replaceChildren();const items=cards[current],first=items[0];holder.append(textNode('p',data.sections[first.section_id].label,'eyebrow'),textNode('h2',first.title||'Teaching moment'));select.value=first.section_id;counter.textContent='Step '+(current+1)+' of '+cards.length;prev.disabled=current===0;next.disabled=current===cards.length-1;status.textContent='';for(const step of items){if(step.type==='expected'){const d=document.createElement('details');d.className='expected';d.append(textNode('summary','Reveal EXPECTED RESPONSE (teacher only)'),textNode('div',step.text));holder.append(d);continue;}if(step.type==='wait'){holder.append(textNode('div','WAIT · '+step.text,'wait'));continue;}const block=document.createElement('div');block.className='block '+(step.type==='ask'?'ask':'');const labelrow=document.createElement('div');labelrow.className='labelrow';labelrow.append(textNode('span',step.type.toUpperCase()+(step.type==='board'?' · COPY TO LIVE WHITEBOARD':step.type==='question'?' · ORIGINAL QUESTION':''),'label'));const payload=step.type==='question'?questionText(step.question):step.text;labelrow.append(copyButton(payload,step.type.toUpperCase()));block.append(labelrow);const content=document.createElement('div');if(step.image)content.className='withimage';const left=document.createElement('div');if(step.type==='question'){left.append(textNode('div',step.question.stimulus,'question'),textNode('div',step.question.stem,'question'));const choices=document.createElement('ul');choices.className='choices question';for(const [key,value] of Object.entries(step.question.choices)){choices.append(textNode('li',key+'. '+value));}left.append(choices);}else{left.append(textNode(step.type==='board'?'pre':'div',step.text,step.type==='board'?'board':'spoken'));}content.append(left);showImage(step,content);block.append(content);holder.append(block);}document.title=data.title+' · Step '+(current+1);window.scrollTo({top:0,behavior:'instant'});}function move(amount){current=Math.max(0,Math.min(cards.length-1,current+amount));render();}prev.onclick=()=>move(-1);next.onclick=()=>move(1);select.onchange=()=>{current=cards.findIndex(card=>card[0].section_id===select.value);render();};document.querySelector('#font').oninput=event=>document.documentElement.style.setProperty('--sayfont',event.target.value+'px');document.querySelector('#brief').onclick=()=>document.querySelector('#prep').showModal();document.querySelectorAll('[data-close]').forEach(button=>button.onclick=()=>button.closest('dialog').close());document.addEventListener('keydown',event=>{if(document.querySelector('dialog[open]')||event.target.isContentEditable||['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName))return;if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();move(event.key==='ArrowRight'?1:-1);}});for(const [id,section] of Object.entries(data.sections)){const option=textNode('option',section.label);option.value=id;select.append(option);}const hash=location.hash.match(/^#segment-(\\d+)$/);if(hash){const key=Object.keys(data.sections)[Number(hash[1])-1];const index=cards.findIndex(card=>card[0].section_id===key);if(index>=0)current=index;}render();"""


PACING_SCRIPT = """const timers={};let automatic=null;function timerBlock(step){const box=document.createElement('div');box.className='wait';box.append(textNode('div','WAIT · '+step.text));if(!step.duration_seconds)return box;const timer=timers[step.id]||(timers[step.id]={remaining:step.duration_seconds,running:false,duration:step.duration_seconds});const controls=document.createElement('div');controls.className='bar';controls.style.marginTop='12px';const label=textNode('label','Seconds ');const input=document.createElement('input');input.type='number';input.min='10';input.max='3600';input.value=timer.duration;input.style.width='90px';input.setAttribute('aria-label','Student work timer seconds');label.append(input);const clock=textNode('strong','');clock.dataset.timer=step.id;const run=textNode('button',timer.running?'Pause timer':'Start timer');run.onclick=()=>{timer.running=!timer.running;run.textContent=timer.running?'Pause timer':'Start timer';};const reset=textNode('button','Reset');reset.onclick=()=>{timer.running=false;timer.remaining=timer.duration;render();};input.onchange=()=>{timer.duration=Math.max(10,Math.min(3600,Number(input.value)||120));timer.remaining=timer.duration;timer.running=false;render();};const done=textNode('button','Student ready: continue');done.onclick=()=>move(1);controls.append(label,clock,run,reset,done);box.append(controls,textNode('p','Suggested teacher pacing, not a timestamp from the source. The timer never advances the lesson.'));return box;}setInterval(()=>{for(const [id,timer] of Object.entries(timers)){if(timer.running&&timer.remaining>0)timer.remaining--;if(timer.remaining===0)timer.running=false;const clock=document.querySelector('[data-timer="'+id+'"]');if(clock)clock.textContent=String(Math.floor(timer.remaining/60)).padStart(2,'0')+':'+String(timer.remaining%60).padStart(2,'0')+(timer.remaining===0?' · Continue when the student is ready':'');}},1000);function scheduleAuto(items){clearTimeout(automatic);const enabled=document.querySelector('#autopace').checked;if(!enabled)return;if(items.some(s=>s.type!=='say')){status.textContent='Auto-read paused for teacher/student interaction. Advance when ready.';return;}const words=items.reduce((total,s)=>total+s.text.split(/\\s+/).length,0),wpm=Number(document.querySelector('#wpm').value)||140;automatic=setTimeout(()=>{if(current<cards.length-1)move(1);},Math.max(4000,words/wpm*60000));status.textContent='Auto-read SAY pacing active. It stops at every question, board, ask, or wait.';}document.querySelector('#autopace').onchange=()=>scheduleAuto(cards[current]);document.querySelector('#wpm').onchange=()=>scheduleAuto(cards[current]);"""


def render(lesson, manifest, output, brief_html):
    cards, assets = prepare_steps(lesson, manifest, output)
    sections = {segment["id"]: {"label": segment.get("nav_label", segment["title"])} for segment in manifest["segments"]}
    data = json.dumps({"title": manifest["title"], "cards": cards, "sections": sections}, ensure_ascii=False).replace("<", "\\u003c")
    e = html.escape
    script = SCRIPT.replace("holder.append(textNode('div','WAIT · '+step.text,'wait'));", "holder.append(timerBlock(step));")
    script = script.replace("left.append(choices);", "left.append(choices);const questionDetails=document.createElement('details');questionDetails.append(textNode('summary','Read original question'));questionDetails.append(...Array.from(left.childNodes));left.append(questionDetails);")
    script = script.replace("frame.append(image,textNode('p','Original source frame. Click to enlarge.'));", "if(step.type==='question'){const view=textNode('button','View question image');view.onclick=image.onclick;frame.append(view);}else{frame.append(image,textNode('p','Original source frame. Click to enlarge.'));}")
    script = script.replace("block.append(labelrow);const content=", "block.append(labelrow);if(step.type==='question'&&step.spoken_intro){block.append(textNode('div',step.spoken_intro,'spoken'));}const content=")
    script = script.replace("window.scrollTo({top:0,behavior:'instant'});", "scheduleAuto(items);window.scrollTo({top:0,behavior:'instant'});")
    script = script.replace("function move(amount){", "function move(amount){Object.values(timers).forEach(timer=>timer.running=false);")
    document = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(manifest['title'])}: teaching view</title><style>{STYLE}</style><header><h1>{e(manifest['title'])} · Teaching view</h1><div class="bar"><label>Section <select id="sections" aria-label="Choose lecture section"></select></label><button id="brief">Before teaching</button><a href="full-script.html">Continuous script</a><details><summary>Reading settings</summary><label>Text size <input id="font" type="range" min="24" max="44" value="30" aria-label="Spoken text size"></label><label><input id="autopace" type="checkbox"> Auto-read SAY only</label><label>Words/min <input id="wpm" type="number" min="80" max="240" value="140" style="width:80px"></label></details></div><p class="private">Private teacher cue sheet. SAY and ASK are spoken; WAIT, EXPECT and BOARD are instructions for you. Advance manually.</p></header><main><article id="card" class="moment"></article><div class="bottom"><button id="prev">Previous</button><span id="count" aria-live="polite"></span><button id="next">Next step</button></div><div id="status" role="status"></div></main><dialog id="prep"><button data-close>Close preparation</button>{brief_html}</dialog><dialog id="zoom"><button data-close>Close full-size image</button><img alt=""></dialog><dialog id="copy-fallback"><button data-close>Close</button><p>Text is selected. Press Ctrl+C or Command+C, then paste into your live board.</p><textarea id="fallback" aria-label="Text to copy" readonly></textarea></dialog><script type="application/json" id="lesson-data">{data}</script><script>{PACING_SCRIPT}{script}</script></html>'''
    return document, assets, len(cards)
