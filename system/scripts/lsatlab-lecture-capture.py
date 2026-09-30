"""Pull authorized LSAT Lab lecture captions/video, normalize captions, extract selected frames.

The player URL must be observed in the selected lesson, not guessed. No cookies,
credentials, or browser internals are read. Existing captures are never overwritten.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]

def run(args):
    subprocess.run(args, check=True)

def seconds(stamp):
    parts = stamp.replace(',', '.').split(':')
    return sum(float(value) * 60 ** power for power, value in enumerate(reversed(parts)))

def normalize(vtt, output):
    cues = []
    for block in re.split(r'\r?\n\s*\r?\n', vtt.read_text(encoding='utf-8-sig')):
        lines = block.splitlines()
        timing = next((i for i, line in enumerate(lines) if ' --> ' in line), None)
        if timing is None:
            continue
        match = re.match(r'(\S+)\s+-->\s+(\S+)', lines[timing])
        if not match:
            raise ValueError('Unrecognized caption timestamp')
        text = html.unescape(re.sub(r'<[^>]+>', '', ' '.join(lines[timing+1:])))
        cues.append({'start': seconds(match[1]), 'end': seconds(match[2]), 'text': text})
    if not cues:
        raise ValueError('No captions found')
    result = '\n'.join(f'[{c["start"]:.3f} - {c["end"]:.3f}] {c["text"]}' for c in cues) + '\n'
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists() and output.read_text(encoding='utf-8') != result:
        raise ValueError('Existing normalized transcript differs; preserve as a separate revision')
    output.write_text(result, encoding='utf-8')
    return cues

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--video-id', required=True)
    parser.add_argument('--player-url', help='Observed Vimeo embed URL including its existing hash')
    parser.add_argument('--video', action='store_true', help='Retrieve video for local exact-time frame captures')
    parser.add_argument('--normalize-to', type=Path)
    parser.add_argument('--frames', type=Path, help='JSON array: path (output filename), at_seconds')
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    if not re.fullmatch(r'\d+', args.video_id):
        parser.error('video-id must be numeric')
    archive = ROOT / 'raw' / 'sources' / 'lsat-lab-lectures' / args.video_id
    archive.mkdir(parents=True, exist_ok=True)
    captions = archive / 'source.en-x-autogen.vtt'
    media = archive / 'source.mp4'
    common = ['yt-dlp', '--referer', 'https://app.lsatlab.com/', '--no-progress', '--retries', '3', '--fragment-retries', '3']
    if not captions.exists():
        if not args.player_url:
            parser.error('player-url needed for initial capture')
        run(common + ['--skip-download', '--write-subs', '--sub-langs', 'en-x-autogen', '--sub-format', 'vtt', '--output', str(archive / 'source.%(ext)s'), args.player_url])
    if args.video and not media.exists():
        if not args.player_url:
            parser.error('player-url needed for initial video capture')
        run(common + ['--format', 'bestvideo[height<=1080]/best', '--concurrent-fragments', '16', '--output', str(archive / 'source.%(ext)s'), args.player_url])
    cues = normalize(captions, args.normalize_to) if args.normalize_to else None
    if args.frames:
        if not args.screenshots or not media.exists():
            parser.error('frames requires screenshots output and downloaded source.mp4')
        args.screenshots.mkdir(parents=True, exist_ok=True)
        frames = json.loads(args.frames.read_text(encoding='utf-8'))
        time_map_path = args.screenshots / 'frame-times.json'
        time_map = json.loads(time_map_path.read_text(encoding='utf-8')) if time_map_path.exists() else {}
        probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(media)], check=True, capture_output=True, text=True)
        duration = float(json.loads(probe.stdout)['format']['duration'])
        if not isinstance(frames, list):
            raise ValueError('Frame plan must be an array')
        for frame in frames:
            name = frame['path']
            if Path(name).name != name or Path(name).suffix.lower() not in ('.png', '.jpg'):
                raise ValueError('Frame path must be an image basename')
            stamp = float(frame['at_seconds'])
            if not 0 <= stamp < duration:
                raise ValueError('Frame timestamp outside video duration')
            target = args.screenshots / name
            if target.exists():
                if name not in time_map or float(time_map[name]) != stamp:
                    raise ValueError(f'Existing frame lacks matching timestamp provenance: {name}')
                continue
            run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-ss', str(stamp), '-i', str(media), '-frames:v', '1', '-update', '1', '-n', str(target)])
            if not target.is_file() or not target.stat().st_size:
                raise ValueError(f'Frame extraction produced no image: {name}')
            time_map[name] = stamp
            time_map_path.write_text(json.dumps(time_map, indent=2) + '\n', encoding='utf-8')
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (captions, media) if p.exists()}
    print(json.dumps({'archive': str(archive), 'sha256': hashes, 'caption_cues': len(cues) if cues else None, 'last_caption_end': cues[-1]['end'] if cues else None}, indent=2))

if __name__ == '__main__':
    main()
