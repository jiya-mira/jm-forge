# Summary — fix-missing-and-untracked-after-restructure

**Task ID:** 31
**Date:** 2026-03-27
**Status:** Completed

---

## Goal
修复目录结构大规模调整后，任务跟踪链路中的缺失与失真问题，恢复任务真源、状态流转和历史可追溯的一致性。

## Changes
- 将任务真源契约统一到 `.workspace/tasks/INDEX.md`，并同步关键 `jmf-*` 技能与 `AGENTS.md`。
- 升级并固化 `tasks/INDEX.md` v2 字段规范（含 `StateMark`、`Dependon`、`Notes`），补齐 task `030/031` 记录。
- 完成历史任务文档中的 legacy 映射标注，使旧 `TASK-REGISTRY.md` 引用可直接映射到当前真源。
- 完成 #31 的阶段产物闭环：`discuss.md`、`plan.md`、`execute.md`、`summary.md`。

## Verification
- `rg -n "TASK-REGISTRY\\.md" skills AGENTS.md -S` 无匹配，确认无活跃旧真源引用。
- `INDEX.md` 结构与 task `031` 状态一致（`Pending -> Active -> Completed`）。
- legacy 映射覆盖检查显示 22 处历史文档引用已迁移为兼容标注。
- #31 目录关键 phase 文件存在且内容完整。

## Risks / Follow-ups
- 历史文档中的 legacy 标注提升了兼容性，但文本噪音略增；如需更简洁可另开任务做“头部统一迁移注释”收敛。
- 可后续增加自动化校验脚本，替代手工回归扫描。
