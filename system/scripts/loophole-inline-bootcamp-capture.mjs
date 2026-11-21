// CUA-only visible UI adapter for lecture-attached Video Bootcamps.
export async function captureInline({tab, fs, directory}) {
  const file = directory + '/inline-bootcamp.json';
  let previous;
  try { previous = JSON.parse(await fs.readFile(file, 'utf8')); } catch {}
  const out = previous || {url:await tab.url(), capturedAt:new Date().toISOString(), questions:[]};
  const toggle = tab.playwright.getByRole('button', {name:'Bootcamp', exact:true});
  if (!await toggle.count()) {out.status='No Bootcamp control observed'; await fs.writeFile(file,JSON.stringify(out,null,2)); return out.status;}
  if (await toggle.getAttribute('aria-expanded') !== 'true') {
    await toggle.click(); await tab.playwright.domSnapshot();
  }
  for (let i=0;i<15;i++) {
    let state = await read(tab);
    if (!state) throw Error('Video Bootcamp region missing');
    if (!state.number) {
      out.final=state;
      out.total=state.total||out.total||out.questions.map(q=>q.final?.total||q.initial?.total||Number(q.initial?.text?.match(/\/\s*(\d+)\s*Complete/i)?.[1])).find(Boolean);
      out.status=out.total===out.questions.length&&out.questions.every(q=>q.resolved)?'Complete observed inline quiz':'Finished displayed sequence; coverage unverified';
      break;
    }
    let question = {number:state.number, initial:state, attempts:[]};
    const existing=out.questions.find(q=>q.number===state.number);
    if (existing) question=existing;
    else out.questions.push(question);
    for (let k=0;k<state.buttons.length;k++) {
      if(state.buttons.every(b=>b.disabled)) break;
      const option=state.buttons[k];if(option.disabled)continue;
      await tab.playwright.getByRole('region',{name:'Video Bootcamp',exact:true}).getByRole('button',{name:option.label,exact:true}).click();
      await tab.playwright.domSnapshot(); state=await read(tab);
      for(let poll=0;poll<5;poll++){
        const selected=state.buttons.find(b=>/\sbg-chartreuse(?:\s|\")/.test(b.html));
        if(selected?.label===option.label)break;
        await tab.getAXState({emit:false});state=await read(tab);
      }
      const selected=state.buttons.find(b=>/\sbg-chartreuse(?:\s|\")/.test(b.html));
      const responseVerified=selected?.label===option.label;
      question.attempts.push({selected:option.label,state,responseVerified});
      await fs.writeFile(file,JSON.stringify(out,null,2));
      if(!responseVerified){
        out.status='Submission response not yet verified; resume this question';
        await fs.writeFile(file,JSON.stringify(out,null,2));
        return {questions:out.questions.length,resolved:out.questions.filter(q=>q.resolved).length,status:out.status};
      }
    }
    question.final=state;
    question.resolved=state.buttons.length>0&&state.buttons.every(b=>b.disabled);
    await fs.writeFile(file,JSON.stringify(out,null,2));
    await fs.writeFile(directory+'/inline-question-'+state.number+'.png',await tab.screenshot({fullPage:false}));
    if (!question.resolved) {out.status='Unresolved question '+state.number;break;}
    const next=tab.playwright.getByRole('region',{name:'Video Bootcamp',exact:true}).getByRole('button',{name:/^next question$/i});
    if(await next.count()) {await next.click();await tab.playwright.domSnapshot();}
    else {out.final=state;out.total=state.total;out.status=state.total===out.questions.length&&out.questions.every(q=>q.resolved)?'Complete observed inline quiz':'No next-question control; inspect coverage';break;}
  }
  await fs.writeFile(file,JSON.stringify(out,null,2));
  return {questions:out.questions.length,resolved:out.questions.filter(q=>q.resolved).length,status:out.status};
}
async function read(tab){return tab.playwright.evaluate(()=>{const r=document.querySelector('[aria-label="Video Bootcamp"]');if(!r)return null;const h=r.querySelector('h2');return{number:Number(h?.innerText.match(/Question\s+(\d+)/)?.[1])||null,total:Number(r.innerText.match(/\/\s*(\d+)\s*Complete/i)?.[1])||null,text:r.innerText,html:r.outerHTML,buttons:Array.from(r.querySelectorAll('button')).filter(b=>/^[A-Z](?:\s|$)/.test(b.innerText.trim())&&!/^(BACK|NEXT|TURN|RETRY|CONTINUE|FINISH)\b/.test(b.innerText.trim())).map(b=>({label:b.innerText.trim().replace(/\s+/g,' '),disabled:b.disabled,html:b.outerHTML})),images:Array.from(r.querySelectorAll('img')).map(e=>({src:e.src,alt:e.alt}))};});}
