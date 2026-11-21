from pathlib import Path
p=Path(r'C:/Users/Joshu/Downloads/LSAT-U-Dashboard-New-Directions/06-refined-studio')
s=(p/'index.html').read_text(encoding='utf-8')
s=s.replace('<label>Type<select','<div class="kind-switch" role="group" aria-label="Question type"><button type="button" data-kind="LR" aria-pressed="true">Logical reasoning</button><button type="button" data-kind="RC" aria-pressed="false">Reading comprehension</button></div><label class="native-kind">Type<select')
s=s.replace('<div class="practice-note"><span aria-hidden="true">↳</span><p>Return to the reasoning.<br><strong>What made the other answer tempting?</strong></p></div>','<div class="review-next"><span class="eyebrow">A useful next step</span><h3>Follow the hesitation.</h3><p>Revisit a sample from your least accurate set. Explain why the tempting answer falls short.</p><button data-sample="2">Revisit passage purpose <span>↗</span></button></div>')
s=s.replace('<div class="orbit-art" aria-hidden="true"><i></i><i></i><i></i><span>REASON / RECONSIDER</span></div>','<div class="orbit-art" aria-hidden="true"><div class="paper-sculpture">'+''.join('<i style="--i:'+str(i)+'"></i>' for i in range(16))+'</div></div>')
(p/'index.html').write_text(s,encoding='utf-8')
