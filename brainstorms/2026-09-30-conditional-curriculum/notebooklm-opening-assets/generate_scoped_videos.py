"""Repair overbroad first-generation videos using one source per lesson."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLI = 'C:/Users/Joshu/.local/bin/notebooklm.exe'
NOTEBOOK = 'e38c0aff-bb6e-498e-a5ef-a6b1bc3a6f5c'
def command(args, json_output=True):
    result = subprocess.run([CLI, *args], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return json.loads(result.stdout) if json_output else result.stdout

teaching = (ROOT / 'teaching-source.md').read_text(encoding='utf-8-sig')
sections = re.split(r'(?m)^## \d+\. ', teaching)[1:]
slugs = ['01-what-conditionals-are', '02-why-direction-matters', '03-sufficient-means-enough', '04-necessary-means-required', '05-group-one', '06-group-two']
path = ROOT / 'scoped-video-manifest.json'
manifest = json.loads(path.read_text()) if path.exists() else {'notebook_id': NOTEBOOK, 'date': '2026-10-02', 'assets': []}
for index, (slug, section) in enumerate(zip(slugs, sections)):
    asset = next((a for a in manifest['assets'] if a['slug'] == slug), None)
    if asset is None:
        asset = {'slug': slug, 'type': 'video', 'revision_reason': 'First video prompts expanded beyond individual lesson. Use chapter-only source.', 'review_status': 'Not watched'}
        manifest['assets'].append(asset)
    source_path = ROOT / (slug + '-source.md')
    section = section.replace('A finalist must attend the interview. | Attends the interview. | Finalist → Attends interview', 'A finalist must attend the interview. | Is required to attend the interview. | Finalist → Required to attend interview')
    if index == 5:
        section += '\nRead must in context. In the interview sentence it states an obligation, not compliance. A finalist is required to attend, but we cannot infer that they actually attend.\n'
    source_path.write_text('# ' + section, encoding='utf-8')
    if not asset.get('source_id'):
        output = command(['source', 'add', str(source_path), '-n', NOTEBOOK, '--json'])
        asset['source_id'] = output.get('source_id', output.get('id', output.get('source', {}).get('id')))
        path.write_text(json.dumps(manifest, indent=2))
    command(['source', 'wait', asset['source_id'], '-n', NOTEBOOK, '--timeout', '600', '--json'])
    if asset.get('generation'):
        continue
    prompt = 'Make ONE brief teaching video about ONLY the supplied single lesson. Teach that lesson with concrete examples, diagram animations, one pause-to-answer moment and a clear explanation. Do not introduce any topic not taught in this source. Do not provide a curriculum overview. Plain natural direct teaching voice, no hype, no AI slogans, no em dashes. Do not conflate obligations with actual compliance. Keep diagrams logically accurate. A rule by itself does not prove its trigger occurred.'
    prompt_path = ROOT / (slug + '-scoped-prompt.txt')
    prompt_path.write_text(prompt, encoding='utf-8')
    try:
        asset['generation'] = command(['generate', 'video', '--prompt-file', str(prompt_path), '-n', NOTEBOOK, '-s', asset['source_id'], '--format', 'brief', '--style', 'custom', '--style-prompt', 'Premium editorial classroom film. Cream, midnight ink, cobalt and emerald. Legible large typography. Precise animated arrows, nested sets and restrained diagrams. Generous whitespace. No decorative diagram unrelated to the lesson.', '--language', 'en', '--no-wait', '--json'])
        asset['status'] = 'submitted'
    except RuntimeError as error:
        asset['status'] = 'submission_failed'
        asset['error'] = str(error)
    path.write_text(json.dumps(manifest, indent=2))
    print(json.dumps(asset), flush=True)
