---
name: skill-scaffold
description: Generate a new skill directory structure. Use when creating a new skill for this framework.
---

# Skill: skill-scaffold

## Purpose

Generates standard skill directory structure for this framework.

## Usage

```bash
uv run skills/skill-scaffold/scaffold.py <skill-name>
```

## Skill Type Decision (Important)

Before calling this script, Agent must decide what type of skill is needed:

**Agent-only skill** (SKILL.md only, no Python):
- Most skills fall here
- Skills executed purely by Agent through SKILL.md instructions
- **Do NOT use this script.** Create SKILL.md manually in `skills/<name>/`

**Python skill** (requires CLI script):
- Skills that need actual CLI tools/scripts
- Uses `uv run` to execute
- **Use this script** to scaffold: `uv run skills/skill-scaffold/scaffold.py <name>`

### Decision Flow

When user asks to create a skill:

1. **Does the skill need a Python script or CLI tool?**
   - If **Yes** → Use `scaffold.py`, generates SKILL.md + main.py + validate.py
   - If **No** (Agent-executed) → Create SKILL.md manually in `skills/<name>/`

2. **If uncertain** → Ask user:
   > "Does this skill need a Python script? Skills that only provide instructions to the Agent (like jm-forge:*) don't need Python. But if it runs CLI tools or scripts, Python is needed."

## Output (Python mode)

When using scaffold.py, creates:
```
skills/<skill-name>/
├── SKILL.md          # Skill definition template
├── validate.py       # Standard validation script
└── main.py          # Skill entry point
```

## Registration

After creation:
1. **Development**: Skill is created directly in `skills/<skill-name>/` (meta-source)
2. **Publish**: Use `uv run scripts/install-workspaces-skills.py --all` to deploy to target directories
3. **Update .workspace/project-map/**: If `.workspace/project-map/` exists, append new skill node to `domains.json` or `assets.json` (type: Domain or Asset) and add relationship edges

**Development/Publish Flow:**
```
skills/<skill-name>/          ← Development happens here
    ↓
uv run scripts/install-workspaces-skills.py --all    ← Publish via install script
    ↓
.claude/skills/<skill-name>/  ← Claude Code target
.gemini/skills/<skill-name>/  ← Gemini CLI target
.agents/skills/<skill-name>/  ← Codex CLI target
```

## Requirements

- Skill name: lowercase, hyphenated (e.g., `code-review`, `jm-forge:new`)
- No spaces or special characters

## Notes

- For updating existing .workspace/project-map/, use `jm-forge:sync`
