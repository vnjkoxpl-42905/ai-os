> Historical snapshot. The "no Git remote" rule quoted below was removed on 2026-09-29. Current rule: see AGENTS.md line 75.
# AIOS Phase 1: Instruction Control-Plane Design Report

**Document Role:** Architectural Analysis & Control-Plane Specification  
**Execution Constraints:** ANALYSIS AND DESIGN ONLY (Zero file modifications, zero configuration changes)  
**Target Audience:** External Systems Architect / Senior AI Engineer  
**Timestamp:** 2026-09-20T02:15:00-04:00  
**Host Machine:** `J` (Windows 11 Home, Build 26100)  
**Workspace Root:** `C:\Users\Joshu\dev\ai-os`  

---

## 1. CURRENT INSTRUCTION GRAPH

Mapping the exact instruction hierarchy and precedence across operational contexts.

### 1.1 Instruction Hierarchy Table

| Context | Loaded Instruction File | Precedence | Approx Tokens | Content Classification | Duplicating Document | Contradicting Document |
|---|---|---|---|---|---|---|
| **Context A: `dev\ai-os` (Root)** | `C:\Users\Joshu\GEMINI.md` | Base fallback (P3) | ~450 tok | Obsolete / Global router | Root `GEMINI.md` | None |
| | `C:\Users\Joshu\dev\ai-os\AGENTS.md` | Primary Codex (P2) | ~3,400 tok | Shared core + Codex skills | `dev\ai-os\CLAUDE.md` (97.5%), `dev\ai-os\GEMINI.md` (80.5%) | None at root |
| | `C:\Users\Joshu\dev\ai-os\GEMINI.md` | Primary Gemini (P1) | ~2,900 tok | Shared core + Gemini workspace | `dev\ai-os\AGENTS.md` (80.5%) | None at root |
| **Context B: `projects\lsatu`** | `C:\Users\Joshu\GEMINI.md` | Base fallback (P5) | ~450 tok | Obsolete router | Root `GEMINI.md` | None |
| | `C:\Users\Joshu\dev\ai-os\AGENTS.md` | Root parent (P4) | ~3,400 tok | Shared core rules | `dev\ai-os\GEMINI.md` | `projects\lsatu\GEMINI.md` (Autonomy conflict) |
| | `C:\Users\Joshu\dev\ai-os\GEMINI.md` | Root parent (P3) | ~2,900 tok | Shared core rules | `dev\ai-os\AGENTS.md` | `projects\lsatu\GEMINI.md` (Autonomy conflict) |
| | `C:\Users\Joshu\dev\ai-os\projects\lsatu\AGENTS.md` | Subtree Codex authority (P2) | ~2,100 tok | Project-specific dev rules | `projects\lsatu\CLAUDE.md` | Root `GEMINI.md` (Push rules) |
| | `C:\Users\Joshu\dev\ai-os\projects\lsatu\GEMINI.md` | Subtree Gemini authority (P1) | ~350 tok | Project-specific autonomy | None | Root `GEMINI.md` (95% Rule vs Maximum Autonomy) |
| **Context C: Future `projects\<project>`** | `C:\Users\Joshu\GEMINI.md` | Base fallback (P3) | ~450 tok | Obsolete router | Root `GEMINI.md` | None |
| | `C:\Users\Joshu\dev\ai-os\AGENTS.md` | Root parent (P2) | ~3,400 tok | Shared core rules | `dev\ai-os\GEMINI.md` | Depends on subproject rules |
| | `C:\Users\Joshu\dev\ai-os\GEMINI.md` | Root parent (P1) | ~2,900 tok | Shared core rules | `dev\ai-os\AGENTS.md` | Depends on subproject rules |
| | `projects\<project>\GEMINI.md` | Subtree authority (P0) | Variable | Subproject domain rules | None | Potential root guardrail collision |

### 1.2 Instruction Dependency & Inheritance Trees

#### Context A: `C:\Users\Joshu\dev\ai-os`
```text
[Global Windows User Profile]
└── C:\Users\Joshu\GEMINI.md (~450 tok) [Fallback router]
    │
    └── [Workspace Root: C:\Users\Joshu\dev\ai-os]
        ├── AGENTS.md (~3,400 tok) [Loaded by Codex & Antigravity]
        └── GEMINI.md (~2,900 tok) [Loaded by Antigravity]
        ──> RESULT: ~6,750 base instruction tokens eagerly injected into Antigravity
```

