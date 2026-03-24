#!/usr/bin/env python3
"""
jm-forge Workspace Skills Installer

Unified installer for jm-forge skills across multiple AI agents.
Supports: Claude Code, Gemini CLI, OpenCode, Codex CLI

Usage:
    # Interactive mode (default)
    uvx scripts/install-workspaces-skills.py

    # Non-interactive mode - install all to all agents
    uvx scripts/install-workspaces-skills.py --all

    # Non-interactive mode - force update
    uvx scripts/install-workspaces-skills.py --all --force

    # Non-interactive mode - specific agents
    uvx scripts/install-workspaces-skills.py --agents claude gemini opencode

Requirements:
    - uv (https://astral.sh/uv)
    - questionary (for interactive mode)
"""

import argparse
import shutil
import sys
import os
from pathlib import Path
from typing import List, Optional

try:
    import questionary
    QUESTIONARY_AVAILABLE = True
except ImportError:
    QUESTIONARY_AVAILABLE = False


# Configuration
META_SKILL_SOURCE = Path("skills")
TARGET_AGENTS = {
    ".claude/skills/": "Claude Code",
    ".gemini/skills/": "Gemini CLI",
    ".opencode/skills/": "OpenCode",
    ".agents/skills/": "Codex CLI",
}
AGENT_ALIASES = {
    "claude": ".claude/skills/",
    "gemini": ".gemini/skills/",
    "opencode": ".opencode/skills/",
    "codex": ".agents/skills/",
}


def get_skills(skills_dir: Path) -> tuple[List[Path], List[Path]]:
    """Get published and dev skills based on naming convention.

    Published skills: jmf-* (installed by default)
    Dev skills: others (opt-in)
    """
    if not skills_dir.exists():
        return [], []

    all_skills = [d for d in skills_dir.iterdir() if d.is_dir()]

    published = [s for s in all_skills if s.name.startswith("jmf-")]
    dev = [s for s in all_skills if not s.name.startswith("jmf-")]

    return published, dev


def select_agents_interactive() -> List[str]:
    """Prompt user to select target agents (interactive mode)."""
    if not QUESTIONARY_AVAILABLE:
        print("Error: questionary is required for interactive mode.")
        print("Install with: uv sync")
        sys.exit(1)

    choices = [
        questionary.Choice(f"{path} ({name})", path)
        for path, name in TARGET_AGENTS.items()
    ]

    selected = questionary.checkbox(
        "选择要安装技能的目标 Agent：",
        choices=choices,
    ).ask()

    return selected if selected else []


def select_skill_mode_interactive() -> bool:
    """Prompt user to select skill installation mode (interactive mode)."""
    if not QUESTIONARY_AVAILABLE:
        return False

    include_dev = questionary.confirm(
        "是否包含开发技能（skill-scaffold, workflow-execute）？",
        default=False,
    ).ask()

    return include_dev


def install_skills(target_path: Path, skills: List[Path], force: bool = False) -> dict:
    """Install skills to target directory.

    Returns:
        Dict with 'installed', 'updated', and 'skipped' skill names.
    """
    result = {"installed": [], "updated": [], "skipped": []}

    # Create target directory if it doesn't exist
    target_path.mkdir(parents=True, exist_ok=True)

    for skill in skills:
        dest = target_path / skill.name

        if dest.exists():
            if not force:
                result["skipped"].append(skill.name)
                continue
            
            # Remove existing directory/file
            if dest.is_dir():
                shutil.rmtree(dest)
            else:
                dest.unlink()
            
            shutil.copytree(skill, dest)
            result["updated"].append(skill.name)
        else:
            shutil.copytree(skill, dest)
            result["installed"].append(skill.name)

    return result


def print_results(agent_name: str, target: str, result: dict):
    """Print installation results."""
    print(f"\n{'='*50}")
    print(f"Agent: {agent_name} ({target})")
    print(f"{'='*50}")

    if result["installed"]:
        print(f"  已安装 ({len(result['installed'])}):")
        for name in sorted(result["installed"]):
            print(f"    + {name}")

    if result["updated"]:
        print(f"  已更新 ({len(result['updated'])}):")
        for name in sorted(result["updated"]):
            print(f"    * {name}")

    if result["skipped"]:
        print(f"  已跳过 ({len(result['skipped'])}):")
        for name in sorted(result["skipped"]):
            print(f"    - {name}")

    if not any(result.values()):
        print("  (无技能)")

    if agent_name == "OpenCode":
        print("\n  [OpenCode 提示]")
        print("  请确保您的 AGENTS.md 包含对这些技能的描述，")
        print("  或者将 .opencode/skills 目录添加到您的工具扫描路径中。")


