# Task: analyze-jm-forge-new-skill-ux

## Iteration 1 - 2026-03-24（Task Created）

### 任务背景
基于 racobit 项目近期对 jm-forge 系列技能的应用案例，分析 `jm-forge:new` 的 UX 优化方向。

### Racobit 案例中的 Tasks #1 和 #2

| ID | Name | State | Dependon |
|----|------|-------|----------|
| 1 | trip-sync-user-issue | Pending | 2 |
| 2 | sunjunfeng-travelconfirm-issue | Planning | - |

### Racobit TASK-REGISTRY 结构
- ID: 自增整数
- Name: kebab-case 任务名
- State: New/Pending/Planning 等
- Dependon: 依赖任务 ID

### 待分析点
1. discuss-log.md 模板内容是否足够？
2. TASK-REGISTRY 是否需要额外列（priority/labels/assignee）？
3. PROJECT-MAP 集成方式（作为 Domain vs Task 类型）是否合理？
4. --dependon 是否需要支持多依赖？
5. 是否需要 --label --priority --domain 等额外选项？

---

## Iteration 2 - 2026-03-24（关键发现）

**Source:** racobit 案例分析 + 用户反馈

### 原始场景回顾

用户一次性提交了两个数据问题反馈，Agent 将其创建为 Task #1。在执行过程中，Agent 实际上已经发现这两个问题的根因和解决方案完全不同，但仍然埋头继续执行 #1，没有主动询问用户。最终是用户发现不对劲，强行暂停 #1 后手动引导创建了 #2。

### 核心发现：Task 的目标定义时机错误

| 维度 | 原始假设 | 实际发现 |
|------|---------|---------|
| Task 创建时 | 目标已清晰定义 | 实际上用户给的只是原始素材/问题陈述 |
| Discuss 起点 | 分析问题本身 | 应该是 **Goal Clarification** —— 先确认"这次任务的目标到底是什么" |
| Discuss vs Plan | discuss = 分析，plan = 方案 | discuss = **搞清楚目标**，plan = **调查方案**，execute = **输出调查结果** |
| Execute 结果 | 假设直接输出修复方案 | 可能是"调查结果"，需要根据结果再判断下一步 |

### 用户补充观点（Split Detection 的广义化）

即使最终目标是"分析问题并给出结论"（而非直接修复），Split Detection 机制仍然必要。原因：

> 当两个反馈需要**完全不同的调查方式**才能得出结论时，即使目标一致（都是"分析"），仍然需要拆分。

例如：
- 反馈 A：需要查服务器日志 + DB 查询
- 反馈 B：需要代码审查 + 接口抓包
- 两者调查路径完全不同，在同一个 task 内交叉执行效率低下

### 修正后的 Phase 职责划分

```
Discuss (目标确认 + 问题初步识别)
  ↓
Plan (调查/分析方案)
  ↓
Execute (执行调查，输出结果)
  ↓
   ├→ 结果符合预期 → 进入下一阶段
   ├→ 发现问题分化（根因不同 OR 调查方式不同）→ Split Checkpoint（询问用户）
   └→ 根因不明 → 继续调查 or 升级
```

### Split Detection 的触发条件（广义版）

```markdown
当 Agent 在 discuss/plan/execute 过程中发现：
1. 两个反馈的根因链条完全独立
2. 或者两个反馈虽然可能同根因，但需要完全不同的调查手段才能确认
→ 触发 Split Checkpoint
```

### 结论

jm-forge 工作流需要增加两个新机制：

1. **Goal Clarification 环节** —— discuss 阶段第一步不是分析问题，而是确认"这次任务的目标是什么"

2. **Split Detection 协议** —— execute（甚至 discuss/plan）阶段发现问题时，停下来询问用户是否需要拆分

### 原始待分析点的处理

| Issue | 结论 |
|-------|------|
| discuss-log.md 模板内容 | **已废弃**，替换为 Goal Clarification 框架 |
| TASK-REGISTRY 扩展列 | **暂缓**，不是当前痛点 |
| PROJECT-MAP 集成类型 | **暂缓**，不是当前痛点 |
| --dependon 多依赖 | **暂缓**，不是当前痛点 |
| --label 等选项 | **暂缓**，不是当前痛点 |

**所有 open issues 已重新分类为 Non-blocking。**

---

## Iteration 3 - 2026-03-24（进一步精化）

**Source:** 用户反馈 + 深入讨论

### 对 new 的重新定位

jm-forge:new 应该达成三个目的：

| # | 目的 | 说明 |
|---|------|------|
| a | 记录最原始的描述 | 保留素材原味，不做预先加工 |
| b | 进行初步的 Goal Clarification 分析和确认 | 初步对焦，但不要求完整清晰 |
| c | 创建 task（即使目标不清晰） | **不同意"说不清目标就不该创建"**——目标往往是干着干着才清晰的 |

### Goal Clarification 是动态的

