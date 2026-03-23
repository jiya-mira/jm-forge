# Discuss — jm-forge-init

**Date:** 2026-03-23
**Status:** Concluded
**Task ID:** 8

---

## Goal

Build a project context map when introducing jm-forge to an existing project. The map should help any Agent quickly index valuable information without blind searching, especially for less capable Agents. Token-efficient by design.

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** Project context discovery, map format and structure, multi-project support, automatic + user-assisted relationship identification
- **Out of scope:** Specific agent platform integration (must be agent-agnostic), implementation code

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. Project types are not limited to software — any work domain (writing, research, hardware, business) can be mapped
2. `jm-forge:init` is separate from `jm-forge:bootstrap` — bootstrap handles environment (uv), init handles project context
3. User manually triggers `jm-forge:init` (not automatic) because the process is token-expensive

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. Map represents the entire working directory's content structure and key file relationships
2. Agent can quickly locate any valuable information by navigating the map, not by blind scanning
3. Map works for any project type (software, writing, research, hardware, etc.)
4. Token-efficient: can represent large project collections without exceeding context limits
5. Agent-agnostic: independent of any specific agent platform

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

| # | Issue | Blocking? | Notes |
|---|-------|-----------|-------|
| 1 | What is the exact schema for typed nodes and relationships? | No | Handled in Plan phase |
| 2 | How to handle unknown/unclear relationships gracefully? | No | Mark as `unknown-type`, don't block |

*(Resolved issues: none)*

---

## Key Decisions

### Map Architecture: Multi-file with Typed Node Graph

**Output location:** `PROJECT-MAP/` directory in project root

**Structure:**
```
PROJECT-MAP/
├── project.json          # Top-level summary + metadata
├── domains.json         # Domain/module structure (for multi-project collections)
├── entries.json         # Entry points index
├── assets.json          # Assets, configs, resources
├── relationships.json   # Typed relationship graph
└── SUMMARY.md          # Human-readable navigation guide
```

**Schema principles:**
- **Typed nodes**: Domain, EntryPoint, Asset, Abstraction, Artifact, Unknown
- **Typed relationships**: depends-on, implements, contains, references, builds-on, unknown-type
- Nodes and relationships are content-agnostic — applicable to any project type

**Source:** discuss-log.md → Iteration 1

### Relationship Identification: Automatic + User Confirmation

- Agent automatically scans and infers relationships
- When structure/content cannot be confidently understood: prompt user to confirm
- If user also cannot identify: mark as `unknown-type` and continue — do not block
- Token-efficient: selective inclusion, not exhaustive coverage

**Source:** discuss-log.md → Iteration 1

### Workflow Integration: Discuss Phase Auto-Read

- Map is stored as standalone files, not tied to any agent platform
- When `jm-forge:discuss` runs for a task, it reads relevant PROJECT-MAP files to understand context
- User can request re-map at any time via `jm-forge:init --refresh`

**Source:** discuss-log.md → Iteration 1

### Token Efficiency Strategy

- Multi-level summaries (top-level → domain-level → file-level)
- Top-level `project.json` is the entry point — small, always loaded
- Detailed data in domain/entries/relationships JSON — loaded on demand
- Agent traverses from summary inward, not always loading full graph

**Source:** discuss-log.md → Iteration 1

---

## Conclusion

`jm-forge:init` creates a `PROJECT-MAP/` directory with typed node graph (JSON) + layered summaries (Markdown). It is:

- **Universal**: typed nodes/relationships work for any project domain
- **Token-efficient**: multi-level summaries, on-demand detail loading
- **Agent-agnostic**: standalone files, no platform binding
- **User-assisted**: falls back to `unknown-type` gracefully when识别 fails

Ready for Plan.

**Source:** discuss-log.md → Iteration 1
