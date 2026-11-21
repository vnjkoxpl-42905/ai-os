import fs from 'node:fs';
const read=f=>Object.fromEntries(fs.readFileSync(f,'utf8').split(/\r?\n/).filter(l=>l.trim()&&!l.trim().startsWith('#')&&l.includes('=')).map(l=>{let i=l.indexOf('=');return [l.slice(0,i).trim(),l.slice(i+1).trim().replace(/^["']|["']$/g,'')]}));
const e={...read('C:/Users/Joshu/dev/ai-os-projects/lsatu/.env'),...read('.env')};
const url=e.VITE_SUPABASE_URL,key=e.VITE_SUPABASE_PUBLISHABLE_KEY;
const t=await (await fetch(url+'/auth/v1/token?grant_type=password',{method:'POST',headers:{apikey:key,'content-type':'application/json'},body:JSON.stringify({email:e.LSATPREP_ADMIN_EMAIL,password:e.LSATPREP_ADMIN_PASSWORD})})).json();if(!t.access_token)throw Error('auth failed');
const h={apikey:key,authorization:'Bearer '+t.access_token,'content-type':'application/json'};

async function request(endpoint,body){const r=await fetch(url+endpoint,{headers:h,...(body?{method:'POST',body:JSON.stringify(body)}:{})});const data=await r.json();if(!r.ok)throw Error(JSON.stringify({status:r.status,data}));return data;}
const path='/rest/v1/booking_passes?id=eq.7eeda40d-852a-43b6-8fe1-7ae44ddb88cc&select=id,total_credits,used_credits,status';
const before=await request(path);if(before[0]?.total_credits!==8||before[0]?.used_credits!==3)throw Error('Unexpected balance; no RPC invoked');
const result=await request('/rest/v1/rpc/admin_return_teacher_missed_credit',{_redemption_id:'80e3ed7e-1abc-4730-b064-1b7a9ef318d6'});
if(result.already_returned!==true)throw Error('Expected already returned');
const after=await request(path);if(JSON.stringify(before)!==JSON.stringify(after))throw Error('Balance changed');
const redemption=await request('/rest/v1/booking_pass_redemptions?id=eq.80e3ed7e-1abc-4730-b064-1b7a9ef318d6&select=id,status,credit_refunded,teacher_missed_at,google_event_id');
console.log(JSON.stringify({idempotent_rpc:result,balance:after[0],remaining:after[0].total_credits-after[0].used_credits,redemption:redemption[0]}));
