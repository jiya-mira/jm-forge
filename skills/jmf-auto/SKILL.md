---
name: jmf-auto
description: Automatically advance a task to its next logical state. Reads current state and proceeds accordingly.
---

# Skill: jmf-auto

## Purpose

Automatically advance a task based on its current state. Acts as a convenience wrapper that determines the next phase and executes it.

## Usage

```
$jmf-auto <task-id>
```

Example:

```
$jmf-auto 3
```

## Input

- `task-id`: The numeric ID of the task

## State Machine

| Current State | Action |
|---------------|--------|
| `New` | Start Discuss phase → `Discussing` |
| `Discussing` | Complete Discuss → `Planning` |
| `Planning` | Complete Plan → `Pending` |
| `Pending` | Start Execute → `Active` |
| `Active` | Continue Execute → `Completed`/`Failed`/`Pending` |
| `Completed` | Report "already completed" |
| `Failed` | Report "failed, needs attention" |
| `Abandoned` | Report "abandoned, cannot auto-advance" |

## Behavior

### 1. Read Current State
1. Read `.workspace/tasks/INDEX.md` to get current state
2. Determine appropriate next action

### 2. Auto-Execute

- **New → Discussing**: Invoke jmf-discuss internally
- **Discussing → Planning**: Complete discuss, update state
- **Planning → Pending**: Complete plan, update state
- **Pending → Active**: Invoke jmf-execute internally
- **Active → Completed/Failed/Pending**: Continue execution, update state

### 3. Stop Conditions

Auto stops when:
- A phase requires user input (structured prompting waiting for response)
- A checkpoint fails and needs user decision
- Task reaches Completed, Failed, or Abandoned
- User says "stop"

### 4. Progress Reporting

After each state transition, report with **Task #\<id\>**: **\<task-name\>** prominently displayed:
- Previous state → New state
- What action was taken
- Current position (e.g., "[Task #24] Discussing → Planning — Discuss complete. Ready for Plan.")

## Interaction Modes

When the task needs user input during auto-execution, include **Task #\<id\>**: **\<task-name\>** in the prompt:
- Present the question with structured options
- Wait for user response

Example: "[Task #24] Stopped — Awaiting your input on blocking issue."
- Continue after response

## Notes

- This is a convenience wrapper. For fine-grained control, use individual phase skills directly.
- Does not handle Dependon blocking — if task is blocked, reports the blockage and suggests resolving the dependency first.
