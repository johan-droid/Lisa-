# Model Routing & Token Bank

To avoid rigid bottlenecks, Autopilot and Spike modes utilize a dynamic Token Bank Broker and Model Router.

## Token Bank
The `TokenBankBroker` manages task-level token budgets, simulating usage accounting via `UsageLedger`.

## Model Routing
The `ModelRouter` monitors LLM health and quickly falls back across models (e.g., GPT-4o-mini to Claude-3-Haiku) using the `FallbackEngine` to prevent failures due to rate limits or API errors. Model switches are inspected by the Judicial Police.
