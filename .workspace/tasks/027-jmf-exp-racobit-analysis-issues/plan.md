# Plan — jmf-exp-racobit-analysis-issues

**Date:** 2026-03-26
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Audit Current Skill Behavior

**Action:** 盘点 `jmf-exp` 与 `jmf-execute` 当前行为、文档与模板缺口，形成“现状 vs 目标”差异清单。

**Approach:**
- 检查 `skills/jmf-exp/` 与 `.agents/skills/jmf-exp/` 的现有流程定义。
- 检查 `skills/jmf-execute/` 与 `.agents/skills/jmf-execute/` 是否已有 summary 关闭前约束。
- 用一页差异清单固定要改的点，避免执行阶段扩散。

**Checkpoint:** `gap-baseline-locked`
- 明确列出“仅最新 task 总结”与“项目级提炼”之间的差异。
- 明确列出“summary 非强制”与“关闭前强制落盘”之间的差异。

---

### Step 2: Define EXP Artifact Contract

**Action:** 冻结 exp 产物契约，定义目录、索引、单条文档以及路由规则。

**Approach:**
- 定义独立目录（例如 `EXP-MAP/` 或等价命名）与索引文件（如 `index.md`）。
- 定义“一条 exp 一个文档”的命名与索引路由字段。
- 约束 `jmf-exp` 输出必须落盘到该结构，而非仅控制台总结。

**Checkpoint:** `artifact-contract-frozen`
- 目录 + 索引 + 单条文档结构有明确规范。
- 产物结构被标记为硬性要求且可被执行阶段验证。

---

### Step 3: Define Single-EXP Template

**Action:** 制定单条 exp 模板，采用 T1 必填字段并支持可选扩展字段。

**Approach:**
- 固定必填字段：`id`、`title`、`type`、`statement`、`applicability`、`evidence`、`counter_example`、`status`。
- 定义可选扩展区（如 `do`/`dont`、`verification`、`notes`）。
- 在 `jmf-exp` 文档中声明生成策略与字段约束。

**Checkpoint:** `exp-template-ready`
- 模板可直接复制用于生成单条 exp 文档。
- 必填与可选字段边界明确，无歧义。

---

### Step 4: Redesign jmf-exp Extraction Rules

**Action:** 将 `jmf-exp` 提炼规则改为项目级，支持两类来源并兼容 summary 缺失。

**Approach:**
- 规则 A：可独立成立的经验信息可直接提炼。
- 规则 B：跨至少 2 个 task 的共性模式可提炼。
- 当 summary 缺失时，回退使用 discuss/plan/execute 等可用工件进行提炼。

**Checkpoint:** `project-level-extraction-enabled`
- 文档明确声明 A/B 两类来源规则。
- 明确说明 summary 缺失时的兼容回退路径。

---

### Step 5: Enforce Summary Gate in jmf-execute

**Action:** 在 `jmf-execute` 增加“关闭前 summary 必须落盘”的强约束与失败阻断策略。

**Approach:**
- 在关闭流程前插入 summary 生成与落盘步骤。
- 若生成或落盘失败，明确阻断关闭并给出恢复动作。
- 对历史 task 作为兼容例外，仅在 `jmf-exp` 侧处理，不放宽新 task 关闭约束。

**Checkpoint:** `summary-gate-enforced`
- `jmf-execute` 文档/流程中存在关闭前 summary 强制步骤。
- 失败阻断关闭策略可被明确验证。

---

### Step 6: Validate With One Real Task Trace

**Action:** 使用一个真实 task 路径做最小验证，确认规则可执行且产物结构落地。

**Approach:**
- 选取一个有完整工件的新 task 路径，演练 summary -> exp 的链路。
- 检查是否生成索引与单条 exp 文档，并验证路由信息完整。
- 记录已知限制（如历史 task summary 缺失的影响边界）。

**Checkpoint:** `minimal-e2e-validated`
- 至少一条 exp 文档成功落盘并被索引引用。
- 验证记录能证明“新 task 强制 summary + exp 项目级提炼”链路成立。

---

## Dependencies

- Step 1 -> Step 2 -> Step 3 -> Step 4 -> Step 5 -> Step 6
- Step 3 依赖 Step 2（模板字段需落在既定产物契约内）
- Step 6 依赖 Step 4/5（需要提炼规则与 summary gate 都可执行）

## Tracking

| Assumption | Risk |
|-----------|------|
| 现有 skill 目录结构允许同步更新 `.agents/skills/` 与 `skills/` | Medium — 两处文档可能漂移 |
| 历史 task 缺失 summary 是可接受存量问题 | Low — Discuss 已确认兼容策略 |
| 仅改元 skill 不触及其他仓库即可完成目标 | Low — 边界已明确 |
| 新增 exp 目录命名可在仓库内稳定落地 | Medium — 需避免与现有 `PROJECT-MAP` 语义冲突 |

## Execution Order

sequential
