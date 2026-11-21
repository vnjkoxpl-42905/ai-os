import fs from 'node:fs';
const entries=[
 ['sandra','Sandra Kooh','f326c9b9-29df-4e17-8042-d1a6c3f45406','New live grant; status assigned.'],
 ['gianna','Gianna Jean','966ebcda-bdbe-430e-a9bb-3653adfb3605','New live grant; status assigned.'],
 ['celia-cutler','Celia Cutler','3ef6c6db-ec23-4da5-9960-221466605fd1','Existing item reused; in_progress preserved.'],
];
function appendCas(file,text){const before=fs.existsSync(file)?fs.readFileSync(file,'utf8'):'';if(before.includes('## 2026-10-18 Reading Center side rail access'))return;if((fs.existsSync(file)?fs.readFileSync(file,'utf8'):'')!==before)throw new Error('Concurrent log edit');fs.writeFileSync(file,before+text);}
for(const [slug,name,id,detail] of entries)appendCas(`students/${slug}/assignment-log.md`,`\n\n## 2026-10-18 Reading Center side rail access\n\n- ${name}: Joshua explicitly requested Reading Center in the homepage side rail.\n- ${detail} Item ID: ${id}.\n- Used existing assign_reading_center RPC with exact live email/class_id resolution and a dry-run first. Fresh readback confirmed visible_to_student=true, no unlock delay, and one qualifying item. No inbox/email notifications sent by this operation.\n- Backend access verified; no student-session UI verification claimed. Teacher sidebar code is a separate branch/PR change.\n`);
appendCas('wiki/log.md','\n\n## 2026-10-18 Reading Center side rail access\n\nEnabled Reading Center for Sandra Kooh and Gianna Jean via the existing admin RPC; verified saved visible assignments with no unlock delay. Celia Cutler already had access; her in-progress item was reused without changes. Exact item evidence is in each student assignment log. Teacher homepage hides the link explicitly; a separate frontend fix is being prepared on codex/reading-center-home-sidebar, pending PR checks and merge authorization. No notifications, paid Lovable calls, or frontend publication occurred during these access grants.\n');
console.log('Appended student evidence and system log.');
