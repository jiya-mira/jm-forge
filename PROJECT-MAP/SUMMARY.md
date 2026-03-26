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
| Domain | `domains.json` | Sub-project / major area nodes |
| Entry | `entries.json` | Entry point files |
| Asset | `assets.json` | Config, resource, data files |
| Graph | `relationships.json` | Typed relationship edges |

---

## Domains

| Domain | Path | Description |
|--------|------|-------------|
| `jmf-bootstrap` | `skills/jmf-bootstrap/` | Ensures uv is installed. Entry skill for new environments. |
| `jmf-exp` | `skills/jmf-exp/` | Extracts structured experience records from real task attempts and task artifacts. |
| `skill-scaffold` | `skills/skill-scaffold/` | Generates new skills. Uses Agent type decision flow. |
| `workflow-execute` | `skills/workflow-execute/` | Thin router / bootstrap entry for the D→P→E workflow. |
| `task-management` | `.claude/skills/` | Core workflow skills: new, discuss, plan, execute, status, list, abandon, auto. |
| `workflow-framework` | `.planning/workflow-framework/` | Discuss→Plan→Execute workflow definition. |

---

## Key Entry Points

| Entry | Path | Description |
|-------|------|-------------|
| `AGENTS.md` | `AGENTS.md` | Primary entry point. Guides AI assistants. Contains project overview, skill registry, conventions. |
| `TASK-REGISTRY.md` | `.planning/TASK-REGISTRY.md` | Central task list. All tasks tracked here. |
| `workflow-framework.md` | `.planning/workflow-framework.md` | D→P→E workflow definition. |
| `manifest.json` | `skills/manifest.json` | Index of all skills. |

---

## Key Relationships

```
AGENTS.md
├── references → TASK-REGISTRY.md
├── references → workflow-framework.md
└── contains → manifest.json

skills/manifest.json
├── contains → jmf-exp
├── contains → workflow-execute
└── contains → other registered skills

TASK-REGISTRY.md
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
