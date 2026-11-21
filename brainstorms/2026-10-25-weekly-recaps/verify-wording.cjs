const {chromium}=require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs=require('fs');const path=require('path');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});const results=[];
 for(const student of ['amanda','ore','yahunatan','charles','zeina','sofia','celia-cutler','whit-wilson']){
  const folder=path.resolve(__dirname,`../2026-10-25-${student}-post-session`);
  const files=fs.readdirSync(folder).filter(x=>x.endsWith('.html')&&!x.includes('.src.')&&!x.startsWith('before-'));
  if(files.length!==3)throw Error(`Expected 3 delivery pages in ${folder}, got ${files}`);
  for(const file of files)for(const width of [1200,390]){
   const page=await browser.newPage({viewport:{width,height:900}});const errors=[];
   page.on('pageerror',e=>errors.push(e.message));
   await page.goto('file:///'+path.join(folder,file).replaceAll('\\','/'));
   const data=await page.evaluate(()=>({title:document.title,bannedVisibleWord:/\bmanual\b/i.test(document.body.innerText),bannedTitle:/\bmanual\b/i.test(document.title),overflow:document.documentElement.scrollWidth>innerWidth}));
   const result={student,file,width,...data,errors};results.push(result);
   if(data.bannedVisibleWord||data.bannedTitle||data.overflow||errors.length)throw Error(JSON.stringify(result));
   if(student==='ore'&&file==='recap.html'&&width===1200){await page.screenshot({path:path.join(__dirname,'ore-current-wording-1200.png'),fullPage:true});}
   await page.close();
  }
 }
 await browser.close();
 const report={checked_at:new Date().toISOString(),scope:'Eight current folders, three delivery HTML pages each; source and before archives excluded',pages:24,renders:results.length,status:'passed',results};
 fs.writeFileSync(path.join(__dirname,'wording-check.generated.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({status:report.status,pages:report.pages,renders:report.renders}));
})().catch(e=>{console.error(e);process.exit(1)});
