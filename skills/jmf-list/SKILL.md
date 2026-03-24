---
name: jmf-list
description: List all tasks from TASK-REGISTRY.md with their IDs, states, and dependencies.
---

# Skill: jm-forge-list

## Purpose

Read `.planning/TASK-REGISTRY.md` and display all tasks in a human-readable format.

## Usage

```
/jmf-list
```

Or as a skill invocation:

```
$jmf-list
```

## Output

Displays:
- All tasks with ID, name, state, and Dependon
- Color-coded or marked states (e.g., Completed ✅, Active 🔄, Pending ⏳, etc.)
- Summary: total tasks, count by state

## Implementation

1. Read `.planning/TASK-REGISTRY.md`
2. Parse the task table
3. Display in readable format with state indicators
4. Show summary counts

## Notes

- If TASK-REGISTRY.md does not exist, report that no tasks have been created yet
- State indicators: New (🆕), Discussing (💬), Planning (📋), Pending (⏳), Active (🔄), Completed (✅), Failed (❌), Abandoned (🚫)
