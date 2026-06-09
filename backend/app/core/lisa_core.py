from app.models.base import NormalizedMessage, IdentitySession, LisaPipelineResult
from app.chat.command_parser import CommandParser
from app.policy_os.permission_engine import PermissionEngine
from app.policy_os.risk_engine import RiskEngine
from app.policy_os.approval_engine import ApprovalEngine
from app.brains.planner import PlannerBrain
from app.brains.feasibility import FeasibilityBrain
from app.brains.ranker import RankerBrain
from app.tokenizer.universal_plan_tokenizer import UniversalPlanTokenizer
from app.loop.loop_governor import LoopGovernor
from app.core.audit_log import AuditLogger

class LisaCore:
    def __init__(self):
        self.parser = CommandParser()
        self.permission_engine = PermissionEngine()
        self.risk_engine = RiskEngine()
        self.approval_engine = ApprovalEngine()
        self.planner = PlannerBrain()
        self.feasibility = FeasibilityBrain()
        self.ranker = RankerBrain()
        self.tokenizer = UniversalPlanTokenizer()
        self.loop_governor = LoopGovernor()
        self.audit = AuditLogger()

    def process(self, msg: NormalizedMessage, session: IdentitySession = None) -> LisaPipelineResult:
        self.audit.log("message_normalized", {"message_id": msg.message_id, "session": session.user_id if session else None}, msg.channel)

        parsed = self.parser.parse(msg.text)
        self.audit.log("command_parsed", {"command": parsed.command, "valid": parsed.is_valid}, msg.channel)

        risk_level = self.risk_engine.evaluate(parsed)
        permission = self.permission_engine.check(parsed, risk_level)
        self.audit.log("policy_decision", {"allowed": permission["allowed"], "risk": risk_level}, msg.channel)

        if not permission["allowed"]:
            self.audit.log("command_blocked", {"reason": permission["reason"]}, msg.channel)
            return LisaPipelineResult(
                status="blocked",
                reply=f"Blocked: {permission['reason']}",
                approval_required=permission["approval_required"],
                risk_level=risk_level
            )

        approval_required = self.approval_engine.check_approval(parsed)

        plan = self.planner.create_plan(parsed.args)
        self.audit.log("plan_created", {"task_id": plan.task_id}, msg.channel, task_id=plan.task_id)

        tokenized = self.tokenizer.tokenize(plan)

        feasibility = self.feasibility.evaluate(plan)
        self.audit.log("feasibility_checked", {"feasible": feasibility.feasible}, msg.channel, task_id=plan.task_id)

        score = self.ranker.score(plan, feasibility)
        self.audit.log("ranker_scored", {"score": score.overall_score}, msg.channel, task_id=plan.task_id)

        gov_result = self.loop_governor.run(plan, score)
        final_plan = gov_result["final_plan_packet"]
        final_score = gov_result["final_score"]

        reply = (f"Plan created for: {final_plan.goal}\n"
                 f"Score: {final_score}\n"
                 f"Approval required: {approval_required}\n"
                 f"Steps: {len(final_plan.ordered_steps)}")

        self.audit.log("response_created", {"task_id": final_plan.task_id}, msg.channel, task_id=final_plan.task_id)

        return LisaPipelineResult(
            status="ok",
            reply=reply,
            task_id=final_plan.task_id,
            approval_required=approval_required,
            risk_level=risk_level
        )
