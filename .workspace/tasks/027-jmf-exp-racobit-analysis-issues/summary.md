# Summary — jmf-exp-racobit-analysis-issues

**Task ID:** 27
**Date:** 2026-03-26
**Status:** Completed

---

## Goal
纠正 `jmf-exp` 的目标偏差，建立项目级 exp 提炼与落盘机制，并在 `jmf-execute` 增加关闭前 summary 强约束。

## Changes
- 重写 `jmf-exp`：支持 Type A/Type B 项目级提炼、历史 summary 缺失兼容、`EXP-MAP` 落盘契约。
- 重写 `jmf-execute`：新增关闭前 `summary.md` 必填与失败阻断关闭规则。
- 新增 `EXP-MAP/INDEX.md` 与 `EXP-MAP/entries/exp-template.md`。
- 完成 Task 27 的 discuss/plan/execute 文档链路。

## Verification
- Checkpoint 1-5 在本仓库内执行并验证通过。
- Checkpoint 6 由用户确认通过（后续若发现问题将通过新 task 跟进）。

## Risks / Follow-ups
- 若真实使用中出现边界案例（例如跨 task 归纳冲突），需新开 task 补充提炼规则和索引更新策略。