```
不是"先定义清楚再开始"（瀑布式）
而是"在过程中发现和修正"（迭代式）
```

- 可能在 discuss/plan/execute 任何一个阶段发生变化
- 这是**正常的**，不是规划失误
- Goal 的演化本身就可能触发 Split Detection

### Split Detection 原则

- **不接受硬编码触发条件**（根因分化、调查方式分化等都无法穷举）
- 采用 **"不确定性询问"原则**：
  > 当 Agent 感到"不确定这算一个 task 还是两个"的时候，就直接问用户
- Agent 的职责：**感到不确定 → 停下来问用户**

### 底层哲学

这是一个 **"Goal 是在过程中发现的"** 的实用主义模型：

| 理想主义模型 | 实用主义模型 |
|-------------|-------------|
| Goal 必须先定义清楚才能开始 | Goal 往往是干着干着才清晰的 |
| 规划是为了消除不确定性 | 规划是为了更好地探索不确定性 |
| 分析后再行动 | 行动本身就是分析的一部分 |

### 下一步

是否需要结合理论来完善 discuss phase？在直接 Plan 之前，可能需要理解：
- 什么是一个好的 discuss phase？
- Goal Clarification 在认知层面发生了什么？
- 有哪些相关领域知识可以借鉴？

---

## Iteration 4 - 2026-03-24（理论支撑）

**Source:** 理论文献研究

### 相关理论框架

#### 1. Wicked Problems (Rittel & Webber, 1973)

**核心观点：**
-  wicked problem 无法在问题定义之前就确定解决方案
- 问题与解决方案相互定义——你无法先完整定义问题再找答案
- 每一个"解决方案"都会揭示新的问题

**对 jm-forge 的启发：**
- 用户报告的"数据问题"本质上是一个 wicked problem
- Task 的创建不是"定义清晰目标"，而是"开启一个探索过程"
- discuss phase 不是一个"澄清已存在的东西"，而是"共同构建问题本身"

#### 2. Double Loop Learning (Argyris & Schön, 1978)

**核心观点：**
- Single Loop Learning：修正行为但不质疑假设
- Double Loop Learning：同时质疑背后的假设和心智模型

**对 jm-forge 的启发：**
- discuss phase 应该允许"质疑基本假设"
- 比如用户最初认为"这是系统 bug"，但 discuss 后发现"其实是用户流程问题"
- 这要求 discuss 能容纳"假设翻转"，而不是线性推进

#### 3. Problem Space vs Solution Space (Newell, Simon, etc.)

**核心观点：**
- 首先理解问题空间（Problem Space）：约束、变量、关系
- 然后才进入解决方案空间（Solution Space）
- 混淆两者是很多问题的根源

**对 jm-forge 的启发：**
| Phase | 职责 |
|-------|------|
| Discuss | 问题空间探索：这是什么类型的问题？边界在哪？ |
| Plan | 解决方案设计：如何解决这个问题？ |
| Execute | 实施和验证：方案有效吗？ |

#### 4. Inquiry-Based Learning

**核心观点：**
- 理解不是被动接收的，而是通过主动探究生成的
- 学习者需要提出假设、收集数据、检验假设

**对 jm-forge 的启发：**
- 用户给的是"原材料/观察"，不是"问题定义"
- discuss phase = 主动探究过程
- Agent 是"探究协作者"，不是"执行者"

### 综合：jm-forge Discuss Phase 的新定位

```
用户报告 ← 原始素材，不是问题定义
    ↓
Discuss Phase
    ├→ Goal Clarification：我们要往哪里走？
    ├→ Problem Space 探索：这到底是什么类型的问题？
    └→ Split Detection：这个问题需要拆分吗？
    ↓
Plan Phase
    └→ Solution Space：如何解决这个问题？
    ↓
Execute Phase
    └→ 验证：方案有效吗？
```

### Discuss Phase 的必要条件

1. **不确定性容忍度** —— 不要求在讨论初期就有清晰结论
2. **假设显式化** —— 把隐含的假设说出来，让用户确认或质疑
3. **Split Detection 意识** —— 持续评估"这还是一个 task 吗"
4. **Goal 动态确认** —— 目标可能演化，这本身是正常的

### Discuss 的产出（更新后的期望）

| 产出 | 说明 |
|------|------|
| 初步 Goal Statement | 暂时性的目标陈述（可演化） |
| 假设清单 | 这次调查/分析依赖的关键假设 |
| 问题类型判断 | Bug？流程问题？数据问题？外部系统问题？ |
| Split 判断 | 是否已经识别到需要拆分的情况？ |
| 调查方向 | 初步的调查路径（不是完整方案） |

### 结论

Discuss Phase 的核心价值不是"找答案"，而是：
- **确保 we're solving the right problem**（而不是直接跳进 solving the problem right）
- **让 Agent 和用户对问题空间有共同理解**
- **持续评估 task 边界是否仍然有效**
