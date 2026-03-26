# Plan — fix-missing-and-untracked-after-restructure

**Date:** 2026-03-27
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Freeze-source-contract

**Action:** 固化任务真源契约，确保任务状态与存在性查询统一基于 `.workspace/tasks/INDEX.md`。

**Approach:**
- 扫描 `jmf-*` 技能与 `AGENTS.md` 中的真源引用，识别仍指向 legacy registry 的位置。
- 更新技能与导航文档中的契约表述，统一状态字段与 `StateMark` 约束。
- 保留 legacy 兼容语义，但不再作为运行时真源。

**Checkpoint:** `source-contract-unified`
- `skills/` 与 `AGENTS.md` 中不再存在将 `TASK-REGISTRY.md` 作为当前真源的描述。
- 任务状态流转关键技能（`jmf-new/discuss/plan/execute/list/status/auto/abandon`）均明确读取/更新 `.workspace/tasks/INDEX.md`。

---

### Step 2: Repair-tracking-artifacts

**Action:** 修补目录重构后缺失或跟踪断裂的任务索引与任务产物。

**Approach:**
- 对 `tasks/INDEX.md` 按 v2 规范补齐字段（`StateMark`/`Dependon`/`Notes`）并补录缺失任务行。
- 对 #31 的 phase 产物链路进行补齐（`discuss.md`、`plan.md`、后续 `execute.md`/`summary.md`）。
- 对必要模板进行更新，避免新任务继续写入 legacy 模式。

**Checkpoint:** `tracking-artifacts-repaired`
- `tasks/INDEX.md` 可独立承载任务跟踪信息，不依赖 legacy registry。
- #31 目录产物完整且与索引状态一致。

---

### Step 3: Migrate-legacy-references-safely

**Action:** 在历史任务文档中补充 legacy→INDEX 映射说明，保证可追溯与可读性。

**Approach:**
- 批量处理 `.workspace/tasks/**/*.md` 的历史引用，将 `TASK-REGISTRY.md` 标记为 legacy 映射。
- 不改写历史决策事实，仅做兼容注释迁移。
- 抽样检查关键历史任务，确认语义未破坏。

**Checkpoint:** `legacy-mapping-visible`
- 历史文档中的 legacy 引用可被读者直接映射到当前真源。
- 抽样检查通过，无明显语义歧义。

---

### Step 4: Run-high-standard-regression

**Action:** 对本次修复执行高标准回归验证并形成可执行结论。

**Approach:**
- 执行契约扫描：真源引用、状态字段、关键路径可达性。
- 执行一致性检查：`INDEX` 状态、任务目录文件、phase 文档链路一致。
- 形成执行证据，作为 `execute.md` 与 `summary.md` 的输入。

**Checkpoint:** `regression-passed`
- 关键扫描命令结果符合预期（无活跃旧真源引用、状态与目录一致）。
- 可复述为“后续任务默认按 INDEX 真源运行”的明确操作规则。

---

## Dependencies

- Step 1 → Step 2 → Step 3 → Step 4（顺序依赖）
- Step 3 可在 Step 2 完成后立即执行；Step 4 依赖前三步产物。

## Tracking

| Assumption | Risk |
|-----------|------|
| INDEX v2 字段足以覆盖原 registry 信息密度 | Medium — 历史个别任务可能存在额外元信息丢失风险 |
| 历史文档仅加 legacy 注释不会影响可读性 | Low — 主要风险是文本噪音增加 |
| 中等改动不触发业务层行为回归 | Medium — 需通过高标准回归验证兜底 |

## Execution Order

sequential
