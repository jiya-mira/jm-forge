# AGENTS.md

This file provides guidance for AI assistants working in this repository.

## Project Overview

This is a **skills-based Agent scaffolding framework** — a meta-engineering project that combines modern software engineering/project management theories with multi-Agent collaboration patterns. The goal is to create a framework that enables AI assistants to efficiently accomplish a wide range of goals through a structured skill system.

### Core Components

1. **Skills System** — The central unit of work. Each skill is a self-contained capability that can be invoked.
2. **Skill Installation Scripts** — Tools to deploy and manage skills across environments.
3. **Skill Validation Framework** — Mechanisms to verify skills work correctly (testing, linting, health checks).
4. **Self-Iteration System** — Framework for skills to improve themselves through reflection and feedback loops.
5. **Utility Scripts** — Minimal helper scripts needed to support the above.

### Architecture Philosophy

The framework evolves through **self-regressive bootstrapping**: the project uses its own constructs to improve its own implementation. Theory and practice are refined iteratively as the framework is applied to real tasks.

---

## Development Conventions

### Directory Structure

```
forge/
├── .claude/skills/                # Claude Code discovery (actual files)
│   ├── jmf-*/               # All jmf-* skills
│   │   └── SKILL.md
│   ├── skill-scaffold/            # Internal build-time helper
│   │   └── SKILL.md
│   └── workflow-execute/          # Thin router / bootstrap entry
│       └── SKILL.md
├── skills/                        # Canonical source (cross-platform)
│   ├── manifest.json              # Index of all skills
│   ├── jmf-bootstrap/
│   ├── skill-scaffold/
│   └── workflow-execute/
├── .workspace/                    # Runtime artifacts root (tasks/maps/exp)
│   ├── tasks/
│   ├── project-map/
│   ├── resource-map/
│   └── exp-map/
├── planning/                      # Workflow entry docs (registry/framework docs)
├── AGENTS.md                      # This file
└── README.md                      # Project documentation
```

**Note:** `.workspace/` is runtime data. Default recommendation is gitignore; teams may override this and commit selected artifacts if collaboration needs it.

**Skill naming conventions:**
- `skill-scaffold` — internal framework build-time helper (no prefix)
- `jmf-*` — publishable skills ready for distribution
- `workflow-execute` — thin router / bootstrap entry for the workflow

**Claude Code integration:**
- Skills are discovered via `.claude/skills/<skill-name>/SKILL.md`
- **Note**: Symlinks are not supported — use actual files
- Each skill must have a `SKILL.md` with YAML frontmatter (`name`, `description`)

### Code Style

- **uv scripts**: All skill scripts use Python with `uv run` invocation
- Write clear, modular code with explicit interfaces between components
- Prefer explicit over implicit; avoid "magical" abstractions
- Each skill should be independently testable
- Document the *why* behind non-obvious design decisions

### Prerequisites

Before using any skill, ensure `uv` is installed. See `skills/jmf-bootstrap/SKILL.md` for instructions.

### Validation

- All skills must pass validation before being considered functional
- Use the validation scripts in `scripts/` directory
- Validation should be deterministic and reproducible

### Bootstrapping Approach

- **Incremental skill creation**: Start with minimal viable skills, expand as needed
- **Framework evolves with usage**: The AGENTS.md is updated when new patterns solidify
- **Self-referential**: Skills may invoke other skills to build new capabilities
- **Validation-first**: Each skill must prove itself before being relied upon

### Non-jmf Skill Boundary

- `workflow-execute` is the only retained non-`jmf-*` runtime/router entry
- `skill-scaffold` is an internal build-time helper and should not be treated as a user-facing runtime skill
- All other runtime workflow behavior belongs in `jmf-*` skills

### Skill Registration

When adding a new skill:
1. Choose a name:
   - Internal skills: `skill-scaffold` (no prefix)
   - Publishable skills: `jmf-<name>` (e.g., `jmf-code-review`)
2. Create `skills/<skill-name>/` directory
3. Add `skills/<skill-name>/SKILL.md` with frontmatter:
   ```yaml
   ---
   name: skill-name
   description: What this skill does and when to use it
   ---
   ```
4. Register it in `skills/manifest.json`
5. Copy SKILL.md to `.claude/skills/` for Claude Code discovery:
   ```bash
   mkdir -p .claude/skills/<skill-name>
   cp skills/<skill-name>/SKILL.md .claude/skills/<skill-name>/
   ```

---

## Design Principles

1. **Skills as first-class citizens** — Everything meaningful is a skill.
2. **Validation over trust** — Skills are verified before being relied upon.
3. **Bootstrapping** — The framework uses itself to evolve.
4. **Minimal surface area** — Small number of essential utilities; complexity lives in skills.

---

## When to Use the jm-forge Workflow

This project uses a **Discuss → Plan → Execute (D→P→E)** workflow for managing tasks. See `workflow-framework.md` for details.

