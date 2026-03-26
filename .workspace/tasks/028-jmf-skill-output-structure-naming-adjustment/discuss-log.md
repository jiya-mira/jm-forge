# Discuss Log - jmf-skill-output-structure-naming-adjustment

**Task ID:** 28
**Created:** 2026-03-26
**Status:** Initial

---

## Iteration 1 - Initial Goal Interpretation

**User Input:** "$jmf-new jmf系列skill的输出产物的目录结构和命名方式调整。"

**Initial Goal Interpretation (pre-Discuss):**

这个任务的核心目标是：系统调整 jmf 系列 skill 的输出产物规范，统一目录结构与命名方式，降低后续维护、检索和跨 skill 协作成本。

可能覆盖的范围包括：
- 产物目录层级约定（例如任务级、阶段级、索引级）
- 文件命名规则（前后缀、语义字段、版本/日期标记）
- 与现有 `.planning/`、`PROJECT-MAP/`、`EXP-MAP/` 的兼容性边界

**待确认：**
1. 本次调整是只定义新规范，还是要求同步改造历史产物？
2. 规范适用范围是全部 `jmf-*` skills，还是先覆盖核心工作流 skills（new/discuss/plan/execute）？
3. 是否要求提供迁移策略（自动迁移脚本或兼容层）以避免破坏现有流程？

---

*Source: jmf-new skill - initial goal interpretation*

---

## Iteration 2 - 2026-03-26

**Trigger:** 用户执行 `$jmf-discuss 28`，进入 Discuss setup

**Topic:** PROJECT-MAP 新鲜度与路径有效性预检查

**Agent recommendation:** 先询问是否运行 `jmf-sync` 修复 map 路径失效，再继续 Discuss 主体

**User decision:** 待确认

**Conclusion:**
- `project.json.lastUpdated=2026-03-26`，时间新鲜
- 检测到 map 中路径 `.planning/templates/` 当前不存在
- 按流程已提示可选执行 `jmf-sync`

## Iteration 3 - 2026-03-26

**Trigger:** 用户回应 PROJECT-MAP 预检查选项

**Topic:** stale map 的处理时机

**Agent recommendation:** 先运行 `jmf-sync` 再继续

**User decision:** 暂不运行，继续 Discuss

**Conclusion:**
- 本次 Discuss 不以 map 同步作为阻塞条件
- 将该问题保留为后续可选维护项

## Iteration 4 - 2026-03-26

**Trigger:** Goal 收敛提问

**Topic:** 目标强度与落地范围

**Agent recommendation:** 制定统一规范并先落地核心工作流 skills

**User decision:** 制定统一规范并落地核心技能

**Conclusion:**
- 任务目标不是纯文档化，也不是一次性全量改造
- 采用“规范定义 + 核心技能先落地”的渐进路径

## Iteration 5 - 2026-03-26

**Trigger:** Boundary 收敛（历史产物处理策略）

**Topic:** 历史产物是否迁移

**Agent recommendation:** 仅新产物生效，历史迁移另开任务

**User decision:** 全量历史产物迁移

**Conclusion:**
- 任务边界显著扩大，包含历史产物统一
- 后续 Plan 需重点控制批量改造风险与回滚策略

## Iteration 6 - 2026-03-26

**Trigger:** Boundary 收敛（适用技能范围）

**Topic:** 覆盖范围

**Agent recommendation:** 先核心 4 个技能，其他后续扩展

**User decision:** 覆盖全部 jmf-* 技能

**Conclusion:**
- 本任务边界覆盖全体 jmf 系列技能
- 需要在 Plan 阶段加入分批执行与一致性校验机制

## Iteration 7 - 2026-03-26

**Trigger:** Assumptions 收敛（兼容性策略）

**Topic:** 是否保持旧产物兼容

**Agent recommendation:** 读兼容保留，写入新规范

**User decision:** 允许破坏兼容，统一切新规范

**Conclusion:**
- 本任务按“硬切换”假设推进，不保留旧命名兼容层
- 需要在 Plan 中加入迁移前预演与回滚点设计

## Iteration 8 - 2026-03-26

**Trigger:** Open Issue #4 收敛

**Topic:** 迁移落地策略

**Agent recommendation:** 自动脚本迁移并先 dry-run 预演

**User decision:** 自动脚本迁移 + dry-run预演

**Conclusion:**
- 迁移策略明确为脚本化执行，且必须先预演
- Open Issue #4 可标记为 non-blocking（已决）

## Iteration 9 - 2026-03-26

**Trigger:** Acceptance Criteria 收敛并结束 Discuss

**Topic:** 验收标准组合

**Agent recommendation:** 规范文档 + 脚本预演 + 全量落地校验

**User decision:** 规范文档+脚本预演+全量落地校验

**Conclusion:**
- Discuss 四要素（Goal/Boundary/Assumptions/Acceptance Criteria）已收敛
- 所有 open issues 已转为 non-blocking
- 任务可从 Discussing 进入 Planning

