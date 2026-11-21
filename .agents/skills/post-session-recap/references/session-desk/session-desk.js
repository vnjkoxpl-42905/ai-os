(function(){
  var doc = document, root = doc.documentElement;
  root.classList.add('js');
  var calm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var each = function(sel, fn, scope){ Array.prototype.forEach.call((scope || doc).querySelectorAll(sel), fn); };
  var press = function(el, fn){
    el.addEventListener('click', fn);
    if (el.tagName !== 'BUTTON') el.addEventListener('keydown', function(e){
      if (e.key === 'Enter' || e.key === ' ' || e.key === 'Spacebar') { e.preventDefault(); fn(); }
    });
  };

  /* tap-to-check rows, with a tally per drill */
  each('.drill', function(drill){
    var chips = drill.querySelectorAll('.chip'), head = drill.querySelector('.drill-head');
    var tally = doc.createElement('div'); tally.className = 'tally';
    var pips = doc.createElement('span'); pips.className = 'pips'; pips.setAttribute('aria-hidden', 'true');
    var count = doc.createElement('span'); count.setAttribute('aria-live', 'polite');
    Array.prototype.forEach.call(chips, function(){ pips.appendChild(doc.createElement('i')); });
    tally.appendChild(pips); tally.appendChild(count);
    if (head) head.appendChild(tally);
    function refresh(){
      var n = drill.querySelectorAll('.chip.on').length;
      count.textContent = n + ' of ' + chips.length + ' checked';
      Array.prototype.forEach.call(pips.children, function(p, i){ p.classList.toggle('on', i < n); });
    }
    Array.prototype.forEach.call(chips, function(c){
      var cue = doc.createElement('span'); cue.className = 'cue'; cue.setAttribute('aria-hidden', 'true'); cue.textContent = 'Tap';
      c.insertBefore(cue, c.querySelector('.stamp'));
      press(c, function(){
        var on = c.classList.toggle('on');
        c.setAttribute('aria-expanded', on ? 'true' : 'false');
        refresh();
      });
    });
    refresh();
  });

  /* two switches and a lamp */
  each('.gate', function(gate){
    var sw = gate.querySelectorAll('.sw');
    Array.prototype.forEach.call(sw, function(b){
      press(b, function(){
        b.setAttribute('aria-checked', b.getAttribute('aria-checked') === 'true' ? 'false' : 'true');
        var a = sw[0].getAttribute('aria-checked') === 'true', c = sw[1].getAttribute('aria-checked') === 'true';
        gate.setAttribute('data-state', a && c ? 3 : a ? 1 : c ? 2 : 0);
      });
    });
  });

  /* pivot tags get a turn arrow */
  each('.flag', function(f){
    f.insertAdjacentHTML('afterbegin', '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 14 4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/></svg>');
  });

  /* steps the student can tick, remembered on this device when storage is allowed */
  var marker = (doc.querySelector('meta[name="lsatu-interactive-lesson"]') || {}).content || 'recap';
  var store = { get: function(k){ try { return localStorage.getItem(k); } catch (e) { return null; } },
                set: function(k, v){ try { localStorage.setItem(k, v); } catch (e) {} } };
  each('ol.todo > li', function(li, i){
    var key = marker + ':todo:' + i, b = doc.createElement('button');
    b.type = 'button'; b.className = 'tick'; b.setAttribute('role', 'checkbox');
    b.setAttribute('aria-label', 'Step ' + (i + 1) + ' done');
    b.innerHTML = '<span>' + (i + 1) + '</span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5 10 17.5 19 7"/></svg>';
    function set(on){ b.setAttribute('aria-checked', on ? 'true' : 'false'); li.classList.toggle('done', on); }
    set(store.get(key) === '1');
    b.addEventListener('click', function(){ var on = b.getAttribute('aria-checked') !== 'true'; set(on); store.set(key, on ? '1' : '0'); });
    li.classList.add('has-tick'); li.insertBefore(b, li.firstChild);
  });

  /* section rail and reading progress, built from the section kickers */
  var rail = doc.querySelector('.rail ol'), links = [], sections = doc.querySelectorAll('main > section');
  Array.prototype.forEach.call(sections, function(s, i){
    s.id = s.id || 'part-' + (i + 1);
    var k = s.querySelector('.sec-kicker'), li = doc.createElement('li'), a = doc.createElement('a');
    var h = s.querySelector('h2');
    a.href = '#' + s.id; a.textContent = (k && k.textContent.trim()) || (h && h.textContent) || 'Part ' + (i + 1);
    li.appendChild(a); rail.appendChild(li); links.push(a);
    if (!calm) s.classList.add('reveal');
  });
  var bar = doc.querySelector('.progress i'), ticking = false;
  function onScroll(){
    ticking = false;
    var max = root.scrollHeight - window.innerHeight;
    bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0) + ')';
    var current = -1, line = window.innerHeight * 0.4;
    Array.prototype.forEach.call(sections, function(s, i){ if (s.getBoundingClientRect().top < line) current = i; });
    links.forEach(function(a, i){ a.classList.toggle('on', i === current); });
  }
  window.addEventListener('scroll', function(){ if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  if (!calm && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.04 });
    each('.reveal', function(el){ io.observe(el); });
  } else { each('.reveal', function(el){ el.classList.add('in'); }); }

  /* objects lean toward the pointer */
  if (!calm && window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    each('[data-tilt]', function(el){
      var max = parseFloat(el.getAttribute('data-tilt')) || 6, host = el.classList.contains('stack') ? el.parentNode : el;
      host.addEventListener('pointermove', function(e){
        var r = host.getBoundingClientRect();
        el.style.setProperty('--ry', (((e.clientX - r.left) / r.width) - 0.5) * 2 * max + 'deg');
        el.style.setProperty('--rx', (0.5 - ((e.clientY - r.top) / r.height)) * 2 * max + 'deg');
      });
      host.addEventListener('pointerleave', function(){ el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg'); });
    });
  }
})();
