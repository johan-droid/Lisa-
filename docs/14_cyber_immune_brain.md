# Cyber-Immune / World-Interaction Brain

Mandatory.

Responsible for interacting with the outside world safely.

## Responsibilities:

```txt
research external tools
inspect packages
scan npm/PyPI packages
scan GitHub repos
scan MCP servers
detect typosquatting
detect malicious install scripts
detect prompt injection
detect poisoned docs
detect unsafe dependencies
write external content only to quarantine
generate trust scores
recommend safe/unsafe decision
notify Telegram before and after every scan
```

The Cyber-Immune Brain must not install packages directly.

It must not activate MCPs directly.

It must not write trusted memory directly.

All package/MCP/tool use must go through:

```txt
Cyber-Immune scan
→ quarantine
→ trust score
→ Policy OS
→ DevShell sandbox test
→ Telegram validation
→ limited activation only if approved
```
