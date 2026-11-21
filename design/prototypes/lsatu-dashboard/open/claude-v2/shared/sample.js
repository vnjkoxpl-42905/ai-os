/* LSAT U Home: shared sample data and the sample-state switcher.
   Prototype only. Nothing here talks to a backend; actions are simulated. */
(function () {
  const NOW = new Date(2026, 9, 22, 17, 12); // Thu Oct 22 2026, 5:12 pm

  const student = {
    name: 'Ada',
    now: NOW,
    testDay: new Date(2026, 10, 29),
    focus: {
      id: 'a-negation',
      kind: 'Activity',
      title: 'Negation Station',
      blurb: 'Negate each statement, then check whether it breaks the argument.',
      total: 12,
      done: 5,
      due: 'tonight at 11:59 pm',
      dueShort: 'Due tonight',
      action: 'Continue at prompt 6',
    },
    queue: [
      { id: 'a-flaw', kind: 'Guided drill', title: 'Flaw questions, guided set 3', meta: 'Due Friday at 9:00 pm', short: 'Fri 9:00 pm', isNew: true, action: 'Open', blurb: 'Eight flaw questions with a hint after each attempt.', total: 8, done: 0 },
      { id: 'a-notes', kind: 'From Joshua', title: "Read Joshua's notes on PT105 S2", meta: 'Assigned yesterday', short: 'No due date', isNew: true, action: 'Open', canMarkDone: true, blurb: 'Notes on the questions you flagged, with what to try next time.' },
      { id: 'a-recap', kind: 'Session recap', title: 'Session recap: sufficient and necessary', meta: 'Posted October 20', short: 'Posted Oct 20', isNew: true, action: 'Read', blurb: 'What we covered on Tuesday, with the three examples from the session.' },
    ],
    message: { from: 'Joshua', time: '9:12 am', text: 'Start with PT105 S2 before Thursday. Mark anything that felt like a guess.', unread: true },
    nextSession: { day: 'Saturday', date: 'Oct 24', time: '7:15 pm', with: 'Joshua' },
    week: [
      { dow: 'Thu', d: 22, today: true, items: [{ t: 'Negation Station', s: 'Due 11:59 pm', k: 'due' }] },
      { dow: 'Fri', d: 23, items: [{ t: 'Flaw questions, guided set 3', s: 'Due 9:00 pm', k: 'due' }] },
      { dow: 'Sat', d: 24, items: [{ t: 'Session with Joshua', s: '7:15 pm', k: 'session' }] },
      { dow: 'Sun', d: 25, items: [] },
      { dow: 'Mon', d: 26, items: [] },
      { dow: 'Tue', d: 27, items: [] },
      { dow: 'Wed', d: 28, items: [] },
    ],
  };

  const teacher = {
    name: 'Joshua',
    now: NOW,
    people: [
      { id: 's-dakota', name: 'Dakota Reyes', first: 'Dakota', active: 'Last active Oct 17', recency: 0.35,
        session: { when: 'Today at 6:00 pm', short: '6:00 pm', mins: 60, inMins: 48 } },
      { id: 's-celia', name: 'Celia Moreno', first: 'Celia', active: 'Active today', recency: 1,
        message: { time: '1:40 pm', text: 'Can we move Thursday to 7:30? I have a lab that runs late.', unread: true },
        session: { when: 'Tomorrow at 7:15 pm', short: 'Fri 7:15 pm', mins: 90 } },
      { id: 's-ivory', name: 'Ivory Chen', first: 'Ivory', active: 'Active today', recency: 1,
        message: { time: '11:02 am', text: 'Here is my PT105 S2 answer sheet. I flagged 14 and 22.', unread: true, attachment: 'PT105-S2-answers.pdf' } },
      { id: 's-lydia', name: 'Lydia Park', first: 'Lydia', active: 'Active yesterday', recency: 0.8,
        message: { time: 'Yesterday', text: 'Could we go over question 16 at our next session?', unread: true } },
    ],
    roster: [
      { name: 'Celia Moreno', last: 'Moreno', first: 'Celia', active: 'Active today', recency: 1 },
      { name: 'Ivory Chen', last: 'Chen', first: 'Ivory', active: 'Active today', recency: 1 },
      { name: 'Lydia Park', last: 'Park', first: 'Lydia', active: 'Active yesterday', recency: 0.8 },
      { name: 'Marcus Webb', last: 'Webb', first: 'Marcus', active: 'Active yesterday', recency: 0.8 },
      { name: 'Priya Nair', last: 'Nair', first: 'Priya', active: 'Active Oct 20', recency: 0.65 },
      { name: 'Tomás Ortega', last: 'Ortega', first: 'Tomás', active: 'Active Oct 19', recency: 0.55 },
      { name: 'Dakota Reyes', last: 'Reyes', first: 'Dakota', active: 'Last active Oct 17', recency: 0.35 },
      { name: 'Hannah Brooks', last: 'Brooks', first: 'Hannah', active: 'Last active Oct 16', recency: 0.3 },
      { name: 'Samuel Okafor', last: 'Okafor', first: 'Samuel', active: 'Last active Oct 14', recency: 0.25 },
      { name: 'Grace Lindqvist', last: 'Lindqvist', first: 'Grace', active: 'Last active Oct 11', recency: 0.18 },
      { name: 'Rafael Duarte', last: 'Duarte', first: 'Rafael', active: 'Last active Oct 9', recency: 0.12 },
      { name: 'Noor Haddad', last: 'Haddad', first: 'Noor', active: 'Last active Oct 2', recency: 0.06 },
    ],
    workTypes: ['Drill', 'Homework set', 'Activity', 'Timed section'],
    week: [
      { dow: 'Thu', d: 22, today: true, items: [{ t: 'Dakota Reyes', s: '6:00 pm, 60 min', k: 'session' }] },
      { dow: 'Fri', d: 23, items: [{ t: 'Celia Moreno', s: '7:15 pm, 90 min', k: 'session' }] },
      { dow: 'Sat', d: 24, items: [] },
      { dow: 'Sun', d: 25, items: [] },
      { dow: 'Mon', d: 26, items: [] },
      { dow: 'Tue', d: 27, items: [] },
      { dow: 'Wed', d: 28, items: [] },
    ],
  };

  const STATES = ['full', 'empty', 'loading', 'error'];
  function readState() {
    const q = new URLSearchParams(location.search).get('state');
    return STATES.includes(q) ? q : 'full';
  }

  const words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];
  const word = (n) => (n >= 0 && n < words.length ? words[n] : String(n));
  const Word = (n) => { const w = word(n); return w.charAt(0).toUpperCase() + w.slice(1); };
  const daysBetween = (a, b) => Math.round((new Date(b.getFullYear(), b.getMonth(), b.getDate()) - new Date(a.getFullYear(), a.getMonth(), a.getDate())) / 864e5);
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /* A small, quiet control so reviewers can see every state. */
  function mountSampleBar(opts) {
    const state = readState();
    const bar = document.createElement('aside');
    bar.className = 'sample-bar';
    bar.setAttribute('aria-label', 'Prototype controls');
    bar.innerHTML = `
      <span class="sample-bar__tag">Sample data</span>
      <label>State <select>${STATES.map((s) => `<option value="${s}"${s === state ? ' selected' : ''}>${s}</option>`).join('')}</select></label>
      <a href="${opts.other}">${opts.otherLabel}</a>
      <a href="../index.html">All directions</a>`;
    bar.querySelector('select').addEventListener('change', (e) => {
      const u = new URL(location.href);
      u.searchParams.set('state', e.target.value);
      location.href = u.toString();
    });
    document.body.appendChild(bar);
    const st = document.createElement('style');
    st.textContent = `.sample-bar{position:fixed;right:12px;bottom:12px;z-index:90;display:flex;flex-wrap:wrap;align-items:center;gap:10px;padding:8px 12px;border-radius:10px;background:rgba(20,20,22,.88);color:#eee;font:500 12px/1.2 system-ui,sans-serif;backdrop-filter:blur(8px);box-shadow:0 6px 24px rgba(0,0,0,.25);max-width:calc(100vw - 24px)}
    .sample-bar__tag{opacity:.7}.sample-bar select{font:inherit;background:#2a2a2e;color:#fff;border:1px solid #444;border-radius:6px;padding:3px 6px;margin-left:4px}
    .sample-bar a{color:#fff;text-underline-offset:3px}.sample-bar a:hover{color:#ffd28a}
    @media (max-width:520px){.sample-bar{left:8px;right:8px;bottom:8px;gap:8px;padding:6px 10px;font-size:11px;flex-wrap:nowrap;justify-content:space-between}.sample-bar__tag{display:none}.sample-bar a:last-child{display:none}}`;
    document.head.appendChild(st);
    return state;
  }

  /* Small shared toast for simulated actions. Styled per direction via .toast. */
  function toast(msg) {
    let t = document.querySelector('.toast');
    if (!t) {
      t = document.createElement('div');
      t.className = 'toast';
      t.setAttribute('role', 'status');
      t.setAttribute('aria-live', 'polite');
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.remove('is-on');
    void t.offsetWidth;
    t.classList.add('is-on');
    clearTimeout(t._h);
    t._h = setTimeout(() => t.classList.remove('is-on'), 2600);
  }

  const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  window.LSATU = { student, teacher, readState, mountSampleBar, toast, word, Word, daysBetween, esc, reduced, NOW };
})();
