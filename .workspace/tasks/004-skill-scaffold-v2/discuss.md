# Discuss — skill-scaffold-v2

**Date:** 2026-03-23
**Status:** Concluded
**Task ID:** 4

---

## Goal

Improve skill-scaffold to generate jm-forge-task-* series skills. Both Python and Agent-only skills supported, with Agent-only as the primary mode.

**Source:** discuss-log.md → Iteration 1

---

## Boundary

- **In scope:** Skill generation modes, template selection, manifest updates
- **Out of scope:** Existing skills in manifest, CI/CD

**Source:** discuss-log.md → Iteration 1

---

## Assumptions

1. Agent-only skills only need SKILL.md
2. Python skills still need main.py + validate.py
3. User chooses which type to generate

**Source:** discuss-log.md → Iteration 1

---

## Acceptance Criteria

1. `skill-scaffold-v2` can generate Agent-only skills (SKILL.md only)
2. `skill-scaffold-v2` can still generate Python skills when needed
3. Manifest.json is updated for new skills

**Source:** discuss-log.md → Iteration 1

---

## Open Issues

None — all issues are non-blocking.

---

## Conclusion

Goal confirmed. Ready to proceed to Plan.

**Source:** discuss-log.md → Iteration 1
