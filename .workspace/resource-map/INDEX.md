# Resource Map Index

Directory index for `.workspace/resource-map/`.

## Managed Files
- `INDEX.md`: human routing entry for this map directory.
- `resources.json`: source of truth for resource entities and relationships.

## Managed Directories
- None.

## Map Boundary Charter
- `resource-map` is the source of truth for resource entities and lightweight relationships.
- `resource-map` borrows layered design ideas from `project-map`, but does not depend on `project-map` structure.
- `project-map` may keep navigation-only resource references; resource details remain in `resource-map`.
- Keep the relationship between `project-map` and `resource-map` thin; allow independent evolution.

## Cascade (Initial)
1. `INDEX.md` (start here)
2. `resources.json` (authoritative data)

## Navigation
- Read `INDEX.md` for usage and ownership.
- Read `resources.json` for full resource data and links.
- Use `jmf-resource` for managed updates.

## Update Rule
Update when resource schema usage, ownership boundary, or navigation guidance changes.
