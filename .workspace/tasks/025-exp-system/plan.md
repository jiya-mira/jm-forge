# Plan — exp-system

**Date:** 2026-03-26
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: Define exp contract

**Action:** Lock the `jmf-exp` data contract and output shape before implementation starts.

**Approach:**
- Define the minimum exp record fields: scene tags, task reference, attempt summary, root cause, resolution, lesson, provenance, and status
- Use a deterministic ID composed from normalized task reference, scene slug, and attempt ordinal
- Make the rule explicit that exp must be derived from at least one real attempt and cannot be sourced directly from external retrieval

**Checkpoint:** `exp-contract-defined`
- A record schema exists in the skill documentation
- The ID rule is deterministic and reproducible
- The attempt-to-exp boundary is written as a hard constraint

---

### Step 2: Design storage layout

**Action:** Decide where exp records live and how they are organized in the repository.

**Approach:**
- Keep the primary output as a Markdown draft
- Do not introduce a separate index file in v1
- Defer persistence layout beyond the draft unless the user explicitly requests a saved file

**Checkpoint:** `exp-storage-layout-defined`
- The storage location is documented
- The layout supports repeated writes without ambiguity
- The plan states what is in scope for v1 and what is deferred

---

### Step 3: Specify lifecycle rules

**Action:** Formalize how exp status changes as evidence accumulates.

**Approach:**
- Preserve the 3-state model: `New`, `Verified`, `Strong`
- Define downgrade behavior when mixed success/failure attempts appear: batch review plus user confirmation decides downgrade or regrade
- State that batch review, not immediate mutation, is the mechanism for reclassification

**Checkpoint:** `exp-lifecycle-defined`
- Status transitions are written as a table or rule set
- Downgrade and regrading rules are unambiguous
- The batch review boundary is explicit

---

### Step 4: Define integration flow

**Action:** Map how `jmf-exp` plugs into the existing workflow without increasing day-to-day friction.

**Approach:**
- Define the user-triggered entry point for generating exp from task artifacts
- Clarify how `jmf-discuss`, `jmf-plan`, and `jmf-execute` outputs are consumed
- Keep the first version as a Skill-only delivery that does not require automatic background execution
- State that external retrieval content cannot be turned into exp directly

**Checkpoint:** `workflow-integration-defined`
- The trigger path is documented
- The consumed inputs are named explicitly
- No new automatic workflow is introduced in v1

---

### Step 5: Validate with racobit sample

**Action:** Run the template against the racobit Task 3 discuss-log as the first proof sample.

**Approach:**
- Extract one concrete exp from the existing task history
- Check whether the template can express provenance, attempt summary, and lesson cleanly
- Use the sample to expose missing fields or unclear wording before finalizing the skill
- If the racobit sample is unavailable in the local workspace, use the current task's discuss-log as a proxy validation sample and record the limitation
- Treat this as the only required v1 validation sample

**Checkpoint:** `sample-validation-passed`
- At least one exp can be produced from the racobit sample
- The result is understandable without extra explanation
- Any missing fields are recorded as follow-up constraints, not hidden

---

### Step 6: Finalize skill packaging

**Action:** Put the contract and template into the `jmf-exp` skill files and align project metadata.

**Approach:**
- Update `skills/jmf-exp/SKILL.md` with the final contract and usage rules
- Add the new skill to `skills/manifest.json`
- Mirror the skill into `.claude/skills/jmf-exp/` for discovery if needed
- Keep the implementation minimal and avoid adding unrelated automation

**Checkpoint:** `skill-packaging-complete`
- The skill exists in the canonical skill location
- Discovery metadata is consistent
- The skill is ready for execution-phase implementation work

---

## Dependencies

Steps 1-4 define the implementation shape and should be completed before Step 5 and Step 6.
Step 5 depends on the contract and lifecycle rules being stable enough to evaluate the sample.
Step 6 depends on the earlier steps so the packaged skill reflects the agreed design.

## Tracking

| Assumption | Risk |
|-----------|------|
| Markdown draft output is sufficient for the first version of exp records | Low - matches current skill delivery style |
| A single racobit sample is enough for first-pass validation | Medium - may miss cross-task reuse issues |
| Manual trigger is acceptable for v1 | Low - aligns with current discuss decision |
| No auto-ingestion of external knowledge into exp | Low - matches the task boundary |

## Execution Order

Sequential with dependencies noted
