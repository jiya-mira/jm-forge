# Tasks Index

Directory index for `.workspace/tasks/`.

## Managed Files
- `INDEX.md`: routing entry and normalized task catalog (source of truth).

## Managed Directories
- `<id>-<task-name>/`: one task directory per workflow task.

## Task Catalog Spec (v2)

- Required columns: `ID | Directory | State | StateMark | Dependon | One-line Summary | Notes`
- `Dependon` uses task ID or `-` if none
- `Notes` stores compact metadata that was historically carried by `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）` (for example, blocked reason, manual override, migration notes)
- StateMark mapping:
  - `New` = `🆕`
  - `Discussing` = `💬`
  - `Planning` = `📋`
  - `Pending` = `⏳`
  - `Active` = `🔄`
  - `Completed` = `✅`
  - `Failed` = `❌`
  - `Abandoned` = `🚫`

## Task Catalog

| ID | Directory | State | StateMark | Dependon | One-line Summary | Notes |
|----|-----------|-------|-----------|----------|------------------|-------|
| 001 | `001-workflow-framework/` | Completed | ✅ | - | 定义 Discuss→Plan→Execute 工作流框架。 | - |
| 002 | `002-jm-forge-bootstrap/` | Completed | ✅ | - | 建立 jm-forge 的基础引导流程。 | - |
| 004 | `004-skill-scaffold-v2/` | Completed | ✅ | - | 升级 skill-scaffold 的决策与模板流程。 | - |
| 005 | `005-doc-relationship-graph/` | Completed | ✅ | - | 建立文档引用关系约定。 | - |
| 006 | `006-task-concurrency-control/` | New | 🆕 | - | 处理多任务并发管理冲突。 | - |
| 007 | `007-skill-naming-overhaul/` | Completed | ✅ | - | 重构技能命名以提升可用性。 | - |
| 008 | `008-jm-forge-init/` | Completed | ✅ | - | 初始化项目上下文映射。 | - |
| 009 | `009-jm-forge-init-refresh/` | Completed | ✅ | - | 增强 init 的重跑与增量更新。 | - |
| 010 | `010-external-resources-support/` | Completed | ✅ | - | 支持外部资源并入 map/sync。 | - |
| 011 | `011-resource-map-redesign/` | Completed | ✅ | - | 将资源模型扩展为 RESOURCE-MAP。 | - |
| 012 | `012-resource-auto-discovery/` | Completed | ✅ | - | 自动发现并登记已有资源。 | - |
| 013 | `013-readme-redesign/` | Completed | ✅ | - | 重写 README 的方法与结构。 | - |
| 014 | `014-mvp-release/` | Completed | ✅ | - | 完成 MVP 发布准备与版本标记。 | - |
| 015 | `015-readme-finalize/` | Completed | ✅ | - | 完成 README 收尾与校验。 | - |
| 016 | `016-gemini-project-skill/` | Completed | ✅ | - | 适配 Gemini 的 project 级技能使用。 | - |
| 017 | `017-skill-naming-standardization/` | Completed | ✅ | - | 统一现有与未来 skill 命名规范。 | - |
| 018 | `018-codex-project-skill/` | Completed | ✅ | - | 适配 Codex 的 project 级技能使用。 | - |
| 019 | `019-agent-install-scripts/` | Completed | ✅ | - | 构建多 Agent 通用安装脚本。 | - |
| 020 | `020-workflow-iteration-norms/` | Completed | ✅ | - | 规范工作流迭代与阶段边界。 | - |
| 021 | `021-bootstrap-iteration-optimization/` | Completed | ✅ | - | 优化技能体系自举迭代流程。 | - |
| 022 | `022-analyze-jm-forge-new-skill-ux/` | Completed | ✅ | - | 分析 jmf-new 的 UX 优化方向。 | - |
| 023 | `023-jmf-task-lifecycle/` | Completed | ✅ | - | 优化任务生命周期管理策略。 | - |
| 024 | `024-manual-mode-prompt-ux/` | Completed | ✅ | - | 优化手动/半自动模式提示体验。 | - |
| 025 | `025-exp-system/` | Completed | ✅ | - | 构建经验沉淀体系（EXP）。 | - |
| 026 | `026-non-jmf-skill-replanning/` | Completed | ✅ | - | 重规划非 jmf-* 技能体系。 | - |
| 027 | `027-jmf-exp-racobit-analysis-issues/` | Completed | ✅ | - | 梳理 jmf-exp 在案例分析中的问题。 | - |
| 028 | `028-jmf-skill-output-structure-naming-adjustment/` | Completed | ✅ | - | 调整 jmf 产物目录结构与命名。 | - |
| 029 | `029-jmf-output-index-and-map-spec-optimization/` | Completed | ✅ | - | 优化 INDEX 规范与 map 级联初步实现。 | - |
| 030 | `030-resource-map-project-map-scan-persist-optimization/` | Completed | ✅ | - | 优化 resource-map 与 project-map 的扫描与落盘逻辑。 | Execute+Summary completed 2026-03-27 |
| 031 | `031-fix-missing-and-untracked-after-restructure/` | Completed | ✅ | - | 修正目录重构后文件缺失或跟踪异常问题。 | Execute+Summary completed 2026-03-27 |

## Navigation
1. Find task by ID or summary in the catalog above.
2. Open the task directory.
3. Read phase docs in order: `discuss.md` -> `plan.md` -> `execute.md` -> `summary.md`.

## Update Rule
Update this index when any of the following changes:
- task directories are added/removed/renamed
- task state changes
- task dependency changes (`Dependon`)
- task-level tracking notes change (blockers, manual override, migration notes)
