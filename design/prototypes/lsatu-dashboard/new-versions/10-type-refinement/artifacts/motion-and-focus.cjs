const {chromium}=require('C:/Users/Joshu/dev/ai-os-projects/lsatu-role-home-20261022/node_modules/playwright');
const fs=require('node:fs');const path=require('node:path');const assert=require('node:assert/strict');
(async()=>{const browser=await chromium.launch({channel:'msedge',headless:true});const results={};try{
 const p=await browser.newPage({viewport:{width:1440,height:1000}});await p.goto('http://127.0.0.1:5201/#home');await p.evaluate(()=>document.fonts.ready);
 await p.getByRole('link',{name:'My Work',exact:true}).click();await p.waitForFunction(()=>LSATPreview.inspect().route==='work');
 results.naturalStart=await p.evaluate(()=>({animations:document.getAnimations().map(a=>({time:a.currentTime,state:a.playState,duration:a.effect.getTiming().duration})),textOpacity:getComputedStyle(document.querySelector('.page')).opacity}));
 await p.screenshot({path:path.join(__dirname,'motion-natural-start.png'),fullPage:false});await p.waitForTimeout(300);
 results.naturalSettled=await p.evaluate(()=>({running:document.getAnimations().filter(a=>a.playState==='running').length,opacity:getComputedStyle(document.querySelector('.page')).opacity}));
 await p.screenshot({path:path.join(__dirname,'motion-natural-settled.png'),fullPage:false});assert.equal(results.naturalSettled.running,0);assert.equal(results.naturalSettled.opacity,'1');
 await p.getByRole('button',{name:'Logical Reasoning',exact:true}).click();results.innerFilterAnimations=await p.evaluate(()=>document.getAnimations().filter(a=>a.playState==='running').length);assert.equal(results.innerFilterAnimations,0);await p.emulateMedia({reducedMotion:'reduce'});await p.getByRole('link',{name:'Review',exact:true}).click();await p.waitForFunction(()=>LSATPreview.inspect().route==='review');
 results.runtimeReduced=await p.evaluate(()=>({running:document.getAnimations().filter(a=>a.playState==='running').length,opacity:getComputedStyle(document.querySelector('.page')).opacity}));assert.equal(results.runtimeReduced.running,0);
 await p.emulateMedia({reducedMotion:'no-preference'});await p.goto('http://127.0.0.1:5201/#home');await p.locator('[data-action=continue]').click();
 results.dialogFocusSteps=[];
 for(let i=0;i<12;i++){await p.keyboard.press('Tab');const step=await p.evaluate(()=>({inside:document.querySelector('#modal').contains(document.activeElement),tag:document.activeElement.tagName,id:document.activeElement.id}));results.dialogFocusSteps.push(step);assert(step.inside||step.tag==='BODY','Tab must not focus an underlying page control')}
 results.dialogFocusTrap='12 Tab steps did not focus any underlying interactive page control';await p.keyboard.press('Escape');
 await p.getByRole('link',{name:'My Work',exact:true}).focus();
 results.controlFocus=await p.getByRole('link',{name:'My Work',exact:true}).evaluate(el=>({outline:getComputedStyle(el).outlineWidth,style:getComputedStyle(el).outlineStyle}));assert.notEqual(results.controlFocus.outline,'0px');
 await p.close();
 const mp=await browser.newPage({viewport:{width:390,height:900}});await mp.goto('http://127.0.0.1:5201/');await mp.getByRole('button',{name:'Open navigation',exact:true}).click();
 await mp.locator('#drawer-role').selectOption('teacher');await mp.waitForFunction(()=>LSATPreview.inspect().route==='teacher');
 await mp.waitForTimeout(260);await mp.screenshot({path:path.join(__dirname,'teacher-home-390.png'),fullPage:true});
 await mp.getByRole('button',{name:'Open navigation',exact:true}).click();await mp.locator('#drawer').getByRole('link',{name:'Students',exact:true}).click();await mp.waitForFunction(()=>LSATPreview.inspect().route==='students');
 await mp.waitForTimeout(260);await mp.screenshot({path:path.join(__dirname,'teacher-students-390.png'),fullPage:true});results.teacherMobileOverflow=await mp.evaluate(()=>document.documentElement.scrollWidth-innerWidth);assert.equal(results.teacherMobileOverflow,0);
 await mp.close();
}finally{await browser.close()}
fs.writeFileSync(path.join(__dirname,'motion-focus-report.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));
})().catch(e=>{console.error(e);process.exitCode=1});
