#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
skill-scaffold: Generate standard skill directory structure.
"""

import re
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run scaffold.py <skill-name>")
        print("Example: uv run scaffold.py code-review")
        sys.exit(1)

    skill_name = sys.argv[1]

    # Validate skill name format
    if not re.match(r"^[a-z][a-z0-9-]*$", skill_name):
        print(f"Error: Invalid skill name '{skill_name}'")
        print("Use lowercase letters, numbers, and hyphens only. Must start with a letter.")
        sys.exit(1)

    skill_dir = Path("skills") / skill_name

    if skill_dir.exists():
        print(f"Error: Skill '{skill_name}' already exists at {skill_dir}")
        sys.exit(1)

    print(f"Creating skill: {skill_name}")

    skill_dir.mkdir(parents=True)

    # Create SKILL.md
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(f"""---
name: {skill_name}
description: (TODO: Describe what this skill does and when to use it)
---

# Skill: {skill_name}

## Purpose

(TODO: Describe what this skill does)

## Usage

```bash
uv run skills/{skill_name}/main.py
```

## Implementation

(TODO: Describe how this skill works)
""")

    # Create validate.py
    validate_py = skill_dir / "validate.py"
    validate_py.write_text(f"""#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
\"\"\"
Validate: {skill_name}
\"\"\"

def main():
    print("Validating skill: {skill_name}")

    # TODO: Add validation logic
    # - Check required files exist
    # - Verify script syntax
    # - Test basic functionality

    print("Validation passed")


if __name__ == "__main__":
    main()
""")

    # Create main.py template
    main_py = skill_dir / "main.py"
    main_py.write_text(f"""#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
\"\"\"
Skill: {skill_name}
\"\"\"

def main():
    # TODO: Implement skill
    pass


if __name__ == "__main__":
    main()
""")

    print(f"Created {skill_dir}/")
    print("- SKILL.md (template with frontmatter)")
    print("- validate.py")
    print("- main.py")

    # Copy to .claude/skills/ for Claude Code discovery
    claude_skills_dir = Path(".claude/skills") / skill_name
    claude_skills_dir.mkdir(parents=True, exist_ok=True)
    import shutil
    shutil.copy(skill_dir / "SKILL.md", claude_skills_dir / "SKILL.md")
    print(f"Copied SKILL.md to {claude_skills_dir}/ for Claude Code")

    print("")
    print("Next: Edit SKILL.md and main.py, then add to manifest.json")


if __name__ == "__main__":
    main()
