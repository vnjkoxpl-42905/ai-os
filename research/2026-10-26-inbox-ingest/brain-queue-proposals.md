# Brain clip queue proposals

### AQ-033 · Audit applications, routines, memory and skills as one operating inventory
- Type: workflow change
- From: [RoboNuggets ARMS walkthrough](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) at 1:52 to 5:39
- Value: exposes useful missing connections and forgotten automation alongside the access already granted.
- Already here: connections.md, skill catalogs, wiki routing and Graphify references provide separate inventories; ingestion did not audit live usage or schedules.
- Steps:
  1. Read the existing registries and obtain a read-only snapshot of active connections, schedules, skill activations and memory homes.
  2. Map ownership, purpose, permissions and links among those four layers; separate observed use from unknown use.
  3. Propose missing integrations only for an actual repeated need; propose unused connection or routine retirement for Joshua's approval without changing them.
  4. Check: every inventory row points to evidence and a purpose, gaps and unknowns are explicit, and no permissions or schedules change during the audit.
- Effort: medium · Status: new (2026-10-26)

### AQ-034 · Benchmark deterministic section retrieval against current wiki routing
- Type: workflow change
- From: [RoboNuggets brain.js description](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) at 6:53 to 10:49
- Value: tests correctness, retrieval speed and token savings before adding another search layer.
- Already here: alias/index routing, pointer links, miss logging and Smart Connections history exist; the source's code and reproducible results are absent.
- Steps:
  1. Build a small representative question set with known supporting files/sections, ambiguous aliases and genuine misses; keep model/runtime and initial context comparable.
  2. Record current index/alias retrieval correctness, elapsed time, message tokens and files read.
  3. In a scratch implementation evaluate deterministic keyword normalization, index scoring, bounded section reads and pointer following; include stale index and unresolved pointer behavior.
  4. Compare maintenance cost and repeated measurements; keep the existing route unless the measured result justifies a change.
  5. Check: saved questions, traces, correctness grades, repeated timings/token measurements and a keep/skip recommendation support the conclusion without borrowing the source's claimed 40% saving.
- Effort: medium · Status: new (2026-10-26)

### AQ-035 · Evaluate second-brain research resources against a concrete retrieval gap
- Type: repo
- From: [RoboNuggets second-brain resources](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) at 10:49 to 13:00 and description
- Value: finds useful methods without importing a replacement system or trusting promotional tool claims.
- Already here: Graphify has a local method reference; wiki schema and existing research tools cover baseline discovery. Exact QMD/G Brain/last30days upstreams and the R65 guide were not included in the clip.
- Steps:
  1. Identify one unresolved inventory or retrieval need and search existing workspace methods first.
  2. Verify exact last30days, QMD, G Brain and Graphify upstream identities; inspect relevant README/code/licence at pinned revisions and compare overlap before running anything.
  3. If accessible, preserve/read the R65 PDF and inspect the import-ready system and RUBRIC only for the identified gap; record access, licence and pricing requirements without purchasing or granting access.
  4. Use bounded recent-practices research to compare evidence with the current setup, keeping creator/funding/model/pricing assertions distinct from tested behavior.
  5. Check: an evidence-linked comparison records each resource's relevance, overlap, access limits and keep/skip recommendation; no tool installation, subscription or replacement vault is implied.
- Effort: medium · Status: new (2026-10-26)

### AQ-036 · Test a useful graph navigation view and its load/interaction targets
- Type: workflow change
- From: [RoboNuggets graph workflow](../../wiki/sources/ultimate-second-brain-arms-robonuggets.md) at 1:08 to 6:53 and 12:14 to 12:38
- Value: determines whether an operating-system map improves actual navigation and explanation.
- Already here: Graphify bridge and Obsidian command-center references already discuss connected sources and navigation; no graph UI or source performance claim was verified during ingestion.
- Steps:
  1. Read the design hub and existing Graphify/command-center references; select one real navigation or client-explanation task and compare the current route.
  2. Only if a gap remains, plan a scratch view showing department sizes and ARMS relationships, folder expansion, actual file opening, skill text and linked routines; get UI-plan approval before implementation.
  3. Measure cold/warm reloads against the source's under-ten-second target, interaction responsiveness and task success on a representative dataset; record machine, dataset size and measurement method.
  4. Check: direct file/source links, readable skill content and useful navigation work in the inspected view, measured loads and interactions meet stated targets, and the keep/skip decision reflects task benefit as well as appearance.
- Effort: medium · Status: new (2026-10-26)

## Merge into existing AQ-015

Add the ARMS source to From, and add Blotato, n8n, Make, ElevenLabs and Apify as promotional candidates to consider only if an actual gap is found. These are affiliate mentions in the description, not substantive capability evidence or commitments to five trials. No separate queue rows needed.
