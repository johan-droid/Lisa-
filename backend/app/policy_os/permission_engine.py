from app.models.base import ParsedCommand
from typing import Dict, Any

class PermissionEngine:
    def check(self, command: ParsedCommand, risk_level: str) -> Dict[str, Any]:
        if not command.is_valid:
            return {"allowed": False, "reason": command.error_reason, "approval_required": False}

        if risk_level == "execution_blocked":
            return {"allowed": False, "reason": "Destructive execution is blocked in Phase 1", "approval_required": False}

        if risk_level == "approval_required":
             return {"allowed": False, "reason": "Approval required before execution", "approval_required": True}

        if command.command in ["/lisa plan", "/lisa status", "/lisa explain"]:
             return {"allowed": True, "reason": "Planning/Read-only allowed", "approval_required": False}

        return {"allowed": False, "reason": "Command not allowed by default policy", "approval_required": False}
