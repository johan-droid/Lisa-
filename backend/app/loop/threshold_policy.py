from typing import Dict, Any
from app.policy_os.policy_loader import PolicyLoader

class ThresholdPolicy:
    def __init__(self):
        self.policy_loader = PolicyLoader()

    def get_min_score(self) -> float:
        policy = self.policy_loader.load_policy("planning_loop")
        return policy.get("min_acceptable_score", 0.7)

    def get_max_iterations(self) -> int:
        policy = self.policy_loader.load_policy("planning_loop")
        return policy.get("max_replan_iterations", 3)
