from typing import Dict, Any

class SlackNotifier:
    def supports(self, channel: str) -> bool:
        return channel == "slack"

    def send(self, event_type: str, data: Dict[str, Any]):
        print(f"[Simulated Slack] {event_type}: {data}")
