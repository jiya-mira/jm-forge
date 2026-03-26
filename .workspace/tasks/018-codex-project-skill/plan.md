# plan.md

**Source:** discuss.md

---

## Goal

配置GitHub Codex CLI的Workspace Skills支持，使其与jm-forge现有的Claude Code技能系统完全兼容，共享同一套技能定义。

---

## Step Decomposition

### Step 1: 创建 `.agents/skills/` 目录结构

**Action:**
- 创建 `.agents/skills/` 目录

**Checkpoint:**
- `ls -la .agents/skills/` 返回空目录

---

### Step 2: 同步所有技能到 Codex Workspace

**Action:**
- 遍历 `.claude/skills/` 下的所有技能目录
- 为每个技能在 `.agents/skills/` 下创建符号链接指向原始技能目录

**Command:**
```bash
for skill in .claude/skills/*/; do
  name=$(basename "$skill")
  ln -s "../../.claude/skills/$name" ".agents/skills/$name"
done
```

**Checkpoint:**
- `.agents/skills/` 包含与 `.claude/skills/` 相同数量的技能目录
- 每个条目都是符号链接，指向 `../../.claude/skills/<skill-name>`

---

### Step 3: 验证目录结构符合 Codex CLI 标准

**Action:**
- 检查每个技能目录包含 `SKILL.md`
- 验证 `.agents/skills/` 结构符合 Workspace Skills 规范

**Checkpoint:**
- 每个 `.agents/skills/<skill>/` 下存在 `SKILL.md`
- 目录结构为：
  ```
  .agents/skills/
    jm-forge-new/      → symlink to ../../.claude/skills/jm-forge-new
    jm-forge-discuss/  → symlink to ../../.claude/skills/jm-forge-discuss
    ...
  ```

---

### Step 4: 提交版本控制

**Action:**
- 将 `.agents/skills/` 目录添加到 git
- 创建初始提交

**Checkpoint:**
- `git status .agents/skills/` 显示所有技能链接已 staged
- `.gitignore` 不存在 `.agents/skills/` 条目（如果已有 .gitignore）

---

## Dependencies

- Step 2 depends on Step 1
- Step 3 depends on Step 2
- Step 4 depends on Step 3

**Total:** 4 steps, linear dependency

---

## Tracking

### Assumptions

1. Codex CLI 在项目根目录扫描 `.agents/skills/`
2. 符号链接在版本控制中正常工作（git 保存链接而非目标内容）
3. 所有 `.claude/skills/` 下的技能都有 `SKILL.md`

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Codex CLI 不跟随符号链接 | Low | High | 可改用硬链接或复制（但复制有同步问题） |
| `.agents/` 目录与项目其他配置冲突 | Low | Low | 独立目录，不影响其他功能 |

---

## Verification

| Acceptance Criteria | Verification Method |
|---------------------|---------------------|
| `.agents/skills/` 目录结构遵循 Codex CLI 标准 | 目录结构匹配文档描述 |
| jm-forge 可发现并列出可用 Workspace Skills | `ls .agents/skills/` 返回所有技能 |
| 显式触发激活 | 未来由 Codex CLI 测试验证（`$skill-name`） |
| 技能内容与 `.claude/skills/` 完全一致 | 符号链接保证一致性 |
| 技能可提交版本控制 | `git status` 验证 |
