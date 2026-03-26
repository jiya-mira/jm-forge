# discuss-log.md: resource-map-redesign

**Source:** (initial creation)

---

## Iteration 1 — 2026-03-23

### Context

Task #10 (external-resources-support) was just completed with design:
- `.external/external-resources.json` for storing external resources
- `jm-forge-external` skill to manage them
- init/sync updated to read from it

### New Insight

User raised a question: "既然有外部资源，就有内部资源吧？"

Then gave a concrete example:
- A company daily management project
- Has: full-time employees, outsourced employees, financial agency
- These are neither "external" (project boundary) nor "internal" (code structure)
- They are the **business entities** the project manages

### Problem

Current "external-resources" naming is misleading:
1. It suggests "resources outside the project boundary"
2. But for many projects (company management, HR systems, etc.), the managed entities ARE the domain

### Proposed Redesign

Rename `.external/` → `RESOURCE-MAP/`

Broader scope: RESOURCE-MAP stores **all entities** the project manages, regardless of whether they exist inside or outside the project directory:

| category | 说明 | 示例 |
|----------|------|------|
| `infrastructure` | 支持性资源 | 服务器、云服务 |
| `equipment` | 设备 | 翻斗车、工程机械 |
| `organization` | 组织 | 外包公司、财务代理 |
| `human` | 个人 | 全职员工、外包员工 |
| `financial` | 财务实体 | 账户、资金 |

### Pending Decisions

1. Rename `.external/` → `RESOURCE-MAP/` (done)
2. Update skill name from `jm-forge-external` to `jm-forge-resource`?
3. Update schema to better reflect broader scope
4. Update all references from external-resources.json to resources.json?

### Next Steps

- Discuss: Is this the right direction?
- Define exact scope of RESOURCE-MAP
- Plan migration from current state

---

## Iteration 2 — 2026-03-23

### Decisions Made

1. **Q1 - Skill Name**: `jm-forge-resource`
2. **Q2 - File Name**: `resources.json`
3. **Q3 - Relationship**: RESOURCE-MAP 与 PROJECT-MAP 并列

### Key Rationale for Q3

PROJECT-MAP = 技术视图（代码结构）
RESOURCE-MAP = 业务视图（管理的实体）

并列关系最清晰，两者独立演进，互不包含。
