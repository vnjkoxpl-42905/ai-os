import urllib.request
import json
import os
import sys

API_KEY = "fc-208ce20aa2704a2d8d13f7cd5b05d739"

def firecrawl_scrape(target_url):
    url = "https://api.firecrawl.dev/v1/scrape"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "url": target_url,
            "formats": ["markdown"]
        }).encode("utf-8")
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("data", {}).get("markdown", "")
    except Exception as e:
        print(f"Error scraping '{target_url}': {e}", file=sys.stderr)
        return ""

urls_to_scrape = [
    ("outreach_app", "https://www.outreach.ai/resources/blog/outreach-chatgpt-app"),
    ("docusign_news", "https://www.docusign.com/company/news-center/docusign-brings-trusted-agreement-intelligence-and-workflows-into-chatgpt-and-codex"),
    ("docusign_blog", "https://www.docusign.com/blog/docusign-contract-ai-chatgpt"),
    ("sales_skills_mcp", "https://mcptop.com/server/openai-sales"),
    ("openai_skills_library", "https://mcpservers.org/agent-skills/author/openai"),
    ("claude_skills", "https://support.claude.com/en/articles/12512176-what-are-skills")
]

os.makedirs("scratch/firecrawl_scrapes", exist_ok=True)

for name, u in urls_to_scrape:
    print(f"Scraping {name} from {u}...")
    md = firecrawl_scrape(u)
    with open(f"scratch/firecrawl_scrapes/{name}.md", "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Saved {name}.md ({len(md)} chars)")

print("Done scraping!")
