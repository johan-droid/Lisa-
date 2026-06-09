from app.policy_os.policy_loader import PolicyLoader

class ThresholdPolicy:
    def __init__(self, policy_loader: PolicyLoader = None):
        self.policy_loader = policy_loader or PolicyLoader()

    def get_min_score(self) -> float:
        policy = self.policy_loader.load()
        return policy.get("thresholds", {}).get("ranker_min_score", 0.7)
