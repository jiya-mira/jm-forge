---
name: jmf-sync
description: Update an existing PROJECT-MAP. Use --force-refresh for full rebuild, or default for incremental sync.
---

# Skill: jm-forge-sync

## Purpose

Update an existing `PROJECT-MAP/` context map. Handles incremental maintenance and force refresh.

## Usage

```
$jmf-sync [--force-refresh] [--stale-threshold <days>]
```

**Flags:**
- `--force-refresh`: Full rebuild — discard Agent's previous merge decisions and re-run discovery from scratch
- `--stale-threshold <days>`: Number of days after which map is considered stale (default: 7)
- (default, no flags): Incremental sync — add new nodes, mark stale, preserve user edits

## Pre-conditions

- `PROJECT-MAP/` must already exist (use `jmf-init` first if it does not)

## Behavior

### 1. Check PROJECT-MAP/ exists

If `PROJECT-MAP/` does not exist: report "PROJECT-MAP/ not found. Run `jmf-init` first."

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

### 4. Update `lastUpdated`

Set `project.json.lastUpdated` to current date.

### 5. Report

Report:
- New nodes added
- Nodes marked stale
- Changes made

### 6. Resources

**Check for resources:**
- During sync, check if `RESOURCE-MAP/resources.json` exists
- If exists, include resources in the sync scope
- Resources should appear in `domains.json` as `resource` nodes

**Resource scan:**
- After sync, ask user: "是否要重新扫描项目发现新资源？"
- If yes, use `jmf-resource scan` workflow
- User confirms each resource before registration
- Scan is non-destructive — only suggests, never auto-registers

**Sync behavior:**
- If resources changed, update the corresponding nodes in domains.json
- If new resources added via `jmf-resource add`, include in next sync

## Notes

- This skill is agent-agnostic — does not depend on Claude Code or any specific agent platform
- For first-time setup, use `jmf-init` — this skill requires an existing PROJECT-MAP/
- Maintenance convention: run this after creating/deleting/renaming meaningful project elements
