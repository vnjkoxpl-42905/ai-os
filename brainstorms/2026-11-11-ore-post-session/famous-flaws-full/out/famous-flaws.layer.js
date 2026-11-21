/* Famous Flaws layer script. Appended after the shell's own script block. */
(function () {
  var doc = document;
  var $ = function (sel, scope) { return (scope || doc).querySelector(sel); };
  var $$ = function (sel, scope) { return Array.prototype.slice.call((scope || doc).querySelectorAll(sel)); };
  var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ----- panels ----- */
  function setPanel(panel, open) {
    var head = $('.fx-head', panel), body = $('.fx-body', panel);
    if (!head || !body) return;
    head.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) body.removeAttribute('hidden'); else body.setAttribute('hidden', '');
  }
  $$('.fx-panel').forEach(function (panel) {
    var head = $('.fx-head', panel);
    if (head) head.addEventListener('click', function () {
      setPanel(panel, head.getAttribute('aria-expanded') !== 'true');
    });
  });

  /* ----- filters ----- */
  var current = 'all';
  function applyFilter(g) {
    current = g;
    $$('.fx-chip').forEach(function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-filter') === g ? 'true' : 'false'); });
    $$('.fx-card, .fx-panel').forEach(function (el) {
      var show = g === 'all' || el.getAttribute('data-g') === g;
      if (show) el.removeAttribute('hidden'); else el.setAttribute('hidden', '');
    });
    var n = $$('.fx-card').filter(function (c) { return !c.hasAttribute('hidden'); }).length;
    var live = $('#fx-live'); if (live) live.textContent = n + ' of 15 flaws shown';
  }
  $$('.fx-chip').forEach(function (c) {
    c.addEventListener('click', function () { applyFilter(c.getAttribute('data-filter')); });
  });

  /* ----- cards open their panel ----- */
  function openById(id, scroll) {
    var panel = doc.getElementById(id);
    if (!panel) return;
    if (panel.hasAttribute('hidden')) applyFilter('all');
    setPanel(panel, true);
    if (scroll) {
      panel.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'start' });
      var head = $('.fx-head', panel); if (head) { try { head.focus({ preventScroll: true }); } catch (e) { head.focus(); } }
    }
  }
  $$('.fx-card').forEach(function (card) {
    card.addEventListener('click', function (e) { e.preventDefault(); openById(card.getAttribute('data-target'), true); });
  });
  var all = $('#fx-open-all'), none = $('#fx-close-all');
  if (all) all.addEventListener('click', function () { $$('.fx-panel').forEach(function (p) { if (!p.hasAttribute('hidden')) setPanel(p, true); }); });
  if (none) none.addEventListener('click', function () { $$('.fx-panel').forEach(function (p) { setPanel(p, false); }); });
  if (location.hash && location.hash.indexOf('#flaw-') === 0) openById(location.hash.slice(1), false);

  /* ----- say it first checks ----- */
  $$('.fx-reveal').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.fx-try');
      var on = box.classList.toggle('open');
      btn.setAttribute('aria-expanded', on ? 'true' : 'false');
      btn.textContent = on ? 'Hide the answer' : 'Check my answer';
    });
  });

  /* ----- matrix forced choice ----- */
  $$('.fx-quiz').forEach(function (q) {
    var right = q.getAttribute('data-right');
    $$('.fx-opt', q).forEach(function (o) {
      o.addEventListener('click', function () {
        $$('.fx-opt', q).forEach(function (x) { x.classList.remove('right', 'wrong'); });
        var ok = o.getAttribute('data-label') === right;
        o.classList.add(ok ? 'right' : 'wrong');
        if (!ok) { $$('.fx-opt', q).forEach(function (x) { if (x.getAttribute('data-label') === right) x.classList.add('right'); }); }
        q.classList.add('done');
        var res = $('.res', q); if (res) res.textContent = ok ? 'Correct. ' : 'Not quite. The answer is ' + right + '. ';
      });
    });
  });

  /* ----- cake on blocks ----- */
  var cake = $('.fx-cake');
  if (cake) {
    var state = $('.state-now', cake), out = $('.out', cake);
    var obj = $('#fx-object'), rst = $('#fx-reset');
    function set(on) {
      cake.classList.toggle('objected', on);
      if (state) state.textContent = on ? 'STATE: AN OBJECTION: WHAT IF...' : 'STATE: VALID ARGUMENT';
      if (out) out.textContent = on
        ? 'The objection found a case where the blocks hold and the cake still falls. The premises did not guarantee the conclusion.'
        : 'Each premise is a block. If the blocks guarantee the conclusion, the cake stays up.';
    }
    if (obj) obj.addEventListener('click', function () { set(true); });
    if (rst) rst.addEventListener('click', function () { set(false); });
  }

  /* ----- later session slots: show a quote block only when it has content ----- */
  $$('.session-quote').forEach(function (q) { if (q.textContent.replace(/\s+/g, '') !== '') q.removeAttribute('hidden'); });

  /* ----- an unfilled next-steps slot must not show its marker: hide that section and its rail link ----- */
  $$('ol.todo li').forEach(function (li) {
    if (li.textContent.indexOf('SLOT:next-steps') === -1) return;
    var sec = li.closest('section');
    if (!sec) return;
    sec.setAttribute('hidden', '');
    if (sec.id) { var a = $('.rail a[href="#' + sec.id + '"]'); if (a && a.parentNode) a.parentNode.setAttribute('hidden', ''); }
  });

  /* ----- rail marker: the shell counts hidden sections too, so recompute it among the visible ones ----- */
  var railBusy = false;
  function updateRail() {
    railBusy = false;
    var links = $$('.rail ol li a'), secs = $$('main > section');
    if (!links.length) return;
    var line = window.innerHeight * 0.4, current = -1;
    secs.forEach(function (s, i) { if (!s.hasAttribute('hidden') && s.getBoundingClientRect().top < line) current = i; });
    links.forEach(function (a, i) { a.classList.toggle('on', i === current); });
  }
  function queueRail() { if (!railBusy) { railBusy = true; requestAnimationFrame(updateRail); } }
  window.addEventListener('scroll', queueRail, { passive: true });
  window.addEventListener('resize', queueRail);
  queueRail();

  applyFilter('all');
})();
