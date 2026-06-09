from typing import Dict, Any, List
from app.models.base import JudicialInspectionRequest, ConstitutionalVerdict, ConstitutionViolation
from app.judicial.suspicion_detector import SuspicionDetector
from app.judicial.constitutional_verdict import create_verdict
import time
import uuid

class JudicialBrain:
    def __init__(self):
        self.suspicion_detector = SuspicionDetector()
        self.always_blocked = [
            "disable_judicial_police",
            "disable_audit_log",
            "disable_sandbox",
            "bypass_approval",
            "modify_constitution_to_reduce_safety",
            "credential_exfiltration"
        ]
        self.approval_required_actions = [
            "direct_push_to_main",
            "merge_to_main",
            "production_deployment",
            "secret_access",
            "env_var_changes",
            "database_writes",
            "package_installation",
            "trusted_tool_activation",
            "mcp_activation",
            "external_messages_outside_channel"
        ]

    def select_mode(self, command: str) -> str:
        command_lower = command.lower()
        if "spike mode:" in command_lower or command_lower.startswith("/lisa spike"):
            return "spike"
        elif "autopilot mode:" in command_lower or command_lower.startswith("/lisa autopilot") or command_lower.startswith("lisa autopilot"):
            return "autopilot"
        return "normal"

    def inspect(self, request: JudicialInspectionRequest) -> ConstitutionalVerdict:
        suspicion_score = self.suspicion_detector.detect(request)

        # Check always blocked
        if request.action_type in self.always_blocked:
            return create_verdict(
                request_id=request.request_id,
                mode=request.mode,
                verdict_type="block_action",
                allowed=False,
                approval_required=False,
                should_pause_loop=False,
                should_stop_loop=True,
                suspicion_score=suspicion_score,
                risk_level="high",
                reason=f"Action {request.action_type} is always blocked by Judicial Police.",
                violated_rules=["always_blocked_action"]
            )

        if suspicion_score >= 0.95:
             return create_verdict(
                request_id=request.request_id,
                mode=request.mode,
                verdict_type="block_action",
                allowed=False,
                approval_required=False,
                should_pause_loop=False,
                should_stop_loop=True,
                suspicion_score=suspicion_score,
                risk_level="high",
                reason=f"High suspicion score detected for {request.action_type}",
                violated_rules=["high_suspicion_score"]
            )

        # Check approval required
        if request.action_type in self.approval_required_actions:
             if request.payload.get("status") != "approved":
                 return create_verdict(
                    request_id=request.request_id,
                    mode=request.mode,
                    verdict_type="require_approval",
                    allowed=False,
                    approval_required=True,
                    should_pause_loop=True,
                    should_stop_loop=False,
                    suspicion_score=suspicion_score,
                    risk_level="medium",
                    reason=f"Action {request.action_type} requires Principal approval.",
                    required_action="request_principal_approval"
                )

        # Mode specific checks
        if request.mode == "normal":
             if request.action_type in ["autonomous_execution", "aggressive_model_routing", "trusted_tool_adoption"]:
                 return create_verdict(
                    request_id=request.request_id,
                    mode=request.mode,
                    verdict_type="block_action",
                    allowed=False,
                    approval_required=False,
                    should_pause_loop=False,
                    should_stop_loop=True,
                    suspicion_score=suspicion_score,
                    risk_level="medium",
                    reason=f"Action {request.action_type} is not allowed in normal mode.",
                    violated_rules=["normal_mode_constraint"]
                )

        if request.mode == "spike":
             if request.action_type in ["irreversible_change", "merge", "deploy"]:
                 return create_verdict(
                    request_id=request.request_id,
                    mode=request.mode,
                    verdict_type="block_action",
                    allowed=False,
                    approval_required=False,
                    should_pause_loop=False,
                    should_stop_loop=True,
                    suspicion_score=suspicion_score,
                    risk_level="medium",
                    reason=f"Action {request.action_type} is not allowed in spike mode.",
                    violated_rules=["spike_mode_constraint"]
                )

        # Default allow
        return create_verdict(
            request_id=request.request_id,
            mode=request.mode,
            verdict_type="allow",
            allowed=True,
            approval_required=False,
            should_pause_loop=False,
            should_stop_loop=False,
            suspicion_score=suspicion_score,
            risk_level="low",
            reason="Action is constitutional."
        )

    # Convenience wrappers for specific lifecycle hooks
    def inspect_autopilot_activation(self, task_id: str) -> ConstitutionalVerdict:
        req = JudicialInspectionRequest(
            request_id=str(uuid.uuid4()), task_id=task_id, mode="autopilot",
            actor_brain="user", action_type="autopilot_activation",
            action_summary="Activating autopilot", risk_level="low", created_at=time.time()
        )
        return self.inspect(req)

    def inspect_tool_candidate(self, task_id: str, candidate_dict: Dict) -> ConstitutionalVerdict:
        req = JudicialInspectionRequest(
            request_id=str(uuid.uuid4()), task_id=task_id, mode="autopilot",
            actor_brain="teacher", action_type="tool_adoption",
            action_summary="Proposing tool candidate", payload=candidate_dict,
            risk_level="medium", created_at=time.time()
        )
        return self.inspect(req)

    def inspect_sandbox_command(self, task_id: str, command: str) -> ConstitutionalVerdict:
         req = JudicialInspectionRequest(
            request_id=str(uuid.uuid4()), task_id=task_id, mode="autopilot",
            actor_brain="sandbox", action_type="shell_command",
            action_summary=f"Running command: {command}", payload={"command": command},
            risk_level="high", created_at=time.time()
        )
         return self.inspect(req)

    def inspect_token_reservation(self, task_id: str, amount: int) -> ConstitutionalVerdict:
         req = JudicialInspectionRequest(
            request_id=str(uuid.uuid4()), task_id=task_id, mode="autopilot",
            actor_brain="model_router", action_type="token_reservation",
            action_summary=f"Reserving {amount} tokens", payload={"amount": amount},
            risk_level="low", created_at=time.time()
        )
         return self.inspect(req)
