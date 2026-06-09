from typing import Dict, Any, List
from app.models.base import JudicialInspectionRequest
from app.config import settings

class SuspicionDetector:
    def __init__(self):
        self.dangerous_commands = [
            "rm -rf /", "rm -rf *", "sudo", "chmod 777", "curl | sh", "wget | sh", "drop table", "delete from"
        ]

    def detect(self, request: JudicialInspectionRequest) -> float:
        score = 0.0

        if request.action_type == "shell_command":
            cmd = request.payload.get("command", "")
            for danger in self.dangerous_commands:
                if danger in cmd:
                    score = max(score, 0.95)

        if request.action_type == "disable_judicial_police":
            score = 1.0

        if request.action_type == "disable_audit_log":
            score = 1.0

        if request.action_type == "disable_sandbox":
            score = 1.0

        if request.action_type == "bypass_approval":
            score = 0.95

        if request.action_type == "tool_installation":
            if request.payload.get("status") != "approved":
                 score = max(score, 0.8)

        return score
