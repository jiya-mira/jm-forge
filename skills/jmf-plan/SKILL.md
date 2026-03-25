---
name: jmf-plan
description: Conduct the Plan phase for a task. Create step decomposition and checkpoints.
---

# Skill: jmf-plan

## Purpose

Conduct the Plan phase for a task. Create an executable plan based on Discuss output.

## Usage

```
$jmf-plan <task-id>
```

Example:

```
$jmf-plan 3
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

1. **Soft Boundaries approach** — Append to `discuss-log.md` with Iteration N
   - Small issues: resolve directly and document
   - Issues needing separate task: spawn new Dependon task, continue planning
2. **Do NOT强制 stop planning** — Continue with append-only iteration recording
3. **Self-resolution** — If resolvable with objectively verifiable new knowledge, resolve and continue

### 4. Document

Write to `.planning/<task-name>/plan.md` using the following template:

```markdown
# Plan — <task-name>

**Date:** <YYYY-MM-DD>
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: <verb-noun>

**Action:** <What to do>

**Approach:**
- <detail>
- <detail>

**Checkpoint:** `<checkpoint-name>`
- <Verification criterion>
- <Verification criterion>

---

## Dependencies

<Step ordering constraints, or "All steps are independent">

## Tracking

| Assumption | Risk |
|-----------|------|
| <assumption> | <Low/Medium/High> — <reason> |

## Execution Order

<sequential | parallel | parallel with dependencies noted>
```

### 5. Completion

When plan is complete:
- Update TASK-REGISTRY.md state to `Pending`
- Present plan summary to user with **Task #\<id\>**: **\<task-name\>** prominently displayed
- Offer to proceed to Execute phase

Example: "**Task #24: manual-mode-prompt-ux** — Plan complete. Ready for Execute."

## Exit Points

User can pause planning at any time. Task state remains `Planning` and can be resumed later.

## Iteration Norms

### Soft Phase Boundaries

- Phases are **guidelines**, not **hard walls**
- When discovering new issues during planning:
  - Append to `discuss-log.md` with Iteration N
  - Resolve directly if small, spawn Dependon if needed
- Do NOT强制 stop — continue with append-only iteration recording

### State as Position Marker

- State reflects main work position
- Iterations do NOT force State changes
- State change = main position change, not phase transition

## Notes

- Plan output is the sole input to Execute — no other sources consulted
- Dependencies use plain integers: `Dependon 3`
