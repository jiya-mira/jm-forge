# discuss.md

**Source:** discuss-log.md

---

## Goal

规范化jm-forge技能命名规则，所有技能统一使用 `jm-forge:<action>` (冒号) 格式。

## Boundary

### In Scope
- 更新 `.claude/skills/` 下所有 SKILL.md 的 `name` 字段为 `jm-forge:<action>` 格式
- 更新 bootstrap 和 skill-scaffold 技能中的旧命名引用
- 更新 TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） Task 3 中的描述
- `.gemini/skills/` 通过符号链接自动同步，无需单独修改

### Out of Scope
- `.planning/` 目录下的历史文档（记录历史，不修改）
- `skills/` 目录（canonical source 在 `.claude/skills/`，保持同步）

## Assumptions

1. `name` 字段支持冒号格式 (`jm-forge:new`)
2. 符号链接保持 `.gemini/skills/` 与 `.claude/skills/` 同步
3. 用户通过 `/jm-forge:new` 调用技能

## Acceptance Criteria

1. 所有 SKILL.md 的 `name` 字段使用 `jm-forge:<action>` 格式
2. Bootstrap 和 skill-scaffold 中无 `jm-forge-task-*` 旧命名
3. TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） Task 3 描述使用新命名
4. `.gemini/skills/` 通过符号链接自动更新

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|----------|------------|
| 1 | 命名格式 | Blocking | **Resolved**: `jm-forge:<action>` 冒号格式 |
| 2 | 历史文档处理 | Non-blocking | **Resolved**: `.planning/` 不修改，仅修改活跃文档 |

## Key Decisions

1. **Naming Format:** `jm-forge:<action>` (冒号)
2. **Scope:** 只修改活跃文档，不修改历史记录
3. **Sync:** `.gemini/skills/` 通过符号链接自动同步
