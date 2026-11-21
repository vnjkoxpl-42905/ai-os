import fs from 'node:fs';
import {Client} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/client/index.js';
import {StdioClientTransport} from 'file:///C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js';
const result={};
const c=new Client({name:'verify-21st-stdio',version:'1.0'});
try {
 await c.connect(new StdioClientTransport({command:'C:/Program Files/nodejs/node.exe',args:['C:/Users/Joshu/dev/ai-os/system/scripts/start-21st-mcp.mjs'],stderr:'pipe'}));
 const list=await c.listTools();result.toolCount=list.tools.length;
 const r=await c.callTool({name:'search',arguments:{query:'calendar',type:'component',limit:1}});
 result.metadataSearch={isError:!!r.isError,contentCount:r.content?.length};
}catch{result.failure='Stdio bridge handshake/search failed';}finally{await c.close();}
for(const u of ['https://godly.design/websites/','https://recent.design/']) {
 try{const r=await fetch(u);const t=await r.text();(result.publicPages??=[]).push({url:r.url,status:r.status,chars:t.length,links:[...t.matchAll(/href="([^"]+)"/g)].slice(0,35).map(x=>x[1])});}
 catch{(result.publicPages??=[]).push({requested:u,failure:'Fetch failed'});}
}
fs.writeFileSync('research/2026-10-24-design-skill-doctor/mcp-repair-probe.json',JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
