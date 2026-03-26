# Discuss — workflow-framework

**Date:** 2026-03-22
**Status:** Concluded

---

**Source:** discuss-log.md

## Goal

Build a general-purpose skill development framework that:
- Any project can adopt by copying the `.claude/skills/` structure
- Uses a theoretically-grounded task execution workflow (not purely empirical)
- Is maintained by a single owner (ryan) for the foreseeable future

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** Framework structure, workflow phases (Discuss/Plan/Execute), skill naming conventions, interaction protocols
- **Out of scope:** Specific skills beyond bootstrap/framework itself, multi-user collaboration, CI/CD

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. Theoretical foundation should guide framework design, not copy existing conventions
2. A task unit is the atomic workflow element
3. A single-agent context (one user, one agent) for now

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. Framework documented in `.planning/workflow-framework.md`
2. At least one working skill (`workflow-execute`) that implements the framework
3. Naming convention documented in `.planning/skill-naming-convention.md`
4. Framework used to build at least one real skill with real task

**Source:** discuss-log.md → Iteration 1

---

## Key Decisions

### Task Unit Definition

Four boundary conditions (all required):
1. **Explicit起点** — A clear trigger/entry point exists
2. **Explicit终点** — A clear completion/closure point exists
3. **Independently verifiable** — An external observer can determine completion
4. **Recursively decomposable** — Decomposition stops when a subtask satisfies condition 3

**Source:** discuss-log.md → Iteration 1

---

### Discuss Phase

- **Termination:** all open issues non-blocking
- **Decision:** Agent leads, user assists via structured prompts, user controls iteration
- **Crossing to Plan:** Enter iff `∀ open_issue: open_issue.blocking == false`

**Source:** discuss-log.md → Iteration 1

---

### Plan Phase

- **Input:** Discuss output (consumed)
- **New blocking issues:** self-resolve → spawn new task with Dependon → abort
- **No backtracking** to Discuss once Plan starts

**Source:** discuss-log.md → Iteration 1

---

### Execute Phase

- **Termination:** all steps completed AND all checkpoints verified
- **Checkpoint failures:** same protocol as Plan blocking issues

**Source:** discuss-log.md → Iteration 1

---

### Interaction Modes

- **mandatory_response** (default): user must respond before proceeding
- **agent_self_decide** (optional): agent proceeds if user silent

**Source:** discuss-log.md → Iteration 1

---

### Structured Prompting

- Single-choice first (2 or 3 options)
- Recommended option first
- Always include "Other/Custom"
- State recommendation + reasoning

**Source:** discuss-log.md → Iteration 1

---

### Dependon Relationship

- Transitive in chained scenarios
- Primary relationship type; others emerge from practice

**Source:** discuss-log.md → Iteration 1

---

### Immediate Documentation

- Key conclusions written to `.planning/<task>/` as they happen
- Documents are source of truth; agent memory is cache
- discuss.md includes source references to discuss-log.md for traceability

**Source:** discuss-log.md → Iteration 1

---

### User Self-Consistency Tracker

discuss-log.md also serves as an externalized trace for detecting contradictions. When a current statement conflicts with history, Agent should proactively surface it.

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Resolution | Source |
|---|-------|-----------|------------|--------|
| 1 | Task unit naming ("task" vs other terms) | Non-blocking | Use "task" | discuss-log.md → Iteration 1 |
| 2 | Execute phase structure detail | Non-blocking | **Resolved (Iteration 2):** Entry/Execution/Checkpoint/Failure/Termination/Output defined in workflow-framework.md §4 | discuss-log.md → Iteration 2 |

---

## Iteration 2 — 2026-03-22

**Trigger:** User selected "Define Execute phase structure" as next step

**Topic:** Execute phase structure detail

**Agent recommendation:** Define complete Execute phase structure including Entry Criteria, Execution Model, Checkpoint Verification, Failure Handling Protocol, Termination, and Output

**User decision:** Accepted proposed structure

**Conclusion:**
- Execute phase structure now defined in workflow-framework.md §4:
  - Entry: Plan output complete
  - Execution: Sequential by default, step + checkpoint per unit
  - Checkpoint: ✅/❌ status with evidence
  - Failure: self-resolve → spawn Dependon → abort → resume
  - Termination: all steps complete + all checkpoints verified
  - Output: Checkpoint log + Acceptance report
- workflow-execute SKILL.md already aligned with this structure
| 3 | Blocking vs non-blocking classification accuracy | Non-blocking | Agent judgment primary, user guided by structured prompts | discuss-log.md → Iteration 1 |
| 4 | What constitutes "objectively verifiable new knowledge" | Non-blocking | Deferred to future practice | discuss-log.md → Iteration 1 |
| 5 | Theoretical references | Non-blocking | **Resolved (Iteration 3):** references.md created — direct influences: WBS, HTN, PDCA, GQM, V&V; acknowledged as first-principles + practical synthesis | discuss-log.md → Iteration 3 |
| 6 | Framework validation (Step 3) | Non-blocking | **Resolved (Iteration 4):** Full D→P→E cycle tested with jm-forge-bootstrap — all 4 checkpoints verified ✅ | discuss-log.md → Iteration 4 |
| 7 | Documentation structure (Step 4) | Non-blocking | **Resolved (Iteration 5):** Templates created in .planning/templates/ — discuss.md, plan.md, execute.md, discuss-log.md | discuss-log.md → Iteration 5 |
| 8 | Partial completion handling (Pending state) | Non-blocking | **Resolved (Iteration 6):** Pending state added to Execute termination; pending = user interruption, can resume | discuss-log.md → Iteration 6 |
| 9 | Task numbering mechanism | Non-blocking | **Resolved (Iteration 6):** Plain natural numbers 1, 2, 3...; in discuss.md frontmatter; used for Dependon references | discuss-log.md → Iteration 6 |
| 10 | Source reference on every section | Non-blocking | **Resolved (Iteration 7):** Source only on key conclusions — Conclusion, Key Decisions (major), resolved Open Issues; not on Goal/Boundary/Assumptions/Acceptance Criteria | discuss-log.md → Iteration 7 |
| 11 | Parallel step checkpoint reporting | Non-blocking | **Resolved (Iteration 8):** ## Batch N grouping; parallel steps in same batch verified simultaneously | discuss-log.md → Iteration 8 |
| 12 | discuss-log.md templating | Non-blocking | **Skipped:** Not a real issue; append-only format is simple enough | — |
| 13 | Task lifecycle & registry | Non-blocking | **Resolved (Iteration 9):** TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） created; 8 states defined; Abandoned is user-set only | discuss-log.md → Iteration 9 |
| 14 | Task skill granularity | Non-blocking | **Resolved (Iteration 10):** Split into jm-forge-task-* series; workflow-execute → task-auto | discuss-log.md → Iteration 10 |
