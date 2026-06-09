# Policy OS

Policy OS is Lisa's authority layer.

Brains can think, but Policy OS decides what Lisa is allowed to do.

---

## 1. Core Principle

```txt
Brains reason.
Multiplexers route.
Policy OS decides authority.
Sandbox executes.
Audit logs record everything.
Telegram reports everything.
```

---

## 2. Permission Levels

```txt
P0 observe
P1 draft
P2 sandbox_write
P3 external_write
P4 production_write
P5 irreversible_or_sensitive
```

Defaults:

```txt
P0/P1: allowed
P2: sandbox only
P3: approval required
P4: approval + tests + rollback required
P5: deny by default
```

---

## 3. Constitution Laws

Lisa's constitution must include:

```yaml
transparency_law:
  - Lisa must notify the user through Telegram for every meaningful internal update.
  - Lisa must clearly state which brain is active during every task phase.
  - Lisa must request validation before crucial workspace, memory, skill, MCP, connector, policy, or execution changes.
  - Lisa must never silently change its environment.
  - Lisa must prefer excessive transparency over hidden automation.

execution_law:
  - Lisa must never execute unrestricted host commands.
  - Lisa must never activate MCPs directly.
  - Lisa must never write production systems without validation.
  - Lisa must never expose secrets.
  - Lisa must never bypass ToolMux, MemoryMux, ApprovalMux, or ExecutionMux.
```

---

## 4. Policy Files

```txt
backend/app/policies/constitution.yaml
backend/app/policies/permissions.yaml
backend/app/policies/planning_loop.yaml
backend/app/policies/context_budget.yaml
backend/app/policies/model_routing.yaml
backend/app/policies/rag_policy.yaml
backend/app/policies/memory.yaml
backend/app/policies/tools.yaml
backend/app/policies/mcp.yaml
backend/app/policies/skills.yaml
backend/app/policies/rollback.yaml
backend/app/policies/devshell.yaml
backend/app/policies/chat_interfaces.yaml
backend/app/policies/notifications.yaml
```

No policy threshold or permission rule should be hardcoded in business logic.

---

## 5. Enforcement Points

Policy OS must control:

- Chat commands.
- Brain loop transitions.
- DevShell commands.
- Tool calls.
- Memory writes.
- RAG retrieval.
- MCP scanning/testing/activation.
- Skill candidate promotion.
- Approval requests.
- Rollback decisions.

---

## 6. Effect-Based Risk Classification

Lisa must classify the effect of an action, not only the tool name.

Example:

```txt
shell.exec: pytest tests/         → P1/P2
shell.exec: rm -rf workspace      → P5
git write README.md               → P2/P3
git write .github/workflows/*     → P4
send external message             → P5
activate MCP                      → P4/P5
promote trusted memory            → P3
```

---

## 7. Required Files

```txt
backend/app/policy_os/policy_loader.py
backend/app/policy_os/constitution_engine.py
backend/app/policy_os/permission_engine.py
backend/app/policy_os/risk_engine.py
backend/app/policy_os/effect_classifier.py
backend/app/policy_os/approval_engine.py
backend/app/policy_os/rollback_engine.py
backend/app/policy_os/circuit_breaker.py
```

---

## 8. Tests

Required tests:

- Policy files load.
- P3 requires approval.
- P4 requires approval + tests + rollback.
- P5 is denied by default.
- Unsafe commands are blocked.
- Brain cannot bypass ToolMux.
- Memory cannot be promoted without policy check.
- Silent action triggers circuit breaker.