def resolve_agent(alias_or_path: str) -> Optional[str]:
    """Resolve agent alias or path to full path."""
    if alias_or_path in AGENT_ALIASES:
        return AGENT_ALIASES[alias_or_path]
    if alias_or_path in TARGET_AGENTS:
        return alias_or_path
    return None


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="jm-forge Workspace Skills Installer (JMF Standard Edition)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  uvx scripts/install-workspaces-skills.py

  # Install all JMF skills to all agents
  uvx scripts/install-workspaces-skills.py --all

  # Force update existing skills
  uvx scripts/install-workspaces-skills.py --all --force

  # Install to specific agents
  uvx scripts/install-workspaces-skills.py --agents claude gemini opencode
        """
    )

    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="安装到所有已知的 Agent（Claude, Gemini, OpenCode, Codex）"
    )

    parser.add_argument(
        "--agents",
        nargs="+",
        metavar="AGENT",
        help="指定目标 Agent（可用别名: claude, gemini, opencode, codex）"
    )

    parser.add_argument(
        "--include-dev",
        action="store_true",
        help="包含开发技能（skill-scaffold, workflow-execute）"
    )

    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="强制覆盖已存在的技能"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="仅显示将执行的操作，不实际安装"
    )

    args = parser.parse_args()

    print("=" * 50)
    print("jm-forge Workspace Skills Installer (JMF Standard)")
    print("=" * 50)

    # Get available skills
    published, dev = get_skills(META_SKILL_SOURCE)

    if not published and not dev:
        print(f"\nError: 技能源目录 '{META_SKILL_SOURCE}' 为空或不存在")
        return 1

    print(f"\n发现技能:")
    print(f"  发布技能 ({len(published)}): {', '.join(sorted(s.name for s in published))}")
    if dev:
        print(f"  开发技能 ({len(dev)}): {', '.join(sorted(s.name for s in dev))}")

    # Determine target agents
    selected_agents: List[str] = []

    if args.agents:
        # Parse --agents argument
        for agent in args.agents:
            resolved = resolve_agent(agent)
            if resolved:
                selected_agents.append(resolved)
            else:
                print(f"Warning: 未知 Agent '{agent}'，跳过")
    elif args.all:
        # Install to all known agents
        selected_agents = list(TARGET_AGENTS.keys())
    else:
        # Interactive mode
        if not QUESTIONARY_AVAILABLE:
            print("\nError: 交互模式需要 questionary 库")
            print("请使用 --all 或 --agents 参数运行非交互模式")
            print("或安装依赖: uv sync")
            return 1

        selected_agents = select_agents_interactive()
        if not selected_agents:
            print("\n未选择任何 Agent，退出")
            return 0

    if not selected_agents:
        print("\n未指定任何 Agent，退出")
        return 1

    # Determine skills to install
    if args.include_dev or (not args.agents and not args.all):
        # In interactive mode, ask; otherwise use --include-dev flag
        if not args.include_dev and not args.agents and not args.all and QUESTIONARY_AVAILABLE:
            include_dev = select_skill_mode_interactive()
        else:
            include_dev = args.include_dev
    else:
        include_dev = False

    skills_to_install = published + (dev if include_dev else [])

    print(f"\n将操作 {len(skills_to_install)} 个技能到 {len(selected_agents)} 个 Agent")
    if args.dry_run:
        print("[DRY RUN - 仅显示不执行]")

    # Install to each selected agent
    all_results = {}
    for target in selected_agents:
        agent_name = TARGET_AGENTS.get(target, target)
        if args.dry_run:
            # Simulate result for dry run
            result = {"installed": [s.name for s in skills_to_install], "updated": [], "skipped": []}
        else:
            result = install_skills(Path(target), skills_to_install, force=args.force)
        all_results[target] = (agent_name, result)

    # Print results
    for target, (agent_name, result) in all_results.items():
        print_results(agent_name, target, result)

    print("\n" + "=" * 50)
    print("操作完成！" if not args.dry_run else "Dry Run 完成！")
    print("=" * 50)

    return 0


if __name__ == "__main__":
    exit(main())
