---
name: jm-forge:new
description: Create a new task and add it to TASK-REGISTRY.md with state New.
---

# Skill: jm-forge-new

## Purpose

Create a new task entry in the task registry.

## Usage

```
$jm-forge:new <task-name> [--dependon <id>]
```

Example:

```
$jm-forge:new my-new-skill
$jm-forge:new another-task --dependon 3
```

## Input

- `task-name`: Name of the new task (kebab-case recommended)
- `--dependon <id>`: Optional. If specified, this task depends on another task

## Behavior

1. **Record Original Description**: Preserve the user's raw input exactly as provided (do not pre-process or interpret)
2. **Goal Clarification (Initial)**: Ask the user:
   - "What is the goal of this task?"
   - "Is this related to an existing task?"
3. **Determine next ID**: Read `.planning/TASK-REGISTRY.md`, find max ID, use next integer
4. **Create task directory**: Create `.planning/<task-name>/` directory
5. **Update TASK-REGISTRY.md**: Add new row with id, name, state=New, Dependon
6. **Create initial discuss-log.md**: With Iteration 0 (Goal Clarification) based on user's responses
7. **Update PROJECT-MAP/**: If `PROJECT-MAP/` exists, append new task node to `domains.json` (type: Domain, path: `.planning/<task-name>/`) and add relationship edge if parent domain exists

## Output

- New task ID
- Task name
- Dependon status (if any)
- Location of task directory
- Recorded original description
- Preliminary Goal Clarification (as provided by user)

## Error Handling

- If task-name already exists in registry: report error
- If `--dependon` ID does not exist: report error

## Notes

- State is always `New` when created via this skill
- To move a task from New to Discussing, use `jm-forge:discuss`
- **Goal Clarification is dynamic**: The goal may evolve during discuss/plan/execute. This is normal, not a planning failure.
- **Split Detection awareness**: If uncertain whether this task should be split or merged with an existing one, prompt the user to use `jm-forge:discuss` for further clarification.
