# Execute — Task #28: jmf-skill-output-structure-naming-adjustment

**Date:** 2026-03-26
**Source:** plan.md

---

## Checkpoint Log

## Batch 1

**[Checkpoint 1: layout-spec-frozen]**
Status: ✅ Verified
Evidence: `plan.md` 已固定目标结构为 `.workspace/{tasks,project-map,resource-map,exp-map}`，任务目录规则为 `<id>-kebab-case`。

**[Checkpoint 2: dry-run-ready]**
Status: ✅ Verified
Evidence: `scripts/migrate-to-workspace-layout.sh dry-run` 已生成 `/tmp/task28-dry-run.txt`（30 条迁移项）。

**[Checkpoint 3: batch1-maps-migrated]**
Status: ✅ Verified
Evidence: `PROJECT-MAP`/`RESOURCE-MAP`/`EXP-MAP` 已迁移到 `.workspace/project-map`、`.workspace/resource-map`、`.workspace/exp-map`；ROOT 下无上述目录。

**[Checkpoint 4: batch2-tasks-migrated]**
Status: ✅ Verified
Evidence: 注册任务目录已迁移到 `.workspace/tasks/`，并采用 `<id>-kebab-case`（示例：`028-jmf-skill-output-structure-naming-adjustment`）。

## Batch 2

**[Checkpoint 5: contracts-updated]**
Status: ✅ Verified
Evidence: 核心 skills、`AGENTS.md`、`README.md`、迁移脚本与 project-map 路径契约已改为 `.workspace` 基线；`rg` 对旧根路径无命中（目标集内）。

**[Checkpoint 6: post-migration-verified]**
Status: ✅ Verified
Evidence: `WORKSPACE_DIRS_OK` 校验通过；关键路径可解析；执行中发现的 map 迁移脚本缺陷已修复并记录于 discuss-log Iteration 18。

**[Checkpoint 7: install-guidance-updated]**
Status: ✅ Verified
Evidence: `README.md` 与 `jmf-bootstrap/jmf-init` 已加入安装期目录语义说明，采用“`.workspace` 默认建议忽略、允许覆盖”的策略。

**[Checkpoint 8: index-guides-ready]**
Status: ✅ Verified
Evidence: 已创建 `.workspace/INDEX.md`、`.workspace/tasks/INDEX.md`、`.workspace/project-map/INDEX.md`、`.workspace/resource-map/INDEX.md`、`.workspace/exp-map/DIRECTORY-INDEX.md`。

---

## Acceptance Report

Discuss 验收标准 1-7 已满足：
1. `.workspace` 统一布局已落地。
2. 任务目录规则 `<id>-kebab-case` 已应用到已登记任务。
3. 迁移脚本提供 dry-run 与 apply，且 dry-run 清单可复核。
4. 迁移按两批执行（map -> tasks）。
5. ROOT 已移除三类 map 目录。
6. 安装期目录语义注入已完成，git 策略为“推荐+可覆盖”。
7. 关键目录 index 向导文件已补齐，便于低能力模型导航。
