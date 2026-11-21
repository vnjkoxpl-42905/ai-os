const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const path = require('path');
const fs = require('fs');
(async()=>{
 const browser = await chromium.launch({channel:'msedge',headless:true});
 const results=[];
 for(const student of ['sofia','celia-cutler']) for(const file of ['recap','drill-primer','method-reference']) for(const width of [1280,390]){
  const folder=path.resolve(__dirname,`../2026-10-25-${student}-post-session`);
  const page=await browser.newPage({viewport:{width,height:900}});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto('file:///'+path.join(folder,file+'.html').replaceAll('\\','/'));
  const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
  if(overflow||errors.length)throw Error(JSON.stringify({student,file,width,overflow,errors}));
  const summaries=page.locator('summary');
  for(let i=0;i<await summaries.count();i++){
   const s=summaries.nth(i);await s.click();
   if(!await s.evaluate(e=>e.parentElement.open))throw Error('Pointer reveal failed');
   await s.focus();await page.keyboard.press('Enter');
   if(await s.evaluate(e=>e.parentElement.open))throw Error('Enter close failed');
   await page.keyboard.press('Space');
   if(!await s.evaluate(e=>e.parentElement.open))throw Error('Space reveal failed');
  }
  const dir=path.join(folder,'rendered-evidence');fs.mkdirSync(dir,{recursive:true});
  await page.screenshot({path:path.join(dir,`${file}-${width}.png`),fullPage:true});
  results.push({student,file,width,overflow,errors,reveals:await summaries.count(),screenshot:`rendered-evidence/${file}-${width}.png`});
  await page.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(__dirname,'sofia-celia-browser-checks.generated.json'),JSON.stringify(results,null,2));
 console.log(JSON.stringify({pages:results.length,checks:'passed',results},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
