from typing import Dict, Any

class WhatsappNotifier:
    def supports(self, channel: str) -> bool:
        return channel == "whatsapp"

    def send(self, event_type: str, data: Dict[str, Any]):
        print(f"[Simulated Whatsapp] {event_type}: {data}")
