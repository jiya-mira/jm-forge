# Discuss Log — exp-system

**Task ID:** 25
**Created:** 2026-03-25
**Status:** Initial

---

## Iteration 1 — Initial Goal Interpretation

**User Input:** "我想构建一个exp的体系"

**Initial Goal Interpretation (pre-Discuss):**

基于 racobit 项目（Task 3: zhang-honggen-data-issue）的实践经验，"exp" 很可能指：

> **经验体系（Experience System）** — 将项目实战中积累的问题分析、调试方法、决策模式结构化沉淀，使未来遇到类似场景时 Agent 能快速复用和推理。

与 racobit 案例的联系：
- Task 3 的 discuss-log 完整记录了：从"用户报错"→"API调试验证"→"定位分页原因"→"结论确认"的全流程
- 这种结构化的过程记录若形成模板/体系，可以复用到其他项目

**待确认：**
1. "exp" 具体指什么？（经验沉淀？实验框架？表达式系统？）
2. 目标是在 jm-forge 内构建，还是作为独立体系？
3. 与现有 document-relationship-graph（Task 5）的边界如何划分？

---

*Source: jmf-new skill — initial goal interpretation*

---

## Iteration 1 — Discuss Sessions

**Trigger:** Task 25 首次 Discuss，目标尚未定义

**Discuss Flow:**
1. **"exp" 含义** → 用户选 A（经验沉淀）
2. **沉淀形态** → 用户选 B（模式库）
3. **定位** → 用户选 C（以 racobit 为分析素材，建在 jm-forge 里）；讨论中发现与"不动 racobit"矛盾 → 用户澄清：交付物是"沉淀方式"本身
4. **形式** → 用户选 Skill（不额外散落 .planning/）
5. **Skill 方向确认** → 用户选 A（合理）

**Resolved Open Issues:**
- 触发时机：用户主动调用
- 安装位置：`skills/`

**Conclusion:** 所有 open issues non-blocking，Discuss 结束

**Source:** discuss-log.md → Iteration 1

---

## Iteration 2 — 2026-03-26

**Trigger:** 用户追加讨论点 — exp 的验证与修缮机制

**Topic:** 经验的生命周期验证：如何记录引证、如何归因失败、如何决定 exp 的状态流转

---

### 子问题 1：引证记录（Provenance）

**用户决策：** D — 引证分级制度

完整记录正向/负向引证，含成功率。理由：exp 的更新是批次性回顾行为，引证记录必须完整才能让 Agent 充分分析。

---

### 子问题 2.1：部分验证（需微调）时 exp 是否更新

**结论：** 不实时修改 exp 正文。引证结果记录清晰，等批次回顾时统一分析是否需要合并/修正。

---

### 子问题 2.2：失败验证的归因机制

**推荐方案：** 双层记录 + 批次回顾时归因

- **第一层（现场）：** 客观事实描述——场景、尝试了什么、结果如何（简单记录）
- **第二层（批次回顾）：** Agent 归因分析 + 用户人工确认

理由：Agent 在现场信息不足，事后归因才更准确；初版引入 Summary 机制即可。

---

### 子问题 3：验证后的 exp 状态流转

**用户决策：** 三级状态

| 状态 | 含义 |
|------|------|
| 待验证（New） | 新创建，尚未被后续 task 引用验证 |
| 已验证（Verified） | 至少 1 次正向引证 |
| 强验证（Strong） | 累计 3+ 正向引证，无失败 |

**流转规则：**
```
新建 ──[首次正引证]──► 已验证
已验证 ──[累计3+正引证，无失败]──► 强验证
已验证 ──[遭遇失败]──► 降级
强验证 ──[遭遇失败]──► 降级
降级 ──[批次回顾分析后]──► 重新分级
```

---

### 子问题 4：推翻 exp 的复杂性处理

**4.1 归因判断机制：** Agent 批次回顾判断 + 用户人工确认

**4.2 推翻后的处理（三种归因对应三种处理）：**
- **A. exp 根本不适用于 #76（场景差异）：** 降级，保留，按场景匹配而非全局禁用
- **B. exp 本身有问题：** 标记为"有问题"，批次回顾时由 Agent 分析是否修正或拆分
- **C. 其他因素干扰：** 归因为"外部因素"，exp 本身不变

组合机制（4.1）的价值正是在此：4.2 的三种情况都需要 Agent 分析 + 用户确认才能最终决策。

---

**Conclusion:** 追加讨论完成。exp 的生命周期验证机制已确立：引证分级记录 → 双层归因 → 三级状态流转 → Agent+用户双层决策。

