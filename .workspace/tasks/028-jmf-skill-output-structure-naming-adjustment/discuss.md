---
id: 28
---

# Discuss - jmf-skill-output-structure-naming-adjustment

**Date:** 2026-03-26
**Status:** Concluded

---

## Goal

统一 jmf 系列相关产物的目录布局，重点解决 ROOT 污染问题：将游离目录下沉到 `.planning`，并建立统一的任务目录聚合结构（`tasks/`）。

**Source:** discuss-log.md → Iteration 10, Iteration 11

---

## Boundary

- **In scope:** 目录结构规范化；`.workspace/tasks/` 聚合任务目录；`PROJECT-MAP`、`RESOURCE-MAP`、`EXP-MAP` 下沉到 `.workspace`（方案 B 的根目录替换）
- **Out of scope:** 目录内部文档内容与字段语义重构；与目录迁移无关的功能逻辑改造

**Source:** discuss-log.md → Iteration 10, Iteration 11

---

## Assumptions

1. 本任务以目录规范化为主，文件内部命名暂不作为主改造对象。
2. ROOT 目录整洁性优先，允许目录位置发生变更并通过迁移修复引用。

**Source:** discuss-log.md → Iteration 10, Iteration 11

---

## Acceptance Criteria

1. 产出并确认统一目录布局方案：`.workspace/tasks/`、`.workspace/project-map/`、`.workspace/resource-map/`、`.workspace/exp-map/`。
2. 产出并确认任务目录命名规则：`.workspace/tasks/<id>-kebab-case/`（存量目录纳入统一改名）。
3. 给出目录迁移与引用修复方案，并能执行 dry-run 预演清单。
4. 迁移执行按分两批策略推进（先 map 目录，再 tasks）。
5. 迁移后项目 ROOT 不再保留上述三类游离 map 目录，且工作流入口与文档引用可正常解析。
6. 安装路径需明确注入目录结构与语义说明（含 `.workspace` 的 git 策略建议：默认建议加入 `.gitignore`，但允许按项目策略覆盖）。
7. 关键目录均提供 index 向导文件，确保低能力模型可快速定位上下文。

**Source:** discuss-log.md → Iteration 11, Iteration 12, Iteration 13, Iteration 16

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | `.workspace/tasks/` 下任务子目录命名规则是否需要统一改名（存量 slug 目录） | No | 已决策：统一改名为 `<id>-kebab-case` |
| 2 | 迁移执行策略：一次性迁移还是分批迁移 | No | 已决策：分两批迁移 |
| 3 | `PROJECT-MAP` 中路径字段迁移后是否同步强制刷新（`jmf-sync`） | No | 可作为收尾步骤处理 |

*(Resolved issues: ROOT 污染治理范围与布局方案 B 已确认；目录命名规则与迁移节奏已确认。Source: discuss-log.md → Iteration 11/12/13)*

---

## Key Decisions

### PROJECT-MAP stale handling
发现 `PROJECT-MAP` 有 1 个失效路径（`.planning/templates/`），本次 Discuss 不阻塞处理，先继续收敛任务定义，后续需要时再单独执行 `jmf-sync`。

**Source:** discuss-log.md → Iteration 3

### Scope correction
本任务核心是目录结构与目录命名规范化，而非目录内部文件命名体系重构。

**Source:** discuss-log.md → Iteration 10

### Root de-pollution layout
三类 map 目录（`PROJECT-MAP` / `RESOURCE-MAP` / `EXP-MAP`）统一下沉到 `.workspace`，并采用方案 B：`.workspace/project-map|resource-map|exp-map + tasks/`。

**Source:** discuss-log.md → Iteration 11

### Task directory naming
任务子目录统一规则为 `<id>-kebab-case`，存量目录纳入改名迁移。

**Source:** discuss-log.md → Iteration 13

### Workspace root naming
统一产物根目录命名为 `.workspace`；git 策略采用“默认建议加入 `.gitignore`，但允许按项目协作需求覆盖”。

**Source:** discuss-log.md → Iteration 15, Iteration 17

### Install-time context injection
在安装/初始化路径中注入 `.workspace` 目录结构与语义说明，显式告知“默认建议 + 可覆盖”的策略。

**Source:** discuss-log.md → Iteration 16, Iteration 17

### Directory index guides
为关键目录提供 index 向导文件，作为低能力模型的稳定导航锚点。

**Source:** discuss-log.md → Iteration 16

### Migration batching
迁移按两批执行：先迁 `project-map/resource-map/exp-map`，再迁 `tasks` 并修复路径引用。

**Source:** discuss-log.md → Iteration 12

---

## Conclusion

Discuss 已完成：目标、边界、假设、验收标准和迁移节奏均已确认，所有 open issues 已为 non-blocking，建议进入 Plan。

**Source:** discuss-log.md → Iteration 13
