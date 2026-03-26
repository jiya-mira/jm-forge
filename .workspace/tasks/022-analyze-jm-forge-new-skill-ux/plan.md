# Plan: analyze-jm-forge-new-skill-ux

**Source:** discuss.md

---

## Goal

将 discuss 阶段的新认知（Goal Clarification、Split Detection 原则）落实为具体的 skill 行为改进。

---

## Scope

**In Scope:**
- `jm-forge:new` skill 行为更新
- `jm-forge:discuss` skill 行为更新
- `jm-forge:plan` skill 行为更新
- `jm-forge:execute` skill 行为更新
- `discuss-log.md` 模板更新
- 相关文档同步

**Out of Scope:**
- 其他 skill 的改动
- GSD 工作流相关功能
- TASK-REGISTRY schema 改动

---

## 核心原则（贯穿所有 Skill）

### 原则 1: Goal Clarification 是上游

Goal Clarification 决定了后续所有行为的内容和方向：

- **Discuss** = 搞清楚 Goal 是什么
- **Plan** = 设计达成 Goal 所需的方案
- **Execute** = 执行达成 Goal 所需的行动

不预先假设 Goal 一定是"调查"或"修复"——具体内容由 Goal Clarification 决定。

### 原则 2: Split Detection 采用"不确定性询问"原则

- 不设计硬编码触发条件
- 当 Agent 感到"不确定这算一个 task 还是两个"时，就停下来询问用户
- Agent 的职责：**感到不确定 → 停下来问用户**

### 原则 3: Goal Clarification 是动态的

- Goal 不是在 new 时就锁定的
- Goal 可能在 discuss / plan / execute 任何一个阶段演化
- 这是**正常的**，不是规划失误

---

## Deliverables

### Step 1: Update jm-forge:new SKILL.md

**Checkpoint:** `SKILL.md` 包含原始描述记录和初步 Goal Clarification

**具体改动：**
1. **Behavior 部分**：
   - 记录用户提供的最原始的描述（保留素材原味）
   - 增加引导问题："这个 task 的目标是什么？"
   - 增加引导问题："这是新问题还是与现有 task 相关？"
2. **Output 部分**：
   - 说明会记录原始描述
   - 说明会记录初步的 Goal Clarification
3. **Notes 部分**：
   - 说明 Goal Clarification 是动态的，后续 phases 会持续确认
   - 说明 Split Detection 意识——如果感到不确定，提示使用 jm-forge:discuss

---

### Step 2: Update jm-forge:discuss SKILL.md

**Checkpoint:** `SKILL.md` 包含 Goal Clarification 标准环节和 Split Detection 协议

**具体改动：**
1. **Conduct Discuss Phase 部分**：
   - 增加 "Iteration 0: Goal Clarification" 作为第一个 iteration
   - 格式引导：原始反馈 → 澄清问题 → 用户回复
2. **Split Detection 机制**：
   - 当 Agent 感到不确定时，追加 Iteration 记录并询问用户
   - 询问格式：选项 A（继续当前 task）、选项 B（拆分）、选项 C（其他）
3. **Iteration Norms 部分**：
   - 明确"不确定性询问"原则
   - Split Detection 的迭代格式模板
4. **Goal Clarification 动态性**：
   - 说明 Goal Clarification 可能在后续 iterations 中演化
   - 如果 Goal 发生变化，应该记录并向用户确认

---

### Step 3: Update jm-forge:plan SKILL.md

**Checkpoint:** `SKILL.md` 体现 Goal Clarification 上游原则和 Split Detection 意识

**具体改动：**
1. **Purpose 部分**：
   - 明确 Plan 的职责由 Goal Clarification 决定
2. **Behavior 部分**：
   - 增加 Split Detection 意识——plan 过程中感到不确定也要停下来问
   - 如果在 planning 过程中 Goal 发生变化，记录并向用户确认后再继续
3. **Notes 部分**：
   - 说明 Plan 的输出内容取决于 Goal 是什么

---

### Step 4: Update jm-forge:execute SKILL.md

**Checkpoint:** `SKILL.md` 体现 Split Detection Checkpoint 和 Goal Clarification 上游原则

**具体改动：**
1. **Behavior 部分**：
   - 增加 Split Detection Checkpoint——execute 中发现问题时停下来问用户
   - "不确定性询问"原则：感到不确定就问，不自己决定继续埋头干
2. **Split Detection 触发**：
   - 当 Agent 感到 task 边界模糊时，追加 Iteration 记录并询问用户
3. **Goal Clarification 演化**：
   - 如果在执行过程中意识到 Goal 需要调整，停下来向用户确认
4. **Notes 部分**：
   - 说明 Execute 的输出由 Goal Clarification 决定

---

### Step 5: Update discuss-log.md 模板

**Checkpoint:** 模板包含 Goal Clarification 和 Split Detection 的标准格式

**具体改动：**
1. Goal Clarification iteration 格式：
```markdown
## Iteration 0 - Goal Clarification

### 原始反馈
（用户报告的问题原文）

### 澄清问题
1. 这次任务的最终目标是什么？
2. 成功的标准是什么？
3. 约束或优先级？

### 用户回复
**等待用户输入...**
```

2. Split Detection iteration 格式：
```markdown
## Iteration N - Split Detection

### 不确定点
（Agent 感到不确定的具体点）

### 建议的行动
- 选项 A：继续在当前 task 处理
- 选项 B：拆分出去，创建新 task
- 选项 C：其他

**等待用户确认后继续...**
```

---

### Step 6: 同步更新 workflow-framework.md（如需要）

**Checkpoint:** 如果 workflow-framework.md 中的 phase 描述与新模型冲突，需要同步

---

## Verification

完成后，回答以下问题：

1. `jm-forge:new` 是否记录原始描述并包含初步 Goal Clarification？
2. `jm-forge:discuss` 是否将 Goal Clarification 作为标准第一个 iteration？
3. `jm-forge:plan` 是否体现 Goal Clarification 上游原则？
4. `jm-forge:execute` 是否包含 Split Detection Checkpoint？
5. Split Detection 是否统一采用"不确定性询问"原则？
6. discuss-log.md 模板是否包含两种标准 iteration 格式？
7. 所有 skill 是否避免了对 Goal 具体内容的预设假设？

---

## Dependencies

- Step 1 → Step 2（new 更新后再更新 discuss）
- Step 3, 4 与 Step 2 可并行（都依赖核心原则）
- Step 5 → Step 2（模板更新后与 discuss 同步）
- Step 6 与前三步可并行

---

## Open Issues

| Issue | Resolution |
|-------|------------|
| Goal Clarification 在 new vs discuss 的边界 | 实践中确定 |
| discuss-log 模板是否需要单独模板文件 | 在 Step 5 中决定 |