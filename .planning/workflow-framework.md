# Workflow Framework — Phase Summary

> Last updated: 2026-03-22
> Status: Draft — pending implementation

---

## 1. Theoretical Foundation

**Task Unit Definition**

A task is the atomic unit of workflow. It must satisfy four boundary conditions:

1. **Explicit起点** — A clear trigger/entry point exists
2. **Explicit终点** — A clear completion/closure point exists
3. **Independently verifiable** — An external observer can determine completion
4. **Recursively decomposable** — A task can be decomposed; decomposition stops when a subtask satisfies condition 2 (independently verifiable endpoint)

> Key insight: "Non-decomposable" is a **result of decomposition**, not a premise. Decomposition continues until a subtask's endpoint is independently verifiable.

---

## 2. Discuss Phase

### Purpose
Clarify and converge the task definition before planning begins.

### Termination Condition
All open issues are classified as **non-blocking**.

- **Blocking issue** — Prevents entry to Plan; must be resolved or delegated to a new task
- **Non-blocking issue** — Exists but does not impede planning

Enter Plan **iff** `∀ open_issue: open_issue.blocking == false`

### Decision Authority
- **Agent leads**: Identifies issues, classifies blocking/non-blocking, generates options
- **User assists**: Agent uses structured prompts (binary choices / impact analysis / options) to reduce cognitive load
- User judgment is guided, not open-ended

### Output (converges into Plan)
1. **Goal** — What we are trying to achieve
2. **Boundary** — In-scope vs out-of-scope
3. **Assumptions** — Premises taken as given
4. **Acceptance criteria** — How to determine "done"
5. **Open issues** — Non-blocking issues carried forward

---

## 3. Plan Phase

### Input
Discuss output (consumed; Discuss artifacts do not independently survive into Execute)

### Output
1. **Step decomposition** — Ordered sequence of actions
2. **Dependencies** — Ordering constraints between steps
3. **Checkpoints** — Per-step verification criteria
4. **Tracking** — Assumptions and risks

### New Blocking Issues During Planning
If Plan encounters a previously unknown blocking issue:

1. **Attempt self-resolution** — If resolvable with objectively verifiable new knowledge, resolve and continue
2. **If unresolvable** — Spawn a new task; mark current task as `Dependon <new task>`
3. **If extremely hard-blocking** — May abort current task; same `Dependon` protocol applies

### Relationship: Dependon
- Task A `Dependon` Task B → A cannot execute until B completes
- Transitive in chained scenarios (A Dependon B, B Dependon C → A effectively Dependon C), but primarily relevant in chained human-operated task flows

> Other relationship types (parallel, parent/child, etc.) are descriptive observations that emerge from execution, not first-class framework constructs. Start with `Dependon` only.

### Task Numbering

Each task is assigned a natural number identifier: `1`, `2`, `3`, ...

- Format: plain integer starting from 1
- Assignment: First task is `1`; subsequent tasks get the next available number
- Location: Recorded in `discuss.md` header or frontmatter as `id: <number>`
- Reference: Use the number in Dependon relationships (e.g., `Dependon 3`)

Task numbers enable:
- Precise task references across contexts
- Easier switching between tasks
- Automation-friendly task identification
- Scope for future tooling (e.g., task lists, status tracking)

### Format
Any format acceptable to the next phase (Execute). Plan output is the **sole input** to Execute.

---

## 4. Execute Phase

### Entry Criteria
Plan output is complete (all steps, dependencies, checkpoints, and tracking defined).

### Execution Model
Execute steps **sequentially** by default, following the dependency order defined in Plan. Each step may contain:
- **Action** — The work to be performed
- **Checkpoint** — Verification criteria for the step outcome

### Checkpoint Verification
After each step:
1. Agent evaluates whether the checkpoint criteria are met
2. Agent reports status: ✅ Verified or ❌ Failed
3. Evidence is documented (required on failure, optional on success)

### Failure Handling Protocol
On checkpoint failure:

1. **Attempt self-resolution** — Adjust subsequent steps, retry if possible
2. **If unresolvable** — Spawn a new task for the blocking issue; mark current task as `Dependon <new task>` and abort current execution
3. **Resume** — Once the blocking task completes, resume from the failed step

### Checkpoint Report Format
```
[Checkpoint N: <name>]
Status: ✅ Verified / ❌ Failed
Evidence: <what was observed>
```

### Termination
Execute terminates in one of three states:

| State | Meaning | Action |
|-------|---------|--------|
| **Completed** | All steps + all checkpoints verified | Normal end; task done |
| **Failed** | A checkpoint failed; cannot continue | Follow failure protocol |
| **Pending** | Task not finished; non-completion is due to user interruption (pause/abandon) | Task remains open; can be resumed later |

**Pending** replaces the previously discussed "Suspended" — it means "waiting to continue," not "abandoned."

### Task Resume
To resume a Pending task:
1. Read `.planning/<task>/execute.md` to identify the last verified checkpoint
2. Continue from the next step

### Output
1. **Checkpoint log** — Structured record of each checkpoint result
2. **Acceptance report** — Summary of whether the task met its acceptance criteria defined in Discuss

---

## 5. Open Questions

- [x] Execute phase structure — Resolved: Entry/Execution/Checkpoint/Failure/Termination/Output defined
- [ ] Task naming conventions
- [ ] How blocking/non-blocking classification accuracy is validated
- [ ] What constitutes "objectively verifiable new knowledge" in Plan self-resolution

---

## 6. Background: Why This Framework Exists

This framework is being built to enable a **skill development framework** where:
- Skills are reusable, project-level components
- The framework itself is general-purpose (not tied to jiya·mira specifically)
- Development follows the workflow defined herein
- Theoretical basis is explicit (see `.planning/workflow-framework/references.md`)

> **Note on theoretical basis:** The framework synthesizes established concepts (WBS, PDCA, GQM, V&V) with first-principles reasoning. Formal citations are documented in references.md.

---

## 7. Key Theoretical Influences

| Concept | Source | Role in Framework |
|---------|--------|-------------------|
| Recursive decomposition | WBS (PMI), HTN planning | Task unit boundary condition #4 |
| Explicit entry/exit criteria | PMBOK work packages | Task unit boundary conditions #1, #2 |
| Verification criteria | IEEE 1012 V&V | Checkpoint design |
| Goal-before-plan | GQM (Basili) | Discuss → Plan direction |
| Iterative verification | PDCA (Deming), Agile | Execute phase structure |
| Blocking issue → Dependon | Theory of Constraints | Plan/Execute failure handling |

## Next Steps

1. ~~Define Execute phase structure~~ ✅ Done
2. ~~Document the theoretical references~~ ✅ Done — see `.planning/workflow-framework/references.md`
3. ~~Test the Discuss → Plan flow with a real task~~ ✅ Done — jm-forge-bootstrap validated
4. ~~Finalize documentation structure~~ ✅ Done — templates in `.planning/templates/`
