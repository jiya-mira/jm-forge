# Execute — skill-naming-overhaul

**Date:** 2026-03-23
**Source:** plan.md

---

## Checkpoint Log

**[Checkpoint 1: naming-convention-updated]**
Status: ✅ Verified
Evidence: `skill-naming-convention.md` updated with new "Task Workflow Skills (jm-forge:*)" section documenting `jm-forge:<action>` pattern. Note added about Claude Code `name` field character restriction.

**[Checkpoint 2: skill-directories-renamed]**
Status: ✅ Verified
Evidence: All 8 `.claude/skills/jm-forge-task-*` directories renamed to `jm-forge-*` using sed replacement pattern `-task-` → `-`. Each SKILL.md `name` field updated from `jm-forge-task-X` to `jm-forge-X`. Usage examples updated from `$jm-forge-task-X` to `$jm-forge:X`. Cross-references in jm-forge-auto updated.

**[Checkpoint 3: skill-docs-updated]**
Status: ✅ Verified
Evidence: AGENTS.md Workflow Skills table updated to show new names `jm-forge:new` through `jm-forge:abandon`. jm-forge-auto internal skill references updated.

**[Checkpoint 4: invocation-documented]**
Status: ✅ Verified
Evidence: skill-naming-convention.md contains note: "The `name` field in SKILL.md controls the slash command on each agent. Some agents (e.g. Claude Code) restrict `name` to lowercase/hyphens only. In that case, use `jm-forge-<action>` as the `name` field and document `jm-forge:<action>` as the brand/invocation name."

**[Checkpoint 5: registry-updated]**
Status: ✅ Verified
Evidence: TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） Task 3 notes updated from "jm-forge-task-*" to "jm-forge:new, :discuss, :plan, :execute, :abandon, :list, :status, :auto".

---

## Acceptance Report

All acceptance criteria from discuss.md met:
1. ✅ New naming is significantly shorter than `jm-forge-task-*` — `jm-forge:new` (10 chars) vs `jm-forge-task-new` (18 chars)
2. ✅ Brand (`jm`) is retained in the name
3. ✅ Ergonomic to type — removed redundant `task-` middle infix
4. ⚠️ `:` compatibility is documented as a known risk — user will test empirically with Gemini/Codex; Claude Code may require fallback to hyphen

## Known Issue

Claude Code skill `name` field restricts to `lowercase letters, numbers, hyphens only`. The `:` character may not be valid in the `name` field on Claude Code. Current implementation uses `name: jm-forge-new` (hyphen) for Claude Code compatibility, with `jm-forge:new` as the brand/invocation name documented in convention. User to verify with Gemini/Codex first.
