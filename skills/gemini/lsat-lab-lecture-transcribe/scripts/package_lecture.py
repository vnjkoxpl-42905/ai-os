"""Package already captured lecture material. No browser or network access."""
import argparse
import base64
import hashlib
import html
import importlib.util
import json
import mimetypes
import re
from pathlib import Path


def stamp(value):
    seconds = int(value)
    return f"{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def render_brief(text):
    """Render the limited headings, paragraphs, lists and local links used by briefs."""
    blocks = []
    for paragraph in text.split("\n\n"):
        paragraph = html.escape(paragraph.strip())
        paragraph = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda match: f'<a href="{match[2]}">{match[1]}</a>' if not re.match(r"(?:javascript|data):", match[2], re.I) else match[1], paragraph)
        if paragraph.startswith("## "):
            blocks.append("<h3>"+paragraph[3:]+"</h3>")
        elif paragraph.startswith("# "):
            blocks.append("<h2>"+paragraph[2:]+"</h2>")
        elif re.match(r"\d+\. ", paragraph):
            blocks.append("<ol>"+"".join("<li>"+re.sub(r"^\d+\. ", "", line)+"</li>" for line in paragraph.splitlines())+"</ol>")
        else:
            blocks.append("<p>"+paragraph.replace("\n", " ")+"</p>")
    return "".join(blocks)


def validate(manifest, transcript, output):
    for key in ("title", "source_url", "duration_seconds", "transcript_method", "capture_date", "source_complete"):
        if key not in manifest:
            raise ValueError(f"Missing manifest field: {key}")
    if not isinstance(manifest["source_complete"], bool):
        raise ValueError("source_complete must be a boolean")
    duration = manifest["duration_seconds"]
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError("Invalid lecture duration")
    segments = manifest.get("segments", [])
    if not segments:
        raise ValueError("No captured script segments")
    lines = len(transcript.decode("utf-8-sig").splitlines())
    ids, questions, pictured = set(), set(), set()
    previous_end, initial_board = 0, False
    assets = {}
    for segment in segments:
        identifier = segment["id"]
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise ValueError("Segment IDs must be unique nonempty strings")
        ids.add(identifier)
        start, end = segment["start_seconds"], segment["end_seconds"]
        if not 0 <= previous_end <= start < end <= duration:
            raise ValueError(f"Invalid/overlapping source times: {identifier}")
        previous_end = end
        first_line, last_line = segment["source_lines"]
        if not 1 <= first_line <= last_line <= lines:
            raise ValueError(f"Invalid transcript line range: {identifier}")
        if not segment.get("script", "").strip():
            raise ValueError(f"Empty spoken script: {identifier}")
        if segment["kind"] not in {"concept", "question", "closing"}:
            raise ValueError(f"Invalid segment kind: {identifier}")
        if segment["kind"] == "question":
            question = segment.get("question_id")
            if not question or not initial_board:
                raise ValueError("Questions need question_id and an earlier introductory concept board")
            questions.add(question)
        for frame in segment.get("images", []):
            relative = Path(frame["path"])
            path = (output / relative).resolve()
            if relative.is_absolute() or not path.is_relative_to((output / "screenshots").resolve()):
                raise ValueError(f"Image must stay beneath screenshots/: {relative}")
            if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"} or not path.is_file():
                raise ValueError(f"Missing or unsupported image: {relative}")
            if not start <= frame["at_seconds"] <= end:
                raise ValueError(f"Image time outside segment: {relative}")
            if frame["kind"] not in {"concept_board", "question", "annotated_board"}:
                raise ValueError(f"Invalid image kind: {relative}")
            if frame["kind"] == "concept_board" and segment["kind"] == "concept":
                initial_board = True
            if frame["kind"] == "question" and segment["kind"] == "question":
                pictured.add(segment["question_id"])
            assets[relative.as_posix()] = path.read_bytes()
    if questions != pictured:
        raise ValueError(f"Question screenshots missing: {sorted(questions - pictured)}")
    if not initial_board:
        raise ValueError("Initial concept board is missing")
    for point in manifest.get("teaching_points", []):
        if not point.get("segment_ids") or not set(point["segment_ids"]) <= ids:
            raise ValueError(f"Unmapped teaching point: {point.get('id')}")
    if manifest["source_complete"] and manifest.get("gaps"):
        raise ValueError("A complete source cannot have unresolved gaps")
    return assets


