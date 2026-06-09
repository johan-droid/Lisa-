import yaml
import os
from typing import Dict, Any

class PolicyLoader:
    def __init__(self, policies_dir: str = "backend/app/policies"):
        self.policies_dir = policies_dir
        self.defaults = {
            "thresholds": {
                "ranker_min_score": 0.7
            },
            "blocked_commands": [
                "rm -rf", "curl | sh", "sudo", "chmod 777", "delete database", "drop table", "devshell terminal"
            ]
        }

    def load(self) -> Dict[str, Any]:
        policy_file = os.path.join(self.policies_dir, "main.yaml")
        if os.path.exists(policy_file):
            try:
                with open(policy_file, 'r') as f:
                    data = yaml.safe_load(f)
                    if data:
                        return {**self.defaults, **data}
            except Exception:
                pass
        return self.defaults
