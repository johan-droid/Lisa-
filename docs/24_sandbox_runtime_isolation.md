# Sandbox Runtime Isolation

Lisa never runs code directly on the host machine. The `WorkspaceRuntime` routes all executions through the `SandboxRuntime`.

## Providers
- LocalSandboxSimulator (Default/Fallback)
- E2BProvider
- CodeSandboxProvider

All commands are intercepted and inspected by the Judicial Police before and after execution.
