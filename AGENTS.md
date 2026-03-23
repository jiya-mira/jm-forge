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
│   ├── jm-forge-*/               # All jm-forge-* skills
│   │   └── SKILL.md
│   ├── skill-scaffold/
│   │   └── SKILL.md
│   └── workflow-execute/
│       └── SKILL.md
├── skills/                        # Canonical source (cross-platform)
│   ├── manifest.json              # Index of all skills
│   ├── jm-forge-bootstrap/
│   └── skill-scaffold/
├── PROJECT-MAP/                   # Project context map (created by jm-forge:init)
├── .planning/                     # Task planning directories
├── AGENTS.md                      # This file
└── README.md                      # Project documentation
```

**Note:** `RESOURCE-MAP/` is project-local (gitignored) — managed by `jm-forge:resource` but not part of framework distribution.

**Skill naming conventions:**
- `skill-scaffold` — internal framework skill (no prefix)
- `jm-forge-*` — publishable skills ready for distribution
- `workflow-execute` — workflow orchestration skill

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

Before using any skill, ensure `uv` is installed. See `skills/jm-forge-bootstrap/SKILL.md` for instructions.

### Validation

- All skills must pass validation before being considered functional
- Use the validation scripts in `scripts/` directory
- Validation should be deterministic and reproducible

### Bootstrapping Approach

- **Incremental skill creation**: Start with minimal viable skills, expand as needed
- **Framework evolves with usage**: The AGENTS.md is updated when new patterns solidify
- **Self-referential**: Skills may invoke other skills to build new capabilities
- **Validation-first**: Each skill must prove itself before being relied upon

### Skill Registration

When adding a new skill:
1. Choose a name:
   - Internal skills: `skill-scaffold` (no prefix)
   - Publishable skills: `jm-forge-<name>` (e.g., `jm-forge-code-review`)
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

This project uses a **Discuss → Plan → Execute (D→P→E)** workflow for managing tasks. See `.planning/workflow-framework.md` for details.

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
| `jm-forge:new` | Create a new task |
| `jm-forge:discuss` | Conduct Discuss phase |
| `jm-forge:plan` | Conduct Plan phase |
| `jm-forge:execute` | Conduct Execute phase |
| `jm-forge:auto` | Auto-advance through phases |
| `jm-forge:list` | List all tasks |
| `jm-forge:status` | Show task details |
| `jm-forge:abandon` | Mark task as abandoned |
| `jm-forge:init` | Analyze project and build PROJECT-MAP |
| `jm-forge:sync` | Update existing PROJECT-MAP |
| `jm-forge:resource` | Manage project resources (add/list/remove) |

### Workflow States

Tasks move through these states: `New → Discussing → Planning → Pending → Active → Completed`

(Or to `Failed` on error, or `Abandoned` if user manually abandons)

---

## Document Index

Entry points for navigating this project:

| Document | Role |
|----------|------|
| `TASK-REGISTRY.md` | Central task list — all tasks with IDs, states, and phase directories |
| `AGENTS.md` | This file — entry point for Agents, skill registry, and conventions |
| `.planning/workflow-framework.md` | Discuss→Plan→Execute workflow definition |
| `.planning/workflow-framework/discuss.md` | Workflow Discuss phase doc |
| `.planning/workflow-framework/references.md` | Workflow reference materials |

### Phase Directories

Each task has its own phase directory under `.planning/<task-name>/`:

| Phase Doc | Source | Description |
|-----------|--------|-------------|
| `discuss.md` | Source of truth for Discuss phase | Goal, boundary, assumptions, acceptance criteria |
| `discuss-log.md` | discuss.md | Iteration log for Discuss phase |
| `plan.md` | discuss.md | Executable plan with step decomposition |
| `execute.md` | plan.md | Execution log with checkpoint verification |

### Skills

All skills live in `.claude/skills/<skill-name>/SKILL.md` and `skills/<skill-name>/SKILL.md`.

### Templates

Phase templates under `.planning/templates/`:
`discuss.md`, `discuss-log.md`, `plan.md`, `execute.md`

### Navigation

```
TASK-REGISTRY.md → .planning/<task-name>/discuss.md → plan.md → execute.md
AGENTS.md → skills + phase docs
```

---

## PROJECT-MAP Maintenance

`PROJECT-MAP/` stores the project context map. Keep it accurate:

1. **When you create, delete, or rename a meaningful project element, update PROJECT-MAP/**
   - `jm-forge:new` and `skill-scaffold` do this automatically
   - For other changes: run `jm-forge:sync` or manually update relevant JSON files

2. **Run `jm-forge:sync` when map is stale**
   - `jm-forge:discuss` will prompt if it detects stale data
   - `--force-refresh` for full rebuild

3. **Use `jm-forge:init` only for first-time setup**
   - Subsequent updates use `jm-forge:sync`

## RESOURCE-MAP (Project-Local)

`RESOURCE-MAP/` is project-local and gitignored — each project manages its own resources. Use `jm-forge:resource` to manage resource entities:
- Add/list/remove resources tracked in the project's `RESOURCE-MAP/resources.json`
- Run `jm-forge:resource scan` to auto-discover resources

---

## Notes

- The specific theoretical foundations (ReAct, Plan-and-Execute, etc.) are determined through iterative practice rather than upfront design.
- As the framework is applied to tasks, it will reveal its own gaps and improvement opportunities.
- This document should be updated when concrete patterns emerge from implementation.
