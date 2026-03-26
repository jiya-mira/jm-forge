# Summary — resource-map-project-map-scan-persist-optimization

**Task ID:** 30
**Date:** 2026-03-27
**Status:** Completed

---

## Goal
修正 map 记录模型偏差，建立 `project-map` 的 tree+graph 分层与 `resource-map` 轻量独立模型，并通过“模板跟 skill 走”降低后续记录偏差。

## Changes
- 为 `jmf-init/jmf-sync/jmf-resource` 引入并接线 map 模板（模板文件 + skill 文档消费规则）。
- 在 `.workspace/project-map/INDEX.md`、`.workspace/resource-map/INDEX.md`、`AGENTS.md` 落盘统一的 `Map Boundary Charter`。
- 新增 `.workspace/project-map/tree.json` 作为 tree 层穿透节点载体，并在 `project-map/INDEX.md`/`SUMMARY.md` 中纳入级联路径。
- 更新 `project-map/entries.json` 与 `SUMMARY.md` 的入口引用，匹配当前 `.workspace/tasks/INDEX.md` 与 `workflow-framework.md`。

## Verification
- 模板存在性校验通过：`OK:templates-ready`。
- 边界宪章一致性校验通过：三处 index/agents + 三个 skill 均包含边界定义。
- tree 穿透校验通过：`OK:tree-children-resolvable`。
- task 状态链路完成：`Pending -> Active -> Completed`。

## Risks / Follow-ups
- `project-map` 中仍有历史时期留下的部分 runtime-oriented node（例如早期 task 节点语义）；建议后续单独任务做“历史节点语义清理”。
- 当前以模板和文档约束为主，后续可再加自动化 contract validator 强化防漂移。
