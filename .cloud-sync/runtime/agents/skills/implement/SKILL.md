---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
---


## Local execution contract (2026-10-10)

Execute only explicitly selected spec/ticket scope. Use actual host planning/delegation tools and relevant typecheck/test/review sequence. Preserve dirty baseline and do not commit/publish beyond authorization.

## Workflow

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "code-review" to review the work.

Commit your work to the current branch.
