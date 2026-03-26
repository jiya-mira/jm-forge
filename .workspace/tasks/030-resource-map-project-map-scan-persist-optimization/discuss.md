---
id: 30
---

# Discuss — resource-map-project-map-scan-persist-optimization

**Date:** 2026-03-27
**Status:** Concluded

---

## Goal

修正当前 map 记录模型与预期不一致的问题，重构为“tree + graph”的分层记录模式：
- `project-map` 聚焦项目源码/业务文件关系与导航，不再承载 `.workspace` 工作流运行态细节；
- `resource-map` 参考 `project-map` 的分层思路，但保持更轻量的数据模型。

**Source:** discuss-log.md → Iteration 3

---

## Boundary

- **In scope:**
  - 重新定义 `project-map` 的记录边界：面向项目本体文件与关系，不含 `.workspace` 运行态细节
  - 定义 tree 层（层级目录/模块归属）与 graph 层（引用/依赖关系）的职责分工
  - 调整 `resource-map` 的结构，使其借鉴分层模式但保持简化
  - 重写 Task #30 的 Plan，以新记录模型为基线
- **Out of scope:**
  - 与 map 结构无关的工作流功能重构
  - 一次性引入过重的 map 引擎或复杂元编排机制

**Source:** discuss-log.md → Iteration 3

---

## Assumptions

1. 当前 `project-map` “单处承载过多信息”的问题是本次偏差核心，应优先处理。
2. `.workspace` 属于 workflow runtime 空间，应作为流程工件管理，不应成为 `project-map` 主体记录对象。
3. `resource-map` 与 `project-map` 不需要同等复杂度，轻量化优先。

**Source:** discuss-log.md → Iteration 3

---

## Acceptance Criteria

1. `project-map` 的记录对象与边界明确：仅聚焦项目本体（源码/文档/资源）的 tree+graph 信息。
2. `.workspace` 相关内容从 `project-map` 主体语义中剥离，仅保留必要引用而非主记录。
3. `resource-map` 新结构能表达资源清单与基础关联，且复杂度显著低于 `project-map`。
4. 重写后的 Plan 与以上边界一致，并可直接指导 Execute。

**Source:** discuss-log.md → Iteration 3

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | tree 层文件组织采用单文件还是多文件目录化 | No | 在 Plan 阶段确定实现颗粒度 |
| 2 | 历史 map 数据迁移策略（一次性/分批） | No | 优先分批迁移，降低回归风险 |

---

## Key Decisions

### 以“记录模型偏差修正”为核心重开 Discuss
本轮不再围绕“泛化优化”展开，而是明确聚焦 map 记录模型本身的偏差：`project-map` 采用 tree+graph 分层，`resource-map` 采用轻量化借鉴。

**Source:** discuss-log.md → Iteration 3

### 重写 Plan
保留 Task #30 任务 ID 与目标域，但废弃上一版计划结构，基于新的边界与验收标准重写 Plan。

**Source:** discuss-log.md → Iteration 3

---

## Conclusion

Discuss 已重新收敛，Open Issues 全为非阻塞。建议立即进入 Planning 并重写 Plan（以“边界重构 + 分层模型 + 渐进迁移”为主线）。

**Source:** discuss-log.md → Iteration 3
