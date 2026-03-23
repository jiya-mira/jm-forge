# Discuss — jm-forge-init-refresh

**Date:** 2026-03-23
**Status:** Concluded
**Task ID:** 9

---

## Goal

Add re-run support and incremental maintenance protocol to PROJECT-MAP. Ensure the map remains accurate and useful over time without requiring full rebuilds.

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** Re-run semantics (split into two skills), incremental maintenance protocol, discuss phase freshness check
- **Out of scope:** Hook-based filesystem monitoring (D) — deferred to future iteration

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. First-time init and refresh/sync are semantically different — should be separate skills
2. Agent can self-decide merge strategy in most cases; user override is available
3. Maintenance should be lightweight and become habitual, not a separate workflow

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. `jm-forge:init` and `jm-forge:sync` are clearly separate skills with distinct purposes
2. User can force a full refresh via `sync --force-refresh`
3. When `jm-forge:new` or other skills create new project elements, PROJECT-MAP is updated
4. `jm-forge:discuss` checks map freshness and prompts user if stale
5. Map maintenance convention is documented and human-habitual

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | Exact merge strategy for sync (preserve user edits, detect stale nodes, delete removed) | No | Agent self-decides with user override |
| 2 | How to detect "stale" — timestamp comparison, structural diff, or heuristic? | No | Check freshness threshold + structural hint |

*(Resolved issues: none)*

---

## Key Decisions

### Skill Split: `jm-forge:init` vs `jm-forge:sync`

**`jm-forge:init`**
- Purpose: First-time project mapping — create PROJECT-MAP/ from scratch
- When: User first introduces jm-forge to a project
- Idempotent: if PROJECT-MAP/ exists, report "already initialized"

**`jm-forge:sync`**
- Purpose: Update existing PROJECT-MAP/ — incremental maintenance
- Flags:
  - `--force-refresh`: full rebuild (like re-running init)
  - (default): incremental merge
- Agent self-decides merge strategy: preserve user-edited descriptions, add new nodes, mark stale nodes (nodes referencing deleted files), remove truly obsolete nodes
- User can override: "force refresh" overrides Agent decisions

**Source:** discuss-log.md → Iteration 1

### Maintenance Protocol: A + B + C

**A. Skills-driven updates:**
- `jm-forge:new` — after creating `.planning/<task-name>/`, update `domains.json` or `entries.json`
- `skill-scaffold` — after generating new skill, update relevant asset/entry maps
- General rule: any skill that creates a new "meaningful" file should update PROJECT-MAP

**B. Convention-driven updates:**
- Document in `PROJECT-MAP/SUMMARY.md` and `AGENTS.md`: "When you create, delete, or rename meaningful project elements, update PROJECT-MAP/"
- This is a human habit, not automated enforcement

**C. Discuss phase freshness check:**
- In `jm-forge:discuss` Setup step 1, after reading PROJECT-MAP/SUMMARY.md, check if map is stale
- Stale threshold: if any map element references a file that no longer exists, or if lastUpdated is older than N days (configurable, default 7)
- If stale: prompt user "PROJECT-MAP may be outdated. Run `jm-forge:sync` to update?"
- This ensures maps don't go stale without user awareness

**Source:** discuss-log.md → Iteration 1

---

## Conclusion

Split into two skills: `jm-forge:init` (first-time) and `jm-forge:sync` (incremental + force refresh). Agent self-decides merge strategy. Skills update map when creating new elements. Convention documents habit. Discuss phase checks freshness and prompts if stale. Hook-based monitoring deferred.

Ready for Plan.

**Source:** discuss-log.md → Iteration 1
