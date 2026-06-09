#!/bin/bash

# Ensure gh cli is installed and authenticated before running
if ! command -v gh &> /dev/null
then
    echo "gh cli could not be found. Please install it first."
fi

echo "Creating Layer 1 issue..."
gh issue create --title "Layer 1: Backend Foundation" --body "Implement FastAPI foundation, config loader, health route, audit log skeleton, and basic task runtime skeleton.

Acceptance:
- FastAPI app boots
- GET /api/health works
- config loads from env
- health route does not require DB
- tests added"

echo "Creating Layer 2 issue..."
gh issue create --title "Layer 2: Chat-Native Interface Layer" --body "Implement Telegram, Slack, and WhatsApp adapters through one Unified Chat Gateway.

Acceptance:
- Telegram webhook works
- Slack event route works
- WhatsApp verification + webhook works
- all messages normalize to LisaChatCommand
- /lisa help and /lisa plan parse correctly"

echo "Creating Layer 3 issue..."
gh issue create --title "Layer 3: Telegram Transparency Layer" --body "Implement Telegram notification engine and no-silent-action policy.

Acceptance:
- notifications include active brain, phase, action, risk, decision, result, next step
- crucial updates create validation request
- secrets are redacted
- silent action triggers circuit breaker"

echo "Creating Layer 4 issue..."
gh issue create --title "Layer 4: Policy OS + Constitution" --body "Implement policy loader, constitution engine, permission engine, risk engine, approval engine, rollback engine, and circuit breaker.

Acceptance:
- YAML policies load
- P3+ requires approval
- P5 denied by default
- policy decision sends Telegram notification"

echo "Creating Layer 5 issue..."
gh issue create --title "Layer 5: Task Runtime + Audit System" --body "Implement task lifecycle, task events, audit logs, approval objects, and state machine.

Acceptance:
- /lisa plan creates a task
- task state transitions are recorded
- audit logs are created
- Telegram receives task lifecycle updates"

echo "Creating Layer 6 issue..."
gh issue create --title "Layer 6: Three-Brain ReAct Planning Loop" --body "Implement Planner, Feasibility, and Ranker brains with threshold-based reloop.

Acceptance:
- Planner creates structured plan
- Feasibility checks realism/safety
- Ranker scores plan
- low score reloops
- max iterations stop safely
- Telegram shows brain switches"

echo "Creating Layer 7 issue..."
gh issue create --title "Layer 7: Universal Plan Tokenizer" --body "Implement UPT plan packet compression and per-brain context packing.

Acceptance:
- verbose plans compress into plan packets
- goal/steps/risks/assumptions are preserved
- token savings tracked
- PLAN_COMPRESSED Telegram notification sent"

echo "Creating Layer 7.5 issue..."
gh issue create --title "Layer 7.5: Teacher / Learner Brain + Night School" --body "Implement Teacher Brain and Night School learning loop.

Acceptance:
- Teacher reads traces
- mines mistakes
- runs debate
- runs quizzes
- creates improvement candidates
- does not activate improvements directly
- sends morning learning report to Telegram"

echo "Creating Layer 7.75 issue..."
gh issue create --title "Layer 7.75: Auditor / School Inspector Brain + Agent Memo" --body "Implement Auditor Brain, report cards, marksheets, learning curves, Agent Memo, and capability recommendation logic.

Acceptance:
- report cards generated for brains
- marksheet generated for Night School
- learning curves tracked
- Agent Memo updated append-only
- skill replacement history preserved
- capability recommendations require Cyber-Immune and Policy OS
- Telegram audit report sent"

echo "Creating Layer 8 issue..."
gh issue create --title "Layer 8: RAG + Memory Trust Zones" --body "Implement RAG skeleton and MemoryMux trust zones.

Acceptance:
- policy docs can be trusted
- external content enters quarantine
- raw external content cannot enter trusted memory
- retrieval respects allowed brains
- MemoryMux controls promotion"

echo "Creating Layer 8.5 issue..."
gh issue create --title "Layer 8.5: Cyber-Immune / World-Interaction Brain" --body "Implement Cyber-Immune Brain for package/MCP/repo/world interaction safety.

Acceptance:
- package install requests trigger scan
- npm install defaults to ignore scripts
- pip install is sandbox virtualenv only
- trust score generated
- low trust blocked
- risky package requires Telegram validation
- MCPs cannot activate directly
- external content is sanitized and quarantined"

echo "Creating Layer 9 issue..."
gh issue create --title "Layer 9: MQTT Event Bus" --body "Implement optional MQTT event bus.

Acceptance:
- MQTT payloads validate
- MQTT-disabled mode works
- no secrets are published
- task/brain/devshell events supported"

echo "Creating Layer 10 issue..."
gh issue create --title "Layer 10: Chat-Controlled DevShell" --body "Implement sandboxed DevShell controlled only through chat.

Acceptance:
- no web terminal
- no browser editor
- safe commands run in sandbox
- forbidden commands blocked
- .env cannot be read
- constitution cannot be edited directly
- Telegram receives command updates"

echo "Creating Layer 11 issue..."
gh issue create --title "Layer 11: MCP Quarantine + Skill Graph Skeleton" --body "Implement MCP quarantine and Skill Graph skeleton.

Acceptance:
- MCP candidates enter quarantine
- MCP trust score generated
- activation requires validation
- skill candidates cannot activate silently
- skill lifecycle is tracked"

echo "Creating Layer 12 issue..."
gh issue create --title "Layer 12: Nightly Harness" --body "Implement nightly learning and reporting harness.

Acceptance:
- traces reviewed
- mistakes mined
- evals run
- Teacher report included
- Auditor report included
- no skill activates automatically
- Telegram morning report sent"

echo "Creating Layer 13 issue..."
gh issue create --title "Layer 13: Tests + Safety Verification" --body "Implement full test suite for safety and architecture.

Acceptance:
- health tests
- chat normalization tests
- policy tests
- planning loop tests
- UPT tests
- Teacher tests
- Auditor tests
- Cyber-Immune tests
- RAG trust-zone tests
- DevShell safety tests
- MCP activation blocking tests
- Telegram notification tests"

echo "Creating Layer 14 issue..."
gh issue create --title "Layer 14: Developer Docs + Lessons" --body "Create learning modules for each implemented layer.

Acceptance:
- each lesson folder has lesson.md, implementation.md, exercises.md, mistakes.md, quiz.md
- docs remain updated with implementation reality"

echo "All issues created successfully!"
