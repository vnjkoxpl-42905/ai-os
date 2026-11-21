const {chromium}=require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs=require('node:fs');const path=require('node:path');const {pathToFileURL}=require('node:url');
const root=path.resolve('C:/Users/Joshu/dev/ai-os/design/prototypes/lsatu-dashboard');
const cards=JSON.parse(fs.readFileSync(path.join(root,'catalog.json'),'utf8'));
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});const results=[];
 try{
  const index=await browser.newPage({viewport:{width:1440,height:1000},offline:true});
  await index.goto(pathToFileURL(path.join(root,'index.html')).href);
  await index.locator('#search').fill('Atmosphere');
  if(await index.locator('article:visible').count()!==1)throw Error('Search did not isolate Atmosphere');
  await index.locator('#search').fill('');await index.getByRole('button',{name:'Intermediate passes',exact:true}).click();
  if(await index.locator('article:visible').count()!==3)throw Error('Intermediate filter count');
  await index.getByRole('button',{name:'All',exact:true}).click();
  await index.evaluate(()=>document.querySelectorAll('img').forEach(i=>i.loading='eager'));
  await index.waitForFunction(()=>[...document.images].every(i=>i.complete));
  const bad=await index.evaluate(()=>[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src));if(bad.length)throw Error('Broken index images '+JSON.stringify(bad));
  await index.screenshot({path:path.join(root,'archive-desktop.png'),fullPage:false});
  results.push({type:'index',width:1440,cards:cards.length,imagesLoaded:true,overflow:await index.evaluate(()=>document.documentElement.scrollWidth-innerWidth)});
  await index.setViewportSize({width:390,height:1000});await index.screenshot({path:path.join(root,'archive-phone.png'),fullPage:false});
  results.push({type:'index',width:390,overflow:await index.evaluate(()=>document.documentElement.scrollWidth-innerWidth)});await index.close();
  const entries=[...new Set(cards.flatMap(c=>c.links.map(l=>l.path)).filter(p=>p.endsWith('.html')))];
  // Separate contexts avoid cross-version sample-storage state. No internet is available.
  for(const entry of entries){
   const ctx=await browser.newContext({viewport:{width:1440,height:1000},offline:true});const p=await ctx.newPage();const errors=[],failed=[];
   p.on('pageerror',e=>errors.push(e.message));p.on('requestfailed',r=>failed.push({url:r.url(),error:r.failure()?.errorText}));
   await p.goto(pathToFileURL(path.join(root,entry)).href,{waitUntil:'load',timeout:20000});
   await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(350);
   const info=await p.evaluate(()=>({title:document.title,text:document.body.innerText.trim().length,gsap:!!window.gsap}));
   results.push({type:'page',entry,...info,errors,failed});
   await ctx.close();
  }
 }finally{await browser.close()}
 const failures=results.filter(r=>r.errors?.length||r.failed?.length||r.overflow>0||(r.type==='page'&&r.text<80));
 fs.writeFileSync(path.join(root,'archive-check.json'),JSON.stringify({offline:true,results,failures},null,2));
 console.log(JSON.stringify({checked:results.length,failures},null,2));if(failures.length)process.exitCode=2;
})().catch(e=>{console.error(e);process.exitCode=1});
