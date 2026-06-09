from app.models.base import ParsedCommand
from app.policy_os.policy_loader import PolicyLoader

class RiskEngine:
    def __init__(self, policy_loader: PolicyLoader = None):
        self.policy_loader = policy_loader or PolicyLoader()

    def evaluate(self, command: ParsedCommand) -> str:
        if not command.is_valid:
            return "unknown"

        policy = self.policy_loader.load()
        blocked_terms = policy.get("blocked_commands", [])

        args_lower = command.args.lower()
        for term in blocked_terms:
            if term in args_lower:
                return "execution_blocked"

        if command.command == "/lisa plan":
            return "planning_only"

        if command.command in ["/lisa status", "/lisa explain"]:
            return "read_only"

        return "approval_required"
