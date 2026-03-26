---
id: 23
---

# Discuss — jmf-task-lifecycle

**Date:** 2026-03-25
**Status:** Concluded

---

## Goal

当新task的goal与REGISTRY中已有task的goal冲突时，提供检测和归档机制，减少agent困扰和token浪费。

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope：**
  - 检测新task的goal与REGISTRY中任意task的goal冲突
  - 冲突处理提示
  - archive操作（用户确认后执行）

- **Out of scope：**
  - task内部的goal调整（那是task自身生命周期的事）
  - 跨task的依赖关系处理

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. 一个task只有一个goal
2. task完成后goal就固定了，不会再变
3. 已完成task的goal是可靠的参照物
4. archive操作需要用户手动确认，不能自动执行

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. jmf-new/discuss/plan能检测当前goal是否与REGISTRY中某task的goal冲突
2. 发现冲突时，提示用户说明冲突的是什么
3. 用户决定处理方式
4. 新task成功后，询问是否archive冲突的旧task
5. 用户确认后，旧task标记Abandoned并可选择移动到TASK-ARCHIVE.md

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| — | 无 | — | — |

---

## Key Decisions

### goal冲突检测机制

冲突检测在以下时机触发：
- `jmf-new` — 创建新task时
- `jmf-discuss` — 讨论阶段
- `jmf-plan` — 计划阶段

检测方式：基于goal文本的相似度判断（具体算法待plan阶段细化）

### archive前提条件

archive操作必须满足：
1. 旧task状态为Completed（goal已固定）
2. 用户手动确认

**Source:** discuss-log.md → Iteration 1

---

## Conclusion

建立goal冲突检测 + 用户确认archive的机制，集成到jmf-new/discuss/plan中，在源头避免无效task处理。

**Source:** discuss-log.md → Iteration 1
