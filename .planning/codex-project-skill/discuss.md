# discuss.md

**Source:** discuss-log.md

---

## Goal

配置GitHub Codex CLI的Workspace Skills支持，使其与jm-forge现有的Claude Code技能系统完全兼容，共享同一套技能定义。

## Boundary

### In Scope
- 创建`.agents/skills/`目录结构（Codex CLI标准Workspace Skills位置）
- 实现技能发现机制：扫描`.agents/skills/`目录
- 实现显式触发激活：`$skill-name`直接激活对应技能
- 技能包结构：`SKILL.md` + 资源文件
- Workspace Skills优先级：REPO > USER > ADMIN > SYSTEM

### Out of Scope
- 修改Codex CLI本身
- 创建Codex API集成
- User-level或Admin-level技能管理
- 隐式激活（description自动匹配）
- 特异化的安装差异（Claude和Codex使用完全相同的技能）

## Assumptions

1. 技能遵循Codex CLI的`SKILL.md` + 资源文件结构
2. `.agents/skills/`中的技能与`.claude/skills/`保持完全一致
3. 通过显式触发：`$skill-name`激活对应技能
4. Workspace Skills优先级最高（REPO级别）
5. 未来通过安装脚本实现自动化配置

## Acceptance Criteria

1. `.agents/skills/`目录结构遵循Codex CLI标准
2. jm-forge可发现并列出可用Workspace Skills
3. 显式触发激活：`$skill-name`直接激活
4. 技能内容与`.claude/skills/`完全一致（无差异）
5. 技能可提交版本控制

## Open Issues

| # | Issue | Blocking? | Resolution |
|---|-------|------------|------------|
| 1 | 目录命名：`.agents/skills/`还是`.codex/skills/`？ | Non-blocking | `.agents/skills/`（Codex CLI官方标准位置） |
| 2 | 激活触发方式 | Non-blocking | **Resolved**: 显式触发 - `$skill-name` |
| 3 | 向后兼容性：现有`.claude/skills/`迁移？ | Non-blocking | 不迁移，保持独立，符号链接或复制同步 |

## Key Decisions

1. **Directory:** `.agents/skills/`（Codex CLI官方标准）
2. **Activation Trigger:** 显式触发 `$skill-name`
3. **Skill Parity:** Codex与Claude使用完全相同的技能定义，无特异化差异
