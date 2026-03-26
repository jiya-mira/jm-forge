---
id: 31
---

# Discuss — fix-missing-and-untracked-after-restructure

**Date:** 2026-03-27
**Status:** Concluded

---

## Goal

在目录结构大规模调整后，修复任务跟踪链路中的缺失/失真点，确保任务创建、状态推进、索引追踪恢复稳定可用。

**Source:** discuss-log.md → Iteration 2

---

## Boundary

- **In scope:**
  - 修复与任务跟踪直接相关的缺失或异常（索引写入、状态流转、关键引用）
  - 允许中等范围的相邻兼容修复（历史引用迁移标注、模板更新）
  - 执行高标准回归验证（覆盖技能契约与历史文档一致性）
- **Out of scope:**
  - 与任务跟踪无关的功能重构
  - 全仓风格化重写或大规模无关清理

**Source:** discuss-log.md → Iteration 2

---

## Assumptions

1. `.workspace/tasks/INDEX.md` 作为任务真源可覆盖原 `TASK-REGISTRY.md` 信息需求。
2. 历史文档允许保留“legacy 映射说明”，无需改写历史事实结论。
3. 中等改动范围可在不引入破坏性变更的前提下完成闭环修复。

**Source:** discuss-log.md → Iteration 2

---

## Acceptance Criteria

1. `jmf-*` 关键技能对任务状态与存在性判断统一基于 `.workspace/tasks/INDEX.md`。
2. 任务 #31 涉及的缺失/跟踪问题有明确修复落盘，路径可达且引用可追踪。
3. 完成高标准回归验证：至少包含技能契约引用扫描、索引状态一致性检查、历史文档 legacy 映射检查。
4. 结论可复述为可执行规则，并可直接进入 Plan 阶段。

**Source:** discuss-log.md → Iteration 2

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | 是否后续彻底删除 legacy 文本 | No | 当前采用兼容标注，后续可独立任务处理 |
| 2 | 是否增加自动化校验脚本 | No | 本任务先手动高标准回归，自动化可后续增补 |

---

## Key Decisions

### 修复优先 + 中等改动 + 高标准回归
本任务采用“修复为主”策略，不做大重构；允许中等范围兼容修复；验收采用高标准全量回归。

**Source:** discuss-log.md → Iteration 2

---

## Conclusion

Discuss 已收敛，无阻塞问题。建议进入 Plan 阶段，围绕“真源统一、缺失补齐、回归验证”拆分执行步骤。

**Source:** discuss-log.md → Iteration 2
