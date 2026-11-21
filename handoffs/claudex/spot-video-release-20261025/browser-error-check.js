async page => {
  await page.route('**/media/spot-the-relationship/how-to-play-v1.mp4', r=>r.fulfill({status:404,body:''}));
  await page.reload();
  await page.getByRole('button',{name:'Expand video',exact:true}).click();
  await page.locator('video').evaluate(v=>v.play().catch(()=>{}));
  const status=page.getByRole('dialog').getByRole('status');
  await status.waitFor({state:'visible'});
  if (!(await status.innerText()).includes('could not load')) throw new Error('missing failure explanation');
  const ring=await page.getByRole('button',{name:'Close video'}).evaluate(b=>getComputedStyle(b).outlineColor);
  console.log(JSON.stringify({forced404:'visible within modal',closeFocusRing:ring}));
  await page.screenshot({path:'C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-video-release-20261025/video-error-visible.png'});
  await page.getByRole('button',{name:'Close video'}).click();
  await page.waitForFunction(()=>!document.querySelector('dialog').matches(':modal'));
  await page.getByRole('status').waitFor({state:'visible'});
  await page.unroute('**/media/spot-the-relationship/how-to-play-v1.mp4');
}
