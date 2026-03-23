# discuss-log.md: resource-auto-discovery

**Source:** (initial creation)

---

## Iteration 1 — 2026-03-23

### Context

Task #10 and #11 completed the basic RESOURCE-MAP framework:
- `jm-forge-resource` skill for add/list/remove resources
- `RESOURCE-MAP/resources.json` for storing resource data
- Resources can be manually registered via `jm-forge:resource add`

### New Feature Request

User asked: "可以支持自动分析一些 project 已经通过其他方式记录的 resource 吗？"

Goal: Auto-discover existing resources from project files, similar to how `jm-forge-init` auto-discovers project structure.

### Potential Discovery Sources

| File | Resource Type | Examples |
|------|---------------|----------|
| `docker-compose.yml` | infrastructure | 服务、容器、端口 |
| `.env.example` | infrastructure | 服务器地址、API endpoints |
| `README.md` | document | 文档链接、外部服务 |
| `contacts.md`, `team.md` | human, organization | 联系人、合作伙伴 |
| `supervisord.conf` | infrastructure | 运行中的服务 |
| `package.json` dependencies | api, repository | 外部依赖 |
| `kubernetes/*.yaml` | infrastructure | K8s 服务、配置 |

### Next Steps

- Discuss: What files/patterns should be auto-scanned?
- Define discovery workflow
- Plan implementation

---

## Iteration 2 — 2026-03-23

### Decisions Made

1. **Q1 - Mode**: C — 独立命令 + 集成到 init
2. **Q2 - Confirmation**: 必须询问用户确认
3. **Q3 - Scan Scope**: 不给固定列表，让 Agent 自行判断
