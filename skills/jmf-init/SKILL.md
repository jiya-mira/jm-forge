---
name: jmf-init
description: Analyze the current project and build a PROJECT-MAP context map. Run when introducing jm-forge to an existing project, or when --refresh is needed.
---

# Skill: jmf-init

## Purpose

Analyze the current working directory and build a `.workspace/project-map/` context map that helps Agents quickly locate valuable information without blind scanning. Token-efficient and agent-agnostic.

## Map Boundary Charter

- `project-map` records project-native structure and relations using a layered `tree + graph` model.
- `.workspace` runtime artifacts are workflow data and must not be the primary recorded objects in `project-map`.
- `resource-map` may borrow the layered design idea, but remains independently modeled and maintained.

## Templates

- `templates/project-map-tree-node.template.json`
- `templates/project-map-graph-edge.template.json`
- `templates/map-boundary-charter.md`

## Usage

```
$jmf-init
```

- First-time only: creates .workspace/project-map/ from scratch
- If .workspace/project-map/ already exists: directs user to `jmf-sync`

## Pre-conditions

- `.workspace/project-map/` must NOT exist
- If .workspace/project-map/ exists: report ".workspace/project-map/ already exists. Use `jmf-sync` to update."

## Behavior

### 1. Check if .workspace/project-map/ exists

If `.workspace/project-map/` exists and `--refresh` not set: report "already initialized, use --refresh to re-run"

### 2. Discover project structure

**Top-level analysis:**
- Scan root directory (ls, glob patterns)
- Detect project type indicators (package.json, Cargo.toml, README, etc.)
- Determine if multi-project collection (`isCollection`)

**Entry point detection:**
- README, index.*, main.*, Makefile, docker-compose.yml, etc.
- Config files, .env templates, static resources

**Relationship inference:**
- Scan source files for import/require/reference statements
- Match against relationship types: depends-on, implements, contains, references, builds-on, delivers

### 3. Populate .workspace/project-map/

Write to `.workspace/project-map/` directory:

| File | Content |
|------|---------|
| `project.json` | Top-level metadata (name, type, description, domains[]) |
| `domains.json` | Domain/module nodes |
| `entries.json` | Entry point nodes |
| `assets.json` | Asset nodes (config, resources) |
| `relationships.json` | Typed relationship edges |
| `SUMMARY.md` | Human-readable navigation guide |
| `schema-reference.md` | Schema documentation |

Template-first rule:
- Generate/refresh tree-layer nodes following `templates/project-map-tree-node.template.json`
- Generate/refresh graph edges following `templates/project-map-graph-edge.template.json`
- Keep boundary language aligned with `templates/map-boundary-charter.md`

### 4. Handle unknowns gracefully

- If content/relationship cannot be determined: mark `confidence: low` and flag for user confirmation
- If user also cannot clarify: set description to `null` and relationship type to `unknown-type` — do not block
- Continue with partial map rather than failing

### 5. Token efficiency

- `SUMMARY.md` is the primary navigation doc — keep it small
- Detailed data in JSON files — loaded on demand
- Top-level `project.json` is always small — always loaded first
- Keep `.workspace/INDEX.md` and `.workspace/project-map/INDEX.md` updated as low-cost navigation anchors

### 6. Resources

**Check for resources:**
- After building .workspace/project-map/, check if `.workspace/resource-map/resources.json` exists
- If exists, load it and include resources in context

**Resource scan:**
- After init, ask user: "是否要扫描项目发现潜在资源？"
- If yes, use `jmf-resource scan` workflow to discover resources
- User confirms each resource before registration
- Scan is non-destructive — only suggests, never auto-registers

**Integration with PROJECT-MAP:**
- Keep resource details in `.workspace/resource-map/resources.json` as source of truth.
- `project-map` may keep lightweight references to resource context only when needed for navigation.

## Schema Reference

**Node types:** Domain, EntryPoint, Asset, Abstraction, Artifact, Unknown

**Relationship types:** depends-on, implements, contains, references, builds-on, delivers, unknown-type

See `.workspace/project-map/schema-reference.md` for full schema.

## Notes

- This skill is agent-agnostic — does not depend on Claude Code or any specific agent platform
- `jmf-discuss` reads `.workspace/project-map/SUMMARY.md` before starting each discuss phase
- Install/init guidance should explain `.workspace` semantics and git policy as recommendation (`.gitignore` by default, override allowed)
- User manually triggers this skill — it is NOT run automatically (token expensive)
- For updating an existing .workspace/project-map/, use `jmf-sync`
