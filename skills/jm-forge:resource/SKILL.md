---
name: jm-forge:resource
description: Manage project resources (entities, assets, equipment, organizations). Use to add, list, or remove resources managed by the project.
---

# Skill: jm-forge-resource

## Purpose

Manage project resources — entities, assets, equipment, organizations, or any valuable resources the project works with, regardless of whether they exist inside or outside the project directory.

Resources are stored in `RESOURCE-MAP/resources.json`.

## Usage

```
$jm-forge-resource <command> [options]
```

Commands:
- `add` — Add a new resource
- `list` — List all registered resources
- `remove <id>` — Remove a resource by ID
- `get <id>` — Show details of a specific resource
- `scan` — Scan project for potential resources

---

## Commands

### add

Interactive flow to add a new resource.

**Prompts:**
1. `id` — Unique identifier (kebab-case, e.g., `prod-server-1`)
2. `name` — Human-readable name
3. `category` — Choose from: infrastructure, document, organization, human, financial, equipment, api, repository, secret, other
4. `description` — Brief description
5. `controllable` — Is this resource controllable by agent? (yes/no)
6. `safety.level` — Choose: none, low, medium, high-caution, restricted
7. `attributes` — Key-value pairs specific to this resource type (press Enter twice to finish)
8. `relationships` — Other resources this connects to (press Enter twice to finish)
9. `notes` — Additional notes

**Behavior:**
- Reads current `RESOURCE-MAP/resources.json`
- Appends new resource
- Writes back to file
- Confirms with user

---

### list

Lists all registered resources in a table format.

**Output:**
| ID | Name | Category | Controllable | Safety |
|----|------|----------|--------------|--------|
| ... | ... | ... | ... | ... |

---

### remove <id>

Removes a resource by its ID.

**Prompts:**
- Confirm before deletion
- Shows resource name before removal

**Error:**
- If resource ID not found, reports error

---

### get <id>

Shows full details of a specific resource in JSON format.

---

### scan

Scan the project directory to discover potential resources that may already be documented elsewhere.

**Workflow:**
1. Agent scans the entire project directory
2. Agent identifies potential resources using own judgment (no fixed file list)
3. Agent presents found candidates to user with evidence (which file/pattern suggested each)
4. User confirms which resources to register
5. Confirmed resources are appended to `RESOURCE-MAP/resources.json`

**Important:**
- Scan is **non-destructive**: it only suggests, never auto-registers
- User confirmation is **required** before any resource is added
- Agent uses project context to decide what to scan (docker-compose.yml, contacts.md, README, etc.)

**Example scan output:**
```
Found 3 potential resources:

1. [infrastructure] Docker services
   Evidence: docker-compose.yml defines "redis", "nginx" services
   Add? (yes/no): y

2. [human] Contact: 李四 (技术负责人)
   Evidence: README.md mentions "联系 人: 李四"
   Add? (yes/no): n

3. [equipment] 翻斗车 #01
   Evidence: notes.txt mentions "工地有翻斗车01在用"
   Add? (yes/no): y
```

---

## File Location

`RESOURCE-MAP/resources.json`

## Installation Notes

- RESOURCE-MAP/resources.json is **project data**, not framework code
- Do NOT copy RESOURCE-MAP/ when installing skills to another project
- The skill will auto-create RESOURCE-MAP/resources.json when first used

## Notes

- Resources are the source of truth — not cached
- Safety attributes control agent behavior when operating on resources
- Use `list` to get IDs before `remove` or `get`
