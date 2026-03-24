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
- **Do NOT use this script.** Create SKILL.md manually in `.claude/skills/<name>/`

**Python skill** (requires CLI script):
- Skills that need actual CLI tools/scripts
- Uses `uv run` to execute
- **Use this script** to scaffold: `uv run skills/skill-scaffold/scaffold.py <name>`

### Decision Flow

When user asks to create a skill:

1. **Does the skill need a Python script or CLI tool?**
   - If **Yes** → Use `scaffold.py`, generates SKILL.md + main.py + validate.py
   - If **No** (Agent-executed) → Create SKILL.md manually in `.claude/skills/<name>/`

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
1. Copy SKILL.md to `.claude/skills/<skill-name>/` for Claude Code discovery
2. Add skill name to `skills/manifest.json`
3. **Update PROJECT-MAP/**: If `PROJECT-MAP/` exists, append new skill node to `domains.json` or `assets.json` (type: Domain or Asset) and add relationship edges

## Requirements

- Skill name: lowercase, hyphenated (e.g., `code-review`, `jm-forge:new`)
- No spaces or special characters

## Notes

- For updating existing PROJECT-MAP/, use `jm-forge:sync`
