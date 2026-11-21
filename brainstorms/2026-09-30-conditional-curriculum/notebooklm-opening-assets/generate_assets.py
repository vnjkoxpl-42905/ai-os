"""Authorized NotebookLM generation. Explicit notebook/source IDs; no credentials."""
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
CLI = pathlib.Path('C:/Users/Joshu/.local/bin/notebooklm.exe')
NOTEBOOK = 'e38c0aff-bb6e-498e-a5ef-a6b1bc3a6f5c'
BASE = '''Create an LSAT U teaching asset from only the supplied Joshua teaching draft. Scope stops at Group 2. Use plain, direct, natural language, short sentences and concrete examples. Explain why each conclusion follows. No hype, no em dashes, no invented LSAT statistics, no AI phrases such as unlock, delve or game-changer. Do not introduce contrapositives, Groups 3/4, chains or quantities. Sufficient means enough; necessary means required. Arrows express a relationship, not necessarily a cause or time order. A rule does not prove that its sufficient condition occurs. All dogs are mammals permits mammals that are not dogs and also does not require sets to have different sizes. Never automatically assign words after an indicator: ask what complete idea it refers to and check the whole meaning. Current Group 1 list: if, when, where, all, the only, every, any. Current Group 2 list: only, only if, only when, only where, always, requires, must. These are teaching groups, not universally mechanical word rules. If and only if differ; only members are admitted and the only people admitted are members both mean admitted -> member. Include original practice only, no copied official LSAT questions. Preserve the author's reasoning, but improve stiff phrasing. Teach before testing.'''
VIDEO_PARTS = [
    ('01-what-conditionals-are', 'Teach what a conditional means using All dogs are mammals, Luna is a dog, therefore Luna is a mammal. Animate nested dog and mammal sets, then place Luna. Distinguish the rule from the fact. No vocabulary overload.'),
    ('02-why-direction-matters', 'Teach why conditionals matter. Compare dog -> mammal with the unsupported reversal using a cat counterexample. Briefly connect to Must Be True, Flaw and Sufficient Assumption without teaching those question types. Show what we know and what remains possible.'),
    ('03-sufficient-means-enough', 'Teach sufficient means enough using earns full credit -> passes. Meeting the left side guarantees the right. Passing without full credit remains possible. Show two routes into passing so enough is not mistaken for the only way.'),
    ('04-necessary-means-required', 'Teach necessary means required using enters archive -> has pass. Show a person with a pass who stays outside. The pass is required by the rule but not enough to establish entry. Compare the two roles side by side.'),
    ('05-group-one', 'Teach all seven Group 1 indicators. Work if-clause at the front and at the end. Teach the What Test, complete modifiers and the only. Animate highlight indicator, identify target idea, place target left, identify remaining idea, read complete arrow back in English. Use short original examples.'),
    ('06-group-two', 'Teach all seven Group 2 indicators. Work only if, required-before-indicator, only versus the only, and if versus only if. Animate highlight indicator, ask what it refers to, place required idea right, supply left, read complete arrow back in English. Show natural worked examples and one pause-to-answer.'),
]

def run(args):
    result = subprocess.run([str(CLI), *args], capture_output=True, text=True, encoding='utf-8')
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return json.loads(result.stdout)

manifest_path = ROOT / 'manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig')) if manifest_path.exists() else {
    'notebook_id': NOTEBOOK, 'created_date': '2026-10-02', 'assets': [],
    'review_status': 'Generated output must be reviewed before embedding or publishing.',
    'source_sha256': hashlib.sha256((ROOT / 'teaching-source.md').read_bytes()).hexdigest(),
}
if not manifest.get('source_id'):
    source = run(['source', 'add', str(ROOT / 'teaching-source.md'), '-n', NOTEBOOK,
                  '--title', 'LSAT U Opening Conditional Lessons: Joshua Review Draft', '--json'])
    manifest['source_id'] = source.get('source_id', source.get('id', source.get('source', {}).get('id')))
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
source_id = manifest['source_id']
run(['source', 'wait', source_id, '-n', NOTEBOOK, '--timeout', '600', '--json'])
jobs = [
    ('opening-study-guide', 'report', ['--format', 'custom'], 'Write a student-ready six-part illustrated study guide. Start with what a conditional is, then why direction matters, sufficient, necessary, Group 1, Group 2. Include a worked example then a small independent task with explained answer per part. Use visual descriptions as captions. Do not include production instructions.'),
    ('opening-flashcards', 'flashcards', ['--quantity', 'more', '--difficulty', 'easy'], 'Create flashcards that require active recall and a short explanation, covering definitions, sufficient/necessary, complete targets, all Group1/2 indicators, varied clause positions, if/only if, only/the only. Answers must include correct arrow and why. Avoid just term-definition cards.'),
    ('opening-quiz', 'quiz', ['--quantity', 'more', '--difficulty', 'easy'], 'Create a progressive quiz after teaching: apply a rule to a fact, identify sufficient and necessary, identify complete indicator target, translate Group1/2, compare if/only if and only/the only. Include clear answer-specific explanations. Each item must be uniquely answerable and logically accurate.'),
    ('sufficient-necessary-infographic', 'infographic', ['--orientation', 'landscape', '--detail', 'standard', '--style', 'editorial', '--language', 'en'], 'Make a visually restrained premium editorial infographic: Enough / Required. Large dog -> mammal nested-set illustration; archive-entry -> pass example. Contrast knowing left gives right with knowing right leaves left undetermined. Group1 left / Group2 right summary. Use ample negative space, legible typography, warm cream, midnight ink, emerald and cobalt accents. No decorative complexity.'),
]
for slug, description in VIDEO_PARTS:
    jobs.append((slug, 'video', ['--format', 'brief', '--style', 'custom', '--style-prompt',
        'Premium editorial learning film. Warm cream backgrounds, deep ink typography, emerald and cobalt diagrams, generous whitespace, animated arrows and precise nested-set graphics. Contemporary high-end classroom, not cartoon clutter.', '--language', 'en'], description + ' One brief video for this part only.'))
completed_slugs = {a['slug'] for a in manifest['assets']}
for slug, kind, options, prompt in jobs:
    prompt_path = ROOT / (slug + '-prompt.txt')
    prompt_path.write_text(BASE + '\n\n' + prompt, encoding='utf-8')
    if slug in completed_slugs:
        continue
    try:
        output = run(['generate', kind, '--prompt-file', str(prompt_path), '-n', NOTEBOOK,
                      '-s', source_id, *options, '--no-wait', '--json'])
        asset = {'slug': slug, 'type': kind, 'generation': output, 'status': 'submitted'}
    except RuntimeError as error:
        asset = {'slug': slug, 'type': kind, 'status': 'submission_failed', 'error': str(error)}
    manifest['assets'].append(asset)
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(json.dumps(asset), flush=True)
