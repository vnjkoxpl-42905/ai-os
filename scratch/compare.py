import json
import sys
import os

# add parent directory to path to import references
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from references.firecrawl.runner import run_agent

schema = {
  "type": "object",
  "properties": {
    "summary": { "type": "string" },
    "comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "version": { "type": "string" },
          "strengths": { "type": "array", "items": { "type": "string" } },
          "weaknesses": { "type": "array", "items": { "type": "string" } },
          "benchmarks": { "type": "object" },
          "best_use_case": { "type": "string" },
          "citation_urls": { "type": "array", "items": { "type": "string" } }
        },
        "required": ["name", "strengths", "weaknesses", "best_use_case"]
      }
    },
    "verdict": {
      "type": "object",
      "properties": {
        "recommended_choice": { "type": "string" },
        "rationale": { "type": "string" },
        "key_tradeoffs": { "type": "array", "items": { "type": "string" } }
      },
      "required": ["recommended_choice", "rationale"]
    }
  },
  "required": ["summary", "comparison", "verdict"]
}

prompt = "Compare Google Gemini 3.1 Pro (High) vs Gemini 3.8 Flash (High) in terms of intelligence, task execution, coding, and benchmark specs. Which model is better and more intelligent for executing complex tasks today? Use Google's official documentation and recent benchmark results (like ARC-AGI-2 or Terminal-Bench)."

print("Launching agent...")
res = run_agent(prompt, schema=schema)
os.makedirs(".firecrawl", exist_ok=True)
with open(".firecrawl/gemini-comparison.json", "w", encoding="utf-8") as f:
    json.dump(res, f, indent=2)

print("Agent completed. Data written to .firecrawl/gemini-comparison.json")