#### Context B: `C:\Users\Joshu\dev\ai-os\projects\lsatu`
```text
[Global Windows User Profile]
└── C:\Users\Joshu\GEMINI.md (~450 tok)
    │
    └── [Workspace Root: C:\Users\Joshu\dev\ai-os]
        ├── AGENTS.md (~3,400 tok) [MANDATE: 95% Rule (Ask first)]
        └── GEMINI.md (~2,900 tok) [MANDATE: 95% Rule (Ask first)]
            │
            └── [Subproject Repo: C:\Users\Joshu\dev\ai-os\projects\lsatu]
                ├── AGENTS.md (~2,100 tok) [MANDATE: Push to origin main]
                └── GEMINI.md (~350 tok)   [MANDATE: Maximum Autonomy (Never ask) + Never auto-push]
                ──> RESULT: Direct instruction collision across root and subtree
```

---

## 2. LINE-BY-LINE OWNERSHIP CLASSIFICATION

Classification of every major section in root `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md`:

| Section / Heading | Line Range (Approx) | Content Summary | Classification | Rationale |
|---|---|---|---|---|
| `# Jay 2 Header & Metadata` | Lines 1 to 5 | Title, author comment, hand-owned notice | **UNIVERSAL** | Establishes document context across runtimes |
| `## Identity and mission` | Lines 6 to 11 | Joshua identity, Jay 2 EA role, standing duties | **UNIVERSAL** | Core identity and EA mission applies to all agents |
| `## Routing map` | Lines 12 to 46 | Path lookup table across the repository | **REFERENCE / KNOWLEDGE** | Static lookup table; better queried on demand via `wiki/index.md` than eagerly injected every turn (~900 tokens) |
| `## Retrieval order` | Lines 47 to 58 | Hot cache -> wiki/index -> live backend rule | **UNIVERSAL** | Fundamental retrieval hierarchy for all runtimes |
| `## Voice` | Lines 59 to 66 | No em-dashes, no AI-slop words, draft-never-send | **UNIVERSAL** | Non-negotiable voice standard for Joshua's brand |
| `## Tools, keys, and secrets` | Lines 67 to 75 | `.env` store, gws CLI, safety at tool layer | **UNIVERSAL** | Security and credential invariant for all agents |
| `## Skills (AGENTS/CLAUDE)` | Lines 76 to 95 | Active skill table, skill activation protocol | **DUPLICATED / VENDOR-SPECIFIC** | Codex/Claude skill table. Redundant with actual filesystem state |
| `## Skills & Workspace (GEMINI)` | Lines 76 to 87 | `.gemini/` subtrees, 217 skills notice | **GEMINI / ANTIGRAVITY ONLY** | Specific to Gemini directory topology |
| `## Guardrails` | Lines 96 to 111 | 95% rule, Lovable credits, thin root, shell ops | **UNIVERSAL** | Operational safety boundaries |
| `## Dual-runtime (Codex + Claude)` | Lines 112 to 120 | Token handoffs, activation copies | **CODEX ONLY / CLAUDE ONLY** | Specific to Codex/Claude dual setup; irrelevant to Gemini |

---

## 3. DUPLICATION MATRIX

### 3.1 Textual & Semantic Overlap Metrics
- **`AGENTS.md` vs `CLAUDE.md`:** **97.5% identical** (SequenceMatcher ratio: `0.975`). The files are identical twins differing only in the header name (`Codex` vs `Claude Code`) and line 113.
- **`AGENTS.md` vs `GEMINI.md`:** **80.5% identical** (SequenceMatcher ratio: `0.805`). Lines 1 through 75 and lines 88 through 111 share word-for-word text.
- **`GEMINI.md` vs `CLAUDE.md`:** **80.5% identical** (SequenceMatcher ratio: `0.805`).

