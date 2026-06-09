from app.models.base import ParsedCommand
from app.policy_os.risk_engine import RiskEngine

class ApprovalEngine:
    def __init__(self, risk_engine: RiskEngine = None):
        self.risk_engine = risk_engine or RiskEngine()

    def check_approval(self, command: ParsedCommand) -> bool:
        risk_level = self.risk_engine.evaluate(command)
        return risk_level == "approval_required"
