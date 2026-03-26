# Tasks Index

Directory index for `.workspace/tasks/`.

## Managed Files
- `INDEX.md`: routing entry and normalized task catalog (source of truth).

## Managed Directories
- `<id>-<task-name>/`: one task directory per workflow task.

## Task Catalog Spec (v2)

- Required columns: `ID | Directory | State | StateMark | Dependon | One-line Summary | Notes`
- `Dependon` uses task ID or `-` if none
- `Notes` stores compact metadata (for example, blocked reason, manual override, migration notes)
- StateMark mapping:
  - `New` = `🆕`
  - `Discussing` = `💬`
  - `Planning` = `📋`
  - `Pending` = `⏳`
  - `Active` = `🔄`
  - `Completed` = `✅`
  - `Failed` = `❌`
  - `Abandoned` = `🚫`

## Task Catalog

| ID | Directory | State | StateMark | Dependon | One-line Summary | Notes |
|----|-----------|-------|-----------|----------|------------------|-------|

## Navigation
1. Find task by ID or summary in the catalog above.
2. Open the task directory.
3. Read phase docs in order: `discuss.md` -> `plan.md` -> `execute.md` -> `summary.md`.

## Update Rule
Update this index when any of the following changes:
- task directories are added/removed/renamed
- task state changes
- task dependency changes (`Dependon`)
- task-level tracking notes change (blockers, manual override, migration notes)
