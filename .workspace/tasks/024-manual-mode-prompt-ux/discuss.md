# Discuss — manual-mode-prompt-ux

**Date:** 2026-03-25
**Status:** Concluded

---

## Goal

确保在手动/半自动模式下，每次任务回报提及任务时都清晰显示 task ID，方便用户记住和引用。

---

## Boundary

- **In scope:** 所有会产生回报的 skills（jmf-discuss, jmf-plan, jmf-execute, jmf-auto, jmf-status 等），特别是阶段完成总结、阻塞问题提示、checkpoint 报告等场景
- **Out of scope:** 纯自动模式的优化

---

## Assumptions

1. Task ID 是用户引用任务的主要方式
2. 用户是手动/半自动模式下的主要参与者

---

## Acceptance Criteria

1. 阶段完成总结时，必须显示 task ID（如 `Task #24: manual-mode-prompt-ux`）
2. 任何回报中首次提及任务时，附带 ID
3. 格式简洁——ID 清晰可见，但不增加额外噪音

---

## Key Decisions

### Task ID Always Visible

确认 task ID 应该总是带上，特别是在阶段完成总结时。格式简洁看得懂即可，不追求特定格式。

**Source:** discuss-log.md → Iteration 1

---

## Conclusion

本任务聚焦于规范 jm-forge 手动/半自动模式下的回报提示——确保每次提及任务时都附带 ID，解决用户"回头想继续任务但忘了 ID"的痛点。scope 清晰，可以进入 Plan 阶段。

**Source:** discuss-log.md → Iteration 1
