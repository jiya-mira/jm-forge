# execute.md

**Source:** plan.md

---

## Execution Summary

| Step | Status | Checkpoint |
|------|--------|------------|
| 1: 更新 jm-forge:discuss | ✅ | 包含 Iteration Norms 章节 |
| 2: 更新 jm-forge:plan | ✅ | Soft Boundaries + Iteration Norms |
| 3: 更新 jm-forge:execute | ✅ | 迭代失败处理 + Iteration Norms |
| 4: 验证更新 | ✅ | 三文件都含 Iteration Norms |
| 5: 同步到 skills/ | ✅ | 文件一致性 |
| 6: 提交版本控制 | ✅ | 6 个文件已 staged |

---

## Execution Details

### Step 1: 更新 `jm-forge:discuss` SKILL.md

- 添加 `## Iteration Norms` 章节
- 内容：Append-Only + Soft Boundaries + Iteration Recording Format

**Checkpoint:** ✅ Verified

---

### Step 2: 更新 `jm-forge:plan` SKILL.md

- 更新 `### 3. Blocking Issues During Planning`
  - 从"强制停止"改为"Soft Boundaries: 追加 Iteration"
- 添加 `## Iteration Norms` 章节

**Checkpoint:** ✅ Verified

---

### Step 3: 更新 `jm-forge:execute` SKILL.md

- 更新 `### 4. Failure Handling`
  - 从"失败→spawn Dependon"改为"迭代→追加 Iteration"
- 添加 `## Iteration Norms` 章节

**Checkpoint:** ✅ Verified

---

### Step 4: 验证更新

```bash
grep -l "Iteration Norms" .claude/skills/jm-forge:*/SKILL.md
# 输出: discuss, plan, execute
```

**Checkpoint:** ✅ Verified — 三个技能都包含 Iteration Norms

---

### Step 5: 同步到 `skills/`

- 将更新的 SKILL.md 同步到 `skills/` 目录
- 确保发布时一致

**Checkpoint:** ✅ Verified

---

### Step 6: 提交版本控制

- git add 更新的 SKILL.md 文件

**Checkpoint:** ✅ Verified — 6 个文件已 staged

---

## Final State

**Task #20: workflow-iteration-norms — Completed**

### 更新的文件

| 文件 | 变更 |
|------|------|
| `.claude/skills/jm-forge:discuss/SKILL.md` | 新增 Iteration Norms |
| `.claude/skills/jm-forge:plan/SKILL.md` | Soft Boundaries + Iteration Norms |
| `.claude/skills/jm-forge:execute/SKILL.md` | 迭代失败处理 + Iteration Norms |
| `skills/jm-forge:discuss/SKILL.md` | 同步更新 |
| `skills/jm-forge:plan/SKILL.md` | 同步更新 |
| `skills/jm-forge:execute/SKILL.md` | 同步更新 |

### 规范内容

| 原则 | 描述 |
|------|------|
| **Append-Only** | 文档只追加，不覆盖 |
| **Soft Boundaries** | 阶段是指导，不强制门禁 |
| **迭代失败处理** | 失败视为迭代，不强制终止 |
| **State as Marker** | State 只标记主位置 |
