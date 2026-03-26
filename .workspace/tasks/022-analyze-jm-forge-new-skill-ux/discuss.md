# Discuss: analyze-jm-forge-new-skill-ux

**Source:** discuss-log.md → Iteration 4

---

## Problem Statement

jm-forge:new 和 discuss phase 存在根本性的设计缺陷：

1. **Task 边界锁死问题**：jm-forge:new 创建 task 后，task 边界就锁死了。Agent 在执行过程中发现问题时，不会主动询问用户是否需要拆分。

2. **Goal Clarification 缺失**：工作流假设用户创建 task 时目标已经清晰，但实际上用户给的只是原始素材。

3. **Split Detection 缺位**：当两个反馈可能同根因或需要不同调查方式时，Agent 没有机制停下来询问用户。

---

## Key Discoveries

### 1. Goal Clarification 是动态的

- 不是"先定义清楚再开始"（瀑布式）
- 而是"在过程中发现和修正"（迭代式）
- 目标往往是干着干着才清晰的

### 2. jm-forge:new 应达成三个目的

| # | 目的 | 说明 |
|---|------|------|
| a | 记录最原始的描述 | 保留素材原味 |
| b | 初步 Goal Clarification | 初步对焦，不要求完整清晰 |
| c | 创建 task | 即使目标不清晰也该创建 |

### 3. Split Detection 原则

- 不接受硬编码触发条件
- 采用"不确定性询问"原则：Agent 感到不确定 → 停下来问用户
- Agent 职责：**感到不确定 → 停下来问**

### 4. 底层哲学

**"Goal 是在过程中发现的"实用主义模型**：
- Goal 不需要先定义清楚才能开始
- 规划不是为了消除不确定性，而是为了更好地探索不确定性
- 行动本身就是分析的一部分

---

## Theoretical Foundations

| Theory | Core Concept | Implication for jm-forge |
|--------|-------------|-------------------------|
| Wicked Problems | 问题无法在定义前确定解 | Task 创建是探索过程的开始，不是终点 |
| Double Loop Learning | 质疑假设而非只修正行为 | Discuss 应容纳"假设翻转" |
| Problem vs Solution Space | 先理解问题，再找方案 | Discuss = 问题空间，Plan = 解决方案 |

---

## Discuss Phase 新定位

```
Discuss (目标确认 + 问题空间探索)
  ↓
Plan (调查方案设计)
  ↓
Execute (执行调查，输出结果)
  ↓
   ├→ 结果符合预期 → 下一阶段
   ├→ Split Detection → 询问用户
   └→ 根因不明 → 继续调查
```

---

## Discuss 产出

| 产出 | 状态 |
|------|------|
| 初步 Goal Statement | 待讨论 |
| 假设清单 | 待讨论 |
| 问题类型判断 | 待讨论 |
| Split 判断 | 待讨论 |
| 调查方向 | 待讨论 |

---

## Open Issues

| Issue | Blocking? | Notes |
|-------|-----------|-------|
| 如何将 Split Detection 嵌入各 phase | Blocking | 需要具体设计 |
| Goal Clarification 在 new vs discuss 的边界 | Non-blocking | 可协商 |
| discuss-log.md 模板更新 | Non-blocking | 实施细节 |