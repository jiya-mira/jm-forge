---
name: jm-forge:plan
description: Conduct the Plan phase for a task. Create step decomposition and checkpoints.
---

# Skill: jm-forge-plan

## Purpose

Conduct the Plan phase for a task. Create an executable plan based on Discuss output.

## Core Principles

### Goal Clarification is Upstream

Plan's content and structure are determined by the Goal Clarification output from Discuss. The Goal defines what this plan is trying to achieve — Plan does not assume a specific type of outcome (e.g., investigation vs. implementation).

### Goal Clarification is Dynamic

The goal may evolve during planning. This is **normal**, not a planning failure. If the goal changes, record it and confirm with the user before proceeding.

### Split Detection: Uncertainty Questioning Principle

- Do not use hardcoded trigger conditions
- When the Agent feels uncertain about task boundaries or whether issues belong to the same task, stop and ask the user
- **Agent's responsibility: feels uncertain → stop and ask**

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
4. Note the Goal Clarification output from Discuss — this defines the plan's direction

### 2. Conduct Plan Phase

Create the plan based on Discuss output and the Goal Clarification:

**Plan elements:**
1. **Goal alignment** — Confirm the plan serves the stated goal from Discuss
2. **Step decomposition** — Ordered sequence of actions to achieve the goal
3. **Dependencies** — Ordering constraints between steps
4. **Checkpoints** — Per-step verification criteria
5. **Tracking** — Assumptions and risks

**Format:** Present steps with clear headings, checkpoints, and proposed recommendation.

### 3. Goal Evolution During Planning

If during planning the Agent realizes the goal has evolved:
1. Record the new goal
2. Present it to the user for confirmation
3. Do not proceed with planning until the goal is confirmed

### 4. Split Detection During Planning

At any point during planning, if the Agent feels uncertain whether:
- Two issues should be in the same plan or separate plans
- The current plan should be split
- This task should be merged with another

The Agent should:
1. Append a Split Detection iteration to `discuss-log.md`
2. Present options to the user:
   - Option A: Continue in current plan
   - Option B: Split out and create new task(s)
   - Option C: Other
3. Wait for user confirmation before proceeding

### 5. Blocking Issues During Planning

If a previously unknown blocking issue is encountered:

1. **Soft Boundaries approach** — Append to `discuss-log.md` with Iteration N
   - Small issues: resolve directly and document
   - Issues needing separate task: spawn new Dependon task, continue planning
2. **Do NOT force stop planning** — Continue with append-only iteration recording
3. **Self-resolution** — If resolvable with objectively verifiable new knowledge, resolve and continue

### 6. Document

Write to `.planning/<task-name>/plan.md` using template from `.planning/templates/plan.md`.

### 7. Completion

When plan is complete:
- Update TASK-REGISTRY.md state to `Pending`
- Present plan summary to user
- Offer to proceed to Execute phase

## Exit Points

User can pause planning at any time. Task state remains `Planning` and can be resumed later.

## Iteration Norms

### Soft Phase Boundaries

- Phases are **guidelines**, not **hard walls**
- When discovering new issues during planning:
  - Append to `discuss-log.md` with Iteration N
  - Resolve directly if small, spawn Dependon if needed
- Do NOT force stop — continue with append-only iteration recording

### State as Position Marker

- State reflects main work position
- Iterations do NOT force State changes
- State change = main position change, not phase transition

## Notes

- Plan output is determined by Goal Clarification — do not assume the plan must be about investigation, implementation, or any specific type of work
- Plan output is the sole input to Execute — no other sources consulted
- Uses templates from `.planning/templates/plan.md`
- Dependencies use plain integers: `Dependon 3`
- **If uncertain about task boundaries at any point, stop and ask the user**
