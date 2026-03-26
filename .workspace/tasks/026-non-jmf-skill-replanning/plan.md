# Plan — non-jmf-skill-replanning

**Date:** 2026-03-26
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Lock classification policy

**Action:** Define which non-`jmf-*` skills are counted as user-facing/runtime skills and which are internal build-time helpers.

**Approach:**
- Treat `workflow-execute` as the single user-facing non-`jmf-*` runtime/router skill
- Treat `skill-scaffold` as an internal build-time helper exception that is not counted in the user-facing runtime total
- Write the classification explicitly so later migration work does not re-open the same ambiguity

**Checkpoint:** `classification-policy-locked`
- The counting rule is explicit in the task documents
- The exception category for `skill-scaffold` is documented
- The retained role of `workflow-execute` is stated as a thin router/entry skill

---

### Step 2: Thin down the router skill

**Action:** Reduce `workflow-execute` to a thin bootstrap/router skill that delegates to the `jmf-*` workflow skills instead of duplicating workflow logic.

**Approach:**
- Keep only the minimal entry behavior needed for navigation and phase handoff
- Remove heavy workflow ownership from the router and defer core behavior to `jmf-discuss`, `jmf-plan`, and `jmf-execute`
- Align the skill description and usage language with its reduced role

**Checkpoint:** `router-skill-thinned`
- `workflow-execute` reads as a lightweight entry/router skill
- Core workflow semantics live in the `jmf-*` phase skills
- The router no longer presents itself as the primary workflow implementation

---

### Step 3: Sync metadata and docs

**Action:** Update registry, manifests, project map, and user-facing docs to reflect the new naming boundary.

**Approach:**
- Update `skills/manifest.json` and the `.claude` skill copy for the retained router skill
- Update `AGENTS.md` and any project-map descriptions so they no longer imply multiple user-facing non-`jmf-*` runtime skills
- Preserve `skill-scaffold` as an internal exception in docs and map text, not as a user-facing runtime entry

**Checkpoint:** `metadata-synced`
- Registry and manifest text match the chosen boundary
- Project map no longer implies the old non-`jmf-*` grouping
- Documentation clearly distinguishes user-facing runtime skills from internal helpers

---

## Dependencies

Step 1 must complete before Steps 2 and 3 so the later edits use a single, explicit rule.
Step 2 should complete before Step 3 so the metadata reflects the final shape of the router skill.

## Tracking

| Assumption | Risk |
|-----------|------|
| `skill-scaffold` can remain an internal exception without confusing users | Medium — the docs must be explicit or the exception will look like drift |
| `workflow-execute` can be reduced to a thin router without breaking current usage expectations | Medium — some references may still assume it is the main orchestrator |
| The repo only needs one user-facing non-`jmf-*` runtime skill | Low — matches the agreed boundary |

## Execution Order

Sequential with dependencies noted
