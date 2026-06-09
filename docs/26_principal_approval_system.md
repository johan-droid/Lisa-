# Principal Approval System

The `PrincipalApprovalEngine` handles high-risk or evolutionary actions proposed by brains.

## Actions Requiring Approval
- Tool promotion from Quarantine to Trusted Registry.
- Package installation.
- Deployments, Merges to Main, and Secret Access.

When an action requires approval, the loop pauses until explicit human/principal confirmation is obtained.
