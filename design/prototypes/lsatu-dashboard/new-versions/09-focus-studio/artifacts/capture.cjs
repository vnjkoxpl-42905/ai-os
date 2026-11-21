const { chromium } = require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs = require('node:fs');
const path = require('node:path');
const out = __dirname;
const base = 'http://127.0.0.1:5200/';
(async () => {
 const browser = await chromium.launch({ channel: 'msedge', headless: true });
 const results = [];
 try {
  for (const width of [1440,1100,768,390,320,1920]) {
   const context = await browser.newContext({ viewport: { width, height: 1000 }, deviceScaleFactor:1 });
   const page = await context.newPage(); const errors=[], failed=[];
   page.on('pageerror', e => errors.push(e.message));
   page.on('response', r => { if(r.status()>=400) failed.push({status:r.status(),url:r.url()}); });
   await page.goto(base, {waitUntil:'load'});
   await page.evaluate(() => document.fonts.ready);
   await page.waitForTimeout(350);
   const metrics = await page.evaluate(() => ({width:innerWidth,overflow:document.documentElement.scrollWidth-innerWidth,h1:document.querySelector('h1')?.textContent,bodyLength:document.body.textContent.trim().length,animations:document.getAnimations().filter(a=>a.playState==='running').length,buttons:[...document.querySelectorAll('button')].filter(b=>b.getBoundingClientRect().width>0).map(b=>({text:b.innerText,label:b.getAttribute('aria-label')}))}));
   await page.screenshot({path:path.join(out,`home-${width}.png`),fullPage:true});
   results.push({view:'home',...metrics,errors,failed});
   if(width===1440||width===390) {
    for(const route of ['work','practice','review','progress','library','messages','reading']) {
     await page.goto(base+'#'+route,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);await page.waitForTimeout(280);
     const info=await page.evaluate(()=>({width:innerWidth,overflow:document.documentElement.scrollWidth-innerWidth,h1:document.querySelector('h1')?.textContent,bodyLength:document.body.textContent.trim().length}));
     await page.screenshot({path:path.join(out,`${route}-${width}.png`),fullPage:true});results.push({view:route,...info,errors:[...errors],failed:[...failed]});
    }
   }
   await context.close();
  }
  const context=await browser.newContext({viewport:{width:390,height:900},reducedMotion:'reduce'});const page=await context.newPage();await page.goto(base,{waitUntil:'load'});await page.evaluate(()=>document.fonts.ready);
  results.push({view:'reduced-motion',...(await page.evaluate(()=>({width:innerWidth,overflow:document.documentElement.scrollWidth-innerWidth,animations:document.getAnimations().filter(a=>a.playState==='running').length})))});
  await page.screenshot({path:path.join(out,'reduced-home-390.png'),fullPage:true});await context.close();
 } finally {await browser.close();}
 fs.writeFileSync(path.join(out,'capture-report.json'),JSON.stringify(results,null,2));
 console.log(JSON.stringify(results.map(({buttons,...rest})=>rest),null,2));
 if(results.some(r=>r.overflow>0||r.errors?.length||r.failed?.length||r.bodyLength<200))process.exitCode=2;
})().catch(e=>{console.error(e);process.exitCode=1});
