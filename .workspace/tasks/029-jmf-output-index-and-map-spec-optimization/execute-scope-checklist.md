# Execute Scope Checklist — Task 29

**Task:** jmf-output-index-and-map-spec-optimization
**Date:** 2026-03-26
**Purpose:** Step 1 baseline and manual verification checklist

---

## A. Mandatory INDEX Targets (`.workspace`)

- [x] `.workspace/INDEX.md`
- [x] `.workspace/tasks/INDEX.md`
- [x] `.workspace/project-map/INDEX.md`
- [x] `.workspace/resource-map/INDEX.md`
- [x] `.workspace/exp-map/INDEX.md`

## B. Map Series Targets

### project-map
- [x] `.workspace/project-map/project.json`
- [x] `.workspace/project-map/domains.json`
- [x] `.workspace/project-map/entries.json`
- [x] `.workspace/project-map/assets.json`
- [x] `.workspace/project-map/relationships.json`
- [x] `.workspace/project-map/SUMMARY.md`
- [x] `.workspace/project-map/INDEX.md`

### resource-map
- [x] `.workspace/resource-map/resources.json`
- [x] `.workspace/resource-map/INDEX.md`

### exp-map (同步规范，不扩展复杂级联)
- [x] `.workspace/exp-map/INDEX.md`
- [x] `.workspace/exp-map/DIRECTORY-INDEX.md`

## C. Reference/Contract Targets

- [x] `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）`（状态与任务记录一致性）
- [x] `.workspace/tasks/029-jmf-output-index-and-map-spec-optimization/discuss.md`
- [x] `.workspace/tasks/029-jmf-output-index-and-map-spec-optimization/plan.md`
- [x] `README.md`（本轮无必要变更）
- [x] `AGENTS.md`（本轮无必要变更）

## D. Manual Verification Checklist

### INDEX completeness
- [x] 每个 INDEX 都说明其管理范围（同目录文件 + 子目录）
- [x] 粒度按目录类型区分（根级可简，task 级更具体）
- [x] 导航入口可达且命名一致

### map cascade (initial)
- [x] `project-map` 明确级联入口与层级关系
- [x] `resource-map` 明确级联入口与层级关系
- [x] `exp-map` 与统一规范保持一致（不引入复杂级联）

### reference integrity
- [x] 关键路径引用无断裂
- [x] 变更后的说明与现有文件结构一致
