---
type: reference
subject: Firecrawl JSON schema cookbook
updated: 2026-09-19
aliases: []
---

# Firecrawl Schema Cookbook

Supplying a JSON schema to `POST https://api.firecrawl.dev/v2/agent` forces the autonomous agent to extract clean, typed data instead of conversational prose.

Use these standard schema templates when dispatching research jobs.

---

## 1. Model / Tech Stack Comparison Schema

Use this when evaluating LLMs, libraries, or developer tools:

```json
{
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
```

---

## 2. Product / Competitor Feature Teardown Schema

Use this when investigating competing platforms, pricing, or product specs:

```json
{
  "type": "object",
  "properties": {
    "product_name": { "type": "string" },
    "company_url": { "type": "string" },
    "pricing_tier": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "tier_name": { "type": "string" },
          "price_per_month": { "type": "string" },
          "included_features": { "type": "array", "items": { "type": "string" } },
          "limits": { "type": "string" }
        }
      }
    },
    "core_capabilities": { "type": "array", "items": { "type": "string" } },
    "limitations_or_gotchas": { "type": "array", "items": { "type": "string" } },
    "sources": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["product_name", "pricing_tier", "core_capabilities"]
}
```

---

## 3. Curriculum / Pedagogical Concept Research Schema

Use this when researching LSAT concepts, teaching methodologies, or student note frameworks:

```json
{
  "type": "object",
  "properties": {
    "topic": { "type": "string" },
    "definitions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "term": { "type": "string" },
          "official_definition": { "type": "string" },
          "source": { "type": "string" }
        }
      }
    },
    "step_by_step_method": { "type": "array", "items": { "type": "string" } },
    "common_traps_or_fallacies": { "type": "array", "items": { "type": "string" } },
    "worked_example": {
      "type": "object",
      "properties": {
        "problem_stimulus": { "type": "string" },
        "solution_walkthrough": { "type": "string" },
        "explanation": { "type": "string" }
      }
    },
    "citations": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["topic", "definitions", "step_by_step_method", "common_traps_or_fallacies"]
}
```
