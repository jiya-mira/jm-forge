# execute.md: resource-map-redesign

**Source:** plan.md

---

## Steps

### Step 1: Rename skill directory

**Status:** ✅ Completed

**Evidence:**
- Renamed `.claude/skills/jm-forge-external` → `.claude/skills/jm-forge-resource`
- Directory `.claude/skills/jm-forge-resource` exists
- Old directory no longer exists

---

### Step 2: Update skill name in SKILL.md

**Status:** ✅ Completed

**Evidence:**
- `name: jm-forge-resource` in SKILL.md
- Description updated to reflect broader scope
- Command updated from `$jm-forge:external` to `$jm-forge:resource`

---

### Step 3: Rename and update resources file

**Status:** ✅ Completed

**Evidence:**
- Renamed `RESOURCE-MAP/external-resources.json` → `RESOURCE-MAP/resources.json`
- Updated schema from `jm-forge:external-resources:v1` to `jm-forge:resource-map:v1`
- Updated description

---

### Step 4: Update jm-forge-init references

**Status:** ✅ Completed

**Evidence:**
- Section 6 renamed "External Resources" → "Resources"
- `.external/external-resources.json` → `RESOURCE-MAP/resources.json`
- `jm-forge:external add` → `jm-forge:resource add`
- No remaining `.external/` references

---

### Step 5: Update jm-forge-sync references

**Status:** ✅ Completed

**Evidence:**
- Section 6 renamed "External Resources" → "Resources"
- `.external/external-resources.json` → `RESOURCE-MAP/resources.json`
- `jm-forge:external add` → `jm-forge:resource add`
- No remaining `.external/` references

---

### Step 6: Update schema-reference.md

**Status:** ✅ Completed

**Evidence:**
- `external-resource` node type replaced with `resource`
- Path updated to `RESOURCE-MAP/resources.json`
- "External Resource Nodes" section renamed to "Resource Nodes"
- No remaining `.external/` references

---

## Checkpoints

| Checkpoint | Status |
|------------|--------|
| skill-renamed | ✅ Verified |
| skill-updated | ✅ Verified |
| file-renamed | ✅ Verified |
| init-updated | ✅ Verified |
| sync-updated | ✅ Verified |
| schema-reference-updated | ✅ Verified |

---

## Final State: Completed

All 6 steps completed, all 6 checkpoints verified.

**Key Changes:**
- `.external/` → `RESOURCE-MAP/`
- `jm-forge-external` → `jm-forge-resource`
- `external-resources.json` → `resources.json`
- `external-resource` node type → `resource`
- Skill command: `$jm-forge:external` → `$jm-forge:resource`
