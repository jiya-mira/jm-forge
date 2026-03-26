# PROJECT-MAP Summary

> Human-readable entry point for project context. For detailed data, see individual JSON files.

**Project:** jm-forge
**Type:** framework
**Last Updated:** 2026-03-26

---

## Quick Navigation

| Layer | File | Purpose |
|-------|------|---------|
| Top | `project.json` | Project metadata, domain list, root entry |
| Tree | `tree.json` | Layered traversal nodes (`children_ids` + `doc_ref`) |
| Domain | `domains.json` | Sub-project / major area nodes |
| Entry | `entries.json` | Entry point files |
| Asset | `assets.json` | Config, resource, data files |
| Graph | `relationships.json` | Typed relationship edges |

---

## Cascade (Initial)

Recommended read order:

1. `INDEX.md`
2. `SUMMARY.md`
3. `project.json`
4. `tree.json`
5. `domains.json` / `entries.json` / `assets.json`
6. `relationships.json`
7. `schema-reference.md`

This is the initial cascade contract. Deep cascade mechanics are intentionally out of scope for Task #29.

---

## Domains

| Domain | Path | Description |
|--------|------|-------------|
| `jmf-bootstrap` | `skills/jmf-bootstrap/` | Ensures uv is installed. Entry skill for new environments. |
| `jmf-exp` | `skills/jmf-exp/` | Builds project-level EXP records and persists them to `.workspace/exp-map` (index + one-entry-per-file). |
| `skill-scaffold` | `skills/skill-scaffold/` | Generates new skills. Uses Agent type decision flow. |
| `workflow-execute` | `skills/workflow-execute/` | Thin router / bootstrap entry for the D→P→E workflow. |
| `task-management` | `.claude/skills/` | Core workflow skills: new, discuss, plan, execute, status, list, abandon, auto. |
| `workflow-framework` | `.workspace/tasks/001-workflow-framework/` | Discuss→Plan→Execute workflow definition. |

---

## Key Entry Points

| Entry | Path | Description |
|-------|------|-------------|
| `AGENTS.md` | `AGENTS.md` | Primary entry point. Guides AI assistants. Contains project overview, skill registry, conventions. |
| `tasks/INDEX.md` | `.workspace/tasks/INDEX.md` | Central task list (source of truth). |
| `workflow-framework.md` | `workflow-framework.md` | D→P→E workflow definition. |
| `manifest.json` | `skills/manifest.json` | Index of all skills. |

---

## Key Relationships

```
AGENTS.md
├── references → tasks/INDEX.md
├── references → workflow-framework.md
└── contains → manifest.json

skills/manifest.json
├── contains → jmf-exp
├── contains → workflow-execute
└── contains → other registered skills

tasks/INDEX.md
├── references → workflow-framework/
└── contains → task-management/

skills/manifest.json → contains → jmf-exp
skills/manifest.json → contains → workflow-execute
task-management/ → builds-on → workflow-framework/
jmf-bootstrap → references → skill-scaffold
skill-scaffold → references → templates/
workflow-execute → delegates → task-management/
skill-naming-convention.md → implements → workflow-framework/
```

---

## Schema Reference

See `schema-reference.md` for node types and relationship types.
