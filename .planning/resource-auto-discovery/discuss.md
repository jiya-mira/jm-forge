# discuss.md: resource-auto-discovery

**Source:** discuss-log.md

---

## Decision 1: Discovery Mode

**Q: Discovery 应该做成独立命令还是集成到 init？**

**结论：C — 两者都要**

1. **独立命令：** `jm-forge-resource scan`
   - 用户可以主动触发
   - 非常态，但可用

2. **集成到 init：**
   - init 时 Agent 自动扫描整个 project
   - Agent 自行判断哪些文件值得扫描（不给固定列表）

---

## Decision 2: Confirmation Mode

**Q: 发现后的处理方式？**

**结论：必须询问用户确认**

- 发现后展示找到的资源候选
- 用户确认后才注册
- 避免误判、误注册

---

## Decision 3: Scan Scope

**Q: 具体扫描哪些文件？**

**结论：不提供固定列表，让 Agent 自行判断**

- Agent 根据项目类型和结构自行决定扫描范围
- 对于 init 集成形态，需要扫描整个 project
- Agent 智能识别：docker-compose.yml、contacts.md、README.md 等

---

## Summary

| # | 决策 |
|---|------|
| 1 | 独立命令 + 集成到 init |
| 2 | 必须询问用户确认 |
| 3 | Agent 自行判断扫描范围 |
