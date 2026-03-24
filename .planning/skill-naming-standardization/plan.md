# plan.md

**Source:** discuss.md

---

## Goal

规范化jm-forge技能命名规则，所有技能统一使用 `jm-forge:<action>` (冒号) 格式。

---

## Step Decomposition

### Step 1: Update jm-forge-* SKILL.md name fields

**Action:**
- Update all 13 jm-forge-* skill SKILL.md files to change `name: jm-forge-<action>` to `name: jm-forge:<action>`

**Files to update:**
- `.claude/skills/jm-forge-abandon/SKILL.md`
- `.claude/skills/jm-forge-auto/SKILL.md`
- `.claude/skills/jm-forge-bootstrap/SKILL.md`
- `.claude/skills/jm-forge-discuss/SKILL.md`
- `.claude/skills/jm-forge-execute/SKILL.md`
- `.claude/skills/jm-forge-init/SKILL.md`
- `.claude/skills/jm-forge-list/SKILL.md`
- `.claude/skills/jm-forge-new/SKILL.md`
- `.claude/skills/jm-forge-plan/SKILL.md`
- `.claude/skills/jm-forge-resource/SKILL.md`
- `.claude/skills/jm-forge-status/SKILL.md`
- `.claude/skills/jm-forge-sync/SKILL.md`
- `.claude/skills/workflow-execute/SKILL.md` (also jm-forge: prefixed but name field needs update)

**Checkpoint:** `skill-names-updated`
- `grep "^name: jm-forge:" .claude/skills/*/SKILL.md` returns all 13 skills with colon format

---

### Step 2: Update bootstrap SKILL.md old references

**Action:**
- Update `.claude/skills/jm-forge-bootstrap/SKILL.md` to replace all `jm-forge-task-*` references with `jm-forge:<action>` format

**Checkpoint:** `bootstrap-cleaned`
- `grep "jm-forge-task-" .claude/skills/jm-forge-bootstrap/SKILL.md` returns empty
- All 8 skill names in table use `jm-forge:<action>` format

---

### Step 3: Update skill-scaffold SKILL.md old references

**Action:**
- Update `.claude/skills/skill-scaffold/SKILL.md` to replace `jm-forge-task-*` with `jm-forge:<action>`

**Checkpoint:** `skill-scaffold-cleaned`
- `grep "jm-forge-task-" .claude/skills/skill-scaffold/SKILL.md` returns empty

---

### Step 4: Update TASK-REGISTRY.md Task 3

**Action:**
- Update Task 3 description from `jm-forge-task-* skills` to `jm-forge:<action>` format

**Checkpoint:** `registry-updated`
- TASK-REGISTRY.md Task 3 notes contain `jm-forge:` instead of `jm-forge-task-`

---

## Dependencies

- All steps are independent (can be done in any order)

**Total:** 4 steps, no dependencies (can batch)

---

## Tracking

### Assumptions

1. SKILL.md `name` field accepts colon format
2. `.gemini/skills/` symlinks auto-sync (no manual update needed)
3. `skills/` directory stays in sync with `.claude/skills/`

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Colon format not supported in name field | Low | High | Revert to hyphen if needed |
| Grep miss replacements | Low | Medium | Manual verification after each step |
