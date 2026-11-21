"""Finish independently discovered contradictions, preserving before bytes."""
from pathlib import Path
import hashlib
import json
import os
import re
import tempfile

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).parent
HOME = Path.home()
NAMES = {'chat-export', 'youtube-full', 'watch', 'claude-api', 'gws-shared'}
SCOPES = [ROOT/'skills'/r for r in ('claude','codex','gemini')]
SCOPES += [ROOT/r/'skills' for r in ('.agents','.claude','.gemini')]
SCOPES += [HOME/r/'skills' for r in ('.agents','.codex','.claude')]
records = []

def save(path, text):
    before = path.read_bytes()
    after = text.encode('utf-8')
    if before == after:
        return
    key = hashlib.sha256(str(path).encode()).hexdigest()[:20]
    backup = OUT/'backups'/'final-direct'/key/path.name
    backup.parent.mkdir(parents=True, exist_ok=True)
    if backup.exists() and backup.read_bytes() != before:
        raise RuntimeError(f'Existing backup differs: {path}')
    backup.write_bytes(before)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.repair-', delete=False) as f:
        f.write(after)
        stage = Path(f.name)
    try:
        if path.read_bytes() != before:
            raise RuntimeError(f'Concurrent edit: {path}')
        os.replace(stage, path)
    finally:
        if stage.exists():
            stage.unlink()
    records.append(dict(path=str(path), before_sha256=hashlib.sha256(before).hexdigest(),
                        after_sha256=hashlib.sha256(after).hexdigest(), backup=str(backup)))

def description(text, value):
    return re.sub(r'^description:.*$', 'description: '+json.dumps(value), text, count=1, flags=re.M)

def entry(name, text):
    if name == 'chat-export':
        text = description(text, 'Export a conversation to a local Markdown file when explicitly asked to save or export the chat. Retrieve original session logs for a verbatim export; disclose missing ranges. Chat-only continuation uses session-handoff.')
        text = text.replace('/Users/joshuaf/ai-os/handoffs/', '<current-project-root>/handoffs/')
        text = re.sub(r'1\. \*\*Reconstruct the full transcript\*\*.*?(?=\n2\.)', '1. **Retrieve original session logs** for the requested conversation. Verify which turns are available and write retrieved user/assistant messages verbatim. If original logs are unavailable or incomplete, export visible turns only, label the transcript partial, and list missing or compacted ranges. Never reconstruct absent messages as verbatim.\n', text, flags=re.S)
        text = re.sub(r'4\. \*\*Save the file\*\* using Desktop Commander.*?(?=\n5\.)', '4. **Save the file** using an available host file-writing tool, then read it back and verify its coverage label and output path.\n', text, flags=re.S)
        text = text.replace('- Never truncate the transcript. If it\'s long, write all of it.', '- Preserve all retrieved turns. A partial source must remain explicitly partial; report unavailable ranges.')
        text = text.replace('## Full transcript', '## Transcript (complete or partial, with coverage)')
        text = text.replace('[...repeat for every message in the conversation...]', '[Repeat for every retrieved message; list unavailable ranges above.]')
    elif name == 'youtube-full':
        text = description(text, 'Use for explicitly selected TranscriptAPI transcript, video/channel search or playlist requests, or an authorized hosted fallback after free captions fail. Ordinary YouTube transcripts use the free local collector first. No automatic signup, key request or spending.')
        text = re.sub(r'^compatibility:.*$', 'compatibility: Free caption extraction uses the installed local collector or yt-dlp; the optional hosted branch requires internet and an authorized TranscriptAPI key.', text, flags=re.M)
        text = re.sub(r'^required_environment_variables:\n.*?(?=^metadata:|^---)', '', text, flags=re.M|re.S)
        def clean_meta(m):
            data = json.loads(m.group(1))
            data.get('openclaw', {}).pop('requires', None)
            data.get('openclaw', {}).pop('primaryEnv', None)
            return 'metadata: '+json.dumps(data, ensure_ascii=False, separators=(',', ':'))
        text = re.sub(r'^metadata: (\{.*\})$', clean_meta, text, flags=re.M)
        text = text.replace('If `$TRANSCRIPT_API_KEY` is not set, read [references/auth-setup.md](references/auth-setup.md) and follow the instructions there to get and store the key.', 'For ordinary transcripts, use the existing free local caption collector or yt-dlp and preserve timestamps, caption provenance and missing-section notices. No provider key is needed for that route.\n\nOnly after the user selects the hosted provider and authorizes any cost, check its key privately. If it is missing, explain that this optional branch is unavailable. Read [references/auth-setup.md](references/auth-setup.md) only for an explicitly requested provider setup; never create an account or transmit credentials automatically.')
        text = text.replace('## Required Headers', '## Required Headers for the optional hosted branch')
        text = text.replace('Every request needs two headers:', 'Every authorized TranscriptAPI request needs two headers:')
    elif name == 'claude-api':
        text = text.replace('ask whether they want to switch the file to Claude or want a non-Claude implementation.', 'respect the selected provider and route to its documentation; clarify only if the provider is actually ambiguous.')
        text = re.sub(r'For the Claude model version, please use Claude Opus 5[^\n]*', 'Honor the user-selected model. Otherwise verify currently available model IDs and capabilities through the installed SDK or official Anthropic documentation before selecting one within the authorized budget. Use streaming for long requests where supported; thinking options depend on the selected model.', text)
        text = re.sub(r'^\*\*ALWAYS use `claude-opus-5`[^\n]*', '**Model selection:** Honor explicit user choices. Otherwise verify available IDs and capabilities through the Models API or [official model documentation](https://platform.claude.com/docs/en/models/overview), then choose within the authorized quality and cost constraints. The cached table is historical reference, not a mandatory default or proof of current availability. Never construct model IDs or add date suffixes without documentation.', text, flags=re.M)
        text = text.replace('## Current Models (cached: 2026-06-24)', '## Historical model reference (cached: 2026-06-24; verify before use)')
    elif name == 'gws-shared':
        text = text.replace('- **Always** confirm with user before executing write/delete commands', '- Verify authorization for the actual write/send/delete scope. Proceed when that scope is already authorized; ask only for missing authorization. Deletion requires explicit authorization for the target.')
        text = text.replace('- If a matching issue already exists, add context by commenting on the existing thread instead of creating a duplicate', '- If a matching issue exists, draft useful context for that thread. Post a comment or create an issue only when the user explicitly authorizes publication.')
        text = re.sub(r'- \*\*zsh `!` expansion:\*\*.*?(?=- \*\*JSON with double quotes)', '- **Shell quoting:** In Bash/zsh, single-quote literal ranges such as `\'Sheet1!A1:D10\'` to avoid expansion. Use the current shell\'s quoting rules rather than copying another shell\'s escapes.\n', text, flags=re.S)
    elif name == 'watch':
        text = re.sub(r'- Does not persist anything outside[^\n]*', '- Keeps task output in its working directory. Preserve frames, captions and downloads; removal requires explicit authorization for the verified task-owned path.', text)
        text = re.sub(r'\*\*Whisper API fallback\.\*\* If no captions.*?(?=\nKeep keys)', '**Whisper API fallback (optional).** Missing captions do not trigger an upload. Only an explicitly selected `--whisper groq` or `--whisper openai` enables that provider after upload and cost authorization. `--no-whisper` always disables it.\n', text, flags=re.S)
        text = re.sub(r'- \*\*Setup preflight failed\*\*:[^\n]*', '- **Setup preflight failed:** Check installed dependencies and PATH first. Do not run the legacy key-coupled installer. Provider setup is separate and only follows an explicitly authorized provider request; keys stay private in the current project central .env/environment.', text)
        text = text.replace('Script prints a hint pointing to setup.', 'Script reports missing captions without automatically setting up a provider.')
        text = text.replace('only when native captions are missing AND Whisper is not disabled with `--no-whisper`', 'only when native captions are missing AND a provider was explicitly selected with `--whisper`, authorized, and not disabled with `--no-whisper`')
        text = text.replace('when `GROQ_API_KEY` is set (preferred — cheaper, faster)', 'only when `--whisper groq` is explicitly selected and authorized')
        text = text.replace('when `OPENAI_API_KEY` is set and Groq is not, or when `--whisper openai` is forced', 'only when `--whisper openai` is explicitly selected and authorized')
        text = text.replace('3 fps', '2 fps').replace('90 frames', '60 frames')
    return text

