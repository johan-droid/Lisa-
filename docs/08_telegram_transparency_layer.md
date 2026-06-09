# Telegram Transparency Layer

Telegram is Lisa's primary live observability and validation channel.

The user explicitly prefers frequent, crystal-clear Telegram updates, even if noisy.

---

## 1. Transparency Law

Lisa must notify the user through Telegram for every meaningful internal update.

Lisa must clearly state:

- Which brain is active.
- What phase is running.
- What decision is being made.
- What file, tool, workspace, skill, MCP, memory, or policy is affected.
- What the risk level is.
- Whether validation is required.
- What happens next.

---

## 2. No Silent Action Rule

No environment or workspace update should happen silently.

If a module changes state without emitting a notification, Lisa must trigger a circuit breaker.

Circuit breaker event:

```txt
SILENT_ACTION_DETECTED
```

Response:

```txt
pause task
write audit log
notify Telegram
require validation before continuing
```

---

## 3. Active Brain States

```txt
PLANNER_ACTIVE
FEASIBILITY_ACTIVE
RANKER_ACTIVE
LEARNER_ACTIVE
RESEARCH_ACTIVE
CYBER_IMMUNE_ACTIVE
RED_TEAM_MIRROR_ACTIVE
POLICY_OS_ACTIVE
DEVSHELL_ACTIVE
MCP_SCANNER_ACTIVE
NIGHTLY_HARNESS_ACTIVE
```

Every brain switch must notify Telegram.

---

## 4. Notification Types

```txt
BRAIN_SWITCH
TASK_CREATED
TASK_PHASE_CHANGED
PLAN_CREATED
PLAN_COMPRESSED
FEASIBILITY_STARTED
FEASIBILITY_COMPLETED
RANKING_STARTED
RANKING_COMPLETED
RELOOP_TRIGGERED
THRESHOLD_PASSED
THRESHOLD_FAILED
TOKEN_BUDGET_WARNING
POLICY_DECISION
APPROVAL_REQUIRED
APPROVAL_RECEIVED
DEVSHELL_SESSION_STARTED
DEVSHELL_COMMAND_STARTED
DEVSHELL_COMMAND_BLOCKED
DEVSHELL_COMMAND_COMPLETED
FILE_CHANGED
DIFF_CREATED
TEST_STARTED
TEST_COMPLETED
MCP_SCAN_STARTED
MCP_SCAN_COMPLETED
SKILL_CANDIDATE_CREATED
MEMORY_WRITE_REQUESTED
MEMORY_PROMOTION_REQUESTED
CIRCUIT_BREAKER_TRIGGERED
ROLLBACK_CREATED
NIGHTLY_STARTED
NIGHTLY_COMPLETED
MORNING_REPORT_READY
ERROR
```

---

## 5. Crucial Update Validation

Crucial updates must pause and request validation.

Examples:

- P3 external write.
- P4 production write.
- P5 irreversible/sensitive action.
- Core file modification.
- Policy file modification.
- Skill activation.
- MCP activation.
- Connector permission grant.
- Network-enabled command.
- Package install with scripts enabled.
- Trusted memory promotion.
- Database schema change.

---

## 6. Validation Message Format

```txt
⚠️ Validation Required

Task: task_184
Active Brain: DevShell / Policy OS
Requested Action: Promote skill candidate auth_refactor_v1
Affected Area: skills/active/auth_refactor
Risk Level: P3
Reason: This changes Lisa's future behavior.
Rollback: Available
Tests: Passed 12/12
Diff: 4 files changed

Reply:
/lisa approve appr_184
/lisa deny appr_184
/lisa explain appr_184
/lisa diff appr_184
```

---

## 7. Notification Files

```txt
backend/app/notifications/telegram_notifier.py
backend/app/notifications/notification_policy.py
backend/app/notifications/notification_renderer.py
backend/app/notifications/notification_queue.py
backend/app/notifications/notification_types.py
backend/app/policies/notifications.yaml
```

---

## 8. Notification Policy

```yaml
telegram_notifications:
  enabled: true
  primary_channel: true
  verbosity: exhaustive
  batching:
    enabled: false
    reason: User requested granular updates even if noisy.
  sensitive_data:
    redact_secrets: true
    redact_env_values: true
    redact_tokens: true
    redact_private_keys: true
    redact_credentials: true
  crucial_validation:
    require_user_validation: true
    block_until_response: true
```

---

## 9. Required Tests

- Telegram notification sent on task creation.
- Telegram notification sent on brain switch.
- Telegram notification sent on plan creation.
- Telegram notification sent on feasibility completion.
- Telegram notification sent on ranker score.
- Telegram notification sent on DevShell command start/completion/block.
- Crucial update creates validation request.
- P3/P4/P5 blocks until validation.
- Secrets are redacted.
- Silent state change triggers circuit breaker.
