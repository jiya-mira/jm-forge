# Plan — jm-forge-bootstrap

**Date:** 2026-03-23
**Source:** Discuss output (consumed)

---

## Steps

### Step 1: define-non-interactive-behavior

**Action:** Add explicit behavior definition for non-interactive environments (CI).

**Approach:**
- When `CI` environment variable detected OR `NONINTERACTIVE=1`, skip prompt and report status
- Add to SKILL.md under "Behavior" section

**Checkpoint:** `non-interactive-behavior-defined`
- CI env var or NONINTERACTIVE=1 triggers skip behavior
- Behavior documented in SKILL.md

---

### Step 2: clarify-permission-error-handling

**Action:** Specify error handling when brew install or script fails due to permissions.

**Approach:**
- Detect non-zero exit code from install command
- Report specific error message to user
- Exit with non-zero status to indicate failure
- Document in SKILL.md under "Error handling"

**Checkpoint:** `permission-error-handling-defined`
- Non-zero exit code triggers error report
- Exit status documented

---

### Step 3: specify-windows-verification

**Action:** Clarify Windows PATH update verification after install.

**Approach:**
- Note in SKILL.md that official installer auto-updates PATH on restart
- On Windows, if `uv --version` fails post-install, suggest restarting shell
- Add Windows-specific note

**Checkpoint:** `windows-verification-specified`
- Windows PATH note documented

---

### Step 4: define-cancel-message

**Action:** Specify exact user-facing message when user declines installation.

**Approach:**
- Add exact message to SKILL.md:
  > "uv is required for this operation. Please install it manually and retry."
- Consistent wording across platforms

**Checkpoint:** `cancel-message-specified`
- Exact message documented in SKILL.md

---

## Dependencies

Steps 1-4 are independent and can be executed in any order.

## Tracking

| Assumption | Risk |
|-----------|------|
| CI env detection is reliable | Low — `CI` is a common convention |
| Exit code capture works across platforms | Low — shell conventions apply |

## Execution Order

Steps 1-4 may run in parallel since they are independent.
