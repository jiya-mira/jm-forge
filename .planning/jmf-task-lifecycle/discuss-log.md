# Discuss Log — jmf-task-lifecycle
# Task ID: 23

> Append-only iteration log. See `discuss.md` for latest consensus.

---

## Iteration 1 — 2026-03-25

**Trigger:** User proposed discussing a new jmf series capability

**Topic:** 任务生命周期管理 — 处理历史无意义task

**Context:**
- 随着项目更迭，出现历史task
- 例子：命名规范调整好几轮，遗留过时的task
- 问题：agent处理时产生困扰，token浪费

**Agent recommendation:** TASK-ARCHIVE方案，在jmf-new/discuss/plan中内置冲突检测

**User decision:** 同意方向，但需明确：冲突是当前task的goal与REGISTRY中任意task的goal冲突；archive前提是旧task已完成；archive需用户确认

**Conclusion:**
- 建立goal冲突检测 + 用户确认archive的机制
- 集成到jmf-new/discuss/plan中
- 在源头避免无效task处理

**Iteration 2 — 2026-03-25**

**Trigger:** 讨论plan时发现原方案太绑定特定skill

**Topic:** 检测时机细化

**Key insight:**
- 不应绑定特定skill
- 应该是：当task的goal发生significant变化时触发检测
- jmf-new形成初版goal、jmf-discuss调整goal时触发
- jmf-plan如goal无变化则不检测

**User decision:** 同意这个方向

**Conclusion:**
- 触发条件：goal发生significant变化
- 规则定义在workflow-framework.md中，各skill引用
- archive沿用Abandoned状态，不新建TASK-ARCHIVE.md

**Status:** Concluded

