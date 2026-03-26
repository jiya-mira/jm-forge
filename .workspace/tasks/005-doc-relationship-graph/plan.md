# Plan — doc-relationship-graph

**Date:** 2026-03-23
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Audit all documents in .planning/

**Action:** Enumerate all documents under `.planning/` and classify them by type

**Approach:**
- List all `.md` files under `.planning/` and `.claude/skills/`
- Classify each as: Entry Point, Phase Doc (discuss/plan/execute), Log, Template, Registry, Skill
- Build a document inventory table

**Checkpoint:** `doc-inventory-complete`
- All .md files in .planning/ are catalogued with type and path
- No orphaned documents without classification

---

### Step 2: Update AGENTS.md as entry point

**Action:** Make AGENTS.md list all key documents with their purpose and relationships

**Approach:**
- Add document index section listing all Phase directories and their documents
- For each skill, list its SKILL.md
- Add navigation summary showing "entry point → phase docs → logs"

**Checkpoint:** `agents-md-complete`
- AGENTS.md contains a "Document Index" section
- Each listed document has a one-line description of its role

---

### Step 3: Update TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） with document relationship note

**Action:** Add reference conventions to TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） header or a dedicated section

**Approach:**
- Append a "Reference Conventions" section explaining the flow: discuss→discuss-log, plan→discuss, execute→plan
- List the entry points (TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） itself, AGENTS.md)

**Checkpoint:** `registry-ref-conventions-added`
- TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） contains a "Reference Conventions" section
- Convention rules are clearly stated

---

### Step 4: Backfill cross-references in existing phase docs

**Action:** Ensure all existing phase docs (discuss.md, plan.md, execute.md) reference their source doc per convention

**Approach:**
- For each phase doc that lacks a reference to its source, add a "Source:" line at the top
- Format: `**Source:** discuss.md` at the top of plan.md; `**Source:** discuss-log.md` at top of discuss.md

**Checkpoint:** `cross-refs-backfilled`
- Every discuss.md, plan.md, execute.md in .planning/ has a **Source:** field
- No phase doc is missing its source reference

---

### Step 5: Verify navigation from entry points

**Action:** Verify that a new Agent can reach any document starting from entry points

**Approach:**
- From TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）: should link to all task phase dirs
- From AGENTS.md: should link to skills and key docs
- Trace manually: TASK-REGISTRY → task-N → discuss → plan → execute (all reachable)

**Checkpoint:** `navigation-verified`
- Entry points list all phase directories
- Each phase directory contains its expected documents
- No document is unreachable from entry points

---

## Dependencies

Steps 1–3 are independent. Step 4 depends on Step 1 (inventory needed to find all phase docs). Step 5 depends on Steps 2, 3, 4.

## Tracking

| Assumption | Risk |
|-----------|------|
| All phase docs follow naming convention (discuss.md, plan.md, execute.md) | Low — existing docs already follow it |
| AGENTS.md and TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） are stable entry points | Low — already established as entry points |
| User wants backfill of existing docs, not just new ones | Medium — if not needed, Step 4 can be skipped |

## Execution Order

Sequential with noted dependencies: 1 → (2, 3) → 4 → 5
