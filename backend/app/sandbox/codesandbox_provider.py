from typing import Dict, Any
from app.config import settings

class CodeSandboxProvider:
    def __init__(self):
        self.api_key = settings.CODESANDBOX_API_KEY
        self.enabled = settings.SANDBOX_ENABLE_CODESANDBOX

    def execute(self, command: str) -> Dict[str, Any]:
        if not self.enabled:
             return {"stdout": "", "stderr": "CodeSandbox disabled", "exit_code": 1}
        return {"stdout": f"Simulated CodeSandbox output for: {command}", "stderr": "", "exit_code": 0}
