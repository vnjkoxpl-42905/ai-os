"""YouTube Transcript Extractor
Pulls public captions/subtitles directly from YouTube at zero cost with no API keys.
Usage:
    python get_youtube_transcript.py <video_url_or_id> [--timestamps] [--lang en]
"""

import argparse
import re
import sys
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"(?:youtu\.be\/)([0-9A-Za-z_-]{11})",
        r"(?:embed\/)([0-9A-Za-z_-]{11})",
        r"(?:shorts\/)([0-9A-Za-z_-]{11})",
        r"^([0-9A-Za-z_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    return url_or_id

def format_timestamp(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Fetch YouTube transcripts for free")
    parser.add_argument("video", help="YouTube video URL or 11-character video ID")
    parser.add_argument("--timestamps", action="store_true", help="Include timestamps")
    parser.add_argument("--lang", default="en", help="Language code (default: en)")
    args = parser.parse_args()

    video_id = extract_video_id(args.video)
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id, languages=[args.lang, "en"])
        
        lines = []
        for snippet in transcript:
            text = snippet.text.replace("\n", " ")
            if args.timestamps:
                ts = format_timestamp(snippet.start)
                lines.append(f"[{ts}] {text}")
            else:
                lines.append(text)
        
        print("\n".join(lines))
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
