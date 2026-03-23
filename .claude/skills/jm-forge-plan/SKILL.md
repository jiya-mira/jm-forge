---
name: jm-forge-plan
description: Conduct the Plan phase for a task. Create step decomposition and checkpoints.
---

# Skill: jm-forge-plan

## Purpose

Conduct the Plan phase for a task. Create an executable plan based on Discuss output.

## Usage

```
$jm-forge:plan <task-id>
```

Example:

```
$jm-forge:plan 3
```

## Input

- `task-id`: The numeric ID of the task

## Pre-conditions

- Task must exist in `.planning/TASK-REGISTRY.md`
- Task state must be `Planning` or previously `Discussing`
- Discuss phase must be complete (all open issues non-blocking)

## Behavior

### 1. Setup
1. Read TASK-REGISTRY.md, confirm task exists
2. Read Discuss output from `.planning/<task-name>/discuss.md`
3. Confirm all open issues are non-blocking before proceeding

### 2. Conduct Plan Phase

Create the plan based on Discuss output:

**Plan elements:**
1. **Step decomposition** — Ordered sequence of actions
2. **Dependencies** — Ordering constraints between steps
3. **Checkpoints** — Per-step verification criteria
4. **Tracking** — Assumptions and risks

**Format:** Present steps with clear headings, checkpoints, and proposed recommendation.

### 3. Blocking Issues During Planning

If a previously unknown blocking issue is encountered:

1. **Attempt self-resolution** — If resolvable with objectively verifiable new knowledge, resolve and continue
2. **If unresolvable** — Spawn a new task, mark current as `Dependon <new-task-id>`, pause planning

### 4. Document

Write to `.planning/<task-name>/plan.md` using template from `.planning/templates/plan.md`.

### 5. Completion

When plan is complete:
- Update TASK-REGISTRY.md state to `Pending`
- Present plan summary to user
- Offer to proceed to Execute phase

## Exit Points

User can pause planning at any time. Task state remains `Planning` and can be resumed later.

## Notes

- Plan output is the sole input to Execute — no other sources consulted
- Uses templates from `.planning/templates/plan.md`
- Dependencies use plain integers: `Dependon 3`
