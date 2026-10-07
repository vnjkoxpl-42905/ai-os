import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const here = path.dirname(new URL(import.meta.url).pathname.replace(/^\/(?=[A-Za-z]:)/, ''));
const require = createRequire(path.join(here, '../../projects/lsatu/package.json'));
const { JSDOM } = require('jsdom');
const source = fs.readFileSync(path.join(here, '08-quantity-statements-visual-preview.html'), 'utf8');
const document = new JSDOM(source).window.document;
const article = document.querySelector('article.quantity-note');
if (!article) throw new Error('Quantity lesson article missing');

for (const image of article.querySelectorAll('figure.quantity-figure img')) {
  const filename = path.basename(image.getAttribute('src'));
  const svg = fs.readFileSync(path.join(here, 'assets', filename), 'utf8')
    .replace(/<\?xml[^>]*>/, '')
    .replace(/<!DOCTYPE[^>]*>/, '');
  const figure = image.closest('figure');
  figure.setAttribute('role', 'img');
  figure.setAttribute('aria-label', image.getAttribute('alt'));
  image.outerHTML = svg;
}

const lab = article.querySelector('.quantity-lab');
lab.outerHTML = `<div class="quantity-static-range"><strong>One shelf. Three thresholds.</strong><span>Some <b>1–8</b></span><span>Most <b>5–8</b></span><span>All <b>8</b></span><small>Number of hardcover books out of eight.</small></div>`;

for (const check of article.querySelectorAll('.quantity-check')) {
  const answer = check.querySelector('.quantity-check-worked');
  if (!answer) throw new Error('Check lacks a worked answer');
  const details = document.createElement('details');
  details.className = 'quantity-answer';
  details.innerHTML = `<summary>Show the worked answer</summary><div>${answer.innerHTML}</div>`;
  check.querySelector('form')?.remove();
  check.querySelector('.quantity-check-result')?.remove();
  check.append(details);
}

article.querySelector('#quantity-overlap-shuffle')?.remove();
article.querySelector('.quantity-jump')?.remove();

const quiz = article.querySelector('#quantity-quiz');
if (!quiz) throw new Error('Cumulative quiz missing');
const quizQuestions = [
  [['Some A are B.', 'All B are C.'], 'Yes. The A that is B must also be C.'],
  [['Some A are B.', 'Most A are C.'], 'No. The A that is B could sit outside the C majority.'],
  [['All A are B.', 'Some B are C.'], 'No. The B that is C could be outside A.'],
  [['Some A are B.', 'Most B are C.'], 'No. The A that is B could be in the B minority that is not C.'],
  [['Some A are B.', 'Some B are C.'], 'No. The two statements may describe different Bs.'],
  [['Most A are B.', 'Most A are C.'], 'Yes. Two majorities of the same A group must overlap.'],
  [['All A are B.', 'All A are C.'], 'No. Neither statement guarantees that any A exists.'],
];
quiz.innerHTML = `<div class="quantity-quiz-top"><span class="quantity-quiz-eyebrow">Practice</span></div><h2>Can you prove the overlap?</h2><p>For each pair, decide whether some A must be C. Say why before opening the answer.</p>${quizQuestions.map(([premises, answer], index) => `<section class="quantity-quiz-card"><span>Question ${index + 1} / 7</span><p><strong>${premises[0]}</strong><br><strong>${premises[1]}</strong></p><details class="quantity-answer"><summary>Show the worked answer</summary><div><p>${answer}</p></div></details></section>`).join('')}`;

