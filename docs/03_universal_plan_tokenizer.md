# Universal Plan Tokenizer

The Universal Plan Tokenizer, or UPT, is Lisa's internal plan compression layer.

It is not a normal language tokenizer. It is a structured context-packing system that reduces verbose inter-brain communication into compact plan packets.

---

## 1. Why UPT Exists

Multi-brain systems can waste tokens quickly.

Without UPT, the same information gets repeated between:

- Planner Brain
- Feasibility Brain
- Ranker Brain
- Learner Brain
- Research Brain
- Memory system

This creates:

- Higher LLM cost.
- Faster rate-limit exhaustion.
- Larger context windows.
- More hallucination surface.
- Slower loops.

UPT fixes this by converting verbose plans into canonical structured packets.

---

## 2. Responsibilities

UPT must:

- Convert verbose plans into compact JSON.
- Deduplicate repeated constraints.
- Replace large context with references.
- Preserve goal, steps, assumptions, risks, and scores.
- Generate per-brain context views.
- Track diffs across iterations.
- Estimate token savings.
- Prevent raw external data from being injected into brain context.

---

## 3. Plan Packet Schema

```json
{
  "plan_packet_id": "pp_001",
  "task_id": "task_001",
  "iteration": 1,
  "goal": "Build Lisa planning core",
  "constraints": [
    "chat-native only",
    "lightweight instance",
    "no destructive execution",
    "Telegram transparency required"
  ],
  "steps": [
    {
      "id": "S1",
      "action": "create_task_runtime",
      "purpose": "store task and lifecycle state",
      "requires": ["database"],
      "risk": "P0",
      "expected_output": "task record"
    }
  ],
  "assumptions": [],
  "risks": [],
  "rag_refs": [],
  "scores": {},
  "diff_from_previous": null,
  "token_estimate": {
    "verbose_tokens": 0,
    "compressed_tokens": 0,
    "saved_tokens": 0
  }
}
```

---

## 4. Per-Brain Views

Each brain receives only what it needs.

### Planner View

- Goal.
- Constraints.
- Previous Ranker feedback.
- Previous failed assumptions.
- Compressed prior plan.

### Feasibility View

- Steps.
- Required tools.
- Required permissions.
- Known constraints.
- Infrastructure limits.
- Risk markers.

### Ranker View

- Goal.
- Compressed plan.
- Feasibility report.
- Risk list.
- Success criteria.
- Grading rubric.

### Learner View

- Final plan.
- All scores.
- Loop history.
- Failure reasons.
- Token usage.

---

## 5. Token Budgeting

UPT must track:

```txt
input_tokens
output_tokens
verbose_tokens
compressed_tokens
saved_tokens
brain_name
iteration
model_tier
```

If token usage is too high:

- Compress plan more aggressively.
- Reduce RAG context.
- Stop re-looping.
- Switch to cheaper model tier.
- Ask user for validation if task is too large.

---

## 6. Required Files

```txt
backend/app/tokenizer/universal_plan_tokenizer.py
backend/app/tokenizer/plan_packet.py
backend/app/tokenizer/context_packer.py
backend/app/tokenizer/plan_diff.py
backend/app/schemas/plan_packet.schema.json
```

---

## 7. Tests

Required tests:

- UPT creates valid plan packet.
- UPT reduces verbose plan size.
- UPT preserves goal, constraints, steps, and risks.
- UPT generates different views for Planner, Feasibility, and Ranker.
- UPT tracks token savings.
- UPT blocks raw external content from direct trusted context.