### 3.2 Token Consumption of Duplicated Material
- Total root instruction tokens on disk across all 3 files: **~9,842 tokens**.
- Active Antigravity base rule consumption: Antigravity eagerly loads both `AGENTS.md` (~3,462 tokens) and `GEMINI.md` (~2,919 tokens), consuming **~6,381 tokens per turn**.
- Redundant token overhead in Antigravity: **~2,800 tokens per interaction turn** are 100% duplicate instructions injected into Gemini context.
- **Potential Token Savings:** Eliminating root duplication and consolidating into a single authoritative core rulefile would immediately liberate **~2,800 to ~3,500 context tokens per turn**.

---

## 4. ROOT VS LSAT U RESPONSIBILITY

Decomposition of rules currently residing in `projects\lsatu` instruction files and their proper conceptual architectural tier:

| Rule / Directive in `projects\lsatu` | Current File | Proper Conceptual Tier | Rationale |
|---|---|---|---|
| **Lovable Credit Spending Confirmation** | Root & Subproject | **Machine / Global Level** | Financial protection invariant; must never be bypassed by subproject autonomy |
| **Lovable Cloud Deployment Routing** | Root & Subproject | **LSAT U Project Level** | Backend hosting implementation detail specific to the LSAT U web application |
| **Git Push / Auto-push Restrictions** | Root & Subproject | **LSAT U Project Level** | Root is not pushed to remote; LSAT U has its own git remote and feature branch workflow |
| **Frontend Browser Verification Gate** | `lsatu\AGENTS.md` & `CLAUDE.md` | **LSAT U Project Level** | Hard gate requiring DOM check or screenshot before marking UI change 'done' |
| **Multi-Viewport Emulate Matrix** | `lsatu\AGENTS.md` & `CLAUDE.md` | **LSAT U Skill / Reference Level** | Specific testing procedure; belongs in `lsat-u-browser-verification` skill |
| **Teaching Voice Mandate** | Root & Subproject | **ai-os Workspace Level** | Universal brand rule for all student-facing copy across business and apps |
| **Obsidian / Wiki Source of Truth** | Root & Subproject | **ai-os Workspace Level** | Knowledge management rule; decision ledger lives in ai-os root |
| **Session Pickup / Wrapup Protocol** | `lsatu\CLAUDE.md` & Root | **ai-os Workspace Level** | Operational cadence for updating tasks, hot cache, and wiki log |
| **Mac Paths (`/Users/joshuaf/...`)** | `lsatu\AGENTS.md` & `CLAUDE.md` | **STALE / NOWHERE** | Broken legacy paths from previous machine; actively causes file-not-found errors |
| **Supabase Client Auto-Gen Rules** | `lsatu\CLAUDE.md` | **LSAT U Project Level** | Strict rule forbidding manual editing of `src/integrations/supabase/client.ts` |

---

## 5. AUTONOMY CONFLICT ANALYSIS

### The Core Collision
- **Root Mandate (`dev\ai-os\GEMINI.md:L124`):** *'95% rule. Make no changes until you are 95% confident what Joshua wants. Ask until you are.'*
- **Subproject Mandate (`projects\lsatu\GEMINI.md:L7`):** *'Maximum Autonomy Rule: NEVER ask clarifying questions. Make sensible architectural decisions independently and implement them directly.'*

### Concrete Scenario Walkthrough

| Operation / Scenario | Current Rule Directive | Operational Ambiguity / Risk |
|---|---|---|
| **1. Simple UI Edit** (e.g. adjust button padding) | Subproject mandates immediate direct implementation without asking | Minimal ambiguity; Maximum Autonomy operates effectively |
| **2. Ambiguous Product Behavior Change** (e.g. free-tier drill access) | Root 95% rule dictates stopping to ask; Subproject mandates deciding independently and executing | High risk: Agent may unilaterally make breaking business or pedagogical decisions |
| **3. Database Migration** (e.g. alter table schema or RLS) | Root safety layer vs Subproject autonomy | Critical risk: Destructive schema changes executed without user review |
| **4. Destructive Filesystem Operation** (e.g. `rm -rf` old module) | Root shell ergonomics require safety; Subproject permits autonomous cleanup | Unsandboxed command execution (`config.json`) could permanently delete code |
| **5. Browser Inspection** (e.g. take port 9223 screenshots) | Both allow; Subproject mandates visual verification before completion | Safe, read-only operation |
| **6. npm install** (e.g. add new third-party dependency) | Subproject mandates autonomous implementation | Modifies package locks without explicit architectural alignment |
| **7. Git Commit** (e.g. commit working changes) | Root bans remote; `lsatu\GEMINI.md` says 'Joshua commits himself'; `lsatu\AGENTS.md` says 'commit and push' | Direct contradiction between `lsatu\GEMINI.md` and `lsatu\AGENTS.md` |
| **8. Git Push** (e.g. push to origin main) | Root strictly bans git push; `lsatu\GEMINI.md` says 'Never auto-push'; `lsatu\AGENTS.md` says 'push to origin main' | Severe contradiction: Agent instructed both to push and never push |
| **9. Lovable Credit Spending** (e.g. trigger Lovable agent deploy) | Root mandates explicit immediate confirmation before credit spend; Subproject mandates never asking | Critical safety conflict: Root confirmation gate must supersede autonomy |
| **10. Student-Facing Message** (e.g. draft consultation email) | Root mandates draft-only via teaching voice; never auto-send | Clear consensus: Draft only, never auto-send |
| **11. Production Deployment** (e.g. deploy Edge Functions) | Root requires confirmation before Lovable deploy; Subproject permits autonomous build | High risk: Deployment triggered prematurely |

