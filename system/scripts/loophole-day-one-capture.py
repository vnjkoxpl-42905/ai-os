"""Archive browser-observed Loophole media and native captions, without cookies."""
import concurrent.futures, hashlib, json, pathlib, re, subprocess, urllib.request, sys

ROOT = pathlib.Path(__file__).resolve().parents[2] / 'Loophole Lecture' / 'Day One'
if len(sys.argv) > 1:
    ROOT = pathlib.Path(sys.argv[1]).resolve()

def run(args):
    p = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return p.returncode == 0

def capture(path):
    d = json.loads(path.read_text(encoding='utf-8'))
    folder = path.parent
    title = d['title']
    caption = folder / 'source.vtt'
    try:
        if not caption.exists():
            req = urllib.request.Request(d['tracks'][0]['src'], headers={'Referer':'https://new.theloophole.com/'})
            with urllib.request.urlopen(req, timeout=60) as r:
                caption.write_bytes(r.read())
        vtt = caption.read_text(encoding='utf-8-sig')
        cues = re.findall(r'(\d\d:\d\d:\d\d[.,]\d+)\s+-->\s+(\d\d:\d\d:\d\d[.,]\d+)\s*\n(.*?)(?=\n\s*\n|\Z)', vtt, re.S)
        assert cues, 'No caption cues'
        body = '\n\n'.join(f'[{a} - {b}]\n{re.sub("<[^>]+>", "", text).strip()}' for a,b,text in cues)
        (folder / (folder.name + '.md')).write_text(f'# {title}\n\nSource: {d["url"]}\n\nDuration: {d["duration"]}. Captured: 2026-10-14.\n\nTranscript origin: English auto-generated native captions. Complete caption extraction, not a human-verified verbatim transcript. Original wording retained.\n\n'+body+'\n', encoding='utf-8')
        video = folder / 'video.mp4'
        if not video.exists():
            run(['yt-dlp','--quiet','--no-warnings','--no-progress','--concurrent-fragments','4','--referer','https://new.theloophole.com/','--merge-output-format','mp4','-o',str(video),d['sources'][0]['src']])
        duration = None
        if video.exists():
            probe = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(video)],capture_output=True,text=True)
            duration = float(json.loads(probe.stdout)['format']['duration'])
            run(['ffmpeg','-hide_banner','-loglevel','error','-n','-i',str(video),'-vn','-c:a','copy',str(folder/'audio.m4a')])
            images=folder/'images'; images.mkdir(exist_ok=True)
            for t in [5, int(duration/2), max(0,int(duration)-8)]:
                run(['ffmpeg','-hide_banner','-loglevel','error','-n','-ss',str(t),'-i',str(video),'-frames:v','1',str(images/f'{t//60:02}-{t%60:02}.jpg')])
        last=cues[-1][1]
        status={'title':title,'cue_count':len(cues),'dom_segments':len(d['transcript']),'last_caption':last,'video_duration':duration,'video_saved':video.exists(),'audio_saved':(folder/'audio.m4a').exists()}
        (folder/'verification.json').write_text(json.dumps(status,indent=2),encoding='utf-8')
        (folder/'PROVENANCE.md').write_text(f'# {title}\n\nLesson: {d["url"]}\n\nCaptured 2026-10-14 from the authorized Codex browser session. source.vtt contains unchanged native auto-generated captions. source.json preserves the rendered transcript and observed media references. Video and audio retain the instructor voice.\n\nAccuracy: captions were not fully checked by listening. Suspect phrases must be checked against audio before quoting or adapting. Frames are sampled at 5 seconds, midpoint, and near the end.\n\nCaption cues: {len(cues)}. Last cue ends {last}. Video duration: {duration}.\n',encoding='utf-8')
        hashes=[]
        for f in sorted(folder.rglob('*')):
            if f.is_file() and f.name!='SHA256SUMS':
                h=hashlib.file_digest(f.open('rb'),'sha256').hexdigest()
                hashes.append(h+'  '+f.relative_to(folder).as_posix())
        (folder/'SHA256SUMS').write_text('\n'.join(hashes)+'\n',encoding='utf-8')
        print(json.dumps(status),flush=True)
        return status
    except Exception as e:
        status={'title':title,'error':type(e).__name__}
        print(json.dumps(status),flush=True)
        return status

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(capture, sorted(ROOT.glob('*/source.json'))))
    (ROOT/'verification.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
