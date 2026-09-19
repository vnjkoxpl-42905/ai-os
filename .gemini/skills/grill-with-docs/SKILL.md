---
name: grill-with-docs
description: Interview the user to sharpen a plan while recording settled terminology and decisions in the project's existing documents. Use when the user invokes grill-with-docs.
disable-model-invocation: true
---

# Grill with docs

Read and apply both sibling files directly. Do not depend on invoking them through the Skill tool: a dependency may disable model invocation.

- [grilling](../grilling/SKILL.md): ask the current round of unresolved design questions.
- [domain-modeling](../domain-modeling/SKILL.md): maintain terminology and record decisions where appropriate.

Resolve file paths relative to this file. Keep both sibling skill folders, including domain-modeling's format references, alongside this skill when activating it.

Start from the conversation's settled requirements and the existing design document. Distinguish user decisions, assistant recommendations, and open questions. A correction overrides an earlier recommendation; document that change and do not re-ask settled questions. Look up facts rather than asking the user to supply them.

Ask only decisions whose prerequisites are settled, with a concrete example and recommendation where useful. When a user corrects an interaction, show a small example of that interaction before proposing further distinctions. Do not invent product differences just to justify previously proposed names or categories.

Update the existing design record as answers arrive. Update the owning glossary when a term is resolved; use the sibling domain-modeling templates. Create an ADR only when its trade-off criteria apply. Preserve source evidence and distinguish a drafted design from implemented behavior.

Recording settled answers and updating the design documents are part of the interview and happen as answers arrive. The grilling instruction to wait for shared understanding applies to implementing or publishing the proposed design, not to these interview records. Preserve authorization already given by the user.
