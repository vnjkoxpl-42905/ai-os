(function(){
  var doc = document;
  var marker = (doc.querySelector('meta[name="lsatu-interactive-lesson"]') || {}).content || 'famous-flaws';
  var store = { get: function(k){ try { return localStorage.getItem(k); } catch (e) { return null; } },
                set: function(k, v){ try { localStorage.setItem(k, v); } catch (e) {} } };
  var flaws = doc.querySelectorAll('section.flaw');
  var total = flaws.length;

  /* rail: flaw names instead of kickers, with tier labels */
  var railLinks = {};
  Array.prototype.forEach.call(doc.querySelectorAll('.rail a'), function(a){
    var id = a.getAttribute('href').slice(1), s = doc.getElementById(id);
    if (!s) return;
    if (s.classList.contains('flaw')) {
      a.textContent = s.querySelector('h2').textContent;
      a.classList.add('flaw-link');
      railLinks[s.getAttribute('data-flaw')] = a;
    }
    if (s.classList.contains('tier')) {
      var li = doc.createElement('li'); li.className = 'rail-tier'; li.setAttribute('aria-hidden', 'true');
      li.textContent = s.querySelector('.sec-kicker').textContent;
      a.parentNode.parentNode.insertBefore(li, a.parentNode);
      a.parentNode.style.display = 'none';
    }
  });

  function refreshProgress(){
    var n = 0;
    for (var k in doneSet) n++;
    var p = doc.querySelector('.fi-progress');
    if (p) p.textContent = n + ' of ' + total + ' done';
  }

  var doneSet = {};
  function markDone(id){
    doneSet[id] = true;
    var a = doc.querySelector('.flaw-sheet a[data-flaw="' + id + '"]');
    if (a) { a.classList.add('done'); var sr = a.querySelector('.fi-sr'); if (sr) sr.textContent = 'done'; }
    if (railLinks[id]) railLinks[id].classList.add('done');
    refreshProgress();
  }

  Array.prototype.forEach.call(doc.querySelectorAll('.q'), function(q){
    var answer = q.getAttribute('data-answer'), id = q.getAttribute('data-flaw');
    var fb = q.querySelector('.qfb'), others = q.querySelector('.others'), list = others.querySelector('ul');
    var buttons = q.querySelectorAll('.choice');
    var actions = doc.createElement('div'); actions.className = 'qactions'; fb.parentNode.insertBefore(actions, fb.nextSibling);
    function exp(L){ var el = q.querySelector('.exp[data-l="' + L + '"]'); return el ? el.textContent : ''; }
    function action(label, fn){ var b = doc.createElement('button'); b.type = 'button'; b.className = 'qbtn'; b.textContent = label; b.addEventListener('click', fn); actions.appendChild(b); return b; }
    function feedback(kind, lead, body){
      fb.className = 'qfb ' + kind; fb.innerHTML = '';
      var l = doc.createElement('b'); l.textContent = lead; fb.appendChild(l); fb.appendChild(doc.createTextNode(body));
    }
    function clear(){
      q.classList.remove('solved');
      Array.prototype.forEach.call(buttons, function(x){ x.classList.remove('wrong', 'right'); x.setAttribute('aria-pressed', 'false'); });
      fb.className = 'qfb'; fb.innerHTML = ''; actions.innerHTML = ''; list.innerHTML = ''; others.hidden = true;
    }
    function reveal(picked){
      q.classList.add('solved');
      Array.prototype.forEach.call(buttons, function(x){
        var L = x.getAttribute('data-l');
        x.classList.toggle('right', L === answer);
        x.classList.toggle('wrong', L === picked && L !== answer);
        x.setAttribute('aria-pressed', L === picked ? 'true' : 'false');
      });
      if (picked === answer) feedback('is-right', 'Right: ' + answer + '. ', exp(answer));
      else feedback('is-wrong', 'The answer is ' + answer + '. ', exp(answer) + (picked ? ' You picked ' + picked + ': ' + exp(picked) : ''));
      list.innerHTML = '';
      Array.prototype.forEach.call(buttons, function(x){
        var L = x.getAttribute('data-l'); if (L === answer) return;
        var li = doc.createElement('li'), t = doc.createElement('b');
        t.textContent = L + '. '; li.appendChild(t); li.appendChild(doc.createTextNode(exp(L))); list.appendChild(li);
      });
      others.hidden = false;
      actions.innerHTML = '';
      action('Try it again', function(){ clear(); buttons[0].focus(); });
    }
    var lastWrong = null;
    Array.prototype.forEach.call(buttons, function(b){
      b.addEventListener('click', function(){
        if (q.classList.contains('solved')) return;
        var L = b.getAttribute('data-l');
        if (L === answer) { reveal(L); store.set(marker + ':done:' + id, '1'); markDone(id); return; }
        lastWrong = L;
        Array.prototype.forEach.call(buttons, function(x){ x.classList.remove('wrong'); x.setAttribute('aria-pressed', 'false'); });
        b.classList.add('wrong'); b.setAttribute('aria-pressed', 'true');
        feedback('is-wrong', 'Not ' + L + '. ', exp(L) + ' Try another choice.');
        actions.innerHTML = '';
        action('Show the answer', function(){ reveal(lastWrong); });
      });
    });
    if (store.get(marker + ':done:' + id) === '1') markDone(id);
  });
  refreshProgress();
})();
