# Map Cascade Spec (Initial, Task 29)

**Primary focus:** `.workspace/project-map/`, `.workspace/resource-map/`
**Secondary sync:** `.workspace/exp-map/` (structure consistency only)

---

## 1. Goal

Provide initial internal cascade support so a reader/model can traverse map artifacts in deterministic order from entry to details.

## 2. Cascade Model (Initial)

### project-map cascade

1. `INDEX.md` (human routing)
2. `SUMMARY.md` (compact semantic overview)
3. `project.json` (global metadata / map root)
4. `domains.json`, `entries.json`, `assets.json` (typed nodes)
5. `relationships.json` (cross-node graph)
6. `schema-reference.md` (schema details)

### resource-map cascade

1. `INDEX.md` (human routing)
2. `resources.json` (resource source of truth)

### exp-map sync rule

- Keep `INDEX.md` + `DIRECTORY-INDEX.md` consistent with the same index writing convention.
- Do not add complex cascade graph in this task.

## 3. Writing Rules

- Each map index must declare:
  - managed files and directory ownership
  - cascade order (what to open first/next)
  - update triggers
- Terminology must be consistent across map indexes (`entry`, `source of truth`, `cascade`).

## 4. Initial Implementation Boundary

In-scope for this task:
- document cascade order in map indexes/summaries
- add minimal cascade metadata where safe

Out-of-scope for this task:
- introducing new map engine
- deep auto-linking mechanics
- schema-versioning redesign

## 5. Verification Points

- `project-map` has explicit cascade entry/order in docs.
- `resource-map` has explicit cascade entry/order in docs.
- No broken path references after updates.
