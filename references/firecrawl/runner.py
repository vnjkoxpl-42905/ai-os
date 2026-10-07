#!/usr/bin/env python3
"""
Firecrawl Task Runner for ai-os.
Standardized interface for executing searches, scrapes, and autonomous research agents.
Usage:
    python references/firecrawl/runner.py search "query"
    python references/firecrawl/runner.py scrape "https://example.com"
    python references/firecrawl/runner.py agent "Research prompt" --output .firecrawl/output.json
"""

import sys
import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path

def get_api_key():
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if not env_path.exists():
        env_path = Path(".env")
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("FIRECRAWL_API_KEY="):
                return line.split("=", 1)[1].strip("\"' ")
    env_key = os.environ.get("FIRECRAWL_API_KEY")
    if env_key:
        return env_key
    raise RuntimeError("FIRECRAWL_API_KEY not found in .env or environment")

def make_request(url, data=None, headers=None, method=None):
    key = get_api_key()
    default_headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    if headers:
        default_headers.update(headers)
    
    encoded_data = json.dumps(data).encode("utf-8") if data is not None else None
    req = urllib.request.Request(url, data=encoded_data, headers=default_headers, method=method)
    
    max_retries = 3
    base_delay = 2
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries - 1:
                wait_time = base_delay * (2 ** attempt)
                print(f"[Firecrawl] Rate limited (429). Waiting {wait_time}s before retry...", file=sys.stderr)
                time.sleep(wait_time)
                continue
            error_body = e.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"Firecrawl HTTP error {e.code}: {error_body}") from e
        except Exception as e:
            raise RuntimeError(f"Firecrawl request failed: {e}") from e

def search(query, limit=5, scrape_markdown=True):
    payload = {"query": query, "limit": limit}
    if scrape_markdown:
        payload["scrapeOptions"] = {"formats": ["markdown"]}
    res = make_request("https://api.firecrawl.dev/v1/search", data=payload)
    return res.get("data", [])

def scrape(target_url):
    payload = {"url": target_url, "formats": ["markdown"]}
    res = make_request("https://api.firecrawl.dev/v1/scrape", data=payload)
    return res.get("data", {}).get("markdown", "")

def run_agent(prompt, schema=None, max_credits=15, poll_interval=6, timeout=180):
    payload = {"prompt": prompt}
    if schema:
        payload["schema"] = schema
    if max_credits:
        payload["maxCredits"] = max_credits
    
    print("[Firecrawl] Dispatching agent job to /v2/agent...", file=sys.stderr)
    launch_res = make_request("https://api.firecrawl.dev/v2/agent", data=payload)
    job_id = launch_res.get("id")
    if not job_id:
        raise RuntimeError(f"Agent did not return job ID: {launch_res}")
    
    print(f"[Firecrawl] Job {job_id} launched. Polling status...", file=sys.stderr)
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        time.sleep(poll_interval)
        status_res = make_request(f"https://api.firecrawl.dev/v2/agent/{job_id}", method="GET")
        status = status_res.get("status")
        print(f"[Firecrawl] Status: {status} ({int(time.time() - start_time)}s elapsed)", file=sys.stderr)
        
        if status == "completed":
            return status_res
        elif status == "failed":
            raise RuntimeError(f"Agent job failed: {status_res}")
            
    raise TimeoutError(f"Agent job {job_id} timed out after {timeout} seconds")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python runner.py [search|scrape|agent] <args>")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    arg = sys.argv[2]
    
    if command == "search":
        items = search(arg)
        print(json.dumps(items, indent=2))
    elif command == "scrape":
        md = scrape(arg)
        print(md)
    elif command == "agent":
        output_path = sys.argv[3] if len(sys.argv) > 3 else None
        res = run_agent(arg)
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            Path(output_path).write_text(json.dumps(res, indent=2), encoding="utf-8")
            print(f"Results saved to {output_path}")
        else:
            print(json.dumps(res, indent=2))
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
