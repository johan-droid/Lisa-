# Teacher Tool Discovery

The `ToolDiscoveryBrain` (Teacher) explores online registries for open-source tools when Lisa needs capabilities it lacks.

## Lifecycle
Tools discovered by the Teacher are classified as `ToolCandidate`s. They are scanned by the Cyber-Immune `ToolRiskScanner` and placed into the `ToolQuarantine`. They cannot be installed or activated without Principal Approval.
