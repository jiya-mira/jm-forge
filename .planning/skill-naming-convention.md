# Skill Naming Convention

> Last updated: 2026-03-23

---

## 1. Skill Naming

### Directory Names
- Format: **kebab-case** (all lowercase, words separated by hyphens)
- Example: `workflow-execute`, `jm-forge-bootstrap`, `skill-scaffold`

### Skill `name` Field (SKILL.md frontmatter)
- Must match the directory name exactly
- Example: `name: workflow-execute` in `workflow-execute/SKILL.md`

**Why kebab-case?**
- Universal across file systems (Linux, macOS, Windows)
- Readable without case ambiguity
- Consistent with npm/package conventions

---

### Task Workflow Skills (jm-forge:*)

Task management skills follow `jm-forge:<action>` pattern:

| Skill | Invocation | Purpose |
|-------|-----------|---------|
| `jm-forge-new` | `/jm-forge:new` | Create a new task |
| `jm-forge-discuss` | `/jm-forge:discuss` | Conduct Discuss phase |
| `jm-forge-plan` | `/jm-forge:plan` | Conduct Plan phase |
| `jm-forge-execute` | `/jm-forge:execute` | Conduct Execute phase |
| `jm-forge-status` | `/jm-forge:status` | Show task details |
| `jm-forge-abandon` | `/jm-forge:abandon` | Mark task abandoned |
| `jm-forge-list` | `/jm-forge:list` | List all tasks |
| `jm-forge-auto` | `/jm-forge:auto` | Auto-advance through phases |

**Components:**
- **Brand:** `jm` (brand identifier)
- **Separator:** `:` (namespace-style separator)
- **Action:** short verb identifying the operation

**Note:** The `name` field in SKILL.md controls the slash command on each agent. Some agents (e.g. Claude Code) restrict `name` to lowercase/hyphens only. In that case, use `jm-forge-<action>` as the `name` field and document `jm-forge:<action>` as the brand/invocation name.

---

## 2. Task Naming

### Planning Artifacts
- Task directory under `.planning/`: **kebab-case** matching the task identifier
- Example: `.planning/workflow-framework/`

### Plan Documents
- `plan.md` — all lowercase, no separator
- `discuss.md` — all lowercase, no separator
- `execute.md` — all lowercase, no separator

### Step Naming
- Format: **verb-noun** in present tense
- Example: `define-task-boundaries`, `write-references`, `validate-checkpoints`
- Use imperative form (imperative mood for consistency)

### Checkpoint Naming
- Format: **past-participle** describing the verified state
- Example: `task-boundaries-defined`, `references-documented`, `checkpoints-validated`
- Checkpoint names in execute.md must match exactly the checkpoint identifiers in plan.md

---

## 3. Enforcement

- All new skills must follow skill naming convention at creation time
- Task/step/checkpoint naming enforced during planning phase
- Compliance is manual; no automatic enforcement tool
