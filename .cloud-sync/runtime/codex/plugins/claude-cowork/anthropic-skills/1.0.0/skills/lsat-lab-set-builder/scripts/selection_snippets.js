/* Copy-paste JavaScript for the LSAT Lab browser step.
 * Run each block as a SEPARATE javascript_tool call (no in-script awaits for
 * pagination — they cause CDP timeouts). Return only numbers/strings, never
 * outerHTML or URLs (the bridge blocks "Cookie/query string data").
 */

/* 1) Set the question-bank table to show 100 rows per page. */
(() => {
  const t1 = document.querySelectorAll('table')[1];
  const wrapper = t1.closest('.dataTables_wrapper');
  const lenSel = wrapper.querySelector('select');
  lenSel.value = '100';
  lenSel.dispatchEvent(new Event('change', { bubbles: true }));
  return JSON.stringify({ rows: t1.querySelectorAll('tbody tr').length });
})();

/* 2) Stash targets + helpers on window. Replace the array with this set's
 *    Set_<n>_targets.json contents ("TEST-S-Q", PT stripped). */
(() => {
  window.__targets = new Set([/* "101-2-12", "101-2-13", ... */]);
  window.__rk = (tr) => {
    const td = tr.querySelectorAll('td');
    return [td[1].innerText.trim(), td[2].innerText.trim(), td[3].innerText.trim()].join('-');
  };
  window.__selected = window.__selected || new Set();
  return JSON.stringify({ targetCount: window.__targets.size });
})();

/* 3) PROCESS the current page: click checkboxes for matching, unselected rows.
 *    Run this once per page. */
(() => {
  const t1 = document.querySelectorAll('table')[1];
  const w = t1.closest('.dataTables_wrapper');
  let c = 0;
  [...t1.querySelectorAll('tbody tr')].forEach((tr) => {
    const k = window.__rk(tr);
    if (window.__targets.has(k) && !window.__selected.has(k)) {
      const cb = tr.querySelector('input[type=checkbox]');
      if (cb && !cb.checked) cb.click();
      window.__selected.add(k);
      c++;
    }
  });
  return JSON.stringify({
    active: w.querySelector('.paginate_button.active').innerText.trim(),
    added: c,
    total: window.__selected.size,
  });
})();

/* 4) ADVANCE one page. Run in a SEPARATE call from step 3, then go back to 3. */
(() => {
  const t1 = document.querySelectorAll('table')[1];
  t1.closest('.dataTables_wrapper').querySelector('.paginate_button.next').click();
  return 'clicked-next';
})();

/* 5) VERIFY across ALL rows (loaded client-side), regardless of page. */
(() => {
  const t1 = document.querySelectorAll('table')[1];
  const dt = window.jQuery(t1).DataTable();
  const checked = [];
  dt.rows().nodes().toArray().forEach((tr) => {
    const cb = tr.querySelector('input[type=checkbox]');
    const td = tr.querySelectorAll('td');
    if (cb && cb.checked) {
      checked.push([td[1].innerText.trim(), td[2].innerText.trim(), td[3].innerText.trim()].join('-'));
    }
  });
  const extras = checked.filter((k) => !window.__targets.has(k));
  const missing = [...window.__targets].filter((k) => !checked.includes(k));
  return JSON.stringify({ totalChecked: checked.length, extras, missing });
})();

/* 6) Diagnose a "missing" target: list available Q numbers for a TEST+S, e.g.
 *    to confirm 103-2-26 doesn't exist (max Q is 25). Edit the TEST/S below. */
(() => {
  const TEST = '103', S = '2';
  const t1 = document.querySelectorAll('table')[1];
  const dt = window.jQuery(t1).DataTable();
  const qs = [];
  dt.rows().nodes().toArray().forEach((tr) => {
    const td = tr.querySelectorAll('td');
    if (td.length > 3 && td[1].innerText.trim() === TEST && td[2].innerText.trim() === S) {
      qs.push(td[3].innerText.trim());
    }
  });
  return JSON.stringify({ test: TEST, section: S, questions: qs.sort((a, b) => a - b) });
})();
