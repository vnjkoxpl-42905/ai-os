// Original material study. Motion lives on the inner sculpture; responsive scale stays in CSS.
document.querySelectorAll('[data-sample]').forEach(b=>b.onclick=()=>showQuestion(examples[+b.dataset.sample]));
// A brief settling movement, followed by pointer-driven depth. No idle animation.
const motionQuery=matchMedia('(prefers-reduced-motion: reduce)');
let cleanupAtmosphere=()=>{};
function setupAtmosphere(){
 cleanupAtmosphere();
 if(!window.gsap||motionQuery.matches)return;
 const card=document.querySelector('.focus-card'),art=document.querySelector('.landscape-art img');
 const intro=gsap.fromTo(art,{scale:1.1,x:8},{scale:1.03,x:0,duration:1.3,ease:'power3.out'});
 const move=e=>{const r=card.getBoundingClientRect();gsap.to(art,{x:(e.clientX-r.left-r.width/2)*.012,y:(e.clientY-r.top-r.height/2)*.012,duration:.65,ease:'power2.out',overwrite:'auto'});};
 const leave=()=>gsap.to(art,{x:0,y:0,duration:.65,ease:'power2.out',overwrite:'auto'});
 if(matchMedia('(hover:hover)').matches){card.addEventListener('pointermove',move);card.addEventListener('pointerleave',leave);}
 cleanupAtmosphere=()=>{intro.kill();gsap.killTweensOf(art);gsap.set(art,{clearProps:'transform'});card.removeEventListener('pointermove',move);card.removeEventListener('pointerleave',leave);};
}
setupAtmosphere();motionQuery.addEventListener('change',setupAtmosphere);
document.querySelectorAll('[data-kind]').forEach(b=>b.onclick=()=>{document.querySelectorAll('[data-kind]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));quickPicker.elements.kind.value=b.dataset.kind;syncPicker(quickPicker);updateReference();});
