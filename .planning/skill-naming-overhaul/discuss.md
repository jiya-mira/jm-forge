# Discuss — skill-naming-overhaul

**Date:** 2026-03-23
**Status:** Concluded
**Task ID:** 7

---

## Goal

Redesign skill naming convention to be ergonomic across multiple AI agents (Claude Code, Gemini, Codex, etc.) while retaining brand identity.

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** Skill invocation names, directory naming, skill-naming-convention.md updates, existing skill renaming
- **Out of scope:** Skill implementation code, workflow framework changes

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. `jm` is the brand (not just a project initial)
2. `forge` is the project/tool name
3. Primary use case: user manually invokes skills across different agents

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. New naming is significantly shorter than `jm-forge-task-*` (e.g. `jm-forge:new` vs `jm-forge-task-new`)
2. Brand (`jm`) is retained in the name
3. Ergonomic to type across different agent CLIs
4. No special characters that break compatibility across mainstream agents

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | Claude Code skill `name` field only allows lowercase, numbers, hyphens — `:` may be invalid | No | User will test empirically with Gemini/Codex first; will revisit Claude Code if needed |

*(Resolved issues: none)*

---

## Key Decisions

### Naming Format: `jm-forge:<action>`

- **Brand:** `jm` (保留品牌缩写)
- **Project:** `forge` (工具名)
- **Separator:** `:` (命名空间风格)
- **Action:** e.g. `new`, `discuss`, `plan`, `execute`, `status`, `abandon`, `list`, `auto`

**Source:** discuss-log.md → Iteration 1

---

## Conclusion

确定命名格式为 **`jm-forge:<action>`**，例如：
- `jm-forge:new`
- `jm-forge:discuss`
- `jm-forge:plan`
- `jm-forge:execute`
- `jm-forge:status`
- `jm-forge:abandon`
- `jm-forge:list`
- `jm-forge:auto`

相比 `jm-forge-task-new` 减少 5 个字符，去掉了冗余的 `task-` 中缀。

注意风险：Claude Code 的 skill `name` 字段只允许 lowercase letters/numbers/hyphens，`:` 可能不兼容。用户将先在 Gemini/Codex 上验证，之后再处理 Claude Code 兼容性问题。

Ready for Plan.

**Source:** discuss-log.md → Iteration 1
