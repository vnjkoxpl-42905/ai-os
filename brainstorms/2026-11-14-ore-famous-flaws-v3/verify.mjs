import { readFileSync } from "node:fs";
const html = readFileSync(new URL("./out/famous-flaws.html", import.meta.url), "utf8");
const Q = JSON.parse(readFileSync(new URL("./src/questions.json", import.meta.url), "utf8"));
const fails = []; const ok = (c, m) => { if (!c) fails.push(m); };
const order = ["necessary-vs-sufficient","causal","part-vs-whole","unproven-vs-proven-false","ad-hominem","sampling","inappropriate-appeal","circular-reasoning","internal-contradiction","equivocation"];
const qkey = {"necessary-vs-sufficient":"nec",causal:"causal","part-vs-whole":"part","unproven-vs-proven-false":"unproven","ad-hominem":"adhom",sampling:"sampling","inappropriate-appeal":"appeal","circular-reasoning":"circular","internal-contradiction":"contradiction",equivocation:"equiv"};
const secs = [...html.matchAll(/<section class="flaw" id="f-([a-z-]+)" data-flaw="[a-z-]+" data-tier="(\d)">([\s\S]*?)<\/section>/g)];
ok(secs.length === 10, `expected 10 flaw sections, got ${secs.length}`);
ok(JSON.stringify(secs.map(s => s[1])) === JSON.stringify(order), "flaw order differs from handout");
ok(secs.filter(s => s[2] === "0").length === 5 && secs.filter(s => s[2] === "1").length === 5, "tiers not 5/5");
const unesc = s => s.replace(/<br>/g, "\n").replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
for (const [, id, , body] of secs) {
  for (const p of ["name","what","example","why","spot","wording","lookalike"]) ok(body.includes(`data-part="${p}"`), `${id}: missing part ${p}`);
  ok((body.match(/<svg /g) || []).length === 1 && /<title id=/.test(body) && /<desc id=/.test(body), `${id}: svg with title+desc`);
  const q = Q[qkey[id]];
  const qb = body.match(/<div class="q" data-answer="([A-E])"[\s\S]*$/);
  ok(qb && qb[1] === q.correctAnswer, `${id}: correct letter`);
  const stim = body.match(/<div class="passage qtext">([\s\S]*?)<\/div>/);
  ok(stim && unesc(stim[1]) === q.stimulus, `${id}: stimulus not byte-equal`);
  const stem = body.match(/<p class="qstem qtext">([\s\S]*?)<\/p>/);
  ok(stem && unesc(stem[1]) === q.questionStem, `${id}: stem not byte-equal`);
  const ch = [...body.matchAll(/data-l="([A-E])" aria-pressed="false"><span class="cl">[A-E]<\/span><span class="ct qtext">([\s\S]*?)<\/span>/g)];
  ok(ch.length === 5, `${id}: 5 choices`);
  for (const [, L, t] of ch) ok(unesc(t) === q.answerChoices[L], `${id}: choice ${L} not byte-equal`);
  ok((body.match(/class="exp"/g) || []).length === 5, `${id}: 5 explanations`);
}
const sheet = html.match(/<section id="sheet">([\s\S]*?)<\/section>/)?.[1] || '';
const groups = [...sheet.matchAll(/<div class="sheet-group" data-tier="([01])">([\s\S]*?)<\/ol><\/div>/g)];
ok(groups.length === 2, 'sheet: two groups');
ok(JSON.stringify(groups.map(g => g[1])) === JSON.stringify(['0','1']), 'sheet: tier order');
for (const g of groups) ok((g[2].match(/class="flaw-card"/g) || []).length === 5, 'sheet: five cards per tier');
const cards = [...sheet.matchAll(/<a class="flaw-card" href="#f-([a-z-]+)"[\s\S]*?<\/a>/g)];
ok(cards.length === 10 && JSON.stringify(cards.map(c => c[1])) === JSON.stringify(order), 'sheet: ten cards in order');
ok(html.indexOf('id="sheet"') < html.indexOf('id="how"'), 'sheet before how');
ok(!html.includes('id="recap"') && !html.includes('class="findex"') && !html.includes('class="callout whatif"'), 'obsolete sections absent');
const sourceDefs = {};
for (const line of readFileSync(new URL('./refs/famous-fallacies-handout.txt', import.meta.url), 'utf8').split(/\r?\n/)) {
  const at = line.indexOf(' \u2013 ');
  if (at >= 0) sourceDefs[line.slice(0, at)] = line.slice(at + 3);
}
const {execFileSync} = await import('node:child_process');
const content = JSON.parse(execFileSync('python', ['-B', '-c', 'import sys,json;sys.path.insert(0,"src");import content as c;print(json.dumps({"defs":c.HANDOUT_DEF,"flaws":c.FLAWS,"explain":c.EXPLAIN}))'], {encoding:'utf8', cwd:new URL('.',import.meta.url)}));
for (const f of content.flaws) {
  ok(content.defs[f.id] === sourceDefs[f.name], `${f.id}: HANDOUT_DEF differs from source`);
  ok(f.what === content.defs[f.id], `${f.id}: content definition differs`);
  const body = secs.find(s => s[1] === f.id)?.[3] || '';
  const what = body.match(/<p class="what" data-part="what">([\s\S]*?)<\/p>/)?.[1];
  ok(what && unesc(what) === content.defs[f.id], `${f.id}: entry definition differs`);
  const card = cards.find(c => c[1] === f.id)?.[0] || '';
  ok(unesc(card.match(/<p class="card-definition">([\s\S]*?)<\/p>/)?.[1] || '') === content.defs[f.id], `${f.id}: card definition differs`);
  for (const area of [card,body]) ok(area.includes('class="flaw-image') && (area.includes('placeholder') || area.includes(`alt="${f.img_alt}"`)), `${f.id}: image slot or image with planned alt`);
  for (const [letter, exp] of Object.entries(content.explain[f.q])) {
    const L = letter === 'right' ? Q[f.q].correctAnswer : letter;
    const actual = body.match(new RegExp(`<div class="exp" data-l="${L}"[^>]*>([\\s\\S]*?)<\\/div>`))?.[1];
    ok(actual && unesc(actual) === exp, `${f.id}: explanation ${L} differs`);
  }
}
const imgs = [...html.matchAll(/<img src="data:image\/webp;base64,[^"]+" alt="([^"]+)"/g)];
ok(imgs.length >= 3 && imgs.every(m => m[1].length > 0), "images with alt text");
for (const cls of ['hero-img','tier-img']) {
  const drawings = [...html.matchAll(new RegExp(`<figure class="${cls}"><img src="data:image/webp;base64,[^"]+" alt="([^"]+)"`, 'g'))];
  ok(drawings.length === (cls === 'hero-img' ? 1 : 2) && drawings.every(m => m[1].length > 20), `${cls}: drawings with descriptive alt`);
}
// visible authored text: strip head, scripts, styles, svg, exempt verbatim blocks
let vis = html.replace(/<head>[\s\S]*?<\/head>/, "").replace(/<script>[\s\S]*?<\/script>/g, "").replace(/<svg[\s\S]*?<\/svg>/g, "")
  .replace(/<div class="passage[^"]*">[\s\S]*?<\/div>/g, "").replace(/<p class="qstem qtext">[\s\S]*?<\/p>/g, "").replace(/<span class="ct qtext">[\s\S]*?<\/span>/g, "")
  .replace(/<\/(?:p|li|h[1-6]|div)>/g, "\n").replace(/<[^>]+>/g, " ");
vis = unesc(vis);
ok(!/[–—]/.test(vis), "en/em dash in authored text: " + (vis.match(/.{30}[–—].{30}/) || [""])[0]);
const banned = /\b(delve|dive deep|unlock|unleash|harness|seamless|robust|elevate|supercharge|game-changer|Certainly|Great question|manual|recognition drill|Codex|Claude|transcript|Gemini|The good news|Your job is to|gap|Before you start|recordings?|handout|platform internals|it's not just)\b/i;
ok(!banned.test(vis), "banned word: " + (vis.match(banned) || [""])[0]);
ok(!/^\s*(Moreover|Furthermore|Additionally),/m.test(vis), "banned paragraph opener");
const all = html.replace(/<script>[\s\S]*?<\/script>/g, "");
ok(!/Fauci|coronavirus|wear(ing)? masks|governor/i.test(all), "pandemic example remnants: " + (all.match(/Fauci|coronavirus|wear(ing)? masks|governor/i) || [""])[0]);
console.log("size", Buffer.byteLength(html), "bytes");
if (fails.length) { console.log("FAIL\n- " + fails.join("\n- ")); process.exit(1); } else console.log("PASS all checks");
