"""Pass-3 accessibility: skip link on every page, spoken inbox labels for the badge counts."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
skip_css = {
    'lamplight/lamplight.css': '.skip { position: absolute; left: 16px; top: -60px; z-index: 100; padding: 10px 16px; border-radius: 6px; background: var(--paper); color: var(--paper-ink); font-weight: 600; text-decoration: none; transition: top .2s; }\n.skip:focus { top: 12px; }\n',
    'carrel/carrel.css': '.skip { position: absolute; left: 16px; top: -60px; z-index: 100; padding: 10px 16px; border-radius: 8px; background: var(--ink); color: var(--paper); font-weight: 700; text-decoration: none; transition: top .2s; }\n.skip:focus { top: 12px; }\n',
    'marginalia/marginalia.css': '.skip { position: absolute; left: 16px; top: -60px; z-index: 100; padding: 10px 16px; border-radius: 6px; background: var(--pencil); color: #fff; font-family: var(--ui); font-weight: 600; text-decoration: none; transition: top .2s; }\n.skip:focus { top: 12px; }\n',
}
for f, css in skip_css.items():
    p = root / f
    p.write_text(p.read_text(encoding='utf-8') + '\n/* pass 3: skip link */\n' + css, encoding='utf-8')

label_js = """
    // spoken label for the badge: a bare "?" or "-" means nothing out loud
    { const btn = c.closest('button'); if (btn) btn.setAttribute('aria-label', c.textContent === '?' ? 'Inbox, unread count unknown' : c.textContent === '\\u2014' ? 'Inbox, loading' : `Inbox, ${c.textContent} unread`); }
"""

for d in ('lamplight', 'carrel', 'marginalia'):
    for role in ('student', 'teacher'):
        p = root / d / f'{role}.html'
        s = p.read_text(encoding='utf-8')
        if 'class="skip"' not in s:
            s = s.replace('<body>\n', '<body>\n<a class="skip" href="#main">Skip to your home page</a>\n', 1)
            if d == 'marginalia':
                s = s.replace('<main id="letter">', '<main id="main"><div id="letter">', 1).replace('</main>', '</div></main>', 1)
            else:
                s = s.replace('<main>', '<main id="main" tabindex="-1">', 1)
        if d != 'marginalia' and 'spoken label for the badge' not in s:
            anchor = "c.textContent = unread; c.classList.toggle('is-zero', !unread);" if role == 'student' or d == 'lamplight' else "c.textContent = u; c.classList.toggle('is-zero', !u);"
            if anchor not in s:
                raise SystemExit(f'{d}/{role} badge anchor missing')
            # label after every assignment path: wrap summary() end by patching the anchor and the loading/error returns
            s = s.replace(anchor, anchor + label_js, 1)
            for early in ("c.textContent = '\\u2014'; return;", "c.textContent = '?'; return;"):
                s = s.replace(early, early.replace(' return;', " c.closest('button').setAttribute('aria-label', c.textContent === '?' ? 'Inbox, unread count unknown' : 'Inbox, loading'); return;"))
        p.write_text(s, encoding='utf-8')
        print(d, role, 'ok')
