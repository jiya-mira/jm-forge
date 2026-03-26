---
id: 25
---

# Discuss — exp-system

**Date:** 2026-03-25 / 2026-03-26
**Status:** Concluded

---

## Goal

设计并构建一套经验沉淀体系：以 Skill 为载体，内嵌经验文档模板规范，通过主动调用嵌入 jm-forge 工作流，实现项目实战经验的结构化沉淀与复用。

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** 经验文档格式规范（模板）设计、`jmf-exp` Skill 建设、与 jmf-discuss/plan/execute 工作流的嵌入点设计、用 racobit Task 3 实例验证模板可行性
- **Out of scope:** 模式内容的批量填充、搜索引擎/检索系统、多语言/多格式支持

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. jmf-exp Skill 由用户主动触发（不自动弹出）
2. 模板格式为纯文本 markdown，足够表达结构
3. 一个 jmf-exp Skill 即可覆盖需求，不需拆分
4. Skill 可自我验证（用 racobit Task 3 discuss-log 跑通）
5. **exp 必须有 attempt 来源**，不接受纯外部信息（RAG、预训练）直接沉淀为 exp

**Source:** discuss-log.md → Iteration 3

---

## Acceptance Criteria

1. `jmf-exp` Skill 存在于 `skills/` 目录，可被 agent 调用
2. Skill 内置经验模板，包含：场景/模式标签/根因/解法/关联任务/教训
3. 模板已在 racobit Task 3 discuss-log 上跑通验证
4. 安装 jm-forge 时不增加额外复杂度

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | 触发时机：用户主动调用，非自动 | No | resolved |
| 2 | 安装位置：`skills/`（安装脚本映射到各 Agent 目标目录） | No | resolved |
| 3 | 经验记录的存储契约：仅 Markdown 还是要配套固定索引/目录 | No | 已定：v1 仅 Markdown |
| 4 | 经验条目的唯一标识：按场景名、任务号、时间戳还是 hash | No | 已定：规则化、可复现的 ID |
| 5 | 更新责任边界：仅手动触发还是允许任务结束时半自动生成 | No | 已定：仅手动触发 |
| 6 | 冲突处理：成功/失败 attempt 混杂时如何裁决 exp 状态 | No | 已定：批次回顾 + 人工确认 |
| 7 | 验证样本范围：racobit Task 3 是否只作为首样本 | No | 已定：先单样本验证 |
| 8 | exp 与 memory 的边界：是否明确禁止吸收外部检索内容 | No | 已定：硬性禁止 |

---

## Key Decisions

### Skill 形式确定
**结论：** 以 `jmf-exp` Skill 为唯一交付物，模板嵌入 Skill 内部，不污染 `.planning/`。

**理由：** Skill 是 jm-forge 的安装单元，模板跟着 Skill 走才能保持安装便捷性。

### 两期规划
**结论：** 本期做模板规范 + Skill 建设；后续可选做 jmf-exp 自动化增强。

### 引证记录制度（Iteration 2）
**结论：** 采用引证分级制度（D），完整记录正向/负向引证，含成功率。

**理由：** exp 的更新是批次性回顾行为，引证记录必须完整才能让 Agent 在后续分析时充分分析。

### 验证结果分类（Iteration 2）
**结论：** 双层记录 + 批次回顾时归因。

- **第一层（现场）：** 简单事实描述——场景、尝试了什么、结果如何
- **第二层（批次回顾）：** Agent 归因分析 + 用户人工确认

### exp 状态流转（Iteration 2）
**结论：** 三级状态 + 流转规则。

| 状态 | 含义 |
|------|------|
| 待验证（New） | 新创建，尚未被后续 task 引用验证 |
| 已验证（Verified） | 至少 1 次正向引证 |
| 强验证（Strong） | 累计 3+ 正向引证，无失败 |

流转：新建→已验证→强验证；失败→降级；降级后可重新分级。

### 推翻 exp 归因机制（Iteration 2）
**结论：** Agent 批次回顾判断 + 用户人工确认。

三种归因及对应处理：
- **A. 场景差异：** 降级，保留，按场景匹配
- **B. exp 本身有问题：** 标记为"有问题"，批次回顾时分析是否修正或拆分
- **C. 外部因素：** 归因为"外部因素"，exp 本身不变

**Source:** discuss-log.md → Iteration 2

### exp 与 memory 的边界（Iteration 3）
**结论：** exp 是归纳产物，memory 是检索产物——本质不同，必须明确区分。

**三层模型：** task（待解决对象）→ attempt（具体处理经历）→ exp（归纳出的可复用模式）

- Memory：外部检索得到（RAG、预训练），默认可信
- Attempt：内部经历得到，实际执行过一次
- Exp：从 attempt 归纳提炼，须满足提升条件（至少两条：不止一次出现、可跨 task 复用、能说清适用条件、有成功/失败证据、能压缩成短规则）

**Source:** discuss-log.md → Iteration 3

### 补充边界确认（Iteration 4）
**结论：** 存储契约、ID 规则、更新责任、冲突处理、样本范围、memory 边界都需要在 Plan 中显式落文，但它们当前均为非阻塞项。

**理由：** 这些点会影响实现方式和后续演进，但不会改变 `jmf-exp` 作为 Skill 的核心定义。

**Source:** discuss-log.md → Iteration 4

### v1 定案（Iteration 5）
**结论：** 采用简化稳妥版作为 `jmf-exp` 第一版本：Markdown 单输出、规则化 ID、仅手动触发、批次回顾 + 人工确认、racobit 单样本验证、禁止外部检索直写 exp。

**理由：** 这套方案最容易在本 task 内交付，并且与当前 workflow 的复杂度最匹配。

**Source:** discuss-log.md → Iteration 5

---

## Conclusion

jm-forge 已有完整的 Discuss→Plan→Execute 工作流（Task 3），缺乏的是经验的结构化沉淀机制。jmf-exp Skill 补全这一环：用户在任务收尾或复盘时主动调用，从工作流产物（discuss-log 等）提取信息，生成结构化经验文档。

Iteration 2 追加了 exp 的生命周期验证机制：引证分级记录 → 双层归因 → 三级状态流转 → Agent+用户双层决策。Iteration 3 进一步明确了 exp 的本质边界——归纳而非检索，三层模型（task/attempt/exp）确立了 exp 的来源规范。

这套机制确保 exp 的质量随使用不断被验证和迭代，而非一次性产出。

**Ready for Plan.**

**Source:** discuss-log.md → Iteration 5
