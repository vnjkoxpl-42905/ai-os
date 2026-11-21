const {chromium}=require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
  const browser=await chromium.launch({channel:'msedge',headless:true});
  const errors=[],proofs=[];
  try {
    for(const width of [1200,390]) {
      const page=await browser.newPage({viewport:{width,height:850}});
      page.on('pageerror',e=>errors.push(e.message));
      page.on('console',m=>{if(m.type()==='error') errors.push(m.text());});
      for(const name of ['recap','primer-recall','argument-reference']) {
        await page.goto('file:///'+path.join(__dirname,name+'.html').replaceAll('\\','/'));
        if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)) throw Error('Overflow '+name+width);
        const text=await page.locator('body').innerText();
        if(/\bmanual\b/i.test(text+' '+await page.title())) throw Error('Banned wording '+name);
        if(name!=='argument-reference') {
          for(const day of ['2026-10-26','2026-10-28','2026-10-29','2026-10-30','2026-10-31']) if(!text.includes(day)) throw Error('Missing schedule '+name+day);
          if(text.includes('2026-11-01')) throw Error('Old deadline '+name);
          if(!text.includes('Do not open Read, Recall, Colour PT104 Section 1 before submitting')) throw Error('Missing section-first instruction '+name);
        }
        const details=page.locator('details');
        for(let i=0;i<await details.count();i++) {
          const detail=details.nth(i),summary=detail.locator('summary');
          await summary.click(); if(!await detail.evaluate(el=>el.open)) throw Error('Pointer '+name);
          await summary.focus(); await page.keyboard.press('Enter'); if(await detail.evaluate(el=>el.open)) throw Error('Enter '+name);
          await page.keyboard.press('Space'); if(!await detail.evaluate(el=>el.open)) throw Error('Space '+name);
        }
        await page.screenshot({path:path.join(__dirname,`${name}-review-${width}.png`),fullPage:true});
        if(name==='recap') await page.locator('section').last().screenshot({path:path.join(__dirname,`schedule-review-${width}.png`)});
        proofs.push({name,width,reveals:await details.count(),bytes:fs.statSync(path.join(__dirname,name+'.html')).size});
      }
      await page.close();
    }
  } finally {await browser.close();}
  if(errors.length) throw Error(errors.join(';'));
  const result={checked_at:new Date().toISOString(),proofs,pageErrors:errors,scope:'All three revised draft pages, pointer/Enter/Space reveals, section-first schedule and banned-word checks'};
  fs.writeFileSync(path.join(__dirname,'review-verification.generated.json'),JSON.stringify(result,null,2));
  console.log(JSON.stringify(result));
})().catch(e=>{console.error(e);process.exitCode=1});
