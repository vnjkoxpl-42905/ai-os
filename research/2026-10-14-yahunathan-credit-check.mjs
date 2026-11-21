import fs from 'node:fs';
const read=f=>Object.fromEntries(fs.readFileSync(f,'utf8').split(/\r?\n/).filter(l=>l.trim()&&!l.trim().startsWith('#')&&l.includes('=')).map(l=>{let i=l.indexOf('=');return [l.slice(0,i).trim(),l.slice(i+1).trim().replace(/^["']|["']$/g,'')]}));
const e={...read('C:/Users/Joshu/dev/ai-os-projects/lsatu/.env'),...read('.env')};
const url=e.VITE_SUPABASE_URL,key=e.VITE_SUPABASE_PUBLISHABLE_KEY;
const t=await (await fetch(url+'/auth/v1/token?grant_type=password',{method:'POST',headers:{apikey:key,'content-type':'application/json'},body:JSON.stringify({email:e.LSATPREP_ADMIN_EMAIL,password:e.LSATPREP_ADMIN_PASSWORD})})).json();if(!t.access_token)throw Error('auth failed');
const h={apikey:key,authorization:'Bearer '+t.access_token,'content-type':'application/json'};
for(const q of ['stripe_payments?select=*&order=created_at.desc&limit=15','booking_offers?select=*']){let r=await fetch(url+'/rest/v1/'+q,{headers:h});console.log(q,r.status,await r.text())}
console.log('stripe credential names',Object.keys(e).filter(k=>/STRIPE/.test(k)));

const queries=['stripe_payments?select=*&email=eq.ynproemail%40gmail.com','booking_passes?select=*&student_id=eq.d9afa662-d72f-44c1-8948-475309268f63','bookings?select=*&student_id=eq.d9afa662-d72f-44c1-8948-475309268f63'];
for(const q of queries){let r=await fetch(url+'/rest/v1/'+q,{headers:h});console.log(q,r.status,await r.text())}
let r=await fetch('https://api.stripe.com/v1/checkout/sessions/cs_live_a11SfoOqpUOU9USo4Nrg2D55iViYJGn3VM4n4ILbbzmVxX2bcebUAdw766',{headers:{authorization:'Bearer '+e.STRIPE_SECRET_KEY}});let j=await r.json();console.log('Stripe',r.status,JSON.stringify({id:j.id,payment_status:j.payment_status,amount_total:j.amount_total,currency:j.currency,payment_link:j.payment_link,customer_email:j.customer_details?.email,created:j.created,error:j.error?.message}));
{const q='booking_pass_redemptions?booking_pass_id=eq.7eeda40d-852a-43b6-8fe1-7ae44ddb88cc&select=*&order=created_at.desc';let r=await fetch(url+'/rest/v1/'+q,{headers:h});console.log('REDEMPTIONS',r.status,await r.text())}
