# Plan — skill-naming-overhaul

**Date:** 2026-03-23
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Update skill-naming-convention.md with new naming rule

**Action:** Add `jm-forge:<action>` as the recommended pattern for task-related skills

**Approach:**
- Read existing `.planning/skill-naming-convention.md`
- Append a section for "Task Workflow Skills" naming pattern
- State the format: `jm-forge:<action>` where action is one of: new, discuss, plan, execute, status, abandon, list, auto

**Checkpoint:** `naming-convention-updated`
- `skill-naming-convention.md` contains the new `jm-forge:<action>` pattern
- Old `jm-forge-task-*` pattern is marked as deprecated

---

### Step 2: Rename skill directories and SKILL.md files

**Action:** Rename `.claude/skills/jm-forge-task-*` directories to `jm-forge-*`

**Approach:**
- List all skills matching `jm-forge-task-*` in `.claude/skills/`
- For each: rename directory, update the skill `name` field in SKILL.md frontmatter
- Skills to rename:
  - `jm-forge-task-new` → `jm-forge-new` (note: `new` is a reserved word in some contexts — use `jm-forge:new` as invocation but filesystem name may need different handling)
  - `jm-forge-task-discuss` → `jm-forge-discuss`
  - `jm-forge-task-plan` → `jm-forge-plan`
  - `jm-forge-task-execute` → `jm-forge-execute`
  - `jm-forge-task-status` → `jm-forge-status`
  - `jm-forge-task-abandon` → `jm-forge-abandon`
  - `jm-forge-task-list` → `jm-forge-list`
  - `jm-forge-task-auto` → `jm-forge-auto`

**Note:** The skill `name` in SKILL.md frontmatter controls the slash command. If `name: jm-forge:new`, the slash command becomes `/jm-forge:new`. If `name` only allows hyphens, we may need to use `jm-forge-new` as the slash command and document the `:` as cosmetic/brand only.

**Checkpoint:** `skill-directories-renamed`
- All 8 `jm-forge-task-*` directories renamed to `jm-forge-*`
- SKILL.md `name` field updated to match new pattern
- Skills directory in `skills/` (canonical source) also updated if present

---

### Step 3: Update SKILL.md content references

**Action:** Update all skill documentation and internal references to use new naming

**Approach:**
- In each renamed skill's SKILL.md, update any references to other skills (e.g. "use `$jm-forge-task-plan`" becomes "use `$jm-forge-plan`")
- Update AGENTS.md skill registry to show new names

**Checkpoint:** `skill-docs-updated`
- All SKILL.md files reference new naming
- AGENTS.md skill table updated

---

### Step 4: Verify slash command invocation

**Action:** Test or document that slash commands work with new names

**Approach:**
- If Claude Code `name` field restriction applies (lowercase/hyphens only), document the workaround
- If other agents accept `:` in names, confirm they work
- Update SKILL.md invocation examples accordingly

**Checkpoint:** `invocation-documented`
- SKILL.md contains clear slash command example
- Any Claude Code specific workaround documented

---

### Step 5: Update TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） notes

**Action:** Update Task 3's description to reflect new naming convention

**Approach:**
- Change "jm-forge-task-*" in Task 3 notes to "jm-forge-*"

**Checkpoint:** `registry-updated`
- TASK-REGISTRY.md（legacy；现对应 `.workspace/tasks/INDEX.md`） Task 3 notes reflect new naming

---

## Dependencies

Steps 1, 2, 3, 5 are largely independent. Step 4 (verification) depends on Step 2.

## Tracking

| Assumption | Risk |
|-----------|------|
| `:` is valid in skill names on Gemini/Codex | Medium — user will test empirically |
| Skill `name` field allows `:` on target agents | High — if not, may need fallback to hyphen |
| File system rename doesn't break symlinks or references | Low — `skills/` is canonical, `.claude/skills/` is copy |

## Execution Order

Sequential: 1 → 2 → 3 → 4 → 5
