from app.models.base import PlanPacket, RankerScore
from app.loop.threshold_policy import ThresholdPolicy
from app.brains.planner import PlannerBrain
from app.brains.feasibility import FeasibilityBrain
from app.brains.ranker import RankerBrain
from typing import Dict, Any, Tuple

class LoopGovernor:
    def __init__(self):
        self.threshold_policy = ThresholdPolicy()
        self.planner = PlannerBrain()
        self.feasibility = FeasibilityBrain()
        self.ranker = RankerBrain()

    def run(self, initial_plan: PlanPacket, initial_score: RankerScore) -> Dict[str, Any]:
        min_score = self.threshold_policy.get_min_score()

        loop_count = 0
        current_plan = initial_plan
        current_score = initial_score
        replan_performed = False

        if current_score.overall_score < min_score or current_score.replan_required:
            loop_count += 1
            replan_performed = True
            # deterministic replan
            current_plan = self.planner.create_plan(initial_plan.goal + " (improved)")
            current_feasibility = self.feasibility.evaluate(current_plan)
            current_score = self.ranker.score(current_plan, current_feasibility)

        return {
            "loop_count": loop_count,
            "final_score": current_score.overall_score,
            "replan_performed": replan_performed,
            "final_plan_packet": current_plan
        }
