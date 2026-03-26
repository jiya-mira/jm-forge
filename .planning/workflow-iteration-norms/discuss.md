# discuss.md

**Source:** discuss-log.md

---

## Goal

规范化工作流迭代行为，解决"阶段边界模糊"问题。目标是：**让迭代自然发生，文档自动记录**，而不是被强制门禁打断。

## Boundary

### In Scope
- 阶段（Phase）之间的过渡规则
- 文档迭代策略（append-only）
- 状态（State）流转语义
- Phase Gate 验证时机

### Out of Scope
- 任务依赖（Dependon）机制改进
- 多 Agent 并发控制
- 其他工作流框架对比研究
- 框架文档作为独立发布物

## Assumptions

1. Agent 工作流上下文在内存中，迭代成本低
2. 发现问题是深入思考的结果，不是失败
3. 文档是上下文的外化，append-only 保留完整历史
4. 状态（State）只是主工作位置标记，不是阶段切换的唯一标志

## Acceptance Criteria

1. 新的迭代规范文档化到 `workflow-framework/` 或相关位置
2. 核心原则：Append-only + Soft Boundaries
3. 阶段切换不再强制要求 State 变更
4. 任何阶段都可以发现问题并追加 Iteration

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | 新规范放在哪里 | Non-blocking | **Resolved (Option B)**: 内化到技能的 SKILL.md 中 |
| 2 | 现有 task #19 如何处理 | Non-blocking | 不追溯，仅作为经验教训 |
| 3 | State 流转是否调整 | Non-blocking | **Resolved**: State 仍是主位置标记，迭代不强制改 State |
| 4 | 需要更新的技能 | Non-blocking | jm-forge:discuss, jm-forge:plan, jm-forge:execute |

## Key Decisions

### 1. Norms Enforcement: Option B (In-Skill)

- 规范**内化到技能**的 SKILL.md 中，而非独立文档
- 用户通过技能工作时自然遵循规范
- 单一来源，避免文档与行为不同步

### 2. Append-Only Documents

- 文档只追加，不覆盖
- `discuss-log.md` 记录每次迭代的输入、决策、结论
- 每次迭代有明确的 Iteration N
- 历史记录永远保留

### 3. Soft Phase Boundaries

- 阶段（Discuss/Plan/Execute）是**指导框架**，不是**硬性门禁**
- 允许在任意阶段发现问题并迭代
- 不强制回退，但允许回跳
- 文档记录比状态切换更重要

### 4. Phase Gate Verification

- 进入 Execute 前快速确认："Plan 是否真正解决了 Discuss 的目标？"
- 不确定时：追加 Iteration 说明疑问，而非强制停止

### 5. Execute 失败处理

- Checkpoint 失败：先 self-resolve
- 无法解决：更新 execute.md，记录失败原因
- 允许回退到 Plan，更新后重新 Execute
- 不视为"失败"，视为"迭代"

### 6. State 流转语义

- State 反映主工作位置
- 迭代不强制变更 State
- 状态切换是"主位置变化"的标志，不是"阶段内小迭代"的标志
