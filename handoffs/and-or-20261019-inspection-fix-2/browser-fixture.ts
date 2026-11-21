import {writeFileSync} from 'node:fs';
import {andOrDrills,andOrQuizzes} from 'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019/src/bootcamps/conditionals/content/andOrItems.ts';
import {choiceStep} from 'C:/Users/Joshu/dev/ai-os-projects/lsatu-and-or-20261019/src/bootcamps/conditionals/content/andOrTasks.ts';
const convert=(item:any)=>({id:item.id,kind:item.task.kind,correct:choiceStep(item)?.options.find(o=>o.correct)?.text,wrong:choiceStep(item)?.options.filter(o=>!o.correct).map(o=>({text:o.text,hint:o.hint}))});
writeFileSync('C:/Users/Joshu/dev/ai-os/handoffs/and-or-20261019-inspection-fix-2/browser-fixture.json',JSON.stringify({drills:andOrDrills.map(s=>({id:s.id,items:s.items.map(convert)})),quizzes:Object.fromEntries(Object.entries(andOrQuizzes).map(([k,v])=>[k,v.map(convert)]))}));
