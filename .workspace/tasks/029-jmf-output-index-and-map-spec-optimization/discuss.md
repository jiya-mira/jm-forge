---
id: 29
---

# Discuss — jmf-output-index-and-map-spec-optimization

**Date:** 2026-03-26
**Status:** Concluded

---

## Goal

统一 `jmf-*` 产出物索引编写规范，并优化 map 系列编写规范，以提升检索效率、一致性和可维护性。

目标强度：规范定义后执行全量改造。
核心变更要点：
1. `.workspace` 下所有 `INDEX` 尽可能简短说明其管理范围内（同目录文件与子目录）的内容梗概，并按目录类型给出不同粒度示例（例如 `.workspace/INDEX` 可极简；task 目录 `INDEX` 需要更具体）。
2. map 系列优先聚焦 `project-map`、`resource-map` 的级联支撑能力；本 task 仅做初步实现，细节后续单独话题展开。

**Source:** discuss-log.md → Iteration 4
**Source:** discuss-log.md → Iteration 10
**Source:** discuss-log.md → Iteration 13

---

## Boundary

- **In scope:** `.workspace/project-map`、`.workspace/resource-map`、`.workspace/exp-map`、`.workspace` 下所有 `INDEX` 文件、`TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）`，以及受影响的 `skills/*/SKILL.md`、相关 docs/scripts 的路径与编写规范引用。
- **Out of scope:** 与本任务无关的业务功能改造；map 级联机制的深度细节设计（后续单独话题处理）。

**Source:** discuss-log.md → Iteration 5
**Source:** discuss-log.md → Iteration 11
**Source:** discuss-log.md → Iteration 12

---

## Assumptions

1. 迁移采用硬切策略，不保留旧规范兼容层。
2. 迁移完成后，新产出与存量产出均按统一新规范维护。

**Source:** discuss-log.md → Iteration 6

---

## Acceptance Criteria

1. 形成可执行的“jmf 产出物索引规范 + map 系列编写规范”文档，覆盖命名、结构、引用与维护规则。
2. 按新规范完成范围内存量产物全量改造（含 `.workspace/*-map`、`.workspace` 全部 INDEX 文档及受影响 skills/docs/scripts 引用）。
3. 通过人工逐项检查确认无关键路径/引用断裂（不使用脚本化校验）。
4. `.workspace` 全部 INDEX 文件均补齐“管理范围内容梗概”，并体现目录类型差异化粒度（例如根 INDEX 简要、task 目录 INDEX 更具体）。
5. `project-map`、`resource-map` 完成面向级联支撑的初步实现与文档说明。

**Source:** discuss-log.md → Iteration 7
**Source:** discuss-log.md → Iteration 12

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | PROJECT-MAP 存在失效路径 `.workspace/templates/`，是否先运行 `jmf-sync` | No | 用户选择先继续 Discuss，后续维护处理 |
| 2 | 一致性校验的实现形式（脚本化或手工清单） | No | 已决：人工逐项检查，不用脚本 |
| 3 | map 规范覆盖范围是否包含 `project-map/resource-map/exp-map` 全量 | No | 已决：三类 map 全覆盖 |

---

## Key Decisions

### PROJECT-MAP stale handling
本轮 Discuss 先继续需求收敛，不将 stale path 作为当前阻塞项。

**Source:** discuss-log.md → Iteration 3

### Optimization Focus
索引规范与 map 规范同权推进；交付形态为“规则清单 + 示例”；采用“规范 + 全量落地”。

**Source:** discuss-log.md → Iteration 10

### Validation Approach
一致性校验采用人工逐项检查，不使用脚本。

**Source:** discuss-log.md → Iteration 12

### Core Change Priorities
优先保证 INDEX 对管理范围内容的简明梗概能力；map 系列先完成级联支撑的初步实现，后续再迭代细节。

**Source:** discuss-log.md → Iteration 13

---

## Conclusion

Discuss 完成，核心变更要点与边界已确认，可进入 Planning。

**Source:** discuss-log.md → Iteration 13
