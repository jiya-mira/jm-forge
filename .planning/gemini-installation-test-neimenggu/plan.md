# Plan — gemini-installation-test-neimenggu

**Date:** 2026-03-24
**Source:** Discuss output (discuss.md)

---

## Steps

### Step 1: Verify environment and prepare Gemini prompt

**Action:** 检查 oc.ams 环境，通过 SSH 连接并准备引导 Gemini 的提示词

**Approach:**
- SSH 到 oc.ams 确认目标目录状态
- 构造基于 README.md 的引导提示词
- 确认 Gemini agent 已运行或可启动

**Checkpoint:** `env-ready`
- oc.ams 目标目录 `/home/ubuntu/solution/内蒙广聚-20260324` 可访问
- 引导提示词已准备就绪

---

### Step 2: 引导 Gemini 执行安装

**Action:** 通过提示词驱动 Gemini 执行 jm-forge skills 安装

**Approach:**
- 使用 README.md 中的引导提示词模板：
  ```
  Clone https://github.com/jiya-mira/jm-forge to a temporary directory.
  This is a skills-based Agent scaffolding framework with a Discuss→Plan→Execute
  workflow. Read scripts/install-workspaces-skills.py to understand how it
  installs skills to platform-specific directories (.claude/skills/,
  .gemini/skills/, .agents/skills/). Then copy the skill directories you
  need from the temporary clone into your actual workspace's skill directory.
  ```
- 目标：让 Gemini 将 jm-forge skills 安装到 `/home/ubuntu/solution/内蒙广聚-20260324/.gemini/skills/`

**Checkpoint:** `gemini-install-started`
- Gemini 接受了提示词并开始执行
- Gemini 克隆了 jm-forge 仓库或开始安装流程

---

### Step 3: 验证安装结果

**Action:** 检查 Gemini 是否成功安装了 jm-forge skills

**Approach:**
- SSH 到 oc.ams 检查目标目录
- 验证 `.gemini/skills/` 目录是否存在
- 列出已安装的 skills 文件

**Checkpoint:** `skills-installed`
- `.gemini/skills/` 目录存在
- jm-forge 相关 skills 已复制到该目录
- skills 文件可读

---

### Step 4: 验证命名格式（关键检查点）

**Action:** 检查安装的 skills 是否采用正确的命名格式 `jm-forge:xxx`（冒号）

**Approach:**
- 列出 `.gemini/skills/` 下的所有 skills
- 对比命名格式：
  - 正确格式：`jm-forge:new`, `jm-forge:discuss`
  - 错误格式（历史遗留）：`jm-forge-new`, `jm-forge-discuss`

**Checkpoint:** `naming-correct`
- skills 采用 `jm-forge:xxx` 命名格式（冒号）
- **如果发现横杠格式（`jm-forge-xxx`），记录为 blocking issue，标记任务需要修复**

---

### Step 5: 验证技能功能性

**Action:** 测试 jm-forge skills 可被 Gemini 调用

**Approach:**
- 让 Gemini 执行一个简单的 jm-forge 命令（如 `jm-forge:list`）
- 验证技能可被正确识别和执行

**Checkpoint:** `skill-functional`
- Gemini 能识别 jm-forge:xxx skills
- 技能可被调用（至少一个）

---

### Step 6: 记录观察和结论

**Action:** 整理测试结果，记录发现的问题

**Approach:**
- 记录所有观察项（尤其是 .planning 复制行为）
- 如果有 blocking issue，更新 discuss.md 和 TASK-REGISTRY
- 提供最终测试报告

**Checkpoint:** `report-complete`
- 测试报告包含所有验收标准的状态
- Blocking issues 已记录

---

## Dependencies

Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6
（顺序执行，每步依赖前一步完成）

---

## Tracking

| Assumption | Risk | Mitigation |
|-----------|------|------------|
| Gemini agent 可在 oc.ams 上通过提示词驱动 | Medium | 如果无法远程交互，可能需要 SSH 会话 |
| 目标目录有足够空间和权限 | Low | Step 1 会验证 |
| Gemini 能理解并执行 README.md 引导词 | Low | README 提示词已设计为简洁明确 |

---

## Execution Order

**Sequential** — 每个步骤依赖前一步的结果，需要顺序执行。

**预计流程：**
1. SSH 到 oc.ams → 准备环境
2. 触发 Gemini 安装流程
3. 等待安装完成
4. 验证结果（可能需要多次 SSH 检查）
5. 报告

---

## Known Blocking Issue

**Issue #2 (from discuss):** jm-forge skills 命名格式错误

- **问题：** 安装后 skills 采用 `jm-forge-XXX`（横杠）而非 `jm-forge:xxx`（冒号）
- **来源：** task #16, #17 的命名规范修复未完全应用到 skills 安装脚本
- **处理：** 如果 Step 4 发现此问题，标记为 blocking，完成报告后需要创建新任务修复

