---
name: jm-forge-bootstrap
description: Ensure uv is installed and usable. Prompts for confirmation before installing. Run before other skills.
---

# Skill: jm-forge-bootstrap

## Purpose

Ensure `uv` (astral.sh) is installed and accessible. This is a prerequisite for all other skills.

## Behavior

1. Run `uv --version`
2. If found: report version and exit success
3. If not found and non-interactive (see below): report that uv is not installed and exit with error
4. If not found and interactive: ask the user for confirmation before installing, then install and verify

### Non-interactive environments

In CI environments or when `NONINTERACTIVE=1` is set, skip the confirmation prompt and report status:

- If uv is not found: report "uv is not installed" and exit with non-zero status
- If uv is found: report version and exit normally

Exit code: `0` if uv is available, `1` otherwise.

## Interactive confirmation

Before installing, ask the user:

> `uv` is not installed. Install it now?
> - **Yes** — installs via Homebrew (macOS) or official script (Linux/Windows)
> - **No** — report "uv is required for this operation. Please install it manually and retry." and exit with non-zero status

Do NOT install without the user's explicit consent.

## Install method (if user confirms)

| Platform | Method | Command |
|----------|--------|---------|
| macOS with Homebrew | Homebrew (recommended) | `brew install uv` |
| Linux/macOS | Official script | `curl -LsSf https://astral.sh/uv/install.sh | sh` |
| Windows | Official script | `irm https://astral.sh/uv/install.ps1 | iex` |

After installation, verify with `uv --version`.

### Error handling

If install command fails (non-zero exit code):
1. Report the error message from the failed command
2. Exit with non-zero status
3. User must resolve the underlying issue (e.g., permissions) manually

### Windows-specific note

The official Windows installer may require a shell restart to update PATH. If `uv --version` fails immediately after installation, restart your terminal and try again.

## Bootstrap Process

When this skill is invoked in a target project, the Agent should:

1. **Check for uv** — Run `uv --version` to verify uv is installed
2. **If uv is not installed:**
   - In non-interactive mode: exit with error
   - In interactive mode: ask user for confirmation, then install
3. **Copy jm-forge-task-* skills** to `.claude/skills/`:
   - `jm-forge-task-new/`
   - `jm-forge-task-discuss/`
   - `jm-forge-task-plan/`
   - `jm-forge-task-execute/`
   - `jm-forge-task-auto/`
   - `jm-forge-task-abandon/`
   - `jm-forge-task-list/`
   - `jm-forge-task-status/`
4. **Update target project's AGENTS.md** — Append the following section:

```markdown
## jm-forge Workflow

This project uses a **Discuss → Plan → Execute** workflow. See `.planning/workflow-framework.md` for details.

### Task Unit Definition
A task is an atomic unit of work with:
1. Explicit start (clear trigger)
2. Explicit end (completion criteria)
3. Independently verifiable (external observer can confirm)
4. Recursively decomposable (break into ordered steps)

### Workflow Skills
| Skill | Purpose |
|-------|---------|
| jm-forge-task-new | Create new task |
| jm-forge-task-discuss | Discuss phase |
| jm-forge-task-plan | Plan phase |
| jm-forge-task-execute | Execute phase |
| jm-forge-task-auto | Auto-advance |
| jm-forge-task-abandon | Abandon task |
| jm-forge-task-list | List tasks |
| jm-forge-task-status | Task details |

### Trigger Rule
When user describes a goal with clear start, end, and verifiable completion — offer or use the workflow.
```

5. **Update target's manifest.json** if it exists in `skills/`

## Notes

`uv` is installed globally (via Homebrew or official installer). After installation, other skills use `uv run` or `uvx` to execute scripts without additional setup.
