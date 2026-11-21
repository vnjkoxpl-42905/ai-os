"""X (Twitter) Post Extractor
Pulls public posts/tweets from X.com directly without paid API keys.
Usage:
    python get_x_post.py <tweet_url_or_id> [--json]
"""

import argparse
import json
import re
import sys
import requests

def extract_status_id(url_or_id: str) -> str:
    # Match status ID from URL or bare ID
    match = re.search(r"status(?:es)?\/(\d+)", url_or_id)
    if match:
        return match.group(1)
    # Check if purely digits
    if url_or_id.strip().isdigit():
        return url_or_id.strip()
    return url_or_id.strip()

def fetch_tweet(status_id: str):
    url = f"https://api.fxtwitter.com/status/{status_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code}: Failed to fetch post {status_id}")
    data = resp.json()
    if data.get("code") != 200:
        raise RuntimeError(f"API Error: {data.get('message', 'Unknown error')}")
    return data.get("tweet")

def format_tweet_markdown(tweet: dict) -> str:
    author = tweet.get("author", {})
    name = author.get("name", "Unknown")
    screen_name = author.get("screen_name", "")
    created_at = tweet.get("created_at", "")
    text = tweet.get("text", "")
    likes = tweet.get("likes", 0)
    retweets = tweet.get("retweets", 0)
    replies = tweet.get("replies", 0)
    bookmarks = tweet.get("bookmarks", 0)
    views = tweet.get("views")

    lines = []
    lines.append(f"**{name}** (@{screen_name}) | *{created_at}*")
    lines.append("-" * 40)
    lines.append(text)
    lines.append("-" * 40)
    
    # Media
    media = tweet.get("media", {})
    photos = media.get("photos", [])
    videos = media.get("videos", [])
    if photos:
        lines.append("\n**Photos:**")
        for p in photos:
            lines.append(f"- {p.get('url')}")
    if videos:
        lines.append("\n**Videos:**")
        for v in videos:
            lines.append(f"- {v.get('url')}")
            
    # Quote
    quote = tweet.get("quote")
    if quote:
        q_author = quote.get("author", {})
        lines.append(f"\n> **Quoting @{q_author.get('screen_name')}:**")
        lines.append(f"> {quote.get('text', '').replace('\n', '\n> ')}")

    # Stats
    stats_parts = [f"Likes: {likes:,}", f"Retweets: {retweets:,}", f"Replies: {replies:,}", f"Bookmarks: {bookmarks:,}"]
    if views is not None:
        stats_parts.append(f"Views: {views:,}")
    lines.append("\nStats: " + " | ".join(stats_parts))
    lines.append(f"Source: {tweet.get('url')}")
    
    return "\n".join(lines)

def main():
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Fetch X/Twitter post details")
    parser.add_argument("target", help="X/Twitter post URL or Status ID")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    status_id = extract_status_id(args.target)
    try:
        tweet = fetch_tweet(status_id)
        if args.json:
            print(json.dumps(tweet, indent=2))
        else:
            print(format_tweet_markdown(tweet))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
