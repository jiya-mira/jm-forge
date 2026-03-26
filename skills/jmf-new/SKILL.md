---
name: jmf-new
description: Create a new task and add it to .workspace/tasks/INDEX.md with state New.
---

# Skill: jmf-new

## Purpose

Create a new task entry in `.workspace/tasks/INDEX.md`.

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
   - Check if `.workspace/tasks/INDEX.md` exists.
   - **If missing**: Create it by copying `templates/tasks-index-header.md`.
   - **If exists**: Read index IDs and existing task directory IDs, use `max_id + 1`.

2. **Create task directory**: Create `.workspace/tasks/<id>-<task-name>/` directory

3. **Update `.workspace/tasks/INDEX.md`**: Append catalog row (v2 schema)
   - Row format: `| <3-digit-id> | \`<3-digit-id>-<task-name>/\` | New | 🆕 | <dependon-id-or-dash> | <one-line-summary> | - |`

4. **Create initial discuss-log.md**: Create `.workspace/tasks/<id>-<task-name>/discuss-log.md` by copying `templates/initial-discuss-log.md` and filling task metadata placeholders:
   - `{{TASK_ID}}` -> numeric task ID
   - `{{TASK_NAME}}` -> task name
   - `{{DATE}}` -> creation date in `YYYY-MM-DD`

5. **Update .workspace/project-map/**: If `.workspace/project-map/` exists, append new task node to `domains.json` and add relationship edge if parent domain exists

## Output

- New task ID
- Task name
- Dependon status (if any)
- Location of task directory

## Error Handling

- If task-name already exists in `.workspace/tasks/INDEX.md`: report error
- If `--dependon` ID does not exist in `.workspace/tasks/INDEX.md`: report error

## Notes

- State is always `New` when created via this skill
- To move a task from New to Discussing, use `jmf-discuss`
- Automatically initializes `.workspace/tasks/INDEX.md` if it doesn't exist
