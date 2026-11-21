from pathlib import Path
p=Path(r'C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio/app.js')
s=p.read_text(encoding='utf-8').replace('lsatu-refined-','lsatu-refined-studio-')
s=s.replace("function questionFromKey(key){const [kind,test,section,question]=key.split('-');return {...(examples.find(x=>refKey(x)===key)||examples.find(x=>x.kind===kind)),kind,test,section,question};}","function questionFromKey(key){return examples.find(x=>refKey(x)===key);}")
s=s.replace("savedRefs.map(questionFromKey)","savedRefs.map(questionFromKey).filter(Boolean)").replace("openedRefs.map(questionFromKey)","openedRefs.map(questionFromKey).filter(Boolean)")
a=s.index('function selectedQuestion(');b=s.index('function renderQuestion',a)
s=s[:a]+"function selectedQuestion(form){const d=Object.fromEntries(new FormData(form));return examples.find(x=>refKey(x)===refKey(d));}\n"+s[b:]
s=s.replace("showQuestion(selectedQuestion(quickPicker));","const q=selectedQuestion(quickPicker);if(q)showQuestion(q);else{panels.unavailable=['Demonstration library','This reference is not in the sample.','<p>Three original questions are available in this prototype. The live question bank is not connected.</p><button class=\"panel-action\" data-open-samples>Browse the three samples →</button>'];openPanel('unavailable');$('#panel-body [data-open-samples]').onclick=()=>{closePanel();openPanel('picker');$('[data-list=all]').click();};}")
s=s.replace("input.value=localStorage.getItem('lsatu-refined-studio-prep')||'';","try{input.value=localStorage.getItem('lsatu-refined-studio-prep')||'';}catch{input.value='';}")
s=s.replace("localStorage.setItem('lsatu-refined-studio-prep',input.value);status.textContent='Your question is saved on this device.';","try{localStorage.setItem('lsatu-refined-studio-prep',input.value);status.textContent='Your question is saved on this device.';}catch{status.textContent='Could not save on this device. Copy your note before closing.';}")
s=s.replace("catch{}const b=e.target.closest('.save-reference');","catch{savedRefs=savedRefs.includes(k)?savedRefs.filter(x=>x!==k):[...savedRefs,k];$('.answer-feedback').textContent='Could not save on this device. Please try again.';}const b=e.target.closest('.save-reference');")
p.write_text(s,encoding='utf-8')
