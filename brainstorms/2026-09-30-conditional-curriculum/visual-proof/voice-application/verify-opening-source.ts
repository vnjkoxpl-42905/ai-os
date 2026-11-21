import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { foundationUnits } from '../../../../../ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/content/foundations.source';
import { applicationUnits } from '../../../../../ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/content/applications.source';
import { validateConditionalContent } from '../../../../../ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/content/validate';
import { findLegacyConditionalQuestion } from '../../../../../ai-os-projects/lsatu-conditional-bootcamp/src/bootcamps/conditionals/content/legacyQuestions';

const openingIds = ['orientation', 'sufficient-necessary', 'group-1', 'group-2'];
const levels = ['beginner', 'medium', 'advanced'] as const;
const replacements: Record<string, string> = { 'group-1-a3': 'group-1-a3-v2', 'group-2-m2': 'group-2-m2-v2', 'group-2-a3': 'group-2-a3-v2' };
const baseline = JSON.parse(readFileSync(new URL('./curriculum-before.json', import.meta.url), 'utf8'));
const historical = JSON.parse(readFileSync(new URL('./historical-questions-v2.json', import.meta.url), 'utf8'));
const units = [...foundationUnits, ...applicationUnits];
const errors = validateConditionalContent(units);
if (errors.length) throw new Error(errors.join('\n'));
const changedLater = baseline.filter(unit => !openingIds.includes(unit.id)).filter(unit => JSON.stringify(unit) !== JSON.stringify(units.find(current => current.id === unit.id))).map(unit => unit.id);
if (changedLater.length) throw new Error(`Later content changed: ${changedLater.join(', ')}`);
const project = (curriculum, mapIds = false) => openingIds.flatMap(id => {
  const unit = curriculum.find(item => item.id === id);
  return levels.flatMap(level => unit.drills[level].map(question => [unit.id, level, mapIds ? replacements[question.id] ?? question.id : question.id, question.prompt, question.options, question.answerIndex]));
});
// CI3-2 replaces the untaught quantifier with the tendency already taught.
// This is the only newly authorized prompt edit; options, key and ID stay exact.
const expected = project(baseline, true).filter(row => row[2] !== 'group-2-a1');
const orientationBefore = expected.find(row => row[2] === 'orientation-m1');
const orientationAfter = project(units).find(row => row[2] === 'orientation-m1');
if (!orientationBefore || !orientationAfter || orientationAfter[3] !== 'Inspected lifts usually operate quietly. Lift 2 was inspected. Is quiet operation guaranteed?') throw new Error('CI3-2 prompt exception must remain explicit.');
orientationBefore[3] = orientationAfter[3];
const actual = project(units);
const preserved = actual.filter(row => row[2] !== 'group-2-a1-v2');
if (JSON.stringify(expected) !== JSON.stringify(preserved)) throw new Error('Preserved 61-question practice contract changed.');
const replacement = actual.find(row => row[2] === 'group-2-a1-v2');
if (!replacement || replacement[1] !== 'advanced' || replacement[5] !== 0 || replacement[4][0] !== 'May inspect these records → reviewer appointed for emergency panel.') throw new Error('OR6 direct translation replacement missing.');
const expectedGuides = baseline.filter(unit => openingIds.includes(unit.id)).map(unit => [unit.id, unit.guidedExample.id, unit.guidedExample.prompt, unit.guidedExample.options, unit.guidedExample.answerIndex]);
const actualGuides = units.filter(unit => openingIds.includes(unit.id)).map(unit => [unit.id, unit.guidedExample.id, unit.guidedExample.prompt, unit.guidedExample.options, unit.guidedExample.answerIndex]);
if (JSON.stringify(expectedGuides) !== JSON.stringify(actualGuides)) throw new Error('Guided answer contract changed.');
for (const row of historical) if (JSON.stringify(findLegacyConditionalQuestion(row.id)) !== JSON.stringify(row)) throw new Error(`Historical question changed: ${row.id}`);
const hash = value => createHash('sha256').update(JSON.stringify(value)).digest('hex');
console.log(JSON.stringify({ units: units.length, totalPractice: units.flatMap(unit => Object.values(unit.drills).flat()).length, openingPractice: actual.length, preservedPractice: preserved.length, practiceSha256: hash(actual), preserved61Sha256: hash(expected), historicalSha256: hash(historical), laterUnitsUnchanged: units.length - openingIds.length, guidedContractsUnchanged: actualGuides.length, legacyQuestionsExact: historical.length }, null, 2));
