# Lisa Documentation Index

This folder contains the developer documentation for Lisa.

Lisa is a chat-native self-improving agentic assistant. It has no browser dashboard. User interaction happens only through Telegram, Slack, and WhatsApp.

---

## Recommended Reading Order

1. [Vision](00_vision.md)
2. [Chat-Native Architecture](01_chat_native_architecture.md)
3. [ReAct Planning Loop](02_react_planning_loop.md)
4. [Universal Plan Tokenizer](03_universal_plan_tokenizer.md)
5. [RAG Pipeline](04_rag_pipeline.md)
6. [Policy OS](05_policy_os.md)
7. [MQTT Protocol Layer](06_mqtt_protocol.md)
8. [Chat-Controlled DevShell](07_chat_controlled_devshell.md)
9. [Telegram Transparency Layer](08_telegram_transparency_layer.md)
10. [Security Model](09_security_model.md)
11. [Lightweight Deployment](10_lightweight_deployment.md)
12. [Developer Execution Plan](11_developer_execution_plan.md)
13. [Roadmap](12_roadmap.md)

---

## Core System Summary

```txt
Telegram / Slack / WhatsApp
        ↓
Unified Chat Gateway
        ↓
Intent Firewall
        ↓
Policy OS
        ↓
Planner → Universal Plan Tokenizer → Feasibility → Ranker
        ↓
Loop Governor
        ↓
Lisa Core Decision
        ↓
ApprovalMux / ToolMux / MemoryMux / ExecutionMux
        ↓
Chat-Controlled DevShell + Sandbox + MCP Test Bench
        ↓
ObservationMux + AuditLog
        ↓
Learner Brain + Nightly Harness
        ↓
Morning Report to Telegram
```

---

## Implementation Priority

Start with:

1. FastAPI foundation.
2. Telegram webhook.
3. Unified Chat Gateway.
4. Policy loader.
5. Telegram Notification Engine.
6. Planner/Feasibility/Ranker loop.
7. Universal Plan Tokenizer.
8. Basic tests.

Do not implement external writes or unrestricted tools in the first phase.
