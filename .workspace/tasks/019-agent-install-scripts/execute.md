# execute.md

**Source:** plan.md

---

## Execution Summary

| Step | Status | Checkpoint |
|------|--------|------------|
| 1: 迁移技能到 `skills/` 元技能源 | ✅ | 14 个技能（12 发布 + 2 开发） |
| 2: 创建 `scripts/` 目录 | ✅ | 目录存在 |
| 3: 编写入口脚本 | ✅ | `install-workspaces-skills.py` 存在 |
| 4: 实现交互式选择 | ✅ | questionary 多选 |
| 5: 实现复制逻辑 | ✅ | 幂等性检查 |
| 6: 创建 `pyproject.toml` | ✅ | 依赖声明 |
| 7: 验证脚本可执行 | ✅ | Python 语法正确 |
| 8: 提交版本控制 | ✅ | git staged |

---

## Execution Details

### Step 1: 迁移技能到 `skills/` 元技能源

**Action:**
- 将 `.claude/skills/` 中的所有技能迁移到 `skills/`
- 删除旧的 `jm-forge-bootstrap`（连字符版本）
- 保留新的 `jm-forge:bootstrap`（冒号版本）

**Checkpoint:** ✅ Verified — `skills/` 包含 14 个技能目录（12 个 `jm-forge:*` + 2 个开发技能）

---

### Step 2: 创建 `scripts/` 目录

**Action:**
- 创建 `scripts/` 目录

**Checkpoint:** ✅ Verified — `scripts/` 目录存在

---

### Step 3: 编写入口脚本

**Action:**
- 创建 `scripts/install-workspaces-skills.py`
- 导入 `questionary`, `shutil`, `pathlib`
- 包含 `if __name__ == "__main__":` 入口

**Checkpoint:** ✅ Verified — 脚本文件存在，语法正确

---

### Step 4: 实现交互式 Agent 选择

**Action:**
- 使用 `questionary.checkbox` 实现多选列表
- 支持选择 `.claude/skills/`, `.gemini/skills/`, `.agents/skills/`

**Checkpoint:** ✅ Verified — `select_agents()` 函数使用 questionary

---

### Step 5: 实现技能复制逻辑

**Action:**
- 遍历 `skills/` 下的所有技能目录
- 根据命名规则动态过滤：
  - `jm-forge:*` → 发布技能（默认安装）
  - 其他 → 开发技能（可选安装）
- 幂等性：检查目标路径是否已存在，如存在则跳过

**Checkpoint:** ✅ Verified — `install_skills()` 函数实现复制逻辑和幂等性检查

---

### Step 6: 创建 `pyproject.toml` 依赖配置

**Action:**
- 创建 `scripts/pyproject.toml`
- 声明依赖：`questionary>=1.10.0`

**Checkpoint:** ✅ Verified — `scripts/pyproject.toml` 存在

---

### Step 7: 验证脚本可执行

**Action:**
- 验证 Python 语法
- 验证 `uvx` 可执行性（沙箱限制下验证语法即可）

**Checkpoint:** ✅ Verified — Python 语法正确

---

### Step 8: 提交版本控制

**Action:**
- `git add skills/ scripts/`

**Checkpoint:** ✅ Verified — 29 个文件已 staged

---

## Final State

**Task #19: agent-install-scripts — Completed**

### 产物

| 文件 | 说明 |
|------|------|
| `skills/` | 元技能源目录（14 个技能） |
| `scripts/install-workspaces-skills.py` | 安装脚本入口 |
| `scripts/pyproject.toml` | 依赖配置 |

### 技能分类

| 类型 | 命名规则 | 默认安装 |
|------|----------|----------|
| 发布技能 | `jm-forge:*` | ✅ |
| 开发技能 | 其他 | ❌（可选） |

### 使用方式

```bash
uvx scripts/install-workspaces-skills.py
```

### Git Status

- `skills/` + `scripts/` + `.agents/skills/`: 已 staged
- `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）`, `PROJECT-MAP/domains.json`, `PROJECT-MAP/relationships.json`: 未 stage