### Task Unit Definition

A task is an atomic unit of work that satisfies **all four** conditions:

1. **Explicit start** — Clear trigger or entry point exists
2. **Explicit end** — Clear completion or closure point exists
3. **Independently verifiable** — An external observer can determine completion
4. **Recursively decomposable** — Can be broken into ordered steps until each step has an independently verifiable endpoint

### Triggering the Workflow

When a user expresses intent that satisfies all four conditions above, the workflow should be offered or triggered automatically.

**Do NOT trigger if:**
- The user's request is a simple question or one-off fact lookup
- The request lacks a decomposable structure (cannot be broken into steps)
- No clear completion criteria exists

**Do trigger if:**
- User describes a goal with clear start, end, and verifiable completion
- User asks to build something, fix something, create something, implement something
- The request naturally decomposes into ordered steps

### Workflow Skills

| Skill | Purpose |
|-------|---------|
| `jmf-new` | Create a new task |
| `jmf-discuss` | Conduct Discuss phase |
| `jmf-plan` | Conduct Plan phase |
| `jmf-execute` | Conduct Execute phase |
| `jmf-auto` | Auto-advance through phases |
| `jmf-list` | List all tasks |
| `jmf-status` | Show task details |
| `jmf-abandon` | Mark task as abandoned |
| `jmf-init` | Analyze project and build project map |
| `jmf-sync` | Update existing project map |
| `jmf-resource` | Manage project resources (add/list/remove) |
| `workflow-execute` | Thin router for the D→P→E workflow entry |

### Workflow States

Tasks move through these states: `New → Discussing → Planning → Pending → Active → Completed`

(Or to `Failed` on error, or `Abandoned` if user manually abandons)

---

## Document Index

Entry points for navigating this project:

| Document | Role |
|----------|------|
| `.workspace/tasks/INDEX.md` | Central task list — all tasks with IDs, states, dependencies, and phase directories |
| `AGENTS.md` | This file — entry point for Agents, skill registry, and conventions |
| `workflow-framework.md` | Discuss→Plan→Execute workflow definition |
| `.workspace/tasks/001-workflow-framework/discuss.md` | Workflow Discuss phase doc |
| `.workspace/tasks/001-workflow-framework/references.md` | Workflow reference materials |

### Phase Directories

Each task has its own phase directory under `.workspace/tasks/<id>-<task-name>/`:

| Phase Doc | Source | Description |
|-----------|--------|-------------|
| `discuss.md` | Source of truth for Discuss phase | Goal, boundary, assumptions, acceptance criteria |
| `discuss-log.md` | discuss.md | Iteration log for Discuss phase |
| `plan.md` | discuss.md | Executable plan with step decomposition |
| `execute.md` | plan.md | Execution log with checkpoint verification |

### Skills

All skills live in `.claude/skills/<skill-name>/SKILL.md` and `skills/<skill-name>/SKILL.md`.

### Templates

Phase templates live with skill-local templates (for example `skills/jmf-new/templates/`).

### Navigation

```
.workspace/tasks/INDEX.md → .workspace/tasks/<id>-<task-name>/discuss.md → plan.md → execute.md
AGENTS.md → skills + phase docs
```

---

## Project Map Maintenance

`.workspace/project-map/` stores the project context map. Keep it accurate:

1. **When you create, delete, or rename a meaningful project element, update .workspace/project-map/**
   - `jmf-new` and `skill-scaffold` do this automatically
   - For other changes: run `jmf-sync` or manually update relevant JSON files

2. **Run `jmf-sync` when map is stale**
   - `jmf-discuss` will prompt if it detects stale data
   - `--force-refresh` for full rebuild

3. **Use `jmf-init` only for first-time setup**
   - Subsequent updates use `jmf-sync`

## Resource Map (Project-Local)

`.workspace/resource-map/` is project-local and gitignored — each project manages its own resources. Use `jmf-resource` to manage resource entities:
- Add/list/remove resources tracked in the project's `.workspace/resource-map/resources.json`
- Run `jmf-resource scan` to auto-discover resources

## Map Boundary Charter

- `project-map` records project-native structure and relations with a layered `tree + graph` model.
- `.workspace` runtime artifacts are workflow data and are not primary `project-map` recording targets.
- `resource-map` is the source of truth for resource entities and lightweight relations.
- `domains.json`, `entries.json`, `assets.json`, `relationships.json` remain the canonical graph-layer records in `project-map`.
- `resource-map` only borrows design ideas from `project-map`; keep relationship thin and data ownership separate.
- Canonical charter references:
  - `.workspace/project-map/INDEX.md`
  - `.workspace/resource-map/INDEX.md`

---

## Notes

- The specific theoretical foundations (ReAct, Plan-and-Execute, etc.) are determined through iterative practice rather than upfront design.
- As the framework is applied to tasks, it will reveal its own gaps and improvement opportunities.
- This document should be updated when concrete patterns emerge from implementation.
