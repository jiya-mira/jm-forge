# Plan — jmf-task-lifecycle

**Date:** 2026-03-25
**Source:** Discuss output (consumed)

---

## Goal

当task的goal与REGISTRY中已完成task的goal发生冲突时，提供检测机制，减少agent困扰和token浪费。

**Source:** discuss.md

---

## Core Rule

**触发条件：goal发生significant变化时，Agent主动检测冲突**

- "significant变化"定义：goal的核心意图发生了改变（不是措辞微调）
- 触发时机：jmf-new初版goal形成、jmf-discuss中goal明确/调整
- 不绑定特定skill，而是引用统一规则

---

## Steps

### Step 1: 定义goal冲突检测规则

**Action:** 在workflow-framework.md或新建文件中定义冲突检测规则

**Approach:**
- 规则内容：
  1. 当goal发生significant变化时触发
  2. Agent读取REGISTRY中所有Completed task的goal
  3. Agent判断当前goal是否与已有goal冲突
  4. 如有冲突，提示用户："与task X (ID: N) 的goal可能冲突"
- 规则供各skill引用

**Checkpoint:** `goal-conflict-rule-defined`
- 规则文档存在
- 规则描述清晰，可被引用

---

### Step 2: 更新 jmf-new SKILL.md

**Action:** 在初版goal解读后添加冲突检测说明

**Approach:**
- 在SKILL.md中添加引用：
  > "当goal形成时，按照workflow-framework.md中的goal冲突检测规则执行"

**Checkpoint:** `jmf-new-references-conflict-rule`
- SKILL.md包含规则引用

---

### Step 3: 更新 jmf-discuss SKILL.md

**Action:** 在goal定义/调整后添加冲突检测说明

**Approach:**
- 在SKILL.md中添加引用：
  > "当goal发生significant变化时，按照workflow-framework.md中的goal冲突检测规则执行"

**Checkpoint:** `jmf-discuss-references-conflict-rule`
- SKILL.md包含规则引用

---

### Step 4: 更新 jmf-plan SKILL.md

**Action:** 在goal确认后添加冲突检测说明（可选，如goal无变化则不检测）

**Approach:**
- 在SKILL.md中添加引用：
  > "当goal发生significant变化时，按照workflow-framework.md中的goal冲突检测规则执行"

**Checkpoint:** `jmf-plan-references-conflict-rule`
- SKILL.md包含规则引用

---

### Step 5: 更新 jmf-abandon SKILL.md

**Action:** 说明Abandoned状态的含义（用于冲突后的archive）

**Approach:**
- 说明：Abandoned状态表示task被放弃，可保留在REGISTRY中供历史参考
- 不做强制archive，用户可自行处理

**Checkpoint:** `jmf-abandon-explains-state`
- SKILL.md有状态说明

---

## Dependencies

Step 2-4依赖Step 1完成。Step 5可独立进行。

## Tracking

| Assumption | Risk |
|-----------|------|
| Agent能准确判断goal是否发生significant变化 | Medium — 需信任Agent判断 |
| 用户能理解冲突提示并做出合理决策 | Low — 用户主导 |
| 冲突检测不显著增加token消耗 | Low — 只是读取和简单对比 |

## Execution Order

sequential (Step 1 → 2 → 3 → 4 → 5)
