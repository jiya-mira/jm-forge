# Discuss Log — skill-naming-overhaul
# Task ID: 7

> Append-only iteration log. See `discuss.md` for latest consensus.

---

## Iteration 1 — 2026-03-23

**Trigger:** User proposed redesigning skill naming from `jm-forge-task-*` to something shorter and more ergonomic

**Topic:** Skill naming ergonomics for cross-agent workflows

**Agent recommendation:** TBD

**User decision:** TBD

**Conclusion:**
- Goal: redesign skill naming convention for usability
- User wants to avoid bike-shedding and iterate empirically
- Brand: `jm` (品牌缩写), Project: `forge`
- Separator: `:` (namespace-like)
- Final form: `jm-forge:<action>`
- Risk noted: Claude Code skill `name` field only allows lowercase/hyphens — `:` may cause issues in Claude Code specifically. User will test with Gemini/Codex separately.
- Ready for Plan
