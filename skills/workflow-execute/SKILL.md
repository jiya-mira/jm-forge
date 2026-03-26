---
name: workflow-execute
description: Thin bootstrap/router skill for the D→P→E workflow. Use when you need a minimal entry that delegates to jmf-* workflow skills.
---

# Skill: workflow-execute

## Purpose

Provide a thin, explicit router for D→P→E workflow entry. This skill does not reimplement workflow phases. It delegates to:

- `jmf-new`
- `jmf-discuss`
- `jmf-plan`
- `jmf-execute`
- `jmf-auto`
- `jmf-list`
- `jmf-status`
- `jmf-abandon`

## Behavior

1. If the user wants to create a task, route to `jmf-new`.
2. If the user wants to define scope, route to `jmf-discuss`.
3. If the user wants a plan, route to `jmf-plan`.
4. If the user wants to execute, route to `jmf-execute`.
5. If the user wants list/status/abandon/auto, route to the matching `jmf-*` skill.
6. Keep this skill thin; do not duplicate phase logic or policy.

## Notes

- This is the only retained non-`jmf-*` runtime/router entry.
- All substantive workflow behavior belongs to the `jmf-*` skills.
- Treat this skill as a router, not as the primary workflow implementation.
