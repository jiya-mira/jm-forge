# Plan — external-resources-support

**Date:** 2026-03-23
**Source:** discuss.md (consumed)

---

## Steps

### Step 1: Define external-resources.json schema

**Action:** Create `.external/external-resources.json` schema definition and sample

**Approach:**
- Define JSON schema for external resources based on discuss decisions
- Core fields: id, name, category, description, controllable, safety, relationships, attributes, notes
- Create sample file with example entries (equipment like dumper truck, server, etc.)
- Place schema definition in `.planning/external-resources-support/`

**Checkpoint:** `schema-defined`
- external-resources.json schema supports all core fields
- Sample demonstrates equipment, server, and organization categories
- JSON is valid

---

### Step 2: Create jm-forge-external skill

**Action:** Create `jm-forge-external` SKILL.md in `.claude/skills/`

**Approach:**
- Define skill with sub-commands: add, list, remove
- `add`: Guide user to add new external resource with interactive prompts
- `list`: Display all registered external resources
- `remove`: Remove a resource by ID
- Skill reads/writes `.external/external-resources.json`

**Checkpoint:** `skill-created`
- SKILL.md exists at `.claude/skills/jm-forge-external/SKILL.md`
- Skill can be invoked via `/jm-forge-external`
- Sub-commands: add, list, remove are documented

---

### Step 3: Integrate external resources into jm-forge-init

**Action:** Update `jm-forge-init` SKILL.md to support external resources

**Approach:**
- During init, check if `.external/external-resources.json` exists
- If exists, load and include external resources in PROJECT-MAP context
- Add prompt to ask user: "是否要注册外部资源？"
- If user says yes, invoke flow to add resource via jm-forge-external

**Checkpoint:** `init-extended`
- init reads `.external/external-resources.json` if present
- init prompts user about external resources
- External resources are included in project context

---

### Step 4: Integrate external resources into jm-forge-sync

**Action:** Update `jm-forge-sync` SKILL.md to support external resources

**Approach:**
- During sync, check if `.external/external-resources.json` exists
- Include external resources in sync scope
- Optionally prompt: "外部资源是否有更新？"

**Checkpoint:** `sync-extended`
- sync reads `.external/external-resources.json` if present
- External resources are included in sync scope

---

### Step 5: Add external-resource node type to PROJECT-MAP

**Action:** Update `PROJECT-MAP/domains.json` to include external-resource nodes

**Approach:**
- When init/sync processes external resources, add them as nodes to PROJECT-MAP
- Node type: `external-resource`
- Include: id, name, category, description from external-resources.json
- Mark with `external: true`

**Checkpoint:** `project-map-extended`
- external-resource nodes appear in PROJECT-MAP/domains.json
- Nodes have `type: "external-resource"` and `external: true`

---

## Dependencies

| Step | Depends on |
|------|------------|
| Step 2 | — |
| Step 3 | Step 1, Step 2 |
| Step 4 | Step 1, Step 2 |
| Step 5 | Step 1 |

**Order:** Step 1 → Step 2 → (Step 3, Step 4, Step 5 in parallel)

---

## Tracking

| Assumption | Risk |
|-----------|------|
| User will manually create `.external/` directory initially | Low — skill can create it |
| JSON schema is flexible enough for all resource types | Low — attributes is fully extensible |
| init/sync modifications won't break existing behavior | Low — additions only, no modifications to existing logic |

---

## Execution Order

**Parallel with dependencies:** Step 3, 4, 5 depend on Step 1 & 2, so execute Step 1 → Step 2, then Steps 3-5 can proceed.
