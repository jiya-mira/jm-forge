# discuss.md

**Source:** discuss-log.md

---

## Goal

配置Gemini CLI的Workspace Skills支持，使其与jm-forge现有的Claude Code技能系统完全兼容，共享同一套技能定义。

## Boundary

### In Scope
- 创建`.gemini/skills/`目录结构（Gemini CLI标准Workspace Skills位置）
- 实现技能发现机制：扫描`.gemini/skills/`目录
- 实现命令匹配触发：`/skill-name`直接激活对应技能
- 技能包结构：`SKILL.md` + 资源文件
- Workspace Skills优先级：Workspace > User > Extension

### Out of Scope
- 修改Gemini CLI本身
- 创建Gemini API集成
- User-level或Extension-level技能管理
- 特异化的安装差异（Claude和Gemini使用完全相同的技能）

## Assumptions

1. 技能遵循Gemini CLI的`SKILL.md` + 资源文件结构
2. `.gemini/skills/`中的技能与`.claude/skills/`保持完全一致
3. 通过命令匹配触发：`/skill-name`激活对应技能
4. Workspace Skills优先级最高
5. 未来通过安装脚本实现自动化配置

## Acceptance Criteria

1. `.gemini/skills/`目录结构遵循Gemini CLI标准
2. jm-forge可发现并列出可用Workspace Skills
3. 命令匹配触发激活：`/skill-name`直接激活
4. 技能内容与`.claude/skills/`完全一致（无差异）
5. 技能可提交版本控制

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | 目录命名：`.gemini/skills/`还是`.agents/skills/`？ | Non-blocking | `.gemini/skills/`（更符合Gemini CLI标准） |
| 2 | 激活触发方式 | Blocking | **Resolved**: 命令匹配 - `/skill-name` |
| 3 | 向后兼容性：现有`.claude/skills/`迁移？ | Non-blocking | 不迁移，保持独立，符号链接或复制同步 |

## Key Decisions

1. **Activation Trigger:** 命令匹配 (`/skill-name`)
2. **Skill Parity:** Gemini与Claude使用完全相同的技能定义，无特异化差异
3. **Directory:** `.gemini/skills/`（Gemini CLI原生位置）
