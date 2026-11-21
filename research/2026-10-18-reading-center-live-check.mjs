const base=process.argv[2]||'https://lsatprep.study';
const html=await (await fetch(base,{cache:'no-store'})).text();
const index=html.match(/src="([^"]*\/index-[^"]+\.js)"/)?.[1];
if(!index)throw new Error('No index bundle found');
const main=await(await fetch(new URL(index,base))).text();
const paths=[...new Set(main.match(/(?:\.\/)?[A-Za-z0-9_/-]*ClassroomLayout[A-Za-z0-9_-]*\.js/g)||[])];
const checks=[{url:String(new URL(index,base)),snippets:[...main.matchAll(/children:"Reading Center"/g)].map(m=>main.slice(Math.max(0,m.index-350),m.index+40))}];
for(const asset of paths){
 const url=new URL(asset.replace(/^\.\//,''),new URL(index,base));
 const body=await(await fetch(url)).text();
 const needle='children:"Reading Center"';
 const positions=[...body.matchAll(/children:"Reading Center"/g)].map(m=>m.index);
 checks.push({url:String(url),snippets:positions.map(i=>body.slice(Math.max(0,i-350),i+40))});
}
console.log(JSON.stringify({index,checks},null,2));