---

## 6. SOURCE-OF-TRUTH CONFLICTS

Identified source-of-truth discrepancies across root and subproject files:

### 1. GitHub vs Lovable Canonical Status
- **`projects\lsatu\CLAUDE.md`:** *'The Lovable-connected project is the source of truth; GitHub (vnjkoxpl-42905/lsatu-684d89db) is the mirror. Treat the connected project as canonical unless told otherwise.'*
- **Root `GEMINI.md`:** *'Lovable Cloud deploys through Lovable. LSAT U currently uses a Lovable Cloud-managed backend. Deploy its Edge Functions through the Lovable agent, not the Supabase CLI... Confirm this route with Joshua before starting.'*
- **Operational Consequence:** Ambiguity over whether changes pushed to GitHub auto-sync to Lovable, or whether Lovable commits will overwrite local Git changes.

### 2. Git Push Authorization
- **`projects\lsatu\AGENTS.md:L11`:** *'After completing a change, stage the intended files, commit with a concise message, and push to origin main unless the user says otherwise.'*
- **`projects\lsatu\GEMINI.md:L11`:** *'Never auto-push. Joshua tests locally, commits, and pushes himself unless explicitly asked.'*
- **Root `GEMINI.md:L118`:** *'No Git remote, ever, without first completing the scrub checklist in wiki/HANDLING.md.'*
- **Operational Consequence:** Direct deadlock. If Antigravity reads `AGENTS.md`, it attempts to push; if it reads `GEMINI.md`, pushing is strictly forbidden.

### 3. Product Context Location
- **`projects\lsatu\CLAUDE.md:L11`:** *'Product context, design decisions, pedagogy, and status do NOT live in this repo. They live in the Obsidian vault at ~/ai-os/.'*
- **`projects\lsatu\AGENTS.md:L7`:** Points to obsolete Mac path `/Users/joshuaf/ai-os`.
- **Operational Consequence:** Agent attempts to open non-existent `/Users/joshuaf/` path when trying to read product context.

---

## 7. PATH STALENESS

Comprehensive inventory of stale Mac/Linux paths discovered in active instruction files:

