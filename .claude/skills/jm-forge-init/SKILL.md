---
name: jm-forge-init
description: Analyze the current project and build a PROJECT-MAP context map. Run when introducing jm-forge to an existing project, or when --refresh is needed.
---

# Skill: jm-forge-init

## Purpose

Analyze the current working directory and build a `PROJECT-MAP/` context map that helps Agents quickly locate valuable information without blind scanning. Token-efficient and agent-agnostic.

## Usage

```
$jm-forge:init
```

- First-time only: creates PROJECT-MAP/ from scratch
- If PROJECT-MAP/ already exists: directs user to `jm-forge:sync`

## Pre-conditions

- `PROJECT-MAP/` must NOT exist
- If PROJECT-MAP/ exists: report "PROJECT-MAP/ already exists. Use `jm-forge:sync` to update."

## Behavior

### 1. Check if PROJECT-MAP/ exists

If `PROJECT-MAP/` exists and `--refresh` not set: report "already initialized, use --refresh to re-run"

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

### 3. Populate PROJECT-MAP/

Write to `PROJECT-MAP/` directory:

| File | Content |
|------|---------|
| `project.json` | Top-level metadata (name, type, description, domains[]) |
| `domains.json` | Domain/module nodes |
| `entries.json` | Entry point nodes |
| `assets.json` | Asset nodes (config, resources) |
| `relationships.json` | Typed relationship edges |
| `SUMMARY.md` | Human-readable navigation guide |
| `schema-reference.md` | Schema documentation |

### 4. Handle unknowns gracefully

- If content/relationship cannot be determined: mark `confidence: low` and flag for user confirmation
- If user also cannot clarify: set description to `null` and relationship type to `unknown-type` — do not block
- Continue with partial map rather than failing

### 5. Token efficiency

- `SUMMARY.md` is the primary navigation doc — keep it small
- Detailed data in JSON files — loaded on demand
- Top-level `project.json` is always small — always loaded first

### 6. Resources

**Check for resources:**
- After building PROJECT-MAP/, check if `RESOURCE-MAP/resources.json` exists
- If exists, load it and include resources in context

**Resource scan:**
- After init, ask user: "是否要扫描项目发现潜在资源？"
- If yes, use `jm-forge:resource scan` workflow to discover resources
- User confirms each resource before registration
- Scan is non-destructive — only suggests, never auto-registers

**Integration with PROJECT-MAP:**
- Resources are added as nodes with `type: "resource"` and `resource: true`
- They appear in `domains.json` under a `resources` domain

## Schema Reference

**Node types:** Domain, EntryPoint, Asset, Abstraction, Artifact, Unknown

**Relationship types:** depends-on, implements, contains, references, builds-on, delivers, unknown-type

See `PROJECT-MAP/schema-reference.md` for full schema.

## Notes

- This skill is agent-agnostic — does not depend on Claude Code or any specific agent platform
- `jm-forge:discuss` reads `PROJECT-MAP/SUMMARY.md` before starting each discuss phase
- User manually triggers this skill — it is NOT run automatically (token expensive)
- For updating an existing PROJECT-MAP/, use `jm-forge:sync`
