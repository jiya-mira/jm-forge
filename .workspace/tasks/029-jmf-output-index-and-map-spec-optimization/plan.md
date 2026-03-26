# Plan — jmf-output-index-and-map-spec-optimization

**Date:** 2026-03-26
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Baseline-and-Scope-Freezing

**Action:**
盘点并冻结本次改造对象清单，明确“必须改造”的 INDEX/map/引用文件范围。

**Approach:**
- 列出 `.workspace` 下全部 `INDEX` 文件与三类 map (`project-map/resource-map/exp-map`) 相关文件。
- 标记受影响的 `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）`、`skills/*/SKILL.md`、docs/scripts 中路径或规范引用。
- 形成“改造目标清单 + 验收清单（人工核对版）”。

**Checkpoint:** `scope-frozen`
- 改造目标清单完整，覆盖 Discuss In scope 中全部对象。
- 人工核对清单已成文，后续逐项勾选可追踪。

---

### Step 2: Define-Index-Writing-Spec

**Action:**
制定 INDEX 编写规范（规则清单 + 示例），强调“说明管理范围内容梗概”与“目录类型差异化粒度”。

**Approach:**
- 定义 INDEX 的必填字段/建议字段、摘要长度建议、目录与文件梗概写法。
- 给出至少两类示例：
  - 根级（如 `.workspace/INDEX`）极简写法
  - task 目录级更具体写法
- 约束更新规则：新增/删除目录或关键文件时何时更新 INDEX。

**Checkpoint:** `index-spec-ready`
- 规则清单可直接执行，无歧义。
- 示例覆盖“极简”和“具体”两档粒度。

---

### Step 3: Define-Map-Cascade-Spec-Initial

**Action:**
制定 map 系列编写规范，并完成 `project-map`、`resource-map` 级联支撑的初步设计说明。

**Approach:**
- 统一 map 内部关键元素命名与关系表达方式（节点、关系、索引入口）。
- 明确“级联初步实现”范围：只做可落地的基础级联，不进入深度机制。
- 保持 `exp-map` 同步到统一规范，但不扩展复杂级联细节。

**Checkpoint:** `map-spec-ready`
- `project-map/resource-map` 的初步级联规则与边界可被明确验证。
- 明确记录“后续单独话题”范围，避免本任务过度扩张。

---

### Step 4: Full-Migration-of-Existing-Artifacts

**Action:**
按新规范完成存量产物全量改造（INDEX + map + 受影响引用）。

**Approach:**
- 先改规范文档，再改目标文件，最后改引用链，避免中途语义漂移。
- 对 `.workspace` 全部 INDEX 执行一致化改写，保持各目录粒度匹配。
- 对 map 系列执行结构与说明更新，落地“级联初步实现”内容。

**Checkpoint:** `migration-complete`
- 清单中的全部对象均已改造，无遗漏项。
- 变更后文件内容与规范逐条对应。

---

### Step 5: Manual-Verification-and-Closure

**Action:**
执行人工逐项检查并形成验收记录（不使用脚本自动校验）。

**Approach:**
- 逐条核对 Step 1 的人工验收清单：INDEX 梗概完整性、粒度正确性、map 初步级联支撑、引用可达性。
- 对关键入口进行人工导航验证（从 INDEX 到目录内容、从 map 到相关文件）。
- 记录未覆盖项或风险项，作为后续任务输入。

**Checkpoint:** `manual-verification-passed`
- 无关键路径/引用断裂。
- INDEX 与 map 改造符合 Discuss 的 5 条 Acceptance Criteria。

---

## Dependencies

- Step 2 依赖 Step 1
- Step 3 依赖 Step 1
- Step 4 依赖 Step 2 与 Step 3
- Step 5 依赖 Step 4

## Tracking

| Assumption | Risk |
|-----------|------|
| 不保留旧规范兼容层，统一硬切新规范 | Medium — 旧引用遗漏会直接暴露为断链 |
| `.workspace` 下 INDEX 粒度可按目录类型统一约束 | Low — 规则清晰且可通过示例约束 |
| map 级联仅做初步实现可控制复杂度 | Medium — 边界定义不清会引发 scope creep |
| 人工逐项校验可替代脚本校验 | Medium — 需严格执行清单，避免漏检 |

## Execution Order

sequential
