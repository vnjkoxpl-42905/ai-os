// Normalized bank-vs-database type sweep. Both sides go through the app's own
// normalizeQType, so only disagreements that change what a student sees remain.
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { normalizeQType, inferTypeFromStem } from 'C:/Users/Joshu/dev/ai-os-projects/lsatu-wt-bankfix-b02/src/lib/questionLoader.ts';

const BANK = 'C:/Users/Joshu/dev/ai-os-projects/lsatu-wt-bankfix-b02/public/data';
const DB = 'C:/Users/Joshu/dev/ai-os/system/scripts/lsatlab-pull/data/db/lr_questions.json';
const OUT = process.argv[2];

const warn = console.warn; console.warn = () => {};
const db = new Map<string, any>();
for (const q of JSON.parse(readFileSync(DB, 'utf-8'))) db.set(`PT${q.preptest}-S${q.section}-Q${q.question_number}`, q);

const rows: any[] = [];
for (const f of readdirSync(BANK).filter(f => /^PT\d+-S\d+-LR\.json$/.test(f)).sort()) {
  for (const b of JSON.parse(readFileSync(join(BANK, f), 'utf-8'))) {
    if (b.status === 'removed') continue;
    const slot = `${b.practiceTest}-S${b.sectionNumber}-Q${b.questionNumber}`;
    const d = db.get(slot);
    const stem = b.questionStem || '';
    const bankRaw = b.questionType ?? null;
    const app = normalizeQType(bankRaw || '', stem);
    const labelOnly = normalizeQType(bankRaw || '');
    const dbRaw = d?.question_type ?? null;
    const dbCanon = dbRaw ? normalizeQType(dbRaw) : 'Unknown';
    const inferred = inferTypeFromStem(stem);
    rows.push({ slot, file: f, bankRaw, app, labelOnly, dbRaw, dbCanon, inferred, stem, dbPrompt: d?.prompt ?? null, inDb: !!d });
  }
}
console.warn = warn;
writeFileSync(OUT, JSON.stringify(rows, null, 1));
const dis = rows.filter(r => r.inDb && r.app !== r.dbCanon);
console.log('bank rows', rows.length, 'in db', rows.filter(r => r.inDb).length, 'disagree', dis.length);
console.log('bank label missing', rows.filter(r => !r.bankRaw).map(r => r.slot));
console.log('bank raw not in taxonomy (resolved via stem or Unknown)', rows.filter(r => r.bankRaw && normalizeQType(r.bankRaw) === 'Unknown').length);
console.log('app Unknown', rows.filter(r => r.app === 'Unknown').map(r => r.slot));
console.log('db Unknown', rows.filter(r => r.inDb && r.dbCanon === 'Unknown').map(r => `${r.slot}=${r.dbRaw}`));
