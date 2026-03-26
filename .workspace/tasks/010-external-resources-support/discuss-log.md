# discuss-log.md: external-resources-support

**Source:** (initial creation)

---

## Iteration 1 — 2026-03-23

### Context

User raised an issue with `jm-forge-init` and `jm-forge-sync`:

- racobit project is actually a **project collection** (contains multiple sub-projects: racobit-server, racobit-web, racobit-wecom-adapter)
- All source code is in the same directory for agent convenience
- But valuable resources and information exist **outside** the project directory (e.g., server configs, external docs)
- Current `init` and `sync` only scan the project root

### Problem Statement

`jm-forge-init` and `jm-forge-sync` cannot discover and incorporate external resources that are valuable for the agent's understanding but live outside the project tree.

### Proposed Approaches ( brainstorming)

1. **External Resource Registry** (`.claude/RESOURCES.md`)
   - Declare external paths in a manifest file
   - init/sync reads and incorporates these paths

2. **Multi-layer PROJECT-MAP**
   - Support sub-project configurations under `.planning/`
   - Allow external resource references

3. **Dynamic Path Parameters**
   - `--extra-paths` flag for init/sync commands

4. **Environment-aware Discovery**
   - Auto-detect resource types and find relevant external resources

### Next Steps

- Discuss which approach best fits the use case
- Consider implementation complexity vs. flexibility trade-offs
- Define acceptance criteria

---

## Iteration 2 — 2026-03-23

### Decisions Made

1. **Q1 - Discovery Mode**: 显式注册为主 + 自动发现为辅
2. **Q2 - PROJECT-MAP Integration**: 独立节点 + 简化 schema
3. **Q3 - Skill Architecture**: 独立 skill（jm-forge-external）+ init/sync 集成询问
4. **Q4 - Location**: `.external/`
5. **Q5 - Schema**: 泛化设计，核心字段 + 完全自由的 attributes，支持任意类型的外部资源

### Key Insights

- 不需要 pull/缓存，只要资源地图（指针清单）即可
- 资源地图本身是有价值的，包含资源的描述、属性、关系
- 泛化设计：任何项目外部的、对项目有价值的人、财、物、信息，都是外部资源
- 安全属性很重要，特别是针对可控资源
