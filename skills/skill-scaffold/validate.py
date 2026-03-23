#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Validate: skill-scaffold
"""

import subprocess
import sys
from pathlib import Path


def main():
    print("Validating skill: skill-scaffold")

    script = Path("skills/skill-scaffold/scaffold.py")

    if not script.exists():
        print(f"FAIL: Missing {script}")
        sys.exit(1)

    # Test: running with no args should fail with usage
    result = subprocess.run(
        ["uv", "run", "skills/skill-scaffold/scaffold.py"],
        capture_output=True
    )
    if result.returncode == 0:
        print("FAIL: Should exit with error when no args provided")
        sys.exit(1)

    # Test: invalid name should fail
    result = subprocess.run(
        ["uv", "run", "skills/skill-scaffold/scaffold.py", "Invalid Name"],
        capture_output=True
    )
    if result.returncode == 0:
        print("FAIL: Should reject invalid skill names")
        sys.exit(1)

    # Test: valid name should create directory
    test_skill = Path("skills/test-valid-name")
    if test_skill.exists():
        import shutil
        shutil.rmtree(test_skill)

    result = subprocess.run(
        ["uv", "run", "skills/skill-scaffold/scaffold.py", "test-valid-name"],
        capture_output=True
    )
    if result.returncode != 0:
        print(f"FAIL: Script failed: {result.stderr.decode()}")
        sys.exit(1)

    if not test_skill.exists():
        print("FAIL: Skill directory not created")
        sys.exit(1)

    if not (test_skill / "skill.md").exists():
        print("FAIL: skill.md not created")
        sys.exit(1)

    if not (test_skill / "validate.py").exists():
        print("FAIL: validate.py not created")
        sys.exit(1)

    if not (test_skill / "main.py").exists():
        print("FAIL: main.py not created")
        sys.exit(1)

    # Cleanup
    import shutil
    shutil.rmtree(test_skill)

    print("Validation passed")


if __name__ == "__main__":
    main()
