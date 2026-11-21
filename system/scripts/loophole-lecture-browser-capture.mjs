// Use only with the selected CUA tab and browser-observed catalog URLs.
export async function captureLecture({tab, fs, root, record}) {
  if(await tab.url()!==record.url)await tab.goto(record.url);
  const transcript=tab.playwright.getByRole('button',{name:'Toggle transcript',exact:true});
  try{await transcript.waitFor({state:'visible'});}catch{}
  await tab.playwright.domSnapshot();
  if(await transcript.getAttribute('aria-expanded')!=='true'){await transcript.click();await tab.playwright.domSnapshot();}
  const data=await tab.playwright.evaluate(()=>{
    const video=document.querySelector('video');
    const notes=Array.from(document.querySelectorAll('h1,h2,h3,h4,h5')).find(e=>/Ellen.?s Notes/i.test(e.innerText))?.parentElement;
    return{title:document.querySelector('h2')?.innerText,url:location.href,duration:video?.duration,
      sources:Array.from(video?.querySelectorAll('source')||[]).map(e=>({src:e.src,type:e.type})),
      tracks:Array.from(video?.querySelectorAll('track')||[]).map(e=>({src:e.src,label:e.label,kind:e.kind})),
      transcript:Array.from(document.querySelectorAll('[aria-label="Transcript"] li button')).map(b=>({time:b.querySelector('span')?.innerText,text:b.querySelectorAll('span')[1]?.innerText})),
      writtenNotes:notes?{status:'present',text:notes.innerText,html:notes.outerHTML,images:Array.from(notes.querySelectorAll('img')).map(e=>({src:e.src,alt:e.alt}))}:{status:'No Ellen’s Notes heading observed'},
      pageText:document.body.innerText,links:Array.from(document.querySelectorAll('a[href]')).map(a=>({title:a.innerText,url:a.href}))};
  });
  if(!data.title||!data.transcript.length||!data.sources.length)throw Error('Missing lecture title, transcript, or media; inspect visible state');
  const directory=root+'/'+data.title.replace(/[<>:"/\\|?*]/g,' ').replace(/\s+/g,' ').trim();
  await fs.mkdir(directory,{recursive:true});
  let exists=false;try{await fs.access(directory+'/source.json');exists=true;}catch{}
  if(!exists)await fs.writeFile(directory+'/source.json',JSON.stringify({...data,capturedAt:new Date().toISOString(),catalogTitle:record.title},null,2));
  const excerpt=tab.playwright.getByRole('button',{name:'Toggle book excerpt',exact:true});
  let ex;
  if(await excerpt.count()){
    if(await excerpt.getAttribute('aria-expanded')!=='true'){await excerpt.click();await tab.playwright.domSnapshot();}
    ex=await tab.playwright.evaluate(()=>{const e=document.querySelector('[aria-label="Book excerpt"]');return{url:location.href,text:e?.innerText,html:e?.outerHTML,images:Array.from(e?.querySelectorAll('img')||[]).map(i=>({src:i.src,alt:i.alt}))};});
    if(!ex.text||!ex.html)throw Error('Book excerpt control exists but its content is not loaded; inspect and resume before saving');
  }else ex={url:data.url,status:'No book-excerpt control observed'};
  await fs.writeFile(directory+'/book-excerpt.json',JSON.stringify(ex,null,2));
  await fs.writeFile(directory+'/page.png',await tab.screenshot({fullPage:false}));
  return{directory,title:data.title,segments:data.transcript.length,notes:data.writtenNotes.status,seconds:data.duration};
}
