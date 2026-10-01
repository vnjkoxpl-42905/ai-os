---
name: codex-review
description: "Codex-host entry point: Codex handles independent review or scoped delegation. Have Codex independently review an existing implementation plan while Codex coordinates a bounded revision loop. For automatic reviewer selection from either host, use claudex-loop with mode=review."
---

## Installed direction: Codex to Codex

This copy is for the Codex host. The current Codex conversation coordinates. Use `host=Codex` in the shared runner. The default independent reviewer and cross-provider handoff target is Codex. Preserve explicit user provider/model choices and authorized scope. For the loop, the host builds by default and the other provider inspects; the build compatibility entry point separately selects the other provider as builder.

# Codex Review

Compatibility entry point: explicitly use Codex as the plan reviewer. The shared workflow and executable live in the sibling `claudex-loop` skill; install that skill alongside this one.

In Codex, load [claudex-loop](../claudex-loop/SKILL.md) and start at `mode=review`, `host=Codex`, reviewer Codex. Preserve `PLAN_FILE`, `LOG_FILE`, `MAX_ROUNDS` / `rounds`, and explicit model/effort arguments. The invocation authorizes reviewing, not implementation. Do not restart an interview when the supplied plan is already adequate.

In Codex, explain that this explicit command would use the same provider for planning and review. Use the shared `claudex-loop mode=review` workflow with Codex as the independent reviewer unless the user specifically requested same-provider review. If they did, perform and label that as ordinary Codex review; do not claim cross-provider approval or use the cross-provider approval runner to certify it.

Read the shared [runtime reference](../claudex-loop/references/runtime.md). Resolve the runner from the installed sibling skill, not the target repository. Use the actual resolved plan path on every round and build handoff. A valid completed result and APPROVED verdict are both required; failed, empty, blocked or malformed results are not approval. The host logs findings and dispositions, and stops at the round cap.

If implementation follows, use the shared build/inspection phase. An independent plan review does not replace independent review of the final code.
