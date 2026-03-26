# discuss.md

**Source:** discuss-log.md

---

## Goal

创建统一的安装脚本，实现一键为多个 Agent 安装/同步 Workspace Skills，入口单一，支持交互式选择。脚本可自我迭代（更新本项目自身技能）作为主要验证方案。

## Boundary

### In Scope
- 单一入口脚本（`scripts/install-workspaces-skills.py`）
- 元技能源目录：`skills/`（所有 jm-forge 技能的原始来源）
- 技能分类（基于命名规则）：
  - **发布技能**（默认安装）：`jm-forge:*` 命名的技能（动态检测，自动包含未来新增）
  - **开发技能**（默认不安装）：非 `jm-forge:*` 命名的技能
- 安装目标：`.claude/skills/`, `.gemini/skills/`, `.agents/skills/`
- 使用复制（cp）同步：灵活支持用户选择配置单一 Agent
- 幂等性：重复执行安全（检测已存在则跳过）
- 跨平台：Linux, macOS, Windows（通过 uvx）
- 交互式选择：通过 questionary 实现友好的 uvx 交互
- 非交互模式：支持 `--all`, `--agents`, `--include-dev` 参数
- 自我迭代支持：脚本可更新本项目自身的技能（主要验证方案）

### Out of Scope
- User-level 或 System-level 安装
- Agent 本身安装（假设 Agent 已存在）

## Assumptions

1. 用户已在环境中安装 uv（`curl -LsSf https://astral.sh/uv/install.sh | sh`）
2. `skills/` 为元技能源目录（需要从 `.claude/skills/` 迁移所有技能）
3. 各 Agent Workspace Skills 使用复制同步（而非 symlink，灵活支持单一 Agent 配置）
4. 交互式模式作为默认运行方式
5. jm-forge 命名规则稳定：`jm-forge:*` 为发布技能，其他为开发技能

## Acceptance Criteria

1. 入口脚本：`scripts/install-workspaces-skills.py` 可通过 `uvx` 执行
2. 元技能源：`skills/` 包含所有 jm-forge 技能
3. 安装目标：支持 `.claude/skills/`, `.gemini/skills/`, `.agents/skills/`
4. 幂等性：重复执行不会重复创建或报错
5. 跨平台：Linux, macOS, Windows 均可用 uvx 运行
6. 交互式：用户可通过 questionary 交互选择目标 Agent
7. 自我迭代：脚本可更新本项目自身的技能

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | 元技能源目录具体位置 | Non-blocking | **Resolved**: `skills/` |
| 2 | 交互式实现方式 | Non-blocking | **Resolved**: questionary |
| 3 | 自我迭代验证方案 | Non-blocking | **Resolved**: 脚本可更新本项目技能 |

## Key Decisions

1. **Entry Point:** `scripts/install-workspaces-skills.py`（单一入口）
2. **Execution:** `uvx scripts/install-workspaces-skills.py`（跨平台）
3. **Meta-Skill Source:** `skills/`（元技能源目录）
4. **Published Skills (default):** `jm-forge:*` 命名的技能（动态检测，自动包含未来新增）
5. **Dev Skills (opt-in):** 非 `jm-forge:*` 命名的技能
6. **Installation Targets:** `.claude/skills/`, `.gemini/skills/`, `.agents/skills/`
7. **Mode:** 双模式支持：交互式（questionary）+ 非交互式（CLI 参数）
8. **Idempotency:** 已存在则跳过，不报错
9. **Sync Method:** 复制（cp）而非符号链接
10. **Self-Iteration:** 支持更新本项目自身技能（主要验证方案）
