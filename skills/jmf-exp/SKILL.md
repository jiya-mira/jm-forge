---
name: jmf-exp
description: Extract a structured experience record from real task attempts and task artifacts. Produces a Markdown exp draft only from observed attempts.
---

# Skill: jmf-exp

## Purpose

Turn one real attempt, or a small set of related attempts, into a reusable experience record for later task reuse.

## Usage

```
$jmf-exp <task-id>
```

Example:

```
$jmf-exp 25
```

## Input

- `task-id`: The numeric ID of the task that produced the attempt artifacts

## Pre-conditions

- Task must exist in `.planning/TASK-REGISTRY.md`
- Task must have at least one concrete attempt artifact, such as `discuss-log.md`, `plan.md`, `execute.md`, or other task output
- The exp must be derived from a real attempt, not from external retrieval alone

## Behavior

### 1. Gather context
1. Read `PROJECT-MAP/SUMMARY.md` if project context is needed
2. Read the task artifacts from `.planning/<task-name>/`
3. Identify the clearest successful or partially successful attempt as the source for the exp draft

### 2. Draft the exp

Emit a Markdown exp draft with these required fields:

- `id`
- `status`
- `task_id`
- `task_name`
- `scene_tags`
- `attempt_sources`
- `attempt_summary`
- `root_cause`
- `resolution`
- `lesson`
- `provenance`
- `validation_notes`

### 3. ID rules

Use a deterministic exp ID:

`exp-<task-id>-<scene-slug>-a<ordinal>`

- `scene-slug` must be normalized to kebab-case
- `ordinal` starts at `01` and increases when multiple exp drafts are produced for the same scene

### 4. Validation rules

- If the evidence is sufficient, mark the draft as `verified` or `strong`
- If evidence is incomplete, mark the draft as `pending-verification`
- If successful and failed attempts both exist, prefer the most recent successful attempt as the primary source and record failed attempts in provenance
- Final downgrade or regrading decisions happen in batch review, not during drafting

### 5. Hard constraints

- Do not convert RAG output, generic web knowledge, or pretraining facts directly into exp
- Do not introduce a separate v1 index file
- Do not require automatic background generation
- Do not write hidden state outside the Markdown draft unless the user explicitly requests persistence

## Markdown Template

```md
---
id: exp-25-task-sample-a01
status: pending-verification
task_id: 25
task_name: exp-system
scene_tags:
  - example
  - workflow
---

# Exp — Short Title

## Scenario
Brief description of the situation.

## Attempt Sources
- `.planning/exp-system/discuss-log.md`

## Attempt Summary
What was tried and what happened.

## Root Cause
Why the situation needed this exp.

## Resolution
What worked or what was decided.

## Lesson
The reusable rule or pattern.

## Provenance
- Positive evidence: ...
- Negative evidence: ...

## Validation Notes
- What confirms this exp
- What remains uncertain
```

## Notes

- Markdown is the only v1 storage format
- This skill is manually triggered
- The v1 scope is draft generation, not automatic indexing or background ingestion
