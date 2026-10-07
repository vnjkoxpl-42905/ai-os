"""Original opening scenarios, replacing borrowed dog/mammal teaching examples."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLI = 'C:/Users/Joshu/.local/bin/notebooklm.exe'
NOTEBOOK = 'e38c0aff-bb6e-498e-a5ef-a6b1bc3a6f5c'
LESSONS = [
('01-what-conditionals-are', '''# What a conditional tells you

Imagine a pickup counter. There is one rule: Every order marked ready has been packed.

Order A is marked ready. What do you know about it? It has been packed. You do not need to open the bag to find that out. The rule covers every order marked ready, and Order A is one of those orders.

That is a conditional. When one condition is met, another must be met too. Here, being marked ready gives you packed.

Marked ready → Packed.

Read it in English: If an order is marked ready, it has been packed. The arrow records the relationship. It does not tell us what caused either condition or which happened first.

The rule and the fact do different jobs. The rule applies to every order marked ready. The fact tells us that Order A meets that condition. Together, they tell us something else about Order A.

Show all ready orders inside a packed-orders boundary. The packed boundary can contain other orders too. The rule does not require the groups to differ in size. No ready order can sit outside packed.

Pause: Order C is marked ready. Has it been packed? Yes. It meets the condition the rule covers.

We have not claimed that every packed order is marked ready. That question comes next.
'''),
('02-why-direction-matters', '''# Why the direction matters

Keep the same pickup-counter rule: Every order marked ready has been packed.

Marked ready → Packed.

Order A is marked ready. The rule tells us it has been packed.

Now look at Order B. It has been packed. Is it marked ready? We cannot tell from this rule. Order B might already be marked ready. It might be packed while it waits for a pickup label. Both possibilities fit.

Notice what changed. With Order A, we knew the condition the rule starts from. With Order B, we only knew the other side.

The rule promises that ready orders are packed. It does not promise that all packed orders are ready. Before accepting a conclusion, check that the rule actually gives it to you.

On the LSAT, this helps you see what follows in a Must Be True question. It also helps you spot an argument that reverses a rule and concludes more than its evidence supports. Later, the same relationships help connect evidence to a conclusion.

Visual: ready orders fit inside packed orders. Put Order A inside ready. Put two possible versions of Order B in packed: one in ready, one outside ready. Neither violates the rule.

Pause: Order D is packed. Does that prove it is not ready? No. Its ready status is undetermined. It could be ready or not ready.
'''),
('03-sufficient-means-enough', '''# Sufficient means enough

Every order marked ready has been packed.

Marked ready → Packed.

Being marked ready is sufficient for having been packed. Sufficient means enough. Once we know the order is marked ready, we have what we need to conclude it has been packed.

Take Order A. It is marked ready. Under the rule, can it be unpacked? No. That would break the rule.

But being marked ready may not be the only way an order can be packed. Order B could be packed while it waits for its pickup label. The rule allows that.

Enough does not mean the only way. That difference matters.

The sufficient condition goes on the left. Do not choose it because it appears first in the sentence. Choose it because meeting that condition guarantees the other one.

Visual: select the ready label on Order A and reveal its packed status. Then show a packed Order B whose ready status is unknown. Keep the arrow ready → packed.

Pause: We know Order C is marked ready. What does the rule give us? It has been packed. Being marked ready is enough to establish that.

We are describing a relationship, not claiming that a ready label causes an order to be packed.
'''),
('04-necessary-means-required', '''# Necessary means required

Every order marked ready has been packed.

Marked ready → Packed.

Packed is necessary for being marked ready under this rule. A ready order has to be packed. You cannot have a ready order that is unpacked without breaking the rule.

Necessary means required. Required does not mean enough.

Order B has been packed. That gives it something every ready order has. But it does not establish that Order B is marked ready. It might still be waiting for a pickup label.

Compare the two roles in the same rule. Being marked ready is enough to establish packed. Being packed is required whenever an order is marked ready.

Marked ready is sufficient, on the left. Packed is necessary, on the right. Required means right.

These are roles in this relationship. A condition is not always sufficient or always necessary in every rule. Read the particular sentence.

Visual: place every ready order inside packed. Highlight packed as the boundary no ready order can leave. Then highlight a packed order outside ready to show why the required condition alone does not establish readiness.

Pause: Order C is marked ready. Identify the sufficient and necessary conditions. Marked ready is sufficient. Packed is necessary. The rule gives us packed when ready is met.

No chronology or cause is asserted. We are checking which condition gives us the other.
'''),
]
def run(args):
    response = subprocess.run([CLI, *args], capture_output=True, text=True, encoding='utf-8')
    if response.returncode:
        raise RuntimeError(response.stderr or response.stdout)
    return json.loads(response.stdout)

path = ROOT / 'original-order-video-manifest.json'
manifest = json.loads(path.read_text()) if path.exists() else {'notebook_id': NOTEBOOK, 'date': '2026-10-02', 'assets': []}
for slug, lesson in LESSONS:
    asset = next((a for a in manifest['assets'] if a['slug'] == slug), None)
    if not asset:
        asset = {'slug': slug, 'type': 'video', 'review_status': 'Not reviewed', 'provenance': 'Original order scenario authorized by Joshua via main agent. Replaces dog/mammal examples.'}
        manifest['assets'].append(asset)
    source = ROOT / (slug + '-original-order-source.md')
    source.write_text(lesson, encoding='utf-8')
    if not asset.get('source_id'):
        response = run(['source', 'add', str(source), '-n', NOTEBOOK, '--json'])
        asset['source_id'] = response['source']['id']
        path.write_text(json.dumps(manifest, indent=2))
    run(['source', 'wait', asset['source_id'], '-n', NOTEBOOK, '--timeout', '600', '--json'])
    if asset.get('generation'):
        continue
    prompt = 'One brief lesson, only the supplied source. Use the original pickup-counter order example throughout. No dogs, mammals, geography, medals or other borrowed examples. Do not give a curriculum overview or introduce later topics. Plain natural teaching voice. No hype or slogans. Teach before asking one pause-to-answer question. Draw ready orders as a subset of packed orders, never the reverse. Every order marked ready has been packed: ready -> packed. Packed alone leaves ready status unknown. Avoid causal or chronological claims. Use large readable diagrams and captions, not decorative abstract arrows.'
    prompt_path = ROOT / (slug + '-original-order-prompt.txt')
    prompt_path.write_text(prompt, encoding='utf-8')
    try:
        asset['generation'] = run(['generate', 'video', '--prompt-file', str(prompt_path), '-n', NOTEBOOK, '-s', asset['source_id'], '--format', 'brief', '--style', 'custom', '--style-prompt', 'Quiet premium editorial teaching film. Cream canvas, deep ink type, emerald ready labels, cobalt packed-order boundaries. Clear pickup-counter parcels, precise nested sets, restrained animated arrows. Big legible words, generous whitespace.', '--language', 'en', '--no-wait', '--json'])
        asset['status'] = 'submitted'
    except RuntimeError as error:
        asset['status'] = 'submission_failed'
        asset['error'] = str(error)
    path.write_text(json.dumps(manifest, indent=2))
    print(json.dumps(asset), flush=True)