**Source:** discuss-log.md → Iteration 2

---

## Iteration 3 — 2026-03-26

**Trigger:** 用户追加讨论点 — exp 与 memory 的关系

**Topic:** exp 的本质定位：区分归纳 vs 检索，明确 exp 不等于 memory

---

### 背景问题

大多数 Agent 已在构建自有 memory 体系，外部 RAG 也提供大量信息。如何正确定性 exp，使其与 memory 明确区分，避免混淆？

---

### task / attempt / exp 三层模型

**结论：** 采用三层分离模型，而非 task = exp。

```
task ──► attempt ──► exp
        （可多个）  （可从多个 attempt 汇聚）
```

| 层 | 本质 | 例子 |
|---|---|---|
| **task** | 待解决对象 | "修 parser timezone bug" |
| **attempt** | 某次具体处理经历 | 2026-03-25 Claude 成功；2026-03-26 MiniMax 失败 |
| **exp** | 从 attempt 归纳的可复用模式 | "datetime-parser-boundary-check-first" |

**核心差异：**
- Memory：外部**检索**得到（RAG、预训练）
- Attempt：**经历**得到（实际执行了一次）
- Exp：**归纳**得到（从多个 attempt 提炼出模式）

**提升条件（attempt → exp）：** 满足以下至少两条才提升：
1. 不止一次出现
2. 能跨相似 task 复用
3. 能说清适用条件
4. 有明确的成功/失败证据
5. 能压缩成短规则

---

### exp 与 memory 的边界

| | **Memory** | **Exp** |
|---|---|---|
| 本质 | 世界知识、事实 | 情境知识、"这在那种情况下管用" |
| 来源 | 外部检索（RAG、预训练） | 内部归纳（attempt 提炼） |
| 可靠性假设 | 默认可信 | 默认待验证 |
| 生命周期 | 持久稳定 | 随验证次数升级或降级 |

**关键结论：** RAG 给的任何信息 → memory，不是 exp。exp 必须有 attempt 来源，不接受纯外部信息直接沉淀为 exp。

---

**Conclusion:** exp 的本质是归纳产物而非检索产物，三层模型明确了 exp 的来源边界。exp 不等于 memory，也不等于 task——它是介于具体经历与抽象知识之间的中层概念。

**Source:** discuss-log.md → Iteration 3

---

## Iteration 4 — 2026-03-26

**Trigger:** 用户追问是否还有遗漏问题，并要求按更严格的讨论方式补充边界

**Topic:** exp-system 的实现边界收紧：存储契约、经验 ID、更新责任、冲突处理、样本范围、memory 边界

**Agent recommendation:** 这些问题都值得落文，但当前仍属于实现约束而非阻塞性缺陷；应进入计划阶段时一并作为约束处理

**User decision:** 全部纳入讨论范围，继续补充

**Conclusion:**
- 需要补充 6 个实现边界，但它们不阻塞 `jmf-exp` 的初版定义
- 这些边界应在 Plan 中转化为明确约束或后续项
- 当前 Discuss 仍可收敛到 non-blocking

---

## Iteration 5 — 2026-03-26

**Trigger:** 用户要求把 6 个边界问题定案，并明确希望在本 task 内产出第一个版本的 `jmf-exp`

**Topic:** `jmf-exp` v1 policy selection

**Agent recommendation:** 采用简化稳妥版，先把第一版做出来，再考虑结构化增强或自动化扩展

**User decision:** 选择 A. 简化稳妥版

**Conclusion:**
- 主输出仅保留 Markdown，暂不引入额外索引文件
- ID 采用规则化、可复现的生成方式，优先服务引证与重分级
- 只允许手动触发，不引入任务结束半自动生成
- 冲突处理以批次回顾 + 人工确认裁决
- 先用 racobit Task 3 单样本验证模板可行性
- 严格禁止把外部检索内容直接写成 exp

---

## Iteration 6 — 2026-03-26

**Trigger:** 执行阶段发现仓库中没有 racobit Task 3 的本地材料可直接引用

**Topic:** 样本验证落点调整

**Agent recommendation:** 采用本地代理样本完成第一版验证，并把 racobit 样本作为后续补充验证项

**User decision:** 接受本地代理样本作为 v1 验证替代

**Conclusion:**
- racobit Task 3 样本当前不可用，不应虚构验证结果
- v1 先用当前 task 的讨论与计划产物做模板代理验证
- racobit 样本保留为后续补充验证项
