---
id: 26
---

# Discuss — non-jmf-skill-replanning

**Date:** 2026-03-26
**Status:** Concluded

---

## Goal

重新规划并收敛非 `jmf-*` 命名的 skill，使其与当前 jm-forge 的命名、安装、入口发现和项目地图保持一致。

**Source:** discuss-log.md → Iteration 5

---

## Boundary

- **In scope:** 非 `jmf-*` skill 的命名策略、目录与 `name` 字段迁移、`skills/manifest.json`、`PROJECT-MAP/`、文档引用与入口路径调整
- **Out of scope:** 具体业务逻辑重写、技能内部算法改造、与本次命名无关的功能新增

**Source:** discuss-log.md → Iteration 5

---

## Assumptions

1. 绝大多数用户只需要 `jmf-*` 系列 skill
2. 非 `jmf-*` 中最多只保留 1 个极薄入口/router skill
3. 该入口 skill 主要用于安装、导航和过渡，不承担复杂业务逻辑
4. 其余 runtime skill 应统一进入 `jmf-*` 命名体系
5. 普通模型更依赖显式、薄边界的入口，而不是厚重的总控 skill

**Source:** discuss-log.md → Iteration 5

---

## Acceptance Criteria

1. 非 `jmf-*` skill 数量收敛到 1 个
2. 保留的那个 skill 仅承担薄入口/router 职能
3. 其余 skill 的名称、目录、manifest 与项目地图已同步到 `jmf-*`
4. 仓库文档不再把非 `jmf-*` skill 当作常规用户入口

**Source:** discuss-log.md → Iteration 5

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | 保留的唯一薄入口 skill 的具体落点是否保持现名 `workflow-execute` | No | resolved：保留现名 `workflow-execute` |

---

## Key Decisions

### 单薄入口策略
非 `jmf-*` skill 最终只保留一个极薄入口/router skill，其余全部迁移进 `jmf-*`。

**理由：** 这样既能满足普通模型对显式入口的需求，又不会让非 `jmf-*` 体系继续膨胀。

**Source:** discuss-log.md → Iteration 5

### 入口定位
保留的入口 skill 主要服务安装、导航和过渡，不作为用户日常常用的厚重控制器。

**理由：** 对普通模型而言，薄边界和明确职责更稳定，也更容易维护。

**Source:** discuss-log.md → Iteration 4

### 具体落点确认
唯一保留的非 `jmf-*` 入口 skill 保持现名 `workflow-execute`，并在实现上收紧为薄 router。

**理由：** 该名称已经被仓库和用户上下文广泛使用，保留现名可以降低迁移摩擦，同时通过职责收缩解决“过厚”的问题。

**Source:** discuss-log.md → Iteration 7

---

## Conclusion

非 `jmf-*` skill 不应再作为常规运行时体系扩张。当前结论是收敛到一个极薄入口/router，其余 skill 统一进入 `jmf-*` 命名体系，并在后续 Plan 中完成具体迁移路径、兼容策略和项目地图同步。

**Source:** discuss-log.md → Iteration 7
