# discuss.md: resource-map-redesign

**Source:** discuss-log.md

---

## Decision 1: Skill Name

**Q: Skill 名字改成什么？**

**结论：`jm-forge-resource`**

简短、通用，聚焦于"资源/实体"本身而非"外部"。

---

## Decision 2: File Name

**Q: 文件名保持 `external-resources.json` 还是改成 `resources.json`？**

**结论：`resources.json`**

更简洁，去掉冗余的"external"限定词。

---

## Decision 3: RESOURCE-MAP and PROJECT-MAP Relationship

**Q: RESOURCE-MAP 和 PROJECT-MAP 的关系？**

**结论：并列**

| 地图 | 描述 |
|------|------|
| PROJECT-MAP | 代码结构（技术视图）：子项目、入口点、依赖关系 |
| RESOURCE-MAP | 业务实体（业务视图）：人、财、物、信息 |

两者平级，Agent 读两个地图获取完整上下文。

---

## Summary

| # | 决策 |
|---|------|
| 1 | Skill 名字：`jm-forge-resource` |
| 2 | 文件名：`resources.json` |
| 3 | 关系：RESOURCE-MAP 与 PROJECT-MAP 并列 |
