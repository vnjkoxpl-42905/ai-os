import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { executeOps } from './lsatu-ops-runtime.mjs';
const args=process.argv.slice(2);
if(args.length!==2||args[0]!=='--json'||/[\r\n]/.test(args[1])) throw new Error('Use --json with one structured catalog query');
try {
 const execution=await executeOps({sourcePath:path.join(path.dirname(fileURLToPath(import.meta.url)),'lsatu-work-search.ts'),scriptName:'work-search.generated.ts',args});
 const line=execution.stdout.split(/\r?\n/).find(x=>x.startsWith('LSATU_SEARCH_RESULT='));
 if(!line)throw new Error('Catalog runner returned no structured result');
 const result=JSON.parse(line.slice('LSATU_SEARCH_RESULT='.length));
 result.runtime={ops_commit:execution.ops_commit,cache_hit:execution.cache_hit,timings:execution.timings};
 console.log(JSON.stringify(result));
} catch(error) {
 const text=String(error.stderr??error.message);
 const line=text.split(/\r?\n/).find(x=>x.startsWith('LSATU_SEARCH_ERROR='));
 console.error(line?line.slice('LSATU_SEARCH_ERROR='.length):JSON.stringify({error:'Catalog runtime failed',details:text}));
 process.exitCode=1;
}
