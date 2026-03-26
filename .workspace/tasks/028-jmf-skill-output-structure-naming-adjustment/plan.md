# Plan — jmf-skill-output-structure-naming-adjustment

**Date:** 2026-03-26
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Freeze target layout and rename spec

**Action:** 固化目录目标结构与任务目录命名规则，作为后续迁移唯一准则。

**Approach:**
- 目标目录结构固定为：`.workspace/tasks/`、`.workspace/project-map/`、`.workspace/resource-map/`、`.workspace/exp-map/`
- 任务目录命名规则固定为：`<id>-kebab-case`
- 生成“当前目录 -> 目标目录”映射清单，明确每一项迁移去向

**Checkpoint:** `layout-spec-frozen`
- 目标布局和命名规则在 `plan.md` 中唯一且无歧义
- 迁移映射清单可覆盖现有任务目录和三类 map 目录
- 映射清单可被脚本直接消费

---

### Step 2: Build dry-run migration script

**Action:** 编写迁移脚本并先输出 dry-run 预演结果，不直接改动文件系统。

**Approach:**
- 脚本支持 `--dry-run` 与 `--apply` 两种模式
- dry-run 输出：待创建目录、待移动目录、待更新文件路径、潜在冲突项
- 在 dry-run 阶段检测命名冲突（同 ID、同 slug、目标已存在）并阻断 apply

**Checkpoint:** `dry-run-ready`
- dry-run 可稳定生成完整变更清单
- 冲突检测能提前报错并退出
- apply 前无需人工猜测变更范围

---

### Step 3: Execute batch-1 migration for map directories

**Action:** 执行第一批迁移：将 `PROJECT-MAP`、`RESOURCE-MAP`、`EXP-MAP` 下沉到 `.workspace` 对应目录。

**Approach:**
- 先执行 `--dry-run`，确认 map 目录迁移清单
- 执行 `--apply` 完成 map 目录迁移
- 立即修复仓库内对这三类目录的显式路径引用（文档、脚本、skill 说明）
- 提供 git 策略建议：默认建议将 `.workspace/` 加入 `.gitignore`，但允许按项目协作策略覆盖

**Checkpoint:** `batch1-maps-migrated`
- ROOT 下不再存在上述三类 map 目录
- `.workspace/project-map|resource-map|exp-map/` 均存在且内容完整
- 已知路径引用更新后可被检索命中（无旧路径残留）

---

### Step 4: Execute batch-2 migration for task directories

**Action:** 执行第二批迁移：任务目录迁入 `.workspace/tasks/`，并统一重命名为 `<id>-kebab-case`。

**Approach:**
- 基于 `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）` 构建任务 ID 与目录名映射
- 对历史目录执行规范化重命名与迁移
- 同步修复任务文档内部及仓库内引用到旧任务目录的路径

**Checkpoint:** `batch2-tasks-migrated`
- 任务目录全部位于 `.workspace/tasks/`
- 任务目录全部符合 `<id>-kebab-case`
- 无断链引用（旧任务目录路径不可再被命中）

---

### Step 5: Update all impacted skill contracts and references

**Action:** 全量修订受目录迁移影响的 skills/docs/scripts，确保执行契约与新目录结构一致。

**Approach:**
- 盘点所有包含旧路径的文件（重点：`skills/jmf-*`、`AGENTS.md`、`.planning` 文档、脚本）
- 批量替换并人工复核关键 skill 指令中的路径语义
- 对关键入口 skill（`jmf-new`、`jmf-discuss`、`jmf-plan`、`jmf-execute`、`jmf-sync`、`jmf-status`、`jmf-list`）逐一确认路径示例与行为描述一致

**Checkpoint:** `contracts-updated`
- 不再存在对旧目录根路径（`PROJECT-MAP/`、`RESOURCE-MAP/`、`EXP-MAP/`、旧任务目录位置）的有效引用
- 关键 `jmf-*` skills 的输入/输出路径描述与新布局一致
- 文档与脚本中的路径变更通过抽样执行或静态检索验证

---

### Step 6: Validate workflow integrity and close

**Action:** 对迁移结果进行一致性验证，确保工作流仍可运行。

**Approach:**
- 校验 `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）`、`discuss/plan/execute` 路径引用可达
- 校验 `PROJECT-MAP` 相关路径字段与实际目录一致
- 如需，执行一次 `jmf-sync` 进行地图收尾刷新

**Checkpoint:** `post-migration-verified`
- 主要工作流文档路径均可解析
- `PROJECT-MAP` 不再包含迁移前失效路径
- 本任务验收标准 1-7 均可逐项对照通过

---

### Step 7: Inject install-time directory guidance

**Action:** 在技能安装/初始化链路中加入 `.workspace` 目录结构与语义说明，明确“默认建议 + 可覆盖”的 git 策略。

**Approach:**
- 更新安装提示文档与相关 skill 说明（例如 README 安装段、`jmf-init/jmf-sync` 相关路径描述）
- 明确说明 `.workspace` 的结构、用途、以及 git 策略建议（默认忽略、可覆盖）
- 对新增说明做最小一致性校验，避免旧路径示例残留

**Checkpoint:** `install-guidance-updated`
- 安装入口能明确告知 `.workspace` 基础结构及意义
- `.workspace` 的 git 策略建议在安装文档中可见，且包含“可覆盖”说明
- 不再出现与新目录基线冲突的安装指引

---

### Step 8: Add index guides for key directories

**Action:** 为关键目录补充 index 向导文件，提升低能力模型导航稳定性。

**Approach:**
- 至少为 `.workspace/`、`.workspace/tasks/`、`.workspace/project-map/`、`.workspace/resource-map/`、`.workspace/exp-map/` 增加 index 文档
- 每个 index 文档包含：目录用途、核心文件、常见操作入口、与上下游目录关系
- 在相关 skill 文档中加入对 index 向导的引用入口

**Checkpoint:** `index-guides-ready`
- 关键目录 index 文件齐全且内容结构一致
- 低能力模型可通过 index 快速定位操作入口
- skill 文档存在可追踪的 index 跳转指引

---

## Dependencies

Step 1 must complete before all later steps.
Step 2 must complete before Steps 3 and 4.
Step 3 must complete before Step 4.
Step 4 must complete before Step 5.
Step 5 must complete before Step 6.
Step 6 must complete before Steps 7 and 8.
Step 7 should complete before Step 8 so index text reflects final contracts.

## Tracking

| Assumption | Risk |
|-----------|------|
| 目录规范化不需要改动目录内文档语义 | Low — 仅处理路径与目录层，行为面较小 |
| `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）` 可提供可靠的任务 ID 与目录映射基线 | Medium — 历史目录命名不一致时需冲突处理 |
| 分两批迁移可显著降低一次性失败面 | Medium — 两批之间仍需保持引用一致性 |
| ROOT 去污染后现有脚本/文档可通过批量替换修复 | Medium — 可能存在隐蔽硬编码路径 |
| 相关 skills 的路径契约可在一次迭代内同步完成 | Medium — 影响面广，易出现漏改 |
| 安装入口可在不引入复杂交互的情况下完成目录认知注入 | Medium — 多处入口文本需要保持同步 |
| index 向导能显著改善低能力模型导航稳定性 | Low — 文档成本可控，收益明确 |

## Execution Order

Sequential with dependencies noted
