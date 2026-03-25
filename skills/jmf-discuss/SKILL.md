---
name: jmf-discuss
description: Conduct the Discuss phase for a task. Define goal, boundary, assumptions, and acceptance criteria.
---

# Skill: jmf-discuss

## Purpose

Conduct the Discuss phase for a task. This defines the task before planning begins.

## Usage

```
$jmf-discuss <task-id>
```

Example:

```
$jmf-discuss 3
```

## Input

- `task-id`: The numeric ID of the task

## Pre-conditions

- Task must exist in `.planning/TASK-REGISTRY.md`
- Task state must be `New`, `Discussing`, or manually set to `Discussing`

## Behavior

### 1. Setup
1. Read `PROJECT-MAP/SUMMARY.md` (and relevant JSON files on demand) to understand project context
2. **Check freshness**: If `PROJECT-MAP/project.json.lastUpdated` is older than 7 days, OR any node references a non-existent path: prompt "PROJECT-MAP may be stale. Run `jmf-sync` to update?"
3. Read TASK-REGISTRY.md, confirm task exists
4. Set task state to `Discussing`
5. Read existing discuss.md and discuss-log.md if they exist (resume scenario)
6. If this is a fresh start, create the task directory structure

### 2. Conduct Discuss Phase

Use structured prompting with these elements:

**Interaction mode declaration:**
> "Mode: mandatory_response. I'll present choices and wait for your input before proceeding."

**Discuss elements (in order):**
1. **Goal** — What are we trying to achieve?
2. **Boundary** — What's in scope vs out of scope?
3. **Assumptions** — What are we taking as given?
4. **Acceptance Criteria** — How do we know when we're done?
5. **Open Issues** — Identify any blocking/non-blocking issues

**Termination condition:** All open issues are classified as non-blocking.

### 3. Document

After each key decision, write to `.planning/<task-name>/discuss.md` and append to `discuss-log.md`.

**Template for `discuss.md`:**

```markdown
---
id: <task-id>
---

# Discuss — <task-name>

**Date:** <YYYY-MM-DD>
**Status:** Concluded / In progress

---

## Goal

<What we are trying to achieve>

**Source:** discuss-log.md → Iteration N

---

## Boundary

- **In scope:** <items>
- **Out of scope:** <items>

**Source:** discuss-log.md → Iteration N

---

## Assumptions

1. <assumption 1>
2. <assumption 2>

**Source:** discuss-log.md → Iteration N

---

## Acceptance Criteria

1. <criterion 1>
2. <criterion 2>

**Source:** discuss-log.md → Iteration N

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | <issue> | Yes/No | <notes> |

*(Resolved issues: include Source reference)*

---

## Key Decisions

### <Decision Title>
<Description>

*(Key decisions only — include Source reference)*

---

## Conclusion

<Summary and recommendation>

**Source:** discuss-log.md → Iteration N
```

**Source references:** Only on key conclusions (Conclusion, Key Decisions, resolved Open Issues).

### 4. Completion

When all open issues are non-blocking:
- Update TASK-REGISTRY.md state to `Planning`
- Present summary to user with **Task #\<id\>**: **\<task-name\>** prominently displayed
- Offer to proceed to Plan phase

Example: "**Task #24: manual-mode-prompt-ux** — Discuss complete. Ready for Plan."

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

When iterating, append to `discuss-log.md`:

```markdown
## Iteration N — YYYY-MM-DD

**Trigger:** <what prompted this iteration>

**Topic:** <what was discussed>

**Agent recommendation:** <what Agent suggested>

**User decision:** <what user chose>

**Conclusion:**
- <key point 1>
- <key point 2>
```

## Notes

- Agent leads with structured prompting; user assists via choices
- User controls iteration — unlimited rounds before crossing to Plan

