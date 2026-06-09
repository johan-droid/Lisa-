from typing import Dict, Any

class LocalSandboxSimulator:
    def execute(self, command: str) -> Dict[str, Any]:
        return {"stdout": f"Simulated local output for: {command}", "stderr": "", "exit_code": 0}
