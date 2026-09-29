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
  <div class="quantity-lab" aria-label="Explore quantity statements with eight books">
    <div class="quantity-lab-head"><span class="quantity-lab-kicker">A little experiment</span><span class="quantity-lab-count" aria-live="polite"><b id="quantity-count">1</b> of 8 books are hardcover</span></div>
    <div class="quantity-lab-books" aria-hidden="true">${Array.from({ length: 8 }, (_, index) => `<span class="quantity-lab-book${index === 0 ? " is-hardcover" : ""}"><i></i></span>`).join("")}</div>
    <label class="quantity-lab-instruction" for="quantity-slider">Move the count. Watch which statements become true.</label>
    <input id="quantity-slider" class="quantity-lab-slider" type="range" min="0" max="8" value="1" aria-label="Number of hardcover books">
    <div class="quantity-lab-verdicts" aria-live="polite"><span data-rule="some" class="is-true"><i></i>Some</span><span data-rule="most"><i></i>Most</span><span data-rule="all"><i></i>All</span></div>
  </div>
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
contentHtml = contentHtml.replace(/<p><strong>(Try it|Quick check):<\/strong>([\s\S]*?)<\/p>\s*(<details class="quantity-answer">[\s\S]*?<\/details>)/g, (_match, label, question, reveal) => `<aside class="quantity-check"><p class="quantity-check-question"><span>${label}</span>${question}</p>${reveal}</aside>`);
const quizQuestions = [
  { premises: ["Some A are B.", "All B are C."], answer: "yes", explanation: "The A that is B must also be C because every B is C. That one A proves the overlap." },
  { premises: ["Some A are B.", "Most A are C."], answer: "no", explanation: "The A that is B could be outside the majority of A that is C. Those parts of A can miss each other." },
  { premises: ["All A are B.", "Some B are C."], answer: "no", explanation: "The B that is C could be outside A. The all rule points from A to B, not back from B to A." },
  { premises: ["Some A are B.", "Most B are C."], answer: "no", explanation: "The known A that is B could be among the B that are not C. A majority of B does not tell us which B are C." },
  { premises: ["Some A are B.", "Some B are C."], answer: "no", explanation: "The B in the first statement could differ from the B in the second. Two some claims need not share a witness." },
  { premises: ["Most A are B.", "Most A are C."], answer: "yes", explanation: "Both majorities count the same A group. They must share at least one A, and that person or thing is both B and C." },
  { premises: ["All A are B.", "All A are C."], answer: "no", explanation: "Every A would be both B and C, but neither all claim tells us an A exists. Add at least one A, and the overlap follows." },
];
const quizMarkup = `<section class="quantity-quiz" id="quantity-quiz" aria-labelledby="quantity-quiz-title">
  <div class="quantity-quiz-top"><span class="quantity-quiz-eyebrow">Inference studio</span><span class="quantity-quiz-progress" id="quantity-quiz-progress">01 / 07</span></div>
  <div class="quantity-quiz-track" aria-hidden="true"><span id="quantity-quiz-track-fill"></span></div>
  <h3 id="quantity-quiz-title">Can you prove the overlap?</h3>
  <p class="quantity-quiz-intro">Seven short answers. Make a call, explain it, then compare your reasoning.</p>
  <div class="quantity-quiz-stage">
    <div class="quantity-quiz-premises" id="quantity-quiz-premises"><span>Given</span><strong>Some A are B.</strong><strong>All B are C.</strong></div>
    <div class="quantity-quiz-bridge" id="quantity-quiz-bridge" aria-hidden="true"><span>A</span><i></i><span>C</span></div>
    <form id="quantity-quiz-form" class="quantity-quiz-form">
      <label for="quantity-quiz-input">Must some A be C?</label>
      <p>Start with <b>Yes</b> or <b>No</b>, then tell me why.</p>
      <textarea id="quantity-quiz-input" rows="3" placeholder="No, because…" required></textarea>
      <div class="quantity-quiz-actions"><button type="submit">Check my answer <span aria-hidden="true">↗</span></button><span id="quantity-quiz-error" role="alert"></span></div>
    </form>
    <div class="quantity-quiz-feedback" id="quantity-quiz-feedback" hidden tabindex="-1" aria-live="polite">
      <div class="quantity-quiz-feedback-label" id="quantity-quiz-feedback-label"></div>
      <p class="quantity-quiz-verdict" id="quantity-quiz-verdict"></p>
      <p class="quantity-quiz-explanation" id="quantity-quiz-explanation"></p>
      <p class="quantity-quiz-reflection">Compare your explanation with this one. Did you identify the same person or the same gap?</p>
      <button class="quantity-quiz-next" id="quantity-quiz-next" type="button">Next question <span aria-hidden="true">→</span></button>
    </div>
  </div>
  <div class="quantity-quiz-done" id="quantity-quiz-done" hidden><span>Practice complete</span><strong id="quantity-quiz-score"></strong><p>You checked each conclusion against a witness or a possible gap. Review any answer where your reason differed, even if your yes or no matched.</p><button id="quantity-quiz-restart" type="button">Try the seven again ↺</button></div>
</section>`;
const quizStart = contentHtml.indexOf("<h3>Pop quiz: decide whether the overlap follows</h3>");
const quizEnd = contentHtml.indexOf("</details>", quizStart);
if (quizStart < 0 || quizEnd < 0) throw new Error("Could not locate the pop quiz in the lesson");
contentHtml = contentHtml.slice(0, quizStart) + quizMarkup + contentHtml.slice(quizEnd + "</details>".length);
const summaryAt = contentHtml.indexOf("<h2>The moves to keep</h2>");
const drillAt = contentHtml.indexOf('<h2 id="drill">');
if (summaryAt < 0 || drillAt < 0) throw new Error("Could not find summary or drill");
contentHtml = contentHtml.slice(0, summaryAt) + '<section class="quantity-summary">' + contentHtml.slice(summaryAt, drillAt) + '</section><section class="quantity-drill">' + contentHtml.slice(drillAt) + '</section>';
const appCss = "../../projects/lsatu/src/components/classroom/classroom.css";

