# discuss.md: external-resources-support

**Source:** discuss-log.md

---

## Decision 1: External Resource Discovery Mode

**Q: 外部资源应该由用户显式声明，还是 agent 自动发现？**

**结论：显式注册为主，自动发现为辅**

### 理由

- 自动发现局限性大：大多数外部资源（服务器配置、API docs、内部笔记）没有任何元信息
- 实际场景中，agent 无法凭空知道项目外部有什么资源
- 有效的自动发现只能覆盖"有明显线索"的情况（如 `.git` 仓库、已有的 `README.md`）

### 设计决策

1. **默认机制：显式注册**
   - 用户在 `.external/external-resources.json` 中声明外部资源
   - init/sync 读取并整合这些资源

2. **辅助机制：主动询问**
   - init 运行时，agent 应主动询问用户："是否有外部资源需要注册？"
   - 收集到信息后，追加到 external-resources.json

3. **自动发现（尽力而为）**
   - 仅作为补充，不作为主要依赖
   - 例如：检测到 `.git` 目录则建议用户是否要注册远程仓库地址

---

## Decision 2: Skill Architecture

**Q: 需要单独 skill 还是融入现有？**

**结论：独立 skill + init/sync 集成询问**

### 组件设计

| 组件 | 职责 |
|------|------|
| `jm-forge-external` | 独立 skill：add/list/remove 外部资源 |
| `.external/` | 外部资源的地图目录 |
| init/sync | 读取资源地图，顺带询问是否要添加 |

### 理由

- 独立 skill → 用户可以主动触发
- init/sync 集成 → 被动/顺手的时候也能用
- 避免 init/sync 臃肿，但保持顺手可用

---

## Decision 3: RESOURCE-MAP Location

**Q: RESOURCE-MAP 放在哪里？**

**结论：`.external/`**

- 不与 agent 私有规范捆绑（不放在 `.claude/`）
- 显式、独立、与项目根目录并列
- 符合 jm-forge 设计哲学

---

## Decision 4: PROJECT-MAP Integration

**Q: 外部资源信息如何整合到 PROJECT-MAP？**

**结论：独立节点 + 简化 schema**

external-resource 作为独立节点类型，与项目内节点区分。

---

## Decision 5: Resource Schema — 泛化设计

**结论：最简核心 + 完全自由扩展（attributes）**

### 核心字段（所有资源都有）

| 字段 | 说明 |
|------|------|
| `id` | 唯一标识 |
| `name` | 名称 |
| `category` | 大类（提示用，不限制） |
| `description` | 描述 |
| `controllable` | 是否可由 agent 修改 |
| `safety` | 安全等级和操作限制 |
| `relationships` | 与其他资源的关系 |
| `attributes` | 完全自由的 key-value，描述资源特有属性 |
| `notes` | 自由备注 |

### category 初始集（可扩展）

| category | 适用场景 |
|----------|----------|
| `infrastructure` | 服务器、云服务 |
| `document` | 文档、资料 |
| `organization` | 公司、合作伙伴 |
| `human` | 个人联系人 |
| `financial` | 资金、投资、资产 |
| `equipment` | 设备、机械、翻斗车等 |
| `api` | API 服务 |
| `repository` | 代码仓库 |
| `secret` | 凭证密钥 |

### 泛化能力

- 金融项目：资金、股权作为资源
- 土方项目：翻斗车、施工设备作为资源
- 运维项目：服务器、服务作为资源
- 任何其他项目：人、财、物、信息都可以纳入

### 示例：翻斗车

```json
{
  "id": "dumper-truck-01",
  "name": "翻斗车 #01",
  "category": "equipment",
  "description": "主要负责A区土方运输",
  "controllable": true,
  "safety": { "level": "medium" },
  "attributes": {
    "type": "翻斗车",
    "capacity": "20立方",
    "status": "运行中",
    "location": "A区施工现场",
    "driver": "王五"
  }
}
```

---

## Summary

### 设计核心

1. **发现机制**：显式注册为主 + 主动询问
2. **架构**：独立 skill（jm-forge-external）+ init/sync 集成
3. **存储**：`.external/external-resources.json`
4. **整合**：PROJECT-MAP 中 external-resource 独立节点
5. **Schema**：泛化设计，核心字段 + 完全自由的 attributes

### 待实现 Acceptance Criteria

1. `jm-forge-external` skill 可 add/list/remove 外部资源
2. init/sync 可读取资源地图并询问用户
3. 资源地图支持泛化类型（人、财、物、信息）
4. 安全属性控制操作权限
