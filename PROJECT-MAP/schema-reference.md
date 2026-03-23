# PROJECT-MAP Schema Reference

> Defines the structure for project context maps. Applicable to any work domain.

---

## Node Types

| Type | Description |
|------|-------------|
| `Domain` | Top-level area/module/sub-project in a project collection |
| `EntryPoint` | File that serves as an entry to understanding or running the project |
| `Asset` | Configuration, resource, data, or static file |
| `Abstraction` | Core concept, interface, or design element |
| `Artifact` | Output/result of work (compiled binary, document, etc.) |
| `resource` | Entity managed by the project (person, equipment, organization, financial, etc.) |
| `Unknown` | Node whose type could not be determined |

---

## Relationship Types

| Type | Description |
|------|-------------|
| `depends-on` | A depends on B (build/runtime dependency) |
| `implements` | A implements B (concrete realizes abstract) |
| `contains` | A contains B (logical grouping or inclusion) |
| `references` | A references B (documentation, import, link) |
| `builds-on` | A builds on B (uses B as foundation) |
| `delivers` | A delivers B (output artifact) |
| `unknown-type` | Relationship type could not be determined |

---

## Node Schema

```json
{
  "id": "string (unique within project)",
  "name": "string (human-readable name)",
  "type": "Domain | EntryPoint | Asset | Abstraction | Artifact | resource | Unknown",
  "path": "string (relative path, optional for Domain)",
  "description": "string | null",
  "tags": ["string"],
  "relationships": ["string (node id references)"]
}
```

### Resource Nodes

When `type: "resource"`, additional fields apply:

```json
{
  "id": "string",
  "name": "string",
  "type": "resource",
  "description": "string | null",
  "category": "infrastructure | document | organization | human | financial | equipment | api | repository | secret | other",
  "controllable": "boolean",
  "safety": {
    "level": "none | low | medium | high-caution | restricted",
    "requiresConfirmation": "boolean",
    "destructiveActionsAllowed": "boolean"
  },
  "attributes": "object (free-form key-value pairs)",
  "relationships": ["string (node id references)"],
  "notes": "string | null"
}
```

Resources are stored in `RESOURCE-MAP/resources.json` and referenced in PROJECT-MAP via `resource` nodes.

---

## Relationship Schema

```json
{
  "from": "string (node id)",
  "to": "string (node id)",
  "type": "depends-on | implements | contains | references | builds-on | delivers | unknown-type",
  "confidence": "high | medium | low",
  "note": "string | null"
}
```
