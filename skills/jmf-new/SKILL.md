---
name: jmf-new
description: Create a new task and add it to TASK-REGISTRY.md with state New.
---

# Skill: jmf-new

## Purpose

Create a new task entry in the task registry.

## Usage

```
$jmf-new <task-name> [--dependon <id>]
```

Example:

```
$jmf-new my-new-skill
$jmf-new another-task --dependon 3
```

## Input

- `task-name`: Name of the new task (kebab-case recommended)
- `--dependon <id>`: Optional. If specified, this task depends on another task

## Behavior

1. **Determine next ID**:
   - Check if `.planning/TASK-REGISTRY.md` exists.
   - **If missing**: Create it by copying `templates/registry-header.md`.
   - **If exists**: Read file, find the maximum numeric ID, use `max_id + 1`.

2. **Create task directory**: Create `.planning/<task-name>/` directory

3. **Update TASK-REGISTRY.md**: Append row `| <id> | <task-name> | New | <dependon-id-or-dash> | |`

4. **Create initial discuss-log.md**: Create `.planning/<task-name>/discuss-log.md` by copying `templates/initial-discuss-log.md` and filling task metadata.

5. **Update PROJECT-MAP/**: If `PROJECT-MAP/` exists, append new task node to `domains.json` and add relationship edge if parent domain exists

## Output

- New task ID
- Task name
- Dependon status (if any)
- Location of task directory

## Error Handling

- If task-name already exists in registry: report error
- If `--dependon` ID does not exist: report error

## Notes

- State is always `New` when created via this skill
- To move a task from New to Discussing, use `jmf-discuss`
- Automatically initializes `.planning/TASK-REGISTRY.md` if it doesn't exist
