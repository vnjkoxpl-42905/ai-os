"""Pass-3 Lamplight page scripts: opacity shades instead of filters, quickTo lamp sway, no height animation, practice strip."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / 'lamplight'


def patch(name, subs):
    p = root / name
    s = p.read_text(encoding='utf-8')
    for a, b in subs:
        if a not in s:
            raise SystemExit(f'{name} missing: {a[:80]}')
        s = s.replace(a, b)
    p.write_text(s, encoding='utf-8')
    print(name, 'patched')


shade_helper = """  // a dark sheet over a surface; animating its opacity dims or lights the surface without repainting filters
  const shade = (el) => { if (!el) return null; let s = el.querySelector(':scope > .shade'); if (!s) { s = document.createElement('span'); s.className = 'shade'; s.setAttribute('aria-hidden', 'true'); el.appendChild(s); } return s; };
"""

common = [
    # entrance: light the paper by fading its shade, not by animating a filter
    ("    gsap.set('.paper', { filter: 'brightness(.42) saturate(.6)' });\n",
     "    gsap.set(shade(document.querySelector('.paper')), { opacity: .58 });\n"),
    # windows: flicker an overlay on each lit pane
    ("lit.forEach((p) => gsap.set(p, { filter: 'brightness(.18) saturate(.3)' }));",
     "lit.forEach((p) => gsap.set(shade(p), { opacity: .82 }));"),
]

patch('student.html', common + [
    ("  const icoResume =", shade_helper + "  const icoResume ="),
    ("      .to('.paper', { filter: 'brightness(1) saturate(1)', duration: .9, clearProps: 'filter' }, .4)",
     "      .to('.paper > .shade', { opacity: 0, duration: .9 }, .4)"),
    ("""          .to(p, { filter: 'brightness(1) saturate(1)', duration: .05 })
          .to(p, { filter: 'brightness(.5) saturate(.7)', duration: .06 })
          .to(p, { filter: 'brightness(1) saturate(1)', duration: .45, clearProps: 'filter' });
        setTimeout(() => gsap.set(p, { clearProps: 'filter' }), 2600);""",
     """          .to(shade(p), { opacity: 0, duration: .05 })
          .to(shade(p), { opacity: .5, duration: .06 })
          .to(shade(p), { opacity: 0, duration: .45 });
        setTimeout(() => gsap.set(shade(p), { opacity: 0 }), 2600);"""),
    # sway: one reusable tween instead of a new tween per pointer frame
    ("""          gsap.to(lamp, { rotation: gsap.utils.clamp(-3, 3, dx * 5), duration: 1.8, ease: 'power3.out', overwrite: 'auto' });""",
     """          swayTo(gsap.utils.clamp(-3, 3, dx * 5));"""),
    ("  if (!reduced()) {\n    let raf = 0, px = 0, py = 0;",
     "  const swayTo = hasGsap ? gsap.quickTo(lamp, 'rotation', { duration: 1.8, ease: 'power3.out' }) : () => {};\n  if (!reduced()) {\n    let raf = 0, px = 0, py = 0;"),
    # clearing the note: fade and lift, then remove (no animated height)
    ("gsap.to(n, { height: 0, opacity: 0, marginTop: 0, paddingTop: 0, paddingBottom: 0, duration: .5, ease: 'power3.inOut', onComplete: done }); else done();",
     "gsap.to(n, { opacity: 0, y: -12, duration: .35, ease: 'power2.in', onComplete: done }); else done();"),
    # practice: one strip with a search field and two plain choices
    ("""      <div class="tools">
        <div class="tool tool--search">
          <h3><label for="q-search">Find a question</label></h3>
          <div class="field">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
            <input id="q-search" type="search" placeholder="PT105 S2 Q14, or a question type" autocomplete="off">
          </div>
        </div>
        <button class="tool" type="button" data-act="smart"><h3>Smart Drill</h3><p>A set built from the questions you've missed.</p></button>
        <button class="tool" type="button" data-act="timed"><h3>Timed section</h3><p>35 minutes, test conditions.</p></button>
      </div>""",
     """      <div class="practice">
        <div>
          <label class="practice__label" for="q-search">Find a question</label>
          <div class="field">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
            <input id="q-search" type="search" placeholder="PT105 S2 Q14, or a question type" autocomplete="off">
          </div>
        </div>
        <div class="practice__alts">
          <button class="practice__btn" type="button" data-act="smart"><b>Smart Drill</b><span>Built from the questions you've missed</span></button>
          <button class="practice__btn" type="button" data-act="timed"><b>Timed section</b><span>35 minutes, test conditions</span></button>
        </div>
      </div>"""),
])

patch('teacher.html', common + [
    ("  let kind = 'Drill';", shade_helper + "  let kind = 'Drill';"),
    ("      .to('.paper', { filter: 'brightness(1) saturate(1)', duration: .9, clearProps: 'filter' }, .4);",
     "      .to('.paper > .shade', { opacity: 0, duration: .9 }, .4);"),
    ("""      gsap.timeline({ delay: i * .3 }).to(p, { filter: 'brightness(1) saturate(1)', duration: .05 }).to(p, { filter: 'brightness(.5)', duration: .06 }).to(p, { filter: 'brightness(1) saturate(1)', duration: .45, clearProps: 'filter' });
      setTimeout(() => gsap.set(p, { clearProps: 'filter' }), 2600);""",
     """      gsap.timeline({ delay: i * .3 }).to(shade(p), { opacity: 0, duration: .05 }).to(shade(p), { opacity: .5, duration: .06 }).to(shade(p), { opacity: 0, duration: .45 });
      setTimeout(() => gsap.set(shade(p), { opacity: 0 }), 2600);"""),
    ("""        if (hasGsap) { const r = lamp.getBoundingClientRect(); gsap.to(lamp, { rotation: gsap.utils.clamp(-3, 3, (px - (r.left + r.width / 2)) / window.innerWidth * 5), duration: 1.8, ease: 'power3.out', overwrite: 'auto' }); }""",
     """        if (hasGsap) { const r = lamp.getBoundingClientRect(); swayTo(gsap.utils.clamp(-3, 3, (px - (r.left + r.width / 2)) / window.innerWidth * 5)); }"""),
    ("  if (!reduced()) {\n    let raf = 0, px = 0, py = 0;",
     "  const swayTo = hasGsap ? gsap.quickTo(lamp, 'rotation', { duration: 1.8, ease: 'power3.out' }) : () => {};\n  if (!reduced()) {\n    let raf = 0, px = 0, py = 0;"),
])
