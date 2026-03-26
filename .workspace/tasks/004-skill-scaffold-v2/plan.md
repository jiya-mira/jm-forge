# Plan — skill-scaffold-v2

**Date:** 2026-03-23
**Task ID:** 4
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: update-scaffold-script

**Action:** Modify `skills/skill-scaffold/scaffold.py` to auto-detect skill type.

**Approach:**
- Remove `--type` flag (not needed)
- Agent decides based on skill purpose:
  - If skill requires CLI tool/script → Python/uv mode
  - If skill is Agent-executed (SKILL.md only) → Agent mode
- If ambiguous: ask user "Does this skill need a Python script? (y/N)" with explanation of why

**Checkpoint:** `scaffold-script-updated`

---

### Step 2: update-skill-md-documentation

**Action:** Update SKILL.md to document the new auto-detection behavior.

**Approach:**
- Remove `--type` flag documentation
- Document that Agent auto-detects skill type
- Show example of what gets generated for each type

**Checkpoint:** `skill-md-updated`

---

## Dependencies

Steps 1 and 2 are independent and can be done in parallel.

## Execution Order

Parallel execution allowed.
