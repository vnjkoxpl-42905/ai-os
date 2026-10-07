# Automation frontmatter schema — version 1

Automation-managed Markdown may declare:

```yaml
---
brain-managed: true
schema-version: 1
domain: lsat-u | personal | ai-workspace
source: relative/origin/path
---
```

If `brain-managed: true` is present, `schema-version: 1` and a recognized `domain` are mandatory. Missing or invalid managed metadata fails closed. Existing hand-authored pages without `brain-managed: true` are not retroactively required to carry frontmatter.

Automations may replace whole files only when the filename contains `.generated.` or is `INDEX.generated.md`. In other pages they may update only explicitly fenced generated sections.

