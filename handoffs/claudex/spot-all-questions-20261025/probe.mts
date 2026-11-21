import { readFileSync } from 'node:fs';
import { matchesCredited } from 'C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-video-release-20261025/src/features/activity-centre/worlds/observatory/observatory.ts';
const bank = JSON.parse(readFileSync('C:/Users/Joshu/dev/ai-os-projects/lsatu-spot-video-release-20261025/src/features/activity-centre/content/spot-the-relationship.json','utf8'));
const get=(n:number)=>bank.items.find((i:any)=>i.order===n);
const cases:[number,string][] = [
 [5,'Causal, caused'], [5,'Causal, "caused"'],
 [5,'causal, '+get(5).prompt],
 [28,'comparative, '+get(28).prompt+'; causal, '+get(28).prompt],
 [34,'comparative, harder ... than; causal, so masons reserve it for thresholds, but only if; conditional, so masons reserve it for thresholds, but only if'],
 [7,'causal, corroded; comparative, lower'],
 [26,'causal, because; comparative, lower'],
 [31,'comparative, larger; causal, which is why'],
];
console.log(JSON.stringify(cases.map(([order,answer])=>({order,answer,instantCorrect:matchesCredited(get(order),answer)})),null,2));
