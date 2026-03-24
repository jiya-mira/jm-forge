---
name: jmf-execute
description: Execute the plan for a task. Verify checkpoints and report results.
---

# Skill: jm-forge-execute

## Purpose

Execute the plan for a task, verifying checkpoints and reporting results.

## Usage

```
$jmf-execute <task-id>
```

Example:

```
$jmf-execute 3
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
2. **If unresolvable** — Append Iteration to `discuss-log.md`, update `execute.md` with failure reason
   - Do NOT视为"失败" — 视为"迭代"
   - Do NOT强制 spawn Dependon — unless truly needed
3. **Continue execution** or update plan and re-execute

### 5. Termination States

| Final State | Condition |
|-------------|-----------|
| `Completed` | All steps + all checkpoints verified |
| `Failed` | Checkpoint failed, cannot continue |
| `Pending` | Blocked by Dependon, can resume |

### 6. Document

Write to `.planning/<task-name>/execute.md` using the following template:

```markdown
# Execute — <task-name>

**Date:** <YYYY-MM-DD>
**Source:** plan.md

---

## Checkpoint Log

## Batch 1

**[Checkpoint 1: <name>]**
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>

**[Checkpoint 2: <name>]**
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>

## Batch 2 (if applicable)

**[Checkpoint 3: <name>]**
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>

---

## Acceptance Report

<Summary of whether task met its acceptance criteria defined in Discuss>
```

## Exit Points

User can pause execution at any time. Task state becomes `Pending` and can be resumed later.

## Iteration Norms

### Execute as Iteration

- Checkpoint failures are "iterations", not "failures"
- Append to `discuss-log.md` with Iteration N when issues arise
- Update `execute.md` with actual results vs expected

### State as Position Marker

- State reflects main work position
- Iterations do NOT force State changes
- Only set `Failed` when truly cannot proceed

## Notes

- Input is solely the plan output — no other sources consulted
- Checkpoint failures use same protocol as Plan blocking issues