STYLE = """body{margin:0;background:#f7f4ed;color:#172d35;font-family:Georgia,serif}header{position:sticky;top:0;background:#fff;padding:12px 24px;z-index:2;border-bottom:1px solid #c8d0ce}nav{display:flex;gap:12px;overflow:auto;font:16px system-ui}button,input,label{font:16px system-ui}main{max-width:1120px;margin:auto;padding:32px 24px 65vh}section{padding:24px 0;scroll-margin-top:150px;border-bottom:1px solid #c8d0ce}.spoken{font-size:30px;line-height:1.65;white-space:pre-wrap}.cue,figcaption{font:16px/1.5 system-ui;color:#4b6068}.cue{border-left:3px solid #738f94;padding:10px;background:#eaf0ef}figure{margin:18px 0}img{width:100%;height:auto}h1{font-size:26px}h2{font-size:24px}a{color:#185a73}.controls{display:flex;gap:14px;flex-wrap:wrap;margin:10px 0} @media(min-width:950px){.reading{display:grid;grid-template-columns:1.1fr 1fr;gap:26px}.visuals{position:sticky;top:155px;align-self:start}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}"""
CONTROLS = """const button=document.querySelector('#run'),speed=document.querySelector('#speed'),status=document.querySelector('#status');let active=false,last=0;const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;status.textContent=reduce?'Reduced motion: use manual scrolling.':'Space: start/pause. Left/right: previous/next section.';function stop(){active=false;button.textContent='Start';}button.onclick=()=>{if(reduce){status.textContent='Reduced motion: use manual scrolling.';return;}active=!active;last=0;button.textContent=active?'Pause':'Start';};function tick(time){if(active){if(last)scrollBy(0,(time-last)*Number(speed.value)/1000);last=time;if(innerHeight+scrollY>=document.documentElement.scrollHeight-2)stop();}requestAnimationFrame(tick);}requestAnimationFrame(tick);document.addEventListener('keydown',event=>{if(['INPUT','BUTTON','TEXTAREA','SELECT','A'].includes(event.target.tagName))return;if(event.code==='Space'){event.preventDefault();button.click();}if(event.code==='ArrowRight'||event.code==='ArrowLeft'){event.preventDefault();stop();const sections=[...document.querySelectorAll('section')];let current=0;sections.forEach((s,i)=>{if(s.getBoundingClientRect().top<=170)current=i;});const next=Math.max(0,Math.min(sections.length-1,current+(event.code==='ArrowRight'?1:-1)));sections[next].scrollIntoView({behavior:'auto'});}});document.querySelector('nav').addEventListener('click',stop);"""


