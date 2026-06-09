# Lisa

**Lisa** is a chat-native, self-improving agentic assistant designed to operate through **Telegram, Slack, and WhatsApp only**.

Lisa is not a normal web dashboard. Lisa is an agentic operating core with controlled planning, strict governance, sandboxed development, RAG-backed memory, MCP quarantine, and mandatory Telegram transparency for every meaningful environment update.

> **Core principle:** Brains reason. Multiplexers route. Policy decides authority. Sandbox executes. Telegram reports everything.

---

## What Lisa Is

Lisa is designed as a long-term personal agentic assistant with:

- A controlled three-brain ReAct planning loop (part of a 7-brain governance system).
- A Universal Plan Tokenizer to reduce token pressure between brains.
- A strict Policy OS and constitution.
- A chat-controlled DevShell for sandboxed self-improvement.
- RAG pipelines with trust zones.
- MCP discovery and quarantine before activation.
- MQTT-based lightweight eventing.
- Mandatory Telegram notifications for every meaningful update.
- Human validation for crucial workspace, memory, MCP, skill, connector, and execution changes.

Lisa should grow in capability, but never through unrestricted autonomy.

---

## User-Facing Interfaces

Lisa has only three user-facing channels:

```txt
Telegram  - primary control, validation, and live update channel
Slack     - secondary team/workspace channel
WhatsApp  - secondary mobile command channel
```

There is **no traditional web dashboard**.

All interaction must happen through chat commands, approval replies, diff summaries, test summaries, and safe artifact references.

---

## Current Build Phase

This repository starts with the **planning and documentation phase**.

The first implementation target is:

```txt
Chat command
→ Unified Chat Gateway
→ Intent Firewall
→ Planner Brain
→ Universal Plan Tokenizer
→ Feasibility Brain
→ Ranker Brain
→ Threshold check
→ Re-loop if needed
→ Final plan packet
→ Telegram update
```

No real-world destructive execution is allowed in the initial phase.

---

## Core Architecture

```mermaid
flowchart TD
    TG[Telegram Primary Control Channel] --> CG[Unified Chat Gateway]
    SL[Slack Secondary Channel] --> CG
    WA[WhatsApp Secondary Channel] --> CG

    CG --> ID[Identity + Session Mapper]
    ID --> IF[Intent Firewall]
    IF --> POS[Policy OS / Lisa Constitution]

    POS --> BM[BrainMux]
    BM --> P[Planner Brain]
    P --> UPT[Universal Plan Tokenizer]
    UPT --> F[Feasibility Brain]
    F --> R[Ranker Brain]

    R --> TH{Score >= Threshold?}
    TH -- No --> LG[Loop Governor / Deep Thinking Re-loop]
    LG --> P
    TH -- Yes --> CORE[Lisa Core Decision]

    CORE --> AP{Approval Needed?}
    AP -- Yes --> VAL[Telegram Validation Required]
    VAL --> POS
    AP -- No --> EX[ExecutionMux]

    EX --> DS[Chat-Controlled DevShell]
    DS --> SB[Sandbox Workspace]
    SB --> CMD[Sandbox Terminal Runner]
    SB --> DIFF[Patch + Diff Manager]
    SB --> TEST[Tests / Evals Runner]
    SB --> MCP[MCP Test Bench]

    CORE --> RAG[RAG Router]
    RAG --> MEM[MemoryMux]

    CMD --> OBS[ObservationMux]
    DIFF --> OBS
    TEST --> OBS
    MCP --> OBS

    OBS --> LEARN[Learner Brain]
    OBS --> AUDIT[Audit Log]
    LEARN --> NIGHT[Nightly Harness]
    NIGHT --> REPORT[Morning Report]
    REPORT --> TG

    RESEARCH[Research / Cyber-Immune Brain] --> RAG
    RESEARCH --> MCP

    NOTIFY[Telegram Notification Engine] --- CG
    NOTIFY --- BM
    NOTIFY --- DS
    NOTIFY --- OBS
    NOTIFY --- NIGHT
```

---

## Lisa Brain System

