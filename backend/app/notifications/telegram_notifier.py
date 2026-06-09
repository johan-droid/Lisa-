from typing import Dict, Any
import os

class TelegramNotifier:
    def supports(self, channel: str) -> bool:
        return channel == "telegram"

    def send(self, event_type: str, data: Dict[str, Any]):
        token = os.environ.get("TELEGRAM_BOT_TOKEN")
        if not token:
             # Simulated notification result
             print(f"[Simulated Telegram] {event_type}: {data}")
             return
        # Real notification logic here
        pass