def payload(path, text):
    if path.name == 'watch.py':
        text = text.replace('help="Force a specific Whisper backend. Default: prefer Groq, fall back to OpenAI."', 'help="Explicitly enable this Whisper provider after upload/cost authorization. Default: captions only."')
        text = text.replace('work.mkdir(parents=True, exist_ok=True)', 'if work.exists() and any(work.iterdir()):\n        raise SystemExit("Output directory is not empty; choose a fresh task directory")\n    work.mkdir(parents=True, exist_ok=True)', 1)
        text = text.replace('if not transcript_segments and not args.no_whisper:', 'if not transcript_segments and not args.no_whisper and args.whisper is not None:')
        text = text.replace('"**Read each frame path below with the Read tool to view the image.** "', '"**View selected frame paths with an available host image-viewing tool.** "')
        text = re.sub(r'        setup_py = SCRIPT_DIR / "setup.py"\n        print\(\n            "_No transcript available.*?\n        \)', '        print("_No transcript available. Proceed with frames only and report missing captions. "\n              "Optional API transcription requires an explicitly selected provider and upload/cost authorization._")', text, flags=re.S)
        text = text.replace('f"_Work dir: `{work}` — delete when done._"', 'f"_Work dir: `{work}`. Preserve output; remove only with explicit authorization._"')
    elif path.name == 'frames.py':
        text = text.replace('    for existing in out_dir.glob("frame_*.jpg"):\n        existing.unlink()', '    if any(out_dir.iterdir()):\n        raise SystemExit("Frame output directory is not empty; existing files were preserved")')
        text = text.replace('        "-y",', '        "-n",')
        text = text.replace('Install with: brew install ffmpeg', 'Check the installed FFmpeg location and refresh PATH before installing for your platform')
    elif path.name == 'whisper.py':
        text = text.replace('        Path.home() / ".config" / "watch" / ".env",\n', '')
    return text

seen = set()
for scope in SCOPES:
    if not scope.exists():
        continue
    for p in scope.rglob('SKILL.md'):
        if p.parent.name not in NAMES or any(x in p.parts for x in ('_snapshots','_project-forks')):
            continue
        real = p.resolve()
        if real in seen:
            continue
        seen.add(real)
        save(real, entry(p.parent.name, real.read_text(encoding='utf-8-sig')))
        if p.parent.name == 'watch':
            for name in ('watch.py','frames.py','whisper.py'):
                script = p.parent/'scripts'/name
                if script.is_file() and script.resolve() not in seen:
                    seen.add(script.resolve())
                    save(script.resolve(), payload(script, script.read_text(encoding='utf-8-sig')))
(OUT/'final-direct-receipts.json').write_text(json.dumps(records, indent=2), encoding='utf-8')
print(json.dumps({'changed_files': len(records), 'receipt':str(OUT/'final-direct-receipts.json')}))
