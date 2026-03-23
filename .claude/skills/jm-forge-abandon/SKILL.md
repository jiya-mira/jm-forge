---
name: jm-forge-abandon
description: Mark a task as Abandoned. This is a user-initiated action only.
---

# Skill: jm-forge-abandon

## Purpose

Mark an existing task as Abandoned.

## Usage

```
$jm-forge:abandon <task-id> [--reason <text>]
```

Example:

```
$jm-forge:abandon 3
$jm-forge:abandon 3 --reason "用户改变主意"
```

## Input

- `task-id`: The numeric ID of the task to abandon
- `--reason <text>`: Optional. Reason for abandoning

## Behavior

1. **Confirm with user**: Ask for confirmation before marking as Abandoned
2. **Update TASK-REGISTRY.md**: Set state to `Abandoned`
3. **Update Notes column**: Add abandonment reason if provided

## Important

- **This is a user-initiated action**. The Agent should confirm before marking.
- Only user can set Abandoned state. Agent never sets this automatically.
- Once Abandoned, the task cannot be moved to any other state.

## Output

- Task ID and name
- Confirmation that it was marked Abandoned
- Reason if provided

## Error Handling

- If task ID not found: report error
- If task already Abandoned: report that it's already abandoned
- If task Completed or Failed: warn user (abandoning completed tasks is unusual)