const noteCss = `
  :root { --quantity-ink: oklch(31% .045 225); --quantity-teal: oklch(52% .09 192); --quantity-warm: oklch(92% .03 75); }
  .quantity-progress { position: fixed; inset: 0 auto auto 0; height: 3px; width: 100%; transform-origin: left; transform: scaleX(0); background: var(--quantity-teal); z-index: 70; pointer-events: none; }
  .classroom-root .quantity-note { width: 100%; max-width: 720px; min-width: 0; padding-bottom: 80px; overflow-wrap: anywhere; }
  .classroom-root .quantity-note h2 { margin-top: 56px; padding-top: 18px; border-top: 1px solid var(--classroom-line); font-size: 23px; }
  .classroom-root .quantity-note h2:first-of-type { margin-top: 34px; }
  .classroom-root .quantity-note p { max-width: 56ch; margin-bottom: 20px; }
  .classroom-root .quantity-note strong { font-weight: 700; color: var(--classroom-ink); }
  .classroom-root .quantity-note blockquote { background: #f8f5ee; border: 1px solid #e4e0d6; border-radius: 10px; padding: 14px 18px 2px; }
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
  .classroom-root .quantity-note .quantity-opening-question { border: 1px solid #c6dfdc; border-radius: 12px; background: #eff8f7; padding: 17px 22px 16px; max-width: 590px; margin: 22px 0 33px; }
  .classroom-root .quantity-note .quantity-opening-question p { color: #173047; font-size: 20px; font-weight: 600; line-height: 1.4; margin: 0; }
  .classroom-root .quantity-note .quantity-opening-question small { color: #45656a; display: block; font: 500 13px 'Outfit',sans-serif; margin-top: 12px; }
  .classroom-root .quantity-note .quantity-lab { max-width: 620px; margin: 42px 0 22px; padding: 27px 29px 25px; border: 1px solid oklch(85% .025 198); border-radius: 16px; background: radial-gradient(circle at 84% 0%, var(--quantity-warm), transparent 36%), oklch(98% .008 187); }
  .classroom-root .quantity-note .quantity-lab-head { display: flex; align-items: baseline; justify-content: space-between; flex-wrap: wrap; gap: 8px 20px; font-family: 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-lab-kicker { text-transform: uppercase; letter-spacing: .11em; font: 700 12px 'IBM Plex Mono',monospace; color: var(--quantity-teal); }
  .classroom-root .quantity-note .quantity-lab-count { color: var(--quantity-ink); font-size: 16px; }
  .classroom-root .quantity-note .quantity-lab-count b { font-size: 27px; font-variant-numeric: tabular-nums; }
  .classroom-root .quantity-note .quantity-lab-books { display: flex; justify-content: space-between; align-items: end; gap: 6px; margin: 30px 0 27px; min-height: 72px; }
  .classroom-root .quantity-note .quantity-lab-book { flex: 1; max-width: 48px; height: 65px; border-radius: 3px 6px 6px 3px; background: oklch(88% .015 213); border: 1px solid oklch(73% .025 213); position: relative; transform: translateY(0); transition: background 240ms cubic-bezier(.19,1,.22,1), transform 240ms cubic-bezier(.19,1,.22,1), border-color 240ms; }
  .classroom-root .quantity-note .quantity-lab-book::before { content: ''; position: absolute; inset: 7px auto 7px 6px; width: 2px; background: currentColor; opacity: .45; }
  .classroom-root .quantity-note .quantity-lab-book i { position: absolute; left: 14px; right: 8px; top: 13px; border-top: 2px solid currentColor; box-shadow: 0 8px currentColor; opacity: .6; }
  .classroom-root .quantity-note .quantity-lab-book.is-hardcover { color: oklch(90% .03 192); border-color: oklch(44% .09 192); background: var(--quantity-teal); transform: translateY(-5px); }
  .classroom-root .quantity-note .quantity-lab-book.is-new::after { content: ''; position: absolute; inset: -10px; border-radius: 13px; background: oklch(82% .08 75 / .75); z-index: -1; animation: quantity-warm-pulse 650ms cubic-bezier(.19,1,.22,1) both; pointer-events: none; }
  @keyframes quantity-warm-pulse { from { opacity: .9; transform: scale(.8); } to { opacity: 0; transform: scale(1.22); } }
  .classroom-root .quantity-note .quantity-lab-instruction { display: block; color: var(--quantity-ink); font: 500 14px 'Outfit',sans-serif; margin-bottom: 12px; }
  .classroom-root .quantity-note .quantity-lab-slider { display: block; width: 100%; height: 30px; margin: 0; accent-color: var(--quantity-teal); cursor: pointer; }
  .classroom-root .quantity-note .quantity-lab-slider:focus-visible { outline: 2px solid var(--quantity-ink); outline-offset: 3px; }
  .classroom-root .quantity-note .quantity-lab-verdicts { display: flex; gap: 9px; flex-wrap: wrap; margin-top: 19px; }
  .classroom-root .quantity-note .quantity-lab-verdicts span { display: inline-flex; align-items: center; gap: 8px; border: 1px solid oklch(84% .015 213); border-radius: 999px; padding: 7px 12px; color: oklch(49% .02 213); font: 600 13px 'Outfit',sans-serif; background: oklch(96% .006 213); transition: background 220ms, color 220ms, border-color 220ms; }
  .classroom-root .quantity-note .quantity-lab-verdicts i { width: 7px; height: 7px; border-radius: 50%; background: currentColor; opacity: .5; }
  .classroom-root .quantity-note .quantity-lab-verdicts .is-true { color: var(--quantity-ink); border-color: oklch(73% .07 192); background: oklch(90% .045 192); }
  .classroom-root .quantity-note .quantity-lab-verdicts .is-true i { background: var(--quantity-teal); opacity: 1; }
  .classroom-root .quantity-note .quantity-lab-verdicts .is-new { animation: quantity-truth-pulse 550ms cubic-bezier(.19,1,.22,1) both; }
  @keyframes quantity-truth-pulse { 0% { transform: scale(.94); } 60% { transform: scale(1.06); } 100% { transform: scale(1); } }
  .classroom-root .quantity-note .quantity-jump { display: flex; flex-wrap: wrap; gap: 0; border-bottom: 1px solid #d9e4e3; margin: 20px 0 42px; }
  .classroom-root .quantity-note .quantity-jump a { color: #536366; font: 600 14px 'Outfit',sans-serif; padding: 10px 15px 13px; border-bottom: 2px solid transparent; }
  .classroom-root .quantity-note .quantity-jump a:first-child { padding-left: 0; }
  .classroom-root .quantity-note .quantity-jump a:hover,
  .classroom-root .quantity-note .quantity-jump a:focus-visible { color: #087e83; border-bottom-color: #087e83; outline-offset: 2px; }
  .classroom-root .quantity-note pre { border: 1px solid #c6dfdc; border-radius: 9px; background: #f4f8f8; font-size: 16px; line-height: 1.8; }
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
  .classroom-root .quantity-note .quantity-quiz { position: relative; isolation: isolate; overflow: hidden; max-width: none; margin: 58px -28px 55px; padding: 33px 40px 40px; border-radius: 18px; background: oklch(24% .043 224); color: oklch(96% .012 190); }
  .classroom-root .quantity-note .quantity-quiz [hidden] { display: none !important; }
  .classroom-root .quantity-note .quantity-quiz::before { content: ''; position: absolute; width: 420px; height: 420px; top: -230px; right: -170px; border-radius: 50%; background: radial-gradient(circle, oklch(59% .09 188 / .25), transparent 69%); z-index: -1; pointer-events: none; }
  .classroom-root .quantity-note .quantity-quiz-top { display: flex; justify-content: space-between; align-items: center; gap: 18px; color: oklch(77% .075 188); font: 600 12px 'IBM Plex Mono',monospace; letter-spacing: .11em; text-transform: uppercase; }
  .classroom-root .quantity-note .quantity-quiz-progress { font-variant-numeric: tabular-nums; color: oklch(90% .025 190); }
  .classroom-root .quantity-note .quantity-quiz-track { height: 2px; width: 100%; margin: 16px 0 34px; background: oklch(42% .035 224); }
  .classroom-root .quantity-note .quantity-quiz-track span { display: block; width: 14.285%; height: 100%; background: oklch(77% .08 188); transition: width 450ms cubic-bezier(.19,1,.22,1); }
  .classroom-root .quantity-note .quantity-quiz h3 { color: oklch(98% .007 190); font: 600 33px/1.13 'Outfit',sans-serif; letter-spacing: -.035em; margin: 0 0 10px; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-intro { color: oklch(78% .018 190); font: 400 16px/1.55 'Source Serif 4',Georgia,serif; margin: 0 0 36px; max-width: 56ch; }
  .classroom-root .quantity-note .quantity-quiz-stage { display: grid; grid-template-columns: minmax(0,1fr) minmax(0,1.05fr); column-gap: 38px; align-items: start; }
  .classroom-root .quantity-note .quantity-quiz-premises { grid-column: 1; display: grid; gap: 9px; padding: 23px 23px 25px; border: 1px solid oklch(53% .045 218); border-radius: 12px; background: oklch(29% .04 224); }
  .classroom-root .quantity-note .quantity-quiz-premises span { color: oklch(76% .065 188); text-transform: uppercase; letter-spacing: .11em; font: 600 11px 'IBM Plex Mono',monospace; margin-bottom: 6px; }
  .classroom-root .quantity-note .quantity-quiz-premises strong { color: oklch(97% .01 190); font: 500 21px/1.35 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-quiz-bridge { grid-column: 1; display: flex; align-items: center; justify-content: center; gap: 0; height: 100px; margin: 8px 0; }
  .classroom-root .quantity-note .quantity-quiz-bridge span { display: grid; place-items: center; width: 48px; height: 48px; border: 1px solid oklch(72% .08 188); border-radius: 50%; color: oklch(92% .03 188); font: 600 20px 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-quiz-bridge i { width: 85px; height: 1px; background: repeating-linear-gradient(90deg,oklch(70% .05 188) 0 6px,transparent 6px 13px); transform-origin: left; transition: background 350ms, transform 500ms cubic-bezier(.19,1,.22,1); }
  .classroom-root .quantity-note .quantity-quiz-bridge.is-yes i { height: 2px; background: oklch(77% .08 188); animation: quantity-bridge 500ms cubic-bezier(.19,1,.22,1) both; }
  .classroom-root .quantity-note .quantity-quiz-bridge.is-no i { opacity: .35; transform: scaleX(.68); }
  @keyframes quantity-bridge { from { transform: scaleX(0); } to { transform: scaleX(1); } }
  .classroom-root .quantity-note .quantity-quiz-form, .classroom-root .quantity-note .quantity-quiz-feedback { grid-column: 2; grid-row: 1 / span 2; }
  .classroom-root .quantity-note .quantity-quiz-form label { display: block; color: oklch(98% .007 190); font: 600 22px/1.3 'Outfit',sans-serif; margin: 1px 0 6px; }
  .classroom-root .quantity-note .quantity-quiz-form p { color: oklch(75% .018 190); font: 400 14px/1.5 'Outfit',sans-serif; margin: 0 0 17px; }
  .classroom-root .quantity-note .quantity-quiz-form textarea { box-sizing: border-box; width: 100%; min-height: 133px; resize: vertical; border: 1px solid oklch(60% .035 220); border-radius: 9px; padding: 15px 16px; background: oklch(31% .035 224); color: oklch(97% .01 190); font: 400 17px/1.5 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-quiz-form textarea::placeholder { color: oklch(72% .018 210); }
  .classroom-root .quantity-note .quantity-quiz-form textarea:focus-visible, .classroom-root .quantity-note .quantity-quiz button:focus-visible { outline: 2px solid oklch(84% .085 188); outline-offset: 3px; }
  .classroom-root .quantity-note .quantity-quiz-actions { display: flex; align-items: center; flex-wrap: wrap; gap: 13px; margin-top: 15px; }
  .classroom-root .quantity-note .quantity-quiz button { min-height: 44px; cursor: pointer; border: 0; border-radius: 7px; padding: 10px 17px; background: oklch(81% .065 187); color: oklch(21% .04 224); font: 700 14px 'Outfit',sans-serif; transition: background 180ms; }
  .classroom-root .quantity-note .quantity-quiz button:hover { background: oklch(91% .045 187); }
  .classroom-root .quantity-note .quantity-quiz-actions button span { margin-left: 16px; font-size: 17px; }
  .classroom-root .quantity-note .quantity-quiz-actions [role='alert'] { color: oklch(88% .1 35); font: 500 13px/1.4 'Outfit',sans-serif; }
  .classroom-root .quantity-note .quantity-quiz-feedback { border-top: 1px solid oklch(49% .04 220); padding-top: 18px; animation: quantity-feedback-enter 420ms cubic-bezier(.19,1,.22,1) both; }
  @keyframes quantity-feedback-enter { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
  .classroom-root .quantity-note .quantity-quiz-feedback-label { color: oklch(78% .08 188); text-transform: uppercase; letter-spacing: .09em; font: 700 11px 'IBM Plex Mono',monospace; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-verdict { color: oklch(98% .005 190); font: 600 24px/1.25 'Outfit',sans-serif; margin: 9px 0 11px; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-explanation { color: oklch(92% .016 190); font: 400 17px/1.55 'Source Serif 4',Georgia,serif; margin: 0 0 15px; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-reflection { color: oklch(75% .018 190); font: 400 13px/1.5 'Outfit',sans-serif; margin: 0 0 17px; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-next span { margin-left: 16px; }
  .classroom-root .quantity-note .quantity-quiz-done { padding: 13px 0 4px; }
  .classroom-root .quantity-note .quantity-quiz-done span { color: oklch(77% .08 188); text-transform: uppercase; letter-spacing: .1em; font: 700 12px 'IBM Plex Mono',monospace; }
  .classroom-root .quantity-note .quantity-quiz-done strong { display: block; color: oklch(98% .007 190); font: 600 38px/1.15 'Outfit',sans-serif; letter-spacing: -.03em; margin: 14px 0; }
  .classroom-root .quantity-note .quantity-quiz .quantity-quiz-done p { color: oklch(84% .015 190); font: 400 16px/1.55 'Source Serif 4',Georgia,serif; max-width: 60ch; }
  .classroom-root .quantity-note .quantity-quiz-done button { margin-top: 8px; }
  @media (max-width: 600px) {
    .classroom-root .quantity-note .quantity-quiz { margin-left: -12px; margin-right: -12px; padding: 23px 19px 29px; border-radius: 13px; }
    .classroom-root .quantity-note .quantity-quiz h3 { font-size: 29px; }
    .classroom-root .quantity-note .quantity-quiz-stage { display: flex; flex-direction: column; gap: 0; }
    .classroom-root .quantity-note .quantity-quiz-premises, .classroom-root .quantity-note .quantity-quiz-form, .classroom-root .quantity-note .quantity-quiz-feedback { width: 100%; box-sizing: border-box; }
    .classroom-root .quantity-note .quantity-quiz-bridge { align-self: center; height: 76px; }
    .classroom-root .quantity-note .quantity-lab { padding: 19px 17px; }
    .classroom-root .quantity-note .quantity-lab-books { gap: 4px; }
    .classroom-root .quantity-note .quantity-lab-book { height: 53px; }
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
  @media (prefers-reduced-motion: reduce) { .quantity-progress, .classroom-root .quantity-note .quantity-lab-book, .classroom-root .quantity-note .quantity-lab-verdicts span, .classroom-root .quantity-note .quantity-quiz * { transition: none !important; animation: none !important; } .classroom-root .quantity-note .quantity-lab-book.is-new::after { display: none; } }
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
<div class="quantity-progress" aria-hidden="true"></div>
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
    <p class="preview-note">Interactive draft. Move the book count and open the answers as you read.</p>
    <article class="classroom-prose quantity-note"><style>${noteCss}</style>${contentHtml}</article>
    <div class="classroom-detail-actions"><button class="classroom-button classroom-button-primary" type="button" disabled>Ask</button><button class="classroom-button" type="button" disabled>Back to notes</button></div>
  </div></main>
</div>
<script>
if(new URLSearchParams(location.search).get('theme')==='dark')document.documentElement.classList.add('dark');
const slider=document.getElementById('quantity-slider');
const count=document.getElementById('quantity-count');
const books=[...document.querySelectorAll('.quantity-lab-book')];
const rules={some:1,most:5,all:8};
slider.addEventListener('input',()=>{const value=Number(slider.value);count.textContent=value;books.forEach((book,index)=>{const was=book.classList.contains('is-hardcover');const now=index<value;book.classList.toggle('is-hardcover',now);if(now&&!was){book.classList.remove('is-new');void book.offsetWidth;book.classList.add('is-new');setTimeout(()=>book.classList.remove('is-new'),700)}});for(const [rule,minimum] of Object.entries(rules)){const pill=document.querySelector('[data-rule="'+rule+'"]');const was=pill.classList.contains('is-true');const now=value>=minimum;pill.classList.toggle('is-true',now);if(now&&!was){pill.classList.remove('is-new');void pill.offsetWidth;pill.classList.add('is-new');setTimeout(()=>pill.classList.remove('is-new'),600)}}});
const progress=document.querySelector('.quantity-progress');let pending=false;
function updateProgress(){const max=document.documentElement.scrollHeight-innerHeight;progress.style.transform='scaleX('+Math.max(0,Math.min(1,max>0?scrollY/max:0))+')';pending=false}
addEventListener('scroll',()=>{if(!pending){requestAnimationFrame(updateProgress);pending=true}},{passive:true});addEventListener('resize',updateProgress);updateProgress();
const quizQuestions=${JSON.stringify(quizQuestions)};
const quizForm=document.getElementById('quantity-quiz-form');
const quizInput=document.getElementById('quantity-quiz-input');
const quizFeedback=document.getElementById('quantity-quiz-feedback');
const quizStage=document.querySelector('.quantity-quiz-stage');
const quizDone=document.getElementById('quantity-quiz-done');
const quizBridge=document.getElementById('quantity-quiz-bridge');
let quizIndex=0,quizMatches=0;
function renderQuiz(){const q=quizQuestions[quizIndex];document.getElementById('quantity-quiz-progress').textContent=String(quizIndex+1).padStart(2,'0')+' / 07';document.getElementById('quantity-quiz-track-fill').style.width=((quizIndex+1)/quizQuestions.length*100)+'%';document.getElementById('quantity-quiz-premises').replaceChildren(Object.assign(document.createElement('span'),{textContent:'Given'}),...q.premises.map(line=>Object.assign(document.createElement('strong'),{textContent:line})));quizInput.value='';quizForm.hidden=false;quizFeedback.hidden=true;quizBridge.classList.remove('is-yes','is-no');document.getElementById('quantity-quiz-error').textContent='';}
quizForm.addEventListener('submit',event=>{event.preventDefault();const response=quizInput.value.trim();const choice=/^(yes|yeah|yep|no|not guaranteed|cannot|can't|does not|doesn't)\b/i.exec(response);if(!choice){document.getElementById('quantity-quiz-error').textContent='Begin with Yes or No, then give your reason.';quizInput.focus();return}const verdict=/^(yes|yeah|yep)/i.test(choice[1])?'yes':'no';const q=quizQuestions[quizIndex];const match=verdict===q.answer;if(match)quizMatches++;document.getElementById('quantity-quiz-error').textContent='';document.getElementById('quantity-quiz-feedback-label').textContent=match?'Your conclusion matches':'Your conclusion needs another look';document.getElementById('quantity-quiz-verdict').textContent=q.answer==='yes'?'Yes. The overlap follows.':'No. The overlap is not guaranteed.';document.getElementById('quantity-quiz-explanation').textContent=q.explanation;document.getElementById('quantity-quiz-next').innerHTML=quizIndex===quizQuestions.length-1?'See your review <span aria-hidden="true">→</span>':'Next question <span aria-hidden="true">→</span>';quizBridge.classList.add(q.answer==='yes'?'is-yes':'is-no');quizForm.hidden=true;quizFeedback.hidden=false;quizFeedback.focus();});
document.getElementById('quantity-quiz-next').addEventListener('click',()=>{if(quizIndex===quizQuestions.length-1){quizStage.hidden=true;quizDone.hidden=false;document.getElementById('quantity-quiz-score').textContent=quizMatches+' of 7 conclusions matched';document.getElementById('quantity-quiz-progress').textContent='07 / 07';}else{quizIndex++;renderQuiz();quizInput.focus()}});
document.getElementById('quantity-quiz-restart').addEventListener('click',()=>{quizIndex=0;quizMatches=0;quizDone.hidden=true;quizStage.hidden=false;renderQuiz();quizInput.focus()});
</script>
</body></html>`;

const out = path.join(here, "08-quantity-statements-visual-preview.html");
fs.writeFileSync(out, page, "utf8");
console.log(out);
