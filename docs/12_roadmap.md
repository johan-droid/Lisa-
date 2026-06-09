# Lisa Roadmap

Lisa must be built in safe capability layers.

Do not give Lisa broad real-world power before the Policy OS, notification system, planning loop, and sandbox controls are stable.

---

## Phase 0 — Documentation and Architecture

Status: current phase.

Deliverables:

- README.
- Architecture docs.
- Visual Mermaid diagrams.
- Developer execution plan.
- Security model.
- Telegram transparency law.

---

## Phase 1 — Chat-Native Foundation

Build:

- FastAPI app.
- Telegram webhook.
- Slack adapter.
- WhatsApp adapter.
- Unified Chat Gateway.
- Message normalizer.
- Command parser.
- Identity/session mapper.

Goal:

```txt
User can send /lisa help and /lisa plan through Telegram.
```

---

## Phase 2 — Policy OS + Notifications

Build:

- Constitution engine.
- Permission engine.
- Risk engine.
- Approval engine.
- Telegram Notification Engine.
- Audit log.

Goal:

```txt
Every meaningful task update is reported to Telegram.
Crucial actions create validation requests.
```

---

## Phase 3 — Three-Brain ReAct Loop

Build:

- Planner Brain.
- Feasibility Brain.
- Ranker Brain.
- Loop Governor.
- Threshold policy.

Goal:

```txt
Lisa can plan, check, rank, and reloop until a quality threshold passes.
```

---

## Phase 4 — Universal Plan Tokenizer

Build:

- Plan packet schema.
- Plan compressor.
- Context packer.
- Plan diff.
- Token budgeter.

Goal:

```txt
Lisa reduces inter-brain token usage and avoids rate-limit pressure.
```

---

## Phase 5 — RAG Skeleton

Build:

- Policy RAG.
- Trace RAG.
- Skill RAG.
- Research RAG.
- MCP connector RAG.
- Trust-zone retrieval.

Goal:

```txt
Lisa retrieves the right context without trusting raw external data.
```

---

## Phase 6 — Chat-Controlled DevShell

Build:

- Sandbox workspace manager.
- Chat command terminal gateway.
- Command risk classifier.
- Diff manager.
- Eval runner.
- Package runner.

Goal:

```txt
Lisa can safely run tests and propose patches inside sandbox through chat.
```

---

## Phase 7 — Skill Graph

Build:

- Candidate skills.
- Skill manifests.
- Skill evals.
- Skill promotion rules.
- Skill retirement.

Goal:

```txt
Lisa can propose improvements without activating them silently.
```

---

## Phase 8 — MCP Quarantine

Build:

- MCP discovery.
- Manifest scanner.
- Tool poisoning scanner.
- Dependency scanner.
- Sandbox test bench.
- Trust score.

Goal:

```txt
Lisa can discover MCPs but not activate unsafe connectors.
```

---

## Phase 9 — Nightly Harness

Build:

- Mistake miner.
- Self-score generator.
- Skill synthesizer.
- Morning report.

Goal:

```txt
Lisa reviews each day and sends a morning learning summary.
```

---

## Phase 10 — Controlled External Connectors

Only after prior phases are tested.

Possible connectors:

- GitHub read-only.
- GitHub PR proposal.
- Gmail draft-only.
- Calendar draft-only.
- Slack team workflows.
- Google Drive read-only.

All external writes require validation.

---

## Final Direction

Lisa should become more powerful through:

```txt
better planning
better feasibility checks
better ranking
better compression
better RAG
better memory
better tests
better sandboxing
better Telegram transparency
```

Not through unrestricted tool power.
