---
name: workflow-execute
description: Execute tasks following the Discuss → Plan → Execute workflow. Use when starting any new task.
---

# Skill: workflow-execute

## Purpose

Execute tasks following the Discuss → Plan → Execute (D→P→E) workflow. This skill ensures every task is well-defined before planning, and planned before execution.

## Interaction Modes

At the start of Discuss phase, Agent should declare and confirm the interaction mode:

- **mandatory_response** (default): User must respond before proceeding. Agent presents structured choices and waits.
- **agent_self_decide** (optional): Agent may proceed with its own recommendation if user does not respond within a reasonable time. Use this when speed is prioritized.

If not explicitly stated by user, default to **mandatory_response**.

## Structured Prompting Rules (All Phases)

When presenting choices to the user:

1. **Single-choice first**: Prefer single-choice questions (2 or 3 options) over open-ended ones
2. **Recommended first**: Place the recommended option as the first choice
3. **Always include "Other/Custom"**: Provide an escape hatch for user-defined input
4. **Present Agent's recommendation with reasoning**: When asking user to choose, state what Agent suggests and why

Example format:
```
Which approach do you prefer?
  1. [Recommended] Option A — because X (Agent suggests this)
  2. Option B — because Y
  3. Other/Custom — specify your own
```

## The Three Phases

### Phase 1: Discuss

**Objective:** Define the task before planning begins.

**Interaction mode declaration:** At the start, Agent states the mode being used (default: mandatory_response).

**Termination condition:** All open issues are classified as non-blocking.

**Output (converges into Plan):**
1. **Goal** — What we are trying to achieve
2. **Boundary** — In-scope vs out-of-scope
3. **Assumptions** — Premises taken as given
4. **Acceptance criteria** — How to determine "done"
5. **Open issues** — Non-blocking issues carried forward

**Decision authority:**
- Agent leads: identifies issues, classifies blocking/non-blocking, proposes structured options with recommendations
- User assists: selects from structured choices (or provides custom input via "Other/Custom")
- User decides when to move on (iteration is unlimited before crossing the phase boundary)

**Crossing to Plan:** Enter Plan iff `∀ open_issue: open_issue.blocking == false`

---

### Phase 2: Plan

**Input:** Discuss output (consumed — Discuss artifacts do not independently survive into Execute)

**Objective:** Create an executable plan based on the Discuss output.

**Structured presentation:** When presenting the plan to user:
- Present steps with clear headings
- State checkpoints and what constitutes verification
- Identify potential risks/assumptions
- Propose a recommendation for the overall plan approach

**Output:**
1. **Step decomposition** — Ordered sequence of actions
2. **Dependencies** — Ordering constraints between steps
3. **Checkpoints** — Per-step verification criteria
4. **Tracking** — Assumptions and risks

**New blocking issues during planning:**
- Attempt self-resolution first (with objectively verifiable basis)
- If unresolvable: spawn a new task, mark current task as `Dependon <task-id>`
- If extremely hard-blocking: may abort, same Dependon protocol

**Presentation format for blocking issues:**
```
[Blocking Issue Detected]
Issue: <description>
Agent's assessment: <why it blocks>
Options:
  1. [Recommended] Attempt self-resolution — because <reason>
  2. Spawn new task — creates Dependon relationship
  3. Other/Custom — <user's alternative>
```

**Crossing to Execute:** Plan output is complete and ready for execution.

---

### Phase 3: Execute

**Input:** Plan output (sole source — no other input is consulted)

**Objective:** Execute the plan and verify completion.

**Structured checkpoint reporting:** After each checkpoint:
```
[Checkpoint N: <name>]
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>
```

**Parallel steps:** When steps execute in parallel, group their checkpoints under a `## Batch N` heading. Steps in the same batch are verified simultaneously.

**Format: Minimal (default)**
- Use ✅/❌ for pass/fail status
- Evidence field: describe what was observed (required on failure, optional on success)
- Timestamp: optional — Agent adds if contextually useful
- Additional diagnostic fields: optional — Agent adds on failure as needed

**Termination condition:** All steps completed AND all checkpoints verified.

**Output:**
- Execution results (structured checkpoint log)
- Acceptance report

**Checkpoint failures:**
- Attempt self-resolution (adjust steps, retry)
- If unresolvable: spawn new task, mark current as `Dependon <task-id>`

---

## Task Relationship: Dependon

When Task A cannot proceed until Task B completes, Task A is marked `Dependon <task-id>` (e.g., `Dependon 3`).

