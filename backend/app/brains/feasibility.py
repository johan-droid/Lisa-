from app.models.base import PlanPacket, FeasibilityReport

class FeasibilityBrain:
    def evaluate(self, plan: PlanPacket) -> FeasibilityReport:
        blockers = []
        if not plan.goal:
            blockers.append("Goal is empty")
        if not plan.ordered_steps:
            blockers.append("Plan has no steps")

        feasible = len(blockers) == 0

        return FeasibilityReport(
            feasible=feasible,
            blockers=blockers,
            warnings=["Requires test coverage"],
            missing_modules=[],
            required_approvals=plan.approval_checkpoints,
            deployment_notes=[],
            safety_notes=[]
        )
