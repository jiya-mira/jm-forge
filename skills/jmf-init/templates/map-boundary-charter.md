# Map Boundary Charter

- `project-map` records project-native structure and relations in a layered `tree + graph` model.
- `.workspace` runtime artifacts are workflow data and are not primary `project-map` recording targets.
- Tree layers expose next-layer minimal summaries and pointers only: `id`, `name`, `type`, `path`, `summary`, `children_ids`, `doc_ref`.
- Details are stored in leaf/detail files; avoid full-field duplication across layers.
- `resource-map` may borrow layered design ideas but keeps independent data ownership and evolution.
- `domains.json`, `entries.json`, `assets.json`, `relationships.json` remain the canonical graph-layer records.
