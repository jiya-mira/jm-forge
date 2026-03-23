---
name: jm-forge-execute
description: Execute the plan for a task. Verify checkpoints and report results.
---

# Skill: jm-forge-execute

## Purpose

Execute the plan for a task, verifying checkpoints and reporting results.

## Usage

```
$jm-forge:execute <task-id>
```

Example:

```
$jm-forge:execute 3
```

## Input

- `task-id`: The numeric ID of the task

## Pre-conditions

- Task must exist in `.planning/TASK-REGISTRY.md`
- Task state must be `Pending`, `Active`, or manually set

## Behavior

### 1. Setup
1. Read TASK-REGISTRY.md, confirm task exists
2. Set task state to `Active`
3. Read plan from `.planning/<task-name>/plan.md`

### 2. Execute Steps

Execute steps sequentially, following the dependency order in Plan.

**Checkpoint reporting format:**
```
[Checkpoint N: <name>]
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>
```

### 3. Batch Handling

If plan has parallel steps (same batch), group checkpoints under `## Batch N` heading.

### 4. Failure Handling

On checkpoint failure:
1. **Attempt self-resolution** — Adjust subsequent steps, retry if possible
2. **If unresolvable** — Spawn a new task, mark current as `Dependon <new-task-id>`
3. **Set state to Pending** — Task can be resumed after blocking issue resolved

### 5. Termination States

| Final State | Condition |
|-------------|-----------|
| `Completed` | All steps + all checkpoints verified |
| `Failed` | Checkpoint failed, cannot continue |
| `Pending` | Blocked by Dependon, can resume |

### 6. Document

Write to `.planning/<task-name>/execute.md` using template from `.planning/templates/execute.md`.

## Exit Points

User can pause execution at any time. Task state becomes `Pending` and can be resumed later.

## Notes

- Input is solely the plan output — no other sources consulted
- Uses templates from `.planning/templates/execute.md`
- Checkpoint failures use same protocol as Plan blocking issues
