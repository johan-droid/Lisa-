from typing import Dict, Any
from app.config import settings

class E2BProvider:
    def __init__(self):
        self.api_key = settings.E2B_API_KEY
        self.enabled = settings.SANDBOX_ENABLE_E2B

    def execute(self, command: str) -> Dict[str, Any]:
        if not self.enabled:
             return {"stdout": "", "stderr": "E2B disabled", "exit_code": 1}
        return {"stdout": f"Simulated E2B output for: {command}", "stderr": "", "exit_code": 0}
