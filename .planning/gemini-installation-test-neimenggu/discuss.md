---
id: 23
---

# Discuss — gemini-installation-test-neimenggu

**Date:** 2026-03-24
**Status:** Concluded

---

## Goal

验证 Gemini 在 oc.ams 服务器上成功安装 jm-forge Workspace Skills。测试采用 README.md 中的引导提示词，让 Gemini 自我引导完成安装。

**Source:** discuss-log.md → Iteration 2

---

## Boundary

- **In scope:**
  - 使用 README.md 中的引导提示词驱动 Gemini 完成安装
  - 验证 jm-forge skills 安装到 `.gemini/skills/` 目录
  - 确认目标目录 `/home/ubuntu/solution/内蒙广聚-20260324` 可用
  - 测试 jm-forge skills 可被 Gemini 正常调用

- **Out of scope:**
  - 修改安装脚本本身
  - Agent 级别配置（假设 Gemini agent 已存在）
  - 在 oc.ams 上安装 uv 或其他依赖

**Source:** discuss-log.md → Iteration 2

---

## Assumptions

1. oc.ams 服务器可达：`ubuntu@144.21.43.180:22`（key 认证）
2. 目标目录已创建：`/home/ubuntu/solution/内蒙广聚-20260324`
3. Gemini agent 已在 oc.ams 运行并可接受提示词
4. 安装目标是 `.gemini/skills/`（而非 `.claude/skills/`）

**Source:** discuss-log.md → Iteration 2

---

## Acceptance Criteria

1. **环境就绪：** 确认 oc.ams 目标目录存在且可写
2. **引导成功：** 使用 README.md 提示词成功引导 Gemini 开始安装
3. **技能安装：** jm-forge skills 安装到 `.gemini/skills/` 目录
4. **命名正确：** skills 采用 `jm-forge:xxx` 命名格式（冒号，非横杠）
5. **功能验证：** 至少一个 jm-forge skill 可被 Gemini 调用

**Source:** discuss-log.md → Iteration 2

---

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | Gemini 会自动复制 .planning 到目标目录 | Non-blocking | 已知行为，记录为观察项 |
| 2 | jm-forge skills 安装后采用旧命名 `jm-forge-XXX` 而非 `jm-forge:xxx` | Yes | 需要修复，参考 task #16 和 #17 的命名规范 |

---

## Key Decisions

1. **安装方式：** 不传输安装脚本，通过 README.md 引导 Gemini 自我安装
2. **验证重点：** 确认 skills 命名格式是否正确（冒号 vs 横杠）
3. **已知问题：** 将 issue #2 作为 blocking 问题记录，需在测试后修复

**Source:** discuss-log.md → Iteration 2

---

## Conclusion

测试目标明确：在 oc.ams 上引导 Gemini 安装 jm-forge skills 并验证功能。主要风险是命名格式问题（横杠 vs 冒号），这是已知的需要修复的问题。

**Next:** 进入 Plan 阶段，创建执行计划。

**Source:** discuss-log.md → Iteration 2
