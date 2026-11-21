import fs from 'node:fs';
const read=f=>Object.fromEntries(fs.readFileSync(f,'utf8').split(/\r?\n/).filter(l=>l.trim()&&!l.trim().startsWith('#')&&l.includes('=')).map(l=>{let i=l.indexOf('=');return [l.slice(0,i).trim(),l.slice(i+1).trim().replace(/^["']|["']$/g,'')]}));
const e={...read('C:/Users/Joshu/dev/ai-os-projects/lsatu/.env'),...read('.env')};
const url=e.VITE_SUPABASE_URL,key=e.VITE_SUPABASE_PUBLISHABLE_KEY;
const t=await (await fetch(url+'/auth/v1/token?grant_type=password',{method:'POST',headers:{apikey:key,'content-type':'application/json'},body:JSON.stringify({email:e.LSATPREP_ADMIN_EMAIL,password:e.LSATPREP_ADMIN_PASSWORD})})).json();if(!t.access_token)throw Error('auth failed');
const h={apikey:key,authorization:'Bearer '+t.access_token,'content-type':'application/json'};

const endpoint=url+'/functions/v1/booking-pass-admin';
async function call(body){const r=await fetch(endpoint,{method:'POST',headers:h,body:JSON.stringify(body)});const j=await r.json();if(!r.ok||j.error)throw Error(j.error||'request failed');return j;}
const id='7eeda40d-852a-43b6-8fe1-7ae44ddb88cc';
const marker='2026-10-14: Joshua authorized +1 replacement credit for missed 2026-10-13 session (redemption 80e3ed7e-1abc-4730-b064-1b7a9ef318d6). Applied via pass total 7 -> 8, used remains 3, available 5. Already compensated; do not also refund this redemption.';
const before=await call({action:'list'});const p=before.passes.find(x=>x.id===id);if(!p||p.total_credits!==8||p.used_credits!==3)throw Error('Unexpected balance');
if(!(p.notes||'').includes(marker))await call({action:'update',pass_id:id,notes:[p.notes,marker].filter(Boolean).join('\n')});
const after=await call({action:'list'});const v=after.passes.find(x=>x.id===id);console.log(JSON.stringify({note_verified:v.notes.includes(marker),remaining:v.total_credits-v.used_credits}));
