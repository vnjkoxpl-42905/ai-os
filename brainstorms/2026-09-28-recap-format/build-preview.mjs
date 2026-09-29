import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { marked } from "file:///C:/Program%20Files/WindowsApps/OpenAI.CodexPrimaryRuntime.v26-923-495-0_26.923.495.0_x64__3k8sg7r9htsxt/dependencies/node/node_modules/marked/lib/marked.esm.js";

const here = path.dirname(fileURLToPath(import.meta.url));
const source = fs.readFileSync(path.join(here, "07-quantity-statements-lesson.md"), "utf8");
const noteBody = source.replace(/^# Some, Most, and All\s*\n/, "");
const withReveals = noteBody.replace(
  /<details><summary>(.*?)<\/summary>\s*([\s\S]*?)\s*<\/details>/g,
  (_match, summary, answer) =>
    `<details class="quantity-answer"><summary>${summary}</summary><div class="quantity-answer-body">${marked.parse(answer)}</div></details>`,
);
const contentHtml = marked.parse(withReveals).replace(/<p><img([^>]+)><\/p>/g, "<figure><img$1></figure>");
const appCss = pathToFileURL(path.resolve(here, "../../projects/lsatu/src/components/classroom/classroom.css")).href;

const noteCss = `
  .classroom-root .quantity-note { padding-bottom: 80px; }
  .classroom-root .quantity-note h2 { margin-top: 56px; padding-top: 18px; border-top: 1px solid var(--classroom-line); font-size: 23px; }
  .classroom-root .quantity-note h2:first-of-type { margin-top: 34px; }
  .classroom-root .quantity-note p { margin-bottom: 20px; }
  .classroom-root .quantity-note strong { font-weight: 700; color: var(--classroom-ink); }
  .classroom-root .quantity-note blockquote { background: #f8f5ee; border-left: 4px solid #087e83; border-radius: 0 10px 10px 0; padding: 14px 18px 2px; }
  .classroom-root .quantity-note blockquote p { margin-bottom: 12px; }
  .classroom-root .quantity-note img { display: block; width: min(100%, 720px); height: auto; border-radius: 16px; margin: 28px 0 30px; border: 1px solid var(--classroom-line); }
  .classroom-root .quantity-note pre { background: #f8f5ee; border: 1px solid #e6e6e0; border-radius: 12px; color: #173047; overflow-x: auto; padding: 18px 20px; margin: 18px 0 28px; font-size: 15px; line-height: 1.7; }
  .classroom-root .quantity-note code { font-family: 'IBM Plex Mono', Consolas, monospace; }
  .classroom-root .quantity-note table { border-collapse: collapse; width: min(720px, 100%); margin: 24px 0 32px; font-size: 15px; line-height: 1.5; }
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
  @media (max-width: 1023px) { .preview-stamp { top: 8px; right: 10px; } }
  html.dark .classroom-root .quantity-note blockquote, html.dark .classroom-root .quantity-note pre, html.dark .classroom-root .quantity-note th { background: #1d1c28; color: #e5e5e5; }
  html.dark .classroom-root .quantity-note .quantity-answer { background: #0a0913; border-color: #3d3c48; }
  html.dark .classroom-root .quantity-note .quantity-answer summary { color: #7bd5d2; }
  html.dark .classroom-root .quantity-note td, html.dark .classroom-root .quantity-note th { border-color: #3d3c48; }
`;

const page = `<!doctype html>
<html lang="en"><head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Some, Most, and All | LSAT U draft preview</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="${appCss}" rel="stylesheet">
  <style>html,body{margin:0;min-height:100%;}body{background:#fff;} ${noteCss}</style>
</head><body>
<span class="preview-stamp">Local draft preview</span>
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
    <p class="preview-note">Draft visual preview. The answer panels below can be opened.</p>
    <article class="classroom-prose quantity-note"><style>${noteCss}</style>${contentHtml}</article>
    <div class="classroom-detail-actions"><button class="classroom-button classroom-button-primary" type="button" disabled>Ask</button><button class="classroom-button" type="button" disabled>Back to notes</button></div>
  </div></main>
</div>
<script>if(new URLSearchParams(location.search).get('theme')==='dark')document.documentElement.classList.add('dark')</script>
</body></html>`;

const out = path.join(here, "07-quantity-statements-preview.html");
fs.writeFileSync(out, page, "utf8");
console.log(out);