- Transitive in chained scenarios (A Dependon B, B Dependon C → A effectively Dependon C)
- Primarily relevant in human-operated task flows

---

## Task Lifecycle & Registry

### Task Registry

All tasks are tracked in `.planning/TASK-REGISTRY.md` with:
- Unique ID (plain integer, e.g., `1`, `2`, `3`)
- Current state
- Dependon relationship
- Optional notes

### Task States

| State | Set By | Description |
|-------|--------|-------------|
| New | Agent (auto) | User proposed idea; Discuss not started |
| Discussing | Agent (auto) | In Discuss phase |
| Planning | Agent (auto) | In Plan phase |
| Pending | Agent (auto) | Plan complete; waiting to execute |
| Active | Agent (auto) | In Execute phase |
| Completed | Agent (auto) | Execute finished successfully |
| Failed | Agent (auto) | Execute failed |
| Abandoned | **User (manual)** | Explicitly abandoned; any state |

### Lifecycle Flow

```
New → Discussing → Planning → Pending → Active → Completed
                                        ↘ Failed
                          ↘ Abandoned (user手动)
    ↘ (any state) → Abandoned (user手动)
```

### Creating New Tasks

When user proposes a new task:
1. Add row to TASK-REGISTRY.md with next available ID
2. Create `.planning/<task-name>/` directory
3. State = New
4. Set Dependon if applicable

### State Transitions

Agent updates state automatically on phase entry/exit. **Abandoned is set by user only.**

---

## Immediate Documentation Principle

Key conclusions reached during discussion should be written to `.planning/<task-name>/` **as they happen**, not only at the end of the session.

This ensures:
- Session interruption does not lose progress
- New agents can restore context by reading `.planning/`
- Documents are the single source of truth (agent memory is a cache)

**Format for live documentation:**
```
.planning/<task-name>/
├── discuss.md        ← Latest consensus with discuss-log.md references
├── discuss-log.md    ← Append-only iteration log (full history)
├── plan.md           ← Steps, Dependencies, Checkpoints, Tracking
└── execute.md        ← Checkpoint log, Acceptance report
```

**Template files:** See `.planning/templates/` for ready-to-copy templates:
- `discuss.md`
- `discuss-log.md`
- `plan.md`
- `execute.md`

**discuss.md format — Source reference on key conclusions only:**
- Include `**Source:** discuss-log.md → Iteration N` on:
  - Final Conclusion section
  - Key Decisions (major conclusions)
  - Resolved Open Issues
- Do NOT include Source on: Goal, Boundary, Assumptions, Acceptance Criteria, or Open Issues (until resolved)

```markdown
## Conclusion: <title>

<content>

**Source:** discuss-log.md → Iteration N
```

**discuss-log.md format:**
```markdown
## Iteration N — <YYYY-MM-DD>

**Trigger:** <what prompted this iteration>
**Topic:** <what was discussed>
**Agent recommendation:** <what Agent suggested>
**User decision:** <what user chose>
**Conclusion:**
- <key point 1>
- <key point 2>
```

**User self-consistency tracker:** discuss-log.md also serves as an externalized trace for detecting contradictions. When a current statement conflicts with history, Agent should proactively surface it:
```
Contradiction detected:
  - Iteration 1: "A is important"
  - Iteration 3: "A is not important"
Please clarify: did you change your mind, or was the earlier statement inaccurate?
```

## Document Reference Convention

Documents reference their sources to enable navigation. This allows any Agent to find key information starting from entry points.

**Entry Points:**
- `.planning/TASK-REGISTRY.md` — Lists all tasks and their states
- `AGENTS.md` — Agent behavior guidelines and workflow overview

**Reference Chain:**

| Document | References | Meaning |
|----------|-----------|---------|
| `discuss.md` | `discuss-log.md` | Decisions traced back to iterations |
| `plan.md` | `discuss.md` | Source: discuss output (consumed) |
| `execute.md` | `plan.md` | Source: plan.md |
| `discuss-log.md` | `discuss.md` | Iterations trace discussions |

**Reference Format:**
```markdown
**Source:** <document-name> → <reference>
```

**Navigation Rule:** To find the origin of any decision, follow the references backward. Entry points have no references.

## Notes

- Iteration within a phase is user-controlled — user decides when to move forward
- Crossing a phase boundary is one-way — do not backtrack to a previous phase
- Open issues that are blocking must be resolved or delegated before crossing to the next phase
- Always use structured prompting with recommendation + "Other/Custom" option
