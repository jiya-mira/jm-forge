# Project Map Index

Directory index for `.workspace/project-map/`.

## Managed Files
- `INDEX.md`: human routing entry for this map directory.
- `SUMMARY.md`: compact semantic overview of domains/entries/relationships.
- `project.json`: map root metadata and global settings.
- `tree.json`: layered tree nodes for traversal (`children_ids` + `doc_ref`).
- `domains.json`: domain/module nodes.
- `entries.json`: entry-point nodes.
- `assets.json`: asset nodes.
- `relationships.json`: typed graph edges.
- `schema-reference.md`: schema and relationship type reference.

## Managed Directories
- None.

## Map Boundary Charter
- `project-map` records project-native structure and relations in a layered `tree + graph` model.
- `.workspace` runtime artifacts are workflow data and are not primary `project-map` recording targets.
- Tree layers expose next-layer minimal summaries and pointers only: `id`, `name`, `type`, `path`, `summary`, `children_ids`, `doc_ref`.
- Details are stored in leaf/detail files; avoid full-field duplication across layers.
- `resource-map` may borrow layered design ideas but keeps independent data ownership and evolution.
- `domains.json`, `entries.json`, `assets.json`, `relationships.json` remain the canonical graph-layer records.

## Cascade (Initial)
1. `INDEX.md` (start here)
2. `SUMMARY.md` (quick semantic context)
3. `project.json` (root metadata)
4. `tree.json` (layered traversal pointers)
5. `domains.json` / `entries.json` / `assets.json` (typed nodes)
6. `relationships.json` (cross-node links)
7. `schema-reference.md` (schema details)

## Navigation
- Fast path: `INDEX.md` -> `SUMMARY.md` -> needed JSON file.
- Deep path: `project.json` -> node files -> `relationships.json`.

## Update Rule
Update when any managed file role, path, or cascade order changes.
