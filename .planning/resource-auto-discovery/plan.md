# Plan — resource-auto-discovery

**Date:** 2026-03-23
**Source:** discuss.md (consumed)

---

## Steps

### Step 1: Add `scan` command to jm-forge-resource

**Action:** Update `.claude/skills/jm-forge-resource/SKILL.md` to add `scan` subcommand

**Approach:**
- Add `scan` command documentation
- Define scan workflow:
  1. Agent scans entire project directory
  2. Agent identifies potential resources (using own judgment, no fixed file list)
  3. Agent presents found candidates to user
  4. User confirms which to register
  5. Registered resources appended to RESOURCE-MAP/resources.json
- Scan is non-destructive: only suggests, never auto-registers

**Checkpoint:** `scan-command-added`
- SKILL.md contains `scan` command documentation
- Scan workflow includes user confirmation step

---

### Step 2: Integrate resource scan into jm-forge-init

**Action:** Update `.claude/skills/jm-forge-init/SKILL.md` Section 6

**Approach:**
- After building PROJECT-MAP/, check if RESOURCE-MAP/resources.json exists
- If RESOURCE-MAP exists or user requests, offer to scan for resources
- Scan entire project using same logic as `jm-forge-resource scan`
- Prompt: "是否要扫描项目发现潜在资源？"
- If yes, run scan and show candidates
- User confirms before registering

**Checkpoint:** `init-scan-integrated`
- Section 6 includes resource scan integration
- User is prompted about resource scanning after init

---

### Step 3: Integrate resource scan into jm-forge-sync

**Action:** Update `.claude/skills/jm-forge-sync/SKILL.md` Section 6

**Approach:**
- During sync, optionally offer to rescan for new resources
- Prompt: "是否要重新扫描项目发现新资源？"
- Same scan logic as `jm-forge-resource scan`
- User confirms before registering new discoveries

**Checkpoint:** `sync-scan-integrated`
- Section 6 includes resource scan integration
- User is prompted about resource scanning during sync

---

## Dependencies

| Step | Depends on |
|------|------------|
| Step 2 | Step 1 |
| Step 3 | Step 1 |

**Order:** Step 1 → (Step 2, Step 3 in parallel)

---

## Tracking

| Assumption | Risk |
|-----------|------|
| Agent can intelligently identify resources without fixed file patterns | Low — Agent has judgment capability |
| Scan won't inadvertently expose sensitive info | Low — scan only reads file metadata and content, doesn't transmit |

---

## Execution Order

**Parallel:** Steps 2 and 3 depend on Step 1's command structure, so execute Step 1 first, then Steps 2-3 in parallel.
