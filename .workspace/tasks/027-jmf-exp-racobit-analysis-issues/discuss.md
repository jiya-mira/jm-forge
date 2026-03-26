---
id: 27
---

# Discuss — jmf-exp-racobit-analysis-issues

**Date:** 2026-03-26
**Status:** Concluded

---

## Goal

基于 racobit workspace 的真实尝试，纠正 `jmf-exp` 的目标偏差：从“最新 task 总结器”调整为“项目级 exp 提炼与沉淀机制”。

---

## Boundary

- **In scope:** `jmf-exp` 在项目级经验提炼中的来源规则、summary 兼容策略、产物结构（目录/索引/单条文档）与执行行为
- **In scope:** `jmf-execute` 在任务关闭前的 summary 产出与落盘约束（作为上游契约）
- **Out of scope:** racobit workspace 代码改动、无关 skill 改动、跨系统端到端联动

---

## Assumptions

1. 你已经在 racobit workspace 进行了至少一次可复现或可描述的尝试，并可提供失败样例信息。
2. 本任务只调整元 skill（`jmf-exp`、`jmf-execute` 及其必要元信息），其他系统或仓库不改动。
3. 当前阶段以问题定义和可执行改进为先，避免无边界扩改。
4. `summary` 可能缺失，流程必须支持在无 summary 条件下继续提炼。

---

## Acceptance Criteria

1. 明确列出 `jmf-exp` 问题清单（含触发条件、偏差点、影响）。
2. 问题清单限定在元 skill 调整边界内，不扩展到其他系统改动。
3. 明确 `jmf-execute -> summary` 的关闭前约束与 `jmf-exp` 的历史兼容策略。
4. Discuss 结束时 open issues 全部 non-blocking，可直接进入 Plan。

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | 优先处理单点 bug 还是系统性问题 | No | 已确定系统性收敛优先 |
| 2 | 具体问题样例是否已完整收集 | No | 已补充关键偏差：项目级 vs 最新 task 总结 |
| 3 | 修复边界是否仅限 `jmf-exp` 本体 | No | 已进一步收紧为仅调整元 skill |
| 4 | 验收是否要求修复草案/回归用例 | No | 已确定仅问题清单 |
| 5 | exp 产物结构是否固定为“目录+索引+单条文档” | No | 已定为硬性要求 |
| 6 | 单条 exp 模版字段是否已冻结 | No | 已定为 T1 必填 + 可选扩展 |
| 7 | summary 生成失败时是否阻断 task 关闭 | No | 已定为强阻断关闭 |

---

## Key Decisions

### Goal 优先级：系统性收敛优先
本任务先沉淀系统性问题与改进方向，具体修复作为后续落地手段而非唯一目标。

**Source:** discuss-log.md → Iteration 2

### Boundary：必须绑定真实失败样例
讨论与后续计划必须锚定 1-2 个失败样例（输入/预期/实际），以保证问题定义和验收可验证。

**Source:** discuss-log.md → Iteration 3

### Boundary：允许小范围联动
修复可覆盖 `jmf-exp` 与其直接上下游契约，但不做端到端大范围联动。

**Source:** discuss-log.md → Iteration 4

### Assumption：仅调整元 skill
实现边界收紧为仅改 `jmf-exp` 相关元 skill，不触碰其他仓库或无关模块。

**Source:** discuss-log.md → Iteration 5

### Acceptance：仅问题清单
本任务 Discuss 的验收以“问题清单收敛”完成，不要求在本阶段附带修复草案与回归用例。

**Source:** discuss-log.md → Iteration 6

### 问题重定义：项目级 exp，而非最新 task 总结
`jmf-exp` 的核心偏差是提炼层级错误，应支持独立经验与跨任务共性经验两类来源，并兼容 summary 缺失场景。

**Source:** discuss-log.md → Iteration 8

### 产物契约：目录+索引+单条文档为硬约束
exp 产物结构必须显式落地，不允许仅输出即时总结。

**Source:** discuss-log.md → Iteration 9

### 模版策略：T1 必填 + 可选扩展
单条 exp 采用精简必填字段作为统一基线，并允许按实际场景附加额外信息。

**Source:** discuss-log.md → Iteration 10

### 上游契约：关闭前必须 summary 落盘
新 task 在 Execute 关闭前必须产出 summary 并按模板落盘；历史 task 缺失 summary 作为兼容例外处理。

**Source:** discuss-log.md → Iteration 11

### 关闭策略：summary 失败即阻断
若 summary 生成或落盘失败，`jmf-execute` 不得关闭 task，必须先修复并成功落盘。

**Source:** discuss-log.md → Iteration 12

---

## Conclusion

问题定义已收敛，当前 open issues 均为 non-blocking。Discuss 结束，可进入 Plan。

**Source:** discuss-log.md → Iteration 13
