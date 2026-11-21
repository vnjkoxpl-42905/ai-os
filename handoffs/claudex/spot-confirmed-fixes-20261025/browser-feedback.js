async page => {
  const assert=(value,message)=>{if(!value)throw new Error(message)};
  await page.goto('http://127.0.0.1:8106/src/dev/relationship-intro-preview.html');
  await page.waitForSelector('.relationship-intro');
  assert((await page.locator('.relationship-instructions').innerText()).includes('rather than the whole sentence'),'focused quotation instruction missing');
  await page.evaluate(async()=>{
    const React=(await import('/node_modules/.vite/deps/react.js')).default;
    const {createRoot}=(await import('/node_modules/.vite/deps/react-dom_client.js')).default;
    const {CoachFeedback}=await import('/src/features/activity-centre/components/CoachFeedback.tsx');
    const bank=(await import('/src/features/activity-centre/content/spot-the-relationship.json?import')).default;
    document.querySelector('#root').style.display='none';
    const host=document.createElement('main');host.className='activity-centre';host.style.cssText='min-height:100vh;padding:24px;background:#fafafa;color:#161616';document.body.append(host);
    const panel=document.createElement('section');panel.style.cssText='max-width:720px;margin:auto;background:white;padding:24px;border:1px solid #ddd;border-radius:12px';host.append(panel);
    const root=createRoot(panel);
    window.showFeedback=(order,revealed=true,resolved=true)=>root.render(React.createElement(CoachFeedback,{activitySlug:bank.slug,verdict:'partial',feedback:'Look again at the words you quoted.',revealed,resolved,item:bank.items.find(i=>i.order===order)}));
    window.showFeedback(27);
  });
  await page.getByText('“because” or “accelerates”',{exact:true}).waitFor();
  const rows=[];
  for(const width of [390,658,768,1280]){
    await page.setViewportSize({width,height:873});
    assert(await page.getByText('One quotation for each relationship type is enough.').isVisible(),'quotation requirement not visible');
    const result=await page.evaluate(()=>({width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,text:document.body.innerText}));
    assert(!result.overflow,'feedback overflows viewport');rows.push({width,overflow:result.overflow});
  }
  await page.evaluate(()=>window.showFeedback(27,false,false));
  await page.getByText('Look again at the words you quoted.',{exact:true}).waitFor();
  assert(await page.getByText('Credited answer',{exact:true}).count()===0,'first hint leaks revealed answer');
  for(const order of [3,7,12,14,15,18,21,23,24,26,38,41,42,45,48]){
    await page.evaluate(n=>window.showFeedback(n),order);
    await page.getByText('Credited answer',{exact:true}).waitFor();
    assert(await page.locator('dt').count()>0,'missing answer types at '+order);
    assert(!(await page.locator('section').last().innerText()).includes('most-missed'),'unsupported performance claim');
  }
  await page.evaluate(()=>window.showFeedback(27));
  await page.setViewportSize({width:1280,height:873});
  await page.screenshot({path:'C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-confirmed-fixes-20261025/feedback-desktop.png'});
  await page.setViewportSize({width:390,height:873});
  await page.screenshot({path:'C:/Users/Joshu/dev/ai-os/handoffs/claudex/spot-confirmed-fixes-20261025/feedback-phone.png',fullPage:true});
  return {viewports:rows,questionsInspected:15,firstHintProtected:true,alternativeIndicatorsVisible:true,scope:'Actual feedback component with Activity Centre styles; no live Coach or student persistence'};
}
