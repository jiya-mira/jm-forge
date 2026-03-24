---
name: jm-forge:execute
description: Execute the plan for a task. Verify checkpoints and report results.
---

# Skill: jm-forge-execute

## Purpose

Execute the plan for a task, verifying checkpoints and reporting results.

## Core Principles

### Goal Clarification is Upstream

Execute's output is determined by the Goal Clarification from Discuss. The Goal defines what Execute is trying to achieve — Execute does not assume a specific type of outcome.

### Goal Clarification is Dynamic

The goal may evolve during execution. This is **normal**, not a planning failure. If the goal changes, record it and confirm with the user before proceeding.

### Split Detection: Uncertainty Questioning Principle

- Do not use hardcoded trigger conditions
- When the Agent feels uncertain about task boundaries or whether issues belong to the same task, stop and ask the user
- **Agent's responsibility: feels uncertain → stop and ask**

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
4. Note the Goal Clarification output from Discuss — this defines what Execute is trying to achieve

### 2. Execute Steps

Execute steps sequentially, following the dependency order in Plan.

**Checkpoint reporting format:**
```
[Checkpoint N: <name>]
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>
```

### 3. Split Detection Checkpoint

At any point during execution, if the Agent feels uncertain whether:
- The current execution approach is still aligned with the goal
- Task boundaries have become unclear
- Issues encountered belong to this task or should be a separate task

The Agent should:
1. **Stop execution** (do not continue blindly)
2. Append a Split Detection iteration to `discuss-log.md`
3. Present options to the user:
   - Option A: Continue in current task
   - Option B: Split out and create new task(s)
   - Option C: Adjust approach but continue
4. Wait for user confirmation before resuming execution

### 4. Goal Evolution During Execution

If during execution the Agent realizes the goal has evolved:
1. **Stop execution** (do not continue blindly)
2. Record the new goal
3. Present it to the user for confirmation
4. Do not proceed until the goal is confirmed

### 5. Batch Handling

If plan has parallel steps (same batch), group checkpoints under `## Batch N` heading.

### 6. Failure Handling

On checkpoint failure:

1. **Attempt self-resolution** — Adjust subsequent steps, retry if possible
2. **If unresolvable** — Append Iteration to `discuss-log.md`, update `execute.md` with failure reason
   - Do NOT treat as "failure" — treat as "iteration"
   - Do NOT force spawn Dependon — unless truly needed
3. **Continue execution** or update plan and re-execute

### 7. Termination States

| Final State | Condition |
|-------------|-----------|
| `Completed` | All steps + all checkpoints verified |
| `Failed` | Checkpoint failed, cannot continue |
| `Pending` | Blocked by Dependon, can resume |

### 8. Document

Write to `.planning/<task-name>/execute.md` using template from `.planning/templates/execute.md`.

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

- Execute output is determined by Goal Clarification — do not assume the output must be investigation results, implementation, or any specific type of work
- Input is solely the plan output — no other sources consulted
- Uses templates from `.planning/templates/execute.md`
- Checkpoint failures use same protocol as Plan blocking issues
- **If uncertain about task boundaries or goal alignment at any point, stop and ask the user**
