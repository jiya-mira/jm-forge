# Discuss Log — non-jmf-skill-replanning

**Task ID:** 26
**Created:** 2026-03-26
**Status:** Initial

---

## Iteration 1 — Initial Goal Interpretation

**User Input:** "$jmf-new 考虑对于非jmf-*明明的skill的重新规划和调整。"

**Initial Goal Interpretation (pre-Discuss):**

这个任务大概率是在问：如何系统性地重新规划、调整、甚至可能改名那些**不是 `jmf-*` 前缀**的 skill，使它们与当前 jm-forge 命名体系、分发方式和项目地图保持一致。

可能涉及的对象包括：
- `skill-scaffold`
- `workflow-execute`
- 以及未来可能新增的非 `jmf-*` 内部 skill

**待确认：**
1. 调整目标是“统一改成 `jmf-*`”还是“保留少数内部 skill 作为例外”？
2. 范围是否包含目录名、`name` 字段、manifest、PROJECT-MAP 和文档引用？
3. 是否需要保留向后兼容的旧名别名？

---

*Source: jmf-new skill — initial goal interpretation*

---

## Iteration 2 — 2026-03-26

**Trigger:** 用户补充说明非 `jmf-*` skill 的两个用途：指导后续 jmf 系列 skill 的自举过程，以及指导 jmf 系列 skill 的使用过程

**Topic:** 非 jmf skill 的定位拆分

**Agent recommendation:** 将非 `jmf-*` skill 分成两类处理：
- **install-time/bootstrap helpers**：只在初始化或生成阶段使用，安装后不必长期暴露给普通用户
- **runtime guidance skills**：面向用户使用流程的，优先收敛为 `jmf-*` 或统一入口向导

**User decision:** 待确认

**Conclusion:**
- 自举过程中的 skill 不需要在安装后继续作为用户常驻入口
- 大多数用户只需要安装 `jmf-*` 系列 skill，加一个整体向导即可
- 下一步需要确定是否保留一个非 `jmf-*` 的总向导入口，还是全部迁移到 `jmf-*`

---

## Iteration 3 — 2026-03-26

**Trigger:** 用户追问总向导是否必须以单独 skill 存在，并要求考虑普通模型的能力边界

**Topic:** 总向导形态选择

**Agent recommendation:** 采用“薄入口 skill + 文档索引”的组合，而不是把总向导做成厚重的控制器

**User decision:** 待确认

**Conclusion:**
- 总向导不一定必须是一个大 skill，但最好仍有一个很小的独立入口 skill
- 纯文档入口对普通模型更脆弱，容易漏读或跳过
- 太厚的总向导 skill 会增加推理和执行负担，不利于普通模型稳定使用

---

## Iteration 4 — 2026-03-26

**Trigger:** 用户确认总向导往往不会被直接调用，追问薄入口 skill 是否仍然合适

**Topic:** 总向导是否需要用户直接调用

**Agent recommendation:** 保留一个极薄的 bootstrap/router skill，但不要把它定义为用户日常会主动调用的重技能

**User decision:** 待确认

**Conclusion:**
- 入口 skill 可以主要服务于安装、引导和技能间跳转
- 用户平时不必直接调用它，但它仍能作为稳定入口存在
- 对普通模型来说，这比纯文档入口更可控，也比重型总向导更轻量

---

## Iteration 5 — 2026-03-26

**Trigger:** 用户确认最终边界，只保留 1 个薄入口 skill

**Topic:** 非 `jmf-*` skill 的最终保留数量

**Agent recommendation:** 保留 1 个薄入口 skill，其余运行时技能统一迁移进 `jmf-*`

**User decision:** 只保留 1 个薄入口

**Conclusion:**
- 非 `jmf-*` skill 的最终形态应当压缩到一个极薄的入口/router
- 其余 skill 应统一进入 `jmf-*` 命名体系
- 这个入口 skill 主要用于安装、导航和过渡，不承担复杂业务逻辑

---

## Iteration 6 — 2026-03-26

**Trigger:** Planning 时发现 `skill-scaffold` 仍是非 `jmf-*`，与“只保留 1 个”存在计数口径冲突

**Topic:** 非 `jmf-*` skill 的计数口径与例外类别

**Agent recommendation:** 将 `skill-scaffold` 明确归类为内部构建工具例外，不计入用户可见/runtime skill 数量；保留 `workflow-execute` 作为唯一薄入口/router

**User decision:** 待确认

**Conclusion:**
- 当前仓库里不可能在短期内把所有非 `jmf-*` 名称都清零
- 更可执行的口径是：用户可见/runtime 的非 `jmf-*` skill 只保留 1 个
- `skill-scaffold` 作为内部构建工具单独例外处理，避免破坏已有自举约定

---

## Iteration 7 — 2026-03-26

**Trigger:** Execute 阶段确认 `workflow-execute` 已被收紧为薄 router，并同步补入项目地图

**Topic:** 最终保留入口与地图同步

**Agent recommendation:** 以 `workflow-execute` 作为唯一保留的非 `jmf-*` runtime/router entry，同时把 `skill-scaffold` 继续视为内部构建助手例外

**User decision:** 采纳

**Conclusion:**
- `workflow-execute` 不是主工作流引擎，而是薄 router
- `skill-scaffold` 继续保留为内部构建工具，不计入 runtime/router 概念
- 项目地图、AGENTS.md 与 skill 文件保持一致，避免后续再出现命名/职责漂移
