const {chromium}=require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs=require('fs'),path=require('path');
(async()=>{const b=await chromium.launch({channel:'msedge',headless:true});let report={};
for(const d of ['lamplight','carrel','marginalia'])for(const role of ['student','teacher'])for(const w of [1440,390]){
 const c=await b.newContext({viewport:{width:w,height:w===390?844:900}}); const p=await c.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));
 const response=await p.goto(`http://127.0.0.1:5191/${d}/${role}.html`,{waitUntil:'networkidle'});if(!response || !response.ok()) throw new Error('Unexpected HTTP status '+response?.status());
 await p.waitForTimeout(1800);let n=`${d}-${role}-${w}`;await p.screenshot({path:path.join(__dirname,n+'-top.png')});
 report[n]=await p.evaluate(()=>({width:innerWidth,height:innerHeight,docHeight:document.documentElement.scrollHeight,overflow:document.documentElement.scrollWidth-innerWidth,nav:Array.from(document.querySelectorAll('nav a')).map(e=>e.textContent.trim())}));report[n].errors=errors;
 await c.close();}
 fs.writeFileSync(path.join(__dirname,'independent-layout-report.json'),JSON.stringify(report,null,2));await b.close();console.log(JSON.stringify(report));})().catch(e=>{console.error(e);process.exit(1)});