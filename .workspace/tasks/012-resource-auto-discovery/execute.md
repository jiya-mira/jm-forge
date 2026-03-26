# execute.md: resource-auto-discovery

**Source:** plan.md

---

## Steps

### Step 1: Add `scan` command to jm-forge-resource

**Status:** ✅ Completed

**Evidence:**
- Added `scan` command to SKILL.md
- Defined scan workflow: scan → identify → present candidates → user confirms → register
- Added Installation Notes section
- Added example scan output

---

### Step 2: Integrate resource scan into jm-forge-init

**Status:** ✅ Completed

**Evidence:**
- Section 6 updated with "Resource scan" subsection
- Added prompt: "是否要扫描项目发现潜在资源？"
- User confirmation before registration documented
- Scan is non-destructive

---

### Step 3: Integrate resource scan into jm-forge-sync

**Status:** ✅ Completed

**Evidence:**
- Section 6 updated with "Resource scan" subsection
- Added prompt: "是否要重新扫描项目发现新资源？"
- Same confirmation workflow as init
- Scan is non-destructive

---

## Checkpoints

| Checkpoint | Status |
|------------|--------|
| scan-command-added | ✅ Verified |
| init-scan-integrated | ✅ Verified |
| sync-scan-integrated | ✅ Verified |

---

## Final State: Completed

All 3 steps completed, all 3 checkpoints verified.

**New capability:**
- `/jm-forge-resource scan` — 独立命令，用户主动触发
- init 后自动询问是否扫描
- sync 后自动询问是否扫描
- 用户确认后才注册
