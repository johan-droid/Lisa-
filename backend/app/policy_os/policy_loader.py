import yaml
import os
from typing import Dict, Any

class PolicyLoader:
    def __init__(self, policy_dir: str = "backend/app/policies"):
        self.policy_dir = policy_dir

    def load_constitution(self, mode: str) -> Dict[str, Any]:
        file_path = os.path.join(self.policy_dir, f"{mode}_constitution.yaml")
        if not os.path.exists(file_path):
             return {}
        with open(file_path, "r") as f:
             return yaml.safe_load(f)

    def load_policy(self, name: str) -> Dict[str, Any]:
        file_path = os.path.join(self.policy_dir, f"{name}.yaml")
        if not os.path.exists(file_path):
             return {}
        with open(file_path, "r") as f:
             return yaml.safe_load(f)
