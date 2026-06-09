from typing import List, Dict, Any, Optional
import time
import uuid
from app.models.base import AuditEvent

class AuditLogger:
    def __init__(self):
        self._logs: List[AuditEvent] = []

    def log(self, stage: str, metadata: Dict[str, Any], channel: str = "system", task_id: Optional[str] = None) -> AuditEvent:
        event = AuditEvent(
            event_id=str(uuid.uuid4()),
            task_id=task_id,
            channel=channel,
            stage=stage,
            summary=f"Event at stage: {stage}",
            timestamp=time.time(),
            metadata=metadata
        )
        self._logs.append(event)
        return event

    def get_logs(self) -> List[AuditEvent]:
        return self._logs

    def filter_by_stage(self, stage: str) -> List[AuditEvent]:
        return [log for log in self._logs if log.stage == stage]
