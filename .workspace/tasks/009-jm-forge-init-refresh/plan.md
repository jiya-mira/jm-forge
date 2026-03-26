# Plan — jm-forge-init-refresh

**Date:** 2026-03-23
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Create `jm-forge:sync` skill

**Action:** Create `jm-forge:sync` skill in `.claude/skills/`

**Approach:**
- Create `.claude/skills/jm-forge-sync/SKILL.md`
- `--force-refresh` flag: full rebuild (equivalent to re-running init)
- Default (no flag): incremental sync
  - Scan for new files → add nodes
  - Check existing nodes for stale references (deleted files) → mark stale
  - Preserve user-edited descriptions unless `--force-refresh`
- Agent self-decides merge strategy; user can override
- Output: updated PROJECT-MAP/ files

**Checkpoint:** `sync-skill-created`
- `.claude/skills/jm-forge-sync/SKILL.md` exists with full behavior defined

---

### Step 2: Update `jm-forge:init` to be first-time only

**Action:** Update `jm-forge:init` SKILL.md to clarify it is first-time only

**Approach:**
- Update SKILL.md: if PROJECT-MAP/ already exists, direct user to `jm-forge:sync`
- Remove any refresh/overwrite logic from init (that's sync's job)

**Checkpoint:** `init-updated`
- `jm-forge:init` SKILL.md states it requires PROJECT-MAP/ to not exist

---

### Step 3: Add maintenance calls in task-creating skills

**Action:** Update `jm-forge:new` and `skill-scaffold` to call `jm-forge:sync` after creating new elements

**Approach:**
- In `jm-forge:new`: after creating `.planning/<task-name>/` directory, append new node to `domains.json` (or entries.json if appropriate)
- In `skill-scaffold`: after creating new skill directory, append new node to relevant JSON
- Use sync-style incremental update (not full refresh)

**Checkpoint:** `task-skills-updated`
- `jm-forge:new` SKILL.md notes PROJECT-MAP update step
- `skill-scaffold` notes PROJECT-MAP update step

---

### Step 4: Document maintenance convention

**Action:** Add maintenance convention to AGENTS.md and PROJECT-MAP/SUMMARY.md

**Approach:**
- In AGENTS.md: add "PROJECT-MAP Maintenance" section: when you create, delete, or rename meaningful project elements, run `jm-forge:sync` or manually update PROJECT-MAP/
- In PROJECT-MAP/SUMMARY.md: add maintenance note at top

**Checkpoint:** `convention-documented`
- AGENTS.md contains PROJECT-MAP maintenance convention
- PROJECT-MAP/SUMMARY.md contains maintenance reminder

---

### Step 5: Add freshness check in `jm-forge:discuss`

**Action:** Update `jm-forge:discuss` to check PROJECT-MAP freshness before starting discuss

**Approach:**
- In Setup step 1 (already reads PROJECT-MAP/SUMMARY.md), add freshness check:
  - If `project.json.lastUpdated` is older than N days (default: 7), flag as stale
  - If any node references a non-existent path, flag as stale
  - If stale: prompt user "PROJECT-MAP may be outdated. Run `jm-forge:sync` to update?"
  - Do not block — user can proceed without syncing
- Threshold configurable: `sync --stale-threshold 30` (days)

**Checkpoint:** `freshness-check-added`
- `jm-forge:discuss` SKILL.md Setup step 1 includes freshness check

---

## Dependencies

Steps 1 and 2 are independent. Steps 3, 4 depend on Steps 1 and 2. Step 5 depends on Steps 1 and 2.

## Tracking

| Assumption | Risk |
|-----------|------|
| Agent self-decides merge strategy correctly in most cases | Medium — user can override with `--force-refresh` |
| 7-day stale threshold is reasonable default | Low — configurable |

## Execution Order

Sequential: 1 → 2 → (3, 4, 5) — Steps 3, 4, 5 can be done in any order after 1 and 2
