# ADR Format

Use an ADR only for decisions that are hard to reverse, surprising without context, and the result of a real trade-off.

Name files with a sequence number and short slug, for example:

```text
docs/adr/0001-use-postgres-for-write-model.md
```

Use this shape:

```markdown
# ADR 0001: Title

## Status

Accepted

## Context

What problem or decision pressure led to this decision?

## Decision

What did we choose?

## Alternatives Considered

What credible options did we reject?

## Consequences

What trade-offs, follow-up obligations, or constraints does this create?
```

Keep ADRs factual and concise. Do not use them for generic notes or reversible implementation details.
