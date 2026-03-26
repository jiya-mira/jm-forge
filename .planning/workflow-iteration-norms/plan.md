# plan.md

**Source:** discuss.md

---

## Goal

将迭代规范（Soft Phase Boundaries + Append-Only）内化到 `jm-forge:discuss`, `jm-forge:plan`, `jm-forge:execute` 三个技能的 SKILL.md 中。

---

## Step Decomposition

### Step 1: 更新 `jm-forge:discuss` SKILL.md

**Action:**
- 在 `## Notes` 之前添加 `## Iteration Norms` 章节
- 内容包括：
  - Append-only 文档策略
  - Soft Phase Boundaries 说明
  - Iteration 记录格式

**Checkpoint:**
- `jm-forge:discuss/SKILL.md` 包含 `## Iteration Norms` 章节
- 章节内容涵盖 append-only + soft boundaries

---

### Step 2: 更新 `jm-forge:plan` SKILL.md

**Action:**
- 更新 `## Behavior` 中的 `### 3. Blocking Issues During Planning`
- 改为 Soft Boundaries 模式：
  - 发现新问题 → 追加 Iteration 到 discuss-log.md
  - 不强制停止或 spawn Dependon（小问题直接处理）
  - 仅在真正需要独立子任务时才 spawn Dependon
- 在 `## Notes` 之前添加 `## Iteration Norms` 章节

**Checkpoint:**
- `jm-forge:plan/SKILL.md` 的 blocking issues 处理改为 Soft Boundaries
- 包含 `## Iteration Norms` 章节

---

### Step 3: 更新 `jm-forge:execute` SKILL.md

**Action:**
- 更新 `## Behavior` 中的 `### 4. Failure Handling`
- 改为迭代模式：
  - Checkpoint 失败 → 先 self-resolve
  - 无法解决 → 追加 Iteration 到 discuss-log.md，更新 execute.md
  - 不视为"失败"，视为"迭代"
  - 不强制 spawn Dependon 或 set state to Failed
- 在 `## Notes` 之前添加 `## Iteration Norms` 章节

**Checkpoint:**
- `jm-forge:execute/SKILL.md` 的 failure handling 改为迭代模式
- 包含 `## Iteration Norms` 章节

---

### Step 4: 验证更新

**Action:**
- 检查三个技能的 SKILL.md 都包含 `## Iteration Norms`
- 检查内容一致性

**Checkpoint:**
- 三个文件都存在且包含 Iteration Norms

---

### Step 5: 同步到 `skills/` 元技能源

**Action:**
- 将更新后的 SKILL.md 同步到 `skills/` 目录（用于发布）

**Checkpoint:**
- `skills/jm-forge:discuss/SKILL.md` 与 `.claude/skills/jm-forge:discuss/SKILL.md` 一致
- `skills/jm-forge:plan/SKILL.md` 与 `.claude/skills/jm-forge:plan/SKILL.md` 一致
- `skills/jm-forge:execute/SKILL.md` 与 `.claude/skills/jm-forge:execute/SKILL.md` 一致

---

### Step 6: 提交版本控制

**Action:**
- 将更新的 SKILL.md 添加到 git

**Checkpoint:**
- `git status` 显示更新的文件已 staged

---

## Dependencies

- Step 2 depends on Step 1
- Step 3 independent (can parallel with Step 2)
- Step 4 depends on Step 1, 2, 3
- Step 5 depends on Step 4
- Step 6 depends on Step 5

**Total:** 6 steps

---

## Tracking

### Assumptions

1. `skills/` 作为元技能源，用于发布
2. `.claude/skills/` 作为当前工作副本
3. 同步后两者保持一致

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| 忘记同步到 skills/ | Low | Medium | Step 5 明确同步 |
| 不同步导致发布不一致 | Low | High | Step 4 验证一致性 |

---

## Verification

| Acceptance Criteria | Verification Method |
|---------------------|---------------------|
| jm-forge:discuss 更新 | SKILL.md 包含 Iteration Norms |
| jm-forge:plan 更新 | SKILL.md 反映 Soft Boundaries |
| jm-forge:execute 更新 | SKILL.md 反映迭代失败处理 |
| 同步到 skills/ | 文件一致性验证 |
| git staged | git status 显示已 staged |
