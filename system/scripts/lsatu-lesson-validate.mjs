// Fail before posting if an interactive lesson depends on files that the
// student's sandboxed Classroom iframe cannot reliably load.
export function lessonMarkerId(html) {
  const head = html.match(/<head\b[^>]*>([\s\S]*?)<\/head\s*>/i)?.[1] ?? '';
  const marker = head.match(/<meta\s+name=["']lsatu-interactive-lesson["']\s+content=["']([a-z0-9][a-z0-9-]{1,79})["']\s*\/?\s*>/i);
  return marker?.[1]?.toLowerCase() ?? null;
}

export function validateInteractiveLesson(html) {
  const lessonId = lessonMarkerId(html);
  if (!lessonId) throw new Error('Lesson needs <meta name="lsatu-interactive-lesson" content="unique-lesson-id"> in its head');
  if (!/<html\b/i.test(html) || !/<\/html\s*>/i.test(html)) throw new Error('Lesson must be a complete HTML document');
  const problems = [];
  const tags = html.match(/<(?:script|link|img|image|use|feimage|source|video|audio|iframe|object|embed)\b[^>]*>/gi) ?? [];
  for (const tag of tags) {
    const name = tag.match(/^<(\w+)/i)?.[1]?.toLowerCase();
    if (name === 'link' && !/\brel=["'](?:stylesheet|icon|preload|modulepreload)["']/i.test(tag)) continue;
    const refs = [...tag.matchAll(/\b(?:src|href|xlink:href|poster|data|srcset)=["']([^"']+)["']/gi)];
    for (const [, ref] of refs) {
      if (!ref.startsWith('data:') && !ref.startsWith('#')) problems.push(`${name}: ${ref.slice(0, 100)}`);
    }
  }
  for (const [, ref] of html.matchAll(/\burl\(\s*["']?([^)'"\s]+)["']?\s*\)/gi)) {
    if (!ref.startsWith('data:') && !ref.startsWith('#')) problems.push(`CSS: ${ref.slice(0, 100)}`);
  }
  if (/@import\b/i.test(html)) problems.push('CSS @import');
  if (problems.length) throw new Error(`Lesson has nonembedded resources: ${[...new Set(problems)].join('; ')}`);
  return lessonId;
}
