# Plan — jm-forge-init

**Date:** 2026-03-23
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Define schema — typed nodes and relationships

**Action:** Define the exact JSON schema for all node types and relationship types

**Approach:**
- Draft `project.json` schema: top-level metadata (name, type, description, domains[])
- Draft `domains.json` schema: domain nodes with typed relationships
- Draft `entries.json` schema: entry point nodes
- Draft `assets.json` schema: asset nodes
- Draft `relationships.json` schema: typed edges between nodes
- Define graceful `unknown-type` fallback for both nodes and relationships
- Output as a schema reference document

**Checkpoint:** `schema-defined`
- All 5 JSON schema files drafted with nodeType and relationshipType enums
- `unknown-type` fallback defined and documented

---

### Step 2: Create PROJECT-MAP/ directory skeleton

**Action:** Create the `PROJECT-MAP/` directory structure and skeleton files

**Approach:**
- Create `PROJECT-MAP/` directory at project root
- Create empty skeleton JSON files: `project.json`, `domains.json`, `entries.json`, `assets.json`, `relationships.json`
- Create `SUMMARY.md` as human-readable entry point
- Add schema reference comment at top of each JSON file

**Checkpoint:** `skeleton-created`
- `PROJECT-MAP/` directory exists with all 6 files (5 JSON + 1 MD)
- Each JSON file has schema documentation comment

---

### Step 3: Implement discovery logic — top-level analysis

**Action:** Scan working directory and populate `project.json` (top-level summary)

**Approach:**
- Scan root directory structure (ls, glob patterns)
- Identify project type indicators (package.json, Cargo.toml, README, etc.)
- Generate top-level `project.json`: name, projectType, description, domainList
- For multi-project collections: populate `domains.json` with sub-project nodes

**Checkpoint:** `top-level-populated`
- `project.json` contains valid top-level summary
- For multi-project: `domains.json` contains all sub-project nodes

---

### Step 4: Implement discovery logic — entries and assets

**Action:** Identify entry points and assets, populate `entries.json` and `assets.json`

**Approach:**
- Entry points: README, main.*, index.*, Makefile, docker-compose.yml, etc.
- Assets: config files, .env templates, static resources, data files
- Each node: `{ id, name, path, type, description, relationships[] }`
- Use heuristics + file content inspection to determine description
- When uncertain: prompt user for confirmation; if user unsure, set description to `null` (unknown)

**Checkpoint:** `entries-assets-populated`
- `entries.json` contains identified entry points
- `assets.json` contains identified assets
- Uncertain items flagged for user confirmation

---

### Step 5: Implement discovery logic — relationships

**Action:** Analyze and populate `relationships.json`

**Approach:**
- Scan source/asset files for import/require/reference statements
- Match relationships against defined types (depends-on, implements, contains, references, builds-on)
- Build typed edge list: `{ from, to, type, confidence }`
- Confidence: high/medium/low — if low, flag for user confirmation
- If relationship type truly unclear: mark as `unknown-type`

**Checkpoint:** `relationships-populated`
- `relationships.json` contains all identified relationships with typed edges
- Low-confidence items flagged for user confirmation

---

### Step 6: Generate SUMMARY.md

**Action:** Generate human-readable `SUMMARY.md` based on all JSON data

**Approach:**
- Read all populated JSON files
- Generate layered summary:
  - Top-level overview (from project.json)
  - Domain breakdown (from domains.json)
  - Key entry points (from entries.json)
  - Key relationships summary (from relationships.json)
- Navigation: each section links to relevant JSON detail
- Token-efficient: SUMMARY.md is the primary human navigation doc

**Checkpoint:** `summary-generated`
- `SUMMARY.md` is readable and navigable
- Each section references relevant JSON data
- Total size kept small (summary only, not full data dump)

---

### Step 7: Implement jm-forge-init skill

**Action:** Create `jm-forge-init` skill in `.claude/skills/`

**Approach:**
- Create `.claude/skills/jm-forge-init/SKILL.md`
- Skill reads all PROJECT-MAP/ files as context when running discuss for any task
- Skill supports `--refresh` flag to re-run discovery
- Document agent-agnostic nature: this skill is not tied to Claude Code

**Checkpoint:** `skill-created`
- `jm-forge-init/SKILL.md` exists and documents the full workflow
- Skill does not depend on any specific agent platform

---

### Step 8: Update jm-forge-discuss to read PROJECT-MAP

**Action:** Update `jm-forge-discuss` skill to read PROJECT-MAP/ during discuss phase

**Approach:**
- In `jm-forge-discuss` SKILL.md, add instruction to read `PROJECT-MAP/SUMMARY.md` (and relevant JSON on demand) before starting discuss
- This ensures all discuss phases benefit from project context

**Checkpoint:** `discuss-updated`
- `jm-forge-discuss` SKILL.md includes PROJECT-MAP reading instruction

---

## Dependencies

Step 3 depends on Step 2. Steps 4 and 5 depend on Step 3. Step 6 depends on Steps 4 and 5. Steps 7 and 8 are independent of earlier steps but depend on having schemas defined.

## Tracking

| Assumption | Risk |
|-----------|------|
| Heuristics for entry point detection work across project types | Medium — may need user confirmation for non-software projects |
| Token cost of full directory scan is acceptable | Medium — user manually triggers, so cost is controlled |
| `unknown-type` fallback is acceptable for Agent usability | Low — Agent can handle null descriptions gracefully |

## Execution Order

Sequential: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
