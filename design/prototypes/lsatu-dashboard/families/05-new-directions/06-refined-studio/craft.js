// Original material study. Motion lives on the inner sculpture; responsive scale stays in CSS.
document.querySelectorAll('[data-sample]').forEach(b=>b.onclick=()=>showQuestion(examples[+b.dataset.sample]));
if(window.gsap&&!reduced){
 const card=document.querySelector('.focus-card'), art=document.querySelector('.paper-sculpture');
 gsap.fromTo(art,{rotationZ:-34},{rotationZ:-25,duration:1.15,ease:'power3.out'});
 if(matchMedia('(hover:hover)').matches){card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();gsap.to(art,{x:(e.clientX-r.left-r.width/2)*.018,y:(e.clientY-r.top-r.height/2)*.025,duration:.8,ease:'power2.out'});});card.addEventListener('pointerleave',()=>gsap.to(art,{x:0,y:0,duration:.8,ease:'power2.out'}));}
}
document.querySelectorAll('[data-kind]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-kind]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));quickPicker.elements.kind.value=b.dataset.kind;syncPicker(quickPicker);updateReference();});