| File | Stale Path Found | Intended Current Windows Path | Operational Failure Risk |
|---|---|---|---|
| `projects\lsatu\AGENTS.md:L7` | `/Users/joshuaf/ai-os` | `C:\Users\Joshu\dev\ai-os` | **HIGH**: Agent file tools fail with 'Path not found' |
| `projects\lsatu\AGENTS.md:L8` | `/Users/joshuaf/ai-os/projects/lsatu` | `C:\Users\Joshu\dev\ai-os\projects\lsatu` | **HIGH**: Subproject resolution failure |
| `projects\lsatu\AGENTS.md:L9` | `/Users/joshuaf/ai-os/wiki/` | `C:\Users\Joshu\dev\ai-os\wiki\` | **HIGH**: Teaching voice and business context lookup failure |
| `projects\lsatu\AGENTS.md:L10` | `/Users/joshuaf/ai-os/archive/wiki-pre-rebuild...` | `C:\Users\Joshu\dev\ai-os\archive\...` | **MEDIUM**: Archive lookup failure |
| `projects\lsatu\AGENTS.md:L12` | `~/Documents/Obsidian Vault/...` | Legacy reference (retired) | **LOW**: Stale historical notice |
| `projects\lsatu\CLAUDE.md:L15` | `/Users/joshuaf/ai-os` | `C:\Users\Joshu\dev\ai-os` | **HIGH**: Claude Code vault resolution failure on Windows |
| `projects\lsatu\CLAUDE.md:L16` | `/Users/joshuaf/ai-os/projects/lsatu` | `C:\Users\Joshu\dev\ai-os\projects\lsatu` | **HIGH**: Subproject repo lookup failure |
| Root `AGENTS.md:L30` | `~/.claude/projects/C--Users-Joshu-dev-a...` | `C:\Users\Joshu\.claude\...` | **LOW**: Unix tilde representation works in bash/git shells |

---

## 8. AGENTS.MD / GEMINI.MD / CLAUDE.MD RUNTIME BEHAVIOR

Empirically observed runtime behaviors on host `J`:

1. **Files Ingested by Antigravity:** `[VERIFIED]` Antigravity reads **both `AGENTS.md` and `GEMINI.md`** when present in the workspace root. Both are injected simultaneously into prompt rules blocks. `CLAUDE.md` is strictly ignored by Antigravity.
2. **Files Ingested by Claude Code:** `[VERIFIED]` Claude Code reads **`CLAUDE.md` only**. It does not ingest `AGENTS.md` or `GEMINI.md`.
3. **Files Ingested by Codex:** `[VERIFIED]` OpenAI Codex reads **`AGENTS.md` only**.
4. **Is `AGENTS.md` Intentionally Cross-Runtime?** `[INFERRED]` Yes. `AGENTS.md` was originally designed for Codex, but modern agent platforms (including Antigravity) adopt it as a generic agent instruction standard. Consequently, Antigravity loads it unless specifically configured otherwise.
5. **Is Concurrent Ingestion Expected?** `[OBSERVED]` In Antigravity's current discovery implementation, having both files at root causes dual injection. This was unintended in the original single-runtime architecture design and causes token bloating and mandate duplication.
6. **Subtree Inheritance:** `[OBSERVED]` Inner instruction files (`projects\lsatu\GEMINI.md`) override broader parent files for their specific directory, but root instructions remain active in the system context, creating internal logical friction.

---

## 9. TARGET CONTROL-PLANE REQUIREMENTS

A formal requirements specification for the future control-plane refactoring:

### Requirement 1: Universal Invariants (Single Authoritative Core)
- Joshua's identity, role as content/product authority, and Jay 2's EA persona.
- The single secret store model: `.env` + `.gitignore` (no vault, no hardcoded secrets).
- Strict Voice Rules: Absolute ban on em-dashes and forbidden AI-slop vocabulary.
- Outbound Communication Rule: Everything student-facing or prospect-facing is drafted, never auto-sent.
- Financial Safety Gate: Explicit confirmation required immediately prior to any Lovable credit spend.

### Requirement 2: Vendor Seam Isolation
- Antigravity configuration must live exclusively in `.gemini/` and not leak into `.agents/` or `.claude/`.
- `skills.json` must be reconfigured to index only `.gemini/skills` and global config, removing the pointer to `.agents/skills`.
- Claude hooks (`auto-pull-hook.sh`, `safe-push.sh`) must stay isolated in `.claude/`.

### Requirement 3: Project-Scoped Responsibility
- Application stack rules (React 18, Vite, Supabase, Tailwind, shadcn) must belong exclusively inside `projects/lsatu/`.
- Visual verification gates (browser tool + dev server DOM check before claiming done) must reside in `projects/lsatu/`.
- Local repository feature-branch workflows (`feat/...`) must not pollute the outer workspace root.

### Requirement 4: On-Demand (Lazy) Reference Architecture
- Routing maps, complete skill tables, and historical product knowledge must NOT be eagerly injected into every turn.
- Eager instructions must be capped under **1,000 tokens**, routing to `wiki/index.md` or dedicated skill files only when relevant to the user request.

### Requirement 5: Tiered Autonomy Framework
- Reconcile the 95% Rule and Maximum Autonomy via explicit risk tiers:
  - **Tier 1 (Read-Only / Verification):** 100% Unilateral Autonomy (file reads, searches, dev-server verification, browser screenshots).
  - **Tier 2 (Reversible Local Development):** Maximum Autonomy without asking (UI edits, bug fixes, unit tests, local branch commits).
  - **Tier 3 (Irreversible / External / Financial):** Mandatory Confirmation Gate (git push to remote, Lovable credit spend, sending emails, database migrations, deleting directories).

---

## 10. ALTERNATIVE ARCHITECTURES

Three candidate control-plane architectures evaluated for external review:

### OPTION A: Minimal Deduplicated Triple (Minimal Change)
- **Layout:** Retain root `AGENTS.md`, `GEMINI.md`, and `CLAUDE.md`, but strictly deduplicate them. Remove the 95% rule from root and replace with the Tiered Autonomy Framework. Fix all stale Mac paths.
- **Eager Token Overhead:** ~4,500 tokens per turn.
- **Advantages:** Lowest migration risk; zero tool or script disruption; preserves familiar file names.
- **Disadvantages:** Antigravity will still ingest both `AGENTS.md` and `GEMINI.md`, continuing to waste ~2,000 tokens on dual rule injection.
- **Complexity & Risk:** Very Low complexity; Very Low risk of regression.

### OPTION B: Shared Universal Core + Vendor Deltas (Recommended)
- **Layout:**
  - `AGENTS.md` at root acts as the **Universal Shared Core** (identity, voice, safety gates, tiered autonomy, retrieval order).
  - Dedicated vendor sub-instructions handle runtime specifics:
    - `.gemini/GEMINI.md` (Antigravity tools, persistent browser port 9223, `.gemini/` paths).
    - `.claude/CLAUDE.md` (Claude Code settings, auto-pull hooks, safe-push script).
    - `.codex/AGENTS.md` (Codex-specific agent TOML configs).
- **Eager Token Overhead:** ~1,800 tokens core + ~500 tokens vendor delta = **~2,300 tokens per turn** (Liberates over 4,000 tokens per interaction!).
- **Advantages:** Single source of truth for identity and voice; clean vendor isolation; massive context window savings.
- **Disadvantages:** Requires ensuring Antigravity and Claude resolve their vendor sub-instructions reliably.
- **Complexity & Risk:** Medium complexity; Low risk of regression.

### OPTION C: Project-First Micro-Control Plane
- **Layout:** Strip root instructions down to an ultra-lean micro-manifest (~600 tokens). Push all operational, development, and testing instructions into `projects/lsatu/GEMINI.md` and skill markdown files.
- **Eager Token Overhead:** ~600 tokens at root; ~1,800 tokens inside subproject.
- **Advantages:** Maximum available context tokens for complex codebase tasks.
- **Disadvantages:** Root EA persona becomes brittle when operating outside `projects/lsatu`; higher risk of agent hallucinating voice or safety rules if sub-skills are not triggered.
- **Complexity & Risk:** High complexity; Medium-High risk of behavioral drift.

---

## 11. EXTERNAL ARCHITECT QUESTIONS

The following fundamental architectural decisions cannot be resolved from machine evidence alone and require human/architect direction:

1. **Instruction Architecture Selection:** Does the architect endorse **Option B (Shared Universal Core + Vendor Deltas)** to eliminate the 2,800-token redundant injection in Antigravity, or is Option A preferred to minimize file structural changes?
2. **Adoption of Tiered Autonomy Framework:** Should the Tiered Autonomy Framework formally replace the binary contradiction between the 95% Rule and the Maximum Autonomy Rule across both root and `projects/lsatu`?
3. **Remote Push Policy Alignment:** What is the authoritative Git push policy for `projects/lsatu`? Should pushing to `origin feat/...` or `origin main` be permitted automatically after passing tests, or must pushes always require explicit user confirmation?
4. **Skill Pruning & Context Curation:** With 98 skills currently suppressed by Antigravity's context budget, should the 10 overlapping skill clusters (e.g. 6 frontend design skills, 5 debugging skills) be consolidated into unified authoritative skills?
5. **Codex Skill Boundary in `skills.json`:** Should `skills.json` be severed from indexing `C:/Users/Joshu/dev/ai-os/.agents/skills` to enforce true runtime isolation between Gemini and Codex?

