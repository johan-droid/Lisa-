from app.models.base import ParsedCommand
from typing import Dict, Any

class PermissionEngine:
    def check(self, parsed: ParsedCommand, risk_level: str) -> Dict[str, Any]:
        # Backwards compat for old tests
        if risk_level == "execution_blocked":
             return {"allowed": False, "reason": "Destructive execution is blocked in Phase 1", "approval_required": False}

        # Allow explicit autopilot triggers through the permission engine
        # so they can reach the autopilot controller.
        cmd_lower = parsed.command.lower()
        if "autopilot mode:" in cmd_lower or "/lisa autopilot" in cmd_lower or "lisa autopilot" in cmd_lower:
            return {"allowed": True, "reason": "Autopilot trigger allowed"}

        if parsed.command == "/lisa run":
             return {"allowed": False, "reason": "Command not allowed by default policy", "approval_required": True}

        # Default allow other valid commands for planning
        return {"allowed": True, "reason": "Allowed by default policy", "approval_required": False}
