import urllib.request
import json

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
        return f"Error: {e}"

urls = [
    ("openai_skills_help", "https://help.openai.com/en/articles/20001066-skills-in-chatgpt"),
    ("chatgpt_plugins_learn", "https://learn.chatgpt.com/docs/plugins")
]

for name, u in urls:
    md = firecrawl_scrape(u)
    with open(f"scratch/firecrawl_scrapes/{name}.md", "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Scraped {name} ({len(md)} chars)")
