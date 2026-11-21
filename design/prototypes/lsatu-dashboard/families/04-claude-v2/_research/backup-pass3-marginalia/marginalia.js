/* Marginalia behaviour shared by both roles: sidenote placement, the pencil leader line, reading position, ink-in. */
(function () {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const anchorSel = (n) => `.tok[data-n="${n}"], .inline-btn[data-n="${n}"], .blank[data-n="${n}"]`;

  // each note sits level with its phrase, pushed down only far enough to clear the note above
  function layoutNotes() {
    const wide = window.innerWidth > 920;
    let last = -Infinity;
    $$('.row .sn').forEach((sn) => {
      sn.style.position = wide ? 'relative' : '';
      sn.style.height = wide ? '0px' : '';
      const base = sn.getBoundingClientRect().top + window.scrollY;
      [...sn.children].forEach((nt) => {
        if (!wide) { nt.style.position = nt.style.top = nt.style.left = nt.style.right = ''; return; }
        const a = nt.dataset.n && sn.closest('.row').querySelector(anchorSel(nt.dataset.n));
        const want = a ? a.getClientRects()[0].top + window.scrollY - 12 : base;
        const top = Math.max(want, last + 10);
        Object.assign(nt.style, { position: 'absolute', left: '0', right: '0', top: (top - base) + 'px' });
        last = top + nt.offsetHeight;
      });
    });
    const foot = $('.row.end');
    if (foot) foot.style.marginTop = wide ? Math.max(0, last - (foot.getBoundingClientRect().top + window.scrollY) + 24) + 'px' : '';
  }

  function clearHot() { $$('.is-hot').forEach((e) => e.classList.remove('is-hot')); const p = $('#leader-path'); if (p) p.setAttribute('d', ''); }
  function hot(n, draw) {
    clearHot();
    const t = $(anchorSel(n)), nt = $(`#note-${n}`), page = $('#page'), lp = $('#leader-path');
    if (t) t.classList.add('is-hot');
    if (!nt) return;
    nt.classList.add('is-hot');
    if (!draw || window.innerWidth <= 920 || !t || !lp) return;
    const pr = page.getBoundingClientRect(), rects = t.getClientRects(), tr = rects[rects.length - 1], nr = nt.getBoundingClientRect();
    const x1 = tr.right - pr.left + 4, y1 = tr.top - pr.top + tr.height * .62;
    const x2 = nr.left - pr.left + 6, y2 = nr.top - pr.top + 20;
    const mx = (x1 + x2) / 2;
    lp.setAttribute('d', `M${x1} ${y1} C ${mx} ${y1}, ${mx} ${y2}, ${x2} ${y2}`);
    if (window.gsap && !reduced()) { const L = lp.getTotalLength(); gsap.fromTo(lp, { strokeDasharray: L, strokeDashoffset: L }, { strokeDashoffset: 0, duration: .45, ease: 'power2.out', overwrite: true }); }
  }

  function wire() {
    $$('.tok, .inline-btn[data-n], .blank[data-n]').forEach((t) => {
      const n = t.dataset.n;
      t.addEventListener('mouseenter', () => hot(n, true));
      t.addEventListener('focus', () => hot(n, true));
      t.addEventListener('mouseleave', () => { if (document.activeElement !== t) clearHot(); });
      t.addEventListener('blur', clearHot);
    });
    $$('.note[data-n]').forEach((nt) => {
      nt.addEventListener('mouseenter', () => hot(nt.dataset.n, true));
      nt.addEventListener('mouseleave', clearHot);
    });
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((es) => es.forEach((e) => e.target.classList.toggle('is-here', e.isIntersecting)), { rootMargin: '-35% 0px -55% 0px' });
      $$('.row.para').forEach((r) => io.observe(r));
    }
    requestAnimationFrame(layoutNotes);
  }

  // the pencil goes over the letter once, underlining as it reads
  function inkIn() {
    const toks = $$('.tok');
    if (!window.gsap || reduced()) { toks.forEach((t) => t.classList.add('is-inked')); return; }
    document.documentElement.classList.add('js-ink');
    toks.forEach((t, i) => t.style.setProperty('--d', (0.35 + i * 0.16) + 's'));
    requestAnimationFrame(() => requestAnimationFrame(() => toks.forEach((t) => t.classList.add('is-inked'))));
    setTimeout(() => toks.forEach((t) => t.classList.add('is-inked')), 300);
    setTimeout(() => toks.forEach((t) => t.style.setProperty('--d', '0s')), 4000);
    const tl = gsap.timeline({ delay: .3 });
    tl.from('.note__n', { scale: 0, duration: .35, stagger: .08, ease: 'back.out(3)' }, .15);
    if ($('.tally .st')) tl.from('.tally .st', { strokeDasharray: 30, strokeDashoffset: 30, duration: .16, stagger: .1, ease: 'power1.in' }, .5);
    if ($('.eve__b')) tl.from('.eve__b', { scaleY: 0, transformOrigin: '50% 100%', duration: .5, stagger: .15, ease: 'power3.out' }, .6);
    setTimeout(() => { if (tl.progress() < 1) tl.progress(1); }, 3200);
  }

  window.addEventListener('resize', layoutNotes);
  if (document.fonts) document.fonts.ready.then(layoutNotes);
  window.Marg = { layoutNotes, hot, clearHot, wire, inkIn };
})();
