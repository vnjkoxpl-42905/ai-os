import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "file:///C:/Program%20Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-923-495-0_26.923.495.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/marked/lib/marked.esm.js";

const here = path.dirname(fileURLToPath(import.meta.url));
const source = fs.readFileSync(path.join(here, "07-quantity-statements-lesson.md"), "utf8");
const noteBody = source.replace(/^# Some, Most, and All\s*\n/, "");
const withReveals = noteBody.replace(
  /<details><summary>(.*?)<\/summary>\s*([\s\S]*?)\s*<\/details>/g,
  (_match, summary, answer) =>
    `<details class="quantity-answer"><summary>${summary}</summary><div class="quantity-answer-body">${marked.parse(answer)}</div></details>`,
);
let contentHtml = marked.parse(withReveals).replace(/<p><img([^>]+)><\/p>/g, "<figure><img$1></figure>");
const firstLessonSection = contentHtml.indexOf("<h2>Some guarantees at least one</h2>");
if (firstLessonSection < 0) throw new Error("Could not find the first lesson section");
const introduction = `<header class="quantity-opening">
  <p class="quantity-lead">Quantity statements tell us whether a claim applies to some members of a group, most of them, or all of them.</p>
  <p class="quantity-scenario">Suppose a class has been assigned a case to read. These are three different claims about that same class:</p>
  <div class="quantity-claims" aria-label="Three claims about the same class">
    <div class="quantity-claim"><b>Some</b><span>students read it.</span></div>
    <div class="quantity-claim"><b>Most</b><span>students read it.</span></div>
    <div class="quantity-claim"><b>All</b><span>students read it.</span></div>
  </div>
  <p class="quantity-scenario">We do not need an exact headcount to understand the difference.</p>
  <div class="quantity-opening-question"><p>What must be true?</p><p>What could still be true?</p><small>The answer changes with the word we use.</small></div>
</header>
<nav class="quantity-jump" aria-label="Jump through the lesson"><a href="#some">Some</a><a href="#most">Most</a><a href="#all">All</a><a href="#inferences">Inferences</a><a href="#drill">Drill</a></nav>`;
contentHtml = introduction + contentHtml.slice(firstLessonSection);
for (const [label, id, index] of [
  ["Some guarantees at least one", "some", "01"],
  ["Most guarantees more than half", "most", "02"],
  ["All leaves no exception", "all", "03"],
]) contentHtml = contentHtml.replace(`<h2>${label}</h2>`, `<h2 id="${id}" class="quantity-chapter"><span class="quantity-chapter-number">${index}</span>${label}</h2>`);
contentHtml = contentHtml.replace("<h2>Carry a claim through an all rule</h2>", '<h2 id="inferences">Carry a claim through an all rule</h2>');
contentHtml = contentHtml.replace("<h2>Short drill: diagram, combine, decide</h2>", '<h2 id="drill">Short drill: diagram, combine, decide</h2>');
contentHtml = contentHtml.replace(/<p><strong>Try it:<\/strong>([\s\S]*?)<\/p>\s*(<details class="quantity-answer">[\s\S]*?<\/details>)/g, (_match, question, reveal) => `<aside class="quantity-check"><p class="quantity-check-question"><span>Try it</span>${question}</p>${reveal}</aside>`);
const summaryAt = contentHtml.indexOf("<h2>The moves to keep</h2>");
const drillAt = contentHtml.indexOf('<h2 id="drill">');
if (summaryAt < 0 || drillAt < 0) throw new Error("Could not find summary or drill");
contentHtml = contentHtml.slice(0, summaryAt) + '<section class="quantity-summary">' + contentHtml.slice(summaryAt, drillAt) + '</section><section class="quantity-drill">' + contentHtml.slice(drillAt) + '</section>';
const appCss = "../../projects/lsatu/src/components/classroom/classroom.css";

const noteCss = `
  .classroom-root .quantity-note { width: 100%; max-width: 720px; min-width: 0; padding-bottom: 80px; overflow-wrap: anywhere; }
  .classroom-root .quantity-note h2 { margin-top: 56px; padding-top: 18px; border-top: 1px solid var(--classroom-line); font-size: 23px; }
  .classroom-root .quantity-note h2:first-of-type { margin-top: 34px; }
  .classroom-root .quantity-note p { max-width: 56ch; margin-bottom: 20px; }
  .classroom-root .quantity-note strong { font-weight: 700; color: var(--classroom-ink); }
  .classroom-root .quantity-note blockquote { background: #f8f5ee; border-left: 4px solid #087e83; border-radius: 0 10px 10px 0; padding: 14px 18px 2px; }
  .classroom-root .quantity-note blockquote p { margin-bottom: 12px; }
  .classroom-root .quantity-note figure { width: 100%; margin: 28px 0 30px; }
  .classroom-root .quantity-note figure img { display: block; width: 100%; max-width: 100%; height: auto; border-radius: 16px; margin: 0; left: auto; right: auto; transform: none; border: 1px solid var(--classroom-line); }
  .classroom-root .quantity-note pre { background: #f8f5ee; border: 1px solid #e6e6e0; border-radius: 12px; color: #173047; overflow-x: auto; padding: 18px 20px; margin: 18px 0 28px; font-size: 15px; line-height: 1.7; }
  .classroom-root .quantity-note code { font-family: 'IBM Plex Mono', Consolas, monospace; }
  .classroom-root .quantity-note table { border-collapse: collapse; display: block; width: min(720px, 100%); max-width: 100%; overflow-x: auto; margin: 24px 0 32px; font-size: 15px; line-height: 1.5; }
  .classroom-root .quantity-note th { text-align: left; background: #f8f5ee; color: #173047; }
  .classroom-root .quantity-note td, .classroom-root .quantity-note th { border-bottom: 1px solid #dce2e3; padding: 11px 12px; vertical-align: top; }
  .classroom-root .quantity-note .quantity-answer { border: 1px solid #d8e4e6; border-radius: 12px; margin: -3px 0 28px; overflow: hidden; background: #fff; }
  .classroom-root .quantity-note .quantity-answer summary { cursor: pointer; color: #086d72; font-weight: 700; padding: 13px 17px; list-style-position: inside; }
  .classroom-root .quantity-note .quantity-answer summary:hover { background: #f1f8f8; }
  .classroom-root .quantity-note .quantity-answer[open] summary { border-bottom: 1px solid #d8e4e6; }
  .classroom-root .quantity-note .quantity-answer-body { padding: 16px 18px 1px; }
  .classroom-root .quantity-note .quantity-answer-body p { font-size: 15px; line-height: 1.65; }
  .classroom-root .quantity-note .quantity-answer-body pre { margin-top: 0; }
  .preview-stamp { position: fixed; top: 14px; right: 18px; z-index: 50; padding: 7px 11px; border-radius: 999px; color: #173047; background: #dff3f1; border: 1px solid #9dcfca; font: 700 12px 'Outfit', sans-serif; letter-spacing: .04em; text-transform: uppercase; }
  .preview-note { font-size: 13px; color: var(--classroom-meta-text); margin: -6px 0 28px; }
  .preview-rail-label { display: block; color: var(--classroom-meta-text); font: 600 11px 'IBM Plex Mono', monospace; letter-spacing: .07em; text-transform: uppercase; margin: 25px 8px 8px; }
  @media (max-width: 1023px) { .preview-stamp { top: 8px; right: 10px; } .classroom-root .classroom-column { min-width: 0; } }
  html.dark .classroom-root .quantity-note blockquote, html.dark .classroom-root .quantity-note pre, html.dark .classroom-root .quantity-note th { background: #1d1c28; color: #e5e5e5; }
  html.dark .classroom-root .quantity-note .quantity-answer { background: #0a0913; border-color: #3d3c48; }
  html.dark .classroom-root .quantity-note .quantity-answer summary { color: #7bd5d2; }
  html.dark .classroom-root .quantity-note td, html.dark .classroom-root .quantity-note th { border-color: #3d3c48; }

  /* Visual study: an editorial reading rhythm with distinct teaching moments. */
  .classroom-root .quantity-note > p,
  .classroom-root .quantity-note > section > p,
  .classroom-root .quantity-note .quantity-opening p,
  .classroom-root .quantity-note .quantity-check-question,
  .classroom-root .quantity-note .quantity-answer-body p {
    font-family: 'Source Serif 4', Georgia, serif;
    font-size: 18px;
    line-height: 1.67;
    font-weight: 400;
    letter-spacing: -0.005em;
  }
  .classroom-root .quantity-note h2 { font-family: 'Outfit',sans-serif; font-size: 25px; line-height: 1.25; margin-top: 65px; padding-top: 20px; border-top: 1px solid #d9e4e3; }
  .classroom-root .quantity-note .quantity-chapter { display: flex; align-items: baseline; gap: 18px; scroll-margin-top: 24px; }
  .classroom-root .quantity-note .quantity-chapter-number { color: #087e83; font: 600 13px 'IBM Plex Mono',Consolas,monospace; letter-spacing: .06em; }
  .classroom-root .quantity-note .quantity-opening { padding: 4px 0 0; }
  .classroom-root .quantity-note .quantity-opening .quantity-lead { max-width: 37ch; color: #173047; font-size: 25px; line-height: 1.38; margin-bottom: 29px; }
  .classroom-root .quantity-note .quantity-scenario { color: var(--classroom-ink-body); max-width: 55ch; margin-bottom: 17px; }
  .classroom-root .quantity-note .quantity-claims { border-top: 1px solid #cadcdd; border-bottom: 1px solid #cadcdd; margin: 22px 0 26px; max-width: 590px; }
  .classroom-root .quantity-note .quantity-claim { display: grid; grid-template-columns: 100px 1fr; align-items: baseline; gap: 16px; padding: 11px 4px; font-family: 'Source Serif 4', Georgia, serif; font-size: 19px; line-height: 1.45; }
  .classroom-root .quantity-note .quantity-claim + .quantity-claim { border-top: 1px solid #e2eceb; }
  .classroom-root .quantity-note .quantity-claim b { color: #087e83; font: 700 23px 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-opening-question { border-left: 4px solid #087e83; background: #eff8f7; padding: 17px 22px 16px; max-width: 590px; margin: 22px 0 33px; }
  .classroom-root .quantity-note .quantity-opening-question p { color: #173047; font-size: 20px; font-weight: 600; line-height: 1.4; margin: 0; }
  .classroom-root .quantity-note .quantity-opening-question small { color: #45656a; display: block; font: 500 13px 'Outfit',sans-serif; margin-top: 12px; }
  .classroom-root .quantity-note .quantity-jump { display: flex; flex-wrap: wrap; gap: 0; border-bottom: 1px solid #d9e4e3; margin: 20px 0 42px; }
  .classroom-root .quantity-note .quantity-jump a { color: #536366; font: 600 14px 'Outfit',sans-serif; padding: 10px 15px 13px; border-bottom: 2px solid transparent; }
  .classroom-root .quantity-note .quantity-jump a:first-child { padding-left: 0; }
  .classroom-root .quantity-note .quantity-jump a:hover,
  .classroom-root .quantity-note .quantity-jump a:focus-visible { color: #087e83; border-bottom-color: #087e83; outline-offset: 2px; }
  .classroom-root .quantity-note pre { border-left: 4px solid #087e83; border-radius: 0 9px 9px 0; background: #f4f8f8; font-size: 16px; line-height: 1.8; }
  .classroom-root .quantity-note .quantity-check { background: #f1f8f7; border: 1px solid #c6dfdc; border-radius: 14px; padding: 20px 22px 2px; max-width: 620px; margin: 30px 0 34px; }
  .classroom-root .quantity-note .quantity-check-question { margin: 0 0 14px; max-width: none; }
  .classroom-root .quantity-note .quantity-check-question > span { display: block; color: #087e83; font: 700 13px 'Outfit',sans-serif; letter-spacing: .02em; margin-bottom: 7px; }
  .classroom-root .quantity-note .quantity-check .quantity-answer { margin: 0 0 19px; background: #fff; border-color: #b5d1cd; }
  .classroom-root .quantity-note .quantity-check .quantity-answer summary { color: #075d63; padding: 10px 15px; font-size: 14px; }
  .classroom-root .quantity-note .quantity-check .quantity-answer-body p { font-size: 16px; }
  .classroom-root .quantity-note .quantity-summary { border: 1px solid #c9dddb; border-radius: 15px; padding: 0 28px 14px; margin: 65px 0 30px; }
  .classroom-root .quantity-note .quantity-summary h2 { margin-top: 0; border-top: 0; padding-top: 28px; }
  .classroom-root .quantity-note .quantity-summary table { margin-top: 16px; }
  .classroom-root .quantity-note .quantity-summary th { background: #eff8f7; }
  .classroom-root .quantity-note .quantity-drill { margin: 70px 0 20px; padding: 8px 28px 28px; background: #f7f9f8; border-top: 5px solid #087e83; }
  .classroom-root .quantity-note .quantity-drill h2 { margin-top: 0; border-top: 0; padding-top: 21px; }
  .classroom-root .quantity-note .quantity-drill > ol { counter-reset: drill; list-style: none; padding-left: 0; max-width: 620px; }
  .classroom-root .quantity-note .quantity-drill > ol li { background: #fff; border-bottom: 1px solid #dce7e5; margin: 0; padding: 12px 16px 12px 46px; position: relative; }
  .classroom-root .quantity-note .quantity-drill > ol li::before { counter-increment: drill; content: counter(drill) "."; color: #087e83; font: 700 14px 'IBM Plex Mono',Consolas,monospace; left: 15px; position: absolute; top: 14px; }
  .classroom-root .quantity-note .quantity-drill > ol li:first-child { border-top: 1px solid #dce7e5; }
  .classroom-root .quantity-note .quantity-drill > .quantity-answer { margin-top: 24px; }
  @media (max-width: 600px) {
    .classroom-root .quantity-note .quantity-opening .quantity-lead { font-size: 22px; }
    .classroom-root .quantity-note .quantity-claim { grid-template-columns: 80px 1fr; gap: 8px; font-size: 17px; }
    .classroom-root .quantity-note .quantity-claim b { font-size: 20px; }
    .classroom-root .quantity-note .quantity-jump a { padding: 9px 10px; }
    .classroom-root .quantity-note .quantity-check,
    .classroom-root .quantity-note .quantity-summary,
    .classroom-root .quantity-note .quantity-drill { padding-left: 16px; padding-right: 16px; }
  }
  html.dark .classroom-root .quantity-note .quantity-opening .quantity-lead { color: #e5f3f2; }
  html.dark .classroom-root .quantity-note .quantity-opening-question,
  html.dark .classroom-root .quantity-note .quantity-check,
  html.dark .classroom-root .quantity-note .quantity-drill { background: #142326; }
  html.dark .classroom-root .quantity-note .quantity-summary { border-color: #315456; }
  html.dark .classroom-root .quantity-note .quantity-claim b,
  html.dark .classroom-root .quantity-note .quantity-chapter-number { color: #7bd5d2; }
`;

const page = `<!doctype html>
<html lang="en"><head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Some, Most, and All | LSAT U visual study</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Outfit:wght@400;500;600;700&family=Source+Serif+4:wght@400;600;700&display=swap" rel="stylesheet">
  <link href="${appCss}" rel="stylesheet">
  <style>html,body{margin:0;min-height:100%;}body{background:#fff;} ${noteCss}</style>
</head><body>
<span class="preview-stamp">Visual study preview</span>
<div class="classroom-root">
  <aside class="classroom-sidebar"><div class="classroom-sidebar-card"><div class="classroom-panel-inner">
    <div class="classroom-brand"><i>U</i><span>LSAT U</span></div>
    <span class="preview-rail-label">Classroom</span>
    <div class="classroom-nav-group">
      <div class="classroom-nav">Home</div>
      <div class="classroom-nav classroom-nav-active">Notes and recaps</div>
      <div class="classroom-nav">Assigned work</div>
      <div class="classroom-nav">Flagged</div>
      <div class="classroom-nav">Wrong answers</div>
    </div>
    <span class="preview-rail-label">Preview</span>
    <p style="font-size:13px;line-height:1.6;color:var(--classroom-meta-text);padding:0 8px">This shows the draft in the Classroom reading layout. Nothing has been posted to a student.</p>
  </div></div></aside>
  <main class="classroom-stage"><div class="classroom-column">
    <div class="classroom-dateline"><time>September 29, 2026</time><span>|</span><span>Note</span></div>
    <h1 class="classroom-title">Some, Most, and All</h1>
    <p class="preview-note">An alternate visual treatment for review. The answer panels can be opened.</p>
    <article class="classroom-prose quantity-note"><style>${noteCss}</style>${contentHtml}</article>
    <div class="classroom-detail-actions"><button class="classroom-button classroom-button-primary" type="button" disabled>Ask</button><button class="classroom-button" type="button" disabled>Back to notes</button></div>
  </div></main>
</div>
<script>if(new URLSearchParams(location.search).get('theme')==='dark')document.documentElement.classList.add('dark')</script>
</body></html>`;

const out = path.join(here, "08-quantity-statements-visual-preview.html");
fs.writeFileSync(out, page, "utf8");
console.log(out);
