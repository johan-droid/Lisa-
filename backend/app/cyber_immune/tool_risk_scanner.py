from app.models.base import ToolCandidate

class ToolRiskScanner:
    def __init__(self):
        self.risky_patterns = ["sudo", "curl | sh", "wget | sh", "chmod 777"]

    def scan(self, candidate: ToolCandidate) -> ToolCandidate:
        flags = []
        score = 1.0

        for cmd in candidate.install_commands:
            for pattern in self.risky_patterns:
                if pattern in cmd:
                    flags.append(f"Risky install command: {pattern}")
                    score -= 0.5

        if candidate.source_type not in ["pypi", "npm", "github"]:
            flags.append(f"Unknown source type: {candidate.source_type}")
            score -= 0.3

        candidate.risk_flags = flags
        candidate.trust_score = max(0.0, score)

        candidate.cyber_immune_report = {
             "scanned": True,
             "flags": flags,
             "score": candidate.trust_score
        }

        return candidate
