---
name: jmf-exp
description: Build project-level EXP records from real task artifacts. Writes to .workspace/exp-map with index + one-entry-per-file format.
---

# Skill: jmf-exp

## Purpose

Extract reusable experience at project scope, not only from the latest task, and persist it in a stable artifact structure.

## Usage

```
$jmf-exp <task-id-or-topic>
```

Example:

```
$jmf-exp 25
$jmf-exp parser-timezone-pattern
```

## Input

- `task-id-or-topic`: Optional anchor for selection; extraction is project-level and may include multiple tasks

## Pre-conditions

- Task must exist in `.workspace/tasks/INDEX.md`
- Project must contain concrete attempt artifacts, such as `summary.md`, `discuss-log.md`, `plan.md`, `execute.md`, or other task outputs
- The exp must be derived from a real attempt, not from external retrieval alone

## Behavior

### 1. Gather context
1. Read `.workspace/project-map/SUMMARY.md` if project context is needed.
2. Read candidate artifacts from `.workspace/tasks/*/` at project scope.
3. Prefer `summary.md` when present; if missing, fallback to `discuss-log.md`, `plan.md`, `execute.md`.
4. Derive evidence from two allowed source classes:
   - Type `A`: independent experience that stands on its own.
   - Type `B`: common pattern abstracted from at least 2 tasks.

### 2. Ensure Artifact Contract

`jmf-exp` must persist output under:

- `.workspace/exp-map/INDEX.md` (summary list and routing)
- `.workspace/exp-map/entries/` (one exp per file)

If missing, create them before writing any exp entry.

### 3. Write Single EXP Entry

Every generated exp must be one Markdown file in `.workspace/exp-map/entries/` using required fields:

- `id`
- `title`
- `type` (`A` or `B`)
- `statement`
- `applicability`
- `evidence`
- `counter_example`
- `status`

Optional fields can be added as needed:

- `do`
- `dont`
- `verification`
- `notes`

### 4. ID and routing rules

Use deterministic ID:

`exp-<topic-slug>-v<ordinal>`

- `topic-slug` must be kebab-case.
- `ordinal` starts from `01`.
- Entry file path: `.workspace/exp-map/entries/<id>.md`.
- `.workspace/exp-map/INDEX.md` must include row with ID, type, status, evidence scope, and file path.

### 5. Validation rules

- `status` defaults to `pending`.
- Promote to `verified` when positive evidence is clear.
- Promote to `strong` when cross-task evidence is stable and no unresolved counter-example remains.
- Failed or conflicting evidence must be recorded in `counter_example`.

### 5. Hard constraints

- Do not convert RAG output, generic web knowledge, or pretraining facts directly into exp
- Do not output only console text without persistence into `.workspace/exp-map`
- Do not require automatic background generation
- Do not require all tasks to have `summary.md`; historical missing summary is allowed via fallback artifacts

## Markdown Template

```md
---
id: exp-parser-boundary-v01
title: Parser boundary check before fix
type: B
statement: When parser anomalies appear, validate boundary assumptions before changing logic.
applicability:
  - parser
  - data-normalization
evidence:
  tasks:
    - 21
    - 27
counter_example:
  - Task 30: issue was caused by environment corruption, not parser boundary.
status: pending
---

# EXP — Parser boundary check before fix

## Evidence

- `.workspace/tasks/021-bootstrap-iteration-optimization/summary.md`
- `.workspace/tasks/027-jmf-exp-racobit-analysis-issues/discuss-log.md`

## Notes

Optional details.

## Do

Optional.

## Dont

Optional.

## Verification

Optional.
```

## INDEX row example

```md
| exp-parser-boundary-v01 | Parser boundary check before fix | B | pending | tasks:21,27 | entries/exp-parser-boundary-v01.md | 2026-03-26 |
```

## Notes

- This skill is manually triggered
- `summary.md` is preferred evidence for new tasks, but not mandatory for historical tasks