Lisa’s planning core starts with Planner, Feasibility, and Ranker.
Lisa’s full governance, learning, safety, and audit architecture has 7 brains.

| Brain | Core Responsibility |
|---|---|
| **1. Planner** | Turns a user goal into a structured, step-by-step implementation plan. |
| **2. Feasibility** | Checks whether the plan is realistic, safe, and executable. |
| **3. Ranker** | Scores the plan and decides whether the planning loop should re-run. |
| **4. Teacher / Learner** | Runs Night School, studies traces, and proposes improvements. |
| **5. Cyber-Immune** | Interacts with the world safely and scans MCPs/packages. |
| **6. Red Team Mirror** | Adversarial safety review and critique of risky plans. |
| **7. Auditor** | Evaluates the learning system, grades brains, and tracks learning curves. |

For detailed internals, see:
- [Chat-Native Architecture](docs/01_chat_native_architecture.md)
- [ReAct Planning Loop](docs/02_react_planning_loop.md)
- [Teacher / Learner Brain](docs/13_teacher_learner_brain.md)
- [Cyber-Immune Brain](docs/14_cyber_immune_brain.md)
- [Auditor / School Inspector Brain](docs/15_auditor_school_inspector_brain.md)


## Mandatory Telegram Transparency

Lisa must notify the user through Telegram for every meaningful update:

- Active brain change.
- Plan creation.
- Plan compression.
- Feasibility result.
- Ranker score.
- Loop re-run.
- Threshold pass/fail.
- DevShell command start/completion/block.
- File change.
- Diff creation.
- Test result.
- MCP scan/test.
- Skill candidate creation.
- Memory promotion request.
- Circuit breaker event.
- Rollback creation.
- Nightly report.

Crucial updates require validation before execution.

> **No silent action. No hidden brain state. No crucial update without Telegram validation.**

---

## Documentation Index

Read these in order:

1. [`docs/00_vision.md`](docs/00_vision.md)
2. [`docs/01_chat_native_architecture.md`](docs/01_chat_native_architecture.md)
3. [`docs/02_react_planning_loop.md`](docs/02_react_planning_loop.md)
4. [`docs/03_universal_plan_tokenizer.md`](docs/03_universal_plan_tokenizer.md)
5. [`docs/04_rag_pipeline.md`](docs/04_rag_pipeline.md)
6. [`docs/05_policy_os.md`](docs/05_policy_os.md)
7. [`docs/06_mqtt_protocol.md`](docs/06_mqtt_protocol.md)
8. [`docs/07_chat_controlled_devshell.md`](docs/07_chat_controlled_devshell.md)
9. [`docs/08_telegram_transparency_layer.md`](docs/08_telegram_transparency_layer.md)
10. [`docs/09_security_model.md`](docs/09_security_model.md)
11. [`docs/10_lightweight_deployment.md`](docs/10_lightweight_deployment.md)
12. [`docs/11_developer_execution_plan.md`](docs/11_developer_execution_plan.md)
13. [`docs/12_roadmap.md`](docs/12_roadmap.md)

---

## Recommended Initial Stack

```txt
Backend: FastAPI
Database: SQLite for dev, Postgres for production
Messaging: Optional MQTT
Chat: Telegram Bot API, Slack App, WhatsApp Cloud API
LLM: Provider-configurable router
RAG: Trust-zoned document pipeline
Sandbox: isolated local workspace first, container/microVM later
```

---

## Non-Negotiable Rules

```txt
No web dashboard.
No unrestricted shell.
No direct host command execution.
No direct production write.
No direct MCP activation.
No direct trusted memory write from brains.
No direct tool execution from brains.
No self-modification of constitution or policy core.
No external write without approval.
No secrets in logs, prompts, MQTT events, traces, chat messages, or memory.
No infinite loops.
No hardcoded model/provider/threshold logic in business logic.
```

---

## Status

Lisa is currently in **architecture and planning documentation phase**.

Next milestone: implement the chat-native FastAPI foundation, Telegram webhook, task runtime, policy loader, and three-brain planning loop.
