from typing import Dict, Any, Optional
from app.sandbox.sandbox_runtime import SandboxRuntime

class WorkspaceRuntime:
    def __init__(self, sandbox: SandboxRuntime):
        self.sandbox = sandbox

    def execute_task(self, task_id: str, command: str) -> Dict[str, Any]:
        # Workspace must never execute directly on host; must use sandbox
        result = self.sandbox.run_command(task_id, command)
        return result
