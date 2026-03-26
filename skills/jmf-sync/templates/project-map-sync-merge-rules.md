# Project Map Sync Merge Rules

- Preserve user-authored descriptions unless `--force-refresh` is used.
- Mark broken references as `stale: true` instead of hard deletion in incremental mode.
- Keep tree node minimal fields stable (`id`, `path`, `children_ids`) to preserve traversal.
- Recompute graph edges when sources change; keep confidence explicit.
- Never upgrade `.workspace` runtime artifacts into primary project-map nodes.
