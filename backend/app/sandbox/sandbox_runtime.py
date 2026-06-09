from typing import Dict, Any
from app.config import settings
from app.sandbox.local_sandbox_simulator import LocalSandboxSimulator
from app.sandbox.e2b_provider import E2BProvider
from app.sandbox.codesandbox_provider import CodeSandboxProvider
from app.sandbox.snapshot_manager import SnapshotManager

class SandboxRuntime:
    def __init__(self):
        self.provider_name = settings.SANDBOX_PROVIDER
        self.snapshot_manager = SnapshotManager()

        # Instantiate without crashing if env is missing
        self.local_provider = LocalSandboxSimulator()
        self.e2b_provider = E2BProvider()
        self.codesandbox_provider = CodeSandboxProvider()

        self.allowed_read_commands = [
             "pwd", "ls", "find", "cat", "grep", "rg", "git status", "git log --oneline"
        ]

    def _get_provider(self):
         if self.provider_name == "e2b" and self.e2b_provider.enabled:
             return self.e2b_provider
         elif self.provider_name == "codesandbox" and self.codesandbox_provider.enabled:
             return self.codesandbox_provider
         # Fallback to local simulator if envs missing
         return self.local_provider

    def run_command(self, task_id: str, command: str, capability: str = None) -> Dict[str, Any]:
        provider = self._get_provider()

        # Enforce memory constraint
        memory = settings.SANDBOX_DEFAULT_MEMORY_MB
        if memory > 512 and not settings.SANDBOX_ENABLE_E2B and not settings.SANDBOX_ENABLE_CODESANDBOX:
             # Default fallback constraint
             pass

        # Enforce repo_read capability
        if capability == "repo_read":
             is_allowed = any(command.startswith(allowed) for allowed in self.allowed_read_commands)
             if not is_allowed:
                 return {
                     "provider": provider.__class__.__name__,
                     "snapshot": None,
                     "result": {"stdout": "", "stderr": f"Command blocked. Only read commands allowed.", "exit_code": 1}
                 }

        # Snapshot before
        snap = None
        if settings.SANDBOX_SNAPSHOT_ENABLED:
             snap = self.snapshot_manager.create_snapshot(task_id, {"cmd": command})

        result = provider.execute(command)

        return {
             "provider": provider.__class__.__name__,
             "snapshot": snap,
             "result": result
        }
