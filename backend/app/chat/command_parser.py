from app.models.base import ParsedCommand
import re

class CommandParser:
    def parse(self, text: str) -> ParsedCommand:
        text = text.strip()

        # Natural language aliases
        nl_plan = re.match(r'(?i)lisa plan this:\s*(.*)', text)
        if nl_plan:
            return ParsedCommand(command="/lisa plan", args=nl_plan.group(1).strip())

        nl_approve = re.match(r'(?i)approve\s+(\S+)', text)
        if nl_approve:
            return ParsedCommand(command="/lisa approve", args=nl_approve.group(1))

        nl_deny = re.match(r'(?i)deny\s+(\S+)', text)
        if nl_deny:
            return ParsedCommand(command="/lisa deny", args=nl_deny.group(1))

        nl_status = re.match(r'(?i)show status\s+(\S+)', text)
        if nl_status:
            return ParsedCommand(command="/lisa status", args=nl_status.group(1))

        # Standard commands
        parts = text.split(" ", 2)
        if len(parts) >= 2 and parts[0].lower() == "/lisa":
            cmd = f"{parts[0].lower()} {parts[1].lower()}"
            args = parts[2] if len(parts) > 2 else ""

            # Allow /lisa run for the risk engine to catch it as blocked
            if parts[1].lower() == "run":
                return ParsedCommand(command="/lisa run", args=args)

            valid_commands = ["/lisa plan", "/lisa status", "/lisa approve", "/lisa deny", "/lisa explain"]

            if cmd in valid_commands:
                return ParsedCommand(command=cmd, args=args)

        return ParsedCommand(
            command="unknown",
            args="",
            is_valid=False,
            error_reason="Invalid or unknown command"
        )
