---
name: jmf-bootstrap
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

When this skill is invoked, the Agent should:

1. **Check for uv** — Run `uv --version` to verify uv is installed
2. **If uv is not installed:**
   - In non-interactive mode: exit with error
   - In interactive mode: ask user for confirmation, then install
3. **Run install script** to deploy skills to target directories:
   ```bash
   uv run scripts/install-workspaces-skills.py --all
   ```
   This installs all `jmf-*` skills to their respective target directories (`.claude/skills/`, `.gemini/skills/`, `.agents/skills/`).
4. **Update target project's AGENTS.md** — Append the following section:

```markdown
## jm-forge Workflow

This project uses a **Discuss → Plan → Execute** workflow. See `.planning/workflow-framework.md` for details.

### Task Lifecycle
| State | Description |
|-------|-------------|
| New | User proposed the idea |
| Discussing | In Discuss phase |
| Planning | In Plan phase |
| Pending | Plan complete, waiting to execute |
| Active | In Execute phase |
| Completed | Execute finished successfully |
| Failed | Execute failed |
| Abandoned | Explicitly abandoned by user |

### Workflow Skills
| Skill | Purpose |
|-------|---------|
| jmf-new | Create new task |
| jmf-discuss | Discuss phase |
| jmf-plan | Plan phase |
| jmf-execute | Execute phase |
| jmf-abandon | Abandon task |
| jmf-list | List tasks |
| jmf-status | Task details |

### Iteration Norms
- **Append-only**: Documents only append, never overwrite
- **Soft Boundaries**: Phases are guidelines, not hard walls. No forced backtracking.

### Trigger Rule
When user describes a goal with clear start, end, and verifiable completion — offer or use the workflow.
```

## Notes

`uv` is installed globally (via Homebrew or official installer). After installation, other skills use `uv run` or `uvx` to execute scripts without additional setup.
