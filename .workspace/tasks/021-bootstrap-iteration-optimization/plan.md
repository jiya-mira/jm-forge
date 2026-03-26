# plan.md

**Source:** discuss.md

---

## Goal

优化 jm-forge 系列技能的自举迭代流程：
- 开发在元技能源 (`skills/`)
- 发布走安装脚本 (install-workspaces-skills.py)
- Bootstrap 后自动调用 install

---

## Step Decomposition

### Step 1: 更新 `jm-forge:bootstrap` SKILL.md

**Action:**
- 添加 Bootstrap 后自动调用 install 脚本的逻辑：
  ```bash
  uv run scripts/install-workspaces-skills.py --all
  ```
- 更新 AGENTS.md 模板：
  - 移除过时内容（jm-forge:auto 等）
  - 简化模板结构
  - 反映新的开发/发布流程

**Checkpoint:**
- `skills/jm-forge:bootstrap/SKILL.md` 包含自动调用 install
- AGENTS.md 模板反映新流程

---

### Step 2: 更新 `skill-scaffold` SKILL.md

**Action:**
- 更新开发/发布流程说明：
  - `skills/` 是元技能源
  - install 脚本是发布途径
  - 不再有 `.claude/skills/` 副本开发模式
- 更新 Registration 步骤

**Checkpoint:**
- `skills/skill-scaffold/SKILL.md` 反映新流程

---

### Step 3: 验证更新一致性

**Action:**
- 检查 bootstrap 和 skill-scaffold 的更新是否一致
- 检查 AGENTS.md 模板是否完整

**Checkpoint:**
- 两个技能文档一致
- 流程描述清晰

---

### Step 4: 同步到 `.claude/skills/`

**Action:**
- 将更新后的 SKILL.md 同步到 `.claude/skills/`

**Checkpoint:**
- `.claude/skills/jm-forge:bootstrap/SKILL.md` 已更新
- `.claude/skills/skill-scaffold/SKILL.md` 已更新

---

### Step 5: 提交版本控制

**Action:**
- git add 更新的文件

**Checkpoint:**
- `git status` 显示更新的文件已 staged

---

## Dependencies

- Step 2 independent (can parallel with Step 1)
- Step 3 depends on Step 1 and Step 2
- Step 4 depends on Step 3
- Step 5 depends on Step 4

**Total:** 5 steps

---

## Tracking

### Assumptions

1. `skills/` 是元技能源
2. install 脚本路径正确
3. 当前 `.claude/skills/` 作为本地安装目标

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| install 脚本路径问题 | Low | Medium | 验证脚本路径 |
| 文档不同步 | Low | High | Step 3 验证一致性 |

---

## Verification

| Acceptance Criteria | Verification Method |
|---------------------|---------------------|
| Bootstrap 后自动调用 install | 检查 bootstrap SKILL.md |
| AGENTS.md 模板更新 | 检查 bootstrap SKILL.md 内容 |
| skill-scaffold 反映新流程 | 检查 skill-scaffold SKILL.md |
| 文档一致性 | Step 3 验证 |
