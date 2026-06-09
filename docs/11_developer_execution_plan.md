# Developer Execution Plan

This document is the implementation order for Lisa.

Follow it strictly. Do not jump to external execution before the planning core, Policy OS, and notification layer exist.

---

## 1. Build Order

```txt
Layer 0 — Repo Understanding + Guardrails
Layer 1 — Backend Foundation
Layer 2 — Chat-Native Interface Layer
Layer 3 — Telegram Transparency Layer
Layer 4 — Policy OS + Constitution
Layer 5 — Task Runtime + Audit System
Layer 6 — Three-Brain ReAct Planning Loop
Layer 7 — Universal Plan Tokenizer
Layer 7.5 — Teacher / Learner Brain + Night School
Layer 7.75 — Auditor / School Inspector Brain
Layer 8 — RAG + Memory Trust Zones
Layer 8.5 — Cyber-Immune / World-Interaction Brain
Layer 9 — MQTT Event Bus
Layer 10 — Chat-Controlled DevShell
Layer 11 — MCP Quarantine + Skill Graph Skeleton
Layer 12 — Nightly Harness
Layer 13 — Tests + Safety Verification
Layer 14 — Developer Docs + Lessons
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
