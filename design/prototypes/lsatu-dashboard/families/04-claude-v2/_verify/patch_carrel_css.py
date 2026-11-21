"""Pass-3 Carrel CSS: AA contrast on linoleum and orange fills, heading level, flashcard band, tape inset, swipe affordance."""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent / 'carrel'
p = root / 'carrel.css'
s = p.read_text(encoding='utf-8')

subs = [
    ('  --ink-3: #5d6157;\n', '  --ink-3: #5d6157;\n  --on-lino: #2b2d27;      /* secondary text sitting directly on the linoleum (6.4:1) */\n  --signal-fill: #d0400c;  /* orange behind white text (4.75:1) */\n'),
    ('rgba(40,55,35,.25), transparent 60%)', 'rgba(40,55,35,.12), transparent 60%)'),
    ('.nav a { text-decoration: none; color: var(--ink-2);', '.nav a { text-decoration: none; color: var(--on-lino);'),
    ('border-radius: 11px; background: var(--signal); color: #fff;', 'border-radius: 11px; background: var(--signal-fill); color: #fff;'),
    ('.hello p { margin: 0; font-size: 18px; line-height: 1.45; color: var(--ink-2); }', '.hello p { margin: 0; font-size: 18px; line-height: 1.45; color: var(--on-lino); }'),
    ('font-weight: 600; color: var(--ink-3); margin-bottom: 12px;', 'font-weight: 600; color: var(--on-lino); margin-bottom: 12px;'),
    ('.obj-label span { font-weight: 500; color: var(--ink-3); font-size: 14px; }', '.obj-label span { font-weight: 500; color: var(--on-lino); font-size: 14px; }'),
    ('border: 2.5px solid var(--signal); border-radius: 6px;\n  color: var(--signal);', 'border: 2.5px solid var(--signal-ink); border-radius: 6px;\n  color: var(--signal-ink);'),
    ('justify-content: center; font-weight: 800; line-height: 1; }', 'justify-content: center; font-weight: 800; line-height: 1; }\n.postage div { background: var(--signal-fill); }'),
    ('text-align: center; background: var(--signal); color: #fff;', 'text-align: center; background: var(--signal-fill); color: #fff;'),
    ('.flap-cap { font-size: 15px; color: var(--ink-2);', '.flap-cap { font-size: 15px; color: var(--on-lino);'),
    ('.caveat { margin: 14px 2px 0; font-size: 14px; color: var(--ink-2);', '.caveat { margin: 14px 2px 0; font-size: 14px; color: var(--on-lino);'),
    ('box-shadow: 0 1px 2px rgba(0,0,0,.2); border-top: 4px solid var(--c); }', 'box-shadow: 0 1px 2px rgba(0,0,0,.2); background: linear-gradient(var(--c) 0 4px, #fff 4px); }'),
    ('.tape { display: flex; align-items: center; gap: 10px; height: 46px; padding: 0 14px;', '.tape { display: flex; align-items: center; gap: 10px; height: 46px; padding: 4px 14px;'),
    ('font-size: 14px; font-weight: 600; color: var(--ink-2); }\n', 'font-size: 14px; font-weight: 600; color: var(--on-lino); }\n'),
    ('.sheet h3 {', '.sheet h2 {'),
]
for a, b in subs:
    if a not in s:
        raise SystemExit('missing: ' + a[:80])
    s = s.replace(a, b, 1)

s += '''
/* ---------- pass 3: the pile can be flicked through ---------- */
.stack { touch-action: pan-y; outline: none; }
.stack:focus-visible { outline: 2.5px solid var(--ink); outline-offset: 10px; border-radius: 8px; }
.icard.is-front { cursor: grab; }
.icard.is-dragging { cursor: grabbing; }
.icard.is-front button, .icard.is-front a { cursor: pointer; }
.pile-hint { display: flex; justify-content: space-between; align-items: center; gap: 12px; margin: 12px 4px 0; font-size: 14px; color: var(--on-lino); }
.pile-hint b { font-weight: 650; }
.pile-hint__keys { display: inline-flex; gap: 6px; }
.pile-hint__keys button { width: 40px; height: 40px; border-radius: 10px; border: 0; background: var(--paper); box-shadow: var(--sh-1); cursor: pointer; display: grid; place-items: center; color: var(--ink); }
.pile-hint__keys button:hover { transform: translateY(-1px); }
.pile-hint__keys svg { width: 18px; height: 18px; }
.tray-foot { color: var(--on-lino); }
.week-rest span { color: var(--ink-2); }
'''
p.write_text(s, encoding='utf-8')

t = root / 'teacher.html'
ts = t.read_text(encoding='utf-8')
if '<h3>Work order</h3>' not in ts:
    raise SystemExit('teacher heading missing')
t.write_text(ts.replace('<h3>Work order</h3>', '<h2>Work order</h2>'), encoding='utf-8')
print('carrel css + teacher heading patched')
