# Developer Execution Plan

This document is the implementation order for Lisa.

Follow it strictly. Do not jump to external execution before the planning core, Policy OS, and notification layer exist.

---

## 1. Build Order

```txt
1. Create FastAPI foundation.
2. Add config system.
3. Add chat gateway.
4. Add Telegram webhook first.
5. Add Slack and WhatsApp adapters.
6. Add task runtime and audit log.
7. Add policy files and policy loader.
8. Add Telegram notification engine.
9. Add Planner, Feasibility, and Ranker brains.
10. Add Universal Plan Tokenizer.
11. Add ReAct loop and threshold policy.
12. Add RAG skeleton and trust zones.
13. Add MQTT optional event layer.
14. Add multiplexer skeletons.
15. Add chat-controlled DevShell backend.
16. Add approval rendering.
17. Add tests.
18. Add docs and lessons.
19. Run test suite.
20. Fix failures.
```

---

## 2. First Implementation Target

The first working flow should be:

```txt
Telegram message: /lisa plan Build the planning core
→ Telegram webhook
→ Unified Chat Gateway
→ Intent Firewall
→ Task Runtime
→ Planner Brain
→ Universal Plan Tokenizer
→ Feasibility Brain
→ Ranker Brain
→ Final score
→ Telegram response
```

---

## 3. Required Backend Folders

```txt
backend/app/chat
backend/app/core
backend/app/policy_os
backend/app/brains
backend/app/loop
backend/app/tokenizer
backend/app/rag
backend/app/mux
backend/app/messaging
backend/app/memory
backend/app/devshell
backend/app/skills
backend/app/mcp
backend/app/llm
backend/app/nightly
backend/app/routes
backend/app/schemas
backend/app/policies
backend/app/notifications
```

---

## 4. Minimum API Routes

Public:

```txt
GET  /api/health
POST /webhooks/telegram
POST /webhooks/slack/events
GET  /webhooks/whatsapp
POST /webhooks/whatsapp
```

Internal:

```txt
POST /internal/tasks
GET  /internal/tasks/{task_id}
POST /internal/tasks/{task_id}/plan
GET  /internal/tasks/{task_id}/events
POST /internal/nightly/run
```

---

## 5. Required Policy Files

```txt
constitution.yaml
permissions.yaml
planning_loop.yaml
context_budget.yaml
model_routing.yaml
rag_policy.yaml
memory.yaml
tools.yaml
mcp.yaml
skills.yaml
rollback.yaml
devshell.yaml
chat_interfaces.yaml
notifications.yaml
```

---

## 6. First Test Set

Implement tests for:

- health route
- Telegram webhook normalization
- task creation
- policy file loading
- plan packet generation
- Ranker scoring
- low-score reloop
- max-iteration stop
- Telegram notification on brain switch
- P3 action requires approval
- DevShell forbidden command blocked
- secrets redacted

---

## 7. Developer Output Required

After implementation, the developer agent must report:

```txt
Files created/modified
Architecture summary
How Telegram/Slack/WhatsApp flow works
How planning loop works
How Telegram transparency works
How DevShell works through chat
Tests run
Test results
How to run locally
Environment variables required
Remaining limitations
Next milestone
```

---

## 8. Do Not Build Yet

Do not implement yet:

- Gmail sending.
- GitHub write.
- Canva connector.
- Jules connector.
- Real MCP activation.
- Production deploy actions.
- Browser dashboard.
- Browser editor.
- Browser terminal.

These come after the governance core is tested.
