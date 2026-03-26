# plan.md

**Source:** discuss.md

---

## Goal

创建统一的安装脚本，实现一键为多个 Agent 安装/同步 Workspace Skills，入口单一，支持交互式选择。脚本可自我迭代（更新本项目自身技能）作为主要验证方案。

---

## Step Decomposition

### Step 1: 迁移技能到 `skills/` 元技能源

**Action:**
- 将 `.claude/skills/` 中的所有技能迁移到 `skills/`
- 技能按命名规则分类：
  - **发布技能**：`jm-forge:*` 命名的技能
  - **开发技能**：非 `jm-forge:*` 命名的技能
- 保留 `manifest.json`（已存在）

**Checkpoint:**
- `ls skills/` 包含所有 14 个技能目录
- 脚本默认只安装 `jm-forge:*` 命名的发布技能（动态检测）

---

### Step 2: 创建 `scripts/` 目录

**Action:**
- 创建 `scripts/` 目录

**Checkpoint:**
- `ls -la scripts/` 返回目录存在

---

### Step 3: 编写 `scripts/install-workspaces-skills.py` 入口脚本

**Action:**
- 创建 Python 脚本，依赖：
  - `questionary`（交互式选择，可选）
  - `argparse`（命令行参数）
  - `shutil`（文件复制）
  - `pathlib`（路径操作）
- 实现双模式：
  1. **交互模式**（默认）：使用 questionary 交互选择
  2. **非交互模式**：支持 `--all`, `--agents`, `--include-dev` 参数
- 功能：
  1. 从 `skills/` 复制技能到选定的目标目录
  2. 幂等性处理（已存在则跳过）
  3. 清晰输出（告知用户每个 Agent 的配置状态）
  4. 自我迭代支持（更新本项目自身技能）

**Checkpoint:**
- `scripts/install-workspaces-skills.py` 文件存在
- 支持 `--help` 参数
- 支持 `--all` 和 `--agents` 参数

---

### Step 4: 实现交互式 Agent 选择

**Action:**
- 使用 questionary 实现多选列表
- 支持的选择：
  - `.claude/skills/` (Claude Code)
  - `.gemini/skills/` (Gemini CLI)
  - `.agents/skills/` (Codex CLI)
- 用户可选择安装到单个或多个目标

**Code Concept:**
```python
import questionary

targets = questionary.checkbox(
    "选择要安装技能的 Agent：",
    choices=[
        questionary.Choice(".claude/skills/ (Claude Code)", ".claude/skills/"),
        questionary.Choice(".gemini/skills/ (Gemini CLI)", ".gemini/skills/"),
        questionary.Choice(".agents/skills/ (Codex CLI)", ".agents/skills/"),
    ]
).ask()
```

**Checkpoint:**
- 脚本运行时显示交互式选择界面
- 用户可选择多个目标

---

### Step 5: 实现技能复制逻辑

**Action:**
- 遍历 `skills/` 下的所有技能目录
- 根据命名规则动态过滤：
  - 默认模式：只安装 `jm-forge:*` 命名的技能（发布技能）
  - 可选模式：用户可选择包含非 `jm-forge:*` 命名的技能（开发技能）
- 复制每个技能目录到选定的目标目录
- 幂等性：检查目标路径是否已存在，如存在则跳过

**Code Concept:**
```python
published_skills = [d for d in skills_dir.iterdir()
                    if d.is_dir() and d.name.startswith("jm-forge:")]
dev_skills = [d for d in skills_dir.iterdir()
               if d.is_dir() and not d.name.startswith("jm-forge:")]
```

**Checkpoint:**
- 默认安装后目标目录只包含 `jm-forge:*` 命名的发布技能
- 重复执行不会报错
- 新增 `jm-forge:xxx` 技能自动被包含

---

### Step 6: 创建 `pyproject.toml` 依赖配置

**Action:**
- 创建 `scripts/pyproject.toml`，声明依赖：
  - `questionary`

**Checkpoint:**
- `scripts/pyproject.toml` 存在且包含 `questionary` 依赖

---

### Step 7: 验证脚本可执行

**Action:**
- 测试 `uvx scripts/install-workspaces-skills.py` 可正常运行
- 验证交互式界面显示正常
- 验证复制逻辑正确

**Checkpoint:**
- `uvx scripts/install-workspaces-skills.py` 无报错退出
- 输出显示选择的 Agent 和复制的技能数量

---

### Step 8: 提交版本控制

**Action:**
- 将 `scripts/` 目录添加到 git
- 创建初始提交

**Checkpoint:**
- `git status scripts/` 显示脚本已 staged

---

## Dependencies

- Step 2 depends on Step 1 (创建 scripts/ 目录)
- Step 3 depends on Step 2
- Step 4 depends on Step 3
- Step 5 depends on Step 4
- Step 6 depends on Step 3 (can parallel)
- Step 7 depends on Step 5 and Step 6
- Step 8 depends on Step 7

**Total:** 8 steps

---

## Tracking

### Assumptions

1. 用户已在环境中安装 uv
2. `skills/` 包含（或将包含）所有待同步的元技能
3. uvx 兼容 Linux, macOS, Windows

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| `skills/` 与 `.claude/skills/` 技能不同步 | Medium | Medium | 定期同步或迁移脚本 |
| questionary 依赖在某些环境不可用 | Low | Low | uvx 自动处理依赖 |

---

## Verification

| Acceptance Criteria | Verification Method |
|---------------------|---------------------|
| 技能迁移完成 | `ls skills/` 包含 14 个技能 |
| 入口脚本可通过 uvx 执行 | `uvx scripts/install-workspaces-skills.py` |
| 默认只安装发布技能 | 目标目录只包含 `jm-forge:*` 命名的技能 |
| 动态检测新技能 | 新增 `jm-forge:xxx` 自动被包含 |
| 安装目标支持三种 Agent | 交互式选择显示所有选项 |
| 幂等性 | 重复执行无报错 |
| 跨平台 | Linux/macOS/Windows 均可用 uvx |
| 交互式选择 | questionary 正常显示 |
| 自我迭代 | 脚本可更新本项目技能 |

---

## Note: 关于 `.claude/skills/` 迁移后的处理

迁移完成后，需要决定：
- 选项 A：清空 `.claude/skills/`，仅保留 `skills/` 作为元技能源
- 选项 B：保持 `.claude/skills/` 不变，由安装脚本负责同步

推荐选项 A，简化架构。
