import fs from 'node:fs';
import path from 'node:path';
const root = process.cwd();
function envFile(p) { return Object.fromEntries(fs.readFileSync(p,'utf8').split(/\r?\n/).filter(x=>x.trim()&&!x.trim().startsWith('#')&&x.includes('=')).map(x=>{const i=x.indexOf('=');return [x.slice(0,i).trim(),x.slice(i+1).trim().replace(/^["']|["']$/g,'')]})); }
const env={...envFile(path.resolve(root,'../ai-os-projects/lsatu/.env')),...envFile(path.join(root,'.env'))};
const base=env.VITE_SUPABASE_URL,key=env.VITE_SUPABASE_PUBLISHABLE_KEY;
async function request(url,init={}) {const r=await fetch(base+url,init);const j=await r.json();if(!r.ok)throw new Error(JSON.stringify({status:r.status,message:j.message||j.error_description||j.error}));return j;}
const tok=await request('/auth/v1/token?grant_type=password',{method:'POST',headers:{apikey:key,'content-type':'application/json'},body:JSON.stringify({email:env.LSATPREP_ADMIN_EMAIL,password:env.LSATPREP_ADMIN_PASSWORD})});
const headers={apikey:key,authorization:`Bearer ${tok.access_token}`,'content-type':'application/json'};
const users=await request('/functions/v1/admin-manage-users',{headers});
const emails=['koohsandra@gmail.com','giannajean005@gmail.com','celiacutler@gmail.com'];
const targets=emails.map(email=>{const hits=users.filter(u=>u.email?.toLowerCase()===email);if(hits.length!==1)throw new Error(`Ambiguous or missing ${email}`);return hits[0];});
const results=[];
for(const u of targets){
 const q=`/rest/v1/classroom_items?student_id=eq.${u.class_id}&type=eq.activity&source_table=eq.reading_center&source_id=eq.library&select=id,title,status,visible_to_student,unlock_at`;
 const before=await request(q,{headers});
 let assigned=null;
 if(process.argv.includes('--apply')) assigned=await request('/rest/v1/rpc/assign_reading_center',{method:'POST',headers,body:JSON.stringify({p_student_id:u.class_id,p_unlock_at:null,p_title:'Reading Center',p_description:null})});
 const after=await request(q,{headers});
 const granted=after.filter(x=>x.visible_to_student&&['assigned','in_progress','completed'].includes(x.status)&&(!x.unlock_at||new Date(x.unlock_at)<=new Date()));
 if(process.argv.includes('--apply')&&granted.length===0)throw new Error(`Readback failed for ${u.email}`);
 results.push({email:u.email,name:u.display_name,class_id:u.class_id,before,result:assigned,after,access_granted:granted.length>0});
}
console.log(JSON.stringify({mode:process.argv.includes('--apply')?'applied':'dry-run',results},null,2));
