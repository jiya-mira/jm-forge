# execute.md: external-resources-support

**Source:** plan.md

---

## Steps

### Step 1: Define external-resources.json schema

**Status:** ✅ Completed

**Evidence:**
- Created `.external/external-resources.json` with full schema
- Sample entries for: equipment (翻斗车), infrastructure (服务器), organization (外包公司)
- JSON validated

---

### Step 2: Create jm-forge-external skill

**Status:** ✅ Completed

**Evidence:**
- Created `.claude/skills/jm-forge-external/SKILL.md`
- Sub-commands: add, list, remove, get
- Documented full workflow

---

### Step 3: Integrate external resources into jm-forge-init

**Status:** ✅ Completed

**Evidence:**
- Updated `.claude/skills/jm-forge-init/SKILL.md` Section 6
- init now checks for `.external/external-resources.json`
- init prompts user about external resources

---

### Step 4: Integrate external resources into jm-forge-sync

**Status:** ✅ Completed

**Evidence:**
- Updated `.claude/skills/jm-forge-sync/SKILL.md` Section 6
- sync includes external resources in sync scope

---

### Step 5: Add external-resource node type to PROJECT-MAP

**Status:** ✅ Completed

**Evidence:**
- Updated `PROJECT-MAP/schema-reference.md` with `external-resource` node type
- Added "External Resource Nodes" section with full schema
- Updated node types table

---

## Checkpoints

| Checkpoint | Status |
|------------|--------|
| schema-defined | ✅ Verified |
| skill-created | ✅ Verified |
| init-extended | ✅ Verified |
| sync-extended | ✅ Verified |
| project-map-extended | ✅ Verified |

---

## Final State: Completed

All 5 steps completed, all 5 checkpoints verified.
