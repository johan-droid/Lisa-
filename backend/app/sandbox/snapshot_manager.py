from typing import Dict, Any
import time

class SnapshotManager:
    def create_snapshot(self, task_id: str, context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "snapshot_id": f"snap_{task_id}_{int(time.time())}",
            "task_id": task_id,
            "context": context
        }
