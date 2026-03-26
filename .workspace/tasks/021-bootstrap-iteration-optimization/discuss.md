# discuss.md

**Source:** discuss-log.md

---

## Goal

优化 jm-forge 系列技能的自举迭代流程，核心变化：
- **开发在元技能源** (`skills/`)
- **发布走安装脚本** (install-workspaces-skills.py)
- **Bootstrap 后自动调用 install**

## Boundary

### In Scope
- Bootstrap 流程优化
- skill-scaffold 更新
- AGENTS.md 模板更新
- 开发/发布流程分离
- iteration norms 应用到自举流程

### Out of Scope
- 不改变现有技能的功能逻辑
- 不重新设计 task lifecycle

## Assumptions

1. `skills/` 是元技能源（开发目录）
2. `.claude/skills/` 是本地安装目标
3. install 脚本是发布到其他 Agent 的唯一途径
4. 开发直接在 `skills/` 进行，不再有 `.claude/skills/` 副本

## Acceptance Criteria

1. Bootstrap 后自动调用 install 脚本
2. AGENTS.md 模板更新，移除过时内容
3. skill-scaffold 更新，反映新的开发/发布流程
4. 开发流程清晰：开发在 `skills/` → install 脚本发布

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | Bootstrap 后自动调用 install | Non-blocking | **Resolved (Option B)**: 自动调用 |
| 2 | 开发/发布流程分离 | Non-blocking | **Resolved (Option A reversed)**: 开发在 skills/，发布走脚本 |
| 3 | AGENTS.md 模板更新 | Non-blocking | **Resolved (Option A)**: 更新模板 |
| 4 | skill-scaffold 更新 | Non-blocking | 反映新的开发/发布流程 |

## Key Decisions

### 1. 开发/发布流程分离（反向）

| 组件 | 角色 |
|------|------|
| `skills/` | **元技能源**（开发目录） |
| `.claude/skills/` | 本地安装目标（通过 install 脚本） |
| `.gemini/skills/` | Gemini 安装目标 |
| `.agents/skills/` | Codex 安装目标 |

**开发流程：**
```
直接编辑 skills/jm-forge:*/SKILL.md
    ↓
运行 install 脚本发布到各目标
```

**不再有 `.claude/skills/` 副本开发模式。**

### 2. Bootstrap 后自动调用 install

jm-forge:bootstrap 完成后：
```bash
uv run scripts/install-workspaces-skills.py --all
```

### 3. AGENTS.md 模板简化

移除过时内容，简化模板结构。

### 4. iteration norms 应用

自举流程本身也要遵循 iteration norms：
- Append-only
- Soft Boundaries
- State as position marker
