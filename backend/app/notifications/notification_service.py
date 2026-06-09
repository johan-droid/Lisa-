from typing import Dict, Any, List

class NotificationService:
    def __init__(self, notifiers: List[Any]):
        self.notifiers = notifiers

    def notify(self, channel: str, event_type: str, data: Dict[str, Any]):
        for notifier in self.notifiers:
            if notifier.supports(channel):
                notifier.send(event_type, data)