const css = `
.lsatu-quantity { color:#223544; font: 17px/1.68 Georgia,serif; max-width:760px; margin:auto; }
.lsatu-quantity * { box-sizing:border-box; }
.lsatu-quantity .quantity-note { width:100%; }
.lsatu-quantity h2,.lsatu-quantity h3,.lsatu-quantity strong,.lsatu-quantity summary,.lsatu-quantity .quantity-check-top,.lsatu-quantity .quantity-quiz-top { font-family:Arial,sans-serif; }
.lsatu-quantity h2 { color:#0f3645; font-size:1.58em; line-height:1.22; margin:2.2em 0 .65em; padding-top:.55em; border-top:2px solid #087c80; }
.lsatu-quantity h3 { color:#0d6268; font-size:1.1em; margin:1.6em 0 .5em; }
.lsatu-quantity p { margin:.8em 0 1.15em; }
.lsatu-quantity .quantity-lead { font-size:1.55em; line-height:1.35; color:#12344e; margin-top:0; }
.lsatu-quantity .quantity-claims { display:grid; gap:5px; margin:22px 0; }
.lsatu-quantity .quantity-claim { display:flex; gap:24px; padding:9px 13px; border-bottom:1px solid #d5e3e5; }
.lsatu-quantity .quantity-claim b { min-width:65px; color:#007e80; font-family:Arial,sans-serif; }
.lsatu-quantity .quantity-claim:nth-child(2) b { color:#af6816; }
.lsatu-quantity .quantity-claim:nth-child(3) b { color:#65509a; }
.lsatu-quantity .quantity-opening-question,.lsatu-quantity .quantity-static-range { border:1px solid #bed9dc; background:#f1f8f7; border-radius:14px; padding:17px 21px; margin:22px 0; }
.lsatu-quantity .quantity-opening-question p { margin:2px 0; font-family:Arial,sans-serif; font-weight:700; }
.lsatu-quantity .quantity-static-range { display:flex; flex-wrap:wrap; gap:8px 18px; font-family:Arial,sans-serif; }
.lsatu-quantity .quantity-static-range strong,.lsatu-quantity .quantity-static-range small { width:100%; }
.lsatu-quantity .quantity-static-range span { border-radius:30px; padding:4px 12px; background:#fff; border:1px solid #c9dddf; }
.lsatu-quantity .quantity-figure { margin:25px 0; padding:18px; border:1px solid #e6dcd0; border-radius:14px; background:#faf8f3; }
.lsatu-quantity .quantity-figure svg { display:block; width:100%; height:auto; max-height:460px; }
.lsatu-quantity pre { white-space:pre-wrap; overflow-wrap:anywhere; background:#eef5f4; color:#12344e; border-radius:9px; padding:14px; font-size:.82em; }
.lsatu-quantity blockquote { border-left:3px solid #007d7e; margin:23px 0; padding:4px 18px; background:#f5f9f8; }
.lsatu-quantity .quantity-chapter-number { color:#008184; font-size:.55em; vertical-align:middle; margin-right:.75em; }
.lsatu-quantity .quantity-check,.lsatu-quantity .quantity-quiz-card { border:1px solid #b8d7d8; border-radius:13px; padding:18px 21px; background:#f0f8f7; margin:24px 0; }
.lsatu-quantity .quantity-check-top,.lsatu-quantity .quantity-quiz-card>span { display:flex; justify-content:space-between; color:#007c7f; font-size:.73em; font-weight:700; text-transform:uppercase; letter-spacing:.09em; }
.lsatu-quantity .quantity-check-question { font-size:1.05em; }
.lsatu-quantity .quantity-answer { border:1px solid #b9d4d6; background:white; border-radius:8px; margin-top:14px; }
.lsatu-quantity .quantity-answer summary { cursor:pointer; color:#006a71; padding:9px 13px; font-size:.85em; font-weight:700; }
.lsatu-quantity .quantity-answer[open] summary { border-bottom:1px solid #d4e5e5; }
.lsatu-quantity .quantity-answer>div { padding:4px 14px; }
.lsatu-quantity .quantity-quiz { background:#072b39; color:#f0fbf8; padding:28px; border-radius:16px; margin:42px 0; }
.lsatu-quantity .quantity-quiz h2 { color:#fff; border:0; padding:0; margin:.4em 0; }
.lsatu-quantity .quantity-quiz-card { background:#123d4b; color:#fff; border-color:#568184; }
.lsatu-quantity .quantity-quiz-card>span { color:#90d5d2; }
.lsatu-quantity .quantity-quiz .quantity-answer { color:#12344e; }
.lsatu-quantity .quantity-overlap-footer button,.lsatu-quantity input,.lsatu-quantity textarea,.lsatu-quantity form { display:none; }
.lsatu-quantity [hidden] { display:none!important; }
@media(max-width:600px){.lsatu-quantity{font-size:16px}.lsatu-quantity .quantity-figure{padding:8px}.lsatu-quantity .quantity-quiz{padding:17px}.lsatu-quantity h2{font-size:1.35em}}
@media(prefers-reduced-motion:reduce){.lsatu-quantity *{animation:none!important;transition:none!important}}
`;
const output = `<div class="lsatu-quantity"><style>${css}</style>${article.outerHTML}</div>`;
const target = path.join(here, '09-quantity-statements-classroom.html');
fs.writeFileSync(target, output);
console.log(`${target} (${Buffer.byteLength(output)} bytes)`);
