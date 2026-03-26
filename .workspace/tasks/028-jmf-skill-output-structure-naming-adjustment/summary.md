# Summary — jmf-skill-output-structure-naming-adjustment

**Task ID:** 28
**Date:** 2026-03-26
**Status:** Completed

---

## Goal
Unify runtime artifact layout under `.workspace`, remove root-level map directory pollution, and make path contracts navigable and stable for skill execution.

## Changes
- Migrated map directories to `.workspace/project-map`, `.workspace/resource-map`, `.workspace/exp-map`.
- Migrated registry-backed task directories to `.workspace/tasks/<id>-kebab-case`.
- Updated core skill path contracts and documentation to `.workspace` baseline.
- Added install-time directory guidance (recommended git policy, override allowed).
- Added index guides for key directories to improve navigation.
- Added migration utility script: `scripts/migrate-to-workspace-layout.sh`.

## Verification
- Dry-run and apply logs generated (`/tmp/task28-dry-run.txt`, `/tmp/task28-apply.log`).
- Root no longer contains `PROJECT-MAP`, `RESOURCE-MAP`, `EXP-MAP`.
- Key docs/skills no longer reference old root map paths in target scope.
- Index guide files exist for all required key directories.

## Risks / Follow-ups
- `.planning` still contains some non-registry historical directories/files; optional cleanup can be a follow-up task.
- Historical task documents may still contain legacy path strings; no functional blocker for current workflow.
