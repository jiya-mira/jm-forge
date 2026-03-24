---
name: jm-forge:discuss
description: Conduct the Discuss phase for a task. Define goal, boundary, assumptions, and acceptance criteria.
---

# Skill: jm-forge-discuss

## Purpose

Conduct the Discuss phase for a task. This defines the task before planning begins.

## Core Principles

### Goal Clarification is Upstream

Discuss phase is primarily about understanding **what we are trying to achieve**. The output of Discuss — the Goal — determines what Plan and Execute will contain.

### Goal Clarification is Dynamic

The goal may evolve during discuss/plan/execute. This is **normal**, not a planning failure. If the goal changes, record it and confirm with the user before proceeding.

### Split Detection: Uncertainty Questioning Principle

- Do not use hardcoded trigger conditions
- When the Agent feels uncertain about whether something belongs to this task or should be a separate task, stop and ask the user
- **Agent's responsibility: feels uncertain → stop and ask**

## Usage

```
$jm-forge:discuss <task-id>
```

Example:

```
$jm-forge:discuss 3
```

## Input

- `task-id`: The numeric ID of the task

## Pre-conditions

- Task must exist in `.planning/TASK-REGISTRY.md`
- Task state must be `New`, `Discussing`, or manually set to `Discussing`

## Behavior

### 1. Setup
1. Read `PROJECT-MAP/SUMMARY.md` (and relevant JSON files on demand) to understand project context
2. **Check freshness**: If `PROJECT-MAP/project.json.lastUpdated` is older than 7 days, OR any node references a non-existent path: prompt "PROJECT-MAP may be stale. Run `jm-forge:sync` to update?"
3. Read TASK-REGISTRY.md, confirm task exists
4. Set task state to `Discussing`
5. Read existing discuss.md and discuss-log.md if they exist (resume scenario)
6. If this is a fresh start, create the task directory structure

### 2. Conduct Discuss Phase

**Interaction mode declaration:**
> "Mode: mandatory_response. I'll present choices and wait for your input before proceeding."

**Iteration 0: Goal Clarification** (must be first)

Before analyzing the problem itself, first confirm the goal:

1. **Original Feedback**: Record the raw user input exactly as provided
2. **Clarifying Questions**:
   - What is the goal of this task?
   - What does success look like?
   - Any constraints or priorities?
3. **User Response**: Wait for user input before proceeding

**Subsequent Iterations**: After Goal Clarification is confirmed, proceed with structured analysis:

1. **Goal** — What are we trying to achieve? (Should align with Iteration 0)
2. **Boundary** — What's in scope vs out of scope?
3. **Assumptions** — What are we taking as given?
4. **Acceptance Criteria** — How do we know when we're done?
5. **Open Issues** — Identify any blocking/non-blocking issues

**Termination condition:** All open issues are classified as non-blocking.

### 3. Split Detection During Discuss

At any point during discuss, if the Agent feels uncertain whether:
- Two reported issues are actually the same problem or different problems
- The current task should be split into multiple tasks
- This task should be merged with another

The Agent should:
1. Append a Split Detection iteration to `discuss-log.md`
2. Present options to the user:
   - Option A: Continue in current task
   - Option B: Split out and create new task(s)
   - Option C: Other
3. Wait for user confirmation before proceeding

### 4. Goal Evolution

If during discuss the Agent realizes the goal has evolved from what was recorded in Iteration 0:
1. Record the new goal
2. Present it to the user for confirmation
3. Do not proceed with planning until the goal is confirmed

### 5. Document

After each key decision, write to `.planning/<task-name>/discuss.md` and append to `discuss-log.md`.

**Source references:** Only on key conclusions (Conclusion, Key Decisions, resolved Open Issues).

### 6. Completion

When all open issues are non-blocking:
- Update TASK-REGISTRY.md state to `Planning`
- Present summary to user
- Offer to proceed to Plan phase

## Exit Points

User can abandon the discuss at any time by saying "stop" or "pause". Task state remains `Discussing` and can be resumed later.

## Iteration Norms

### Append-Only Documents

- Documents only append, never overwrite
- `discuss-log.md` records each iteration's input, decisions, and conclusions
- Each iteration has a clear Iteration N
- History is always preserved

### Soft Phase Boundaries

- Phases (Discuss/Plan/Execute) are **guidelines**, not **hard walls**
- Permitted to discover issues at any phase and iterate
- No forced backtracking, but backtracking is allowed
- Document recording is more important than state transitions

### Iteration Recording Format

**Goal Clarification iteration:**
```markdown
## Iteration 0 - Goal Clarification

**Date:** YYYY-MM-DD

### Original Feedback
(Raw user input, preserved exactly)

### Clarifying Questions
1. What is the goal of this task?
2. What does success look like?
3. Any constraints or priorities?

### User Response
**Waiting for user input...**
```

**Standard iteration:**
```markdown
## Iteration N

**Date:** YYYY-MM-DD
**Input:** ...
**Summary:** ...
**Conclusion:** ...
```

**Split Detection iteration:**
```markdown
## Iteration N - Split Detection

**Date:** YYYY-MM-DD

### Uncertainty Point
(What the Agent is uncertain about)

### Suggested Actions
- Option A: Continue in current task
- Option B: Split out and create new task(s)
- Option C: Other

**Waiting for user confirmation...**
```

## Notes

- Uses templates from `.planning/templates/discuss.md`
- Agent leads with structured prompting; user assists via choices
- User controls iteration — unlimited rounds before crossing to Plan
- **Goal Clarification is the mandatory first iteration** — do not skip to problem analysis before confirming the goal