def package(manifest_path, transcript_path, output):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    transcript = transcript_path.read_bytes()
    assets = validate(manifest, transcript, output)
    source = output / "transcript.md"
    if source.exists() and source.read_bytes() != transcript:
        raise ValueError("Preserved transcript differs; refusing to overwrite source")
    hashes = output / "SHA256SUMS"
    preserved_assets = {}
    if hashes.exists():
        for record in hashes.read_text(encoding="utf-8").splitlines():
            old_hash, name = record.split("  ", 1)
            if name == "transcript.md" or name.startswith("screenshots/"):
                current = output / name
                if not current.is_file() or digest(current.read_bytes()) != old_hash:
                    raise ValueError(f"Preserved source changed: {name}")
                if name.startswith("screenshots/"):
                    preserved_assets[name] = current.read_bytes()
    e = html.escape
    title = manifest["title"]
    state = "Source marked complete; review verification notes." if manifest["source_complete"] else "INCOMPLETE CAPTURE: consult coverage and gaps."
    markdown = [f"# {title}", "", state, "", f"Source: {manifest['source_url']}", ""]
    sections, navigation = [], []
    for index, segment in enumerate(manifest["segments"]):
        anchor = f"segment-{index+1}"
        heading = segment["title"]
        if segment["kind"] == "question":
            heading = f"{segment['question_id']}: {heading}"
        times = f"{stamp(segment['start_seconds'])} to {stamp(segment['end_seconds'])}"
        cue = f"Source {times}; transcript lines {segment['source_lines'][0]}-{segment['source_lines'][1]}"
        markdown += [f"## {heading}", "", f"> UNSPOKEN: {cue}", ""]
        visuals, image_buttons = [], []
        for frame_index, frame in enumerate(segment.get("images", [])):
            caption = f"{stamp(frame['at_seconds'])}: {frame['caption']}"
            name = Path(frame["path"]).as_posix()
            markdown += [f"> SHOW: {caption}", f"![{frame['caption']}]({name})", ""]
            mime = mimetypes.guess_type(name)[0] or "image/png"
            encoded = base64.b64encode(assets[name]).decode("ascii")
            hidden = " hidden" if frame_index else ""
            visuals.append(f'<figure data-frame="{frame_index}"{hidden}><img alt="{e(frame["caption"])}" src="data:{mime};base64,{encoded}" title="Click to enlarge"><figcaption>{e(caption)}</figcaption></figure>')
            image_buttons.append(f'<button type="button" data-show-frame="{frame_index}" aria-label="Show {e(caption)}">{stamp(frame["at_seconds"])}</button>')
        cues = " | ".join(segment.get("cues", []))
        if cues:
            markdown += [f"> UNSPOKEN: {cues}", ""]
        markdown += [segment["script"], ""]
        navigation.append(f'<a href="#{anchor}">{e(segment.get("nav_label", heading))}</a>')
        sections.append(f'<section id="{anchor}"><h2>{e(heading)}</h2><p class="cue">{e(cue)}</p><div class="reading"><div><p class="cue">{e(cues)}</p><div class="spoken">{e(segment["script"])}</div></div><div class="visuals"><div class="controls">{"".join(image_buttons)}</div>{"".join(visuals)}</div></div></section>')
    gallery = """const zoom=document.querySelector('#zoom');const header=document.querySelector('header');new ResizeObserver(()=>document.documentElement.style.setProperty('--headerheight',header.getBoundingClientRect().height+'px')).observe(header);document.addEventListener('click',event=>{const pick=event.target.closest('[data-show-frame]');if(pick){const panel=pick.closest('.visuals');panel.querySelectorAll('figure').forEach(f=>{f.hidden=f.dataset.frame!==pick.dataset.showFrame;});}const image=event.target.closest('figure img');if(image){stop();zoom.querySelector('img').src=image.src;zoom.querySelector('img').alt=image.alt;zoom.showModal();}});zoom.querySelector('button').onclick=()=>zoom.close();"""
    document = f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{STYLE} section{{scroll-margin-top:calc(var(--headerheight,150px) + 12px)}} .visuals{{top:calc(var(--headerheight,150px) + 12px)}} [hidden]{{display:none!important}} dialog{{width:94vw;max-width:1800px;border:0;padding:12px}} dialog::backdrop{{background:#000b}} dialog img{{width:100%}} figure img{{cursor:zoom-in}} </style><header><h1>{e(title)}</h1><nav>{"".join(navigation)}</nav><div class="controls"><button id="run">Start</button><label>Speed <input id="speed" type="range" min="5" max="90" value="24" aria-label="Scroll pixels per second"></label><span id="status" role="status"></span></div></header><main><p class="cue">{e(state)}</p>{"".join(sections)}</main><dialog id="zoom"><button type="button">Close full-size image</button><img alt=""></dialog><script>{CONTROLS}{gallery}</script></html>'
    brief = manifest.get("teaching_brief", "")
    if brief:
        document = document.replace('<nav>', '<nav><a href="#teaching-brief">Before teaching</a>', 1)
        preparation = f'<details id="teaching-brief" open style="scroll-margin-top:calc(var(--headerheight,150px) + 12px);font:18px/1.6 system-ui;padding:20px;background:#eaf0ef"><summary>Before teaching: unspoken preparation</summary><div>{render_brief(brief)}</div></details>'
        document = document.replace('<main>', '<main>'+preparation, 1)
    coverage = [f"# Coverage: {title}", "", state, "", "## Teaching-point mapping", ""]
    for point in manifest.get("teaching_points", []):
        coverage.append(f"- {point['id']}: {point['description']} -> {', '.join(point['segment_ids'])}")
    for key, heading in (("verification_notes", "Actual verification"), ("gaps", "Unresolved gaps"), ("omissions", "Removed from the spoken script"), ("source_corrections", "Explicit source corrections")):
        coverage += ["", f"## {heading}", ""]
        coverage += [f"- {item}" for item in manifest.get(key, [])] or ["- None recorded. This is not proof of completeness."]
    coverage += ["", "Mapping and file integrity were checked by the helper. Content completeness, image legibility, and logical correctness require human/agent review."]
    provenance = f"# Source provenance\n\nSource: {manifest['source_url']}\n\nCaptured: {manifest['capture_date']}\n\nMethod: {manifest['transcript_method']}\n\nInstructor: {manifest.get('instructor', 'Not verified')}\n\nLecture date: {manifest.get('lecture_date', 'Not verified')}\n\nRights: Joshua stated that, as an LSAT Lab tutor, he is authorized to use and adapt the selected lecture.\n\nThe source transcript and screenshots are preserved. The teleprompter is an adapted reading copy.\n"
    outputs = {"transcript.md": transcript, "teleprompter.md": "\n".join(markdown).encode(), "teleprompter.html": document.encode(), "timeline.json": (json.dumps(manifest, ensure_ascii=False, indent=2)+"\n").encode(), "coverage.md": "\n".join(coverage).encode()}
    if brief:
        outputs["teaching-brief.md"] = brief.encode("utf-8")
    lesson_path = output / "lesson-steps.json"
    teaching_cards = None
    if lesson_path.exists():
        lesson = json.loads(lesson_path.read_text(encoding="utf-8-sig"))
        module_path = Path(__file__).with_name("teaching_view.py")
        specification = importlib.util.spec_from_file_location("lecture_teaching_view", module_path)
        renderer = importlib.util.module_from_spec(specification)
        specification.loader.exec_module(renderer)
        teaching_document, teaching_assets, teaching_cards = renderer.render(lesson, manifest, output, render_brief(brief))
        assets.update(teaching_assets)
        outputs["full-script.html"] = document.encode("utf-8")
        outputs["continuous-script.html"] = document.encode("utf-8")
        outputs["teleprompter.html"] = teaching_document.encode("utf-8")
        outputs["lesson-steps.json"] = lesson_path.read_bytes()
    if not (output / "PROVENANCE.md").exists():
        outputs["PROVENANCE.md"] = provenance.encode()
    for name, data in outputs.items():
        (output / name).write_bytes(data)
    records = {**preserved_assets, **assets, **{name: (output / name).read_bytes() for name in (*outputs, "PROVENANCE.md")}}
    hashes.write_text("\n".join(f"{digest(data)}  {name}" for name, data in sorted(records.items()))+"\n", encoding="utf-8")
    return {"output": str(output), "segments": len(manifest["segments"]), "images": len(assets), "teaching_moments": teaching_cards, "source_complete": manifest["source_complete"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--transcript", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    try:
        print(json.dumps(package(arguments.manifest, arguments.transcript, arguments.output.resolve())))
    except (ValueError, KeyError, OSError, UnicodeError) as error:
        parser.exit(1, f"Packaging stopped: {error}\n")
