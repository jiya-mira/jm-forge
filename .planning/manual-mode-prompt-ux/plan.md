# Plan — manual-mode-prompt-ux

**Date:** 2026-03-25
**Source:** discuss.md

---

## Steps

### Step 1: Audit current skill outputs

**Action:** Review all relevant skills to identify exact locations where Task ID is missing or inconsistently displayed.

**Approach:**
- Already completed: jmf-discuss, jmf-plan, jmf-execute, jmf-auto, jmf-status
- Gaps found:
  - **jmf-discuss** §4 Completion: summary prompt lacks Task ID
  - **jmf-plan** §5 Completion: summary prompt lacks Task ID
  - **jmf-execute** §2 Checkpoint format: lacks task context; §6 execute.md template header missing ID
  - **jmf-auto** §4 Progress Reporting: no Task ID; §Interaction Modes: stop prompt lacks Task ID
  - **jmf-status** §Output: Task header could be more explicit

**Checkpoint:** `audit-complete`
- All 5 skills reviewed and gaps documented

---

### Step 2: Update jmf-discuss SKILL.md

**Action:** Add Task ID to completion summary in §4 Completion.

**Approach:**
- Change "Present summary to user" → "Present summary with Task #\<id\> prominently displayed"
- Example: "**Task #24: manual-mode-prompt-ux** — Discuss complete. Ready for Plan."

**Checkpoint:** `discuss-updated`
- Skill file updated
- New completion message format recorded

---

### Step 3: Update jmf-plan SKILL.md

**Action:** Add Task ID to completion summary in §5 Completion.

**Approach:**
- Change "Offer to proceed to Execute phase" → "Present plan summary with Task #\<id\> prominently displayed"
- Example: "**Task #24: manual-mode-prompt-ux** — Plan complete. Ready for Execute."

**Checkpoint:** `plan-updated`
- Skill file updated
- New completion message format recorded

---

### Step 4: Update jmf-execute SKILL.md

**Action:** Add Task ID to checkpoint format, setup header, and execute.md template.

**Approach:**
- **§2 Checkpoint format**: Change `[Checkpoint N: <name>]` → `[Task #<id> | Checkpoint N: <name>]`
- **§1 Setup**: Add "Present Task #\<id\> header when starting execute"
- **§6 execute.md template**: Change `# Execute — <task-name>` → `# Execute — Task #<id>: <task-name>`

**Checkpoint:** `execute-updated`
- Skill file updated
- All three locations modified

---

### Step 5: Update jmf-auto SKILL.md

**Action:** Add Task ID to progress reporting and interaction mode stop prompts.

**Approach:**
- **§4 Progress Reporting**: Change format to include Task #\<id\>
  - Example: `[Task #24] Active → Completed — Task finished successfully`
- **§Interaction Modes**: When stopping for user input, include Task ID
  - Example: `[Task #24] Stopped — Awaiting your input on blocking issue`

**Checkpoint:** `auto-updated`
- Skill file updated
- Progress report format updated
- Stop prompt format updated

---

### Step 6: Update jmf-status SKILL.md

**Action:** Make Task ID more prominent in output header.

**Approach:**
- **§Output Task header**: Change format to `**Task #<id>: <name>**` (bold, explicit # prefix)

**Checkpoint:** `status-updated`
- Skill file updated
- Task header format improved

---

## Dependencies

All steps are independent — each skill is updated separately. Steps 2-6 can be done in parallel.

## Tracking

| Assumption | Risk |
|-----------|------|
| Changes are additive only (format/display), no behavior change | Low — skill logic unchanged |
| User approves format changes before finalizing | Low — format is simple and consistent |

## Execution Order

Parallel: Steps 2-6 can execute simultaneously after Step 1 audit is confirmed.
