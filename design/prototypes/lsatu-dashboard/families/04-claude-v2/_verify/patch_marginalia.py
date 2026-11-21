"""Pass-3 Marginalia: cooler paper, AA margin text, run-in small caps, pop-in notes on phones (per Gwern's sidenote survey)."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / 'marginalia'


def patch(name, subs, append=''):
    p = root / name
    s = p.read_text(encoding='utf-8')
    for a, b in subs:
        if a not in s:
            raise SystemExit(f'{name} missing: {a[:80]}')
        s = s.replace(a, b, 1)
    p.write_text(s + append, encoding='utf-8')
    print(name, 'patched')


patch('marginalia.css', [
    ('  --paper: #f6f5f0;\n  --paper-2: #efeee7;', '  --paper: #f3f4f1;\n  --paper-2: #e9ebe6;'),
    ('  --faint: #8d9098;', '  --faint: #666a72;'),
    ('  --rule: #dcdbd3;', '  --rule: #d6d8d2;'),
], append='''
/* ---------- pass 3: run-in small caps open each paragraph, as in a well-set book ---------- */
.runin { font-variant-caps: all-small-caps; letter-spacing: .07em; font-weight: 600; font-variant-numeric: oldstyle-nums; }

/* ---------- pass 3: note headers are buttons so phones can open notes one at a time ---------- */
.note__toggle { all: unset; display: block; color: var(--ink); font-weight: 600; font-size: 15px; }
.note__toggle:focus-visible { outline: 2px solid var(--pencil); outline-offset: 3px; border-radius: 3px; }
@media (min-width: 921px) { .note__toggle { cursor: default; } }
@media (max-width: 920px) {
  .note { padding: 12px 12px 12px 40px; border-radius: 6px; }
  .note__toggle { cursor: pointer; display: flex; justify-content: space-between; gap: 12px; align-items: baseline; min-height: 24px; }
  .note__toggle::after { content: 'Open'; font-weight: 600; font-size: 13px; color: var(--pencil); flex: none; }
  .note.is-open .note__toggle::after { content: 'Close'; }
  .note:not(.is-open) > :not(.note__n):not(.note__toggle) { display: none; }
  .sn { gap: 6px; }
}
''')

# Student: run-ins + shared behaviour file for pop-ins
patch('student.html', [
    ('<p class="lead">Tonight is for ', '<p class="lead"><span class="runin">Tonight</span> is for '),
    ("${waiting ? `${Word(waiting)} more ${waiting === 1 ? 'thing is' : 'things are'} waiting.` : 'Everything else is done.'}",
     "${waiting ? `<span class=\"runin\">${Word(waiting)} more</span> ${waiting === 1 ? 'thing is' : 'things are'} waiting.` : '<span class=\"runin\">Everything else</span> is done.'}"),
    ('<p>Joshua wrote to you this morning:</p>', '<p><span class="runin">Joshua wrote</span> to you this morning:</p>'),
    ('<p>Your next session with Joshua is ', '<p><span class="runin">Your next session</span> with Joshua is '),
    ('<p>If you want more practice, look up', '<p><span class="runin">If you want more practice,</span> look up'),
    ('<script src="../shared/sample.js"></script>', '<script src="../shared/sample.js"></script>\n<script src="marginalia.js"></script>'),
    ("    if (typeof layoutNotes === 'function') requestAnimationFrame(layoutNotes);",
     "    Marg.popins();\n    if (typeof layoutNotes === 'function') requestAnimationFrame(layoutNotes);"),
    ("      const nt = $(`#note-${b.dataset.n}`);\n      if (nt && window.innerWidth <= 920)",
     "      const nt = $(`#note-${b.dataset.n}`);\n      if (nt) Marg.openNote(nt);\n      if (nt && window.innerWidth <= 920)"),
])

patch('teacher.html', [
    ("${lead} ${tok(1, 'Celia'", "<span class=\"runin\">${lead.split(' ').slice(0, 2).join(' ')}</span> ${lead.split(' ').slice(2).join(' ')} ${tok(1, 'Celia'"),
    ('`<p>You teach ${tok(4', '`<p><span class="runin">You teach</span> ${tok(4'),
    ('`<p>Assign <label class="sr"', '`<p><span class="runin">Assign</span> <label class="sr"'),
    ("    Marg.wire();\n", "    Marg.popins();\n    Marg.wire();\n"),
    ("if (t) { e.preventDefault(); const nt = $(`#note-${t.dataset.n}`); if (nt && window.innerWidth <= 920)",
     "if (t) { e.preventDefault(); const nt = $(`#note-${t.dataset.n}`); if (nt) Marg.openNote(nt); if (nt && window.innerWidth <= 920)"),
])

patch('marginalia.js', [
    ("  window.addEventListener('resize', layoutNotes);",
     """  // Note headers become buttons. On phones each note starts closed (a pop-in) and opens on tap; on desktop all stay open.
  function popins() {
    $$('.note').forEach((nt) => {
      let t = nt.querySelector(':scope > .note__t');
      if (t && t.tagName !== 'BUTTON') {
        const b = document.createElement('button');
        b.type = 'button'; b.className = 'note__t note__toggle'; b.innerHTML = t.innerHTML;
        t.replaceWith(b); t = b;
      }
      if (t) t.setAttribute('aria-expanded', String(window.innerWidth > 920 || nt.classList.contains('is-open')));
    });
  }
  function openNote(nt) { nt.classList.add('is-open'); const t = nt.querySelector('.note__toggle'); if (t) t.setAttribute('aria-expanded', 'true'); }
  document.addEventListener('click', (e) => {
    const t = e.target.closest('.note__toggle');
    if (!t || window.innerWidth > 920) return;
    const nt = t.closest('.note');
    nt.classList.toggle('is-open');
    t.setAttribute('aria-expanded', String(nt.classList.contains('is-open')));
  });
  window.addEventListener('resize', () => { popins(); layoutNotes(); });"""),
    ("  window.Marg = { layoutNotes, hot, clearHot, wire, inkIn };", "  window.Marg = { layoutNotes, hot, clearHot, wire, inkIn, popins, openNote };"),
])
