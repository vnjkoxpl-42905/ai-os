"""Pass-3 Lamplight CSS: remove decorative glows, fix contrast, no stripes, dvh, practice strip, shade overlays."""
import pathlib

p = pathlib.Path(__file__).resolve().parent.parent / 'lamplight' / 'lamplight.css'
s = p.read_text(encoding='utf-8')
subs = [
    ('  min-height: 100vh;\n', '  min-height: 100dvh;\n'),
    ('background: var(--lamp); box-shadow: 0 0 10px var(--lamp); }', 'background: var(--lamp); }'),
    ('  min-height: calc(100vh - 76px);', '  min-height: calc(100dvh - 76px);'),
    ('.ledger i.is-next { border: 1.5px solid #b06a17; background: repeating-linear-gradient(-45deg, rgba(201,130,46,.22) 0 4px, transparent 4px 8px); }',
     '/* the next prompt: an unlit bulb with its filament drawn in */\n'
     '.ledger i.is-next { border: 1.5px solid #9a5810; background: #f6ecd8; }\n'
     '.ledger i.is-next::after { content: ""; position: absolute; left: 30%; right: 30%; top: 50%; height: 2px; margin-top: -1px; border-radius: 1px; background: #9a5810; }'),
    ('background: var(--lamp); box-shadow: 0 0 0 3px rgba(245,185,97,.15), 0 0 14px var(--lamp); }',
     'background: var(--lamp); box-shadow: 0 0 0 3px rgba(245,185,97,.18); }'),
    ('box-shadow: inset 0 0 0 6px rgba(120,70,15,.18), 0 0 40px rgba(245,185,97,.18); }', 'box-shadow: inset 0 0 0 6px rgba(120,70,15,.18); }'),
    ('box-shadow: inset 0 0 0 6px rgba(40,60,90,.18), 0 0 40px rgba(169,193,228,.16); }', 'box-shadow: inset 0 0 0 6px rgba(40,60,90,.18); }'),
    ('background: var(--lamp-hot); box-shadow: 0 0 0 5px rgba(245,185,97,.15), 0 0 22px var(--lamp); }', 'background: var(--lamp-hot); box-shadow: 0 0 0 4px rgba(245,185,97,.2); }'),
    ('background: var(--moon); box-shadow: 0 0 14px rgba(169,193,228,.7); }', 'background: var(--moon); }'),
    ('border: 1.5px solid var(--ivory); box-shadow: 0 0 18px rgba(239,232,220,.3); }', 'border: 1.5px solid var(--ivory); }'),
    ('.field input::placeholder { color: #77746f; }', '.field input::placeholder { color: #8f8b84; }'),
    ('.sig--ses i { background: var(--moon); box-shadow: 0 0 10px rgba(169,193,228,.8); }', '.sig--ses i { background: var(--moon); }'),
    ('transition: color .3s, text-shadow .3s, opacity .3s; border-radius: 4px; }', 'transition: color .3s, opacity .3s; border-radius: 4px; }'),
    ('.names button:hover { color: var(--ivory); text-shadow: 0 0 24px rgba(245,185,97,.5); }', '.names button:hover { color: var(--ivory); text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 8px; text-decoration-color: rgba(245,185,97,.6); }'),
    ('.names button.is-match { color: var(--lamp-hot); text-shadow: 0 0 26px rgba(245,185,97,.6); }', '.names button.is-match { color: var(--lamp-hot); }'),
    ('box-shadow: 0 20px 40px -12px rgba(0,0,0,.7), 0 0 40px rgba(245,185,97,.2);', 'box-shadow: 0 20px 40px -12px rgba(0,0,0,.7);'),
    ('    0 18px 30px -18px rgba(0,0,0,.7),\n    0 0 120px rgba(245, 185, 97, .12);', '    0 18px 30px -18px rgba(0,0,0,.7);'),
    ('.names__empty { font-family: var(--sans); font-size: 15px; color: var(--dim); }', '.names__empty { font-family: var(--sans); font-size: 15px; color: var(--dim); }\n.names button:focus-visible { color: var(--ivory); }'),
]
for a, b in subs:
    if a not in s:
        raise SystemExit('missing: ' + a[:70])
    s = s.replace(a, b)

# overlays that the motion animates instead of CSS filters (opacity stays on the compositor)
s += '''
/* ---------- pass 3: shade overlays animated by opacity ---------- */
.shade { position: absolute; inset: 0; z-index: 3; pointer-events: none; background: #0b0c11; opacity: 0; border-radius: inherit; }
.pane > .shade { z-index: 2; }

/* ---------- pass 3: practice as one strip, not three cards ---------- */
.practice {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 18px 40px; align-items: center;
  padding: 26px 28px; border-radius: 4px; border: 1px solid var(--line); background: linear-gradient(180deg, var(--night-2), var(--night));
}
.practice .field { max-width: 640px; }
.practice__label { display: block; font-family: var(--serif); font-size: 26px; margin-bottom: 6px; }
.practice__alts { display: flex; flex-wrap: wrap; gap: 10px; }
.practice__btn {
  display: flex; flex-direction: column; align-items: flex-start; gap: 2px; min-width: 190px; padding: 14px 18px;
  border-radius: 4px; border: 1px solid var(--line-2); background: transparent; cursor: pointer; text-align: left; color: var(--ivory);
  transition: border-color .25s, background .25s;
}
.practice__btn b { font-family: var(--serif); font-weight: 500; font-size: 22px; }
.practice__btn span { font-size: 13.5px; color: var(--dim); }
.practice__btn:hover { border-color: rgba(245,185,97,.55); background: rgba(245,185,97,.05); }
@media (max-width: 720px) {
  .practice { grid-template-columns: minmax(0, 1fr); padding: 20px; }
  .practice__btn { flex: 1; min-width: 0; }
}
'''
p.write_text(s, encoding='utf-8')
print('lamplight.css patched')
