# Plan — resource-map-project-map-scan-persist-optimization

**Date:** 2026-03-27
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Define-map-recording-contract

**Action:** 固化 map 记录契约，明确 `project-map` 的 tree+graph 分层与 `.workspace` 边界。

**Approach:**
- 明确 tree 层记录什么（项目本体层级/模块归属/导航入口）。
- 明确 graph 层记录什么（引用/依赖/实现关系）。
- 明确边界：`.workspace` 仅作为 workflow 运行工件，不进入 `project-map` 主体记录。
- 定义 tree 层“可穿透最小节点模型”：每层仅记录下一层的基础信息与跳转指针，不做全量详情复制。
  - 最小字段：`id`, `name`, `type`, `path`, `summary`, `children_ids`, `doc_ref`
  - 规则：`summary` 保持一行；`children_ids` 必须可解析到真实节点；详情下沉到叶子或专用 detail 文件。

**Checkpoint:** `map-contract-defined`
- tree/graph 职责和字段边界明确。
- `.workspace` 出主记录规则可执行。
- tree 层“最小摘要+指针”规则明确，可支持层级穿透检索。

---

### Step 2: Introduce-skill-local-map-templates

**Action:** 在相关 skill 下引入模板，作为 map 产物的标准写入骨架（模板跟着 skill 走）。

**Approach:**
- 在 `skills/jmf-init/templates/` 增加 `project-map` tree/graph/index 模板。
- 在 `skills/jmf-sync/templates/` 增加与增量更新相关的 map 模板。
- 在 `skills/jmf-resource/templates/` 增加轻量 `resource-map` 模板。
- 在 `skills/jmf-new/templates/` 补充对 map 初始化/引用的模板入口说明（如需要）。

**Checkpoint:** `skill-local-templates-ready`
- 相关 skill 均具备可复用模板，结构一致。
- 模板字段覆盖 Discuss 定义的核心契约。

---

### Step 3: Wire-templates-into-project-map-flow

**Action:** 将模板接入 `project-map` 的扫描与落盘流程，确保输出遵循分层模型。

**Approach:**
- 用模板驱动 `project-map` 初次生成和同步更新路径。
- 清理当前“单处承载过多信息”的写法，改为分层输出。
- 保留必要兼容引用，避免历史导航断裂。
- 在 tree 各层模板中实现“下一层最小摘要+指针”输出，并验证可逐层穿透。

**Checkpoint:** `project-map-template-driven`
- `project-map` 输出符合 tree+graph 分层。
- 不再混入 `.workspace` 主体运行态记录。
- 从任意上层节点可通过 `children_ids/doc_ref` 穿透到下层节点详情。

---

### Step 4: Wire-templates-into-resource-map-flow

**Action:** 将模板接入 `resource-map` 读写流程，落地轻量化结构。

**Approach:**
- 以模板约束资源条目与基础关联字段。
- 只借鉴 `project-map` 的分层设计思想，避免复制其复杂 graph 语义。
- 不建立对 `project-map` 的结构依赖；`resource-map` 可独立演进与维护。

**Checkpoint:** `resource-map-template-driven`
- `resource-map` 结构轻量且表达完整。
- 与 `project-map` 保持薄关系（设计思想借鉴），无强耦合字段或流程依赖。

---

### Step 5: Reconcile-docs-and-verify-consistency

**Action:** 同步文档契约并完成“功能+一致性”验收。

**Approach:**
- 更新相关技能文档与导航说明，使其与模板化流程一致。
- 在 `.workspace/project-map/INDEX.md` 与 `.workspace/resource-map/INDEX.md` 落盘同一份“Map Boundary Charter”（边界宪章）核心定义。
- 在 `AGENTS.md` 增加该宪章的引用入口，作为后续 map 相关任务的默认约束。
- 验证 map 边界、字段、路径、交叉引用一致性。
- 验证 tree 层穿透检索能力：随机抽样上层节点，确认可到达下层节点与详情文件。
- 汇总证据，支持后续 `execute.md` 与 `summary.md`。

**Checkpoint:** `functional-consistency-passed`
- Discuss 的 4 条验收标准全部满足。
- “模板跟 skill 走”在文档与产物上均可复现。
- Map Boundary Charter 在 project-map/resource-map/AGENTS 三处定义一致，无互相冲突。

---

## Dependencies

- Step 1 是 Step 2~5 的语义前置
- Step 2 完成后才能执行 Step 3/4（模板先行）
- Step 3 与 Step 4 可并行
- Step 5 依赖 Step 3/4 结果

## Tracking

| Assumption | Risk |
|-----------|------|
| 模板化能显著减少记录模式漂移 | Low — 需要保证模板字段与实现同步演进 |
| 模板随 skill 管理可提升维护一致性 | Medium — 多 skill 同步改动时需严格对齐 |
| resource-map 可独立于 project-map 演进 | Low — 仅保留设计思想层面的借鉴即可 |

## Execution Order

parallel with dependencies noted
