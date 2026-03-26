---
name: jmf-sync
description: Update an existing PROJECT-MAP. Use --force-refresh for full rebuild, or default for incremental sync.
---

# Skill: jmf-sync

## Purpose

Update an existing `.workspace/project-map/` context map. Handles incremental maintenance and force refresh.

## Map Boundary Charter

- `project-map` focuses on project-native files/modules and their layered `tree + graph` relations.
- `.workspace` runtime artifacts are not primary `project-map` recording targets.
- `resource-map` and `project-map` keep a thin relationship: design ideas may be shared, but data ownership is separate.

## Templates

- `templates/project-map-sync-merge-rules.md`

## Usage

```
$jmf-sync [--force-refresh] [--stale-threshold <days>]
```

**Flags:**
- `--force-refresh`: Full rebuild — discard Agent's previous merge decisions and re-run discovery from scratch
- `--stale-threshold <days>`: Number of days after which map is considered stale (default: 7)
- (default, no flags): Incremental sync — add new nodes, mark stale, preserve user edits

## Pre-conditions

- `.workspace/project-map/` must already exist (use `jmf-init` first if it does not)

## Behavior

### 1. Check .workspace/project-map/ exists

If `.workspace/project-map/` does not exist: report ".workspace/project-map/ not found. Run `jmf-init` first."

### 2. Determine mode

**Force refresh (`--force-refresh`):**
- Re-run full discovery from scratch
- Discard previous merge decisions
- Equivalent to re-running `jmf-init` but preserves the same directory

**Incremental sync (default):**
- Scan for new files → add nodes
- Check existing nodes for stale references (path no longer exists) → mark as `stale: true`
- Check for deleted files → mark corresponding nodes stale
- Preserve user-edited descriptions (don't overwrite unless `--force-refresh`)
- Agent self-decides: when in doubt, prefer preservation over deletion

### 3. Merge Strategy

| Scenario | Action |
|----------|--------|
| New file discovered | Add node with inferred type and description |
| Existing node still valid | Preserve (keep existing description) |
| Node references deleted file | Mark `stale: true`, keep in map |
| Node type unclear | Set `type: Unknown`, confidence: low |
| Relationship unclear | Set `type: unknown-type` |

Template-first rule:
- Apply merge constraints from `templates/project-map-sync-merge-rules.md`

### 4. Update `lastUpdated`

Set `project.json.lastUpdated` to current date.

### 5. Report

Report:
- New nodes added
- Nodes marked stale
- Changes made

### 6. Resources

**Check for resources:**
- During sync, check if `.workspace/resource-map/resources.json` exists
- If exists, include lightweight resource references only when they help project navigation
- Resource details remain in `.workspace/resource-map/resources.json`

**Resource scan:**
- After sync, ask user: "是否要重新扫描项目发现新资源？"
- If yes, use `jmf-resource scan` workflow
- User confirms each resource before registration
- Scan is non-destructive — only suggests, never auto-registers

**Sync behavior:**
- If resources changed, update related lightweight references only where needed
- If new resources added via `jmf-resource add`, include in next sync

## Notes

- This skill is agent-agnostic — does not depend on Claude Code or any specific agent platform
- For first-time setup, use `jmf-init` — this skill requires an existing .workspace/project-map/
- Maintenance convention: run this after creating/deleting/renaming meaningful project elements
