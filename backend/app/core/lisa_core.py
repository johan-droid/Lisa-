from typing import Optional
import uuid
from app.models.base import NormalizedMessage, IdentitySession, LisaPipelineResult
from app.chat.command_parser import CommandParser
from app.policy_os.permission_engine import PermissionEngine
from app.policy_os.risk_engine import RiskEngine
from app.policy_os.approval_engine import ApprovalEngine
from app.policy_os.policy_loader import PolicyLoader
from app.brains.planner import PlannerBrain
from app.brains.feasibility import FeasibilityBrain
from app.brains.ranker import RankerBrain
from app.tokenizer.universal_plan_tokenizer import UniversalPlanTokenizer
from app.loop.loop_governor import LoopGovernor
from app.core.audit_log import AuditLogger
from app.judicial.judicial_brain import JudicialBrain
from app.autopilot.autopilot_detector import AutopilotDetector
from app.autopilot.autopilot_controller import AutopilotController
from app.teacher.tool_discovery_brain import ToolDiscoveryBrain
from app.cyber_immune.tool_risk_scanner import ToolRiskScanner
from app.tools.tool_quarantine import ToolQuarantine
from app.principal.principal_approval_engine import PrincipalApprovalEngine

class JobRouter:
    def classify(self, text: str) -> str:
        text_lower = text.lower()
        if "find" in text_lower and "tool" in text_lower:
             return "tool_adoption_job"
        if "research" in text_lower:
             return "research_job"
        if "implement" in text_lower or "refactor" in text_lower:
             return "implementation_job"
        if "plan" in text_lower:
             return "planning_job"
        return "unknown_job"

