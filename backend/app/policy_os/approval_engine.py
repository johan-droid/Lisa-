from app.models.base import ParsedCommand

class ApprovalEngine:
    def check_approval(self, parsed: ParsedCommand) -> bool:
        if parsed.command == "/lisa run":
            return True
        return False