## Iteration 10 - 2026-03-26

**Trigger:** 用户指出讨论结论偏离真实诉求（"具体要改什么还没讨论"）

**Topic:** 改动对象重新定界

**Agent recommendation:** 先锁定改动对象，再讨论方案

**User decision:** 目录层规范化优先；目录内部文件命名暂不作为本次重点

**Conclusion:**
- 任务核心从“文件命名体系重构”收敛为“目录结构与目录命名规范化”
- 讨论需围绕目录布局而非文档字段细节

## Iteration 11 - 2026-03-26

**Trigger:** 继续收敛归一化范围

**Topic:** 统一目录边界（哪些目录迁入 `.planning`）

**Agent recommendation:** 明确游离目录清单并选择统一布局方案

**User decision:** `EXP-MAP` + `RESOURCE-MAP` + `PROJECT-MAP` 全部迁入 `.planning`；布局选 `B: .planning/project-map|resource-map|exp-map + tasks/`

**Conclusion:**
- ROOT 污染治理范围明确：三类 map 目录全部下沉
- 任务目录将进入 `.planning/tasks/` 聚合管理

## Iteration 12 - 2026-03-26

**Trigger:** 处理剩余 blocking issues（目录命名与迁移节奏）

**Topic:** 任务目录重命名范围与执行节奏

**Agent recommendation:** 保留历史目录名 + 分批迁移

**User decision:** 统一重命名存量任务子目录；迁移分两批执行

**Conclusion:**
- 存量任务目录将纳入统一命名改造
- 执行策略采用分批迁移以降低一次性失败面

## Iteration 13 - 2026-03-26

**Trigger:** 收敛统一命名规则

**Topic:** `.planning/tasks/` 子目录命名格式

**Agent recommendation:** `task-<id>-kebab-case`

**User decision:** `<id>-kebab-case`

**Conclusion:**
- 任务目录最终规则确定为 `<id>-kebab-case`
- Discuss 阶段 blocking issues 已清零，可进入 Plan

## Iteration 14 - 2026-03-26

**Trigger:** 用户指出计划缺少关键项：目录变化将影响相关 skills 内容

**Topic:** 迁移后的 skill 契约同步范围

**Agent recommendation:** 在 Plan 中新增独立大项：盘点并修订所有受目录变更影响的 skills/docs/scripts，附一致性校验

**User decision:** 采纳（由用户反馈直接触发）

**Conclusion:**
- 目录迁移不是纯文件移动，必须同步更新执行契约
- Plan 需要新增“全量受影响技能内容修订”步骤及验证检查点

## Iteration 15 - 2026-03-26

**Trigger:** 用户确认统一目录命名方案

**Topic:** 工作产物根目录命名与提交策略

**Agent recommendation:** 使用隐藏目录并默认不提交

**User decision:** 使用 `.workspace`

**Conclusion:**
- 统一产物根目录确定为 `.workspace`
- 该目录应加入 `.gitignore`，默认不提交以避免污染 ROOT 与仓库历史

## Iteration 16 - 2026-03-26

**Trigger:** 用户补充两个遗漏项（安装期目录认知、索引向导）

**Topic:** 迁移后可用性与低能力模型可导航性

**Agent recommendation:** 将两项纳入主计划必做范围：
1) 安装路径加入目录结构与语义说明（含 `.gitignore` 约束）
2) 为关键目录提供 index 向导文件，降低模型迷失风险

**User decision:** 采纳（由用户反馈直接触发）

**Conclusion:**
- 目录迁移不仅是路径调整，还需完成“认知注入 + 导航锚点”
- Plan 需新增对应步骤、检查点与验收项

## Iteration 17 - 2026-03-26

**Trigger:** 用户纠正安装期策略语气（推荐 vs 强制）

**Topic:** `.workspace` 与 `.gitignore` 的策略级别

**Agent recommendation:** 采用“默认推荐”而非强制：默认建议忽略 `.workspace`，允许用户按项目协作策略覆盖

**User decision:** 采纳

**Conclusion:**
- 目录语义注入应提供默认建议，不应作为硬约束
- 需兼容非 git 项目与需要共享该目录的场景

## Iteration 18 - 2026-03-26

**Trigger:** Execute 阶段发现迁移脚本在 map 目录迁移时的实现缺陷

**Topic:** apply 逻辑先建目标目录导致 map 迁移被跳过

**Agent recommendation:** 修复脚本并补做 map 目录迁移，再继续执行后续步骤

**User decision:** 按执行阶段自解决处理

**Conclusion:**
- 已修复 `scripts/migrate-to-workspace-layout.sh`：`run_apply` 不再预建 map 目标目录
- 已手动完成 `PROJECT-MAP` / `RESOURCE-MAP` / `EXP-MAP` 下沉到 `.workspace/*`
- 执行继续，无需新增 dependon 任务
