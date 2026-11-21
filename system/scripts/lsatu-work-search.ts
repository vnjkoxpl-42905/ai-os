// Runs through the dedicated headless app runtime. Read-only catalog discovery.
import fs from 'node:fs';
import path from 'node:path';
import { performance } from 'node:perf_hooks';
import { supabase } from '@/integrations/supabase/client';
import { BOOTCAMPS } from '@/lib/bootcamps';
const VAULT = '__VAULT_ROOT__';
const started = performance.now();
const i = process.argv.indexOf('--json');
const input = JSON.parse(i >= 0 ? process.argv[i + 1] : '{}');
async function query(request: any) { const { data, error } = await request; if (error) throw error; return data ?? []; }
async function main() {
  if (typeof input.query !== 'string' || input.query.length > 200 || !Number.isInteger(input.limit ?? 12) || (input.limit ?? 12) < 1 || (input.limit ?? 12) > 30 || (input.kind && !['activity', 'bootcamp', 'guided_drill'].includes(input.kind))) throw new Error('Invalid catalog query');
  const env: Record<string,string> = {};
  for (const line of fs.readFileSync(path.join(VAULT,'.env'),'utf8').split(/\r?\n/)) {
    const m = /^\s*([^#=\s]+)\s*=\s*(.*?)\s*$/.exec(line);
    if (m) env[m[1]] = m[2].replace(/^["']|["']$/g,'');
  }
  const { data, error } = await supabase.auth.signInWithPassword({email:env.LSATPREP_ADMIN_EMAIL,password:env.LSATPREP_ADMIN_PASSWORD});
  if (error || !data.user) throw new Error('Admin sign-in failed');
  const [activities, drills] = await Promise.all([
    input.kind && input.kind !== 'activity' ? [] : query(supabase.from('activities').select('id,title,slug,mode')),
    input.kind && input.kind !== 'guided_drill' ? [] : query(supabase.from('guided_drills').select('id,title,slug,question_count,estimated_minutes,level,bank_filter').eq('is_published',true)),
  ]);
  const aliases: Record<string,string[]> = {'7946f46b-e7f8-4c60-b405-4ece9c409deb':['General Conditionals','general-conditionals']};
  const rows: any[] = [
    ...activities.map((a:any)=>({kind:'activity',id:a.id,title:a.title,slug:a.slug,mode:a.mode,aliases:aliases[a.id]??[]})),
    ...drills.map((d:any)=>({kind:'guided_drill',id:d.id,title:d.title,slug:d.slug,count:d.question_count,minutes:d.estimated_minutes,level:d.level,filter:d.bank_filter})),
    ...(!input.kind || input.kind==='bootcamp' ? BOOTCAMPS.map(b=>({kind:'bootcamp',id:b.id,title:b.title,route:b.route,group:b.group??'bootcamp'})) : []),
  ];
  const normalize=(s:string)=>s.toLowerCase().replace(/[^a-z0-9]+/g,' ').trim();
  const term=normalize(input.query), words=term.split(' ').filter(Boolean);
  const matching=rows.filter(r=>words.every(w=>normalize(JSON.stringify(r)).includes(w))).map(r=>{
    const exact=[r.id,r.slug,r.title,...(r.aliases??[])].filter(Boolean).some(x=>normalize(x)===term);
    return {...r, exact_match: !!term && exact};
  }).sort((a,b)=>Number(b.exact_match)-Number(a.exact_match)||a.title.localeCompare(b.title));
  return {fetched_at:new Date().toISOString(),query:input.query,total_matches:matching.length,items:matching.slice(0,input.limit??12),metrics:{sign_ins:1,elapsed_ms:Math.round(performance.now()-started)},limits:'Guided difficulty/pool eligibility is validated by assignment preflight, not inferred from titles. Notes use an approved local HTML path.'};
}
main().then(r=>console.log('LSATU_SEARCH_RESULT='+JSON.stringify(r))).catch(e=>{console.error('LSATU_SEARCH_ERROR='+JSON.stringify({error:e?.message??String(e)}));process.exitCode=1;});
