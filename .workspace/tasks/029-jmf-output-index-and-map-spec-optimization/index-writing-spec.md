# INDEX Writing Spec (Task 29)

**Scope:** All `INDEX.md` files under `.workspace/`
**Style:** concise, directory-owned, navigation-first

---

## 1. Purpose

Each `INDEX.md` must explain the content summary of its managed scope:
- sibling files in the same directory
- immediate child directories under the same directory

The index should help a reader decide where to open next with minimal scanning.

## 2. Required Sections

1. `# <Name> Index`
2. One-sentence scope statement (what this directory manages)
3. `## Managed Files` (main files + short purpose)
4. `## Managed Directories` (child dirs + short purpose; if none, write `None`)
5. `## Navigation` (recommended open order / entry links)
6. `## Update Rule` (when to update this INDEX)

## 3. Granularity by Directory Type

- Root-like stable directory (example: `.workspace/`):
  - Keep concise, emphasize top-level routing and fixed structure.
- Task-aggregation directory (example: `.workspace/tasks/`):
  - More specific; include normalized task catalog that can replace legacy task-registry metadata.
- Map directories (example: `project-map`, `resource-map`, `exp-map`):
  - Explain data ownership boundaries and file roles.

## 3.1 Task Catalog Schema (for `.workspace/tasks/INDEX.md`)

Required columns:

`ID | Directory | State | StateMark | Dependon | One-line Summary | Notes`

Rules:
- `State` uses canonical workflow states: `New`, `Discussing`, `Planning`, `Pending`, `Active`, `Completed`, `Failed`, `Abandoned`.
- `StateMark` is the visual marker mapped from `State`:
  - `New` `🆕`, `Discussing` `💬`, `Planning` `📋`, `Pending` `⏳`, `Active` `🔄`, `Completed` `✅`, `Failed` `❌`, `Abandoned` `🚫`
- `Dependon` stores upstream task ID(s), or `-`.
- `Notes` is a compact operator field for items historically stored in `TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`）` notes, for example:
  - blocked reason
  - manual state override reason
  - migration remark
- Keep one row per task directory; do not collapse multiple tasks into one row.

## 4. Brevity Rules

- One-line description per listed file or directory.
- Prefer <= 20 Chinese chars for short labels when possible.
- Avoid repeating schema details already covered in dedicated docs.

## 5. Example A (root, concise)

```md
# Workspace Index

Runtime artifacts root for workflow execution.

## Managed Files
- `INDEX.md`: top-level navigation entry.

## Managed Directories
- `tasks/`: all task artifacts.
- `project-map/`: project context map.

## Navigation
1. Open `tasks/INDEX.md`.
2. Open map indexes as needed.

## Update Rule
Update when top-level directories or navigation paths change.
```

## 6. Example B (task directory, specific)

```md
# Tasks Index

Task artifact hub. One directory per task.

## Managed Files
- `INDEX.md`: task routing and catalog.

## Managed Directories
- `001-.../`: workflow framework definition.
- `029-.../`: index/map spec optimization execution artifacts.

## Task Catalog
| ID | Directory | State | StateMark | Dependon | Purpose | Notes |
|----|-----------|-------|-----------|----------|---------|-------|
| 29 | `029-...` | Active | 🔄 | - | Define and apply index/map specs | - |

## Navigation
1. Find task in catalog.
2. Open task folder and phase docs.

## Update Rule
Update when task directories, task states, dependencies, or task notes change.
```
