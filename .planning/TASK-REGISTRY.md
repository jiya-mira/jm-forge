# Task Registry

> Centralized task list with IDs, states, and dependencies.

---

## Reference Conventions

Documents reference their sources as follows:

| Phase Doc | Source | Format |
|-----------|--------|--------|
| `discuss.md` | `discuss-log.md` | `**Source:** discuss-log.md` (top of doc) |
| `plan.md` | `discuss.md` | `**Source:** discuss.md` (top of doc) |
| `execute.md` | `plan.md` | `**Source:** plan.md` (top of doc) |

**Entry points:** `TASK-REGISTRY.md`, `AGENTS.md`

---

| ID | Task | State | Dependon | Notes |
|----|------|-------|----------|-------|
| 1 | workflow-framework | Completed | — | |
| 2 | jm-forge-bootstrap | Completed | — | |
| 3 | jm-forge:* skills | Completed | — | jm-forge:new, :discuss, :plan, :execute, :abandon, :list, :status, :auto |
| 4 | skill-scaffold-v2 | Completed | — | skill-scaffold SKILL.md updated with Agent type decision flow |
| 5 | doc-relationship-graph | Completed | — | Document reference conventions established |
| 6 | task-concurrency-control | New | — | Prevent conflicts when user manages multiple tasks simultaneously |
| 7 | skill-naming-overhaul | Completed | — | Redesign skill naming convention for usability |
| 8 | jm-forge-init | Completed | — | Analyze existing project and build context map for jm-forge workflow |
| 9 | jm-forge-init-refresh | Completed | — | Add re-run support and incremental maintenance protocol to jm-forge:init |
| 10 | external-resources-support | Completed | — | Support external resources in jm-forge-init and jm-forge-sync for project collections |
| 11 | resource-map-redesign | Completed | — | Redesign .external into RESOURCE-MAP with broader scope (人、财、物、信息) |
| 12 | resource-auto-discovery | Completed | 10 | Auto-discover and register resources from existing project files |
| 13 | readme-redesign | Completed | — | Write comprehensive README for MVP release: methodology, theory, getting started |
| 14 | mvp-release | Completed | — | Git repo initialized, commit 665058e created, tag v0.1.0 tagged, pending push |
| 15 | readme-finalize | Completed | 13 | All 3 steps verified: Roadmap expanded, Dev Environment fixed, paper links added |
| 16 | gemini-project-skill | Completed | — | 配置gemini对应的skill，使其可以以project级别的使用本工作流 |
| 17 | skill-naming-standardization | Completed | — | jm-forge现存的skill以及未来的skill的命名规则问题，再次需要修正与规范化 |

---

## State Legend

| State | Set By | Description |
|-------|--------|-------------|
| New | Agent (auto) | User just proposed the idea |
| Discussing | Agent (auto) | In Discuss phase |
| Planning | Agent (auto) | In Plan phase |
| Pending | Agent (auto) | Plan complete, waiting to execute |
| Active | Agent (auto) | In Execute phase |
| Completed | Agent (auto) | Execute finished successfully |
| Failed | Agent (auto) | Execute failed |
| Abandoned | **User (manual)** | Explicitly abandoned by user |

## Task Lifecycle

```
New → Discussing → Planning → Pending → Active → Completed
                                        ↘ Failed
                          ↘ Abandoned (user手动)
    ↘ (any state) → Abandoned (user手动)
```

**Blocked:** When a task Dependons another that is not Completed, it is effectively Blocked. The Dependon column shows the blocking task.

## Creating New Tasks

When a user proposes a new task:
1. Agent adds a row to this registry with the next available ID
2. Agent creates `.planning/<task-name>/` directory
3. State is set to New
4. Dependon is set if applicable
