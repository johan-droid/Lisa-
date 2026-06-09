# Autopilot Mode

Autopilot Mode is a constitutional state triggered exclusively by explicit user commands like "Autopilot mode: <goal>" or "/lisa autopilot <goal>".

## Capabilities
In Autopilot Mode, Lisa utilizes the Brain Swarm orchestrator, consumes larger token budgets via the Token Bank, performs fast model switching, and executes commands iteratively within a Sandboxed Runtime.

## Limitations
Autopilot remains legally bounded by the Autopilot Constitution and the Judicial Police. It cannot merge, deploy, access secrets, change environment variables, or write to databases without explicit Principal approval.

## Simulated vs Real
Currently, the execution sandbox (E2B and CodeSandbox) and FreeLLMAPI token bank are implemented with fallback simulators. Execution happens via the SandboxRuntime, which relies on LocalSandboxSimulator by default unless external providers are enabled via config.
