async page => {
  const assert = (condition, message) => { if (!condition) throw new Error(message); };
  await page.reload();
  const player = page.locator('video');
  const open = page.getByRole('button', {name:'Expand video', exact:true});
  const close = page.getByRole('button', {name:'Close video', exact:true});
  await open.waitFor();
  const rows=[];
  for (const width of [390,658,768,1280]) {
    await page.setViewportSize({width,height:873});
    assert(!(await player.evaluate(v=>v.controls)), 'inline controls must be absent');
    assert(await page.getByRole('dialog').count()===0, 'inline player exposed as dialog');
    await open.click();
    await page.waitForFunction(()=>document.querySelector('dialog').matches(':modal'));
    await page.waitForFunction(()=>document.querySelector('dialog').getAnimations().length===0);
    const row=await page.evaluate(()=>{
      const d=document.querySelector('dialog'), r=d.getBoundingClientRect();
      return {width:innerWidth,playerWidth:r.width,left:r.left,right:r.right,top:r.top,bottom:r.bottom,controls:document.querySelector('video').controls,overflow:document.documentElement.scrollWidth>innerWidth};
    });
    assert(row.controls&&!row.overflow&&row.left>=0&&row.right<=width+1&&row.top>=0&&row.bottom<=874, 'player must fit viewport');
    rows.push(row);
    await close.click();
    await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
    await page.waitForFunction(()=>document.activeElement?.classList.contains('relationship-video-expand'));
  }
  await player.click();
  await close.waitFor();
  await page.waitForFunction(()=>document.querySelector('dialog').matches(':modal'));
  await player.evaluate(v=>v.play());
  await page.waitForFunction(()=>document.querySelector('video').currentTime>0.5);
  const before=await player.evaluate(v=>v.currentTime);
  await close.click();
  await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
  const after=await player.evaluate(v=>({paused:v.paused,time:v.currentTime}));
  assert(after.paused&&after.time>=before&&after.time-before<2,'close must pause and retain position');
  await open.click();
  assert(await player.evaluate(v=>v.paused),'reopening must not autoplay');
  await page.keyboard.press('Escape');
  await page.keyboard.press('Escape');
  await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
  await open.click();
  await page.waitForFunction(()=>document.querySelector('dialog').getAnimations().length===0);
  await page.mouse.click(3,3);
  await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
  await page.emulateMedia({reducedMotion:'reduce'});
  await open.click();
  assert(await page.locator('dialog').evaluate(d=>d.getAnimations().length===0),'reduced motion must skip animation');
  await page.screenshot({path:'C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-video-release-20261025/release-video-expanded.png'});
  await close.click();
  await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
  await page.emulateMedia({reducedMotion:'no-preference'});
  console.log(JSON.stringify({rows,playback:{before,after},checks:'direct video click, focus return, close-pause, no autoplay, double Escape, backdrop, reduced motion'}));
}
