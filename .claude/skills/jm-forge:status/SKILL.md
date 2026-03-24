---
name: jm-forge:status
description: Show detailed status for a specific task including its discuss.md, plan.md, and execute.md if they exist.
---

# Skill: jm-forge-status

## Purpose

Show detailed information about a specific task.

## Usage

```
$jm-forge:status <task-id>
```

Example:

```
$jm-forge:status 3
```

## Input

- `task-id`: The numeric ID of the task (e.g., `3`)

## Output

Displays:
1. **Task header**: ID, name, state, Dependon
2. **Phase files**: If discuss.md exists, show goal and open issues count
3. **Plan summary**: If plan.md exists, show step count and checkpoint count
4. **Execute summary**: If execute.md exists, show checkpoint results and final state
5. **Recent iterations**: If discuss-log.md exists, show last iteration summary

## Error Handling

- If task ID not found in TASK-REGISTRY.md: report error
- If phase file missing: note that phase has not been started

## Notes

- Task ID is required as argument
- Always reads from `.planning/TASK-REGISTRY.md` for current state
- Phase files read from `.planning/<task-name>/`
