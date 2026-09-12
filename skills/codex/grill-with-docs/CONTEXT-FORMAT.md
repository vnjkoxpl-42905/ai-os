# CONTEXT.md Format

`CONTEXT.md` is a domain glossary only. Keep it free of implementation notes, roadmap items, architecture decisions, API details, and scratch-pad thinking.

Use this shape:

```markdown
# Context

## Purpose

One or two sentences describing the bounded context in domain language.

## Glossary

### Canonical Term

Definition in business/domain language.

- Also known as: optional aliases, if useful
- Not: nearby terms this should not be confused with
- Example: one concrete scenario, if it clarifies the boundary
```

Prefer short, precise entries. Add a term only after it has been resolved with the user or confirmed from existing documentation/code.
