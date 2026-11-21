import { useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { ConditionalLessonNote } from '@/bootcamps/conditionals/components/ConditionalLessonNote';
import { findConditionalUnit } from '@/bootcamps/conditionals/content';

/** Isolated development harness. It does not mount assignment or account persistence. */
export default function ConditionalOpeningPreview() {
  const [params, setParams] = useSearchParams();
  const [reviewed, setReviewed] = useState(false);
  const id = params.get('unit') ?? 'orientation';
  const ids = ['orientation', 'sufficient-necessary', 'group-1', 'group-2'];
  const unit = findConditionalUnit(ids.includes(id) ? id : 'orientation')!;
  const next = ids[(ids.indexOf(unit.id) + 1) % ids.length];
  return <main style={{ background: '#e9e7dd', minHeight: '100vh', padding: '20px 12px 70px' }}><nav aria-label="Development lesson preview" style={{ maxWidth: 1060, margin: '0 auto 20px', display: 'flex', flexWrap: 'wrap', gap: 12 }}>{ids.map(value => <button key={value} style={{ padding: '10px 15px' }} aria-pressed={value === unit.id} onClick={() => { setParams({ unit: value }); setReviewed(false); }}>{value}</button>)}</nav><ConditionalLessonNote unit={unit} reviewed={reviewed} onComplete={() => setReviewed(true)} continueHref={`/dev/conditional-opening-preview?unit=${next}`} continueLabel="Preview next lesson"/></main>;
}
