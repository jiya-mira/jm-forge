# Plan — resource-map-redesign

**Date:** 2026-03-23
**Source:** discuss.md (consumed)

---

## Steps

### Step 1: Rename skill directory

**Action:** Rename `.claude/skills/jm-forge-external` to `.claude/skills/jm-forge-resource`

**Approach:**
- Use bash mv command to rename directory

**Checkpoint:** `skill-renamed`
- Directory `.claude/skills/jm-forge-resource` exists
- Directory `.claude/skills/jm-forge-external` no longer exists

---

### Step 2: Update skill name in SKILL.md

**Action:** Update the skill metadata and content in `.claude/skills/jm-forge-resource/SKILL.md`

**Approach:**
- Change `name: jm-forge-external` to `name: jm-forge-resource`
- Update description to reflect broader scope
- No functional changes to commands (add/list/remove/get remain)

**Checkpoint:** `skill-updated`
- SKILL.md has `name: jm-forge-resource`
- Description reflects "resource" not "external resource"

---

### Step 3: Rename and update resources file

**Action:** Rename `RESOURCE-MAP/external-resources.json` to `RESOURCE-MAP/resources.json` and update internal schema comments

**Approach:**
- Rename file via bash mv
- Update "$schema" comment from "jm-forge:external-resources:v1" to "jm-forge:resource-map:v1"
- Update description field

**Checkpoint:** `file-renamed`
- File `RESOURCE-MAP/resources.json` exists
- File `RESOURCE-MAP/external-resources.json` does not exist
- JSON schema comment updated

---

### Step 4: Update jm-forge-init references

**Action:** Update `.claude/skills/jm-forge-init/SKILL.md` references

**Approach:**
- Change `.external/external-resources.json` to `RESOURCE-MAP/resources.json`
- Change "external resources" wording to "resources" where appropriate
- Update Section 6 heading if needed

**Checkpoint:** `init-updated`
- No references to `.external/` or `external-resources.json` remain in jm-forge-init

---

### Step 5: Update jm-forge-sync references

**Action:** Update `.claude/skills/jm-forge-sync/SKILL.md` references

**Approach:**
- Change `.external/external-resources.json` to `RESOURCE-MAP/resources.json`
- Change "external resources" wording to "resources" where appropriate

**Checkpoint:** `sync-updated`
- No references to `.external/` or `external-resources.json` remain in jm-forge-sync

---

### Step 6: Update schema-reference.md

**Action:** Update `PROJECT-MAP/schema-reference.md` references

**Approach:**
- Change "external-resource" node type description to reflect resource-map context
- Update path reference: "External resources are stored in `.external/external-resources.json`" → "Resources are stored in `RESOURCE-MAP/resources.json`"

**Checkpoint:** `schema-reference-updated`
- No references to `.external/` or `external-resources.json` remain

---

## Dependencies

All steps are sequential. Each step depends on the previous step completing.

| Step | Depends on |
|------|------------|
| Step 2 | Step 1 |
| Step 3 | — |
| Step 4 | Step 2, Step 3 |
| Step 5 | Step 2, Step 3 |
| Step 6 | Step 3 |

**Order:** Step 1 → Step 2 → Step 3 → (Step 4, Step 5, Step 6 in parallel)

---

## Tracking

| Assumption | Risk |
|-----------|------|
| No other files reference `.external/` or `jm-forge-external` | Medium — may miss some references |
| User has not yet deployed jm-forge-external to other projects | Low — if deployed, those need updating too |

---

## Execution Order

**Sequential with parallel batch:** Steps 1-3 sequential, then Steps 4-6 can run in parallel after Step 3 completes.
