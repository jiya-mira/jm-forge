# Workflow Framework — Theoretical References

> Last updated: 2026-03-22

---

## 1. Direct Influences

Concepts explicitly drawn from established theory:

### 1.1 Task Unit (4 Boundary Conditions)

**Work Breakdown Structure (WBS)**
- Origin: Project Management Institute (PMI), *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*
- Concept: Decompose work into manageable sections until work packages are independently verifiable
- Connection: Our "independently verifiable endpoint" mirrors WBS work package criterion

**Hierarchical Task Network (HTN) Planning**
- Origin: Artificial Intelligence planning literature (e.g., Erol, Hendler, and Nau)
- Concept: Tasks recursively decomposed into subtasks until primitive actions
- Connection: "Recursively decomposable" directly parallels HTN decomposition semantics

### 1.2 Discuss → Plan → Execute Flow

**PDCA Cycle (Plan-Do-Check-Act)**
- Origin: W. Edwards Deming (attributed); popularized in *Out of the Crisis* (1982)
- Concept: Iterative management method with explicit planning, execution, and verification phases
- Connection: Our D→P→E is a restructured PDCA with explicit Discuss (goal alignment) before Plan

**Inspect and Adapt**
- Origin: Agile/Scrum methodology; Extreme Programming (Beck, 1999)
- Concept: Continuous verification during execution, adaptation based on feedback
- Connection: Checkpoint verification and failure handling protocol

### 1.3 Checkpoint Verification

**Verification vs Validation (V&V)**
- Origin: IEEE Standard 1012 for Software Verification and Validation
- Concept: Verification = "Are we building the product right?" (meets specifications); checkpoint criteria align with verification activities
- Connection: Our checkpoints serve as verification criteria before proceeding

### 1.4 Goal Definition

**Goal-Question-Metric (GQM)**
- Origin: Victor Basili, *Goal Question Metric Paradigm* (1992)
- Concept: Define goals, derive questions, select metrics — we follow this in Discuss (Goal/Boundary/Assumptions → Acceptance Criteria)
- Connection: Discuss phase explicitly targets goal clarity analogous to GQM's goal definition

---

## 2. Related Frameworks (Inspirational, Not Direct引用)

These frameworks informed the design without direct conceptual borrowing:

| Framework | Relevance |
|-----------|-----------|
| **Rational Unified Process (RUP)** | Phased approach with explicit milestones and phase gates |
| **Cleanroom Software Engineering** | Formal verification combined with incremental development |
| **Theory of Constraints (TOC)** | Identifying and resolving blocking issues — relevant to our Dependon relationship |

---

## 3. Key Concepts — Defined

### "Objectively Verifiable New Knowledge" ✅ Resolved

**Definition:** Information that can be confirmed by an external observer through direct evidence, without relying on subjective judgment or private information.

**Criteria for "objectively verifiable":**

| Type | Verifiable? | Reason |
|------|-------------|--------|
| Documented fact (URL, book, spec) | ✅ Yes | External artifact with persistent reference |
| Command output / build result | ✅ Yes | Reproducible by anyone with same inputs |
| File existence / content | ✅ Yes | Observable state |
| Expert opinion / judgment call | ❌ No | Private, subjective |
| Unverifiable claim ("always works") | ❌ No | No testable evidence |
| Historical preference ("we always did X") | ❌ No | Not independently confirmable |

**Application in Plan phase:** When self-resolving a blocking issue, Agent must cite new knowledge that is objectively verifiable. Subjective intuition alone does not qualify.

**Note:** This definition is operational (designed for workflow utility), not philosophically rigorous. It mirrors IEEE 1012's verification criteria.

---

### Remaining Open Items

| Concept | Status | Notes |
|---------|--------|-------|
| Blocking vs Non-blocking classification | Heuristic | Agent judgment primary; guided by structured prompts |
| Task naming conventions | ✅ Resolved | Defined in `.planning/skill-naming-convention.md` |

---

## 4. Acknowledged Absence

The framework claims "theoretical basis is explicit" but:

- Most concepts are **first-principles reasoning** or **practical synthesis** rather than direct citations
- The 4 boundary conditions for task unit are abductive reasoning from what makes tasks workable, not a referenced theory
- Structured prompting draws from general UX/human-computer interaction intuitions

This document serves to make the theoretical **influences** explicit, even where citations are not formal.

---

## 5. References

- Beck, K. (1999). *Extreme Programming Explained*. Addison-Wesley.
- Basili, V. (1992). "The Goal Question Metric Paradigm." In *Encyclopedia of Software Engineering*.
- Deming, W.E. (1982). *Out of the Crisis*. MIT Press.
- IEEE (2012). *IEEE Standard 1012-2012 for Verification and Validation*.
- PMI (2021). *A Guide to the Project Management Body of Knowledge (PMBOK Guide)* (7th ed.).
