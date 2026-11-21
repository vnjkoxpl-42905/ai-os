// Read-only public frontend release evidence. No credentials or student APIs.
import fs from 'node:fs';
const target = process.argv[2] ?? 'https://lsatprep.study';
const output = process.argv[3];
const html = await fetch(target, { cache: 'no-store' }).then(r => { if (!r.ok) throw new Error(`HTML ${r.status}`); return r.text(); });
const scripts = [...html.matchAll(/(?:src|href)=["']([^"']*\/assets\/[^"']+\.js)["']/g)].map(m => new URL(m[1],target).href);
const indexBundle = scripts.find(url => /\/index-[^/]+\.js$/.test(url));
const checked = [];
let previewMarker = false;
for (const url of [...new Set(scripts)]) {
  const source = await fetch(url).then(r => r.text());
  checked.push(url);
  if (source.includes('This does not start or score a drill')) previewMarker = true;
  // Finder can be contained in a route chunk imported by the initial bundle.
  for (const match of source.matchAll(/["'](?:\.\/)?([^"']*(?:QuestionFinder|ClassroomHome|AcademyMainhub)[^"']*\.js)["']/g)) {
    const chunkUrl = new URL(match[1],url).href;
    if (checked.includes(chunkUrl)) continue;
    const chunk = await fetch(chunkUrl).then(r => r.text());
    checked.push(chunkUrl);
    if (chunk.includes('This does not start or score a drill')) previewMarker = true;
  }
}
const evidence = { checkedAt: new Date().toISOString(), target, indexBundle, previewMarker, checked };
if (output) fs.writeFileSync(output, JSON.stringify(evidence,null,2)+'\n');
console.log(JSON.stringify(evidence,null,2));