class LisaCore:
    def __init__(self):
        self.parser = CommandParser()
        self.permission_engine = PermissionEngine()
        self.risk_engine = RiskEngine()
        self.approval_engine = ApprovalEngine()
        self.policy_loader = PolicyLoader()

        self.planner = PlannerBrain()
        self.feasibility = FeasibilityBrain()
        self.ranker = RankerBrain()
        self.tokenizer = UniversalPlanTokenizer()
        self.loop_governor = LoopGovernor()
        self.audit = AuditLogger()

        # New Brains & Engines
        self.judicial_brain = JudicialBrain()
        self.autopilot_detector = AutopilotDetector()
        self.autopilot_controller = AutopilotController()
        self.teacher_brain = ToolDiscoveryBrain()
        self.cyber_immune = ToolRiskScanner()
        self.tool_quarantine = ToolQuarantine()
        self.principal = PrincipalApprovalEngine()
        self.job_router = JobRouter()

    def process(self, msg: NormalizedMessage, session: IdentitySession = None) -> LisaPipelineResult:
        user_id = session.user_id if session else msg.external_user_id
        self.audit.log("message_normalized", {"message_id": msg.message_id, "session": user_id}, msg.channel)

        parsed = self.parser.parse(msg.text)
        self.audit.log("command_parsed", {"command": parsed.command, "valid": parsed.is_valid}, msg.channel)

        # Handle specific commands
        if parsed.command == "/lisa approve":
            approval_id = parsed.args
            try:
                dec = self.principal.record_decision(approval_id, "approved", "User command", user_id=user_id)
                if dec:
                     return LisaPipelineResult(status="ok", reply=f"Approval {approval_id} processed: approved.", task_id=None)
                return LisaPipelineResult(status="error", reply="Approval request not found.", task_id=None)
            except ValueError as e:
                return LisaPipelineResult(status="error", reply=str(e), task_id=None)

        if parsed.command == "/lisa deny":
            approval_id = parsed.args
            try:
                dec = self.principal.record_decision(approval_id, "denied", "User command", user_id=user_id)
                if dec:
                     return LisaPipelineResult(status="ok", reply=f"Approval {approval_id} processed: denied.", task_id=None)
                return LisaPipelineResult(status="error", reply="Approval request not found.", task_id=None)
            except ValueError as e:
                return LisaPipelineResult(status="error", reply=str(e), task_id=None)

        if parsed.command == "/lisa status":
            task_id = parsed.args
            return LisaPipelineResult(status="ok", reply=f"Status for task {task_id}: Processing", task_id=task_id)

        if parsed.command == "/lisa explain":
            task_id = parsed.args
            return LisaPipelineResult(status="ok", reply=f"Explanation for task {task_id}: Pending architecture details.", task_id=task_id)

        # 1. Classify Job & Mode
        job_type = self.job_router.classify(msg.text)
        mode = self.autopilot_detector.get_mode(msg.text)

        self.audit.log(f"{mode}_constitution_applied", {"job_type": job_type, "mode": mode}, msg.channel)

        # Load Constitution
        constitution = self.policy_loader.load_constitution(mode)
        self.audit.log("constitution_loaded", {"mode": mode}, msg.channel)

        # Basic permission/risk
        risk_level = self.risk_engine.evaluate(parsed)
        permission = self.permission_engine.check(parsed, risk_level)

        if not permission["allowed"]:
            self.audit.log("command_blocked", {"reason": permission["reason"]}, msg.channel)
            return LisaPipelineResult(
                status="blocked",
                reply=f"Blocked: {permission['reason']}",
                approval_required=permission["approval_required"],
                risk_level=risk_level
            )

        # 2. Planning Phase
        plan = self.planner.create_plan(parsed.args)
        self.audit.log("plan_created", {"task_id": plan.task_id, "mode": mode}, msg.channel, task_id=plan.task_id)

        # 3. Tool Discovery if needed
        if job_type in ["tool_adoption_job", "research_job"]:
            candidates = self.teacher_brain.research(parsed.args)
            for c in candidates:
                self.audit.log("judicial_inspection_requested", {"action": "tool_adoption", "candidate": c.name}, msg.channel, task_id=plan.task_id)
                verdict = self.judicial_brain.inspect_tool_candidate(plan.task_id, c.model_dump())
                self.audit.log("judicial_verdict_created", {"verdict": verdict.verdict_type}, msg.channel, task_id=plan.task_id)

                scanned = self.cyber_immune.scan(c)
                self.tool_quarantine.add(scanned)

                # Request Principal Approval for promotion
                self.audit.log("principal_escalation_requested", {"candidate": c.name}, msg.channel, task_id=plan.task_id)
                self.principal.create_request(
                     task_id=plan.task_id,
                     requested_by="teacher",
                     action_type="tool_promotion",
                     reason=f"Need to adopt {c.name}",
                     risk_level="medium",
                     evidence=scanned.cyber_immune_report,
                     user_id=user_id
                )

        # 4. Execution Phase
        reply = ""
        if mode in ["autopilot", "spike"]:
             self.audit.log("judicial_police_activated", {"mode": mode}, msg.channel, task_id=plan.task_id)
             self.audit.log("judicial_inspection_requested", {"action": "autopilot_activation"}, msg.channel, task_id=plan.task_id)

             auto_result = self.autopilot_controller.start_task(plan, mode)

             if auto_result["status"] == "blocked":
                  self.audit.log("action_blocked_by_judicial_police", {"reason": auto_result["reason"]}, msg.channel, task_id=plan.task_id)
                  self.audit.log("loop_stopped_by_judicial_police", {"reason": auto_result["reason"]}, msg.channel, task_id=plan.task_id)
                  reply = f"[Judicial Block] {auto_result['reason']}"
                  return LisaPipelineResult(status="blocked", reply=reply, task_id=plan.task_id)

             if auto_result["status"] == "requires_approval":
                  self.audit.log("approval_required_by_judicial_police", {"reason": auto_result["reason"]}, msg.channel, task_id=plan.task_id)
                  self.audit.log("loop_paused_by_judicial_police", {"reason": auto_result["reason"]}, msg.channel, task_id=plan.task_id)
                  reply = f"[Judicial Pause] Requires Approval: {auto_result['reason']}"
                  return LisaPipelineResult(status="paused", reply=reply, task_id=plan.task_id, approval_required=True)

             reply = f"[{mode.capitalize()} Mode Completed]\nSteps: {auto_result.get('completed_steps')}\nJudicial Verdict: Allowed"

        else:
             # Normal mode flow
             tokenized = self.tokenizer.tokenize(plan)
             feasibility = self.feasibility.evaluate(plan)
             score = self.ranker.score(plan, feasibility)
             gov_result = self.loop_governor.run(plan, score)

             final_plan = gov_result["final_plan_packet"]
             approval_required = self.approval_engine.check_approval(parsed)

             reply = (f"Plan created for: {final_plan.goal}\n"
                      f"Job: {job_type}\n"
                      f"Approval required: {approval_required}\n"
                      f"Steps: {len(final_plan.ordered_steps)}")

        # Step 5 enhancements added directly to core process return to ensure it catches all requests
        reply += f"\n\n--- Metadata ---\nMode: {mode}\nSandbox Provider: Simulated LocalSandboxSimulator\nModel Routing: Simulated LocalFreeLLMAPISimulator\nApproval State: {'Pending' if hasattr(self, 'approval_required') and getattr(self, 'approval_required') else 'None'}"

        self.audit.log("response_created", {"task_id": plan.task_id}, msg.channel, task_id=plan.task_id)

        return LisaPipelineResult(
            status="ok",
            reply=reply,
            task_id=plan.task_id,
            approval_required=False,
            risk_level=risk_level
        )
